#!/usr/bin/env python
# encoding: utf-8

name = "Surface Adsorption Corrections Pt(111)"
shortDesc = u"Surface adsorption corrections Pt(111)"
longDesc = u"""
Changes in thermophysical properties due to adsorption on a surface, here Pt(111). Adsorption corrections are based on DFT calculations performed by Katrin Blondal and 
Bjarne Kreitz (Brown University). The computational methods and details are explained in Kreitz, Blöndal, Goldsmith et al. ACS Catal, 2022, 12,
11137-11151 (https://doi.org/10.1021/acscatal.2c03378) and Kreitz, Goldsmith et al., Angew. Chem. Int. Ed., 2023, 62, e202306514 (https://onlinelibrary.wiley.com/doi/10.1002/anie.202306514). 
The calculation of the adsorption corrections is explained in detail in the SI. 
If you use these adsorption corrections database in your work, please cite the publications mentioned above. 

TODO: Update adsorption corrections for N containing molecules. 
"""

entry(
    index = 1,
    label = "R*",
    group=
"""
1 R  ux
2 * X ux
""",
    thermo=None,
    shortDesc=u"""Anything adsorbed anyhow.""",
    longDesc=u"""
   R
   X
***********
This node should be empty, ensuring that one of the nodes below is used.


The group could well be defined as:

    1 R ux
    2 * Xux

but then it is identical with the R*vdW node, and the database tests
do not like that. It should be OK, because things would check the
tree in order, and if there *was* a bond it would match either
R*bidentate or R*single_chemisorbed and thus not R*vdW.
""",
    metal = "Pt",
    facet = "111",
)

#entry(
#    index = 1,
#    label = "R-*",
#    group =
#"""
#1 * X u0 p0 c0 {2,S}
#2 R  u0 p0 c0 {1,S}
#""",
#    thermo=ThermoData(
#        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
#        Cpdata=([-2.46, -1.45, -0.78, -0.33, 0.18, 0.46, 0.74], 'cal/(mol*K)'),
#        H298=(-58.54, 'kcal/mol'),
#        S298=(-26.39, 'cal/(mol*K)'),
#    ),
#    shortDesc=u"""Came from H single-bonded on Pt(111)""",
#    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
#            DFT binding energy: -2.479 eV.
#            Linear scaling parameters: ref_adatom_H = -2.479 eV, psi = 0.00000 eV, gamma_H(X) = 1.000.
#
#   R
#   |
#***********
#
#""",
#    metal = "Pt",
#    facet = "111",
#)

### This doesn't have a place in the tree, so I'm commenting it out. -- RHW
# entry(
#     index = 2,
#     label = "(R2)*",
#     group =
# """
# 1 * X u0 p0 c0
# 2 R  u0 p0 c0 {3,S}
# 3 R  u0 p0 c0 {2,S}
# """,
#     thermo=ThermoData(
#         Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
#         Cpdata=([0.92, 0.95, 0.97, 0.98, 0.98, 0.99, 0.99], 'cal/(mol*K)'),
#         H298=(-1.45, 'kcal/mol'),
#         S298=(-7.73, 'cal/(mol*K)'),
#     ),
#     shortDesc=u"""Came from H2 physisorbed on Pt(111)""",
#     longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
#             DFT binding energy: -0.054 eV.
#             Linear scaling parameters: ref_adatom_H = -2.479 eV, psi = -0.05448 eV, gamma_H(X) = 0.000.
#             The two lowest frequencies, 14.0 and 24.4 cm-1, where replaced by the 2D gas model.
#
#   R-R
#    :
# ***********
#""",
#    metal = "Pt",
#    facet = "111",
# )

entry(
    index = 3,
    label = "(OR2)*",
    group =
"""
1 * X u0 p0 c0
2 O  u0 p2 c0 {3,S} {4,S}
3 R  u0 p[0,1,2] c0 {2,S}
4 R  u0 p[0,1,2] c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.39, 8.41, 8.91, 9.16, 9.4, 9.51, 9.6], 'J/(mol*K)'),
        H298=(-49.08, 'kJ/mol'),
        S298=(-123.53, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged H2OX, HOOHX, CH3OHX, HCOOHX, CH3CH2OHX, CH3OCH3X, CH3OCH2OHX on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.   
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method.    

 RO-R
   :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 4,
    label = "O-*R",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.67, 8.28, 9.16, 9.7, 10.33, 10.68, 11.17], 'J/(mol*K)'),
        H298=(-194.2, 'kJ/mol'),
        S298=(-157.49, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XOCH3, XOH, XOCH2CH3, HOC(O)XO, HC(O)XO, XOCHCH2, XOOH, XOCH2OH on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   R
   |
   O
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 5,
    label = "(OROR)*",
    group =
"""
1 * X u0 p0 c0
2 O  u0 p2 c0 {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {5,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.32, 7.23, 7.68, 7.95, 8.29, 8.51, 8.71], 'J/(mol*K)'),
        H298=(-63.01, 'kJ/mol'),
        S298=(-110.35, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from HOOHX physisorbed on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            
            The two lowest frequencies, 12.0 and 47.7 cm-1, where replaced by the 2D gas model.  
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method.           
            
 RO-OR
   :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 6,
    label = "O*O*",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,S}
3 O  u0 p2 c0 {1,S} {4,S}
4 O  u0 p2 c0 {2,S} {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([8.69, 12.02, 13.4, 13.87, 13.89, 13.63, 13.13], 'J/(mol*K)'),
        H298=(-107.21, 'kJ/mol'),
        S298=(-167.43, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XOXO, twice single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   O--O
   |  |
***** *****
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 7,
    label = "O-*OR",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([10.21, 11.38, 11.38, 11.02, 10.19, 9.56, 8.77], 'J/(mol*K)'),
        H298=(-134.04, 'kJ/mol'),
        S298=(-120.71, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XOOH single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   OR
   |
   O
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 8,
    label = "O=*",
    group =
"""
1 * X u0 p0 c0 {2,D}
2 O  u0 p2 c0 {1,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-2.44, 0.14, 1.49, 2.26, 3.07, 3.45, 3.84], 'J/(mol*K)'),
        H298=(-382.56, 'kJ/mol'),
        S298=(-140.6, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XO double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   O
   ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 9,
    label = "O-*NR2",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 N  u0 p1 c0 {3,S} {4,S} {5,S}
3 O  u0 p2 c0 {1,S} {2,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.24, 2.94, 3.33, 3.56, 3.78, 3.87, 3.95], 'cal/(mol*K)'),
        H298=(-30.61, 'kcal/mol'),
        S298=(-35.75, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from XONH2 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.698 eV.
            Linear scaling parameters: ref_adatom_O = -3.586 eV, psi = 1.09537 eV, gamma_O(X) = 0.500.

   NR2
   |
   O
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 10,
    label = "O-*CR3",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 O  u0 p2 c0 {1,S} {2,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.44, 2.24, 2.93, 3.54, 4.49, 5.18, 6.35], 'J/(mol*K)'),
        H298=(-182.55, 'kJ/mol'),
        S298=(-149.81, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XOCH3, XOCH2CH3, and XOCH2OH on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   CR3
   |
   O
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 11,
    label = "(NR3)*",
    group =
"""
1 * X u0 p0 c0
2 N  u0 p1 c0 {3,S} {4,S} {5,S}
3 R  u0 px c0 {2,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.6, 10.71, 12.53, 13.66, 14.94, 15.59, 16.25], 'J/(mol*K)'),
        H298=(-99.73, 'kJ/mol'),
        S298=(-171.19, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from NH3*, NH2NH2*, and H2NOH* averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
    NR3
     :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 12,
    label = "N-*R2",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 N u0 p1 c0 {1,S} {3,S} {4,S}
3 R u0 px c0 {2,S}
4 R u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.17, 8.34, 10.84, 12.4, 14.11, 14.97, 15.88], 'J/(mol*K)'),
        H298=(-207.59, 'kJ/mol'),
        S298=(-187.48, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from *NH2, *NHCH3, *NHOH, and *NHNH2 averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
     NR2
     |
***********
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 13,
    label = "N=*R",
    group =
"""
1 * X u0 p0 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.03, 9.33, 11.56, 12.71, 13.59, 13.86, 14.24], 'J/(mol*K)'),
        H298=(-324.56, 'kJ/mol'),
        S298=(-174.98, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
     NR
    ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 14,
    label = "N#*",
    group =
"""
1 * X u0 p0 c0 {2,T}
2 N  u0 p1 c0 {1,T}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.93, -0.2, 0.19, 0.42, 0.66, 0.78, 0.9], 'cal/(mol*K)'),
        H298=(-103.33, 'kcal/mol'),
        S298=(-32.92, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from XN triple-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -4.352 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = 0.00000 eV, gamma_N(X) = 1.000.

    N
   |||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 15,
    label = "(NR2OR)*",
    group =
"""
1 * X u0 p0 c0
2 N  u0 p1 c0 {3,S} {4,S} {5,S}
3 O  u0 p2 c0 {2,S} {6,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
6 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.36, 0.16, 0.59, 0.93, 1.37, 1.64, 1.92], 'cal/(mol*K)'),
        H298=(-18.16, 'kcal/mol'),
        S298=(-32.2, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from H2XNOH physisorbed on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.654 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.65407 eV, gamma_N(X) = 0.000.
            The two lowest frequencies, 17.1 and 68.9 cm-1, where replaced by the 2D gas model.

 R2N-OR
    :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 16,
    label = "(NRO)*",
    group =
"""
1 * X u0 p0 c0
2 N  u0 p1 c0 {3,D} {4,S}
3 O  u0 p2 c0 {2,D}
4 R  u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.95, 11.63, 13.59, 14.61, 15.38, 15.61, 15.88], 'J/(mol*K)'),
        H298=(-173.61, 'kJ/mol'),
        S298=(-171.34, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from HNO* averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
    RN=O
     :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 17,
    label = "N-*ROR",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {5,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.77, 11.52, 13.47, 14.57, 15.71, 16.26, 16.74], 'J/(mol*K)'),
        H298=(-193.22, 'kJ/mol'),
        S298=(-192.96, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XNHOH single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

 R-N-OR
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 18,
    label = "N-*R",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,D}
