#!/usr/bin/env python
# encoding: utf-8

name = "local"
shortDesc = u""
longDesc = u"""
from Deutschmann CPOX, and Schneider Amoonia
"""

entry(
    index = 1,
    label = "H2 + Pt + Pt <=> HX + HX",
    kinetics = StickingCoefficient(
        A = 4.6E-2,
        n = 0,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        coverage_dependence = {'Pt': {'a': 0.0, 'm': -1.0, 'E': (0.0, 'J/mol')}},
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R1""",
	metal = "Pt",
)

entry(
    index = 2,
    label = "H2O + Pt <=> H2OX",
    kinetics = StickingCoefficient(
        A = 7.5E-1,
        n = 0,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R6. H2OX is vdW H2O.""",
	metal = "Pt",
)

entry(
    index = 3,
    label = "CO2 + Pt <=> CO2X",
    kinetics = StickingCoefficient(
        A = 5.0E-3,
        n = 0,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R7. H2OX is vdW CO2.""",
	metal = "Pt",
)

entry(
   index = 4,
   label = "OX + OX <=> Pt + Pt + O2",
   kinetics = SurfaceArrhenius(
       A=(3.7E17, 'm^2/(mol*s)'),
       n = 0,
       Ea=(278700.0, 'J/mol'),
       Tmin = (200, 'K'),
       Tmax = (3000, 'K'),
       coverage_dependence = {'OX': {'a': 0.0, 'm': 0.0, 'E': (-188280, 'J/mol')}},
   ),
   shortDesc = u"""Default""",
   longDesc = u"""R10. Ea raised from 235.5 to 278.7 kJ/mol to match
   endothermicity of reaction.""",
   metal = "Pt",
)

entry(
   index = 5,
   label = "OCX <=> CO + Pt",
   kinetics = SurfaceArrhenius(
       A=(1.0E11, '1/s'),
       n = 0,
       Ea=(169500.0, 'J/mol'),
       Tmin = (200, 'K'),
       Tmax = (3000, 'K'),
       coverage_dependence = {'OCX': {'a': 0.0, 'm': 0.0, 'E': (-33000, 'J/mol')}},
   ),
   shortDesc = u"""Default""",
   longDesc = u"""R12. Ea raised from 146.0 to 169.5 kJ/mol to match
   endothermicity of reaction.""",
   metal = "Pt",
)

entry(
   index = 6,
   label = "CH3X + HX <=> CH4 + Pt + Pt",
   kinetics = SurfaceArrhenius(
       A=(3.3E21, 'cm^2/(mol*s)'),
       n = 0,
       Ea=(50000, 'J/mol'),
       Tmin = (200, 'K'),
       Tmax = (3000, 'K'),
       coverage_dependence = {'HX': {'a': 0.0, 'm': 0.0, 'E': (-28000, 'J/mol')}},
   ),
   shortDesc = u"""Default""",
   longDesc = u"""R34""",
   metal = "Pt",
)

entry(
    index = 7,
    label = "N_X + N_X <=> N2 + Pt + Pt",
    kinetics = SurfaceArrhenius(
        A = (3.71E20, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (244119.7, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""N2 Surface_Adsorption_Dissociative""",
    longDesc = u"""
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 9.2E12(1/s)/2.483E-9(mol/cm^2) = 3.71E21 cm^2/(mol*s)
revised A from 3.71E21 to 3.71E20 based on the ammonia model

Ea = 2.53eV = 244119.7J/mol

This is R11 in Table S2 and S4
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 8,
    label = "NO_X <=> NO + Pt",
    kinetics = SurfaceArrhenius(
        A = (2.6E17, '1/s'),   
        n = 0.0,
        Ea = (184295.9, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

Ea = 1.91eV = 184295.9J/mol

This is R13 in Table S2 and S4
""",
    metal = "Pt",
    facet = "111",
)

