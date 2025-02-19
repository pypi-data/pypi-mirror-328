from ._utility._funs import prim2conv, draw_peak_density, theta_intensity_area,combined_peak,generate_random_polynomial,scale_list
from pymatgen.core.structure import Structure, Lattice
import spglib
from ase import Atoms
from pymatgen.analysis.diffraction import xrd
import numpy as np

def _atom2str(atoms, deformation):
    """
    Convert an ASE Atoms object into a Pymatgen Structure.

    Parameters:
    ----------
    atoms : ase.Atoms
        The atomic structure in ASE format.
    deformation : bool
        Whether to apply deformation to the atomic structure.

    Returns:
    -------
    pymatgen.core.structure.Structure
        The converted Pymatgen Structure object.
    """
    _, _, c_atom = prim2conv(atoms, deformation)
    cell = c_atom.get_cell()
    symbols = c_atom.get_chemical_symbols()
    positions = c_atom.get_scaled_positions()
    lattice = Lattice(cell)
    
    return Structure(lattice, symbols, positions)

def get_diff(atom, deformation):
    """
    Compute the X-ray diffraction (XRD) pattern for a given atomic structure.

    Parameters:
    ----------
    atom : ase.Atoms
        The atomic structure in ASE format.
    deformation : bool
        Whether to apply deformation to the structure.

    Returns:
    -------
    tuple of np.ndarray
        - `mu_array` : 2θ angles of diffraction peaks.
        - `Ints` : Corresponding diffraction intensities.
    """
    calculator = xrd.XRDCalculator()
    struc = _atom2str(atom, deformation)
    
    pattern = calculator.get_pattern(struc, two_theta_range=(10, 80))
    
    return pattern.x, pattern.y

def matgen_xrdsim(atom):
    """
    Simulate X-ray diffraction (XRD) pattern using Pymatgen's XRD calculator.

    Parameters:
    ----------
    atom : ase.Atoms
        The atomic structure in ASE format.

    Returns:
    -------
    tuple
        - `None` (placeholder for additional output, if needed in the future).
        - `nor_y` : Normalized diffraction intensity profile.
    """
    wavelength = 1.54184
    two_theta_range = (10, 80.0, 0.1)

    mu_array, Ints = get_diff(atom, deformation=False)
    Γ = 0.888 * wavelength / (20 * np.cos(np.radians(np.array(mu_array) / 2)))  # GrainSize = 20nm
    gamma_list = Γ / 2 + 1e-10
    sigma2_list = Γ**2 / (8 * np.sqrt(2)) + 1e-10

    x_sim = np.arange(two_theta_range[0], two_theta_range[1], two_theta_range[2])
    y_sim = sum(draw_peak_density(x_sim, Ints[i], mu_array[i], gamma_list[i], sigma2_list[i]) for i in range(len(Ints)))
    
    nor_y = y_sim / theta_intensity_area(x_sim, y_sim)  # Normalize the profile
    
    return None, nor_y