3 R  u0 p0 c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.65, 9.96, 11.81, 12.89, 13.88, 14.26, 14.64], 'J/(mol*K)'),
        H298=(-196.81, 'kJ/mol'),
        S298=(-175.89, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from *NO, *NCH2, and *NNH averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
     NR
     |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 19,
    label = "N=*O-*",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {4,S}
3 N  u0 p1 c0 {1,D} {4,S}
4 O  u0 p2 c0 {2,S} {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.99, 2.43, 2.68, 2.82, 2.96, 3.00, 3.01], 'cal/(mol*K)'),
        H298=(-42.57, 'kcal/mol'),
        S298=(-35.43, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from XNXO bidentate, double- and single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.390 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = 1.51181 eV, gamma_N(X) = 0.667.

   N--O
  ||  |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 20,
    label = "N=*OR",
    group =
"""
1 * X u0 p0 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([8.94, 13.02, 14.82, 15.53, 15.69, 15.49, 15.39], 'J/(mol*K)'),
        H298=(-302.25, 'kJ/mol'),
        S298=(-181.63, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XNOH double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
 RO-N
    ||
***********
""",
    metal = "Pt",
    facet = "111",
)
entry(
    index = 21,
    label = "(NR2NR2)*",
    group =
"""
1 * X u0 p0 c0
2 N  u0 p1 c0 {3,S} {4,S} {5,S}
3 N  u0 p1 c0 {2,S} {6,S} {7,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
6 R  u0 p0 c0 {3,S}
7 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.52, 10.71, 12.51, 13.63, 14.89, 15.53, 16.19], 'J/(mol*K)'),
        H298=(-127.67, 'kJ/mol'),
        S298=(-191.32, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from NH2NH2* averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

  R2N-NR2
     :            
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 22,
    label = "(NRNR)*",
    group =
"""
1 * X u0 p0 c0
2 N  u0 p1 c0 {3,D} {4,S}
3 N  u0 p1 c0 {2,D} {5,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.95, 11.63, 13.59, 14.61, 15.38, 15.61, 15.88], 'J/(mol*K)'),
        H298=(-173.61, 'kJ/mol'),
        S298=(-171.34, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from HNO* averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
   RN=NR
     :
***********
""",
    metal = "Pt",
    facet = "111",
)


#entry(
#    index = 23,
#    label = "(NN)*",
#    group =
#"""
#1 * X u0 p0 c0
#3 N  u0 p1 c0 {3,T}
#4 N  u0 p1 c0 {2,T}
#""",
#    thermo=ThermoData(
#        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
#        Cpdata=([2.62, 3.77, 4.27, 4.45, 4.43, 4.3, 4.09], 'cal/(mol*K)'),
#        H298=(-6.31, 'kcal/mol'),
#        S298=(-15.27, 'cal/(mol*K)'),
#    ),
#    shortDesc=u"""Came from NN physisorbed on Pt(111)""",
#    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
#            DFT binding energy: -0.109 eV.
#            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.10949 eV, gamma_N(X) = 0.000.
#            The two lowest frequencies, 6.3 and 24.2 cm-1, where replaced by the 2D gas model.
#
#  N#N
#   :
#***********
#"""
#)

entry(
    index = 24,
    label = "N-*RNR2",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,S} {4,S}
3 N  u0 p1 c0 {2,S} {5,S} {6,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.18, 10.41, 12.36, 13.6, 15.01, 15.73, 16.43], 'J/(mol*K)'),
        H298=(-181.46, 'kJ/mol'),
        S298=(-190.4, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XNHNH2 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
 R-N-NR2
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 25,
    label = "N-*NR",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,D}
