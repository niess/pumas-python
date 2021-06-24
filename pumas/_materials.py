# Tabulated materials from the Particle Data Group (PDG)
# Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/index.html
from .definitions import MaterialDefinition

data = {

    # A-150 tissue-equivalent plastic
    # Category: biologicals
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/a-150_tissue-equivalent_plastic.html
    'A150TissueEquivalentPlastic' : MaterialDefinition(
        I = 6.51E-08, density = 1127, elements = {'O' : 0.052316,
        'N' : 0.035057, 'F' : 0.017422, 'H' : 0.101327, 'Ca' : 0.018378, 'C' : 0.775501}
    ),

    # Acetone
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/acetone.html
    'Acetone' : MaterialDefinition(
        I = 6.42E-08, density = 789.9,
        elements = {'H' : 0.104122, 'C' : 0.620405, 'O' : 0.275473}
    ),

    # Acetylene CHCH
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/acetylene_CHCH.html
    'Acetylene' : MaterialDefinition(
        I = 5.82E-08, density = 1.097,
        elements = {'C' : 0.922582, 'H' : 0.077418}
    ),

    # Polymethylmethacrylate acrylic
    # Category: polymers
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/polymethylmethacrylate_acrylic.html
    'Acrylic' : MaterialDefinition(
        I = 7.4E-08, density = 1190, elements = {'H' : 0.080538,
        'C' : 0.599848, 'O' : 0.319614}
    ),

    # Actinium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/actinium_Ac.html
    'Actinium' : MaterialDefinition(
        I = 8.41E-07, density = 10070, elements = {'Ac' : 1}
    ),

    # Adenine
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/adenine.html
    'Adenine' : MaterialDefinition(
        I = 7.14E-08, density = 1350, elements = {'H' : 0.037294,
        'C' : 0.44443, 'N' : 0.518275}
    ),

    # Adipose tissue ICRP
    # Category: biologicals
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/adipose_tissue_ICRP.html
    'AdiposeTissue' : MaterialDefinition(
        I = 6.32E-08, density = 920, elements = {'K' : 0.00032,
        'O' : 0.232333, 'S' : 0.00073, 'H' : 0.119477, 'P' : 0.00016, 'N' : 0.00797,
        'Zn' : 2E-05, 'C' : 0.63724, 'Na' : 0.0005, 'Mg' : 2E-05, 'Cl' : 0.00119,
        'Ca' : 2E-05, 'Fe' : 2E-05}
    ),

    # Ag halides in phot emulsion
    # Category: mixtures
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/ag_halides_in_phot_emulsion.html
    'AgHalidesInPhotEmulsion' : MaterialDefinition(
        I = 4.871E-07, density = 6470, elements = {'I' : 0.003357,
        'Br' : 0.422895, 'Ag' : 0.573748}
    ),

    # Air dry 1 atm
    # Category: mixtures
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/air_dry_1_atm.html
    'Air' : MaterialDefinition(
        I = 8.57E-08, density = 1.205,
        elements = {'Ar' : 0.012827, 'O' : 0.231781, 'C' : 0.000124, 'N' : 0.755267}
    ),

    # Alanine
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/alanine.html
    'Alanine' : MaterialDefinition(
        I = 7.19E-08, density = 1420, elements = {'O' : 0.359159,
        'H' : 0.07919, 'C' : 0.404439, 'N' : 0.157213}
    ),

    # Aluminum
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/aluminum_Al.html
    'Aluminum' : MaterialDefinition(
        I = 1.66E-07, density = 2699, elements = {'Al' : 1}
    ),

    # Aluminum oxide sapphire
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/aluminum_oxide_sapphire.html
    'AluminumOxideSapphire' : MaterialDefinition(
        I = 1.452E-07, density = 3970,
        elements = {'O' : 0.470749, 'Al' : 0.529251}
    ),

    # Amber
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/amber.html
    'Amber' : MaterialDefinition(
        I = 6.32E-08, density = 1100, elements = {'H' : 0.10593,
        'C' : 0.788973, 'O' : 0.105096}
    ),

    # Americium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/americium_Am.html
    'Americium' : MaterialDefinition(
        I = 9.34E-07, density = 13670, elements = {'Am' : 1}
    ),

    # Ammonia
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/ammonia.html
    'Ammonia' : MaterialDefinition(
        I = 5.37E-08, density = 0.826,
        elements = {'H' : 0.177547, 'N' : 0.822453}
    ),

    # Aniline
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/aniline.html
    'Aniline' : MaterialDefinition(
        I = 6.62E-08, density = 1023, elements = {'H' : 0.075759,
        'C' : 0.773838, 'N' : 0.150403}
    ),

    # Anthracene
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/anthracene.html
    'Anthracene' : MaterialDefinition(
        I = 6.95E-08, density = 1283, elements = {'C' : 0.94345,
        'H' : 0.05655}
    ),

    # Antimony
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/antimony_Sb.html
    'Antimony' : MaterialDefinition(
        I = 4.87E-07, density = 6691, elements = {'Sb' : 1}
    ),

    # Argon gas
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/argon_gas_Ar.html
    'ArgonGas' : MaterialDefinition(
        I = 1.88E-07, density = 1.662, elements = {'Ar' : 1}
    ),

    # Arsenic
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/arsenic_As.html
    'Arsenic' : MaterialDefinition(
        I = 3.47E-07, density = 5730, elements = {'As' : 1}
    ),

    # Astatine
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/astatine_At.html
    'Astatine' : MaterialDefinition(
        I = 8.25E-07, density = 14000, elements = {'At' : 1}
    ),

    # B-100 Bone-equivalent plastic
    # Category: biologicals
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/b-100_Bone-equivalent_plastic.html
    'B100BoneEquivalentPlastic' : MaterialDefinition(
        I = 8.59E-08, density = 1450, elements = {'O' : 0.032085,
        'N' : 0.0215, 'F' : 0.167411, 'H' : 0.065471, 'Ca' : 0.176589, 'C' : 0.536945}
    ),

    # Bakelite
    # Category: polymers
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/bakelite.html
    'Bakelite' : MaterialDefinition(
        I = 7.24E-08, density = 1250, elements = {'H' : 0.057441,
        'C' : 0.774591, 'O' : 0.167968}
    ),

    # Barium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/barium_Ba.html
    'Barium' : MaterialDefinition(
        I = 4.91E-07, density = 3500, elements = {'Ba' : 1}
    ),

    # Barium fluoride
    # Category: scintillators
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/barium_fluoride.html
    'BariumFluoride' : MaterialDefinition(
        I = 3.759E-07, density = 4893, elements = {'F' : 0.21672,
        'Ba' : 0.78328}
    ),

    # Barium sulfate
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/barium_sulfate.html
    'BariumSulfate' : MaterialDefinition(
        I = 2.857E-07, density = 4500,
        elements = {'O' : 0.274212, 'S' : 0.137368, 'Ba' : 0.58842}
    ),

    # Benzene
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/benzene.html
    'Benzene' : MaterialDefinition(
        I = 6.34E-08, density = 878.7,
        elements = {'C' : 0.922582, 'H' : 0.077418}
    ),

    # Berkelium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/berkelium_Bk.html
    'Berkelium' : MaterialDefinition(
        I = 9.52E-07, density = 9860, elements = {'Bk' : 1}
    ),

    # Beryllium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/beryllium_Be.html
    'Beryllium' : MaterialDefinition(
        I = 6.37E-08, density = 1848, elements = {'Be' : 1}
    ),

    # Beryllium oxide BeO
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/beryllium_oxide_BeO.html
    'BerylliumOxide' : MaterialDefinition(
        I = 9.32E-08, density = 3010, elements = {'Be' : 0.36032,
        'O' : 0.63968}
    ),

    # Bismuth
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/bismuth_Bi.html
    'Bismuth' : MaterialDefinition(
        I = 8.23E-07, density = 9747, elements = {'Bi' : 1}
    ),

    # Bismuth germanate BGO
    # Category: scintillators
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/bismuth_germanate_BGO.html
    'BismuthGermanate' : MaterialDefinition(
        I = 5.341E-07, density = 7130,
        elements = {'Bi' : 0.671054, 'O' : 0.154126, 'Ge' : 0.17482}
    ),

    # Bismuth silicate BSO
    # Category: scintillators
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/bismuth_silicate_BSO.html
    'BismuthSilicate' : MaterialDefinition(
        I = 5.192E-07, density = 7120,
        elements = {'Si' : 0.075759, 'O' : 0.172629, 'Bi' : 0.751613}
    ),

    # Blood ICRP
    # Category: biologicals
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/blood_ICRP.html
    'Blood' : MaterialDefinition(
        I = 7.52E-08, density = 1060, elements = {'K' : 0.00163,
        'O' : 0.759414, 'S' : 0.00185, 'H' : 0.101866, 'N' : 0.02964, 'P' : 0.00035,
        'Si' : 3E-05, 'Zn' : 1E-05, 'C' : 0.10002, 'Na' : 0.00185, 'Mg' : 4E-05,
        'Cl' : 0.00278, 'Ca' : 6E-05, 'Fe' : 0.00046}
    ),

    # Bohrium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/bohrium_Bh.html
    'Bohrium' : MaterialDefinition(
        I = 1.087E-06, density = 14000, elements = {'Bh' : 1}
    ),

    # Boron
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/boron_B.html
    'Boron' : MaterialDefinition(
        I = 7.6E-08, density = 2370, elements = {'B' : 1}
    ),

    # Boron carbide
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/boron_carbide.html
    'BoronCarbide' : MaterialDefinition(
        I = 8.47E-08, density = 2520, elements = {'B' : 0.78261,
        'C' : 0.21739}
    ),

    # Boron oxide
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/boron_oxide.html
    'BoronOxide' : MaterialDefinition(
        I = 9.96E-08, density = 1812, elements = {'B' : 0.310551,
        'O' : 0.689449}
    ),

    # Borosilicate glass Pyrex Corning 7740
    # Category: mixtures
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/borosilicate_glass_Pyrex_Corning_7740.html
    'BorosilicateGlass' : MaterialDefinition(
        I = 1.34E-07, density = 2230, elements = {'B' : 0.040061,
        'O' : 0.539564, 'Na' : 0.028191, 'Al' : 0.011644, 'Si' : 0.37722, 'K' : 0.003321}
    ),

    # Brain ICRP
    # Category: biologicals
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/brain_ICRP.html
    'Brain' : MaterialDefinition(
        I = 7.33E-08, density = 1030, elements = {'K' : 0.0031,
        'O' : 0.737723, 'S' : 0.00177, 'H' : 0.110667, 'P' : 0.00354, 'N' : 0.01328,
        'Zn' : 1E-05, 'C' : 0.12542, 'Na' : 0.00184, 'Mg' : 0.00015, 'Cl' : 0.00236,
        'Ca' : 9E-05, 'Fe' : 5E-05}
    ),

    # Bromine gas
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/bromine_gas.html
    'BromineGas' : MaterialDefinition(
        I = 3.43E-07, density = 7.072, elements = {'Br' : 1}
    ),

    # Butane
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/butane.html
    'Butane' : MaterialDefinition(
        I = 4.83E-08, density = 2.489,
        elements = {'C' : 0.826592, 'H' : 0.173408}
    ),

    # C-552 air-equivalent plastic
    # Category: biologicals
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/C-552_air-equivalent_plastic.html
    'C552AirEquivalentPlastic' : MaterialDefinition(
        I = 8.68E-08, density = 1760,
        elements = {'Si' : 0.003973, 'F' : 0.465209, 'H' : 0.02468, 'C' : 0.50161,
        'O' : 0.004527}
    ),

    # Cadmium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/cadmium_Cd.html
    'Cadmium' : MaterialDefinition(
        I = 4.69E-07, density = 8650, elements = {'Cd' : 1}
    ),

    # Cadmium telluride CdTe
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/cadmium_telluride_CdTe.html
    'CadmiumTelluride' : MaterialDefinition(
        I = 5.393E-07, density = 6200,
        elements = {'Te' : 0.531645, 'Cd' : 0.468355}
    ),

    # Cadmium tungstate
    # Category: scintillators
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/cadmium_tungstate.html
    'CadmiumTungstate' : MaterialDefinition(
        I = 4.683E-07, density = 7900,
        elements = {'O' : 0.177644, 'Cd' : 0.312027, 'W' : 0.510329}
    ),

    # Caesium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/caesium_Cs.html
    'Caesium' : MaterialDefinition(
        I = 4.88E-07, density = 1873, elements = {'Cs' : 1}
    ),

    # Calcium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/calcium_Ca.html
    'Calcium' : MaterialDefinition(
        I = 1.91E-07, density = 1550, elements = {'Ca' : 1}
    ),

    # Calcium carbonate
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/calcium_carbonate.html
    'CalciumCarbonate' : MaterialDefinition(
        I = 1.364E-07, density = 2800,
        elements = {'O' : 0.479554, 'C' : 0.120003, 'Ca' : 0.400443}
    ),

    # Calcium fluoride
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/calcium_fluoride.html
    'CalciumFluoride' : MaterialDefinition(
        I = 1.66E-07, density = 3180,
        elements = {'Ca' : 0.513341, 'F' : 0.486659}
    ),

    # Calcium oxide CaO
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/calcium_oxide_CaO.html
    'CalciumOxide' : MaterialDefinition(
        I = 1.761E-07, density = 3300,
        elements = {'Ca' : 0.714701, 'O' : 0.285299}
    ),

    # Calcium sulfate
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/calcium_sulfate.html
    'CalciumSulfate' : MaterialDefinition(
        I = 1.523E-07, density = 2960,
        elements = {'O' : 0.470095, 'S' : 0.235497, 'Ca' : 0.294408}
    ),

    # Calcium tungstate
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/calcium_tungstate.html
    'CalciumTungstate' : MaterialDefinition(
        I = 3.95E-07, density = 6062, elements = {'O' : 0.22227,
        'Ca' : 0.139202, 'W' : 0.638529}
    ),

    # Californium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/californium_Cf.html
    'Californium' : MaterialDefinition(
        I = 9.66E-07, density = 15100, elements = {'Cf' : 1}
    ),

    # Carbon amorphous
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/carbon_amorphous_C.html
    'CarbonAmorphous' : MaterialDefinition(
        I = 7.8E-08, density = 2000, elements = {'C' : 1}
    ),

    # Carbon compact
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/carbon_compact_C.html
    'CarbonCompact' : MaterialDefinition(
        I = 7.8E-08, density = 2265, elements = {'C' : 1}
    ),

    # Carbon gem diamond
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/carbon_gem_diamond.html
    'CarbonDiamond' : MaterialDefinition(
        I = 7.8E-08, density = 3520, elements = {'C' : 1}
    ),

    # Carbon dioxide gas
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/carbon_dioxide_gas.html
    'CarbonDioxideGas' : MaterialDefinition(
        I = 8.5E-08, density = 1.842, elements = {'C' : 0.272916,
        'O' : 0.727084}
    ),

    # Solid carbon dioxide dry ice
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/solid_carbon_dioxide_dry_ice.html
    'CarbonDioxideIce' : MaterialDefinition(
        I = 8.5E-08, density = 1563, elements = {'C' : 0.272916,
        'O' : 0.727084}
    ),

    # Carbon graphite
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/carbon_graphite_C.html
    'CarbonGraphite' : MaterialDefinition(
        I = 7.8E-08, density = 2210, elements = {'C' : 1}
    ),

    # Carbon tetrachloride
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/carbon_tetrachloride.html
    'CarbonTetrachloride' : MaterialDefinition(
        I = 1.663E-07, density = 1594,
        elements = {'C' : 0.078083, 'Cl' : 0.921917}
    ),

    # Carbon tetrafluoride
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/carbon_tetrafluoride.html
    'CarbonTetrafluoride' : MaterialDefinition(
        I = 1.15E-07, density = 3.78, elements = {'C' : 0.136548,
        'F' : 0.86345}
    ),

    # Cellulose
    # Category: polymers
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/cellulose.html
    'Cellulose' : MaterialDefinition(
        I = 7.76E-08, density = 1420, elements = {'H' : 0.062162,
        'C' : 0.444462, 'O' : 0.493376}
    ),

    # Cellulose acetate butyrate
    # Category: polymers
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/cellulose_acetate_butyrate.html
    'CelluloseAcetateButyrate' : MaterialDefinition(
        I = 7.46E-08, density = 1200, elements = {'H' : 0.067125,
        'C' : 0.545403, 'O' : 0.387472}
    ),

    # Cellulose nitrate
    # Category: polymers
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/cellulose_nitrate.html
    'CelluloseNitrate' : MaterialDefinition(
        I = 8.7E-08, density = 1490, elements = {'O' : 0.578212,
        'H' : 0.029216, 'C' : 0.271296, 'N' : 0.121276}
    ),

    # Ceric sulfate dosimeter solution
    # Category: biologicals
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/ceric_sulfate_dosimeter_solution.html
    'CericSulfateDosimeterSolution' : MaterialDefinition(
        I = 7.67E-08, density = 1030, elements = {'O' : 0.874976,
        'S' : 0.014627, 'N' : 0.0008, 'H' : 0.107596, 'Ce' : 0.002001}
    ),

    # Cerium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/cerium_Ce.html
    'Cerium' : MaterialDefinition(
        I = 5.23E-07, density = 6770, elements = {'Ce' : 1}
    ),

    # Cerium fluoride
    # Category: scintillators
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/cerium_fluoride.html
    'CeriumFluoride' : MaterialDefinition(
        I = 3.484E-07, density = 6160,
        elements = {'Ce' : 0.710847, 'F' : 0.289153}
    ),

    # Cesium fluoride CsF
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/cesium_fluoride_CsF.html
    'CesiumFluoride' : MaterialDefinition(
        I = 4.407E-07, density = 4115,
        elements = {'Cs' : 0.874931, 'F' : 0.125069}
    ),

    # Cesium iodide CsI
    # Category: scintillators
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/cesium_iodide_CsI.html
    'CesiumIodide' : MaterialDefinition(
        I = 5.531E-07, density = 4510, elements = {'I' : 0.488451,
        'Cs' : 0.511549}
    ),

    # Chlorine gas
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/chlorine_gas.html
    'ChlorineGas' : MaterialDefinition(
        I = 1.74E-07, density = 2.98, elements = {'Cl' : 1}
    ),

    # Chlorobenzene
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/chlorobenzene.html
    'Chlorobenzene' : MaterialDefinition(
        I = 8.91E-08, density = 1106, elements = {'H' : 0.044772,
        'C' : 0.640254, 'Cl' : 0.314974}
    ),

    # Chloroform
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/chloroform.html
    'Chloroform' : MaterialDefinition(
        I = 1.56E-07, density = 1483, elements = {'H' : 0.008443,
        'C' : 0.100613, 'Cl' : 0.890944}
    ),

    # Chromium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/chromium_Cr.html
    'Chromium' : MaterialDefinition(
        I = 2.57E-07, density = 7180, elements = {'Cr' : 1}
    ),

    # Cobalt
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/cobalt_Co.html
    'Cobalt' : MaterialDefinition(
        I = 2.97E-07, density = 8900, elements = {'Co' : 1}
    ),

    # Compact bone ICRU
    # Category: biologicals
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/compact_bone_ICRU.html
    'CompactBone' : MaterialDefinition(
        I = 9.19E-08, density = 1850, elements = {'Mg' : 0.002,
        'O' : 0.410016, 'S' : 0.002, 'N' : 0.027, 'C' : 0.278, 'H' : 0.063984, 'Ca' : 0.147,
        'P' : 0.07}
    ),

    # Copernicium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/copernicium_Cn.html
    'Copernicium' : MaterialDefinition(
        I = 1.156E-06, density = 14000, elements = {'Cn' : 1}
    ),

    # Copper
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/copper_Cu.html
    'Copper' : MaterialDefinition(
        I = 3.22E-07, density = 8960, elements = {'Cu' : 1}
    ),

    # Cortical bone ICRP
    # Category: biologicals
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/cortical_bone_ICRP.html
    'CorticalBone' : MaterialDefinition(
        I = 1.064E-07, density = 1850,
        elements = {'O' : 0.446096, 'S' : 0.00315, 'H' : 0.047234, 'P' : 0.10497,
        'Zn' : 0.0001, 'N' : 0.04199, 'Mg' : 0.0022, 'Ca' : 0.20993, 'C' : 0.14433}
    ),

    # Curium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/curium_Cm.html
    'Curium' : MaterialDefinition(
        I = 9.39E-07, density = 13510, elements = {'Cm' : 1}
    ),

    # Cyclohexane
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/cyclohexane.html
    'Cyclohexane' : MaterialDefinition(
        I = 5.64E-08, density = 779, elements = {'C' : 0.856289,
        'H' : 0.143711}
    ),

    # Darmstadtium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/darmstadtium_Ds.html
    'Darmstadtium' : MaterialDefinition(
        I = 1.129E-06, density = 14000, elements = {'Ds' : 1}
    ),

    # Deuterium gas
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/deuterium_gas.html
    'DeuteriumGas' : MaterialDefinition(
        I = 1.92E-08, density = 0.1677, elements = {'D' : 1}
    ),

    # Deuterium oxide liquid
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/deuterium_oxide_liquid.html
    'DeuteriumOxideLiquid' : MaterialDefinition(
        I = 7.97E-08, density = 1107, elements = {'D' : 0.201133,
        'O' : 0.798867}
    ),

    # 12-dichlorobenzene
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/12-dichlorobenzene.html
    'Dichlorobenzene' : MaterialDefinition(
        I = 1.065E-07, density = 1305,
        elements = {'H' : 0.027425, 'C' : 0.490233, 'Cl' : 0.482342}
    ),

    # Dichlorodiethyl ether
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/dichlorodiethyl_ether.html
    'DichlorodiethylEther' : MaterialDefinition(
        I = 1.033E-07, density = 1220,
        elements = {'O' : 0.111874, 'H' : 0.056381, 'C' : 0.335942, 'Cl' : 0.495802}
    ),

    # 12-dichloroethane
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/12-dichloroethane.html
    'Dichloroethane' : MaterialDefinition(
        I = 1.119E-07, density = 1235, elements = {'H' : 0.04074,
        'C' : 0.242746, 'Cl' : 0.716515}
    ),

    # Diethyl ether
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/diethyl_ether.html
    'DiethylEther' : MaterialDefinition(
        I = 6E-08, density = 713.8, elements = {'H' : 0.135978,
        'C' : 0.648171, 'O' : 0.215851}
    ),

    # Dimethyl sulfoxide
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/dimethyl_sulfoxide.html
    'DimethylSulfoxide' : MaterialDefinition(
        I = 9.86E-08, density = 1101, elements = {'O' : 0.204782,
        'H' : 0.077403, 'S' : 0.410348, 'C' : 0.307467}
    ),

    # Dubnium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/dubnium_Db.html
    'Dubnium' : MaterialDefinition(
        I = 1.061E-06, density = 14000, elements = {'Db' : 1}
    ),

    # Dysprosium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/dysprosium_Dy.html
    'Dysprosium' : MaterialDefinition(
        I = 6.28E-07, density = 8551, elements = {'Dy' : 1}
    ),

    # E-Glass
    # Category: mixtures
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/E-Glass.html
    'EGlass' : MaterialDefinition(
        I = 1.434E-07, density = 2610,
        elements = {'B' : 0.031058, 'O' : 0.488551, 'Mg' : 0.018094, 'Al' : 0.074093,
        'Ca' : 0.135793, 'Si' : 0.252411}
    ),

    # Einsteinium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/einsteinium_Es.html
    'Einsteinium' : MaterialDefinition(
        I = 9.8E-07, density = 14000, elements = {'Es' : 1}
    ),

    # Epotek-301-1
    # Category: mixtures
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/Epotek-301-1.html
    'EpoTek301' : MaterialDefinition(
        I = 7.67E-08, density = 1190, elements = {'O' : 0.231531,
        'H' : 0.069894, 'C' : 0.68964, 'N' : 0.008936}
    ),

    # Erbium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/erbium_Er.html
    'Erbium' : MaterialDefinition(
        I = 6.58E-07, density = 9026, elements = {'Er' : 1}
    ),

    # Ethane
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/ethane.html
    'Ethane' : MaterialDefinition(
        I = 4.54E-08, density = 1.263,
        elements = {'C' : 0.798885, 'H' : 0.201115}
    ),

    # Ethanol
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/ethanol.html
    'Ethanol' : MaterialDefinition(
        I = 6.29E-08, density = 789.3,
        elements = {'H' : 0.131269, 'C' : 0.521438, 'O' : 0.347294}
    ),

    # Ethyl cellulose
    # Category: polymers
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/ethyl_cellulose.html
    'EthylCellulose' : MaterialDefinition(
        I = 6.93E-08, density = 1130, elements = {'H' : 0.090027,
        'C' : 0.585182, 'O' : 0.324791}
    ),

    # Ethylene
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/ethylene.html
    'Ethylene' : MaterialDefinition(
        I = 5.07E-08, density = 1.175,
        elements = {'C' : 0.856289, 'H' : 0.143711}
    ),

    # Europium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/europium_Eu.html
    'Europium' : MaterialDefinition(
        I = 5.8E-07, density = 5244, elements = {'Eu' : 1}
    ),

    # Eye lens ICRP
    # Category: biologicals
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/eye_lens_ICRP.html
    'EyeLens' : MaterialDefinition(
        I = 7.33E-08, density = 1100, elements = {'O' : 0.653751,
        'H' : 0.099269, 'C' : 0.19371, 'N' : 0.05327}
    ),

    # Fermium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/fermium_Fm.html
    'Fermium' : MaterialDefinition(
        I = 9.94E-07, density = 14000, elements = {'Fm' : 1}
    ),

    # Ferric oxide
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/ferric_oxide.html
    'FerricOxide' : MaterialDefinition(
        I = 2.273E-07, density = 5200,
        elements = {'Fe' : 0.699433, 'O' : 0.300567}
    ),

    # Ferroboride FeB
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/ferroboride_FeB.html
    'Ferroboride' : MaterialDefinition(
        I = 2.61E-07, density = 7150, elements = {'B' : 0.162174,
        'Fe' : 0.837826}
    ),

    # Ferrous oxide FeO
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/ferrous_oxide_FeO.html
    'FerrousOxide' : MaterialDefinition(
        I = 2.486E-07, density = 5700,
        elements = {'Fe' : 0.777311, 'O' : 0.222689}
    ),

    # Ferrous sulfate dosimeter solution
    # Category: biologicals
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/ferrous_sulfate_dosimeter_solution.html
    'FerrousSulfateDosimeterSolution' : MaterialDefinition(
        I = 7.64E-08, density = 1024, elements = {'Fe' : 5.4E-05,
        'O' : 0.878636, 'S' : 0.012968, 'Na' : 2.2E-05, 'H' : 0.108259, 'N' : 2.7E-05,
        'Cl' : 3.4E-05}
    ),

    # Flerovium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/flerovium_Fl.html
    'Flerovium' : MaterialDefinition(
        I = 1.185E-06, density = 14000, elements = {'Fl' : 1}
    ),

    # Fluorine gas
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/fluorine_gas.html
    'FluorineGas' : MaterialDefinition(
        I = 1.15E-07, density = 1.58, elements = {'F' : 1}
    ),

    # Francium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/francium_Fr.html
    'Francium' : MaterialDefinition(
        I = 8.27E-07, density = 1870, elements = {'Fr' : 1}
    ),

    # Freon-12
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/Freon-12.html
    'Freon12' : MaterialDefinition(
        I = 1.43E-07, density = 1120, elements = {'F' : 0.314247,
        'C' : 0.099335, 'Cl' : 0.586418}
    ),

    # Freon-13
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/Freon-13.html
    'Freon13' : MaterialDefinition(
        I = 1.266E-07, density = 950, elements = {'F' : 0.545622,
        'C' : 0.114983, 'Cl' : 0.339396}
    ),

    # Freon-13b1
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/Freon-13b1.html
    'Freon13b1' : MaterialDefinition(
        I = 2.105E-07, density = 1500, elements = {'F' : 0.382749,
        'C' : 0.080659, 'Br' : 0.536592}
    ),

    # Freon-13i1
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/Freon-13i1.html
    'Freon13i1' : MaterialDefinition(
        I = 2.935E-07, density = 1800,
        elements = {'I' : 0.647767, 'F' : 0.290924, 'C' : 0.061309}
    ),

    # G10
    # Category: mixtures
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/G10.html
    'G10' : MaterialDefinition(
        I = 1.104E-07, density = 1800, elements = {'B' : 0.01864,
        'O' : 0.385764, 'H' : 0.275853, 'Si' : 0.151423, 'Mg' : 0.010842, 'Al' : 0.044453,
        'Ca' : 0.081496, 'C' : 0.003583, 'N' : 0.027945}
    ),

    # Gadolinium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/gadolinium_Gd.html
    'Gadolinium' : MaterialDefinition(
        I = 5.91E-07, density = 7901, elements = {'Gd' : 1}
    ),

    # Gadolinium oxysulfide
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/gadolinium_oxysulfide.html
    'GadoliniumOxysulfide' : MaterialDefinition(
        I = 4.933E-07, density = 7440,
        elements = {'O' : 0.084528, 'S' : 0.08469, 'Gd' : 0.830782}
    ),

    # Gadolinium silicate
    # Category: scintillators
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/gadolinium_silicate.html
    'GadoliniumSilicate' : MaterialDefinition(
        I = 4.054E-07, density = 6710,
        elements = {'Si' : 0.066462, 'Gd' : 0.744233, 'O' : 0.189305}
    ),

    # Gallium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/gallium_Ga.html
    'Gallium' : MaterialDefinition(
        I = 3.34E-07, density = 5904, elements = {'Ga' : 1}
    ),

    # Gallium arsenide GaAs
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/gallium_arsenide_GaAs.html
    'GalliumArsenide' : MaterialDefinition(
        I = 3.849E-07, density = 5310,
        elements = {'Ga' : 0.482019, 'As' : 0.517981}
    ),

    # Gel in photographic emulsion
    # Category: mixtures
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/gel_in_photographic_emulsion.html
    'GelInPhotographicEmulsion' : MaterialDefinition(
        I = 7.48E-08, density = 1291, elements = {'O' : 0.38064,
        'S' : 0.01088, 'N' : 0.11124, 'H' : 0.08118, 'C' : 0.41606}
    ),

    # Germanium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/germanium_Ge.html
    'Germanium' : MaterialDefinition(
        I = 3.5E-07, density = 5323, elements = {'Ge' : 1}
    ),

    # Glucose dextrose monohydrate
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/glucose_dextrose_monohydrate.html
    'Glucose' : MaterialDefinition(
        I = 7.72E-08, density = 1540, elements = {'H' : 0.071204,
        'C' : 0.363652, 'O' : 0.565144}
    ),

    # Glutamine
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/glutamine.html
    'Glutamine' : MaterialDefinition(
        I = 7.33E-08, density = 1460, elements = {'O' : 0.328427,
        'H' : 0.068965, 'C' : 0.410926, 'N' : 0.191681}
    ),

    # Glycerol
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/glycerol.html
    'Glycerol' : MaterialDefinition(
        I = 7.26E-08, density = 1261, elements = {'H' : 0.087554,
        'C' : 0.391262, 'O' : 0.521185}
    ),

    # Gold
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/gold_Au.html
    'Gold' : MaterialDefinition(
        I = 7.9E-07, density = 19320, elements = {'Au' : 1}
    ),

    # Guanine
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/guanine.html
    'Guanine' : MaterialDefinition(
        I = 7.5E-08, density = 1580, elements = {'O' : 0.105867,
        'H' : 0.033346, 'C' : 0.39738, 'N' : 0.463407}
    ),

    # Gypsum plaster of Paris
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/gypsum_plaster_of_Paris.html
    'GypsumPlasterOfParis' : MaterialDefinition(
        I = 1.297E-07, density = 2320,
        elements = {'H' : 0.023416, 'O' : 0.557572, 'Ca' : 0.232797, 'S' : 0.186215}
    ),

    # Hafnium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/hafnium_Hf.html
    'Hafnium' : MaterialDefinition(
        I = 7.05E-07, density = 13310, elements = {'Hf' : 1}
    ),

    # Hassium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/hassium_Hs.html
    'Hassium' : MaterialDefinition(
        I = 1.102E-06, density = 14000, elements = {'Hs' : 1}
    ),

    # Heavymet in ATLAS calorimeter
    # Category: mixtures
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/heavymet_in_ATLAS_calorimeter.html
    'HeavymetInATLASCalorimeter' : MaterialDefinition(
        I = 7.27E-07, density = 19300, elements = {'Ni' : 0.035,
        'Cu' : 0.015, 'W' : 0.95}
    ),

    # Heavymet in Rochester gamma stop
    # Category: mixtures
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/heavymet_in_Rochester_gamma_stop.html
    'HeavymetInRochesterGammaStop' : MaterialDefinition(
        I = 7.27E-07, density = 19300, elements = {'Ni' : 0.06,
        'Cu' : 0.04, 'W' : 0.9}
    ),

    # Helium gas
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/helium_gas_He.html
    'HeliumGas' : MaterialDefinition(
        I = 4.18E-08, density = 0.1663, elements = {'He' : 1}
    ),

    # Holmium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/holmium_Ho.html
    'Holmium' : MaterialDefinition(
        I = 6.5E-07, density = 8795, elements = {'Ho' : 1}
    ),

    # Hydrogen gas
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/hydrogen_gas.html
    'HydrogenGas' : MaterialDefinition(
        I = 1.92E-08, density = 0.08376, elements = {'H' : 1}
    ),

    # Indium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/indium_In.html
    'Indium' : MaterialDefinition(
        I = 4.88E-07, density = 7310, elements = {'In' : 1}
    ),

    # Iodine
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/iodine_I.html
    'Iodine' : MaterialDefinition(
        I = 4.91E-07, density = 4930, elements = {'I' : 1}
    ),

    # Iridium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/iridium_Ir.html
    'Iridium' : MaterialDefinition(
        I = 7.57E-07, density = 22420, elements = {'Ir' : 1}
    ),

    # Iron
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/iron_Fe.html
    'Iron' : MaterialDefinition(
        I = 2.86E-07, density = 7874, elements = {'Fe' : 1}
    ),

    # Krypton gas
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/krypton_gas_Kr.html
    'KryptonGas' : MaterialDefinition(
        I = 3.52E-07, density = 3.486, elements = {'Kr' : 1}
    ),

    # Lanthanum
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/lanthanum_La.html
    'Lanthanum' : MaterialDefinition(
        I = 5.01E-07, density = 6145, elements = {'La' : 1}
    ),

    # Lanthanum bromide
    # Category: scintillators
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/lanthanum_bromide.html
    'LanthanumBromide' : MaterialDefinition(
        I = 4.545E-07, density = 5290,
        elements = {'Br' : 0.633124, 'La' : 0.366875}
    ),

    # Lanthanum chloride
    # Category: scintillators
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/lanthanum_chloride.html
    'LanthanumChloride' : MaterialDefinition(
        I = 3.295E-07, density = 3860,
        elements = {'La' : 0.56635, 'Cl' : 0.43365}
    ),

    # Lanthanum fluoride
    # Category: scintillators
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/lanthanum_fluoride.html
    'LanthanumFluoride' : MaterialDefinition(
        I = 3.363E-07, density = 5900,
        elements = {'La' : 0.709061, 'F' : 0.290939}
    ),

    # Lanthanum oxybromide LaOBr
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/lanthanum_oxybromide_LaOBr.html
    'LanthanumOxybromide' : MaterialDefinition(
        I = 4.397E-07, density = 6280, elements = {'O' : 0.068138,
        'Br' : 0.340294, 'La' : 0.591568}
    ),

    # Lanthanum oxysulfide
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/lanthanum_oxysulfide.html
    'LanthanumOxysulfide' : MaterialDefinition(
        I = 4.212E-07, density = 5860, elements = {'O' : 0.0936,
        'S' : 0.093778, 'La' : 0.812622}
    ),

    # Lawrencium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/lawrencium_Lr.html
    'Lawrencium' : MaterialDefinition(
        I = 1.034E-06, density = 14000, elements = {'Lr' : 1}
    ),

    # Lead
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/lead_Pb.html
    'Lead' : MaterialDefinition(
        I = 8.23E-07, density = 11350, elements = {'Pb' : 1}
    ),

    # Lead fluoride
    # Category: scintillators
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/lead_fluoride.html
    'LeadFluoride' : MaterialDefinition(
        I = 6.354E-07, density = 7770,
        elements = {'Pb' : 0.845035, 'F' : 0.154965}
    ),

    # Lead glass
    # Category: mixtures
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/lead_glass.html
    'LeadGlass' : MaterialDefinition(
        I = 5.264E-07, density = 6220,
        elements = {'Si' : 0.080866, 'O' : 0.156453, 'Ti' : 0.008092, 'Pb' : 0.751938,
        'As' : 0.002651}
    ),

    # Lead oxide PbO
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/lead_oxide_PbO.html
    'LeadOxide' : MaterialDefinition(
        I = 7.667E-07, density = 9530,
        elements = {'Pb' : 0.928318, 'O' : 0.071682}
    ),

    # Lead tungstate
    # Category: scintillators
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/lead_tungstate.html
    'LeadTungstate' : MaterialDefinition(
        I = 6.007E-07, density = 8300,
        elements = {'Pb' : 0.455347, 'O' : 0.140462, 'W' : 0.404011}
    ),

    # Liquid argon
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/liquid_argon.html
    'LiquidArgon' : MaterialDefinition(
        I = 1.88E-07, density = 1396, elements = {'Ar' : 1}
    ),

    # Liquid bromine
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/liquid_bromine.html
    'LiquidBromine' : MaterialDefinition(
        I = 3.57E-07, density = 3103, elements = {'Br' : 1}
    ),

    # Liquid chlorine
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/liquid_chlorine.html
    'LiquidChlorine' : MaterialDefinition(
        I = 1.74E-07, density = 1574, elements = {'Cl' : 1}
    ),

    # Liquid deuterium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/liquid_deuterium.html
    'LiquidDeuterium' : MaterialDefinition(
        I = 2.18E-08, density = 163.8, elements = {'D' : 1}
    ),

    # Liquid fluorine
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/liquid_fluorine.html
    'LiquidFluorine' : MaterialDefinition(
        I = 1.15E-07, density = 1507, elements = {'F' : 1}
    ),

    # Liquid helium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/liquid_helium.html
    'LiquidHelium' : MaterialDefinition(
        I = 4.18E-08, density = 124.9, elements = {'He' : 1}
    ),

    # Liquid hydrogen
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/liquid_hydrogen.html
    'LiquidHydrogen' : MaterialDefinition(
        I = 2.18E-08, density = 70.8, elements = {'H' : 1}
    ),

    # Liquid krypton
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/liquid_krypton_Kr.html
    'LiquidKrypton' : MaterialDefinition(
        I = 3.52E-07, density = 2418, elements = {'Kr' : 1}
    ),

    # Liquid neon
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/liquid_neon.html
    'LiquidNeon' : MaterialDefinition(
        I = 1.37E-07, density = 1204, elements = {'Ne' : 1}
    ),

    # Liquid nitrogen
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/liquid_nitrogen.html
    'LiquidNitrogen' : MaterialDefinition(
        I = 8.2E-08, density = 807, elements = {'N' : 1}
    ),

    # Liquid oxygen
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/liquid_oxygen.html
    'LiquidOxygen' : MaterialDefinition(
        I = 9.5E-08, density = 1141, elements = {'O' : 1}
    ),

    # Liquid propane
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/liquid_propane.html
    'LiquidPropane' : MaterialDefinition(
        I = 5.2E-08, density = 493, elements = {'C' : 0.817145,
        'H' : 0.182855}
    ),

    # Liquid xenon
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/liquid_xenon_Xe.html
    'LiquidXenon' : MaterialDefinition(
        I = 4.82E-07, density = 2953, elements = {'Xe' : 1}
    ),

    # Lithium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/lithium_Li.html
    'Lithium' : MaterialDefinition(
        I = 4E-08, density = 534, elements = {'Li' : 1}
    ),

    # Lithium amide
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/lithium_amide.html
    'LithiumAmide' : MaterialDefinition(
        I = 5.55E-08, density = 1178, elements = {'H' : 0.087783,
        'Li' : 0.302262, 'N' : 0.609955}
    ),

    # Lithium carbonate
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/lithium_carbonate.html
    'LithiumCarbonate' : MaterialDefinition(
        I = 8.79E-08, density = 2110, elements = {'O' : 0.649579,
        'C' : 0.16255, 'Li' : 0.187871}
    ),

    # Lithium fluoride LiF
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/lithium_fluoride_LiF.html
    'LithiumFluoride' : MaterialDefinition(
        I = 9.4E-08, density = 2635, elements = {'Li' : 0.267585,
        'F' : 0.732415}
    ),

    # Lithium hydride LiH
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/lithium_hydride_LiH.html
    'LithiumHydride' : MaterialDefinition(
        I = 3.65E-08, density = 820, elements = {'H' : 0.126797,
        'Li' : 0.873203}
    ),

    # Lithium iodide LiI
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/lithium_iodide_LiI.html
    'LithiumIodide' : MaterialDefinition(
        I = 4.851E-07, density = 3494,
        elements = {'I' : 0.948142, 'Li' : 0.051858}
    ),

    # Lithium oxide
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/lithium_oxide.html
    'LithiumOxide' : MaterialDefinition(
        I = 7.36E-08, density = 2013, elements = {'Li' : 0.46457,
        'O' : 0.53543}
    ),

    # Lithium tetraborate
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/lithium_tetraborate.html
    'LithiumTetraborate' : MaterialDefinition(
        I = 9.46E-08, density = 2440, elements = {'B' : 0.25568,
        'O' : 0.662235, 'Li' : 0.082085}
    ),

    # Livermorium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/livermorium_Lv.html
    'Livermorium' : MaterialDefinition(
        I = 1.213E-06, density = 14000, elements = {'Lv' : 1}
    ),

    # Lung ICRP
    # Category: biologicals
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/lung_ICRP.html
    'Lung' : MaterialDefinition(
        I = 7.53E-08, density = 1050, elements = {'K' : 0.00194,
        'O' : 0.757072, 'S' : 0.00225, 'H' : 0.101278, 'P' : 0.0008, 'N' : 0.02865,
        'Zn' : 1E-05, 'C' : 0.10231, 'Na' : 0.00184, 'Mg' : 0.00073, 'Cl' : 0.00266,
        'Ca' : 9E-05, 'Fe' : 0.00037}
    ),

    # Lutetium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/lutetium_Lu.html
    'Lutetium' : MaterialDefinition(
        I = 6.94E-07, density = 9841, elements = {'Lu' : 1}
    ),

    # Lutetium aluminum oxide 1
    # Category: scintillators
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/lutetium_aluminum_oxide_1.html
    'LutetiumAluminumOxide1' : MaterialDefinition(
        I = 4.232E-07, density = 8300,
        elements = {'Al' : 0.107949, 'Lu' : 0.700017, 'O' : 0.192034}
    ),

    # Lutetium aluminum oxide 2
    # Category: scintillators
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/lutetium_aluminum_oxide_2.html
    'LutetiumAluminumOxide2' : MaterialDefinition(
        I = 3.659E-07, density = 6730,
        elements = {'Al' : 0.158379, 'Lu' : 0.616224, 'O' : 0.225396}
    ),

    # Lutetium fluoride
    # Category: scintillators
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/lutetium_fluoride.html
    'LutetiumFluoride' : MaterialDefinition(
        I = 4.587E-07, density = 8300,
        elements = {'Lu' : 0.754291, 'F' : 0.245709}
    ),

    # Lutetium silicon oxide
    # Category: scintillators
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/lutetium_silicon_oxide.html
    'LutetiumSiliconOxide' : MaterialDefinition(
        I = 4.72E-07, density = 7400, elements = {'Si' : 0.06132,
        'O' : 0.17466, 'Lu' : 0.76402}
    ),

    # M3 WAX
    # Category: biologicals
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/M3_WAX.html
    'M3Wax' : MaterialDefinition(
        I = 6.79E-08, density = 1050, elements = {'O' : 0.092183,
        'Mg' : 0.134792, 'H' : 0.114318, 'C' : 0.655823, 'Ca' : 0.002883}
    ),

    # Magnesium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/magnesium_Mg.html
    'Magnesium' : MaterialDefinition(
        I = 1.56E-07, density = 1740, elements = {'Mg' : 1}
    ),

    # Magnesium carbonate
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/magnesium_carbonate.html
    'MagnesiumCarbonate' : MaterialDefinition(
        I = 1.18E-07, density = 2958, elements = {'O' : 0.569278,
        'C' : 0.142455, 'Mg' : 0.288267}
    ),

    # Magnesium fluoride
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/magnesium_fluoride.html
    'MagnesiumFluoride' : MaterialDefinition(
        I = 1.343E-07, density = 3000, elements = {'F' : 0.609883,
        'Mg' : 0.390117}
    ),

    # Magnesium oxide MgO
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/magnesium_oxide_MgO.html
    'MagnesiumOxide' : MaterialDefinition(
        I = 1.438E-07, density = 3580,
        elements = {'O' : 0.396964, 'Mg' : 0.603036}
    ),

    # Magnesium tetraborate
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/magnesium_tetraborate.html
    'MagnesiumTetraborate' : MaterialDefinition(
        I = 1.083E-07, density = 2530,
        elements = {'B' : 0.240837, 'O' : 0.62379, 'Mg' : 0.135373}
    ),

    # Manganese
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/manganese_Mn.html
    'Manganese' : MaterialDefinition(
        I = 2.72E-07, density = 7440, elements = {'Mn' : 1}
    ),

    # Meitnerium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/meitnerium_Mt.html
    'Meitnerium' : MaterialDefinition(
        I = 1.115E-06, density = 14000, elements = {'Mt' : 1}
    ),

    # Mendelevium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/mendelevium_Md.html
    'Mendelevium' : MaterialDefinition(
        I = 1.007E-06, density = 14000, elements = {'Md' : 1}
    ),

    # Mercuric iodide
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/mercuric_iodide.html
    'MercuricIodide' : MaterialDefinition(
        I = 6.845E-07, density = 6360, elements = {'I' : 0.55856,
        'Hg' : 0.44144}
    ),

    # Mercury
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/mercury_Hg.html
    'Mercury' : MaterialDefinition(
        I = 8E-07, density = 13550, elements = {'Hg' : 1}
    ),

    # Methane
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/methane.html
    'Methane' : MaterialDefinition(
        I = 4.17E-08, density = 0.6672,
        elements = {'C' : 0.748694, 'H' : 0.251306}
    ),

    # Methanol
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/methanol.html
    'Methanol' : MaterialDefinition(
        I = 6.76E-08, density = 791.4, elements = {'H' : 0.125822,
        'C' : 0.374852, 'O' : 0.499326}
    ),

    # Mix D wax
    # Category: biologicals
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/mix_D_wax.html
    'MixDWax' : MaterialDefinition(
        I = 6.09E-08, density = 990, elements = {'O' : 0.03502,
        'Mg' : 0.038594, 'H' : 0.13404, 'C' : 0.77796, 'Ti' : 0.014386}
    ),

    # Mn-dimethyl formamide
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/mn-dimethyl_formamide.html
    'MnDimethylFormamide' : MaterialDefinition(
        I = 6.66E-08, density = 948.7,
        elements = {'O' : 0.218887, 'H' : 0.096523, 'C' : 0.492965, 'N' : 0.191625}
    ),

    # Molybdenum
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/molybdenum_Mo.html
    'Molybdenum' : MaterialDefinition(
        I = 4.24E-07, density = 10220, elements = {'Mo' : 1}
    ),

    # Moscovium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/moscovium_Mc.html
    'Moscovium' : MaterialDefinition(
        I = 1.199E-06, density = 14000, elements = {'Mc' : 1}
    ),

    # Ms20 tissue substitute
    # Category: biologicals
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/ms20_tissue_substitute.html
    'Ms20TissueSubstitute' : MaterialDefinition(
        I = 7.51E-08, density = 1000, elements = {'O' : 0.186381,
        'Mg' : 0.130287, 'N' : 0.017798, 'H' : 0.081192, 'C' : 0.583442, 'Cl' : 0.0009}
    ),

    # Muscle-equivalent liquid without sucrose
    # Category: biologicals
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/muscle-equivalent_liquid_without_sucrose.html
    'MuscleEquivalentLiquidWithoutSucrose' : MaterialDefinition(
        I = 7.42E-08, density = 1070, elements = {'O' : 0.742522,
        'H' : 0.101969, 'C' : 0.120058, 'N' : 0.035451}
    ),

    # Muscle-equivalent liquid with sucrose
    # Category: biologicals
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/muscle-equivalent_liquid_with_sucrose.html
    'MuscleEquivalentLiquidWithSucrose' : MaterialDefinition(
        I = 7.43E-08, density = 1110, elements = {'O' : 0.7101,
        'H' : 0.098234, 'C' : 0.156214, 'N' : 0.035451}
    ),

    # Polyethylene terephthalate Mylar
    # Category: polymers
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/polyethylene_terephthalate_Mylar.html
    'Mylar' : MaterialDefinition(
        I = 7.87E-08, density = 1400, elements = {'H' : 0.041959,
        'C' : 0.625017, 'O' : 0.333025}
    ),

    # Naphtalene
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/naphtalene.html
    'Naphtalene' : MaterialDefinition(
        I = 6.84E-08, density = 1145, elements = {'C' : 0.937091,
        'H' : 0.062909}
    ),

    # N-butyl alcohol
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/n-butyl_alcohol.html
    'NButylAlcohol' : MaterialDefinition(
        I = 5.99E-08, density = 809.8,
        elements = {'H' : 0.135978, 'C' : 0.648171, 'O' : 0.215851}
    ),

    # Neodymium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/neodymium_Nd.html
    'Neodymium' : MaterialDefinition(
        I = 5.46E-07, density = 7008, elements = {'Nd' : 1}
    ),

    # Neon gas
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/neon_gas_Ne.html
    'NeonGas' : MaterialDefinition(
        I = 1.37E-07, density = 0.8385, elements = {'Ne' : 1}
    ),

    # Neptunium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/neptunium_Np.html
    'Neptunium' : MaterialDefinition(
        I = 9.02E-07, density = 20250, elements = {'Np' : 1}
    ),

    # N-heptane
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/n-heptane.html
    'NHeptane' : MaterialDefinition(
        I = 5.44E-08, density = 683.8,
        elements = {'C' : 0.839063, 'H' : 0.160937}
    ),

    # N-hexane
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/n-hexane.html
    'NHexane' : MaterialDefinition(
        I = 5.4E-08, density = 660.3, elements = {'C' : 0.836259,
        'H' : 0.163741}
    ),

    # Nickel
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/nickel_Ni.html
    'Nickel' : MaterialDefinition(
        I = 3.11E-07, density = 8902, elements = {'Ni' : 1}
    ),

    # Nihonium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/nihonium_Nh.html
    'Nihonium' : MaterialDefinition(
        I = 1.171E-06, density = 14000, elements = {'Nh' : 1}
    ),

    # Niobium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/niobium_Nb.html
    'Niobium' : MaterialDefinition(
        I = 4.17E-07, density = 8570, elements = {'Nb' : 1}
    ),

    # Nitrobenzene
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/nitrobenzene.html
    'Nitrobenzene' : MaterialDefinition(
        I = 7.58E-08, density = 1199, elements = {'O' : 0.259918,
        'H' : 0.040935, 'C' : 0.585374, 'N' : 0.113773}
    ),

    # Nitrogen gas
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/nitrogen_gas.html
    'NitrogenGas' : MaterialDefinition(
        I = 8.2E-08, density = 1.165, elements = {'N' : 1}
    ),

    # Nitrous oxide
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/nitrous_oxide.html
    'NitrousOxide' : MaterialDefinition(
        I = 8.49E-08, density = 1.831,
        elements = {'N' : 0.636483, 'O' : 0.363517}
    ),

    # Nobelium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/nobelium_No.html
    'Nobelium' : MaterialDefinition(
        I = 1.02E-06, density = 14000, elements = {'No' : 1}
    ),

    # N-pentane
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/n-pentane.html
    'NPentane' : MaterialDefinition(
        I = 5.36E-08, density = 626.2,
        elements = {'C' : 0.832365, 'H' : 0.167635}
    ),

    # N-propyl alcohol
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/n-propyl_alcohol.html
    'NPropylAlcohol' : MaterialDefinition(
        I = 6.11E-08, density = 803.5,
        elements = {'H' : 0.134173, 'C' : 0.599595, 'O' : 0.266232}
    ),

    # Nylon du Pont Elvamide 8062M
    # Category: polymers
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/Nylon_du_Pont_Elvamide_8062M.html
    'NylonDuPontElvamide' : MaterialDefinition(
        I = 6.43E-08, density = 1080, elements = {'O' : 0.148539,
        'H' : 0.103509, 'C' : 0.648415, 'N' : 0.099536}
    ),

    # Nylon type 11 Rilsan
    # Category: polymers
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/Nylon_type_11_Rilsan.html
    'NylonType11Rilsan' : MaterialDefinition(
        I = 6.16E-08, density = 1425, elements = {'O' : 0.087289,
        'H' : 0.115476, 'C' : 0.720819, 'N' : 0.076417}
    ),

    # Nylon type 6-10
    # Category: polymers
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/Nylon_type_6-10.html
    'NylonType610' : MaterialDefinition(
        I = 6.32E-08, density = 1140, elements = {'O' : 0.1133,
        'H' : 0.107062, 'C' : 0.680449, 'N' : 0.099189}
    ),

    # Nylon type 6 6-6
    # Category: polymers
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/Nylon_type_6_6-6.html
    'NylonType666' : MaterialDefinition(
        I = 6.39E-08, density = 1180, elements = {'O' : 0.141389,
        'H' : 0.097976, 'C' : 0.636856, 'N' : 0.123779}
    ),

    # Octane
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/octane.html
    'Octane' : MaterialDefinition(
        I = 5.47E-08, density = 702.6,
        elements = {'C' : 0.841179, 'H' : 0.158821}
    ),

    # Oganesson
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/oganesson_Og.html
    'Oganesson' : MaterialDefinition(
        I = 1.242E-06, density = 12, elements = {'Og' : 1}
    ),

    # Osmium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/osmium_Os.html
    'Osmium' : MaterialDefinition(
        I = 7.46E-07, density = 22570, elements = {'Os' : 1}
    ),

    # Oxygen gas
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/oxygen_gas.html
    'OxygenGas' : MaterialDefinition(
        I = 9.5E-08, density = 1.332, elements = {'O' : 1}
    ),

    # Palladium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/palladium_Pd.html
    'Palladium' : MaterialDefinition(
        I = 4.7E-07, density = 12020, elements = {'Pd' : 1}
    ),

    # Paraffin
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/paraffin.html
    'Paraffin' : MaterialDefinition(
        I = 5.59E-08, density = 930, elements = {'C' : 0.851395,
        'H' : 0.148605}
    ),

    # Parylene
    # Category: polymers
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/parylene.html
    'Parylene' : MaterialDefinition(
        I = 6.6E-08, density = 1060, elements = {'C' : 0.922577,
        'H' : 0.077423}
    ),

    # Phosphorus
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/phosphorus_P.html
    'Phosphorus' : MaterialDefinition(
        I = 1.73E-07, density = 2200, elements = {'P' : 1}
    ),

    # Photographic emulsion
    # Category: mixtures
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/photographic_emulsion.html
    'PhotographicEmulsion' : MaterialDefinition(
        I = 3.31E-07, density = 3815, elements = {'I' : 0.00312,
        'O' : 0.066101, 'S' : 0.00189, 'N' : 0.01932, 'C' : 0.072261, 'H' : 0.0141,
        'Br' : 0.349103, 'Ag' : 0.474105}
    ),

    # Plate glass
    # Category: mixtures
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/plate_glass.html
    'PlateGlass' : MaterialDefinition(
        I = 1.454E-07, density = 2400,
        elements = {'Si' : 0.336553, 'O' : 0.4598, 'Ca' : 0.107205, 'Na' : 0.096441}
    ),

    # Platinum
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/platinum_Pt.html
    'Platinum' : MaterialDefinition(
        I = 7.9E-07, density = 21450, elements = {'Pt' : 1}
    ),

    # Plutonium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/plutonium_Pu.html
    'Plutonium' : MaterialDefinition(
        I = 9.21E-07, density = 19840, elements = {'Pu' : 1}
    ),

    # Plutonium dioxide
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/plutonium_dioxide.html
    'PlutoniumDioxide' : MaterialDefinition(
        I = 7.465E-07, density = 11460,
        elements = {'Pu' : 0.881945, 'O' : 0.118055}
    ),

    # Polonium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/polonium_Po.html
    'Polonium' : MaterialDefinition(
        I = 8.3E-07, density = 9320, elements = {'Po' : 1}
    ),

    # Polyacrylonitrile
    # Category: polymers
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/polyacrylonitrile.html
    'Polyacrylonitrile' : MaterialDefinition(
        I = 6.96E-08, density = 1170, elements = {'H' : 0.056983,
        'C' : 0.679056, 'N' : 0.263962}
    ),

    # Polycarbonate Lexan
    # Category: polymers
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/polycarbonate_Lexan.html
    'PolycarbonateLexan' : MaterialDefinition(
        I = 7.31E-08, density = 1200, elements = {'H' : 0.055491,
        'C' : 0.755751, 'O' : 0.188758}
    ),

    # Polychlorostyrene
    # Category: polymers
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/polychlorostyrene.html
    'Polychlorostyrene' : MaterialDefinition(
        I = 8.17E-08, density = 1300, elements = {'H' : 0.061869,
        'C' : 0.696325, 'Cl' : 0.241806}
    ),

    # Polyethylene
    # Category: polymers
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/polyethylene.html
    'Polyethylene' : MaterialDefinition(
        I = 5.74E-08, density = 890, elements = {'C' : 0.856289,
        'H' : 0.143711}
    ),

    # Polyimide film
    # Category: polymers
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/polyimide_film.html
    'PolyimideFilm' : MaterialDefinition(
        I = 7.96E-08, density = 1420, elements = {'O' : 0.209235,
        'H' : 0.026362, 'C' : 0.691133, 'N' : 0.07327}
    ),

    # Polyoxymethylene
    # Category: polymers
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/polyoxymethylene.html
    'Polyoxymethylene' : MaterialDefinition(
        I = 7.74E-08, density = 1425, elements = {'H' : 0.067135,
        'C' : 0.400017, 'O' : 0.532848}
    ),

    # Polypropylene
    # Category: polymers
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/polypropylene.html
    'Polypropylene' : MaterialDefinition(
        I = 5.74E-08, density = 905, elements = {'C' : 0.856289,
        'H' : 0.143711}
    ),

    # Polystyrene
    # Category: polymers
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/polystyrene.html
    'Polystyrene' : MaterialDefinition(
        I = 6.87E-08, density = 1060, elements = {'C' : 0.922582,
        'H' : 0.077418}
    ),

    # Polytrifluorochloroethylene
    # Category: polymers
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/polytrifluorochloroethylene.html
    'Polytrifluorochloroethylene' : MaterialDefinition(
        I = 1.207E-07, density = 2100,
        elements = {'F' : 0.489354, 'C' : 0.20625, 'Cl' : 0.304395}
    ),

    # Polyvinylacetate
    # Category: polymers
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/polyvinylacetate.html
    'Polyvinylacetate' : MaterialDefinition(
        I = 7.37E-08, density = 1190, elements = {'H' : 0.070245,
        'C' : 0.558066, 'O' : 0.371689}
    ),

    # Polyvinyl alcohol
    # Category: polymers
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/polyvinyl_alcohol.html
    'PolyvinylAlcohol' : MaterialDefinition(
        I = 6.97E-08, density = 1300, elements = {'H' : 0.091517,
        'C' : 0.545298, 'O' : 0.363185}
    ),

    # Polyvinyl butyral
    # Category: polymers
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/polyvinyl_butyral.html
    'PolyvinylButyral' : MaterialDefinition(
        I = 6.72E-08, density = 1120, elements = {'H' : 0.092802,
        'C' : 0.680561, 'O' : 0.226637}
    ),

    # Polyvinylidene chloride Saran
    # Category: polymers
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/polyvinylidene_chloride_Saran.html
    'PolyvinylideneChloride' : MaterialDefinition(
        I = 1.343E-07, density = 1700,
        elements = {'H' : 0.020793, 'C' : 0.247793, 'Cl' : 0.731413}
    ),

    # Polyvinylidene fluoride
    # Category: polymers
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/polyvinylidene_fluoride.html
    'PolyvinylideneFluoride' : MaterialDefinition(
        I = 8.88E-08, density = 1760, elements = {'H' : 0.03148,
        'C' : 0.375141, 'F' : 0.593379}
    ),

    # Polyvinyl pyrrolidone
    # Category: polymers
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/polyvinyl_pyrrolidone.html
    'PolyvinylPyrrolidone' : MaterialDefinition(
        I = 6.77E-08, density = 1250, elements = {'O' : 0.143953,
        'H' : 0.081616, 'C' : 0.648407, 'N' : 0.126024}
    ),

    # Polyvinyltoluene
    # Category: polymers
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/polyvinyltoluene.html
    'Polyvinyltoluene' : MaterialDefinition(
        I = 6.47E-08, density = 1032, elements = {'C' : 0.915,
        'H' : 0.085}
    ),

    # Potassium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/potassium_K.html
    'Potassium' : MaterialDefinition(
        I = 1.9E-07, density = 862, elements = {'K' : 1}
    ),

    # Potassium iodide KI
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/potassium_iodide_KI.html
    'PotassiumIodide' : MaterialDefinition(
        I = 4.319E-07, density = 3130,
        elements = {'K' : 0.235528, 'I' : 0.764472}
    ),

    # Potassium oxide
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/potassium_oxide.html
    'PotassiumOxide' : MaterialDefinition(
        I = 1.899E-07, density = 2320,
        elements = {'K' : 0.830148, 'O' : 0.169852}
    ),

    # Praseodymium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/praseodymium_Pr.html
    'Praseodymium' : MaterialDefinition(
        I = 5.35E-07, density = 6773, elements = {'Pr' : 1}
    ),

    # Promethium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/promethium_Pm.html
    'Promethium' : MaterialDefinition(
        I = 5.6E-07, density = 7264, elements = {'Pm' : 1}
    ),

    # Propane
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/propane.html
    'Propane' : MaterialDefinition(
        I = 4.71E-08, density = 1.868,
        elements = {'C' : 0.817145, 'H' : 0.182855}
    ),

    # Protactinium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/protactinium_Pa.html
    'Protactinium' : MaterialDefinition(
        I = 8.78E-07, density = 15370, elements = {'Pa' : 1}
    ),

    # Polyvinylchloride PVC
    # Category: polymers
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/polyvinylchloride_PVC.html
    'PVC' : MaterialDefinition(
        I = 1.082E-07, density = 1300, elements = {'H' : 0.04838,
        'C' : 0.38436, 'Cl' : 0.56726}
    ),

    # Pyridine
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/pyridine.html
    'Pyridine' : MaterialDefinition(
        I = 6.62E-08, density = 981.9, elements = {'H' : 0.06371,
        'C' : 0.759217, 'N' : 0.177073}
    ),

    # Radium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/radium_Ra.html
    'Radium' : MaterialDefinition(
        I = 8.26E-07, density = 5000, elements = {'Ra' : 1}
    ),

    # Radon
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/radon_Rn.html
    'Radon' : MaterialDefinition(
        I = 7.94E-07, density = 9.066, elements = {'Rn' : 1}
    ),

    # Rhenium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/rhenium_Re.html
    'Rhenium' : MaterialDefinition(
        I = 7.36E-07, density = 21020, elements = {'Re' : 1}
    ),

    # Rhodium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/rhodium_Rh.html
    'Rhodium' : MaterialDefinition(
        I = 4.49E-07, density = 12410, elements = {'Rh' : 1}
    ),

    # Roentgenium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/roentgenium_Rg.html
    'Roentgenium' : MaterialDefinition(
        I = 1.143E-06, density = 14000, elements = {'Rg' : 1}
    ),

    # Rubber butyl
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/rubber_butyl.html
    'RubberButyl' : MaterialDefinition(
        I = 5.65E-08, density = 920, elements = {'C' : 0.856289,
        'H' : 0.143711}
    ),

    # Rubber natural
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/rubber_natural.html
    'RubberNatural' : MaterialDefinition(
        I = 5.98E-08, density = 920, elements = {'C' : 0.881629,
        'H' : 0.118371}
    ),

    # Rubber neoprene
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/rubber_neoprene.html
    'RubberNeoprene' : MaterialDefinition(
        I = 9.3E-08, density = 1230, elements = {'H' : 0.05692,
        'C' : 0.542646, 'Cl' : 0.400434}
    ),

    # Rubidium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/rubidium_Rb.html
    'Rubidium' : MaterialDefinition(
        I = 3.63E-07, density = 1532, elements = {'Rb' : 1}
    ),

    # Ruthenium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/ruthenium_Ru.html
    'Ruthenium' : MaterialDefinition(
        I = 4.41E-07, density = 12410, elements = {'Ru' : 1}
    ),

    # Rutherfordium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/rutherfordium_Rf.html
    'Rutherfordium' : MaterialDefinition(
        I = 1.047E-06, density = 14000, elements = {'Rf' : 1}
    ),

    # Samarium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/samarium_Sm.html
    'Samarium' : MaterialDefinition(
        I = 5.74E-07, density = 7520, elements = {'Sm' : 1}
    ),

    # Scandium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/scandium_Sc.html
    'Scandium' : MaterialDefinition(
        I = 2.16E-07, density = 2989, elements = {'Sc' : 1}
    ),

    # Seaborgium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/seaborgium_Sg.html
    'Seaborgium' : MaterialDefinition(
        I = 1.074E-06, density = 14000, elements = {'Sg' : 1}
    ),

    # Selenium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/selenium_Se.html
    'Selenium' : MaterialDefinition(
        I = 3.48E-07, density = 4500, elements = {'Se' : 1}
    ),

    # Shielding concrete
    # Category: mixtures
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/shielding_concrete.html
    'ShieldingConcrete' : MaterialDefinition(
        I = 1.352E-07, density = 2300, elements = {'K' : 0.013,
        'O' : 0.529107, 'Al' : 0.033872, 'Si' : 0.337021, 'H' : 0.01, 'Mg' : 0.002,
        'C' : 0.001, 'Fe' : 0.014, 'Ca' : 0.044, 'Na' : 0.016}
    ),

    # Silica aerogel
    # Category: mixtures
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/silica_aerogel.html
    'SilicaAerogel' : MaterialDefinition(
        I = 1.392E-07, density = 200,
        elements = {'Si' : 0.453451, 'O' : 0.543192, 'H' : 0.003357}
    ),

    # Silicon
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/silicon_Si.html
    'Silicon' : MaterialDefinition(
        I = 1.73E-07, density = 2329, elements = {'Si' : 1}
    ),

    # Silicon dioxide fused quartz
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/silicon_dioxide_fused_quartz.html
    'SiliconDioxide' : MaterialDefinition(
        I = 1.392E-07, density = 2200,
        elements = {'Si' : 0.467435, 'O' : 0.532565}
    ),

    # Silver
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/silver_Ag.html
    'Silver' : MaterialDefinition(
        I = 4.7E-07, density = 10500, elements = {'Ag' : 1}
    ),

    # Silver bromide AgBr
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/silver_bromide_AgBr.html
    'SilverBromide' : MaterialDefinition(
        I = 4.866E-07, density = 6473,
        elements = {'Br' : 0.425537, 'Ag' : 0.574463}
    ),

    # Silver chloride AgCl
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/silver_chloride_AgCl.html
    'SilverChloride' : MaterialDefinition(
        I = 3.984E-07, density = 5560,
        elements = {'Cl' : 0.247368, 'Ag' : 0.752632}
    ),

    # Silver iodide AgI
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/silver_iodide_AgI.html
    'SilverIodide' : MaterialDefinition(
        I = 5.435E-07, density = 6010,
        elements = {'I' : 0.540542, 'Ag' : 0.459458}
    ),

    # Skeletal muscle ICRP
    # Category: biologicals
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/skeletal_muscle_ICRP.html
    'SkeletalMuscle' : MaterialDefinition(
        I = 7.53E-08, density = 1040, elements = {'K' : 0.00302,
        'O' : 0.754773, 'S' : 0.00241, 'H' : 0.100637, 'P' : 0.0018, 'N' : 0.02768,
        'Zn' : 5E-05, 'C' : 0.10783, 'Na' : 0.00075, 'Mg' : 0.00019, 'Cl' : 0.00079,
        'Ca' : 3E-05, 'Fe' : 4E-05}
    ),

    # Skin ICRP
    # Category: biologicals
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/skin_ICRP.html
    'Skin' : MaterialDefinition(
        I = 7.27E-08, density = 1100, elements = {'K' : 0.00085,
        'O' : 0.619002, 'S' : 0.00159, 'H' : 0.100588, 'P' : 0.00033, 'N' : 0.04642,
        'Zn' : 1E-05, 'C' : 0.22825, 'Na' : 7E-05, 'Mg' : 6E-05, 'Cl' : 0.00267,
        'Ca' : 0.00015, 'Fe' : 1E-05}
    ),

    # Sodium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/sodium_Na.html
    'Sodium' : MaterialDefinition(
        I = 1.49E-07, density = 971, elements = {'Na' : 1}
    ),

    # Sodium carbonate
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/sodium_carbonate.html
    'SodiumCarbonate' : MaterialDefinition(
        I = 1.25E-07, density = 2532, elements = {'O' : 0.452861,
        'C' : 0.113323, 'Na' : 0.433815}
    ),

    # Sodium chloride NaCl
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/sodium_chloride_NaCl.html
    'SodiumChloride' : MaterialDefinition(
        I = 1.753E-07, density = 2170,
        elements = {'Na' : 0.393375, 'Cl' : 0.606626}
    ),

    # Sodium iodide NaI
    # Category: scintillators
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/sodium_iodide_NaI.html
    'SodiumIodide' : MaterialDefinition(
        I = 4.52E-07, density = 3667, elements = {'I' : 0.846627,
        'Na' : 0.153373}
    ),

    # Sodium monoxide
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/sodium_monoxide.html
    'SodiumMonoxide' : MaterialDefinition(
        I = 1.488E-07, density = 2270,
        elements = {'O' : 0.258143, 'Na' : 0.741857}
    ),

    # Sodium nitrate
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/sodium_nitrate.html
    'SodiumNitrate' : MaterialDefinition(
        I = 1.146E-07, density = 2261, elements = {'O' : 0.56472,
        'N' : 0.164795, 'Na' : 0.270485}
    ),

    # Soft tissue ICRP
    # Category: biologicals
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/soft_tissue_ICRP.html
    'SoftTissue' : MaterialDefinition(
        I = 7.23E-08, density = 1000, elements = {'K' : 0.00199,
        'O' : 0.630238, 'S' : 0.00199, 'H' : 0.104472, 'P' : 0.00133, 'N' : 0.02488,
        'Zn' : 3E-05, 'C' : 0.23219, 'Na' : 0.00113, 'Mg' : 0.00013, 'Cl' : 0.00134,
        'Ca' : 0.00023, 'Fe' : 5E-05}
    ),

    # Soft tissue ICRU four-component
    # Category: biologicals
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/soft_tissue_ICRU_four-component.html
    'SoftTissueICRUFourComponent' : MaterialDefinition(
        I = 7.49E-08, density = 1000, elements = {'O' : 0.761828,
        'H' : 0.101172, 'C' : 0.111, 'N' : 0.026}
    ),

    # Standard rock
    # Category: mixtures
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/standard_rock.html
    'StandardRock' : MaterialDefinition(
        I = 1.364E-07, density = 2650, elements = {'Rk' : 1}
    ),

    # Stilbene
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/stilbene.html
    'Stilbene' : MaterialDefinition(
        I = 6.77E-08, density = 970.7,
        elements = {'C' : 0.932899, 'H' : 0.067101}
    ),

    # Striated muscle ICRU
    # Category: biologicals
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/striated_muscle_ICRU.html
    'StriatedMuscle' : MaterialDefinition(
        I = 7.47E-08, density = 1040, elements = {'K' : 0.005,
        'O' : 0.729003, 'S' : 0.005, 'H' : 0.101997, 'P' : 0.002, 'Na' : 0.0008,
        'N' : 0.035, 'C' : 0.123, 'Mg' : 0.0002}
    ),

    # Strontium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/strontium_Sr.html
    'Strontium' : MaterialDefinition(
        I = 3.66E-07, density = 2540, elements = {'Sr' : 1}
    ),

    # Sucrose
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/sucrose.html
    'Sucrose' : MaterialDefinition(
        I = 7.75E-08, density = 1581, elements = {'H' : 0.064779,
        'C' : 0.42107, 'O' : 0.514151}
    ),

    # Sulfur
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/sulfur_S.html
    'Sulfur' : MaterialDefinition(
        I = 1.8E-07, density = 2000, elements = {'S' : 1}
    ),

    # Tantalum
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/tantalum_Ta.html
    'Tantalum' : MaterialDefinition(
        I = 7.18E-07, density = 16650, elements = {'Ta' : 1}
    ),

    # Technetium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/technetium_Tc.html
    'Technetium' : MaterialDefinition(
        I = 4.28E-07, density = 11500, elements = {'Tc' : 1}
    ),

    # Polytetrafluoroethylene Teflon
    # Category: polymers
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/polytetrafluoroethylene_Teflon.html
    'Teflon' : MaterialDefinition(
        I = 9.91E-08, density = 2200, elements = {'C' : 0.240183,
        'F' : 0.759817}
    ),

    # Tellurium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/tellurium_Te.html
    'Tellurium' : MaterialDefinition(
        I = 4.85E-07, density = 6240, elements = {'Te' : 1}
    ),

    # Tennessine
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/tennessine_Ts.html
    'Tennessine' : MaterialDefinition(
        I = 1.227E-06, density = 14000, elements = {'Ts' : 1}
    ),

    # Terbium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/terbium_Tb.html
    'Terbium' : MaterialDefinition(
        I = 6.14E-07, density = 8230, elements = {'Tb' : 1}
    ),

    # Terphenyl
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/terphenyl.html
    'Terphenyl' : MaterialDefinition(
        I = 7.17E-08, density = 1234, elements = {'C' : 0.955457,
        'H' : 0.044543}
    ),

    # Testes ICRP
    # Category: biologicals
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/testes_ICRP.html
    'Testes' : MaterialDefinition(
        I = 7.5E-08, density = 1040, elements = {'K' : 0.00208,
        'O' : 0.773884, 'S' : 0.00146, 'H' : 0.104166, 'P' : 0.00125, 'N' : 0.01994,
        'Zn' : 2E-05, 'C' : 0.09227, 'Na' : 0.00226, 'Mg' : 0.00011, 'Cl' : 0.00244,
        'Ca' : 0.0001, 'Fe' : 2E-05}
    ),

    # Tetrachloroethylene
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/tetrachloroethylene.html
    'Tetrachloroethylene' : MaterialDefinition(
        I = 1.592E-07, density = 1625,
        elements = {'C' : 0.144856, 'Cl' : 0.855144}
    ),

    # Thallium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/thallium_Tl.html
    'Thallium' : MaterialDefinition(
        I = 8.1E-07, density = 11720, elements = {'Tl' : 1}
    ),

    # Thallium chloride TlCl
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/thallium_chloride_TlCl.html
    'ThalliumChloride' : MaterialDefinition(
        I = 6.903E-07, density = 7004,
        elements = {'Tl' : 0.852187, 'Cl' : 0.147822}
    ),

    # Thorium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/thorium_Th.html
    'Thorium' : MaterialDefinition(
        I = 8.47E-07, density = 11720, elements = {'Th' : 1}
    ),

    # Thulium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/thulium_Tm.html
    'Thulium' : MaterialDefinition(
        I = 6.74E-07, density = 9321, elements = {'Tm' : 1}
    ),

    # Tin
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/tin_Sn.html
    'Tin' : MaterialDefinition(
        I = 4.88E-07, density = 7310, elements = {'Sn' : 1}
    ),

    # Tissue-equivalent gas Methane based
    # Category: biologicals
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/tissue-equivalent_gas_Methane_based.html
    'TissueEquivalentGasMethaneBased' : MaterialDefinition(
        I = 6.12E-08, density = 1.064, elements = {'O' : 0.40678,
        'H' : 0.101869, 'C' : 0.456179, 'N' : 0.035172}
    ),

    # Tissue-equivalent gas Propane based
    # Category: biologicals
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/tissue-equivalent_gas_Propane_based.html
    'TissueEquivalentGasPropaneBased' : MaterialDefinition(
        I = 5.95E-08, density = 1.826,
        elements = {'O' : 0.293366, 'H' : 0.102672, 'C' : 0.56894, 'N' : 0.035022}
    ),

    # Titanium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/titanium_Ti.html
    'Titanium' : MaterialDefinition(
        I = 2.33E-07, density = 4540, elements = {'Ti' : 1}
    ),

    # Titanium dioxide
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/titanium_dioxide.html
    'TitaniumDioxide' : MaterialDefinition(
        I = 1.795E-07, density = 4260,
        elements = {'O' : 0.400592, 'Ti' : 0.599408}
    ),

    # Toluene
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/toluene.html
    'Toluene' : MaterialDefinition(
        I = 6.25E-08, density = 866.9, elements = {'C' : 0.91249,
        'H' : 0.08751}
    ),

    # Trichloroethylene
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/trichloroethylene.html
    'Trichloroethylene' : MaterialDefinition(
        I = 1.481E-07, density = 1460, elements = {'H' : 0.007671,
        'C' : 0.182831, 'Cl' : 0.809498}
    ),

    # Triethyl phosphate
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/triethyl_phosphate.html
    'TriethylPhosphate' : MaterialDefinition(
        I = 8.12E-08, density = 1070, elements = {'O' : 0.351334,
        'H' : 0.082998, 'C' : 0.395628, 'P' : 0.17004}
    ),

    # Tungsten
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/tungsten_W.html
    'Tungsten' : MaterialDefinition(
        I = 7.27E-07, density = 19300, elements = {'W' : 1}
    ),

    # Tungsten hexafluoride
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/tungsten_hexafluoride.html
    'TungstenHexafluoride' : MaterialDefinition(
        I = 3.544E-07, density = 2400,
        elements = {'F' : 0.382723, 'W' : 0.617277}
    ),

    # Uranium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/uranium_U.html
    'Uranium' : MaterialDefinition(
        I = 8.9E-07, density = 18950, elements = {'U' : 1}
    ),

    # Uranium dicarbide
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/uranium_dicarbide.html
    'UraniumDicarbide' : MaterialDefinition(
        I = 7.52E-07, density = 11280,
        elements = {'C' : 0.091669, 'U' : 0.908331}
    ),

    # Uranium monocarbide UC
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/uranium_monocarbide_UC.html
    'UraniumMonocarbide' : MaterialDefinition(
        I = 8.62E-07, density = 13630,
        elements = {'C' : 0.048036, 'U' : 0.951964}
    ),

    # Uranium oxide
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/uranium_oxide.html
    'UraniumOxide' : MaterialDefinition(
        I = 7.206E-07, density = 10960,
        elements = {'O' : 0.118502, 'U' : 0.881498}
    ),

    # Urea
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/urea.html
    'Urea' : MaterialDefinition(
        I = 7.28E-08, density = 1323, elements = {'O' : 0.266411,
        'H' : 0.067131, 'C' : 0.199999, 'N' : 0.466459}
    ),

    # Valine
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/valine.html
    'Valine' : MaterialDefinition(
        I = 6.77E-08, density = 1230, elements = {'O' : 0.27315,
        'H' : 0.094641, 'C' : 0.512645, 'N' : 0.119565}
    ),

    # Vanadium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/vanadium_V.html
    'Vanadium' : MaterialDefinition(
        I = 2.45E-07, density = 6110, elements = {'V' : 1}
    ),

    # Viton fluoroelastomer
    # Category: polymers
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/viton_fluoroelastomer.html
    'VitonFluoroelastomer' : MaterialDefinition(
        I = 9.86E-08, density = 1800, elements = {'H' : 0.009417,
        'C' : 0.280555, 'F' : 0.710028}
    ),

    # Water liquid
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/water_liquid.html
    'Water' : MaterialDefinition(
        I = 7.97E-08, density = 1000, elements = {'H' : 0.111894,
        'O' : 0.888106}
    ),

    # Water ice
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/water_ice.html
    'WaterIce' : MaterialDefinition(
        I = 7.97E-08, density = 918, elements = {'H' : 0.111894,
        'O' : 0.888106}
    ),

    # Water vapor
    # Category: inorganics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/water_vapor.html
    'WaterVapor' : MaterialDefinition(
        I = 7.16E-08, density = 0.7562,
        elements = {'H' : 0.111894, 'O' : 0.888106}
    ),

    # Xenon gas
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/xenon_gas_Xe.html
    'XenonGas' : MaterialDefinition(
        I = 4.82E-07, density = 5.483, elements = {'Xe' : 1}
    ),

    # Xylene
    # Category: organics
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/xylene.html
    'Xylene' : MaterialDefinition(
        I = 6.18E-08, density = 870, elements = {'C' : 0.905065,
        'H' : 0.094935}
    ),

    # Ytterbium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/ytterbium_Yb.html
    'Ytterbium' : MaterialDefinition(
        I = 6.84E-07, density = 6903, elements = {'Yb' : 1}
    ),

    # Yttrium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/yttrium_Y.html
    'Yttrium' : MaterialDefinition(
        I = 3.79E-07, density = 4469, elements = {'Y' : 1}
    ),

    # Yttrium aluminum oxide 1
    # Category: scintillators
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/yttrium_aluminum_oxide_1.html
    'YttriumAluminumOxide1' : MaterialDefinition(
        I = 2.393E-07, density = 5500,
        elements = {'Y' : 0.542487, 'Al' : 0.164636, 'O' : 0.292876}
    ),

    # Yttrium aluminum oxide 2
    # Category: scintillators
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/yttrium_aluminum_oxide_2.html
    'YttriumAluminumOxide2' : MaterialDefinition(
        I = 2.18E-07, density = 4560, elements = {'Y' : 0.449308,
        'Al' : 0.227263, 'O' : 0.323428}
    ),

    # Yttrium bromide
    # Category: scintillators
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/yttrium_bromide.html
    'YttriumBromide' : MaterialDefinition(
        I = 4.1E-07, density = 5290, elements = {'Y' : 0.270545,
        'Br' : 0.729455}
    ),

    # Yttrium silicon oxide
    # Category: scintillators
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/yttrium_silicon_oxide.html
    'YttriumSiliconOxide' : MaterialDefinition(
        I = 2.581E-07, density = 4540,
        elements = {'Y' : 0.621949, 'O' : 0.279813, 'Si' : 0.098237}
    ),

    # Zinc
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/zinc_Zn.html
    'Zinc' : MaterialDefinition(
        I = 3.3E-07, density = 7133, elements = {'Zn' : 1}
    ),

    # Zirconium
    # Category: elements
    # Ref: https://pdg.lbl.gov/2020/AtomicNuclearProperties/HTML/zirconium_Zr.html
    'Zirconium' : MaterialDefinition(
        I = 3.93E-07, density = 6506, elements = {'Zr' : 1}
    ),

}
