"""
Chemical reactions engine.

Each Reaction stores:
  - reactants / products as {Molecule: stoichiometric coefficient}
  - enthalpy change (ΔH, kJ/mol) — negative = exothermic
  - reaction type (combustion, acid-base, decomposition, …)

Helper functions perform stoichiometry calculations.
"""

from dataclasses import dataclass, field
from typing import Dict, Optional
from molecule import Molecule


@dataclass
class Reaction:
    """
    Represents a balanced chemical reaction.

    Attributes:
        name: Short descriptive name
        reactants: {Molecule: stoichiometric coefficient}
        products:  {Molecule: stoichiometric coefficient}
        delta_h:   Enthalpy change in kJ/mol (None if unknown)
        rxn_type:  Category string
        conditions: Reaction conditions (catalyst, temperature, etc.)
        description: Longer explanation
    """
    name: str
    reactants: Dict[Molecule, int]
    products: Dict[Molecule, int]
    delta_h: Optional[float] = None
    rxn_type: str = "general"
    conditions: Optional[str] = None
    description: Optional[str] = None

    # ------------------------------------------------------------------ #
    #  Properties                                                          #
    # ------------------------------------------------------------------ #

    @property
    def is_exothermic(self) -> Optional[bool]:
        if self.delta_h is None:
            return None
        return self.delta_h < 0

    @property
    def equation(self) -> str:
        """Return a human-readable balanced equation string."""
        def side(species: Dict[Molecule, int]) -> str:
            parts = []
            for mol, coeff in species.items():
                state = {"g": "(g)", "l": "(l)", "s": "(s)", "aq": "(aq)"}.get(mol.state, "")
                prefix = f"{coeff} " if coeff != 1 else ""
                parts.append(f"{prefix}{mol.formula}{state}")
            return " + ".join(parts)

        arrow = " → "
        lhs = side(self.reactants)
        rhs = side(self.products)
        dh = f"   ΔH = {self.delta_h:+.1f} kJ/mol" if self.delta_h is not None else ""
        return f"{lhs}{arrow}{rhs}{dh}"

    @property
    def is_balanced(self) -> bool:
        """Check atom balance (ignores charge for simplicity)."""
        from collections import Counter
        left: Counter = Counter()
        right: Counter = Counter()
        for mol, coeff in self.reactants.items():
            for el, n in mol.atoms.items():
                left[el] += n * coeff
        for mol, coeff in self.products.items():
            for el, n in mol.atoms.items():
                right[el] += n * coeff
        return left == right

    # ------------------------------------------------------------------ #
    #  Stoichiometry helpers                                               #
    # ------------------------------------------------------------------ #

    def moles_of_product(self, reactant: Molecule, moles: float,
                          product: Molecule) -> float:
        """
        Given `moles` of a reactant, return the theoretical moles of product
        produced (assuming all other reactants are in excess).
        """
        r_coeff = self.reactants.get(reactant)
        p_coeff = self.products.get(product)
        if r_coeff is None:
            raise ValueError(f"{reactant.formula} is not a reactant in this reaction.")
        if p_coeff is None:
            raise ValueError(f"{product.formula} is not a product in this reaction.")
        return moles * (p_coeff / r_coeff)

    def limiting_reagent(self, available: Dict[Molecule, float]) -> Molecule:
        """
        Determine the limiting reagent given a dict of {Molecule: moles available}.
        Returns the Molecule that limits the reaction.
        """
        ratios = {}
        for mol, coeff in self.reactants.items():
            if mol not in available:
                raise ValueError(f"No amount given for reactant {mol.formula}")
            ratios[mol] = available[mol] / coeff
        return min(ratios, key=lambda m: ratios[m])

    def theoretical_yield(self, available: Dict[Molecule, float],
                           product: Molecule) -> float:
        """
        Return theoretical yield (in moles) of `product` given available moles.
        """
        lr = self.limiting_reagent(available)
        lr_moles = available[lr]
        return self.moles_of_product(lr, lr_moles, product)

    def percent_yield(self, actual_grams: float,
                      available: Dict[Molecule, float],
                      product: Molecule) -> float:
        """
        Return percent yield given the actual grams of product obtained.
        """
        theo_moles = self.theoretical_yield(available, product)
        theo_grams = product.moles_to_grams(theo_moles)
        return (actual_grams / theo_grams) * 100

    def __repr__(self) -> str:
        return f"Reaction({self.name!r}: {self.equation})"


