import bpy
import globalVar


def hello(rotSpeed, curRot):
    scn = bpy.context.scene
    currentFrame = scn.frame_current
    fps = scn.render.fps
    
    time = currentFrame / fps
    
    dt = time - globalVar.prevTime
    
    newRot = curRot + rotSpeed * dt
    
    globalVar.prevTime = time
    
    return newRot

bpy.app.driver_namespace['ReturnOne'] = hello