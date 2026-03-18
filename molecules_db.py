"""
Extended molecule database — covers inorganic, organic, acids/bases, salts,
atmospheric gases, and common laboratory compounds.
"""

from molecule import Molecule

# ============================================================= #
#  INORGANIC — Simple diatomic & triatomic gases                #
# ============================================================= #

H2 = Molecule(
    name="hydrogen gas",
    formula="H2",
    atoms={"H": 2},
    state="g",
    iupac_name="dihydrogen",
    cas_number="1333-74-0",
    description="Lightest element; fuel in hydrogen cells.",
)

O2 = Molecule(
    name="oxygen gas",
    formula="O2",
    atoms={"O": 2},
    state="g",
    iupac_name="dioxygen",
    cas_number="7782-44-7",
    description="Essential for aerobic respiration and combustion.",
)

N2 = Molecule(
    name="nitrogen gas",
    formula="N2",
    atoms={"N": 2},
    state="g",
    iupac_name="dinitrogen",
    cas_number="7727-37-9",
    description="Makes up ~78% of Earth's atmosphere.",
)

Cl2 = Molecule(
    name="chlorine gas",
    formula="Cl2",
    atoms={"Cl": 2},
    state="g",
    iupac_name="dichlorine",
    cas_number="7782-50-5",
    description="Yellow-green toxic gas; used as disinfectant.",
)

F2 = Molecule(
    name="fluorine gas",
    formula="F2",
    atoms={"F": 2},
    state="g",
    iupac_name="difluorine",
    cas_number="7782-41-4",
    description="Most electronegative element; extremely reactive.",
)

Br2 = Molecule(
    name="bromine",
    formula="Br2",
    atoms={"Br": 2},
    state="l",
    iupac_name="dibromine",
    cas_number="7726-95-6",
    description="Reddish-brown liquid halogen.",
)

I2 = Molecule(
    name="iodine",
    formula="I2",
    atoms={"I": 2},
    state="s",
    iupac_name="diiodine",
    cas_number="7553-56-2",
    description="Purple-black solid; essential trace element.",
)

# ============================================================= #
#  WATER & HYDROGEN COMPOUNDS                                    #
# ============================================================= #

H2O = Molecule(
    name="water",
    formula="H2O",
    atoms={"H": 2, "O": 1},
    state="l",
    iupac_name="oxidane",
    cas_number="7732-18-5",
    description="Universal solvent; essential for life.",
)

H2O2 = Molecule(
    name="hydrogen peroxide",
    formula="H2O2",
    atoms={"H": 2, "O": 2},
    state="l",
    cas_number="7722-84-1",
    description="Oxidiser and bleaching agent.",
)

H2S = Molecule(
    name="hydrogen sulfide",
    formula="H2S",
    atoms={"H": 2, "S": 1},
    state="g",
    cas_number="7783-06-4",
    description="Toxic gas with rotten-egg odour.",
)

NH3 = Molecule(
    name="ammonia",
    formula="NH3",
    atoms={"N": 1, "H": 3},
    state="g",
    iupac_name="azane",
    cas_number="7664-41-7",
    description="Base; used in fertilisers and refrigerants.",
)

HCl = Molecule(
    name="hydrochloric acid",
    formula="HCl",
    atoms={"H": 1, "Cl": 1},
    state="g",
    iupac_name="hydrogen chloride",
    cas_number="7647-01-0",
    description="Strong acid; produced in the stomach.",
)

HF = Molecule(
    name="hydrofluoric acid",
    formula="HF",
    atoms={"H": 1, "F": 1},
    state="g",
    cas_number="7664-39-3",
    description="Weak acid but extremely corrosive.",
)

HBr = Molecule(
    name="hydrobromic acid",
    formula="HBr",
    atoms={"H": 1, "Br": 1},
    state="g",
    cas_number="10035-10-6",
    description="Strong acid; used in organic synthesis.",
)

HI = Molecule(
    name="hydroiodic acid",
    formula="HI",
    atoms={"H": 1, "I": 1},
    state="g",
    cas_number="10034-85-2",
    description="Strong acid; reducing agent.",
)

