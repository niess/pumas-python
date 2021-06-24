'''
  Tabulated atomic elements from the Particle Data Group (PDG)
  Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/index.html
'''
from .definitions import ElementDefinition


data = {
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/hydrogen_gas.html
    'H'  : ElementDefinition(A = 1.008, I = 1.92E-08, Z = 1),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/deuterium_gas.html
    'D'  : ElementDefinition(A = 2.0141, I = 1.92E-08, Z = 1),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/helium_gas_He.html
    'He' : ElementDefinition(A = 4.0026, I = 4.18E-08, Z = 2),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/lithium_Li.html
    'Li' : ElementDefinition(A = 6.94, I = 4E-08, Z = 3),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/beryllium_Be.html
    'Be' : ElementDefinition(A = 9.01218, I = 6.37E-08, Z = 4),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/boron_B.html
    'B'  : ElementDefinition(A = 10.81, I = 7.6E-08, Z = 5),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/carbon_amorphous_C.html
    'C'  : ElementDefinition(A = 12.0107, I = 7.8E-08, Z = 6),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/nitrogen_gas.html
    'N'  : ElementDefinition(A = 14.007, I = 8.2E-08, Z = 7),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/oxygen_gas.html
    'O'  : ElementDefinition(A = 15.999, I = 9.5E-08, Z = 8),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/fluorine_gas.html
    'F'  : ElementDefinition(A = 18.9984, I = 1.15E-07, Z = 9),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/neon_gas_Ne.html
    'Ne' : ElementDefinition(A = 20.1797, I = 1.37E-07, Z = 10),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/sodium_Na.html
    'Na' : ElementDefinition(A = 22.9898, I = 1.49E-07, Z = 11),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/magnesium_Mg.html
    'Mg' : ElementDefinition(A = 24.305, I = 1.56E-07, Z = 12),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/aluminum_Al.html
    'Al' : ElementDefinition(A = 26.9815, I = 1.66E-07, Z = 13),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/silicon_Si.html
    'Si' : ElementDefinition(A = 28.0855, I = 1.73E-07, Z = 14),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/phosphorus_P.html
    'P'  : ElementDefinition(A = 30.9738, I = 1.73E-07, Z = 15),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/sulfur_S.html
    'S'  : ElementDefinition(A = 32.065, I = 1.8E-07, Z = 16),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/chlorine_gas.html
    'Cl' : ElementDefinition(A = 35.453, I = 1.74E-07, Z = 17),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/argon_gas_Ar.html
    'Ar' : ElementDefinition(A = 39.948, I = 1.88E-07, Z = 18),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/potassium_K.html
    'K'  : ElementDefinition(A = 39.0983, I = 1.9E-07, Z = 19),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/calcium_Ca.html
    'Ca' : ElementDefinition(A = 40.078, I = 1.91E-07, Z = 20),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/scandium_Sc.html
    'Sc' : ElementDefinition(A = 44.9559, I = 2.16E-07, Z = 21),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/titanium_Ti.html
    'Ti' : ElementDefinition(A = 47.867, I = 2.33E-07, Z = 22),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/vanadium_V.html
    'V'  : ElementDefinition(A = 50.9415, I = 2.45E-07, Z = 23),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/chromium_Cr.html
    'Cr' : ElementDefinition(A = 51.9961, I = 2.57E-07, Z = 24),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/manganese_Mn.html
    'Mn' : ElementDefinition(A = 54.938, I = 2.72E-07, Z = 25),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/iron_Fe.html
    'Fe' : ElementDefinition(A = 55.845, I = 2.86E-07, Z = 26),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/cobalt_Co.html
    'Co' : ElementDefinition(A = 58.9332, I = 2.97E-07, Z = 27),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/nickel_Ni.html
    'Ni' : ElementDefinition(A = 58.6934, I = 3.11E-07, Z = 28),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/copper_Cu.html
    'Cu' : ElementDefinition(A = 63.546, I = 3.22E-07, Z = 29),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/zinc_Zn.html
    'Zn' : ElementDefinition(A = 65.38, I = 3.3E-07, Z = 30),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/gallium_Ga.html
    'Ga' : ElementDefinition(A = 69.723, I = 3.34E-07, Z = 31),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/germanium_Ge.html
    'Ge' : ElementDefinition(A = 72.63, I = 3.5E-07, Z = 32),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/arsenic_As.html
    'As' : ElementDefinition(A = 74.9216, I = 3.47E-07, Z = 33),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/selenium_Se.html
    'Se' : ElementDefinition(A = 78.971, I = 3.48E-07, Z = 34),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/liquid_bromine.html
    'Br' : ElementDefinition(A = 79.904, I = 3.57E-07, Z = 35),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/krypton_gas_Kr.html
    'Kr' : ElementDefinition(A = 83.798, I = 3.52E-07, Z = 36),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/rubidium_Rb.html
    'Rb' : ElementDefinition(A = 85.4678, I = 3.63E-07, Z = 37),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/strontium_Sr.html
    'Sr' : ElementDefinition(A = 87.62, I = 3.66E-07, Z = 38),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/yttrium_Y.html
    'Y'  : ElementDefinition(A = 88.9058, I = 3.79E-07, Z = 39),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/zirconium_Zr.html
    'Zr' : ElementDefinition(A = 91.224, I = 3.93E-07, Z = 40),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/niobium_Nb.html
    'Nb' : ElementDefinition(A = 92.9064, I = 4.17E-07, Z = 41),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/molybdenum_Mo.html
    'Mo' : ElementDefinition(A = 95.95, I = 4.24E-07, Z = 42),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/technetium_Tc.html
    'Tc' : ElementDefinition(A = 97.9072, I = 4.28E-07, Z = 43),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/ruthenium_Ru.html
    'Ru' : ElementDefinition(A = 101.07, I = 4.41E-07, Z = 44),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/rhodium_Rh.html
    'Rh' : ElementDefinition(A = 102.906, I = 4.49E-07, Z = 45),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/palladium_Pd.html
    'Pd' : ElementDefinition(A = 106.42, I = 4.7E-07, Z = 46),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/silver_Ag.html
    'Ag' : ElementDefinition(A = 107.868, I = 4.7E-07, Z = 47),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/cadmium_Cd.html
    'Cd' : ElementDefinition(A = 112.414, I = 4.69E-07, Z = 48),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/indium_In.html
    'In' : ElementDefinition(A = 114.818, I = 4.88E-07, Z = 49),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/tin_Sn.html
    'Sn' : ElementDefinition(A = 118.71, I = 4.88E-07, Z = 50),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/antimony_Sb.html
    'Sb' : ElementDefinition(A = 121.76, I = 4.87E-07, Z = 51),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/tellurium_Te.html
    'Te' : ElementDefinition(A = 127.6, I = 4.85E-07, Z = 52),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/iodine_I.html
    'I'  : ElementDefinition(A = 126.904, I = 4.91E-07, Z = 53),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/xenon_gas_Xe.html
    'Xe' : ElementDefinition(A = 131.293, I = 4.82E-07, Z = 54),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/caesium_Cs.html
    'Cs' : ElementDefinition(A = 132.905, I = 4.88E-07, Z = 55),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/barium_Ba.html
    'Ba' : ElementDefinition(A = 137.327, I = 4.91E-07, Z = 56),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/lanthanum_La.html
    'La' : ElementDefinition(A = 138.905, I = 5.01E-07, Z = 57),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/cerium_Ce.html
    'Ce' : ElementDefinition(A = 140.116, I = 5.23E-07, Z = 58),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/praseodymium_Pr.html
    'Pr' : ElementDefinition(A = 140.908, I = 5.35E-07, Z = 59),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/neodymium_Nd.html
    'Nd' : ElementDefinition(A = 144.242, I = 5.46E-07, Z = 60),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/promethium_Pm.html
    'Pm' : ElementDefinition(A = 144.913, I = 5.6E-07, Z = 61),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/samarium_Sm.html
    'Sm' : ElementDefinition(A = 150.36, I = 5.74E-07, Z = 62),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/europium_Eu.html
    'Eu' : ElementDefinition(A = 151.964, I = 5.8E-07, Z = 63),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/gadolinium_Gd.html
    'Gd' : ElementDefinition(A = 157.25, I = 5.91E-07, Z = 64),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/terbium_Tb.html
    'Tb' : ElementDefinition(A = 158.925, I = 6.14E-07, Z = 65),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/dysprosium_Dy.html
    'Dy' : ElementDefinition(A = 162.5, I = 6.28E-07, Z = 66),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/holmium_Ho.html
    'Ho' : ElementDefinition(A = 164.93, I = 6.5E-07, Z = 67),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/erbium_Er.html
    'Er' : ElementDefinition(A = 167.259, I = 6.58E-07, Z = 68),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/thulium_Tm.html
    'Tm' : ElementDefinition(A = 168.934, I = 6.74E-07, Z = 69),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/ytterbium_Yb.html
    'Yb' : ElementDefinition(A = 173.054, I = 6.84E-07, Z = 70),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/lutetium_Lu.html
    'Lu' : ElementDefinition(A = 174.967, I = 6.94E-07, Z = 71),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/hafnium_Hf.html
    'Hf' : ElementDefinition(A = 178.49, I = 7.05E-07, Z = 72),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/tantalum_Ta.html
    'Ta' : ElementDefinition(A = 180.948, I = 7.18E-07, Z = 73),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/tungsten_W.html
    'W'  : ElementDefinition(A = 183.84, I = 7.27E-07, Z = 74),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/rhenium_Re.html
    'Re' : ElementDefinition(A = 186.207, I = 7.36E-07, Z = 75),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/osmium_Os.html
    'Os' : ElementDefinition(A = 190.23, I = 7.46E-07, Z = 76),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/iridium_Ir.html
    'Ir' : ElementDefinition(A = 192.217, I = 7.57E-07, Z = 77),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/platinum_Pt.html
    'Pt' : ElementDefinition(A = 195.084, I = 7.9E-07, Z = 78),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/gold_Au.html
    'Au' : ElementDefinition(A = 196.967, I = 7.9E-07, Z = 79),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/mercury_Hg.html
    'Hg' : ElementDefinition(A = 200.592, I = 8E-07, Z = 80),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/thallium_Tl.html
    'Tl' : ElementDefinition(A = 204.38, I = 8.1E-07, Z = 81),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/lead_Pb.html
    'Pb' : ElementDefinition(A = 207.2, I = 8.23E-07, Z = 82),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/bismuth_Bi.html
    'Bi' : ElementDefinition(A = 208.98, I = 8.23E-07, Z = 83),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/polonium_Po.html
    'Po' : ElementDefinition(A = 208.982, I = 8.3E-07, Z = 84),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/astatine_At.html
    'At' : ElementDefinition(A = 209.987, I = 8.25E-07, Z = 85),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/radon_Rn.html
    'Rn' : ElementDefinition(A = 222.018, I = 7.94E-07, Z = 86),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/francium_Fr.html
    'Fr' : ElementDefinition(A = 223.02, I = 8.27E-07, Z = 87),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/radium_Ra.html
    'Ra' : ElementDefinition(A = 226.025, I = 8.26E-07, Z = 88),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/actinium_Ac.html
    'Ac' : ElementDefinition(A = 227.028, I = 8.41E-07, Z = 89),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/thorium_Th.html
    'Th' : ElementDefinition(A = 232.038, I = 8.47E-07, Z = 90),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/protactinium_Pa.html
    'Pa' : ElementDefinition(A = 231.036, I = 8.78E-07, Z = 91),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/uranium_U.html
    'U'  : ElementDefinition(A = 238.029, I = 8.9E-07, Z = 92),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/neptunium_Np.html
    'Np' : ElementDefinition(A = 237.048, I = 9.02E-07, Z = 93),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/plutonium_Pu.html
    'Pu' : ElementDefinition(A = 244.064, I = 9.21E-07, Z = 94),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/americium_Am.html
    'Am' : ElementDefinition(A = 243.061, I = 9.34E-07, Z = 95),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/curium_Cm.html
    'Cm' : ElementDefinition(A = 247.07, I = 9.39E-07, Z = 96),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/berkelium_Bk.html
    'Bk' : ElementDefinition(A = 247.07, I = 9.52E-07, Z = 97),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/californium_Cf.html
    'Cf' : ElementDefinition(A = 251.08, I = 9.66E-07, Z = 98),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/einsteinium_Es.html
    'Es' : ElementDefinition(A = 252.083, I = 9.8E-07, Z = 99),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/fermium_Fm.html
    'Fm' : ElementDefinition(A = 257.095, I = 9.94E-07, Z = 100),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/mendelevium_Md.html
    'Md' : ElementDefinition(A = 258.098, I = 1.007E-06, Z = 101),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/nobelium_No.html
    'No' : ElementDefinition(A = 259.101, I = 1.02E-06, Z = 102),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/lawrencium_Lr.html
    'Lr' : ElementDefinition(A = 262.11, I = 1.034E-06, Z = 103),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/rutherfordium_Rf.html
    'Rf' : ElementDefinition(A = 267.122, I = 1.047E-06, Z = 104),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/dubnium_Db.html
    'Db' : ElementDefinition(A = 268.126, I = 1.061E-06, Z = 105),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/seaborgium_Sg.html
    'Sg' : ElementDefinition(A = 269.129, I = 1.074E-06, Z = 106),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/bohrium_Bh.html
    'Bh' : ElementDefinition(A = 270.133, I = 1.087E-06, Z = 107),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/hassium_Hs.html
    'Hs' : ElementDefinition(A = 269.134, I = 1.102E-06, Z = 108),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/meitnerium_Mt.html
    'Mt' : ElementDefinition(A = 278.156, I = 1.115E-06, Z = 109),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/darmstadtium_Ds.html
    'Ds' : ElementDefinition(A = 281.164, I = 1.129E-06, Z = 110),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/roentgenium_Rg.html
    'Rg' : ElementDefinition(A = 282.169, I = 1.143E-06, Z = 111),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/copernicium_Cn.html
    'Cn' : ElementDefinition(A = 285.177, I = 1.156E-06, Z = 112),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/nihonium_Nh.html
    'Nh' : ElementDefinition(A = 286.182, I = 1.171E-06, Z = 113),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/flerovium_Fl.html
    'Fl' : ElementDefinition(A = 289.19, I = 1.185E-06, Z = 114),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/moscovium_Mc.html
    'Mc' : ElementDefinition(A = 289.194, I = 1.199E-06, Z = 115),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/livermorium_Lv.html
    'Lv' : ElementDefinition(A = 293.204, I = 1.213E-06, Z = 116),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/tennessine_Ts.html
    'Ts' : ElementDefinition(A = 294.211, I = 1.227E-06, Z = 117),
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/oganesson_Og.html
    'Og' : ElementDefinition(A = 294.214, I = 1.242E-06, Z = 118),

    # Fictious Rockium element for Standard Rock
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/standardrock.html
    'Rk' : ElementDefinition(A = 22, I = 1.364E-07, Z = 11)
}
