import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

num_pts=500

name='reactions'

CH4_diss=[]
C2H6_diss=[]
for k in range(num_pts):
    file="".join((name,'_',str(k),".py"))
    s=open('reactions.py','r')
    
  
####### CH4 + Pt + Pt <=> CH3X + CHX ###### 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 18," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])
                   CH4_diss.append(correction)
                   new_line=line.replace(old,old)
                   new_file_content += new_line   
              elif "    index = 19," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
    
####### C2H6 + Pt + Pt <=> CH2CH3X + CHX ###### 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 19," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                    old=line.strip()
                    bits=line.split("(")
                    correction=float(bits[1].split(",")[0])
                    C2H6_diss.append(correction)
                    new_line=line.replace(old,old)
                    new_file_content += new_line   
              elif "    index = 20," in line:  
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line    
                    break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
import matplotlib.gridspec as gridspec

#Makes the diagrams look nice and shiny
plt.rcParams['figure.figsize']=(7,6)
plt.rcParams['axes.linewidth'] = 2
plt.rc('xtick', labelsize=14)
plt.rc('ytick', labelsize=14)
plt.rc('axes', labelsize=16)
plt.rc('legend', fontsize=14)
plt.rcParams['lines.markersize'] = 10
plt.rcParams['xtick.direction']='in'
plt.rcParams['ytick.direction']='in'
plt.rcParams['xtick.major.size']=10
plt.rcParams['xtick.major.width']=2
plt.rcParams['ytick.major.size']=10
plt.rcParams['ytick.major.width']=2
plt.rcParams['legend.edgecolor']='k'
plt.rcParams['axes.unicode_minus']=False
plt.rcParams["legend.framealpha"] = 1
plt.rcParams['xtick.major.pad'] = 8
plt.rcParams['ytick.major.pad'] = 8
plt.rcParams['legend.handletextpad']=0.4
plt.rcParams['legend.columnspacing']=0.5
plt.rcParams['legend.labelspacing']=0.3
plt.rcParams['legend.title_fontsize'] = 14
plt.rcParams['axes.formatter.limits']=(-3, 6)

gs=gridspec.GridSpec(nrows=1, ncols=1)
gs.update(wspace=0.3, hspace=0.4)

ax0=plt.subplot(gs[0,0])

ax0.plot(CH4_diss, C2H6_diss, marker='o', linestyle='None')