# ============================================================= #
#  OXIDES & CARBON COMPOUNDS                                     #
# ============================================================= #

CO2 = Molecule(
    name="carbon dioxide",
    formula="CO2",
    atoms={"C": 1, "O": 2},
    state="g",
    iupac_name="carbon dioxide",
    cas_number="124-38-9",
    description="Greenhouse gas; product of combustion.",
)

CO = Molecule(
    name="carbon monoxide",
    formula="CO",
    atoms={"C": 1, "O": 1},
    state="g",
    cas_number="630-08-0",
    description="Toxic gas; product of incomplete combustion.",
)

NO = Molecule(
    name="nitric oxide",
    formula="NO",
    atoms={"N": 1, "O": 1},
    state="g",
    iupac_name="nitrogen monoxide",
    cas_number="10102-43-9",
    description="Free radical; biological signalling molecule.",
)

NO2 = Molecule(
    name="nitrogen dioxide",
    formula="NO2",
    atoms={"N": 1, "O": 2},
    state="g",
    cas_number="10102-44-0",
    description="Reddish-brown gas; component of smog.",
)

SO2 = Molecule(
    name="sulfur dioxide",
    formula="SO2",
    atoms={"S": 1, "O": 2},
    state="g",
    cas_number="7446-09-5",
    description="Pungent gas; causes acid rain.",
)

SO3 = Molecule(
    name="sulfur trioxide",
    formula="SO3",
    atoms={"S": 1, "O": 3},
    state="g",
    cas_number="7446-11-9",
    description="Reacts with water to form sulfuric acid.",
)

P2O5 = Molecule(
    name="phosphorus pentoxide",
    formula="P2O5",
    atoms={"P": 2, "O": 5},
    state="s",
    cas_number="1314-56-3",
    description="Powerful desiccant.",
)

SiO2 = Molecule(
    name="silicon dioxide",
    formula="SiO2",
    atoms={"Si": 1, "O": 2},
    state="s",
    iupac_name="silicon dioxide",
    cas_number="7631-86-9",
    description="Sand / quartz; major component of glass.",
)

# ============================================================= #
#  STRONG ACIDS                                                  #
# ============================================================= #

H2SO4 = Molecule(
    name="sulfuric acid",
    formula="H2SO4",
    atoms={"H": 2, "S": 1, "O": 4},
    state="l",
    cas_number="7664-93-9",
    description="Strong diprotic acid; most widely produced chemical.",
)

HNO3 = Molecule(
    name="nitric acid",
    formula="HNO3",
    atoms={"H": 1, "N": 1, "O": 3},
    state="l",
    cas_number="7697-37-2",
    description="Strong oxidising acid; used in fertiliser production.",
)

H3PO4 = Molecule(
    name="phosphoric acid",
    formula="H3PO4",
    atoms={"H": 3, "P": 1, "O": 4},
    state="l",
    cas_number="7664-38-2",
    description="Triprotic weak acid; used in food industry.",
)

H2CO3 = Molecule(
    name="carbonic acid",
    formula="H2CO3",
    atoms={"H": 2, "C": 1, "O": 3},
    state="aq",
    cas_number="463-79-6",
    description="Weak diprotic acid; CO2 dissolved in water.",
)

# ============================================================= #
#  BASES                                                         #
# ============================================================= #

NaOH = Molecule(
    name="sodium hydroxide",
    formula="NaOH",
    atoms={"Na": 1, "O": 1, "H": 1},
    state="s",
    iupac_name="sodium hydroxide",
    cas_number="1310-73-2",
    description="Strong base (lye); used in soap making.",
)

KOH = Molecule(
    name="potassium hydroxide",
    formula="KOH",
    atoms={"K": 1, "O": 1, "H": 1},
    state="s",
    cas_number="1310-58-3",
    description="Strong base; used in batteries.",
)

Ca_OH_2 = Molecule(
    name="calcium hydroxide",
    formula="Ca(OH)2",
    atoms={"Ca": 1, "O": 2, "H": 2},
    state="s",
    iupac_name="calcium dihydroxide",
    cas_number="1305-62-0",
    description="Slaked lime; used in construction and water treatment.",
)

