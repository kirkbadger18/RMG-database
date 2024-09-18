#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Charged_Bidentate_Dissociation/groups"
shortDesc = u""
longDesc = u"""
A bidentate species with a single bond dissociates. The reverse reaction is when two adsorbates, each with double-bonds or higher to the surface, come together and form a single bond between them (thereby reducing the bond orders to the surface).

 *1--*2(+)-*3(-)          *1   +   *2=*3
  |  ||            ---->   ||       |
~*4~~*5~~                ~*4~~ +  ~*5~~ 

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2)
so k should be in (1/s)
"""

template(reactants=["Combined"], products=["Adsorbate1", "Adsorbate2"], ownReverse=False)

reverse = "Surface_Charged_Bidentate_Association"

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['CHANGE_BOND', '*1', 1, '*4'],
    ['CHANGE_BOND', '*2', -1, '*5'],
    ['CHANGE_BOND', '*2', 1, '*3'],
    ['LOSE_PAIR', '*3', 1],
    ['GAIN_PAIR', '*2', 1],
])

entry(
    index = 1,
    label = "Combined",
    group =
"""
1 *1 R!H u0 px c0 {2,[S]} {4,[S,D,T]}
2 *2 N u0 p0 cx {1,[S]} {5,[D]} {3,[S]}
3 *3 R!H u0 px cx {2,S}
4 *4 Xo u0 p0 c0 {1,[S,D,T]}
5 *5 Xo u0 p0 c0 {2,[D]}
""",
    kinetics = None,
)


tree(
"""
L1: Combined
"""
)