3 N  u0 p1 c0 {2,D} {4,S}
4 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.22, 10.09, 12.25, 13.47, 14.53, 14.93, 15.45], 'J/(mol*K)'),
        H298=(-165.68, 'kJ/mol'),
        S298=(-180.55, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XNNH single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
   NR
  ||
   N
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 26,
    label = "N=*NR2",
    group =
"""
1 * X u0 p0 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 N  u0 p1 c0 {2,S} {4,S} {5,S}
4 R  u0 p0 c0 {3,S}
5 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([11.18, 15.35, 17.04, 17.47, 16.95, 16.19, 15.45], 'J/(mol*K)'),
        H298=(-257.92, 'kJ/mol'),
        S298=(-177.23, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XNNH2 double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
   NR2
   |
   N
  ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 27,
    label = "N-*RN-*R",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,S}
3 N  u0 p1 c0 {1,S} {4,S} {5,S}
4 N  u0 p1 c0 {2,S} {3,S} {6,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([11.71, 16.21, 18.16, 18.81, 18.66, 18.1, 17.2], 'J/(mol*K)'),
        H298=(-123.48, 'kJ/mol'),
        S298=(-173.87, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XNHXNH on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
  RN-NR
   | |
***********
""",
    metal = "Pt",
    facet = "111",
)
entry(
    index = 28,
    label = "N-*RCR3",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 N  u0 p1 c0 {1,S} {2,S} {7,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
6 R  u0 p0 c0 {2,S}
7 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.07, 8.34, 10.43, 11.82, 13.43, 14.3, 15.34], 'J/(mol*K)'),
        H298=(-227.24, 'kJ/mol'),
        S298=(-193.23, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XNHCH3 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
 R-N-CR3
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 29,
    label = "N-*CR2",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 N  u0 p1 c0 {1,S} {2,D}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.97, 10.16, 11.97, 13.08, 14.28, 14.88, 15.61], 'J/(mol*K)'),
        H298=(-221.11, 'kJ/mol'),
        S298=(-179.69, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XNCH2 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

   CR2
  ||
   N
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 30,
    label = "N=*CR3",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 N  u0 p1 c0 {1,D} {2,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
6 R  u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.69, 9.54, 11.16, 12.22, 13.49, 14.22, 15.21], 'J/(mol*K)'),
        H298=(-361.58, 'kJ/mol'),
        S298=(-180.78, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XNCH3 double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

 R3C-N
     || 
***********
""",
    metal = "Pt",
    facet = "111",
)


### Leads to AtomTypeError: Unable to determine atom type for atom O-, which has 3 single bonds, 0 double bonds to C, 0 double bonds to O, 0 double bonds to S, 0 triple bonds, 0 benzene bonds, 0 lone pairs, and 2 charge.
### And is not in the tree anyway, so commenting out. RHW
# entry(
#     index = 31,
#     label = "N-*O2",
#     group =
# """
# 1 * X u0  p0 c0 {2,S}
# 2 N  u0  p0 c+1 {1,S} {3,S} {4,D}
# 3 O  u0  p2 c-1 {2,S}
# 4 O  u0  p2 c0 {2,D}
# """,
#     thermo=ThermoData(
#         Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
#         Cpdata=([1.92, 2.12, 2.17, 2.17, 2.13, 2.09, 2.04], 'cal/(mol*K)'),
#         H298=(34.56, 'kcal/mol'),
#         S298=(-33.93, 'cal/(mol*K)'),
#     ),
#     shortDesc=u"""Came from ON-O single-bonded on Pt(111)""",
#     longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
#             Linear scaling parameters: ref_adatom_N = 0.525 eV, psi = -0.86302 eV, gamma_N(X) = 0.333.
#             The two lowest frequencies, -33.2 and 55.1 cm-1, where replaced by the 2D gas model.
#
#  O-N=O
#    |
# ***********
# """,
#    metal = "Pt",
#    facet = "111",
# )

entry(
    index = 32,
    label = "Cq*",
    group =
"""
1 * X u0 p0 c0 {2,Q}
2 C  u0 p0 c0 {1,Q}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-7.34, -3.34, -1.0, 0.42, 1.97, 2.73, 3.51], 'J/(mol*K)'),
        H298=(-657.91, 'kJ/mol'),
        S298=(-133.84, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XC quadruple-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   C
 ||||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 33,
    label = "C-*C-*",
    group =
"""
1 * X u0  p0 c0 {3,D}
2 X u0  p0 c0 {4,D}
3 C  u0  p0 c0 {1,D} {4,D}
4 C  u0  p0 c0 {2,D} {3,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.31, 7.38, 9.53, 10.71, 11.76, 12.14, 12.4], 'J/(mol*K)'),
        H298=(-613.35, 'kJ/mol'),
        S298=(-163.77, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCXC double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

  C==C
 ||  ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 34,
    label = "C=*(=R)",
    group =
"""
1 * X  u0  p0 c0 {2,D}
2 C   u0  p0 c0 {1,D} {3,D}
3 R!H u0  px c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.94, 6.26, 8.08, 9.18, 10.4, 11.04, 11.77], 'J/(mol*K)'),
        H298=(-429.79, 'kJ/mol'),
        S298=(-168.79, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCCH2, XCCCH2, XCCO on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   R
  ||
   C
  ||
***********

Because the C atom bonded to the surface only has one ligand
not two, it is not a child of the C=*R2 node
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 35,
    label = "C#*CR3",
    group =
"""
1 * X u0 p0 c0 {3,T}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {1,T} {2,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.91, 1.58, 4.18, 6.07, 8.47, 9.86, 11.63], 'J/(mol*K)'),
        H298=(-594.9, 'kJ/mol'),
        S298=(-174.23, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCCH3, XCCH2CH3, XCCH2OH on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   CR3
   |
   C
  |||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 36,
    label = "C#*R",
    group =
"""
1 * X u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.12, 2.73, 5.33, 7.1, 9.21, 10.37, 11.81], 'J/(mol*K)'),
        H298=(-571.12, 'kJ/mol'),
        S298=(-176.66, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCH, XCCH3, XCOH, XCCHCH2, XCCH2CH3, XCCHO, XCCH2OH on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   R
   |
   C
  |||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 37,
    label = "C=*RC=*R",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 C  u0 p0 c0 {2,D} {3,S} {6,S}
5 R  u0 px c0 {3,S}
6 R  u0 px c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-5.41, -0.06, 4.05, 6.96, 10.38, 12.03, 13.24], 'J/(mol*K)'),
        H298=(-221.27, 'kJ/mol'),
        S298=(-175.96, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHXCH double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

 R-C--C-R
  ||  ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 38,
    label = "C=*R2",
    group =
"""
1 * X u0 p0 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 R  u0 px c0 {2,S}
4 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.24, 3.87, 6.15, 7.64, 9.38, 10.32, 11.42], 'J/(mol*K)'),
        H298=(-370.06, 'kJ/mol'),
        S298=(-174.19, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCH2, CH3XCCH3, CH3XCOH, XCHCH2CH3, XCHCH3, XCHCHCH2, XCHCHO, XCHOH on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

 R-C-R
  ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 39,
    label = "C-*R2C-*R2",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C  u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
5 R  u0 px c0 {3,S}
6 R  u0 px c0 {3,S}
7 R  u0 px c0 {4,S}
8 R  u0 px c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.94, 10.72, 13.46, 15.04, 16.54, 17.1, 17.33], 'J/(mol*K)'),
        H298=(-124.09, 'kJ/mol'),
        S298=(-192.34, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCH2XCH2 and CH3XCHXCH2 on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

 R2C--CR2
   |  |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 40,
    label = "C-*R3",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 R  u0 px c0 {2,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.16, 2.29, 4.74, 6.49, 8.69, 9.93, 11.24], 'J/(mol*K)'),
        H298=(-212.02, 'kJ/mol'),
        S298=(-176.19, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCH2CH2CH3, XCH2CH2OH, XCH2CH3, XCH2CHCH2, XCH2CHO, XCH3, CH3XCHCH3, CH3XCHOH, XCH2OH on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   CR3
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 41,
    label = "(CR3CR3)*",
    group =
"""
1 * X u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {2,S}
7 R  u0 px c0 {3,S}
8 R  u0 px c0 {3,S}
9 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([9.04, 9.93, 10.39, 10.67, 10.97, 11.11, 11.2], 'J/(mol*K)'),
        H298=(-29.6, 'kJ/mol'),
        S298=(-137.34, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged CH3CH3X, CH3CH2CH3X, CH3CH2OHX on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

 R3C-CR3
    :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 42,
    label = "(CR4)*",
    group =
"""
1 * X u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 R  u0 px c0 {2,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([8.55, 9.48, 9.93, 10.16, 10.36, 10.44, 10.48], 'J/(mol*K)'),
        H298=(-41.27, 'kJ/mol'),
        S298=(-125.91, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged CH4X, CH3CH3X, CH3CH2CH3X, CH3CH2OHX, CH3OHX, CH3OCH3X, CH3OCH2OHX on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

  R3C-R
     :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 43,
    label = "C=*N-*",
    group =
"""
1 * X u0  p0 c0 {3,D}
2 X u0  p0 c0 {4,S}
3 C  u0  p0 c0 {1,D} {4,D}
4 N  u0  p1 c0 {2,S} {3,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.74, 7.17, 9.76, 11.28, 12.72, 13.25, 13.53], 'J/(mol*K)'),
        H298=(-172.9, 'kJ/mol'),
        S298=(-186.0, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from 2*(*CH*N), *CH2*N, *CH2*NH, and *CH*NH averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
    C=N
   || |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 44,
    label = "C=*(=NR)",
    group =
"""
1 * X u0  p0 c0 {2,D}
2 C  u0  p0 c0 {1,D} {3,D}
3 N  u0  p1 c0 {2,D} {4,S}
4 R  u0  p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.67, 8.37, 10.13, 11.25, 12.43, 12.91, 13.12], 'J/(mol*K)'),
        H298=(-213.74, 'kJ/mol'),
        S298=(-159.4, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from *CNH averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

    NR
   ||
    C
   ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 45,
    label = "C#*NR2",
    group =
"""
1 * X u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 N  u0 p1 c0 {2,S} {4,S} {5,S}
4 R  u0 p0 c0 {3,S}
5 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([9.9, 12.91, 14.31, 14.98, 15.41, 15.46, 15.56], 'J/(mol*K)'),
        H298=(-456.52, 'kJ/mol'),
        S298=(-182.19, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from *CNH2 averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

   NR2
   |
   C
  |||
***********
""",
    metal = "Pt",
    facet = "111",
)


## Not present in the tree
# entry(
#     index = 46,
#     label = "C=*O",
#     group =
# """
# 1 * X u0  p0 c0 {2,D}
# 2 C  u0  p0 c0 {1,D} {3,D}
# 3 O  u0  p2 c0 {2,D}
# """,
#     thermo=ThermoData(
#         Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
#         Cpdata=([1.81, 2.37, 2.68, 2.88, 3.05, 3.1, 3.08], 'cal/(mol*K)'),
#         H298=(-41.06, 'kcal/mol'),
#         S298=(-38.09, 'cal/(mol*K)'),
#     ),
#     shortDesc=u"""Came from CO-f double-bonded on Pt(111)""",
#     longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
#             DFT binding energy: -1.480 eV.
#             Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = 1.89529 eV, gamma_C(X) = 0.500.
#
#    O
#   ||
#    C
#   ||
# ***********
# """,
#    metal = "Pt",
#    facet = "111",
# )

entry(
    index = 47,
    label = "C#*OR",
    group =
"""
1 * X u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.83, 9.83, 11.9, 12.95, 13.69, 13.91, 14.43], 'J/(mol*K)'),
        H298=(-463.49, 'kJ/mol'),
        S298=(-187.54, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCOH triple-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   OR
   |
   C
  |||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 48,
    label = "C-*R2C=*R",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C  u0 p0 c0 {2,D} {3,S} {7,S}
5 R  u0 px c0 {3,S}
6 R  u0 px c0 {3,S}
7 R  u0 px c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.74, 6.17, 9.66, 11.87, 14.28, 15.41, 16.39], 'J/(mol*K)'),
        H298=(-330.81, 'kJ/mol'),
        S298=(-214.97, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCHXCH2, XCH2XCOH, XCHXCHCH3 on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

 R2C--CR
   |  ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 49,
    label = "C-*R2CR3",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C  u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {3,S}
7 R  u0 px c0 {3,S}
8 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.39, 3.93, 6.35, 8.02, 10.07, 11.2, 12.43], 'J/(mol*K)'),
        H298=(-214.46, 'kJ/mol'),
        S298=(-192.28, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCH2CH2CH3, XCH2CH2OH, XCH2CH3, CH3XCHCH3, CH3XCHOH on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   R
   |
 R-C-CR3
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 50,
    label = "(CR2NR)*",
    group =
"""
1 * X u0 p0 c0
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 N  u0 p1 c0 {2,D} {6,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
6 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([11.08, 14.41, 16.06, 16.83, 17.25, 17.21, 16.97], 'J/(mol*K)'),
        H298=(-65.13, 'kJ/mol'),
        S298=(-170.9, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CH2NH* averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

  R2C=NR
     :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 51,
    label = "C-*R2NR2",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 N  u0 p1 c0 {2,S} {6,S} {7,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
6 R  u0 p0 c0 {3,S}
7 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.3, 7.27, 9.52, 11.2, 13.4, 14.65, 15.96], 'J/(mol*K)'),
        H298=(-238.22, 'kJ/mol'),
        S298=(-180.15, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from *CH2NH2 averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

   R
   |
 R-C-NR2
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 52,
    label = "(CR2O)*",
    group =
"""
1 * X u0 p0 c0
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 O  u0 p2 c0 {2,D}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.0, 6.87, 7.39, 7.72, 8.09, 8.27, 8.39], 'J/(mol*K)'),
        H298=(-73.08, 'kJ/mol'),
        S298=(-122.36, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged H2COX, HCOOHX, CH3CHOX, OCO2H2X, CH2COX on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

 R2C=O
    :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 53,
    label = "C-*R2OR",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 O  u0 p2 c0 {2,S} {6,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-3.14, 0.0, 2.2, 3.74, 5.64, 6.69, 7.8], 'J/(mol*K)'),
        H298=(-225.57, 'kJ/mol'),
        S298=(-157.56, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCH2OH, CH3XCHOH on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

    R
    |
  R-C-OR
    |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 54,
    label = "(CR3NR2)*",
    group =
"""
1 * X u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 N  u0 p1 c0 {2,S} {7,S} {8,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
6 R  u0 p0 c0 {2,S}
7 R  u0 p0 c0 {3,S}
8 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.87, 10.67, 12.38, 13.47, 14.7, 15.34, 16.04], 'J/(mol*K)'),
        H298=(-111.7, 'kJ/mol'),
        S298=(-185.03, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CH3NH2* averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

 R3C-NR2
    :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 55,
    label = "(CR3OR)*",
    group =
"""
1 * X u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 O  u0 p2 c0 {2,S} {7,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {2,S}
7 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([8.44, 9.53, 10.02, 10.25, 10.41, 10.45, 10.47], 'J/(mol*K)'),
        H298=(-57.56, 'kJ/mol'),
        S298=(-139.36, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged CH3OHX, CH3OCH3X, H2CO2H2X, CH3OCH2OHX on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

 R3C-OR
    :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 56,
    label = "C-*RC=*",
    group =
"""
1 * X u0  p0 c0 {3,S}
2 X u0  p0 c0 {4,D}
3 C  u0  p0 c0 {1,S} {4,D} {5,S}
4 C  u0  p0 c0 {2,D} {3,D}
5 R  u0  px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.53, 3.23, 6.15, 7.98, 10.0, 10.99, 11.95], 'J/(mol*K)'),
        H298=(-440.52, 'kJ/mol'),
        S298=(-184.43, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHXC single- and double bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

 RC--C
  |  ||
***********
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 57,
    label = "C-*RCR2",
    group =
"""
1 * X u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 C  u0  p0 c0 {2,D} {5,S} {6,S}
4 R  u0  px c0 {2,S}
5 R  u0  px c0 {3,S}
6 R  u0  px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.29, 4.86, 7.35, 9.04, 10.97, 11.92, 12.82], 'J/(mol*K)'),
        H298=(-288.17, 'kJ/mol'),
        S298=(-182.51, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged CH2XCCH3, CH2XCOH, XCHCCH2, XCHCH2, XCHCHCH3 on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   CR2
  ||
   C-R
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 58,
    label = "C=*RCR3",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {1,D} {2,S} {7,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {2,S}
7 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.78, 4.72, 6.6, 7.86, 9.39, 10.26, 11.34], 'J/(mol*K)'),
        H298=(-372.23, 'kJ/mol'),
        S298=(-179.04, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged CH3XCCH3, CH3XCOH, XCHCH2CH3, XCHCH3 on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   CR3
   |
   C-R
  ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 59,
    label = "(CRN)*",
    group =
"""
1 * X u0  p0 c0
2 C  u0  p0 c0 {3,T} {4,S}
3 N  u0  p1 c0 {2,T}
4 R  u0  p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([10.32, 11.33, 11.98, 12.42, 12.91, 13.1, 13.08], 'J/(mol*K)'),
        H298=(-44.8, 'kJ/mol'),
        S298=(-138.37, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from HCN* averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

    RC#N
     :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 60,
    label = "C=*RN=*",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 N  u0 p1 c0 {2,D} {3,S}
5 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.48, 2.75, 4.98, 6.5, 8.18, 8.88, 9.19], 'J/(mol*K)'),
        H298=(-108.43, 'kJ/mol'),
        S298=(-174.03, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHXN on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
    R
    |
    C-N
   || ||
***********
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 61,
    label = "C-*RNR",
    group =
"""
1 * X u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 N  u0  p1 c0 {2,D} {5,S}
4 R  u0  p0 c0 {2,S}
5 R  u0  p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.74, 10.1, 12.12, 13.39, 14.78, 15.44, 16.11], 'J/(mol*K)'),
        H298=(-278.59, 'kJ/mol'),
        S298=(-177.54, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from *CHNH averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
   NR
  ||
   C-R
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 62,
    label = "C=*RN-*R",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 N  u0 p1 c0 {2,S} {3,S} {6,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.6, 8.95, 11.51, 13.07, 14.67, 15.37, 16.01], 'J/(mol*K)'),
        H298=(-306.43, 'kJ/mol'),
        S298=(-190.18, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHXNH on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
    R
    |
    C-NR
   || |
***********
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 63,
    label = "C=*RNR2",
    group =
"""
1 * X u0 p0 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 N  u0 p1 c0 {2,S} {5,S} {6,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([9.01, 12.46, 14.13, 14.95, 15.55, 15.72, 15.92], 'J/(mol*K)'),
        H298=(-308.59, 'kJ/mol'),
        S298=(-174.93, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from *CHNH2 averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

   NR2
   |
   C-R
  ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 64,
    label = "C-*RO",
    group =
"""
1 * X u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 O  u0  p2 c0 {2,D}
4 R  u0  px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.65, 2.4, 4.38, 5.69, 7.2, 7.95, 8.71], 'J/(mol*K)'),
        H298=(-282.27, 'kJ/mol'),
        S298=(-161.1, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged HXCO, OXCOH, CH3XCO, CHXCO, CH3CH2XCO on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   R
   |
   C=O
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 65,
    label = "C=*RO-*",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 O  u0 p2 c0 {2,S} {3,S}
5 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.91, 10.27, 12.84, 14.27, 15.45, 15.81, 16.1], 'J/(mol*K)'),
        H298=(-238.17, 'kJ/mol'),
        S298=(-167.73, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHXO double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

  R
  |
  C--O
 ||  |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 66,
    label = "C=*ROR",
    group =
"""
1 * X u0 p0 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {5,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.05, 2.82, 4.47, 5.52, 6.78, 7.48, 8.24], 'J/(mol*K)'),
        H298=(-325.89, 'kJ/mol'),
        S298=(-146.57, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCHOH and CH3XCOH on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   OR
   |
   C-R
  ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 67,
    label = "C*",
    group =
"""
1 * X u0 {2,[S,D,T,Q]}
2 C  ux {1,[S,D,T,Q]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.31, 3.22, 5.55, 7.13, 8.99, 9.99, 11.1], 'J/(mol*K)'),
        H298=(-359.63, 'kJ/mol'),
        S298=(-173.0, 'J/(mol*K)'),
    ),
    shortDesc=u"""Averaged from all children on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 68,
    label = "N*",
    group =
"""
1 * X u0 {2,[S,D,T]}
2 N  ux {1,[S,D,T]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.71, 7.61, 9.76, 10.97, 12.06, 12.47, 12.86], 'J/(mol*K)'),
        H298=(-223.98, 'kJ/mol'),
        S298=(-179.25, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 69,
    label = "O*",
    group =
"""
1 * X u0 {2,[S,D]}
2 O  ux {1,[S,D]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.66, 7.38, 8.31, 8.88, 9.52, 9.88, 10.36], 'J/(mol*K)'),
        H298=(-215.12, 'kJ/mol'),
        S298=(-155.61, 'J/(mol*K)'),
    ),
    shortDesc=u"""Averaged from all children on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 70,
    label = "R*single-chemisorbed",
    group =
"""
1 * X u0 {2,[S,D,T,Q]}
2 R  ux {1,[S,D,T,Q]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.84, 4.02, 6.08, 7.46, 9.09, 9.97, 10.96], 'J/(mol*K)'),
        H298=(-331.96, 'kJ/mol'),
        S298=(-169.67, 'J/(mol*K)'),
    ),
    shortDesc=u"""Averaged from all children on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 71,
    label = "C*C*",
    group =
"""
1 * X u0 {3,[S,D,T]}
2 X u0 {4,[S,D,T]}
3 C  u0 {1,[S,D,T]} {4,[S,D,T]}
4 C  u0 {2,[S,D,T]} {3,[S,D,T]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.88, 5.67, 8.7, 10.62, 12.69, 13.65, 14.5], 'J/(mol*K)'),
        H298=(-353.37, 'kJ/mol'),
        S298=(-192.89, 'J/(mol*K)'),
    ),
    shortDesc=u"""Averaged from all children on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 72,
    label = "C*N*",
    group =
"""
1 * X u0 {3,[S,D]}
2 X u0 {4,[S,D,T]}
3 C  u0 {1,[S,D]} {4,[S,D,T]}
4 N  u0 {2,[S,D,T]} {3,[S,D,T]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.74, 7.17, 9.76, 11.28, 12.72, 13.25, 13.53], 'J/(mol*K)'),
        H298=(-172.9, 'kJ/mol'),
        S298=(-186.0, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from 2*(*CH*N), *CH2*N, *CH2*NH, and *CH*NH averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)