Mg_OH_2 = Molecule(
    name="magnesium hydroxide",
    formula="Mg(OH)2",
    atoms={"Mg": 1, "O": 2, "H": 2},
    state="s",
    cas_number="1309-42-8",
    description="Milk of magnesia; antacid.",
)

Al_OH_3 = Molecule(
    name="aluminium hydroxide",
    formula="Al(OH)3",
    atoms={"Al": 1, "O": 3, "H": 3},
    state="s",
    cas_number="21645-51-2",
    description="Amphoteric hydroxide; antacid and flame retardant.",
)

# ============================================================= #
#  SALTS                                                         #
# ============================================================= #

NaCl = Molecule(
    name="sodium chloride",
    formula="NaCl",
    atoms={"Na": 1, "Cl": 1},
    state="s",
    iupac_name="sodium chloride",
    cas_number="7647-14-5",
    description="Table salt.",
)

KCl = Molecule(
    name="potassium chloride",
    formula="KCl",
    atoms={"K": 1, "Cl": 1},
    state="s",
    cas_number="7447-40-7",
    description="Salt substitute; used in medicine.",
)

CaCl2 = Molecule(
    name="calcium chloride",
    formula="CaCl2",
    atoms={"Ca": 1, "Cl": 2},
    state="s",
    cas_number="10043-52-4",
    description="De-icing agent and desiccant.",
)

MgCl2 = Molecule(
    name="magnesium chloride",
    formula="MgCl2",
    atoms={"Mg": 1, "Cl": 2},
    state="s",
    cas_number="7786-30-3",
    description="Electrolyte; used in road treatment.",
)

Na2SO4 = Molecule(
    name="sodium sulfate",
    formula="Na2SO4",
    atoms={"Na": 2, "S": 1, "O": 4},
    state="s",
    cas_number="7757-82-6",
    description="Used in detergents and paper industry.",
)

Na2CO3 = Molecule(
    name="sodium carbonate",
    formula="Na2CO3",
    atoms={"Na": 2, "C": 1, "O": 3},
    state="s",
    iupac_name="disodium carbonate",
    cas_number="497-19-8",
    description="Soda ash / washing soda.",
)

NaHCO3 = Molecule(
    name="sodium bicarbonate",
    formula="NaHCO3",
    atoms={"Na": 1, "H": 1, "C": 1, "O": 3},
    state="s",
    cas_number="144-55-8",
    description="Baking soda; antacid.",
)

CaCO3 = Molecule(
    name="calcium carbonate",
    formula="CaCO3",
    atoms={"Ca": 1, "C": 1, "O": 3},
    state="s",
    cas_number="471-34-1",
    description="Limestone / chalk / marble.",
)

BaSO4 = Molecule(
    name="barium sulfate",
    formula="BaSO4",
    atoms={"Ba": 1, "S": 1, "O": 4},
    state="s",
    cas_number="7727-43-7",
    description="Insoluble salt; used as X-ray contrast agent.",
)

AgCl = Molecule(
    name="silver chloride",
    formula="AgCl",
    atoms={"Ag": 1, "Cl": 1},
    state="s",
    cas_number="7783-90-6",
    description="Insoluble white precipitate; photosensitive.",
)

FeCl3 = Molecule(
    name="iron(III) chloride",
    formula="FeCl3",
    atoms={"Fe": 1, "Cl": 3},
    state="s",
    cas_number="7705-08-0",
    description="Lewis acid; used in PCB etching.",
)

CuSO4 = Molecule(
    name="copper(II) sulfate",
    formula="CuSO4",
    atoms={"Cu": 1, "S": 1, "O": 4},
    state="s",
    cas_number="7758-98-7",
    description="Blue vitriol; algicide and fungicide.",
)

ZnSO4 = Molecule(
    name="zinc sulfate",
    formula="ZnSO4",
    atoms={"Zn": 1, "S": 1, "O": 4},
    state="s",
    cas_number="7733-02-0",
    description="White vitriol; dietary supplement.",
)

# ============================================================= #
#  ATMOSPHERIC & NOBLE GASES                                     #
# ============================================================= #

