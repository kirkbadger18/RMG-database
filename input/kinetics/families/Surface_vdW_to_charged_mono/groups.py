#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation/groups"
shortDesc = u""
longDesc = u"""
Surface bond fission of one species into two distinct adsorbates. Atom *1 is bonded to the surface (*3). The image below shows a single bond, but single, double, and triple are possible. What matters is that the bond between *1 and *2 must be single.
    # NOTE: we should probably include vdW, too!

 R*1==*2                 R*1 -*2
   :            ---->     ||      |
 ~*3~ + ~*4~~            ~*3~ + ~*4~~


The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)
so k should be in (m2/mol/s)
"""

template(reactants=["Combined"], products=["Adsorbate1"], ownReverse=False)

reverse = "Surface_charged_mono_to_vdw"

reactantNum=1
productNum=1

recipe(actions=[
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['CHANGE_BOND', '*1', 1, '*3'],
    ['CHANGE_BOND', '*1', 1, '*3'],
    ['GAIN_PAIR', '*2', 1],
    ['LOSE_PAIR', '*1', 1],
])

entry(
    index = 1,
    label = "Combined",
    group =
"""
1 *1 N u0 p1 cx {2,D} {4,S}
2 *2 R!H u0 px cx {1,D}
3 *3 Xv u0 p0 c0 
4 *4 R u0 px c0 {1,S}
""",
    kinetics = None,
)


tree(
"""
L1: Combined
"""
)
