#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_NO2/groups"
shortDesc = u""
longDesc = u"""
Surface bond fission of one species into two distinct adsorbates. Atom *1 is bonded to the surface (*3). The image below shows a single bond, but single, double, and triple are possible. What matters is that the bond between *1 and *2 must be single.
    # NOTE: we should probably include vdW, too!

*4--*1==*2               *5==*1p    *2
     |            ---->       |      ||
   ~*3~ + ~*5~~             ~*3~ + ~*5~~


The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)
so k should be in (m2/mol/s)
"""

template(reactants=["Combined", "VacantSite"], products=["Adsorbate1", "Adsorbate2"], ownReverse=False)

reverse = "Surface_Association_NO2"

reactantNum=2
productNum=2

recipe(actions=[
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['BREAK_BOND', '*1', 1, '*2'],
    ['FORM_BOND', '*2', 1, '*5'],
    ['CHANGE_BOND', '*2', 1, '*5'],
    ['CHANGE_BOND', '*1', 1, '*4'],
    ['LOSE_PAIR','*4','1'],
    ['GAIN_PAIR', '*1', '1'],
])

entry(
    index = 1,
    label = "Combined",
    group =
"""
1 *1 N u0 p0 cx {2,D} {3,S} {4,S}
2 *2 R!H u0 px c0 {1,D}
3 *3 Xo u0 p0 c0 {1,S}
4 *4 R!H u0 px cx {1,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label="VacantSite",
    group =
"""
1 *5 Xv u0 p0 c0
""",
    kinetics = None,
)

tree(
"""
L1: Combined
L1: VacantSite
"""
)