Ar = Molecule(
    name="argon",
    formula="Ar",
    atoms={"Ar": 1},
    state="g",
    cas_number="7440-37-1",
    description="Third most abundant gas in Earth's atmosphere.",
)

He = Molecule(
    name="helium",
    formula="He",
    atoms={"He": 1},
    state="g",
    cas_number="7440-59-7",
    description="Lightest noble gas; used in balloons and MRI.",
)

Ne = Molecule(
    name="neon",
    formula="Ne",
    atoms={"Ne": 1},
    state="g",
    cas_number="7440-01-9",
    description="Noble gas used in neon lighting.",
)

O3 = Molecule(
    name="ozone",
    formula="O3",
    atoms={"O": 3},
    state="g",
    cas_number="10028-15-6",
    description="Allotrope of oxygen; UV shield in stratosphere.",
)

# ============================================================= #
#  ORGANIC — HYDROCARBONS                                        #
# ============================================================= #

CH4 = Molecule(
    name="methane",
    formula="CH4",
    atoms={"C": 1, "H": 4},
    state="g",
    iupac_name="methane",
    cas_number="74-82-8",
    description="Simplest alkane; main component of natural gas.",
)

C2H6 = Molecule(
    name="ethane",
    formula="C2H6",
    atoms={"C": 2, "H": 6},
    state="g",
    iupac_name="ethane",
    cas_number="74-84-0",
    description="Alkane; component of natural gas.",
)

C3H8 = Molecule(
    name="propane",
    formula="C3H8",
    atoms={"C": 3, "H": 8},
    state="g",
    iupac_name="propane",
    cas_number="74-98-6",
    description="LPG fuel.",
)

C4H10 = Molecule(
    name="butane",
    formula="C4H10",
    atoms={"C": 4, "H": 10},
    state="g",
    iupac_name="butane",
    cas_number="106-97-8",
    description="LPG fuel; used in lighters.",
)

C5H12 = Molecule(
    name="pentane",
    formula="C5H12",
    atoms={"C": 5, "H": 12},
    state="l",
    iupac_name="pentane",
    cas_number="109-66-0",
    description="Liquid alkane; lab solvent.",
)

C6H14 = Molecule(
    name="hexane",
    formula="C6H14",
    atoms={"C": 6, "H": 14},
    state="l",
    iupac_name="hexane",
    cas_number="110-54-3",
    description="Non-polar solvent.",
)

C8H18 = Molecule(
    name="octane",
    formula="C8H18",
    atoms={"C": 8, "H": 18},
    state="l",
    iupac_name="octane",
    cas_number="111-65-9",
    description="Main component of petrol (gasoline); octane rating reference.",
)

C2H4 = Molecule(
    name="ethylene",
    formula="C2H4",
    atoms={"C": 2, "H": 4},
    state="g",
    iupac_name="ethene",
    cas_number="74-85-1",
    description="Simplest alkene; plant hormone; polymer precursor.",
)

C3H6 = Molecule(
    name="propylene",
    formula="C3H6",
    atoms={"C": 3, "H": 6},
    state="g",
    iupac_name="propene",
    cas_number="115-07-1",
    description="Alkene; monomer for polypropylene.",
)

C2H2 = Molecule(
    name="acetylene",
    formula="C2H2",
    atoms={"C": 2, "H": 2},
    state="g",
    iupac_name="ethyne",
    cas_number="74-86-2",
    description="Alkyne; used in welding torches.",
)

C6H6 = Molecule(
    name="benzene",
    formula="C6H6",
    atoms={"C": 6, "H": 6},
    state="l",
    iupac_name="benzene",
    cas_number="71-43-2",
    description="Aromatic hydrocarbon; known carcinogen; solvent.",
)

C7H8 = Molecule(
    name="toluene",
    formula="C7H8",
    atoms={"C": 7, "H": 8},
    state="l",
    iupac_name="methylbenzene",
    cas_number="108-88-3",
    description="Aromatic solvent; octane booster.",
)

# ============================================================= #
#  ORGANIC — OXYGENATED                                          #
# ============================================================= #

CH3OH = Molecule(
    name="methanol",
    formula="CH3OH",
    atoms={"C": 1, "H": 4, "O": 1},
    state="l",
    iupac_name="methanol",
    cas_number="67-56-1",
    description="Simplest alcohol; fuel and solvent.",
)

