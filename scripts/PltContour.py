#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 16:13:19 2020

@author: D. Li (lMU)
"""
from pandas import read_csv as rd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.interpolate import griddata

#%% load data from WaveQLab output
folder ='/import/freenas-m-05-seissol/dli/ExaHyPE/TPV5/contour/'
waveq_file = folder+'waveq_conf.dat'
waveq = np.loadtxt(waveq_file,comments='#',skiprows=16)

x1 = waveq[:,0]/1e3
y1 = waveq[:,1]/1e3
ar_waveq = waveq[:,2]

nfilter = np.where(ar_waveq<12.1) # filter out 1e9

x1 = x1[nfilter] + 20
y1 = y1[nfilter]
ar_waveq=ar_waveq[nfilter]

points1 = np.zeros((len(x1),2))
points1[:,0] = np.array(x1[:])
points1[:,1] = np.array(y1[:])

xgrid1,ygrid1 = np.mgrid[0:50:100j,0:25:50j]
grid_waveq = griddata(points1, ar_waveq, (xgrid1, ygrid1), method='linear')

# %% setup folder and prefix for input and output folder
model = 'fault_out'
figout = folder + model+'_contour'+'.png'

# load arrival time data from .csv 
fname = folder + model + '.csv'
figout = model + '.png'
data1 = rd(fname,sep=',')
ar_all = data1['Q:7'] # arrival time

# set grid data of arrival time
xgrid,ygrid = np.mgrid[0:40:80j,0:30:60j]

z_all = data1["coordinates:2"]
y_all = data1["coordinates:1"]

points = np.zeros((len(z_all),2))
points[:,0] = np.array(z_all[:])
points[:,1] = np.array(y_all[:])

grid_z2 = griddata(points, ar_all, (xgrid, ygrid), method='linear')

#%% set 0.5 sec contours of arrival times
cf = np.linspace(0.5,12.0,num=23)

# plot
fig,ax = plt.subplots()

# ExaSeis data
cntr1 = ax.contour(np.transpose(grid_z2),cf,cmap='plasma')
# WaveQLab data
cntr2 = ax.contour(np.transpose(grid_waveq),cf,cmap='plasma',linestyles='dashed')

plt.xlabel('fault parallel (km)')
plt.ylabel('downdip distance (km)')

h1,_ = cntr1.legend_elements()
h2,_ = cntr2.legend_elements()
ax.legend([h1[0], h2[0]], ['ExaSeis', 'WaveQLab'])


plt.ylim(0,30)
plt.xlim(10,70)
#plt.show()
plt.savefig(figout,dpi=100)

