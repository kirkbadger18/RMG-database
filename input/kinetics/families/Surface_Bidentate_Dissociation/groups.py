#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Bidentate_Dissociation/groups"
shortDesc = u""
longDesc = u"""
A bidentate species with a single bond dissociates. The reverse reaction is when two adsorbates, each with double-bonds or higher to the surface, come together and form a single bond between them (thereby reducing the bond orders to the surface).

 *1--*2             *1   +  *2
  |  |     ---->    ||       ||
~*3~~*4~~          ~*3~~ +  ~*4~~ 

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2)
so k should be in (1/s)
"""

template(reactants=["Combined"], products=["Adsorbate1", "Adsorbate2"], ownReverse=False)

reverse = "Surface_Bidentate_Association"

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['CHANGE_BOND', '*1', 1, '*3'],
    ['CHANGE_BOND', '*2', 1, '*4'],
])

entry(
    index = 1,
    label = "Combined",
    group =
"""
1 *1 R!H u0 c0 {2,[S]} {3,[S,D,T]}
2 *2 R!H u0 c0 {1,[S]} {4,[S,D,T]}
3 *3 Xo  u0 {1,[S,D,T]}
4 *4 Xo  u0 {2,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "N-C",
    group =
"""
1 *1 N u0  p1 c0 {2,S} {3,[S,D,T]}
2 *2 C u0 p0 c0 {1,S} {4,[S,D,T]}
3 *3 Xo u0 {1,[S,D,T]}
4 *4 Xo u0 {2,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "C-N",
    group =
"""
1 *1 C u0  p0 c0 {2,S} {3,[S,D,T]}
2 *2 N u0 p1 c0 {1,S} {4,[S,D,T]}
3 *3 Xo u0 {1,[S,D,T]}
4 *4 Xo u0 {2,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "R-N",
    group =
"""
1 *1 R!H u0 c0 {2,[S]} {3,[S,D,T]}
2 *2 N u0 p1 c0 {1,[S]} {4,[S,D,T]}
3 *3 Xo  u0 {1,[S,D,T]}
4 *4 Xo  u0 {2,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "N-R",
    group =
"""
1 *1 N u0 p1 c0 {2,[S]} {3,[S,D,T]}
2 *2 R!H u0 c0 {1,[S]} {4,[S,D,T]}
3 *3 Xo  u0 {1,[S,D,T]}
4 *4 Xo  u0 {2,[S,D,T]}
""",
    kinetics = None,
)

tree(
"""
L1: Combined
    L2: R-N
        L3: C-N
    L2: N-R
	L3: N-C
"""
)

