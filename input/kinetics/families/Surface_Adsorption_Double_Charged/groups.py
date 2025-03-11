#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_Double_Charged/groups"
shortDesc = u""
longDesc = u"""
Adsorption of a gas-phase triplet onto the surface. The unpaired electrons in the reactant form a double bond with the metal.

 *1==*2       *1(+)-*2(-)
        ---->  ||
~*3~         ~*3~~

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m3)
so k should be in (m3/mol/s). We will use sticking coefficients.
"""

template(reactants=["Adsorbate", "VacantSite"], products=["Adsorbed"], ownReverse=False)

reverse = "Surface_Desorption_Double_Charged"

reactantNum=2
productNum=1

recipe(actions=[
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['CHANGE_BOND', '*1', 1, '*3'],
    ['LOSE_PAIR','*1','1'],
    ['GAIN_PAIR', '*2', '1'],
    ['LOSE_CHARGE','*2','1'],
    ['GAIN_CHARGE', '*1', '1'],
])

entry(
    index = 1,
    label = "Adsorbate",
    group =
"""
1 *1 R!H u0 p1 c0 {2,D} {3,S}  
2 *2 R!H u0 px c0 {1,D} 
3    R u0 px c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label="VacantSite",
    group =
"""
1 *3 Xv u0
""",
    kinetics = None,
)


tree(
"""
L1: Adsorbate
L1: VacantSite
"""
)
