"""Generate Smaps for an antenna."""

import numpy as np
from numpy.typing import NDArray


def get_smaps(
    shape: tuple[int, ...],
    n_coils: int,
    antenna: str = "birdcage",
) -> NDArray[np.complex64]:
    """Get sensitivity maps for a specific antenna.

    Parameters
    ----------
    shape
        Volume shape
    n_coils
        number of coil in the antenna
    antenna
        name of the antenna to emulate. Only "birdcage" is currently supported.
    dtype
        return datatype for the sensitivity maps.
    """
    if antenna == "birdcage":
        return _birdcage_maps((n_coils, *shape), nzz=n_coils)
    else:
        raise NotImplementedError


def _birdcage_maps(
    shape: tuple[int, ...],
    r: float = 1.5,
    nzz: int = 8,
) -> NDArray[np.complex64]:
    """Simulate birdcage coil sensitivities.

    Parameters
    ----------
    shape
        sensitivity maps shape (nc, x,y,z)
    r
        Relative radius of birdcage.
    nzz
        number of coils per ring.
    dtype

    Returns
    -------
    np.ndarray: complex sensitivity profiles.

    References
    ----------
    https://sigpy.readthedocs.io/en/latest/_modules/sigpy/mri/sim.html
    """
    if len(shape) == 4:
        nc, nz, ny, nx = shape
    elif len(shape) == 3:
        nc, ny, nx = shape
        nz = 1
    else:
        raise ValueError("shape must be [nc, nx, ny, nz] or [nc, nx, ny]")
    c, z, y, x = np.mgrid[:nc, :nz, :ny, :nx]

    nc_arr = np.arange(nc)[:, np.newaxis, np.newaxis, np.newaxis]
    coilx = r * np.cos(nc_arr * (2 * np.pi / nzz), dtype=np.float32)
    coily = r * np.sin(nc_arr * (2 * np.pi / nzz), dtype=np.float32)
    coilz = np.floor(nc_arr / nzz) - 0.5 * (np.ceil(nc / nzz) - 1)
    coil_phs = -(nc_arr + np.floor(nc_arr / nzz)) * (2 * np.pi / nzz)

    z, y, x = np.meshgrid(
        np.arange(nz, dtype=np.float32),
        np.arange(ny, dtype=np.float32),
        np.arange(nx, dtype=np.float32),
        indexing="ij",
    )
    x_co = (x - nx / 2.0) / (nx / 2.0) - coilx
    y_co = (y - ny / 2.0) / (ny / 2.0) - coily
    z_co = (z - nz / 2.0) / (nz / 2.0) - coilz
    rr = np.sqrt(x_co**2 + y_co**2 + z_co**2)
    phi = np.arctan2(x_co, -y_co) + coil_phs

    out = (1 / rr) * np.exp(1j * phi)
    rss = np.sqrt(np.sum(np.abs(out) ** 2, axis=0))
    out /= rss
    out = np.squeeze(out)
    return out.astype(np.complex64)