# ================================================================= #
#  REACTION LIBRARY                                                   #
# ================================================================= #

from molecules_db import (
    H2, O2, N2, H2O, H2O2, H2S, NH3, HCl, HF, HBr,
    CO2, CO, NO, NO2, SO2, SO3,
    H2SO4, HNO3, H3PO4, H2CO3,
    NaOH, KOH, Ca_OH_2, Mg_OH_2,
    NaCl, CaCl2, Na2SO4, Na2CO3, NaHCO3, CaCO3, BaSO4, AgCl,
    CH4, C2H6, C3H8, C4H10, C8H18, C2H4, C2H2, C6H6,
    CH3OH, C2H5OH, C6H12O6, CO_NH2_2,
    CH2Cl2, CHCl3, CCl4,
    Ar, O3,
)

# ------------------------------------------------------------------ #
#  COMBUSTION                                                         #
# ------------------------------------------------------------------ #

combustion_H2 = Reaction(
    name="Combustion of hydrogen",
    reactants={H2: 2, O2: 1},
    products={H2O: 2},
    delta_h=-571.6,
    rxn_type="combustion",
    conditions="ignition",
    description="Clean combustion; used in hydrogen fuel cells.",
)

combustion_CH4 = Reaction(
    name="Combustion of methane",
    reactants={CH4: 1, O2: 2},
    products={CO2: 1, H2O: 2},
    delta_h=-890.4,
    rxn_type="combustion",
    conditions="ignition",
    description="Natural gas burning.",
)

combustion_C2H6 = Reaction(
    name="Combustion of ethane",
    reactants={C2H6: 2, O2: 7},
    products={CO2: 4, H2O: 6},
    delta_h=-3120.0,
    rxn_type="combustion",
)

combustion_C3H8 = Reaction(
    name="Combustion of propane",
    reactants={C3H8: 1, O2: 5},
    products={CO2: 3, H2O: 4},
    delta_h=-2220.0,
    rxn_type="combustion",
    description="LPG combustion.",
)

combustion_C4H10 = Reaction(
    name="Combustion of butane",
    reactants={C4H10: 2, O2: 13},
    products={CO2: 8, H2O: 10},
    delta_h=-5756.0,
    rxn_type="combustion",
    description="Lighter fuel combustion.",
)

combustion_C8H18 = Reaction(
    name="Combustion of octane",
    reactants={C8H18: 2, O2: 25},
    products={CO2: 16, H2O: 18},
    delta_h=-10942.0,
    rxn_type="combustion",
    description="Petrol combustion in engines.",
)

combustion_C2H5OH = Reaction(
    name="Combustion of ethanol",
    reactants={C2H5OH: 1, O2: 3},
    products={CO2: 2, H2O: 3},
    delta_h=-1366.8,
    rxn_type="combustion",
    description="Ethanol biofuel burning.",
)

combustion_C6H6 = Reaction(
    name="Combustion of benzene",
    reactants={C6H6: 2, O2: 15},
    products={CO2: 12, H2O: 6},
    delta_h=-6534.0,
    rxn_type="combustion",
)

combustion_CH3OH = Reaction(
    name="Combustion of methanol",
    reactants={CH3OH: 2, O2: 3},
    products={CO2: 2, H2O: 4},
    delta_h=-1452.0,
    rxn_type="combustion",
)

combustion_C2H2 = Reaction(
    name="Combustion of acetylene",
    reactants={C2H2: 2, O2: 5},
    products={CO2: 4, H2O: 2},
    delta_h=-2600.0,
    rxn_type="combustion",
    conditions="ignition — oxy-acetylene torch",
)

incomplete_combustion_CH4 = Reaction(
    name="Incomplete combustion of methane",
    reactants={CH4: 2, O2: 3},
    products={CO: 2, H2O: 4},
    rxn_type="combustion",
    description="Produces toxic CO when O2 is limited.",
)

# ------------------------------------------------------------------ #
#  ACID–BASE (NEUTRALISATION)                                         #
# ------------------------------------------------------------------ #

