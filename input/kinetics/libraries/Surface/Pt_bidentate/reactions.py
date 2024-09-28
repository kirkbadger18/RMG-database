#!/usr/bin/env python
# encoding: utf-8

name = "Pt111"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 1,
    label = "h-CCX <=> CX + CX",
    kinetics = SurfaceArrhenius(
        A=(4.22E12, '1/s'),
        n = 0.0,
        Ea=(104, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""DFT value from Katrin Blondal"""
)

entry(
    index = 2,
    label = "h-C2HX <=> CHX + CX",
    kinetics = SurfaceArrhenius(
        A=(1.3e12, '1/s'),
        n = 0,
        Ea=(77, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""DFT value from Katrin Blondal"""
)

entry(
    index = 3,
    label = "h-C2H2X <=> CHX + CHX",
    kinetics = SurfaceArrhenius(
        A=(7.93e12, '1/s'),
        n = 0,
        Ea=(90, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""DFT value from Katrin Blondal"""
)


entry(
    index = 4,
    label = "h-C2H3X <=> CHX + CH2X",
    kinetics = SurfaceArrhenius(
        A=(2.74e13, '1/s'),
        n = 0,
        Ea=(140, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""DFT value from Katrin Blondal"""
)


entry(
    index = 5,
    label = "CH2X + CH2X <=> h-C2H4X",
    kinetics = SurfaceArrhenius(
        A=(9.89e23, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(154, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""DFT value from Katrin Blondal, implemented in reverse since it is endothermic according to RMG"""
)

entry(
    index = 6,
    label = "h-C2H2X + HX <=> h-C2H3X + Pt",
    kinetics = SurfaceArrhenius(
        A=(3.68e21, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(76, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""DFT value from Katrin Blondal, implemented in reverse since it is endothermic according to RMG"""
)

entry(
    index = 7,
    label = "h-C2H3X + HX <=> h-C2H4X + Pt",
    kinetics = SurfaceArrhenius(
        A=(6.21e21, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(63, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""DFT value from Katrin Blondal, implemented in reverse since it is endothermic according to RMG"""
)

entry(
    index = 8,
    label = "h-C2HX + HX <=> h-CCH2X + Pt",
    kinetics = SurfaceArrhenius(
        A=(5.19e19, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(34, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value, implemented in reverse since it is endothermic according to RMG"""
)

entry(
    index = 9,
    label = "h-C2HX + HX <=> h-C2H2X + Pt",
    kinetics = SurfaceArrhenius(
        A=(3.32e21, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(62, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value, implemented in reverse since it is endothermic according to RMG"""
)


entry(
    index = 12,
    label = "h-C2H3X + Pt <=> h-CCH2X + HX",
    kinetics = SurfaceArrhenius(
        A=(9.69e21, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(48, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)


entry(
    index = 13,
    label = "CH2CH3X + Pt + Pt <=> h-C2H4X + HX",
    kinetics = SurfaceArrhenius(
        A=(1.67e30, 'cm^4/(mol^2*s)'),
        n = 0,
        Ea=(46, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""DFT value from Katrin Blondal"""
)


entry(
    index = 14,
    label = "CHCH3X + Pt + Pt  <=>  h-C2H3X + HX",
    kinetics = SurfaceArrhenius(
        A=(1.95e30, 'cm^4/(mol^2*s)'),
        n = 0,
        Ea=(49, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""DFT value from Katrin Blondal"""
)

entry(
    index = 15,
    label = "CCH3X + Pt + Pt <=> h-CCH2X + HX",
    kinetics = SurfaceArrhenius(
        A=(1.07E+30, 'cm^4/(mol^2*s)'),
        n = 0,
        Ea=(103, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value, it is endothermic, but kept in this direction, since we are going to switch it later afterwards due to the coverage dependence of CCH3"""
)

entry(
    index = 16,
    label = "C2H2X + Pt <=> h-C2H2X",
    kinetics = SurfaceArrhenius(
        A=(5.0E21, 'cm^2/(mol*s)'),
        n = 0.0,
        Ea=(0.0, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""Barrierless according to DFT calculations by Katrin Blondal"""
)

entry(
    index = 17,
    label = "C2H4X + Pt <=> h-C2H4X",
    kinetics = SurfaceArrhenius(
        A=(1.78E21, 'cm^2/(mol*s)'),
        n = 0.0,
        Ea=(12, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""DFT value from Katrin Blondal"""
)

entry(
    index = 18,
    label = "C2H2 + Pt + Pt <=> h-C2H2X",
    kinetics = StickingCoefficient(
        A=0.0083,
        n =0,
        Ea=(0.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""Experimental value with single-crystal adsorption calorimetry (SCAC) for #initial sticking probability:
    "Energetics and kinetics of the interaction of acetylene and ethylene with Pd{100} and #Ni{100}"
    Vattuone et al
    Surface Science, 2000, 447, 1-14""",
)

