#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_Double_vdW/rules"
shortDesc = u""
longDesc = u"""
A vdW double bonded species dissociatively adsorbing to the surface with double
bonds.
"""

entry(
    index = 1,
    label = "AdsorbateVdW;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (1.0e13, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.44,
        E0 = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""Made up"""
)

entry(
    index = 2,
    label = "ON;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (2.62e18, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.567,
        E0 = (138, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""Made up"""
)

entry(
    index = 3,
    label = "NC;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (2.62e18, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.567,
        E0 = (138, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""Made up"""
)
