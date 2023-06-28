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
        body = rootComp.bRepBodies.item(0)
        
        xs, ys = (60, 110)
        # geometry = [[0 for i in range(ys)] for j in range(xs)]

        # for x in geometry:
        #     for y in x:
        #         point = adsk.core.Point3D.create(0.5*x, 0.5*y, 0)
        #         geometry[x][y] = body.pointContainment(point)
        
        f = open(r"/Users/jaccuzi/Documents/PROJECTALG/GENALGcode/BaseGeometry.txt", "w")
        for y in range(ys):
            for x in range(xs):
                point = adsk.core.Point3D.create(0.05*x, 0.05*y, 0.5)
                if body.pointContainment(point)==0 or body.pointContainment(point)==1:
                    f.write(str(1))
                else:
                    f.write(str(0))
                f.write(" ")
            f.write("\n")

        f.close()

        ui.messageBox('sucessfully created a matrix')


    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
