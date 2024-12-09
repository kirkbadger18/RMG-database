#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Monodentate_to_Bidentate"
shortDesc = u""
longDesc = u"""
If a monodentate adsorbate has an internal double or triple bond, then it can fall over onto a vacant site, creating a bidentate.

 *1-*2=*4                 *1--*2-*4  
  |              ---->    ||   ||     
~*3~ + ~*5~~             ~*3~~*5~~ 

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)
so k should be in (m2/mol/s)
"""

template(reactants=["Monodentate", "VacantSite"], products=["Bidentate"], ownReverse=False)

reverse = "Surface_Bidentate_to_Monodentate"

recipe(actions=[
    ['FORM_BOND', '*2', 1, '*5'],
    ['CHANGE_BOND', '*2', 1, '*5'],
    ['CHANGE_BOND', '*2', -1, '*4'],
    ['LOSE_PAIR','*2','1'],
    ['GAIN_PAIR', '*4', '1'],

]) 

entry(
    index = 1,
    label = "Monodentate",
    group =
"""
1 *1 R!H u0 px c0 {2,S} {3,[S,D,T]}
2 *2 N u0 p1 cx {1,S} {4,D} 
3 *3 Xo  u0 p0 c0 {1,[S,D,T]}
4 *4 R!H u0 px cx {2,D}
""",
    kinetics = None,
)

entry(
    index = 2,
    label="VacantSite",
    group =
"""
1 *5 Xv u0 p0 c0
""",
    kinetics = None,
)


tree(
"""
L1: Monodentate
L1: VacantSite
"""
)

