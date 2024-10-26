import maya.cmds
import random
import math
# Set World Space Transform position vector
def setWStransform(obj,position):
	maya.cmds.xform( obj, ws=True, t=(position[0],position[1],position[2]) )