import heat as ht
import torch
from heat.core.dndarray import DNDarray
from warnings import warn


from typing import Union, Tuple, TypeVar

self = TypeVar("self")

import numpy as np
# from ..core import BaseEstimator  # Assuming BaseEstimator and ClusteringMixin are in a parent or sibling directory in a library structure.
# from ..utils import ClusteringMixin
from typing import Union, List, Tuple, Dict # Import necessary type hints

import itertools # For generating combinations (potentially)

class Dendrogram(): # Removed inheritance from BaseEstimator and ClusteringMixin for simplicity in standalone context, can be added back if needed

    def __init__(
        self,
        connectivity: int = 4, # Default connectivity as 4 (2D) or 6 (3D)
        dmax: int = 3, # Spatial box size parameter
        vmax: int = 7, # Velocity/Channel box size parameter (for 3D)
        rms_noise: float = 0.3, # RMS noise level
        ppb: float = 1.3, # Pixels per beam
        min_value: Union[float, None] = None, # Minimum value threshold
        enforce_binary_mergers: bool = True, # Enforce binary mergers (basic check, refinement not fully implemented)
    ):
        """
        Initializes the Dendrogram object with parameters for dendrogram construction.

        Args:
            connectivity (int): Connectivity type (4, 8 in 2D; 6, 18, 26 in 3D).
            dmax (int): Spatial box size parameter for local maxima refinement.
            vmax (int): Velocity/Channel box size parameter for local maxima refinement (3D).
            rms_noise (float): Estimated RMS noise level.
            ppb (float): Pixels per beam, for minimum pixel volume criterion.
            min_value (float, None): Intensity value below which to ignore (noise threshold).
            enforce_binary_mergers (bool): Whether to perform basic check for binary mergers.
        """
        self.connectivity = connectivity
        self.dmax = dmax
        self.vmax = vmax
        self.rms_noise = rms_noise
        self.ppb = ppb
        self.min_value = min_value
        self.enforce_binary_mergers = enforce_binary_mergers
        self.name = "Vectorized Dendrogram" # Name to distinguish implementation


    def compute(self, image: torch.Tensor, contour_levels: Union[List[float], np.ndarray]) -> Tuple[Dict, List, torch.Tensor]: # Specify return type
        """
        Computes the dendrogram for a given intensity image and contour levels.

        Args:
            image (torch.Tensor): N-dimensional intensity image.
            contour_levels (list or np.ndarray): List of contour levels (descending order).

        Returns:
            tuple: (dendrogram, merge_history, local_maxima_mask).
                dendrogram (dict): Dendrogram information (merges at each level).
                merge_history (list): List of all merge events.
                local_maxima_mask (torch.Tensor): Boolean mask of decimated local maxima.
        """
        dendrogram_info, merge_history_info, local_maxima_mask_info = self._build_dendrogram_refined_maxima_internal(image, contour_levels) # Call internal method
        return dendrogram_info, merge_history_info, local_maxima_mask_info


    def _build_dendrogram_refined_maxima_internal(self, image, contour_levels): # Renamed and made internal
        """
        Internal method to construct a dendrogram with refined local maxima.
        """
        dendrogram = {}
        previous_regions_mask = None
        merge_history = []

        tmax_factor = 2.0 # Based on astrodendro example: min_delta=2*sigma
        nmin = int(3 * self.ppb) # Based on astrodendro example: min_npix=3*ppb

        # **Image Pre-processing: Apply min_value threshold**
        if self.min_value is not None:
            image_masked = image.clone() #clone to avoid in-place modification
            image_masked[image_masked < self.min_value] = torch.nan # Set values below min_value to NaN
        else:
            image_masked = image # If min_value is None, use original image


        # Use refined local maxima identification - Handles NaNs, now on masked image
        local_maxima_mask = self._identify_local_maxima_refined( # Call internal method
            image_masked, contour_levels, self.dmax, self.vmax, tmax_factor, nmin, self.connectivity, self.rms_noise
        )

        # Original dendrogram building logic (modified to potentially use local_maxima_mask if needed) - operates on masked image
        for level in contour_levels:
            binary_mask = self._contour_image_internal(image_masked, level) # contour_image handles NaNs, now on masked image # Call internal method
            current_regions_mask, num_regions = self._identify_regions_internal(binary_mask, self.connectivity) # identify_regions (BFS) handles NaNs, on masked image # Call internal method

            if previous_regions_mask is not None:
                merges = self._detect_merges_internal(previous_regions_mask, current_regions_mask) # detect_merges handles NaNs in region masks # Call internal method
                if merges:
                    print(f"Merges detected at contour level: {level}, Merged regions (previous level IDs): {merges}")
                    dendrogram[level] = merges
                    merge_history.extend([(level, merge) for merge in merges])

                    if self.enforce_binary_mergers: # Basic check - not full refinement
                        for merge_group in merges:
                            if len(merge_group) > 2:
                                print(f"Warning: Non-binary merge detected at level {level} involving regions {merge_group}. Binary merger enforcement is not fully implemented; level refinement is needed.")


            previous_regions_mask = current_regions_mask

        return dendrogram, merge_history, local_maxima_mask # Return also the local maxima mask if needed later


    def _identify_local_maxima_refined(self, image, contour_levels, dmax, vmax, tmax_factor, nmin, connectivity, rms_noise): # Made internal
        """
        Internal method - Identifies local maxima with noise suppression using box filter and decimation.
        """
        # 1. Identify Candidate Local Maxima (Box-based) - Handles NaNs
        candidate_maxima_mask = self._identify_candidate_local_maxima_box_internal(image, dmax, vmax) # Call internal method
        candidate_maxima_coords_list = []
        for coords_index in np.ndindex(image.shape):
            if candidate_maxima_mask[coords_index]:
                candidate_maxima_coords_list.append(coords_index)

        print(f"Number of candidate local maxima (before decimation): {len(candidate_maxima_coords_list)}")

        # 2. Decimate Local Maxima based on noise criteria - Handles NaNs in merge level and volume calculation
        device = image.device # Get device of the image tensor and pass it to decimate_local_maxima
        decimated_maxima_coords_list = self._decimate_local_maxima_internal( # Call internal method
            image, candidate_maxima_coords_list, contour_levels, dmax, vmax, tmax_factor, nmin, connectivity, rms_noise
        )

        print(f"Number of decimated local maxima (after noise suppression): {len(decimated_maxima_coords_list)}")

        # Create a boolean mask for the decimated maxima
        decimated_maxima_mask = torch.zeros_like(image, dtype=torch.bool, device=image.device) # Ensure mask is on same device as image
        for coords in decimated_maxima_coords_list:
            decimated_maxima_mask[coords] = True

        return decimated_maxima_mask


    def _decimate_local_maxima_internal(self, image, candidate_maxima_coords_list, contour_levels, dmax, vmax, tmax_factor, nmin, connectivity, rms_noise): # Made internal
        """
        Vectorized Internal method - Decimates candidate local maxima based on noise suppression criteria.
        --- VECTORIZED VERSION ---
        """
        tmax = tmax_factor * rms_noise # Tmax threshold based on noise level
        decimated_maxima_coords = list(candidate_maxima_coords_list) # Start with all candidates - list of tuples

        if not decimated_maxima_coords or len(decimated_maxima_coords) < 2: # Need at least 2 maxima to compare
            return decimated_maxima_coords


        maxima_coords_tensor = torch.tensor(decimated_maxima_coords, dtype=torch.long, device=image.device) # Convert maxima coords to tensor [N_maxima, ndim]
        num_maxima = maxima_coords_tensor.shape[0]

        # 1. Generate all pairs of maxima indices
        maxima_indices = torch.arange(num_maxima) # [0, 1, 2, ..., N_maxima-1]
        pairs_indices = torch.combinations(maxima_indices, r=2) # Get all unique pairs of indices [N_pairs, 2]

        num_pairs = pairs_indices.shape[0]
        if num_pairs == 0: # No pairs to compare
            return decimated_maxima_coords


        maxima1_indices = pairs_indices[:, 0] # Indices of the first maximum in each pair [N_pairs]
        maxima2_indices = pairs_indices[:, 1] # Indices of the second maximum in each pair [N_pairs]


        current_maxima_coords_tensor = maxima_coords_tensor # Working copy - will be filtered

        maxima1_coords = current_maxima_coords_tensor[maxima1_indices] # Coordinates of the first maxima in each pair [N_pairs, ndim]
        maxima2_coords = current_maxima_coords_tensor[maxima2_indices] # Coordinates of the second maxima in each pair [N_pairs, ndim]


        # Initialize masks to keep track of maxima to remove (initially none to remove)
        remove_maxima_mask = torch.zeros(num_maxima, dtype=torch.bool, device=image.device) # [N_maxima] - boolean mask to mark maxima for removal



        for level in contour_levels: # Iterate through contour levels (descending)

            # --- Vectorized Merge Check and Volume Calculation ---
            merge_info_list = self._calculate_merge_level_and_volume_vectorized_internal(image, maxima1_coords, maxima2_coords, level, connectivity, nmin) # Vectorized call

            merge_levels_tensor, vol1_tensor, vol2_tensor, merged_mask_level = merge_info_list # [N_pairs], [N_pairs], [N_pairs], [N_pairs] (bool) - for the *current level*


            # --- Apply Noise Criteria (Vectorized) - only to pairs that *did* merge at this level ---
            merged_pairs_indices_level = pairs_indices[merged_mask_level] # Indices of pairs that merged at *this level* [N_merged_pairs_level, 2]
            if merged_pairs_indices_level.numel() == 0: # No merges at this level
                continue # Go to next contour level


            merged_maxima1_indices_level = merged_pairs_indices_level[:, 0] # Indices of max1 for merged pairs at this level [N_merged_pairs_level]
            merged_maxima2_indices_level = merged_pairs_indices_level[:, 1] # Indices of max2 for merged pairs at this level [N_merged_pairs_level]


            merged_vol1_level = vol1_tensor[merged_mask_level] # Volumes for merged pairs [N_merged_pairs_level]
            merged_vol2_level = vol2_tensor[merged_mask_level] # Volumes for merged pairs [N_merged_pairs_level]
            merged_level_proxy_level = merge_levels_tensor[merged_mask_level] # Merge levels (proxy) [N_merged_pairs_level]


            deltaT1_level = image[tuple(maxima1_coords[merged_maxima1_indices_level].T)] - merged_level_proxy_level # [N_merged_pairs_level]
            deltaT2_level = image[tuple(maxima2_coords[merged_maxima2_indices_level].T)] - merged_level_proxy_level # [N_merged_pairs_level]
            tmax_tensor = torch.full_like(deltaT1_level, tmax) # [N_merged_pairs_level] - tensor of tmax values


            # --- Volume Criterion (Vectorized) ---
            volume_criterion_failed_mask = (merged_vol1_level < nmin) | (merged_vol2_level < nmin) # [N_merged_pairs_level]

            # --- Contrast Criterion (Vectorized) ---
            contrast_criterion_failed_mask = (deltaT1_level < tmax_tensor) | (deltaT2_level < tmax_tensor) # [N_merged_pairs_level]


            # --- Determine Maxima to Remove (Vectorized) ---
            maxima_to_remove_indices_level_max1 = merged_maxima1_indices_level[volume_criterion_failed_mask & (merged_vol2_level >= nmin)] # Max1 to remove if vol1 < nmin and vol2 >= nmin
            maxima_to_remove_indices_level_max2 = merged_maxima2_indices_level[volume_criterion_failed_mask & (merged_vol1_level >= nmin)] # Max2 to remove if vol2 < nmin and vol1 >= nmin

            # Both volumes small, remove lower intensity one (vectorized)
            both_volumes_small_mask = volume_criterion_failed_mask & (merged_vol1_level < nmin) & (merged_vol2_level < nmin) # Both vols < nmin
            lower_intensity_maxima_indices_max1 = merged_maxima1_indices_level[both_volumes_small_mask & (image[tuple(maxima1_coords[merged_maxima1_indices_level].T)] <= image[tuple(maxima2_coords[merged_maxima2_indices_level].T)])] # if max1 intensity <= max2
            lower_intensity_maxima_indices_max2 = merged_maxima2_indices_level[both_volumes_small_mask & (image[tuple(maxima1_coords[merged_maxima1_indices_level].T)] > image[tuple(maxima2_coords[merged_maxima2_indices_level].T)])] # if max1 intensity > max2


            # Contrast Criterion failures - similar logic as volume
            contrast_failed_maxima_indices_max1 = merged_maxima1_indices_level[contrast_criterion_failed_mask & (deltaT2_level >= tmax_tensor)] # Max1 to remove if deltaT1 < tmax and deltaT2 >= tmax
            contrast_failed_maxima_indices_max2 = merged_maxima2_indices_level[contrast_criterion_failed_mask & (deltaT1_level >= tmax_tensor)] # Max2 to remove if deltaT2 < tmax and deltaT1 >= tmax

            # Both contrasts fail - remove lower intensity one
            both_contrasts_fail_mask = contrast_criterion_failed_mask & (deltaT1_level < tmax_tensor) & (deltaT2_level < tmax_tensor)
            lower_intensity_contrast_fail_maxima_indices_max1 = merged_maxima1_indices_level[both_contrasts_fail_mask & (image[tuple(maxima1_coords[merged_maxima1_indices_level].T)] <= image[tuple(maxima2_coords[merged_maxima2_indices_level].T)])]
            lower_intensity_contrast_fail_maxima_indices_max2 = merged_maxima2_indices_level[both_contrasts_fail_mask & (image[tuple(maxima1_coords[merged_maxima1_indices_level].T)] > image[tuple(maxima2_coords[merged_maxima2_indices_level].T)])]


            # --- Update remove_maxima_mask (Vectorized) ---
            remove_maxima_mask[maxima_to_remove_indices_level_max1] = True
            remove_maxima_mask[maxima_to_remove_indices_level_max2] = True
            remove_maxima_mask[lower_intensity_maxima_indices_max1] = True
            remove_maxima_mask[lower_intensity_maxima_indices_max2] = True
            remove_maxima_mask[contrast_failed_maxima_indices_max1] = True
            remove_maxima_mask[contrast_failed_maxima_indices_max2] = True
            remove_maxima_mask[lower_intensity_contrast_fail_maxima_indices_max1] = True
            remove_maxima_mask[lower_intensity_contrast_fail_maxima_indices_max2] = True


        # --- Filter Maxima Coordinates (Vectorized) ---
        keep_maxima_mask = ~remove_maxima_mask # Invert the mask to keep maxima that are *not* marked for removal
        decimated_maxima_coords_tensor_final = current_maxima_coords_tensor[keep_maxima_mask] # Apply mask to filter

        decimated_maxima_coords_list = [tuple(coords) for coords in decimated_maxima_coords_tensor_final.tolist()] # Convert back to list of tuples


        return decimated_maxima_coords_list



    def _calculate_merge_level_and_volume_vectorized_internal(self, image, maxima1_coords, maxima2_coords, contour_level, connectivity, nmin):
        """
        Vectorized Internal method - Calculates merge level and volumes for *pairs* of local maxima.
        """
        merge_level_proxy = contour_level # Using contour level as proxy for merge level
        num_pairs = maxima1_coords.shape[0]

        # 1. Contour at the given level (once for all pairs at this level)
        binary_mask = self._contour_image_internal(image, merge_level_proxy) # Call internal method
        regions_mask, num_regions = self._identify_regions_internal(binary_mask, connectivity) # Call internal method

        # 2. Get Region Labels for Maxima (Vectorized)
        maxima1_region_labels = regions_mask[tuple(maxima1_coords.T)] # [N_pairs] - region labels for max1 in each pair
        maxima2_region_labels = regions_mask[tuple(maxima2_coords.T)] # [N_pairs] - region labels for max2 in each pair


        # 3. Check for Merges (Vectorized) - Maxima in same non-background region
        merged_mask = ~(torch.isnan(maxima1_region_labels) | torch.isnan(maxima2_region_labels)) & (maxima1_region_labels != 0) & (maxima1_region_labels == maxima2_region_labels) # [N_pairs] - boolean mask - True if merged


        merge_levels_tensor = torch.full((num_pairs,), merge_level_proxy, dtype=image.dtype, device=image.device) # [N_pairs] - tensor of merge levels (proxy)
        vol1_tensor = torch.zeros(num_pairs, dtype=torch.float, device=image.device) # [N_pairs] - volumes for max1's regions
        vol2_tensor = torch.zeros(num_pairs, dtype=torch.float, device=image.device) # [N_pairs] - volumes for max2's regions


        # 4. Calculate Volumes for Merged Pairs (Vectorized - only for merged pairs)
        merged_pair_indices = torch.arange(num_pairs)[merged_mask] # Indices of pairs that are merged [N_merged_pairs_level]

        if merged_pair_indices.numel() > 0: # Only compute volumes if there are merged pairs
            merged_region_labels = maxima1_region_labels[merged_mask] # Region labels for merged pairs (using max1 labels as they are same) [N_merged_pairs_level]

            for i in range(merged_pair_indices.shape[0]): # Iterate through merged pair indices (can we vectorize this further?)
                pair_index = merged_pair_indices[i] # Original pair index
                region_label = merged_region_labels[i].int() # Get int label for masking
                merged_region_mask = (regions_mask == region_label) # Mask of the merged region

                volume = torch.sum(merged_region_mask).item() # Calculate volume for the *merged* region (shared volume)
                vol1_tensor[pair_index] = volume # Assign same volume to both for now - simplification
                vol2_tensor[pair_index] = volume # Assign same volume to both for now - simplification


        return merge_levels_tensor, vol1_tensor, vol2_tensor, merged_mask # Return all info as tensors



    def _identify_candidate_local_maxima_box_internal(self, image, dmax, vmax): # Made internal
        """
        Internal method - Identifies candidate local maxima using a box filter approach.
        Compatibility fix for PyTorch versions < 1.12 (no nan_to_num in MaxPool).
        """
        ndim = image.ndim
        if ndim == 2:
            kernel_size = 2 * dmax + 1
            padding = dmax
            max_pool = torch.nn.MaxPool2d(kernel_size=kernel_size, padding=padding) # nan_to_num removed for older PyTorch
        elif ndim == 3:
            kernel_size = (2 * vmax + 1, 2 * dmax + 1, 2 * dmax + 1) # (depth, height, width)
            padding = (vmax, dmax, dmax)
            print(f"kernel_size: {kernel_size}, padding: {padding}")
            max_pool = torch.nn.MaxPool3d(kernel_size=kernel_size, padding=padding) # nan_to_num removed for older PyTorch
        else:
            raise ValueError("Image must be 2D or 3D.")

        # Replace NaNs with a very small negative number *before* max pooling for older PyTorch versions
        nan_mask = torch.isnan(image)
        print(f"Number of NaNs in image: {torch.sum(nan_mask)}")
        image_nan_filled = image.clone() # Clone to avoid modifying original image
        image_nan_filled[nan_mask] = torch.tensor(float('-inf'), dtype=image.dtype, device=image.device) # Replace NaNs with -inf
        max_pooled_image = max_pool(image_nan_filled.unsqueeze(0).unsqueeze(0)).squeeze(0).squeeze(0) # Add channel and batch dims for pooling

        # Compare original image with max-pooled image to find maxima candidates
        candidate_maxima = (image == max_pooled_image)
        return candidate_maxima


    def _detect_merges_internal(self, previous_regions_mask, current_regions_mask): # Made internal
        """
        Internal method - Detects merges between regions from a previous contour level to the current one.
        """
        if previous_regions_mask is None: # No previous regions to compare to at the very first level
            return []

        merges = []
        previous_region_labels = set(int(x) for x in torch.unique(previous_regions_mask) if x != 0 and not torch.isnan(x)) # Exclude background label 0 and NaN labels
        current_region_labels = set(int(x) for x in torch.unique(current_regions_mask) if x != 0 and not torch.isnan(x)) # Exclude background label 0 and NaN labels


        # For each region in the previous level, find which current region(s) it overlaps with
        region_overlap = {} # Key: previous region label, Value: set of current region labels it overlaps with

        for prev_label in previous_region_labels:
            overlap_current_labels = set()
            prev_region_mask = (previous_regions_mask == prev_label)
            overlap_mask = prev_region_mask & (current_regions_mask != 0) # Pixels of prev region that are also in any current region (non-background)
            overlapping_current_region_labels = set(int(x) for x in torch.unique(current_regions_mask[overlap_mask]) if x != 0 and not torch.isnan(x)) # Exclude background label 0 and NaN labels
            region_overlap[prev_label] = overlapping_current_region_labels

        merged_region_map = {} # Key: current region label, Value: set of previous region labels merged into it

        for prev_label in previous_region_labels:
            for current_label in region_overlap[prev_label]:
                merged_region_map.setdefault(current_label, set()).add(prev_label)

        detected_merges = []
        for current_label, prev_labels in merged_region_map.items():
            if len(prev_labels) > 1: # More than one previous region merged into this current region - a merge occurred.
                detected_merges.append(tuple(sorted(list(prev_labels)))) # Store the merged previous region IDs (tuple for immutability)

        region_merges_list = []
        for current_label in current_region_labels:
            current_region_mask = (current_regions_mask == current_label)
            overlapping_prev_region_labels = set(int(x) for x in torch.unique(previous_regions_mask[current_region_mask]) if x != 0 and not torch.isnan(x)) # Exclude background label 0 and NaN labels
            if len(overlapping_prev_region_labels) > 1:
                region_merges_list.append(tuple(sorted(list(overlapping_prev_region_labels)))) # Store merged previous region IDs


        # Remove duplicates and sort the merges (by merged region IDs)
        unique_merges = sorted(list(set(region_merges_list))) # Use set to remove duplicates, then sort for consistent order

        return unique_merges


    def _identify_regions_internal(self, binary_contour_mask, connectivity): # Made internal
        """
        Internal method - Identifies connected regions in a binary contour mask using connected components labeling.
        """
        return self._identify_regions_torch_bfs_internal(binary_contour_mask, connectivity) # Call internal method


    def _identify_regions_torch_bfs_internal(self, binary_contour_mask, connectivity): # Made internal
        """
        Internal method - Identifies connected regions in a binary contour mask using BFS (PyTorch implementation for GPU).
        """
        image_shape = binary_contour_mask.shape
        labeled_mask = torch.zeros_like(binary_contour_mask, dtype=torch.int32, device=binary_contour_mask.device) # Initialize labeled mask on same device
        region_label = 0

        # Get indices of foreground pixels (True values, excluding NaNs - NaNs in boolean context are False)
        foreground_indices = (binary_contour_mask > 0).nonzero() # Get coordinates of foreground pixels

        processed_pixels = torch.zeros_like(binary_contour_mask, dtype=torch.bool, device=binary_contour_mask.device) # Track processed pixels on same device

        for start_coords_index in foreground_indices:
            start_coords = tuple(start_coords_index.tolist()) # Convert to tuple for indexing

            if not processed_pixels[start_coords]: # If pixel not yet processed, start new region
                region_label += 1
                queue = [start_coords] # Initialize BFS queue
                processed_pixels[start_coords] = True
                labeled_mask[start_coords] = region_label

            while queue:
                current_coords = queue.pop(0)

                for neighbor_coords_tensor in self._get_neighbors_torch_internal(current_coords, image_shape, connectivity): # Get neighbors as tensor # Call internal method
                    neighbor_coords = tuple(neighbor_coords_tensor.tolist()) # Convert neighbor coords to tuple for indexing

                    if (0 <= neighbor_coords[0] < image_shape[0] and 0 <= neighbor_coords[1] < image_shape[1] and  # Basic bounds check - already done in get_neighbors_torch, but double check for 2D
                        binary_contour_mask[neighbor_coords] and not processed_pixels[neighbor_coords]): # Check if neighbor is foreground and not processed (binary_contour_mask[NaN] is False)

                        processed_pixels[neighbor_coords] = True
                        labeled_mask[neighbor_coords] = region_label
                        queue.append(neighbor_coords) # Add neighbor to queue

        num_regions = region_label # Max region label is the number of regions

        return labeled_mask, num_regions


    def _contour_image_internal(self, image, level): # Made internal
        """
        Internal method - Contours the image at a given intensity level.
        """
        return image >= level


    def _get_neighbors_torch_internal(self, coords, image_shape, connectivity): # Made internal, static
        """
        Internal static method - Get neighbors of a pixel/voxel based on connectivity, PyTorch version.
        """
        ndim = len(image_shape)
        neighbor_offsets_list = []

        if ndim == 2:
            if connectivity == 4:
                neighbor_offsets_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            elif connectivity == 8:
                neighbor_offsets_list = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            else:
                raise ValueError("Invalid connectivity for 2D. Choose 4 or 8.")
        elif ndim == 3:
            if connectivity == 6:
                neighbor_offsets_list = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
            elif connectivity == 26:
                neighbor_offsets_list = []
                for dd in [-1, 0, 1]:
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if (dd, dr, dc) != (0, 0, 0):
                                neighbor_offsets_list.append((dd, dr, dc))
            elif connectivity == 18:
                neighbor_offsets_list = [
                    (-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1),
                    (-1, -1, 0), (-1, 1, 0), (-1, 0, -1), (-1, 0, 1),
                    (1, -1, 0), (1, 1, 0), (1, 0, -1), (1, 0, 1),
                    (0, -1, -1), (0, -1, 1), (0, 1, -1), (0, 1, 1)
                ]
            elif connectivity == 6:
                 neighbor_offsets_list = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
            else:
                raise ValueError("Invalid connectivity for 3D. Choose 6, 18, or 26.")
        else:
            raise ValueError("Image must be 2D or 3D.")

        neighbor_offsets = torch.tensor(neighbor_offsets_list, dtype=torch.long) # Convert to tensor

        coords_tensor = torch.tensor(coords, dtype=torch.long) # Input coords to tensor

        neighbor_coords = coords_tensor + neighbor_offsets # Calculate neighbor coords

        # Keep only valid coordinates within image bounds
        valid_neighbors_mask = torch.ones(neighbor_coords.shape[0], dtype=torch.bool)
        for i in range(ndim):
            valid_neighbors_mask = valid_neighbors_mask & (neighbor_coords[:, i] >= 0) & (neighbor_coords[:, i] < image_shape[i])

        return neighbor_coords[valid_neighbors_mask] # Return only valid neighbors


