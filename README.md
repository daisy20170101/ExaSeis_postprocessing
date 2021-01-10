# ExaSeis_postprocessing
scripts for ExaSeis post-processing

## Load on-fault variables from ExaSeis output
$$ python WritePVD.py

(create a .pvd file containing the last step .pvtu)

$$ pvpython LoadContourData.py 

(create a fault_out.csv file containing arrival time for each points on the fault)

## Plot contour of arrival time and make a comparison with SCEC benchmark
$$ python PltContour.py

(create a plot for comparison of contour plot. WaveQLab contour data is written in contour/waveq_conf.data.  Please change the x- and y-range accordingly to the coorodinates in ExaSeis)

![image](https://github.com/daisy20170101/ExaSeis_postprocessing/blob/main/figures/fault_coutour.png)


