#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_vdWBidentate/groups"
shortDesc = u""
longDesc = u"""
Surface bond fission of one species into two distinct adsorbates. Atom *1 is bonded to the surface (*3). The image below shows a single bond, but single, double, and triple are possible. What matters is that the bond between *1 and *2 must be single.
    # NOTE: we should probably include vdW, too!

 *1-*2=*3              *1     *2=*3
  |     :     ---->    ||      |
~*4~  ~*5~~           ~*4~ + ~*5~~


The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)
so k should be in (m2/mol/s)
"""

template(reactants=["Combined"], products=["Adsorbate1", "Adsorbate2"], ownReverse=False)

reverse = "Surface_Association_vdWBidentate"

reactantNum=1
productNum=2

recipe(actions=[
    ['CHANGE_BOND', '*1', 1, '*4'],
    ['BREAK_BOND', '*1', 1, '*2'],
    ['CHANGE_BOND', '*3', 1, '*5'],
    ['BREAK_BOND', '*3', 1, '*5'],
    ['FORM_BOND', '*2', 1, '*5'],
])

entry(
    index = 1,
    label = "Combined",
    group =
"""
1 *1 O   u0 p2 {2,S} {4,S}
2 *2 R!H u0 {1,S} {3,D}
3 *3 O   u0 p2 {2,D} {5,vdW}
4 *4 X  u0 {1,S}
5 *5 X  u0 {3,vdW}
""",
    kinetics = None,
)

tree(
"""
L1: Combined
"""
)
