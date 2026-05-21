#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Monodentate_to_vdW_Bidentate"
shortDesc = u""
longDesc = u"""
If a monodentate adsorbate has an internal double or triple bond, then it can fall over onto a vacant site, creating a bidentate.

 *1-*2=*3                 *1=*2-*3  
  |              ---->     :     |     
~*4~ + ~*5~~             ~*4~~~~*5~~ 

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)
so k should be in (m2/mol/s)
"""

template(reactants=["Monodentate", "VacantSite"], products=["Bidentate"], ownReverse=False)

reverse = "Surface_vdW_Bidentate_to_Monodentate"

recipe(actions=[
    ['FORM_BOND', '*3', 1, '*5'],
    ['CHANGE_BOND', '*2', -1, '*3'],
    ['CHANGE_BOND', '*1', 1, '*2'],
    ['CHANGE_BOND', '*1', -1, '*4'],
]) 

entry(
    index = 1,
    label = "Monodentate",
    group =
"""
1 *1 O  u0 p2 {2,S} {4,S}
2 *2 C  u0 p0 {1,S} {3,D}
3 *3 O  u0 p2 {2,D} 
4 *4 Xo u0 {1,S}
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
L1: Monodentate

L1: VacantSite
"""
)

