#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation/groups"
shortDesc = u""
longDesc = u"""
Surface bond fission of one species into two distinct adsorbates. Atom *1 is bonded to the surface (*3). The image below shows a single bond, but single, double, and triple are possible. What matters is that the bond between *1 and *2 must be single.
    # NOTE: we should probably include vdW, too!

 *1--*2                 *1     *2
  |            ---->    ||      |
~*3~ + ~*4~~           ~*3~ + ~*4~~


The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)
so k should be in (m2/mol/s)
"""

template(reactants=["Combined", "VacantSite"], products=["Adsorbate1", "Adsorbate2"], ownReverse=False)

reverse = "Surface_Association"

reactantNum=2
productNum=2

recipe(actions=[
    ['FORM_BOND', '*2', 1, '*4'],
    ['CHANGE_BOND', '*1', 1, '*3'],
    ['BREAK_BOND', '*1', 1, '*2']
])

entry(
    index = 1,
    label = "Combined",
    group =
"""
1 *1 R!H u0 c0 {2,S} {3,[S,D,T]}
2 *2 R   u0 c0 {1,S}
3 *3 Xo  u0 {1,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 2,
    label="VacantSite",
    group =
"""
1 *4 Xv u0
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "C",
    group =
"""
1 *1 C  u0 {2,S} {3,[S,D,T]}
2 *2 R  u0 {1,S}
3 *3 Xo u0 {1,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "O",
    group =
"""
1 *1 O  u0 {2,S} {3,S}
2 *2 R  u0 {1,S}
3 *3 Xo u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "C-H",
    group =
"""
1 *1 C   u0 {2,S} {3,[S,D,T]}
2 *2 H   u0 {1,S}
3 *3 Xo  u0 {1,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "C-O",
    group =
"""
1 *1 C   u0 {2,S} {3,[S,D,T]}
2 *2 O   u0 {1,S}
3 *3 Xo  u0 {1,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "O-H",
    group =
"""
1 *1 O   u0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3 *3 Xo  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "O-C",
    group =
"""
1 *1 O   u0 {2,S} {3,S}
2 *2 C   u0 {1,S}
3 *3 Xo  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "N",
    group =
"""
1 *1 N  u0 {2,S} {3,[S,D]}
2 *2 R  u0 {1,S}
3 *3 Xo u0 {1,[S,D]}
""",
    kinetics = None,
)

#entry(
#    index = 10,
#    label = "N-H2",
#    group =
#"""
#1 *1 N  u0 p1 {2,S} {3,S} {4,S}
#2 *2 H  u0    {1,S}
#3 *3 Xo u0    {1,S}
#4    H  u0    {1,S}
#""",
#    kinetics = None,
#)

entry(
    index = 11,
    label = "N-H",
    group =
"""
1 *1 N  u0 p1 {2,S} {3,[S,D]}
2 *2 H  u0    {1,S}
3 *3 Xo u0    {1,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "CH",
    group =
"""
1 *1 C   u0 {2,S} {3,T}
2 *2 H   u0 {1,S}
3 *3 Xo  u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "CH2",
    group =
"""
1 *1 C   u0 {2,S} {3,D} {4,S}
2 *2 H   u0 {1,S}
3 *3 Xo  u0 {1,D}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "CH3",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3 *3 Xo  u0 {1,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "C-OH",
    group =
"""
1 *1 C   u0 {2,S} {3,S}
2 *2 O   u0 {1,S} {4,S}
3 *3 Xo  u0 {1,S}
4    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "O-C=O",
    group =
"""
1 *1 O   u0 {2,S} {3,S}
2 *2 C   u0 {1,S} {4,D}
3 *3 Xo  u0 {1,S}
4    O   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "O-N",
    group =
"""
1 *1 O  u0 {2,S} {3,S}
2 *2 N  u0 {1,S}
3 *3 Xo u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "O-N=O",
    group =
"""
1 *1 O  u0 {2,S} {3,S}
2 *2 N  u0 {1,S} {4,D}
3 *3 Xo u0 {1,S}
4    O  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "N-N",
    group =
"""
1 *1 N  u0 {2,S} {3,[S,D]}
2 *2 N  u0 {1,S}
3 *3 Xo u0 {1,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "C-H_Bidentate",
    group =
"""
1 *1 C   u0 {2,S} {3,[S,D]} {4,[S,D]}
2 *2 H   u0 {1,S}
3 *3 Xo  u0 {1,[S,D]}
4    R!H u0 {1,[S,D]} {5,[S,D,T]}
5    Xo  u0 {4,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "C-C",
    group =
"""
1 *1 C   u0 {2,S} {3,[S,D,T]}
2 *2 C   u0 {1,S}
3 *3 Xo  u0 {1,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "CH2R",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3 *3 Xo  u0 {1,S}
4    H   u0 {1,S}
5    R!H u0 px cx {1,S}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "CHR",
    group =
"""
1 *1 C   u0 {2,S} {3,D} {4,S}
2 *2 H   u0 {1,S}
3 *3 Xo  u0 {1,D}
4    R!H u0 px cx {1,S}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "C-N",
    group =
"""
1 *1 C   u0 {2,S} {3,[S,D,T]}
2 *2 N   u0 {1,S}
3 *3 Xo  u0 {1,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "N-O",
    group =
"""
1 *1 N  u0 {2,S} {3,[S,D]}
2 *2 O  u0 {1,S}
3 *3 Xo u0 {1,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "N-C",
    group =
"""
1 *1 N  u0 {2,S} {3,[S,D]}
2 *2 C  u0 {1,S}
3 *3 Xo u0 {1,[S,D]}
""",
    kinetics = None,
)

tree(
"""
L1: Combined
    L2: C
        L3: C-H
            L4: CH
            L4: CH2
            L4: CH3
            L4: C-H_Bidentate
            L4: CH2R
            L4: CHR
        L3: C-O
            L4: C-OH
        L3: C-C
        L3: C-N
    L2: O
        L3: O-H
        L3: O-C
            L4: O-C=O
        L3: O-N
            L4: O-N=O
    L2: N
        L3: N-H
        L3: N-N
        L3: N-O
        L3: N-C
L1: VacantSite
"""
)

forbidden(
    label = "Surf_Atom",
    group =
"""
1 *1 R!H u0 c0 {2,S} {3,[S,D,T]}
2 *2 R   u0 c0 {1,S} {4,[S,D,T]}
3 *3 Xo  u0 {1,[S,D,T]}
4 Xo u0 {2,[S,D,T]}
""",
)