neutralisation_HCl_NaOH = Reaction(
    name="HCl + NaOH neutralisation",
    reactants={HCl: 1, NaOH: 1},
    products={NaCl: 1, H2O: 1},
    delta_h=-57.3,
    rxn_type="acid-base",
    description="Classic strong acid–strong base neutralisation.",
)

neutralisation_H2SO4_NaOH = Reaction(
    name="H2SO4 + NaOH neutralisation",
    reactants={H2SO4: 1, NaOH: 2},
    products={Na2SO4: 1, H2O: 2},
    rxn_type="acid-base",
)

neutralisation_HNO3_KOH = Reaction(
    name="HNO3 + KOH neutralisation",
    reactants={HNO3: 1, KOH: 1},
    products={NaCl: 1, H2O: 1},   # note: KNO3 would be exact, simplified here
    rxn_type="acid-base",
)

neutralisation_H2SO4_Ca_OH_2 = Reaction(
    name="H2SO4 + Ca(OH)2 neutralisation",
    reactants={H2SO4: 1, Ca_OH_2: 1},
    products={},  # CaSO4 + 2H2O
    rxn_type="acid-base",
    description="Forms gypsum (CaSO4).",
)

# ------------------------------------------------------------------ #
#  DECOMPOSITION                                                       #
# ------------------------------------------------------------------ #

decomp_H2O2 = Reaction(
    name="Decomposition of hydrogen peroxide",
    reactants={H2O2: 2},
    products={H2O: 2, O2: 1},
    delta_h=-196.0,
    rxn_type="decomposition",
    conditions="MnO2 catalyst or UV light",
    description="Used in rocketry and antiseptics.",
)

decomp_CaCO3 = Reaction(
    name="Thermal decomposition of limestone",
    reactants={CaCO3: 1},
    products={},   # CaO + CO2
    rxn_type="decomposition",
    conditions="~840 °C",
    description="Industrial production of quicklime (CaO).",
)

decomp_NaHCO3 = Reaction(
    name="Decomposition of baking soda",
    reactants={NaHCO3: 2},
    products={Na2CO3: 1, H2O: 1, CO2: 1},
    rxn_type="decomposition",
    conditions="heat",
    description="CO2 released makes baked goods rise.",
)

decomp_NH3 = Reaction(
    name="Decomposition of ammonia",
    reactants={NH3: 2},
    products={N2: 1, H2: 3},
    delta_h=+92.0,
    rxn_type="decomposition",
    conditions="catalyst, high temperature",
    description="Reverse of Haber process.",
)

# ------------------------------------------------------------------ #
#  SYNTHESIS / COMBINATION                                            #
# ------------------------------------------------------------------ #

synthesis_H2O = Reaction(
    name="Synthesis of water",
    reactants={H2: 2, O2: 1},
    products={H2O: 2},
    delta_h=-571.6,
    rxn_type="synthesis",
)

haber_process = Reaction(
    name="Haber–Bosch process (ammonia synthesis)",
    reactants={N2: 1, H2: 3},
    products={NH3: 2},
    delta_h=-92.4,
    rxn_type="synthesis",
    conditions="450 °C, 200 atm, Fe catalyst",
    description="Industrial ammonia production; basis of nitrogen fertilisers.",
)

contact_process_SO3 = Reaction(
    name="Contact process — SO2 to SO3",
    reactants={SO2: 2, O2: 1},
    products={SO3: 2},
    delta_h=-197.8,
    rxn_type="synthesis",
    conditions="V2O5 catalyst, ~450 °C",
    description="Step 2 in industrial sulfuric acid production.",
)

ostwald_NO = Reaction(
    name="Ostwald process — NH3 to NO",
    reactants={NH3: 4, O2: 5},
    products={NO: 4, H2O: 6},
    delta_h=-907.0,
    rxn_type="synthesis",
    conditions="Pt catalyst, ~800 °C",
    description="First step of industrial nitric acid production.",
)

# ------------------------------------------------------------------ #
#  REDOX                                                               #
# ------------------------------------------------------------------ #

