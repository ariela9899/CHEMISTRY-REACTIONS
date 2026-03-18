"""
Chemistry Reactions — demo entry point.

Run:  python main.py
"""

from molecules_db import REGISTRY, lookup, search
from reactions import REACTION_REGISTRY, get_reactions_by_type, get_reactions_involving


def section(title: str) -> None:
    print(f"\n{'='*60}")
    print(f"  {title}")
    print('='*60)


def demo_registry():
    section("MOLECULE REGISTRY — summary")
    print(f"Total molecules in registry: {len(REGISTRY)}")
    organic = [m for m in REGISTRY.values() if m.is_organic]
    inorganic = [m for m in REGISTRY.values() if not m.is_organic]
    print(f"  Organic    : {len(organic)}")
    print(f"  Inorganic  : {len(inorganic)}")

    # Heaviest 5
    heaviest = sorted(REGISTRY.values(), key=lambda m: m.molecular_weight, reverse=True)[:5]
    print("\nHeaviest molecules:")
    for m in heaviest:
        print(f"  {m.formula:<12}  {m.molecular_weight:>10.3f} g/mol  — {m.name}")


def demo_molecule_properties():
    section("MOLECULE PROPERTIES — selected examples")
    formulas = ["H2O", "C6H12O6", "H2SO4", "C8H18", "NH3", "CO_NH2_2"]
    # CO_NH2_2 has special key name, use name lookup fallback
    molecules = []
    for f in formulas:
        try:
            molecules.append(lookup(f))
        except KeyError:
            pass
    # add urea via direct import
    from molecules_db import CO_NH2_2 as urea
    molecules.append(urea)

    for m in molecules:
        print(f"\n{m}")
        print(f"  Atom count : {m.atom_count}")
        print(f"  Organic    : {m.is_organic}")
        composition = "  |  ".join(f"{el} {pct}%" for el, pct in m.mass_composition.items())
        print(f"  Composition: {composition}")
        if m.description:
            print(f"  Info       : {m.description}")


def demo_reactions():
    section("REACTION LIBRARY — summary")
    print(f"Total reactions: {len(REACTION_REGISTRY)}")
    types = {}
    for r in REACTION_REGISTRY.values():
        types[r.rxn_type] = types.get(r.rxn_type, 0) + 1
    for t, n in sorted(types.items()):
        print(f"  {t:<15} {n} reaction(s)")

    section("COMBUSTION REACTIONS")
    for r in get_reactions_by_type("combustion"):
        exo = "exothermic" if r.is_exothermic else ("endothermic" if r.is_exothermic is False else "")
        print(f"  {r.equation}")
        if exo:
            print(f"    [{exo}]")

    section("BIOLOGICAL REACTIONS")
    for r in get_reactions_by_type("biological"):
        print(f"  {r.name}")
        print(f"    {r.equation}")
        if r.description:
            print(f"    {r.description}")


def demo_stoichiometry():
    section("STOICHIOMETRY — combustion of methane")
    from reactions import combustion_CH4
    from molecules_db import CH4, O2, CO2, H2O

    # How many moles of CO2 from 5 mol CH4?
    moles_CH4 = 5.0
    moles_CO2 = combustion_CH4.moles_of_product(CH4, moles_CH4, CO2)
    print(f"\n  {moles_CH4} mol CH4 → {moles_CO2:.1f} mol CO2")
    print(f"  Mass of CO2 produced: {CO2.moles_to_grams(moles_CO2):.2f} g")

    # Limiting reagent
    available = {CH4: 3.0, O2: 5.0}   # O2 is limiting (need 6 mol O2 for 3 mol CH4)
    lr = combustion_CH4.limiting_reagent(available)
    print(f"\n  Available: CH4={available[CH4]} mol, O2={available[O2]} mol")
    print(f"  Limiting reagent: {lr.formula} ({lr.name})")
    theo = combustion_CH4.theoretical_yield(available, CO2)
    print(f"  Theoretical yield of CO2: {theo:.2f} mol  ({CO2.moles_to_grams(theo):.2f} g)")


def demo_search():
    section("SEARCH — molecules containing 'chlor'")
    results = search("chlor")
    for m in results:
        print(f"  {m.formula:<12}  {m.name}")

    section("SEARCH — reactions involving CO2")
    from molecules_db import CO2
    rxns = get_reactions_involving(CO2)
    print(f"  Found {len(rxns)} reaction(s):")
    for r in rxns:
        print(f"  [{r.rxn_type}]  {r.name}")


if __name__ == "__main__":
    demo_registry()
    demo_molecule_properties()
    demo_reactions()
    demo_stoichiometry()
    demo_search()
    print("\nDone.")
