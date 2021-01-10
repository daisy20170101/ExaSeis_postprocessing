# trace generated using paraview version 5.6.2
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'PVD Reader'
tpv5faultseriespvd = PVDReader(FileName='/import/freenas-m-05-seissol/dli/ExaHyPE/TPV5/tpv5-fault-out.pvd')
tpv5faultseriespvd.CellArrays = ['Q']

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.AnimationTime = 11.9
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [2070, 1276]

# show data in view
tpv5faultseriespvdDisplay = Show(tpv5faultseriespvd, renderView1)

# trace defaults for the display properties.
tpv5faultseriespvdDisplay.Representation = 'Surface'
tpv5faultseriespvdDisplay.ColorArrayName = [None, '']
tpv5faultseriespvdDisplay.EdgeColor = [1.0, 0.9999694819562066, 0.9999847409781033]
tpv5faultseriespvdDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
tpv5faultseriespvdDisplay.SelectOrientationVectors = 'None'
tpv5faultseriespvdDisplay.ScaleFactor = 3.95
tpv5faultseriespvdDisplay.SelectScaleArray = 'None'
tpv5faultseriespvdDisplay.GlyphType = 'Arrow'
tpv5faultseriespvdDisplay.GlyphTableIndexArray = 'None'
tpv5faultseriespvdDisplay.GaussianRadius = 0.1975
tpv5faultseriespvdDisplay.SetScaleArray = [None, '']
tpv5faultseriespvdDisplay.ScaleTransferFunction = 'PiecewiseFunction'
tpv5faultseriespvdDisplay.OpacityArray = [None, '']
tpv5faultseriespvdDisplay.OpacityTransferFunction = 'PiecewiseFunction'
tpv5faultseriespvdDisplay.DataAxesGrid = 'GridAxesRepresentation'
tpv5faultseriespvdDisplay.SelectionCellLabelFontFile = ''
tpv5faultseriespvdDisplay.SelectionPointLabelFontFile = ''
tpv5faultseriespvdDisplay.PolarAxes = 'PolarAxesRepresentation'
tpv5faultseriespvdDisplay.ScalarOpacityUnitDistance = 0.7585205907349032

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tpv5faultseriespvdDisplay.OSPRayScaleFunction.Points = [-11.098907470703125, 0.0, 0.5, 0.0, -8.762530326843262, 0.0, 0.5, 0.0, -8.694214871847134, 0.28125, 0.15094318985939026, 0.0, -7.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tpv5faultseriespvdDisplay.ScaleTransferFunction.Points = [-11.098907470703125, 0.0, 0.5, 0.0, -8.762530326843262, 0.0, 0.5, 0.0, -8.694214871847134, 0.28125, 0.15094318985939026, 0.0, -7.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tpv5faultseriespvdDisplay.OpacityTransferFunction.Points = [-11.098907470703125, 0.0, 0.5, 0.0, -8.762530326843262, 0.0, 0.5, 0.0, -8.694214871847134, 0.28125, 0.15094318985939026, 0.0, -7.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tpv5faultseriespvdDisplay.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
tpv5faultseriespvdDisplay.DataAxesGrid.XTitleFontFile = ''
tpv5faultseriespvdDisplay.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
tpv5faultseriespvdDisplay.DataAxesGrid.YTitleFontFile = ''
tpv5faultseriespvdDisplay.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
tpv5faultseriespvdDisplay.DataAxesGrid.ZTitleFontFile = ''
tpv5faultseriespvdDisplay.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
tpv5faultseriespvdDisplay.DataAxesGrid.XLabelFontFile = ''
tpv5faultseriespvdDisplay.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
tpv5faultseriespvdDisplay.DataAxesGrid.YLabelFontFile = ''
tpv5faultseriespvdDisplay.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
tpv5faultseriespvdDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tpv5faultseriespvdDisplay.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
tpv5faultseriespvdDisplay.PolarAxes.PolarAxisTitleFontFile = ''
tpv5faultseriespvdDisplay.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
tpv5faultseriespvdDisplay.PolarAxes.PolarAxisLabelFontFile = ''
tpv5faultseriespvdDisplay.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
tpv5faultseriespvdDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
tpv5faultseriespvdDisplay.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
tpv5faultseriespvdDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(tpv5faultseriespvdDisplay, ('CELLS', 'Q', '7'))

# rescale color and/or opacity maps used to include current data range
tpv5faultseriespvdDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
tpv5faultseriespvdDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Q'
qLUT = GetColorTransferFunction('Q')

# get opacity transfer function/opacity map for 'Q'
qPWF = GetOpacityTransferFunction('Q')

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(Input=tpv5faultseriespvd)

# show data in view
cellDatatoPointData1Display = Show(cellDatatoPointData1, renderView1)

# trace defaults for the display properties.
cellDatatoPointData1Display.Representation = 'Surface'
cellDatatoPointData1Display.ColorArrayName = [None, '']
cellDatatoPointData1Display.EdgeColor = [1.0, 0.9999694819562066, 0.9999847409781033]
cellDatatoPointData1Display.OSPRayScaleArray = 'Q'
cellDatatoPointData1Display.OSPRayScaleFunction = 'PiecewiseFunction'
cellDatatoPointData1Display.SelectOrientationVectors = 'None'
cellDatatoPointData1Display.ScaleFactor = 3.95
cellDatatoPointData1Display.SelectScaleArray = 'None'
cellDatatoPointData1Display.GlyphType = 'Arrow'
cellDatatoPointData1Display.GlyphTableIndexArray = 'None'
cellDatatoPointData1Display.GaussianRadius = 0.1975
cellDatatoPointData1Display.SetScaleArray = ['POINTS', 'Q']
cellDatatoPointData1Display.ScaleTransferFunction = 'PiecewiseFunction'
cellDatatoPointData1Display.OpacityArray = ['POINTS', 'Q']
cellDatatoPointData1Display.OpacityTransferFunction = 'PiecewiseFunction'
cellDatatoPointData1Display.DataAxesGrid = 'GridAxesRepresentation'
cellDatatoPointData1Display.SelectionCellLabelFontFile = ''
cellDatatoPointData1Display.SelectionPointLabelFontFile = ''
cellDatatoPointData1Display.PolarAxes = 'PolarAxesRepresentation'
cellDatatoPointData1Display.ScalarOpacityUnitDistance = 0.7585205907349032

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
cellDatatoPointData1Display.OSPRayScaleFunction.Points = [-11.098907470703125, 0.0, 0.5, 0.0, -8.762530326843262, 0.0, 0.5, 0.0, -8.694214871847134, 0.28125, 0.15094318985939026, 0.0, -7.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
cellDatatoPointData1Display.ScaleTransferFunction.Points = [-11.098907470703125, 0.0, 0.5, 0.0, -8.762530326843262, 0.0, 0.5, 0.0, -8.694214871847134, 0.28125, 0.15094318985939026, 0.0, -7.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
cellDatatoPointData1Display.OpacityTransferFunction.Points = [-11.098907470703125, 0.0, 0.5, 0.0, -8.762530326843262, 0.0, 0.5, 0.0, -8.694214871847134, 0.28125, 0.15094318985939026, 0.0, -7.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
cellDatatoPointData1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.DataAxesGrid.XTitleFontFile = ''
cellDatatoPointData1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.DataAxesGrid.YTitleFontFile = ''
cellDatatoPointData1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.DataAxesGrid.ZTitleFontFile = ''
cellDatatoPointData1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.DataAxesGrid.XLabelFontFile = ''
cellDatatoPointData1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.DataAxesGrid.YLabelFontFile = ''
cellDatatoPointData1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
cellDatatoPointData1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.PolarAxes.PolarAxisTitleFontFile = ''
cellDatatoPointData1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.PolarAxes.PolarAxisLabelFontFile = ''
cellDatatoPointData1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.PolarAxes.LastRadialAxisTextFontFile = ''
cellDatatoPointData1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# hide data in view
Hide(tpv5faultseriespvd, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(cellDatatoPointData1Display, ('POINTS', 'Q', '7'))

# rescale color and/or opacity maps used to include current data range
cellDatatoPointData1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
cellDatatoPointData1Display.SetScalarBarVisibility(renderView1, True)

# change representation type
cellDatatoPointData1Display.SetRepresentationType('Points')

# save data
SaveData('/import/freenas-m-05-seissol/dli/ExaHyPE/TPV5/fault_out.csv', proxy=cellDatatoPointData1)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [127.91600689897066, 19.75, 19.75]
renderView1.CameraFocalPoint = [20.0, 19.75, 19.75]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 27.93071785686863

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