C2H5OH = Molecule(
    name="ethanol",
    formula="C2H5OH",
    atoms={"C": 2, "H": 6, "O": 1},
    state="l",
    iupac_name="ethanol",
    cas_number="64-17-5",
    description="Drinking alcohol; fuel additive; disinfectant.",
)

C3H7OH = Molecule(
    name="isopropanol",
    formula="C3H7OH",
    atoms={"C": 3, "H": 8, "O": 1},
    state="l",
    iupac_name="propan-2-ol",
    cas_number="67-63-0",
    description="Rubbing alcohol; common solvent.",
)

C6H12O6 = Molecule(
    name="glucose",
    formula="C6H12O6",
    atoms={"C": 6, "H": 12, "O": 6},
    state="s",
    iupac_name="(3R,4S,5S,6R)-6-(hydroxymethyl)oxane-2,3,4,5-tetrol",
    cas_number="50-99-7",
    description="Simple sugar; primary cellular energy source.",
)

C12H22O11 = Molecule(
    name="sucrose",
    formula="C12H22O11",
    atoms={"C": 12, "H": 22, "O": 11},
    state="s",
    iupac_name="sucrose",
    cas_number="57-50-1",
    description="Table sugar; disaccharide of glucose + fructose.",
)

HCHO = Molecule(
    name="formaldehyde",
    formula="HCHO",
    atoms={"H": 2, "C": 1, "O": 1},
    state="g",
    iupac_name="methanal",
    cas_number="50-00-0",
    description="Simplest aldehyde; preservative and disinfectant.",
)

CH3CHO = Molecule(
    name="acetaldehyde",
    formula="CH3CHO",
    atoms={"C": 2, "H": 4, "O": 1},
    state="l",
    iupac_name="ethanal",
    cas_number="75-07-0",
    description="Aldehyde; metabolite of ethanol oxidation.",
)

CH3COCH3 = Molecule(
    name="acetone",
    formula="CH3COCH3",
    atoms={"C": 3, "H": 6, "O": 1},
    state="l",
    iupac_name="propan-2-one",
    cas_number="67-64-1",
    description="Simplest ketone; common solvent (nail polish remover).",
)

CH3COOH = Molecule(
    name="acetic acid",
    formula="CH3COOH",
    atoms={"C": 2, "H": 4, "O": 2},
    state="l",
    iupac_name="ethanoic acid",
    cas_number="64-19-7",
    description="Weak acid; component of vinegar.",
)

HCOOH = Molecule(
    name="formic acid",
    formula="HCOOH",
    atoms={"C": 1, "H": 2, "O": 2},
    state="l",
    iupac_name="methanoic acid",
    cas_number="64-18-6",
    description="Simplest carboxylic acid; found in ant venom.",
)

# ============================================================= #
#  ORGANIC — NITROGEN-CONTAINING                                 #
# ============================================================= #

CH3NH2 = Molecule(
    name="methylamine",
    formula="CH3NH2",
    atoms={"C": 1, "H": 5, "N": 1},
    state="g",
    iupac_name="methanamine",
    cas_number="74-89-5",
    description="Simplest amine; fishy odour.",
)

C6H5NH2 = Molecule(
    name="aniline",
    formula="C6H5NH2",
    atoms={"C": 6, "H": 7, "N": 1},
    state="l",
    iupac_name="aniline",
    cas_number="62-53-3",
    description="Aromatic amine; precursor to dyes.",
)

CH3CN = Molecule(
    name="acetonitrile",
    formula="CH3CN",
    atoms={"C": 2, "H": 3, "N": 1},
    state="l",
    iupac_name="acetonitrile",
    cas_number="75-05-8",
    description="Polar aprotic solvent.",
)

CO_NH2_2 = Molecule(
    name="urea",
    formula="CO(NH2)2",
    atoms={"C": 1, "O": 1, "N": 2, "H": 4},
    state="s",
    iupac_name="urea",
    cas_number="57-13-6",
    description="End product of nitrogen metabolism; nitrogen fertiliser.",
)