#Changed the adjacency list because O can only have a single bond to the surface and another atom. 
#Always 2 free electron pairs. BK 2023/1/10
entry(
    index = 73,
    label = "C*O*",
    group =
"""
1 * X u0 {3,[S,D,T]}
2 X u0 {4,S}
3 C  u0 {1,[S,D,T]} {4,S}
4 O  u0 p2 {2,S} {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.34, 11.93, 14.46, 15.74, 16.6, 16.72, 16.63], 'J/(mol*K)'),
        H298=(-149.6, 'kJ/mol'),
        S298=(-169.0, 'J/(mol*K)'),
    ),
    shortDesc=u"""Averaged from all child nodes on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 74,
    label = "N*N*",
    group =
"""
1 * X u0 {3,[S,D]}
2 X u0 {4,[S,D]}
3 N  u0 {1,[S,D]} {4,[S,D]}
4 N  u0 {2,[S,D]} {3,[S,D]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([8.14, 12.68, 14.94, 15.99, 16.54, 16.47, 16.28], 'J/(mol*K)'),
        H298=(-156.49, 'kJ/mol'),
        S298=(-181.52, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from *NH*N, and *NH*NH averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 75,
    label = "R*bidentate",
    group =
"""
1 * X  u0 {3,[S,D,T]}
2 X  u0 {4,[S,D,T]}
3 R!H ux {1,[S,D,T]} {4,[S,D,T]}
4 R!H ux {2,[S,D,T]} {3,[S,D,T]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.59, 6.37, 9.34, 11.19, 13.12, 13.99, 14.74], 'J/(mol*K)'),
        H298=(-330.73, 'kJ/mol'),
        S298=(-190.23, 'J/(mol*K)'),
    ),
    shortDesc=u"""Averaged from all child nodes on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 76,
    label = "R*vdW",
    group =
"""
1 * X u0
2 R  u0
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.25, 8.33, 8.9, 9.23, 9.56, 9.7, 9.8], 'J/(mol*K)'),
        H298=(-56.05, 'kJ/mol'),
        S298=(-125.18, 'J/(mol*K)'),
    ),
    shortDesc=u"""Averaged of (CR4)*, (CR3)*, and (OR2)* (nitrogen is not included) on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 77,
    label = "N*O*",
    group =
"""
1 * X u0 p0 c0 {3,[S,D]}
2 X u0 p0 c0 {4,[S,D]}
3 N  u0 p1 c0 {1,[S,D]} {4,[S,D]}
4 O  u0 p2 c0 {2,[S,D]} {3,[S,D]}
""",
    thermo=u'N=*O-*',
    longDesc=u"""Is there really any way to do N*O* besides N=*O-* ?""",
    metal = "Pt",
    facet = "111",
)

#entry(
#    index = 78,
#    label = "O*O*",
#    group =
#"""
#1 * X u0 p0 c0 {3,S}
#2 * X u0 p0 c0 {4,S}
#3 O  u0 p2 c0 {1,S} {4,S}
#4 O  u0 p2 c0 {2,S} {3,S}
#""",
#    thermo=u'O-*O-*',
#    longDesc=u"""Is there really any way to do O*O* besides O-*O-* ?""",
#    metal = "Pt",
#    facet = "111",
#)

