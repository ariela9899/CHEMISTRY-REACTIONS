"""
Core Molecule model — supports atoms, molecular weight, charge, state of matter,
and various chemical properties.
"""

from dataclasses import dataclass, field
from typing import Dict, Optional


# Atomic weights (g/mol)
ATOMIC_WEIGHTS: Dict[str, float] = {
    "H": 1.008,
    "He": 4.003,
    "Li": 6.941,
    "Be": 9.012,
    "B": 10.811,
    "C": 12.011,
    "N": 14.007,
    "O": 15.999,
    "F": 18.998,
    "Ne": 20.180,
    "Na": 22.990,
    "Mg": 24.305,
    "Al": 26.982,
    "Si": 28.086,
    "P": 30.974,
    "S": 32.065,
    "Cl": 35.453,
    "Ar": 39.948,
    "K": 39.098,
    "Ca": 40.078,
    "Fe": 55.845,
    "Cu": 63.546,
    "Zn": 65.38,
    "Br": 79.904,
    "Ag": 107.868,
    "I": 126.904,
    "Ba": 137.327,
    "Pb": 207.2,
}

# Electronegativity values (Pauling scale)
ELECTRONEGATIVITY: Dict[str, float] = {
    "H": 2.20, "C": 2.55, "N": 3.04, "O": 3.44, "F": 3.98,
    "Na": 0.93, "Mg": 1.31, "Al": 1.61, "Si": 1.90, "P": 2.19,
    "S": 2.58, "Cl": 3.16, "K": 0.82, "Ca": 1.00, "Fe": 1.83,
    "Cu": 1.90, "Zn": 1.65, "Br": 2.96, "I": 2.66,
}


@dataclass
class Molecule:
    """
    Represents a chemical molecule with its composition and properties.

    Attributes:
        name: Common name (e.g. "water")
        formula: Chemical formula string (e.g. "H2O")
        atoms: Dict mapping element symbol to atom count (e.g. {"H": 2, "O": 1})
        charge: Net ionic charge (0 for neutral molecules)
        state: Physical state at standard conditions ("g", "l", "s", "aq")
        iupac_name: IUPAC systematic name (optional)
        cas_number: CAS registry number (optional)
        description: Short description (optional)
    """
    name: str
    formula: str
    atoms: Dict[str, int]
    charge: int = 0
    state: str = "g"  # g=gas, l=liquid, s=solid, aq=aqueous
    iupac_name: Optional[str] = None
    cas_number: Optional[str] = None
    description: Optional[str] = None

    # ------------------------------------------------------------------ #
    #  Computed properties                                                 #
    # ------------------------------------------------------------------ #

    @property
    def molecular_weight(self) -> float:
        """Molecular weight in g/mol."""
        return sum(
            ATOMIC_WEIGHTS.get(element, 0) * count
            for element, count in self.atoms.items()
        )

    @property
    def atom_count(self) -> int:
        """Total number of atoms in one molecule."""
        return sum(self.atoms.values())

    @property
    def element_symbols(self) -> list:
        """List of unique elements in the molecule."""
        return list(self.atoms.keys())

    @property
    def is_organic(self) -> bool:
        """True if the molecule contains carbon."""
        return "C" in self.atoms

    @property
    def is_ionic(self) -> bool:
        """True if net charge is non-zero."""
        return self.charge != 0

    @property
    def mass_composition(self) -> Dict[str, float]:
        """Percentage mass of each element."""
        mw = self.molecular_weight
        if mw == 0:
            return {}
        return {
            element: round((ATOMIC_WEIGHTS.get(element, 0) * count / mw) * 100, 2)
            for element, count in self.atoms.items()
        }

    @property
    def empirical_formula(self) -> str:
        """Empirical formula — atoms divided by their GCD."""
        from math import gcd
        from functools import reduce
        counts = list(self.atoms.values())
        common = reduce(gcd, counts)
        parts = "".join(
            f"{el}{count // common if count // common > 1 else ''}"
            for el, count in self.atoms.items()
        )
        return parts

    # ------------------------------------------------------------------ #
    #  Helpers                                                             #
    # ------------------------------------------------------------------ #

    def moles_to_grams(self, moles: float) -> float:
        """Convert moles of this molecule to grams."""
        return moles * self.molecular_weight

    def grams_to_moles(self, grams: float) -> float:
        """Convert grams of this molecule to moles."""
        return grams / self.molecular_weight

    def contains(self, element: str) -> bool:
        """Return True if the molecule contains the given element."""
        return element in self.atoms

    def __repr__(self) -> str:
        state_label = {"g": "(g)", "l": "(l)", "s": "(s)", "aq": "(aq)"}.get(self.state, "")
        charge_label = f"  charge={self.charge:+d}" if self.charge != 0 else ""
        return (
            f"Molecule({self.formula}{state_label}  MW={self.molecular_weight:.3f} g/mol"
            f"{charge_label}  [{self.name}])"
        )

    def __eq__(self, other) -> bool:
        if not isinstance(other, Molecule):
            return NotImplemented
        return self.formula == other.formula and self.charge == other.charge

    def __hash__(self) -> int:
        return hash((self.formula, self.charge))
