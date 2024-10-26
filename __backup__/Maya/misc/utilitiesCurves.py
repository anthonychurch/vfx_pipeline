import maya.cmds
import random
import math


"""
USAGE :  This tool creates a spline curve that has its CV's position exactly where you want them. I have used this mainly in creating a spline curve that positions it's CV's on every second joint in a chain, when creating a spline IK rig.

REQUIRES:
1. utilities.setWStransform
2. utilities.getWStransform

INPUTS :
1. objArray = Array String
2. name = String
3. grp = String

OUTPUT :
1. rename = String
2. howManyObjs = Integer

NOTES : 
1. NA
""" 
def createCurve(objArray,name,grp):
	howManyObjs = len(objArray)
	print ('howManyObjs = ' + str(howManyObjs))
	points =''
	pos1 = (0,0,0)
	for i in range(0,howManyObjs,1):
		print ('i = ' + str(i))
		if(i != 1):
			pos = getWStransform(objArray[i])
			p = '(' + str(pos[0]) + ',' + str(pos[1]) + ',' + str(pos[2]) + ')'
			print('p = ' + str(p))
			if(i != howManyObjs-1):
				p = p + ', '
		else:
			pos1 = getWStransform(objArray[i])
			print('pos1 = ' + str(pos1))
		points = points + p
		print('points = ' + str(points))

	eval('maya.cmds.curve(p=[' + points + '])')
	curve = maya.cmds.ls(selection=True)
	print ('curve = ' + str(curve))
	rename = maya.cmds.rename(curve,name)
	maya.cmds.parent(rename,grp)
	setWStransform(str(rename) + '.cv[1]',pos1)

	#returns name of curve and number of CV's
	return (rename,howManyObjs-1)
	
	
"""
USAGE :  This tool creates a spline curve that has its CV's position exactly where you want them. I have used this mainly in creating a spline curve that positions it's CV's on every second joint in a chain, when creating a spline IK rig.

REQUIRES:
1. utilities.setWStransform
2. utilities.getWStransform

INPUTS :
1. name = String
2. colour = Integer
3. axis = Vector
4. scle = Vector

OUTPUT :
1. name = String

NOTES : 
1. NA
""" 
def createCrossCtrl(name,colour,axis,scle):
	maya.cmds.curve(p=[(-2,0,-10),(-2,0,-10),(-2,0,-10),(-2,0,-2),(-2,0,-2),(-2,0,-2),(-10,0,-2),(-10,0,-2),(-10,0,-2),(-10,0,2),(-10,0,2),(-10,0,2),(-2,0,2),(-2,0,2),(-2,0,2),(-2,0,10),(-2,0,10),(-2,0,10),(2,0,10),(2,0,10),(2,0,10),(2,0,2),(2,0,2),(2,0,2),(10,0,2),(10,0,2),(10,0,2),(10,0,-2),(10,0,-2),(10,0,-2),(2,0,-2),(2,0,-2),(2,0,-2),(2,0,-10),(2,0,-10),(2,0,-10)],k=[0,0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10,11,11,11,12,12,12])
	ctrl = maya.cmds.ls(selection=True)
	print('ctrl = ' + str(ctrl))
	maya.cmds.rename(ctrl,name)
	shpe = getShapeNodes(name)
	print('shpe[0][0] = ' + str(shpe[0][0]))
	maya.cmds.setAttr(str(shpe[0][0]) + '.overrideEnabled',1)
	maya.cmds.setAttr(str(shpe[0][0]) + '.overrideColor', colour)
	maya.cmds.setAttr(str(name) + '.rotate' + str(axis), 90)
	maya.cmds.setAttr(str(name) + '.scaleX', scle)
	maya.cmds.setAttr(str(name) + '.scaleY', scle)
	maya.cmds.setAttr(str(name) + '.scaleZ', scle)
	maya.cmds.makeIdentity( str(name), apply=True, t=1, r=1, s=1 )
	return name
	
	
"""
USAGE :  This tool creates a spline curve that has its CV's position exactly where you want them. I have used this mainly in creating a spline curve that positions it's CV's on every second joint in a chain, when creating a spline IK rig.

REQUIRES:
1. utilities.setWStransform
2. utilities.getWStransform

INPUTS :
1. name = String
2. colour = Integer
3. axis = Vector
4. scle = Vector

OUTPUT :
1. name = String

NOTES : 
1. NA
""" 
def createArrowCtrl(name,colour,axis,scle):
	maya.cmds.curve(p=[(0,0,-14),(0,0,-14),(-4,0,-10),(-4,0,-10),(-4,0,-10),(-2,0,-10),(-2,0,-10),(-2,0,-10),(-2,0,-2),(-2,0,-2),(-2,0,-2),(-10,0,-2),(-10,0,-2),(-10,0,-2),(-10,0,-4),(-10,0,-4),(-10,0,-4),(-14,0,0),(-14,0,0),(-14,0,0),(-10,0,4),(-10,0,4),(-10,0,4),(-10,0,2),(-10,0,2),(-10,0,2),(-2,0,2),(-2,0,2),(-2,0,2),(-2,0,10),(-2,0,10),(-2,0,10),(-4,0,10),(-4,0,10),(-4,0,10),(0,0,14),(0,0,14),(0,0,14),(4,0,10),(4,0,10),(4,0,10),(2,0,10),(2,0,10),(2,0,10),(2,0,2),(2,0,2),(2,0,2),(10,0,2),(10,0,2),(10,0,2),(10,0,4),(10,0,4),(10,0,4),(14,0,0),(14,0,0),(14,0,0),(10,0,-4),(10,0,-4),(10,0,-4),(10,0,-2),(10,0,-2),(10,0,-2),(2,0,-2),(2,0,-2),(2,0,-2),(2,0,-10),(2,0,-10),(2,0,-10),(4,0,-10),(4,0,-10),(4,0,-10),(0,0,-14),(0,0,-14)],k=[0,0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10,11,11,11,12,12,12,13,13,13,14,14,14,15,15,15,16,16,16,17,17,17,18,18,18,19,19,19,20,20,20,21,21,21,22,22,22,23,23,23,24,24,24])
	ctrl = maya.cmds.ls(selection=True)
	print('ctrl = ' + str(ctrl))
	maya.cmds.rename(ctrl,name)
	shpe = getShapeNodes(name)
	print('shpe[0][0] = ' + str(shpe[0][0]))
	maya.cmds.setAttr(str(shpe[0][0]) + '.overrideEnabled',1)
	maya.cmds.setAttr(str(shpe[0][0]) + '.overrideColor', colour)
	maya.cmds.setAttr(str(name) + '.rotate' + str(axis), 90)
	maya.cmds.setAttr(str(name) + '.scaleX', scle)
	maya.cmds.setAttr(str(name) + '.scaleY', scle)
	maya.cmds.setAttr(str(name) + '.scaleZ', scle)
	maya.cmds.makeIdentity( str(name), apply=True, t=1, r=1, s=1 )
	return name