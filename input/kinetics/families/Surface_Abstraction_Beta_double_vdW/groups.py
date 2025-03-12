#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction_Beta_double_vdW/groups"
shortDesc = u""
longDesc = u"""
Surface abstraction of one atom to another adsorbate. The bond fission occurs not at the binding atom, but in the beta position of the adsorbate, that is the bond between Atom *2 and *3 is broken.  The bond between *2 and *3 must be single. Atom *1 is bonded to the surface (*5). Two vdW species are formed. An example for this reaction is: COOH* + OH* = H2O* + CO2*.


 *1-*2--*3  *4            *1=*2   *3-*4
  |         |       ---->   :       :
~*5~ +    ~*6~~           ~*5~ +  ~*6~~

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)
so k should be in (m2/mol/s). 
"""

template(reactants=["Abstracting", "Donating"], products=["Adsorbate2","Adsorbate3"], ownReverse=False)

reverse = "Surface_Abstraction_reverse_Beta_vdW"

reactantNum=2
productNum=2

recipe(actions=[
    ['FORM_BOND', '*3', 1, '*4'],
    ['CHANGE_BOND', '*1', -1, '*5'],
    ['CHANGE_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*2', 1, '*3'],
    ['CHANGE_BOND', '*4',-1,'*6'],
])

entry(
    index = 1,
    label = "Donating",
    group =
"""
1 *1 R!H u0 px c0 {2,[S,D]} {4,S}
2 *2 R!H u0 px c0 {1,[S,D]} {3,S}
3 *3 R   u0 {2,S}
4 *5 Xo  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label="Abstracting",
    group =
"""
1 *6 Xo  u0 {2,S}
2 *4 R!H u0 px c0 {1,S}	
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "R-C-H",
    group =
"""
1 *1 R!H u0 px cx {2,[S,D]} {4,S}
2 *2 C   u0 px cx {1,[S,D]} {3,S}
3 *3 H   u0 {2,S}
4 *5 Xo  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "R-O-H",
    group =
"""
1 *1 R!H u0 px cx {2,S} {4,S}
2 *2 O   u0 px cx {1,S} {3,S}
3 *3 H   u0 {2,S}
4 *5 Xo  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "OH",
    group =
"""
1 *4 O   u0 p2 c0 {2,S} {3,S}
2    H   u0 {1,S}
3 *6 Xo  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "R-CH3",
    group =
"""
1 *1 R!H u0 px cx {2,S} {4,S}
2 *2 C   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 *3 H   u0 {2,S}
4 *5 Xo  u0 {1,S}
5    H   u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)



tree(
"""
L1: Abstracting
    L2: OH
L1: Donating
    L2: R-C-H
	    L3: R-CH3
    L2: R-O-H
"""
)

forbidden(
    label = "C",
    group =
"""
1 *1 R!H u0 px c0 {2,[S,D]} {4,S}
2 *2 R!H u0 px c0 {1,[S,D]} {3,S}
3 *3 C   u0 {2,S}
4 *5 Xo  u0 {1,S}
""",
)
