#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction_vdW_Bidentate_Beta/groups"
shortDesc = u""
longDesc = u"""
Surface abstraction of one atom to another adsorbate. The bond fission occurs not at the binding atom, but in the beta position of the adsorbate, that is the bond between Atom *2 and *3 is broken. Atom *1 is bonded to the surface (*5). The bond order between *1/*3 and the surface decreases. An example for this reaction is: COH* + CH2* = CO* + CH3*. The bond between *2 and *3 must be single.

    *4
     |
 *1-*2=*3          *7            *1=*2=*3    *7-*4
  |     :          ||      ---->              |
~*5~ +~*6~  +     ~*8~~           ~*5~  +   ~*8~~  + ~*6~

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)
so k should be in (m2/mol/s). 
"""

template(reactants=["Donating", "Abstracting"], products=["Adsorbate2","Adsorbate3", "VacantSite"], ownReverse=False)

reverse = "Surface_Abstraction_vdW_Bidentate_reverse_Beta"

reactantNum=2
productNum=3

recipe(actions=[
    ['FORM_BOND', '*4', 1, '*7'],
    ['CHANGE_BOND', '*7', -1, '*8'],
    ['CHANGE_BOND', '*1', -1, '*5'],
    ['CHANGE_BOND', '*1', 1, '*2'],
    ['CHANGE_BOND', '*3', 1, '*6'],
    ['BREAK_BOND', '*3', 1, '*6'],
    ['BREAK_BOND', '*2', 1, '*4'],
])

entry(
    index = 1,
    label = "Donating",
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

entry(
    index = 2,
    label="Abstracting",
    group =
"""
1 *8 Xo  u0 {2,[D,T,Q]}
2 *7 R!H u0 px c0 {1,[D,T,Q]}	
""",
    kinetics = None,
)

tree(
"""
L1: Abstracting
L1: Donating
"""
)