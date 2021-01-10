#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 16:13:19 2020

@author: D. Li (lMU)
"""


import numpy as np
import sys
import os


# set up time step and dt in fault output files .pvtu 
ndt = 121
dt = 0.1

# set up folder of output
folder = '/import/freenas-m-05-seissol/dli/ExaHyPE/TPV5/fault_79/'
prefix = 'fout_'

# outpuf pvd filename
fout = "tpv5-fault-out.pvd"
f1 = open(fout,'w')


# write out a pvd file
f1.write("<?xml version=\"1.0\"?>\n")
f1.write("<VTKFile type=\"Collection\" version=\"0.1\" byte_order=\"LittleEndian\">\n")
f1.write("<Collection>\n")

for i in range(0,ndt,5):
	f1.write('%s%6.3f%s%s%s%d%s\n' %("<DataSet timestep=\"",i*dt,"\" group=\"\" part=\"0\" file=\"",folder,prefix,i,".pvtu\"/>"))

f1.write("</Collection>\n")
f1.write("</VTKFile>\n")
f1.close()

