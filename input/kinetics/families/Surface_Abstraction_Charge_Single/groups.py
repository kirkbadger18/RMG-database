#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction/groups"
shortDesc = u""
longDesc = u"""
Two adsorbates react. One has a multiple bond to the surface, the other has a
single-bond to the surface and some functional group.
The functional group is transferred from the single
to the multiple-bonded species.
     *1  *4-*3[+]-*6[-]          *1-*4  *3=*6
     ||      ||           ---->   |      |
    ~*2~~ + ~*5~~               ~*2~ + ~*5~~
The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)
so k should be in (m2/mol/s)
"""

template(reactants=["Abstracting", "Donating"], products=["Abstracted", "Donated"], ownReverse=False)

reactantNum=2
productNum=2

recipe(actions=[
    ['FORM_BOND', '*1', 1, '*4'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['LOSE_PAIR','*6','1'],
    ['GAIN_PAIR', '*3', '1'],
    ['CHANGE_BOND', '*3', 1, '*6'],
    ['CHANGE_BOND', '*3', -1, '*5'],
])

entry(
    index = 1,
    label = "Abstracting",
    group =
"""
1 *1 R!H u0 px c0 {2,[D,T,Q]}
2 *2 Xo  u0 p0 c0 {1,[D,T,Q]}
""",
    kinetics = None,
)

entry(
    index = 2,
    label="Donating",
    group =
"""
1 *4 R u0 px c0 {2,S}
2 *3 N u0 p0 cx {1,S} {3,D} {4,S}
3 *5 Xo u0 p0 c0 {2,D}
4 *6 R u0 px cx {2,S}
""",
    kinetics = None,
)


tree(
"""
L1: Abstracting
L1: Donating
"""
)

forbidden(
    label = "Bidentate",
    group =
"""
1 *4 R u0 px c0 {2,S}
2 *3 N u0 p0 cx {1,S} {3,D} {4,S}
3 *5 Xo u0 p0 c0 {2,D}
4 *6 R u0 px cx {2,S}
5 Xo u0
""",
)

