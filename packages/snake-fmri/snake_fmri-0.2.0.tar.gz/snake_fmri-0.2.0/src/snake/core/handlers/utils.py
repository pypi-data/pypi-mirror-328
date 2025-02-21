"""Utility functions for handlers."""

from numpy.typing import NDArray
from ..phantom import Phantom
from copy import deepcopy


def apply_weights(
    phantom: Phantom, tissue_name: str, weights: NDArray, time_idx: int
) -> Phantom:
    """Apply weights to the tissue."""
    new_phantom = deepcopy(phantom)
    weights = weights.ravel()
    tissue_idx = list(phantom.labels).index(tissue_name)
    new_phantom.masks[tissue_idx] = phantom.masks[tissue_idx] * weights[time_idx]
    return new_phantom
