#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_Triple/groups"
shortDesc = u""
longDesc = u"""
Surface bond fission of one species into two distinct adsorbates. Atom *1 is bonded to the surface (*3). The image below shows a single bond, but single, double, and triple are possible. What matters is that the bond between *1 and *2 must be single.
    # NOTE: we should probably include vdW, too!

 *1##*2                 *1     *2
  |            ---->   ||||    |||
~*3~ + ~*4~~           ~*3~ + ~*4~~


The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)
so k should be in (m2/mol/s)
"""

template(reactants=["Combined", "VacantSite"], products=["Adsorbate1", "Adsorbate2"], ownReverse=False)

reverse = "Surface_Association_Triple"

reactantNum=2
productNum=2

recipe(actions=[
 
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['BREAK_BOND', '*1', 1, '*2'],
    
    ['CHANGE_BOND', '*1', 1, '*3'],
    ['CHANGE_BOND', '*1', 1, '*3'],
    ['CHANGE_BOND', '*1', 1, '*3'],
    
    ['FORM_BOND', '*2', 1, '*4'],
    ['CHANGE_BOND', '*2', 1, '*4'],
    ['CHANGE_BOND', '*2', 1, '*4'],
   

    ])

entry(
    index = 1,
    label = "Combined",
    group =
"""
1 *1 R!H u0 px c0 {3,[S]} {2,[T]}
2 *2 R!H u0 px c0 {1,[T]}
3 *3 Xo u0 {1,[S]}
""",
    kinetics = None,
)

entry(
    index = 2,
    label="VacantSite",
    group =
"""
1 *4 Xv u0 p0 c0
""",
    kinetics = None,
)


tree(
"""
L1: Combined
L1: VacantSite
"""
)

#forbidden(
#    label = "bonds1",
#    group =
#"""
#1 *1 C u0 {2,[S,D,T]}
#2 *3 Xo u0 {1,[S,D,T]}
#""",
#)

#forbidden(
#    label = "bonds2",
#    group =
#"""
#1 *4 X u0 {2,[S,D,Q]}
#2 *2 R u0 {1,[S,D,Q]}

#""",

#)
#forbidden(
#    label = "branch",
#    group =
#"""
#1 *3 X u0 {2,Q}
#2 *1 R u0 {1,Q} {3,S}
#3    R u0 {2,S}
#""",
#
#)

forbidden(
    label = "wrongbonds",
    group =
"""
1 *1 C ux px cx {3,[S,D,T,Q]} {2,[S,D]}
2 *2 R!H ux px cx {1,[S,D]}
3 *3 Xo u0 p0 c0 {1,[S,D,T,Q]}
""",
)