###Have not been able to find any examples of when N is triple bonded to the surface and
###has an R group attached.  Redid for no R group below. --EM
#entry(
#    index = 79,
#    label = "N#*R",
#    group =
#"""
#1 * X u0 c-1 {2,T}
#2 N  u0 c+1 {1,T} {3,S}
#3 R  u0 c0  {2,S}
#""",
#    thermo=u'N*',
#    metal = "Pt",
#    facet = "111",
#)

entry(
    index = 79,
    label = "N#*",
    group =
"""
1 * X u0 p0 {2,T}
2 N  u0 p1 {1,T}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-12.26, -9.29, -7.94, -7.48, -7.74, -8.48, -10.07], 'J/(mol*K)'),
        H298=(31.25, 'kJ/mol'),
        S298=(-173.48, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XN on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
    N
   |||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 80,
    label = "(CR3)*",
    group =
"""
1 * X  u0
2 C   u0 {3,D} {4,S} {5,S}
3 R!H u0 {2,D}
4 R   u0 {2,S}
5 R   u0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.54, 7.68, 8.34, 8.74, 9.14, 9.32, 9.44], 'J/(mol*K)'),
        H298=(-74.45, 'kJ/mol'),
        S298=(-130.43, 'J/(mol*K)'),
    ),
    shortDesc=u"""Averaged from all children on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 81,
    label = "(CR2)*",
    group =
"""
1 * X  u0
2 C   u0 {3,T} {4,S}
3 R!H u0 {2,T}
4 R   u0 {2,S}
""",
    thermo=u'(CRCR)*',
    metal = "Pt",
    facet = "111",
)

entry(
    index = 82,
    label = "(N=[O,N]R)*",
    group =
"""
1 * X    u0
2 N     u0 {3,D} {4,S}
3 [N,O] u0 {2,D}
4 R     u0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.95, 11.63, 13.59, 14.61, 15.38, 15.61, 15.88], 'J/(mol*K)'),
        H298=(-173.61, 'kJ/mol'),
        S298=(-171.34, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from HNO* averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
   R=N-R
     :
***********
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 83,
    label = "N-*RN=*",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,D}
