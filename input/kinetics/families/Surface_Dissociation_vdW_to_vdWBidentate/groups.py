#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_vdW_to_vdWBidentate/groups"
shortDesc = u""
longDesc = u"""
Surface bond fission of one vdW species into two distinct adsorbates. Atom *3 is vdW, but we leave that out of the graph.

 *4-*1--*2=*3                                *1-*2=*3      *4
     :                             ---->      |     :       |
   ~*5~    +   ~*6~~    +   ~*7~~           ~*5~  ~*6~ +  ~*7~


The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)
so k should be in (m2/mol/s)
"""

template(reactants=["Combined", "VacantSite1", "VacantSite2"], products=["Adsorbate1", "Adsorbate2"], ownReverse=False)

reverse = "Surface_Association_vdWBidentate_to_vdW"

reactantNum=3
productNum=2

recipe(actions=[
    ['CHANGE_BOND', '*1', 1, '*5'],
    ['BREAK_BOND', '*1', 1, '*4'],
    ['FORM_BOND', '*4', 1, '*7'],
    ['FORM_BOND', '*3', 1, '*6'],
    ['CHANGE_BOND', '*3', -1, '*6'],
])

entry(
    index = 1,
    label = "Combined",
    group =
"""
multiplicity [1]
1 *1 R!H u0 px c0 {2,S} {4,S}
2 *2 R!H u0 px c0 {1,S} {3,D}
3 *3 R   u0 px c0 {2,D}
4 *4 R   u0 px c0 {1,S}
5 *5 Xv  u0 p0 c0
""",
    kinetics = None,
)

entry(
    index = 2,
    label="VacantSite1",
    group =
"""
1 *6 Xv u0 p0 c0
""",
    kinetics = None,
)

entry(
    index = 3,
    label="VacantSite2",
    group =
"""
1 *7 Xv u0 p0 c0
""",
    kinetics = None,
)


tree(
"""
L1: Combined
L1: VacantSite1
L1: VacantSite2
"""
)