oxidation_CO = Reaction(
    name="CO oxidation to CO2",
    reactants={CO: 2, O2: 1},
    products={CO2: 2},
    delta_h=-566.0,
    rxn_type="redox",
    conditions="catalytic converter",
    description="Removes toxic CO from exhaust gases.",
)

oxidation_SO2 = Reaction(
    name="SO2 to SO3",
    reactants={SO2: 2, O2: 1},
    products={SO3: 2},
    rxn_type="redox",
)

formation_NO2 = Reaction(
    name="Oxidation of NO to NO2",
    reactants={NO: 2, O2: 1},
    products={NO2: 2},
    delta_h=-114.0,
    rxn_type="redox",
    description="Key step in smog and acid rain formation.",
)

ozone_formation = Reaction(
    name="Ozone formation",
    reactants={O2: 3},
    products={O3: 2},
    delta_h=+284.0,
    rxn_type="redox",
    conditions="UV radiation in stratosphere",
)

# ------------------------------------------------------------------ #
#  PRECIPITATION                                                       #
# ------------------------------------------------------------------ #

precip_BaSO4 = Reaction(
    name="Barium sulfate precipitation",
    reactants={H2SO4: 1},   # simplified: Ba²⁺ + SO4²⁻ → BaSO4
    products={BaSO4: 1},
    rxn_type="precipitation",
    description="Qualitative test for sulfate ions.",
)

precip_AgCl = Reaction(
    name="Silver chloride precipitation",
    reactants={HCl: 1},     # simplified: Ag⁺ + Cl⁻ → AgCl
    products={AgCl: 1},
    rxn_type="precipitation",
    description="Qualitative test for chloride ions.",
)

# ------------------------------------------------------------------ #
#  FERMENTATION & BIOLOGICAL                                           #
# ------------------------------------------------------------------ #

fermentation = Reaction(
    name="Alcoholic fermentation",
    reactants={C6H12O6: 1},
    products={C2H5OH: 2, CO2: 2},
    delta_h=-67.0,
    rxn_type="biological",
    conditions="yeast, anaerobic",
    description="Glucose → ethanol + carbon dioxide.",
)

cellular_respiration = Reaction(
    name="Aerobic cellular respiration",
    reactants={C6H12O6: 1, O2: 6},
    products={CO2: 6, H2O: 6},
    delta_h=-2803.0,
    rxn_type="biological",
    description="Primary energy pathway in living organisms.",
)

photosynthesis = Reaction(
    name="Photosynthesis",
    reactants={CO2: 6, H2O: 6},
    products={C6H12O6: 1, O2: 6},
    delta_h=+2803.0,
    rxn_type="biological",
    conditions="light, chlorophyll",
    description="Plants convert sunlight into chemical energy.",
)

# ------------------------------------------------------------------ #
#  REACTION REGISTRY                                                   #
# ------------------------------------------------------------------ #

REACTION_REGISTRY: Dict[str, Reaction] = {
    r.name: r for r in [
        # Combustion
        combustion_H2, combustion_CH4, combustion_C2H6, combustion_C3H8,
        combustion_C4H10, combustion_C8H18, combustion_C2H5OH, combustion_C6H6,
        combustion_CH3OH, combustion_C2H2, incomplete_combustion_CH4,
        # Acid–base
        neutralisation_HCl_NaOH, neutralisation_H2SO4_NaOH,
        neutralisation_HNO3_KOH,
        # Decomposition
        decomp_H2O2, decomp_CaCO3, decomp_NaHCO3, decomp_NH3,
        # Synthesis
        synthesis_H2O, haber_process, contact_process_SO3, ostwald_NO,
        # Redox
        oxidation_CO, oxidation_SO2, formation_NO2, ozone_formation,
        # Precipitation
        precip_BaSO4, precip_AgCl,
        # Biological
        fermentation, cellular_respiration, photosynthesis,
    ]
}


def get_reactions_by_type(rxn_type: str) -> list[Reaction]:
    """Return all reactions of the given type."""
    return [r for r in REACTION_REGISTRY.values() if r.rxn_type == rxn_type]


def get_reactions_involving(molecule: Molecule) -> list[Reaction]:
    """Return all reactions where the molecule appears as reactant or product."""
    return [
        r for r in REACTION_REGISTRY.values()
        if molecule in r.reactants or molecule in r.products
    ]