3 N  u0 p1 c0 {1,S} {4,S} {5,S}
4 N  u0 p1 c0 {2,D} {3,S}
5 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.58, 9.14, 11.72, 13.17, 14.41, 14.84, 15.36], 'J/(mol*K)'),
        H298=(-189.5, 'kJ/mol'),
        S298=(-189.18, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XNHXN on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
   N-NR
  || |
***********
""",
    metal = "Pt",
    facet = "111",
)
entry(
    index = 84,
    label = "(CRCR)*",
    group =
"""
1 * X u0 p0 c0
2 C  u0 p0 c0 {3,T} {4,S}
3 C  u0 p0 c0 {2,T} {5,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.69, 1.89, 2.02, 2.13, 2.46, 2.9, 3.96], 'J/(mol*K)'),
        H298=(-59.58, 'kJ/mol'),
        S298=(-115.19, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged CHCHX and CHCCH3X on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

  RC#CR
    :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 85,
    label = "C-*R2N=*",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 N  u0 p1 c0 {2,D} {3,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.68, 8.55, 11.36, 13.0, 14.54, 15.16, 15.78], 'J/(mol*K)'),
        H298=(-224.9, 'kJ/mol'),
        S298=(-193.78, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCH2XN on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
 R2C-N
   | ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 86,
    label = "C-*R2N-*R",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 N  u0 p1 c0 {2,S} {3,S} {7,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {3,S}
7 R  u0 p0 c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.38, 12.87, 15.96, 17.33, 18.05, 17.97, 17.46], 'J/(mol*K)'),
        H298=(-116.31, 'kJ/mol'),
        S298=(-197.95, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCH2XNH on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
 R2C-NR
   | |
***********
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 87,
    label = "C=*(=C)",
    group =
"""
1 * X u0  p0 c0 {2,D}
2 C  u0  p0 c0 {1,D} {3,D}
3 C  u0  p0 c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.94, 6.26, 8.08, 9.18, 10.4, 11.04, 11.77], 'J/(mol*K)'),
        H298=(-429.79, 'kJ/mol'),
        S298=(-168.79, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCCH2, XCCCH2, XCCO on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   C
  ||
   C
  ||
***********

Because the C atom bonded to the surface only has one ligand
not two, it is not a child of the C=*R2 node
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 88,
    label = "C-*R2O-*",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 O  u0 p2 c0 {2,S} {3,S}
5 R  u0 px c0 {3,S}
6 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([8.78, 13.6, 16.07, 17.2, 17.75, 17.62, 17.16], 'J/(mol*K)'),
        H298=(-61.03, 'kJ/mol'),
        S298=(-170.27, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCH2XO single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

 R2C--O
   |  |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 89,
    label = "(CR2CR)*",
    group =
"""
1 * X u0 p0 c0
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 C  u0 p0 c0 {2,D} {6,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.43, 9.04, 9.92, 10.43, 10.9, 11.07, 11.17], 'J/(mol*K)'),
        H298=(-76.74, 'kJ/mol'),
        S298=(-143.86, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged CH2CH2X, CH3CHCH2X, CH2CCH2X on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
 R2C=CR
    :
***********
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 90,
    label = "C=*RC-*R",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 C  u0 p0 c0 {2,S} {3,S} {6,D}
5 R  u0 px c0 {3,S}
6 R!H  u0 px c0 {4,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-5.37, 0.67, 4.68, 7.31, 10.25, 11.63, 12.69], 'J/(mol*K)'),
        H298=(-396.35, 'kJ/mol'),
        S298=(-202.17, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHXCO double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
   RC---C=R
    ||  |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 91,
    label = "C#*C-*R",
    group =
"""
1 * X u0 p0 c0 {3,T}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,T} {4,S}
4 C  u0 p0 c0 {2,S} {3,S} {5,D}
5 R!H  u0 px c0 {4,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.41, 8.3, 11.6, 13.47, 15.23, 15.91, 16.41], 'J/(mol*K)'),
        H298=(-440.28, 'kJ/mol'),
        S298=(-204.35, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCXCCH2 twice single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
     C---C=R
    |||  |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 92,
    label = "C#*C-*R2",
    group =
"""
1 * X u0 p0 c0 {3,T}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,T} {4,S}
4 C  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5 R  u0 px c0 {4,S}
6 R  u0 px c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.9, 4.58, 8.22, 10.59, 13.24, 14.53, 15.76], 'J/(mol*K)'),
        H298=(-436.46, 'kJ/mol'),
        S298=(-201.88, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCXCH2 and XCXCHCH3 on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
     C---CR2
    |||  |
***********
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 93,
    label = "C-*R2C-*R",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C  u0 p0 c0 {2,S} {3,S} {7,D}
5 R  u0 px c0 {3,S}
6 R  u0 px c0 {3,S}
7 R!H  u0 px c0 {4,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.18, 10.54, 13.14, 14.74, 16.34, 16.95, 17.2], 'J/(mol*K)'),
        H298=(-179.99, 'kJ/mol'),
        S298=(-191.92, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCH2CXCH2 single and single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  R2C--C=R
    |  |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 95,
    label = "C-*RC-*R",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,D} {5,S}
