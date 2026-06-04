#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_vdWBidentate_Beta/groups"
shortDesc = u""
longDesc = u"""
Surface bond fission of one species into two distinct adsorbates. Atom *1 is bonded to the surface (*3). The image below shows a single bond, but single, double, and triple are possible. What matters is that the bond between *1 and *2 must be single.
    # NOTE: we should probably include vdW, too!

    *4
     |
 *1-*2=*3           *1=*2=*3  *4
  |     :     ---->            |
~*5~  ~*6~~           ~*5~ + ~*6~~


The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)
so k should be in (m2/mol/s)
"""

template(reactants=["Combined"], products=["Adsorbate1", "Adsorbate2"], ownReverse=False)

reverse = "Surface_Association_vdWBidentate_Beta"

reactantNum=1
productNum=2

recipe(actions=[
    ['CHANGE_BOND', '*1', -1, '*5'],
    ['CHANGE_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*2', 1, '*4'],
    ['CHANGE_BOND', '*3', 1, '*6'],
    ['BREAK_BOND', '*3', 1, '*6'],
    ['FORM_BOND', '*4', 1, '*6'],
])

entry(
    index = 1,
    label = "Combined",
    group =
"""
1 *1 O   u0 p2 {2,S} {5,S}
2 *2 R!H u0 {1,S} {3,D} {4,S}
3 *3 O   u0 p2 {2,D} {6,vdW}
4 *4 R u0 {2,S}
5 *5 X  u0 {1,S}
6 *6 X  u0 {3,vdW}
""",
    kinetics = None,
)

tree(
"""
L1: Combined
"""
)
