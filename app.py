"""
Chemistry Reactions — Streamlit app
Run:  streamlit run app.py
"""

import streamlit as st
from molecules_db import REGISTRY, search
from reactions import REACTION_REGISTRY, get_reactions_by_type, get_reactions_involving

st.set_page_config(
    page_title="Chemistry Reactions",
    page_icon="⚗️",
    layout="wide",
)

st.title("⚗️ Chemistry Reactions Explorer")

# ------------------------------------------------------------------ #
#  Sidebar navigation                                                  #
# ------------------------------------------------------------------ #
page = st.sidebar.radio(
    "Navigate",
    ["🔍 Molecule Search", "⚗️ Reactions", "🧮 Stoichiometry Calculator"],
)

# ================================================================== #
#  PAGE 1 — Molecule Search                                           #
# ================================================================== #
if page == "🔍 Molecule Search":
    st.header("🔍 Molecule Search")

    col1, col2 = st.columns([2, 1])
    with col1:
        query = st.text_input("Search by name, formula, or element", placeholder="e.g. water, H2O, Cl")
    with col2:
        filter_organic = st.selectbox("Filter", ["All", "Organic only", "Inorganic only"])

    # Resolve molecule list
    if query:
        results = search(query)
    else:
        results = list(REGISTRY.values())

    if filter_organic == "Organic only":
        results = [m for m in results if m.is_organic]
    elif filter_organic == "Inorganic only":
        results = [m for m in results if not m.is_organic]

    st.caption(f"{len(results)} molecule(s) found")

    if not results:
        st.info("No molecules match your search.")
    else:
        selected_formula = st.selectbox(
            "Select a molecule to inspect",
            options=[m.formula for m in results],
            format_func=lambda f: f"{f}  —  {REGISTRY[f].name}" if f in REGISTRY else f,
        )

        mol = REGISTRY.get(selected_formula) or next(
            (m for m in results if m.formula == selected_formula), None
        )

        if mol:
            st.divider()
            c1, c2 = st.columns(2)

            with c1:
                st.subheader(mol.name.capitalize())
                st.markdown(f"**Formula:** `{mol.formula}`")
                if mol.iupac_name:
                    st.markdown(f"**IUPAC name:** {mol.iupac_name}")
                if mol.cas_number:
                    st.markdown(f"**CAS number:** {mol.cas_number}")
                state_map = {"g": "Gas", "l": "Liquid", "s": "Solid", "aq": "Aqueous"}
                st.markdown(f"**State (STP):** {state_map.get(mol.state, mol.state)}")
                st.markdown(f"**Organic:** {'Yes' if mol.is_organic else 'No'}")
                if mol.description:
                    st.info(mol.description)

            with c2:
                st.subheader("Properties")
                st.metric("Molecular weight", f"{mol.molecular_weight:.3f} g/mol")
                st.metric("Total atoms", mol.atom_count)

                st.markdown("**Atom composition:**")
                for el, count in mol.atoms.items():
                    st.markdown(f"- {el}: {count}")

                st.markdown("**Mass composition (%):**")
                comp = mol.mass_composition
                comp_data = {"Element": list(comp.keys()), "Mass %": list(comp.values())}
                st.bar_chart(comp_data, x="Element", y="Mass %", height=200)

            # Reactions involving this molecule
            st.divider()
            rxns = get_reactions_involving(mol)
            if rxns:
                st.subheader(f"Reactions involving {mol.formula} ({len(rxns)})")
                for r in rxns:
                    role = "reactant" if mol in r.reactants else "product"
                    with st.expander(f"{r.name}  [{r.rxn_type}]  — as {role}"):
                        st.code(r.equation)
                        if r.description:
                            st.write(r.description)
                        if r.conditions:
                            st.caption(f"Conditions: {r.conditions}")
            else:
                st.caption("No reactions in library involve this molecule.")