# ============================================================= #
#  ORGANIC — HALOGENATED                                         #
# ============================================================= #

CH3Cl = Molecule(
    name="chloromethane",
    formula="CH3Cl",
    atoms={"C": 1, "H": 3, "Cl": 1},
    state="g",
    iupac_name="chloromethane",
    cas_number="74-87-3",
    description="Methyl chloride; refrigerant.",
)

CH2Cl2 = Molecule(
    name="dichloromethane",
    formula="CH2Cl2",
    atoms={"C": 1, "H": 2, "Cl": 2},
    state="l",
    iupac_name="dichloromethane",
    cas_number="75-09-2",
    description="Paint stripper; extraction solvent.",
)

CHCl3 = Molecule(
    name="chloroform",
    formula="CHCl3",
    atoms={"C": 1, "H": 1, "Cl": 3},
    state="l",
    iupac_name="trichloromethane",
    cas_number="67-66-3",
    description="Former anaesthetic; solvent.",
)

CCl4 = Molecule(
    name="carbon tetrachloride",
    formula="CCl4",
    atoms={"C": 1, "Cl": 4},
    state="l",
    iupac_name="tetrachloromethane",
    cas_number="56-23-5",
    description="Non-flammable solvent; ozone-depleting substance.",
)

# ============================================================= #
#  POLYMERS & LARGE BIOMOLECULES (simplified)                   #
# ============================================================= #

C2H4_polymer = Molecule(
    name="polyethylene (repeat unit)",
    formula="C2H4",
    atoms={"C": 2, "H": 4},
    state="s",
    description="Monomer unit of polyethylene (PE) plastic.",
)

C3H4O2 = Molecule(
    name="acrylic acid",
    formula="C3H4O2",
    atoms={"C": 3, "H": 4, "O": 2},
    state="l",
    iupac_name="prop-2-enoic acid",
    cas_number="79-10-7",
    description="Monomer for polyacrylate polymers.",
)

# ============================================================= #
#  REGISTRY — easy lookup by formula                            #
# ============================================================= #

REGISTRY: dict[str, Molecule] = {
    m.formula: m for m in [
        # Diatomic gases
        H2, O2, N2, Cl2, F2, Br2, I2,
        # Water & H-compounds
        H2O, H2O2, H2S, NH3, HCl, HF, HBr, HI,
        # Oxides & carbon
        CO2, CO, NO, NO2, SO2, SO3, P2O5, SiO2,
        # Acids
        H2SO4, HNO3, H3PO4, H2CO3,
        # Bases
        NaOH, KOH, Ca_OH_2, Mg_OH_2, Al_OH_3,
        # Salts
        NaCl, KCl, CaCl2, MgCl2, Na2SO4, Na2CO3, NaHCO3,
        CaCO3, BaSO4, AgCl, FeCl3, CuSO4, ZnSO4,
        # Atmospheric
        Ar, He, Ne, O3,
        # Hydrocarbons
        CH4, C2H6, C3H8, C4H10, C5H12, C6H14, C8H18,
        C2H4, C3H6, C2H2, C6H6, C7H8,
        # Oxygenated organic
        CH3OH, C2H5OH, C3H7OH, C6H12O6, C12H22O11,
        HCHO, CH3CHO, CH3COCH3, CH3COOH, HCOOH,
        # N-containing organic
        CH3NH2, C6H5NH2, CH3CN, CO_NH2_2,
        # Halogenated organic
        CH3Cl, CH2Cl2, CHCl3, CCl4,
        # Polymers
        C3H4O2,
    ]
}


def lookup(formula: str) -> Molecule:
    """Return a molecule by its formula, or raise KeyError."""
    if formula not in REGISTRY:
        raise KeyError(f"Molecule '{formula}' not found in registry. "
                       f"Available: {', '.join(sorted(REGISTRY))}")
    return REGISTRY[formula]


def search(query: str) -> list[Molecule]:
    """Search molecules by name, formula, or element symbol (case-insensitive)."""
    q = query.lower()
    return [
        m for m in REGISTRY.values()
        if q in m.name.lower()
        or q in m.formula.lower()
        or q in [el.lower() for el in m.atoms]
    ]