# Re-assigning methods to the class (no changes in these, just ensuring they are part of the Dendrogram class)
Dendrogram._identify_candidate_local_maxima_box_internal = Dendrogram._identify_candidate_local_maxima_box_internal
Dendrogram._detect_merges_internal = Dendrogram._detect_merges_internal
Dendrogram._identify_regions_internal = Dendrogram._identify_regions_internal
Dendrogram._identify_regions_torch_bfs_internal = Dendrogram._identify_regions_torch_bfs_internal
Dendrogram._contour_image_internal = Dendrogram._contour_image_internal
Dendrogram._get_neighbors_torch_internal = Dendrogram._get_neighbors_torch_internal


if __name__ == '__main__':
    # Example Usage and Comparison - Including original loop-based Dendrogram for timing comparison
    import time

    # Dummy 3D data with a peak and some NaNs (adjust size for timing tests)
    data_3d_np = np.zeros((30, 60, 60), dtype=np.float32) # Larger data for timing
    data_3d_np[15, 30, 30] = 20  # Strong peak
    data_3d_np[10:20, 20:40, 20:40] = 10 # Extended emission
    data_3d_np[:5, :, :] = np.nan  # Add NaN slices at the beginning
    data_3d_np[:, :10, :] = np.nan  # Add NaN columns at the beginning
    data_cube_torch = torch.from_numpy(data_3d_np).to("cpu") # Run on CPU for consistent timing in example


    sigma_noise = 0.5 # Example noise level
    pixels_per_beam = 1.5 # Example pixels per beam
    min_value_threshold_K = 0.75 # Example min_value
    contour_levels_example = np.linspace(np.nanmax(data_3d_np), min_value_threshold_K, num=10)


    # 1. Original Loop-Based Dendrogram (for timing comparison - assuming you have the loop-based version saved as 'dendrogram_loop.py')
    # (You would need to have a Dendrogram class saved in 'dendrogram_loop.py' with the original _decimate_local_maxima_internal)
    # from dendrogram_loop import Dendrogram as DendrogramLoop # Uncomment if you have the loop-based version in a separate file
    class DendrogramLoop(Dendrogram): # Temporary - rename to DendrogramLoop and adjust name in init if you want to keep original code in same file
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.name = "Loop-Based Dendrogram" # For comparison output
        _decimate_local_maxima_internal = Dendrogram.__dict__['_decimate_local_maxima_internal'] # Revert to loop-based version (if you have it saved under the same class name)
        # (If you have a separate file, just import DendrogramLoop from it instead of this temporary definition)


    dendrogram_loop_class = DendrogramLoop(connectivity=6, dmax=2, vmax=2, rms_noise=sigma_noise, ppb=pixels_per_beam, min_value=min_value_threshold_K)


    start_time_loop = time.perf_counter()
    dendrogram_loop_output, merge_history_loop_output, local_maxima_mask_loop_output = dendrogram_loop_class.compute(data_cube_torch, contour_levels_example)
    end_time_loop = time.perf_counter()
    time_loop = end_time_loop - start_time_loop

    num_maxima_loop = int(torch.sum(local_maxima_mask_loop_output).item())


    # 2. Vectorized Dendrogram Class (the code from this response)
    dendrogram_vectorized_class = Dendrogram(connectivity=6, dmax=2, vmax=2, rms_noise=sigma_noise, ppb=pixels_per_beam, min_value=min_value_threshold_K)

    start_time_vectorized = time.perf_counter()
    dendrogram_vectorized_output, merge_history_vectorized_output, local_maxima_mask_vectorized_output = dendrogram_vectorized_class.compute(data_cube_torch, contour_levels_example)
    end_time_vectorized = time.perf_counter()
    time_vectorized = end_time_vectorized - start_time_vectorized

    num_maxima_vectorized = int(torch.sum(local_maxima_mask_vectorized_output).item())


    # --- Comparison Output ---
    print("\n--- Dendrogram Implementation Comparison (Timing and Maxima Count) ---")
    print(f"Data Cube Size: {data_3d_np.shape}")
    print(f"Contour Levels: {len(contour_levels_example)}")
    print(f"Parameters: connectivity={6}, dmax=2, vmax=2, rms_noise={sigma_noise}, ppb={pixels_per_beam}, min_value={min_value_threshold_K}")

    print(f"\n{dendrogram_loop_class.name}:")
    print(f"  Execution Time: {time_loop:.4f} seconds")
    print(f"  Number of Maxima: {num_maxima_loop}")

    print(f"\n{dendrogram_vectorized_class.name}:")
    print(f"  Execution Time: {time_vectorized:.4f} seconds")
    print(f"  Number of Maxima: {num_maxima_vectorized}")

    speedup = time_loop / time_vectorized if time_vectorized > 0 else float('inf')
    maxima_diff_percent = 0
    if max(num_maxima_loop, num_maxima_vectorized) > 0:
        maxima_diff_percent = abs(num_maxima_loop - num_maxima_vectorized) / max(num_maxima_loop, num_maxima_vectorized) * 100.0

    print(f"\nSpeedup (Loop-based vs. Vectorized): ~{speedup:.2f}x")
    print(f"Difference in Number of Maxima: {abs(num_maxima_loop - num_maxima_vectorized)} ( ~{maxima_diff_percent:.2f}%)")

    # --- (Optional) Add more detailed comparison of dendrogram structure and merge history if needed ---
    print("\n--- Comparison Complete ---")