# ================================================================== #
#  PAGE 2 — Reactions                                                 #
# ================================================================== #
elif page == "⚗️ Reactions":
    st.header("⚗️ Reaction Library")

    all_types = sorted({r.rxn_type for r in REACTION_REGISTRY.values()})
    selected_types = st.multiselect(
        "Filter by type", all_types, default=all_types
    )

    show_only_balanced = st.checkbox("Show only balanced reactions", value=False)

    filtered = [
        r for r in REACTION_REGISTRY.values()
        if r.rxn_type in selected_types
        and (not show_only_balanced or r.is_balanced)
    ]

    st.caption(f"{len(filtered)} reaction(s)")

    for r in filtered:
        label = f"**{r.name}**  `[{r.rxn_type}]`"
        if r.delta_h is not None:
            label += f"  ΔH = {r.delta_h:+.1f} kJ/mol"
        with st.expander(label):
            st.code(r.equation, language="")
            cols = st.columns(3)
            cols[0].metric("Type", r.rxn_type)
            if r.delta_h is not None:
                heat = "Exothermic 🔥" if r.delta_h < 0 else "Endothermic ❄️"
                cols[1].metric("Energy", heat)
            if r.conditions:
                cols[2].metric("Conditions", r.conditions)
            if r.description:
                st.write(r.description)
            balanced_label = "✅ Balanced" if r.is_balanced else "⚠️ Not balanced"
            st.caption(balanced_label)

# ================================================================== #
#  PAGE 3 — Stoichiometry Calculator                                  #
# ================================================================== #
elif page == "🧮 Stoichiometry Calculator":
    st.header("🧮 Stoichiometry Calculator")

    reaction_name = st.selectbox("Choose a reaction", list(REACTION_REGISTRY.keys()))
    rxn = REACTION_REGISTRY[reaction_name]

    st.code(rxn.equation, language="")

    st.subheader("Available moles of reactants")
    available = {}
    cols = st.columns(len(rxn.reactants))
    for i, (mol, coeff) in enumerate(rxn.reactants.items()):
        val = cols[i].number_input(
            f"{mol.formula} (stoich: {coeff})",
            min_value=0.0,
            value=float(coeff),
            step=0.1,
            key=f"reactant_{mol.formula}",
        )
        available[mol] = val

    if rxn.products:
        target_formula = st.selectbox(
            "Target product",
            [m.formula for m in rxn.products],
            format_func=lambda f: f"{f}  ({next(m.name for m in rxn.products if m.formula==f)})",
        )
        target = next(m for m in rxn.products if m.formula == target_formula)

        if st.button("Calculate"):
            try:
                lr = rxn.limiting_reagent(available)
                theo_moles = rxn.theoretical_yield(available, target)
                theo_grams = target.moles_to_grams(theo_moles)

                st.divider()
                c1, c2, c3 = st.columns(3)
                c1.metric("Limiting reagent", f"{lr.formula} ({lr.name})")
                c2.metric("Theoretical yield", f"{theo_moles:.4f} mol")
                c3.metric("Theoretical yield", f"{theo_grams:.4f} g")

                # Percent yield input
                st.subheader("Percent yield")
                actual_g = st.number_input(
                    "Actual grams obtained", min_value=0.0, value=0.0, step=0.01
                )
                if actual_g > 0:
                    pct = rxn.percent_yield(actual_g, available, target)
                    st.metric("Percent yield", f"{pct:.2f} %")
            except Exception as e:
                st.error(str(e))
    else:
        st.info("This reaction has no products defined in the library.")

    # Unit converter
    st.divider()
    st.subheader("Quick unit converter")
    mol_formula = st.selectbox(
        "Molecule", list(REGISTRY.keys()),
        format_func=lambda f: f"{f}  —  {REGISTRY[f].name}",
        key="converter_mol",
    )
    m = REGISTRY[mol_formula]
    conv_col1, conv_col2 = st.columns(2)
    grams_in = conv_col1.number_input("Grams →", min_value=0.0, value=18.015, step=0.001)
    conv_col1.write(f"= **{m.grams_to_moles(grams_in):.6f} mol**")
    moles_in = conv_col2.number_input("Moles →", min_value=0.0, value=1.0, step=0.001)
    conv_col2.write(f"= **{m.moles_to_grams(moles_in):.6f} g**")
