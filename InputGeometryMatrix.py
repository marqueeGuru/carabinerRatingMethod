#Author- me
#Description- test

import adsk.core, adsk.fusion, adsk.cam, traceback
from array import *

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        design = adsk.fusion.Design.cast(app.activeProduct)
        
        # Get the root component of the active design.
        rootComp = design.rootComponent        
        
        sketches = rootComp.sketches;
        xyPlane = rootComp.xYConstructionPlane
        sketch = sketches.add(xyPlane)
        lines = sketch.sketchCurves.sketchLines;
        extrudes = rootComp.features.extrudeFeatures
        prof = adsk.core.ObjectCollection.create()
        # Get sketch health state
        health = sketch.healthState
        if health == adsk.fusion.FeatureHealthStates.ErrorFeatureHealthState or health == adsk.fusion.FeatureHealthStates.WarningFeatureHealthState:        
            msg = sketch.errorOrWarningMessage
        
        tempCount = 0           
        xs, ys = (60, 110)
        # geometry = [[0 for i in range(ys)] for j in range(xs)]

        # for x in geometry:
        #     for y in x:
        #         point = adsk.core.Point3D.create(0.5*x, 0.5*y, 0)
        #         geometry[x][y] = body.pointContainment(point)
        
        f = open(r"/Users/jaccuzi/Documents/PROJECTALG/GENALGcode/GENCURRENT/PART4.txt", "r")
        mask = open(r"/Users/jaccuzi/Documents/PROJECTALG/GENALGcode/BaseGeometry.txt", "r")

        for y in range(0, ys):
            line = f.readline() # reading a line
            lineMask = mask.readline()
            for x in range(xs):
                tempBodyData = int(line[2*x])
                tempMaskData = int(lineMask[2*x])
                if tempBodyData!=tempMaskData:        # Create a new sketch on the xy plane.
                    # Draw a rectangle by two points.
                    recLines = lines.addTwoPointRectangle(adsk.core.Point3D.create(x/20, y/20, 0), adsk.core.Point3D.create(x/20 + 0.5/10, y/20 + 0.5/10, 0))
            if sketch.profiles.count != 0:
                for i in range(0, sketch.profiles.count):
                    prof.add(sketch.profiles.item(i))
                distance = adsk.core.ValueInput.createByReal(1)
                extrude1 = extrudes.addSimple(prof, distance, adsk.fusion.FeatureOperations.CutFeatureOperation)        
                body1 = extrude1.bodies.item(0)    

                body1.name = "simple"
                health = extrude1.healthState
                if health == adsk.fusion.FeatureHealthStates.WarningFeatureHealthState or health == adsk.fusion.FeatureHealthStates.ErrorFeatureHealthState:
                    message = extrude1.errorOrWarningMessage
                    
                timeline = design.timeline
                timelineObj = timeline.item(timeline.count - 1);
                health = timelineObj.healthState
                message = timelineObj.errorOrWarningMessage
                prof.clear()

            sketch.deleteMe()
            sketch = sketches.add(xyPlane)
            lines = sketch.sketchCurves.sketchLines;
            health = sketch.healthState
            if health == adsk.fusion.FeatureHealthStates.ErrorFeatureHealthState or health == adsk.fusion.FeatureHealthStates.WarningFeatureHealthState:        
                msg = sketch.errorOrWarningMessage


        f.close()

        ui.messageBox('sucessfull test')


    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