4 C  u0 p0 c0 {2,S} {3,D} {6,S}
5 R  u0 px c0 {3,S}
6 R  u0 px c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.8, 1.82, 4.66, 6.68, 9.21, 10.78, 13.11], 'J/(mol*K)'),
        H298=(-227.58, 'kJ/mol'),
        S298=(-194.29, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHXCCH3 single and single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
 RC==CR
  |  |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 96,
    label = "C#*C=*R",
    group =
"""
1 * X u0 p0 c0 {3,T}
2 X u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,T} {4,S}
4 C  u0 p0 c0 {2,D} {3,S} {5,S}
5 R  u0 px c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-2.0, 1.29, 3.27, 4.54, 5.97, 6.69, 7.48], 'J/(mol*K)'),
        H298=(-488.53, 'kJ/mol'),
        S298=(-158.38, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCXCCH3 triple and double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  C--CR
 ||| ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 97,
    label = "C=*=R-C-*R2",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {5,S}
3 C  u0 p0 c0 {1,D} {4,D} 
4 R!H  u0 px c0 {3,D} {5,S}
5 C  u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
6 R  u0 px c0 {5,S}
7 R  u0 px c0 {5,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-3.01, 2.84, 6.84, 9.5, 12.5, 13.99, 15.5], 'J/(mol*K)'),
        H298=(-543.25, 'kJ/mol'),
        S298=(-229.45, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCCHXCH2 double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  C=R--CR2
 ||    |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 98,
    label = "R2C-*-R-C-*R2",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {5,S}
3 C  u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
4 R!H  u0 px c0 {3,S} {5,S}
5 C  u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
6 R  u0 px c0 {5,S}
7 R  u0 px c0 {5,S}
8 R  u0 px c0 {3,S}
9 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.02, 3.61, 7.1, 9.67, 12.99, 14.82, 16.51], 'J/(mol*K)'),
        H298=(-389.14, 'kJ/mol'),
        S298=(-209.34, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCH2CH2XCH2 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
 R2C--R--CR2
   |     |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 99,
    label = "RC=*-R=C-*R",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {5,S}
3 C  u0 p0 c0 {1,D} {4,S} {6,S}
4 R!H  u0 px c0 {3,S} {5,D}
5 C  u0 p0 c0 {2,S} {4,D} {7,S}
6 R  u0 px c0 {3,S}
7 R  u0 px c0 {5,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-6.06, -1.1, 2.74, 5.57, 9.12, 11.14, 13.63], 'J/(mol*K)'),
        H298=(-612.92, 'kJ/mol'),
        S298=(-200.99, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHCHXCH single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  RC--R==CR
  ||     |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 100,
    label = "RC-*=R-C-*R2",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {5,S}
3 C  u0 p0 c0 {1,S} {4,D} {6,S}
4 R!H  u0 px c0 {3,D} {5,S}
5 C  u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
6 R  u0 px c0 {3,S}
7 R  u0 px c0 {5,S}
8 R  u0 px c0 {5,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.12, 6.05, 9.54, 11.64, 13.78, 14.75, 15.73], 'J/(mol*K)'),
        H298=(-426.75, 'kJ/mol'),
        S298=(-227.78, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHCHXCH2 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  RC==R--CR2
  |      |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 101,
    label = "RC=*-R-C-*R2",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {5,S}
3 C  u0 p0 c0 {1,D} {4,S} {6,S}
4 R!H  u0 px c0 {3,S} {5,S}
5 C  u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
6 R  u0 px c0 {3,S}
7 R  u0 px c0 {5,S}
8 R  u0 px c0 {5,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-7.57, -2.61, 1.61, 4.87, 9.19, 11.68, 14.45], 'J/(mol*K)'),
        H298=(-529.03, 'kJ/mol'),
        S298=(-222.29, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHCH2XCH2 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  RC--R--CR2
  ||     |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 102,
    label = "RC-*=R=C-*R",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {5,S}
3 C  u0 p0 c0 {1,S} {4,D} {6,S}
4 R!H  u0 p0 c0 {3,D} {5,D}
5 C  u0 p0 c0 {2,S} {4,D} {7,S}
6 R  u0 px c0 {3,S}
7 R  u0 px c0 {5,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.01, 7.65, 10.53, 12.32, 14.26, 15.17, 16.03], 'J/(mol*K)'),
        H298=(-370.79, 'kJ/mol'),
        S298=(-196.35, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHCXCH single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  RC==R==CR
   |     |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 103,
    label = "RC-*=R=C=*",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {5,D}
3 C  u0 p0 c0 {1,S} {4,D} {6,S}
4 R!H  u0 p0 c0 {3,D} {5,D}
5 C  u0 p0 c0 {2,D} {4,D}
6 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.81, 3.88, 6.24, 7.94, 10.04, 11.14, 12.17], 'J/(mol*K)'),
        H298=(-432.93, 'kJ/mol'),
        S298=(-179.15, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHCXC single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  RC==R==C
   |     ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 104,
    label = "O-*-C-O-*",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {5,S}
3 O  u0 p2 c0 {1,S} {4,S}
4 C  u0 p0 c0 {3,S} {5,S}
5 O  u0 p2 c0 {2,S} {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.33, 6.34, 8.03, 9.06, 10.2, 10.82, 11.57], 'J/(mol*K)'),
        H298=(-354.62, 'kJ/mol'),
        S298=(-179.72, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged OC(XO)XO and H2C(XO)XO on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
   O--R--O
   |     |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 105,
    label = "RC-*=R-O-*",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {5,S}
3 C  u0 p0 c0 {1,S} {4,D} {6,S}
4 R!H  u0 px c0 {3,D} {5,S}
5 O  u0 p2 c0 {2,S} {4,S}
6 R  u0 px c0 {3,S} 
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.77, 6.69, 9.4, 11.28, 13.55, 14.75, 15.95], 'J/(mol*K)'),
        H298=(-446.49, 'kJ/mol'),
        S298=(-211.15, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHCHXO single and single -bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  RC==R--O
   |     |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 106,
    label = "C-*R2",
    group =
"""
1 * X u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 R!H u0  px c0 {2,D}
4 R  u0  px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.32, 3.63, 5.87, 7.37, 9.08, 9.94, 10.77], 'J/(mol*K)'),
        H298=(-285.22, 'kJ/mol'),
        S298=(-171.81, 'J/(mol*K)'),
    ),
    shortDesc=u"""Averaged from all children on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 107,
    label = "C=*RCR2",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 C  u0 p0 c0 {3,S} {4,S} {5,D}
3 C  u0 p0 c0 {1,D} {2,S} {6,S}
4 R  u0 px c0 {2,S}
5 R!H  u0 px c0 {2,D}
6 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.82, 4.08, 6.24, 7.7, 9.5, 10.49, 11.57], 'J/(mol*K)'),
        H298=(-379.17, 'kJ/mol'),
        S298=(-179.05, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCHCHCH2 and XCHCHO on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   CR2
   |
   C-R
  ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 108,
    label = "C#*CR2",
    group =
"""
1 * X u0 p0 c0 {3,T}
2 C  u0 p0 c0 {3,S} {4,S} {5,D}
3 C  u0 p0 c0 {1,T} {2,S}
4 R  u0 px c0 {2,S}
5 R!H  u0 px c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.45, 2.64, 4.89, 6.54, 8.67, 9.9, 11.29], 'J/(mol*K)'),
        H298=(-565.15, 'kJ/mol'),
        S298=(-180.28, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCCHCH2 and XCCHO triple-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   CR2
   |
   C
  |||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 109,
    label = "O-*CR2",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 C  u0 p0 c0 {3,S} {4,S} {5,D}
3 O  u0 p2 c0 {1,S} {2,S}
4 R  u0 px c0 {2,S}
5 R!H  u0 px c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([11.17, 13.37, 14.54, 15.21, 15.91, 16.23, 16.51], 'J/(mol*K)'),
        H298=(-228.04, 'kJ/mol'),
        S298=(-194.23, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XOCHCH2, HOC(O)XO, HC(O)XO on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   CR2
   |
   O
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 110,
    label = "C*RC*",
    group =
"""
1 * X u0 {3,[S,D,T]}
2 X u0 {4,[S,D,T]}
3 C  u0 {1,[S,D,T]} {5,[S,D,T]}
4 C  u0 {2,[S,D,T]} {5,[S,D,T]}
5 R!H  u0 {3,[S,D,T]} {4,[S,D,T]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.71, 5.77, 9.02, 11.15, 13.56, 14.75, 15.84], 'J/(mol*K)'),
        H298=(-461.69, 'kJ/mol'),
        S298=(-209.35, 'J/(mol*K)'),
    ),
    shortDesc=u"""Averaged from all child nodes on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 111,
    label = "R*bridged-bidentate",
    group =
"""
1 * X  u0 {3,[S,D,T]}
2 X  u0 {4,[S,D,T]}
3 R!H ux {1,[S,D,T]} {5,[S,D,T]}
4 R!H ux {2,[S,D,T]} {5,[S,D,T]}
5 R!H ux {3,[S,D,T]} {4,[S,D,T]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.19, 5.91, 8.92, 10.88, 13.11, 14.22, 15.28], 'J/(mol*K)'),
        H298=(-446.4, 'kJ/mol'),
        S298=(-205.52, 'J/(mol*K)'),
    ),
    shortDesc=u"""Averaged from all child nodes on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 112,
    label = "C*RO*",
    group =
"""
1 * X u0 {3,[S,D,T]}
2 X u0 {4,S}
3 C  u0 {1,[S,D,T]} {5,[S,D,T]}
4 O  u0 p2 {2,S} {5,S}
5 R!H  u0 px {3,[S,D,T]} {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.77, 6.69, 9.4, 11.28, 13.55, 14.75, 15.95], 'J/(mol*K)'),
        H298=(-446.49, 'kJ/mol'),
        S298=(-211.15, 'J/(mol*K)'),
    ),
    shortDesc=u"""Same as child node RC-*=R-O-*""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 113,
    label = "O*RO*",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,S}
3 O  u0 p2 c0 {1,S} {5,S}
4 O  u0 p2 c0 {2,S} {5,S}
5 R!H  u0 px c0 {3,S} {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.33, 6.34, 8.03, 9.06, 10.2, 10.82, 11.57], 'J/(mol*K)'),
        H298=(-354.62, 'kJ/mol'),
        S298=(-179.72, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged OC(XO)XO and H2C(XO)XO on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
   O--R--O
   |     |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 114,
    label = "C#*-R-C-*R2",
    group =
"""
1 * X u0 p0 c0 {3,T}
2 X u0 p0 c0 {5,S}
3 C  u0 p0 c0 {1,T} {4,S} 
4 R!H  u0 px c0 {3,S} {5,S}
5 C  u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
6 R  u0 px c0 {5,S}
7 R  u0 px c0 {5,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.53, 3.81, 6.89, 9.14, 12.06, 13.73, 15.5], 'J/(mol*K)'),
        H298=(-477.2, 'kJ/mol'),
        S298=(-200.61, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCCH2XCH2 double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  C--R--CR2
 |||    |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 115,
    label = "C#*-R=C-*R",
    group =
"""
1 * X u0 p0 c0 {3,T}
2 X u0 p0 c0 {5,S}
3 C  u0 p0 c0 {1,T} {4,S} 
4 R!H  u0 px c0 {3,S} {5,D}
5 C  u0 p0 c0 {2,S} {4,D} {6,S} 
6 R  u0 px c0 {5,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.8, 11.4, 13.67, 14.88, 16.0, 16.45, 16.74], 'J/(mol*K)'),
        H298=(-402.33, 'kJ/mol'),
        S298=(-202.29, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHCHXC single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  C--R==CR
 |||    |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 116,
    label = "C#*-R-C#*",
    group =
"""
1 * X u0 p0 c0 {3,T}
2 X u0 p0 c0 {5,T}
3 C  u0 p0 c0 {1,T} {4,S} 
4 R!H  u0 px c0 {3,S} {5,S}
5 C  u0 p0 c0 {2,T} {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-4.88, 4.76, 10.17, 13.18, 15.82, 16.67, 17.03], 'J/(mol*K)'),
        H298=(-671.16, 'kJ/mol'),
        S298=(-243.65, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCCH2XC single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  C--R--C
 |||   |||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 117,
    label = "RC=*-R-C=*R",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {5,D}
3 C  u0 p0 c0 {1,D} {4,S} {6,S}
4 R!H  u0 px c0 {3,S} {5,S}
5 C  u0 p0 c0 {2,D} {4,S} {7,S} 
6 R  u0 px c0 {3,S}
7 R  u0 px c0 {5,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.9, 10.63, 13.33, 14.98, 16.74, 17.49, 17.8], 'J/(mol*K)'),
        H298=(-230.02, 'kJ/mol'),
        S298=(-203.94, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHCH2XCH single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  RC--R--CR
  ||     ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 118,
    label = "C#*-R-C=*R",
    group =
"""
1 * X u0 p0 c0 {3,T}
2 X u0 p0 c0 {5,D}
3 C  u0 p0 c0 {1,T} {4,S} 
4 R!H  u0 px c0 {3,S} {5,S}
5 C  u0 p0 c0 {2,D} {4,S} {6,S} 
6 R  u0 p0 c0 {5,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.0, 5.76, 9.53, 11.98, 14.68, 15.93, 16.88], 'J/(mol*K)'),
        H298=(-457.3, 'kJ/mol'),
        S298=(-222.49, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHCH2XC single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  C--R--CR
 |||    ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 119,
    label = "C-*RN-*",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {5,S}
3 C u0 p0 c0 {1,S} {4,S} {5,D} 
4 R u0 px c0 {3,S}
5 N u0 p2 c0 {2,S} {3,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.48, 2.75, 4.98, 6.5, 8.18, 8.88, 9.19], 'J/(mol*K)'),
        H298=(-108.43, 'kJ/mol'),
        S298=(-174.03, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHXN on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
  RC=N
   | |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 120,
    label = "(OR)*",
    group =
"""
1 * X u0 p0 c0
2 O u0 p2 c0 {3,D}
3 R u0 px c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.0, 5.76, 9.53, 11.98, 14.68, 15.93, 16.88], 'J/(mol*K)'),
        H298=(-457.3, 'kJ/mol'),
        S298=(-222.49, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHCH2XC single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  C--R--CR
 |||    ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 121,
    label = "(ONR)*",
    group =
"""
1 * X u0 p0 c0
2 O u0 p2 c0 {3,D}
3 N u0 p1 c0 {2,D} {4,S}
4 R u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([11.39, 13.26, 14.34, 15.06, 15.98, 16.51, 16.97], 'J/(mol*K)'),
        H298=(-135.12, 'kJ/mol'),
        S298=(-184.06, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from ONOH*, and ONNH2* averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

    O=NR
     :
***********
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 122,
    label = "(ONOR)*",
    group =
"""
1 * X u0 p0 c0
2 O u0 p2 c0 {3,D}
3 N u0 p1 c0 {2,D} {4,S}
4 O u0 p2 c0 {3,S} {5,S}
5 R u0 px c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([10.87, 12.82, 14.04, 14.89, 16.01, 16.66, 17.21], 'J/(mol*K)'),
        H298=(-128.28, 'kJ/mol'),
        S298=(-185.24, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from ONOH* averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
  O=N-O-R
     :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 123,
    label = "(ONNR2)*",
    group =
"""
1 * X u0 p0 c0
2 O u0 p2 c0 {3,D}
3 N u0 p1 c0 {2,D} {4,S}
4 N u0 p2 c0 {3,S} {5,S} {6,S}
5 R u0 px c0 {4,S}
6 R u0 px c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([11.91, 13.69, 14.63, 15.23, 15.94, 16.35, 16.73], 'J/(mol*K)'),
        H298=(-141.96, 'kJ/mol'),
        S298=(-182.87, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from ONNH2* averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
  O=N-NR2
     :
***********
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 124,
    label = "C=*(-CR2)",
    group =
"""
1 * X u0  p0 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 R u0 px c0 {3,S}
5 R u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.0, 5.76, 9.53, 11.98, 14.68, 15.93, 16.88], 'J/(mol*K)'),
        H298=(-457.3, 'kJ/mol'),
        S298=(-222.49, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHCH2XC single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  C--R--CR
 |||    ||
***********
""",
    metal = "Pt",
    facet = "111",
)


tree(
"""
L1: R*
    L2: R*bridged-bidentate
        L3: C*RC*
            L4: C=*=R-C-*R2
            L4: R2C-*-R-C-*R2
            L4: RC=*-R=C-*R
            L4: RC-*=R-C-*R2
            L4: RC=*-R-C-*R2
            L4: RC-*=R=C-*R
            L4: RC-*=R=C=*
            L4: C#*-R-C-*R2
            L4: C#*-R=C-*R
            L4: C#*-R-C#*
            L4: RC=*-R-C=*R
            L4: C#*-R-C=*R
        L3: C*RO*
            L4: RC-*=R-O-*
        L3: O*RO*
            L4: O-*-C-O-*
    L2: R*bidentate
        L3: C*C*
            L4: C-*C-*
            L4: C=*RC=*R
            L4: C-*R2C-*R2
            L4: C-*R2C=*R
            L4: C-*RC=*
            L4: C=*RC-*R
            L4: C#*C-*R
            L4: C#*C-*R2
            L4: C#*C=*R
            L4: C-*R2C-*R
            L4: C-*RC-*R
        L3: C*N*
            L4: C-*R2N=*
            L4: C-*R2N-*R
            L4: C=*N-*
            L4: C=*RN=*
            L4: C=*RN-*R
            L4: C-*RN-*
        L3: C*O*
            L4: C=*RO-*
            L4: C-*R2O-*
        L3: N*N*
            L4: N-*RN-*R
            L4: N-*RN=*
        L3: N*O*
            L4: N=*O-*
        L3: O*O*
    L2: R*single-chemisorbed
        L3: C*
            L4: Cq*
            L4: C#*R
                L5: C#*CR3
                L5: C#*NR2
                L5: C#*OR
                L5: C#*CR2
            L4: C=*R2
                L5: C=*RCR3
                L5: C=*RNR2
                L5: C=*ROR
                L5: C=*RCR2
            L4: C=*(=R)
                L5: C=*(=C)
                L5: C=*(=NR)
            L4: C-*R3
                L5: C-*R2CR3
                L5: C-*R2NR2
                L5: C-*R2OR
            L4: C-*R2
                L5: C-*RO
                L5: C-*RCR2
                L5: C-*RNR
        L3: N*
            L4: N#*
            L4: N=*R
                L5: N=*CR3
                L5: N=*NR2
                L5: N=*OR
            L4: N-*R2
                L5: N-*RCR3
                L5: N-*RNR2
                L5: N-*ROR
            L4: N-*R
                L5: N-*CR2
                L5: N-*NR
        L3: O*
            L4: O=*
            L4: O-*R
                L5: O-*CR3
                L5: O-*CR2
                L5: O-*NR2
                L5: O-*OR
    L2: R*vdW
        L3: (CR4)*
            L4: (CR3CR3)*
            L4: (CR3NR2)*
            L4: (CR3OR)*
        L3: (CR3)*
            L4: (CR2NR)*
            L4: (CR2CR)*
            L4: (CR2O)*
        L3: (CR2)*
            L4: (CRN)*
            L4: (CRCR)*
        L3: (NR3)*
            L4: (NR2NR2)*
            L4: (NR2OR)*
        L3: (N=[O,N]R)*
            L4: (NRO)*
            L4: (NRNR)*
        L3: (OR2)*
            L4: (OROR)*
        L3: (OR)*
            L4: (ONR)*
                L5: (ONOR)*
                L5: (ONNR2)*
""",
)
