#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_Beta/groups"
shortDesc = u""
longDesc = u"""
Surface bond fission of one species into two distinct adsorbates. The bond fission occurs not at the binding atom, but in the beta position of the adsorbate, that is the bond between Atom *2 and *3 is broken. Atom *1 binds to the surface (*4). The image below shows a double bond, but a triple bond is also possible. What matters is that the bond between *2 and *3 must be single.


  *1--*2==*3              *1##*2   *3
  |||            ---->     |       ||
 ~*4~ + ~*5~~            ~*4~ +  ~*5~~

The rate, which should be in mol/m2/s, so k should be in (m2/mol/s).
"""

template(reactants=["Combined", "VacantSite"], products=["Adsorbate1","Adsorbate2"], ownReverse=False)

reverse = "Surface_Association_Beta"

reactantNum=2
productNum=2

recipe(actions=[
    ['FORM_BOND', '*3', 1, '*5'],
    ['CHANGE_BOND', '*3', 1, '*5'],
    ['CHANGE_BOND', '*2', -1, '*3'],
    ['BREAK_BOND', '*2', 1, '*3'],
    ['CHANGE_BOND', '*2', 1, '*1'],
    ['CHANGE_BOND', '*2', 1, '*1'],
    ['CHANGE_BOND', '*1', -1, '*4'],
    ['CHANGE_BOND', '*1', -1, '*4'],

])

entry(
    index = 1,
    label = "Combined",
    group =
"""
1 *1 C u0 c0 {2,S} {4,T}
2 *2 R!H u0 c0 {1,S} {3,D}
3 *3 R!H u0 c0 {2,D}
4 *4 Xo  u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 2,
    label="VacantSite",
    group =
"""
1 *5 Xv u0
""",
    kinetics = None,
)


tree(
"""
L1: Combined
L1: VacantSite
"""
)

forbidden(
    label = "Bidentate",
    group =
"""
1 *1 C u0 c0 {2,S} {4,T}
2 *2 R!H u0 c0 {1,S} {3,D}
3 *3 R!H u0 c0 {2,D} {5,[S,D,T]}
4 *4 Xo  u0 {1,T}
5    Xo  u0 {3,[S,D,T]}
"""
)