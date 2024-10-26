#import maya.cmds
#import random
#import math
# USE : test whether a particular attribute exists on a maya node and that its attributes have the correct parameters 
# NOTES : NA

def checkAttrExist(obj,attr,type,min,max,default,keyable,replace):
	attrExist = maya.cmds.attributeQuery(attr, node=obj, exists=True)
	print('checkAttrExist :: attrExist = ' + str(attrExist) + ' : attr = ' + str(attr))
	newAttr = ''
	if(attrExist == False):
		newAttr = maya.cmds.addAttr(obj, longName=attr, at=type, defaultValue=default, minValue=min, maxValue=max )
		#print('checkAttrExist :: newAttr = ' + str(newAttr))

		if(keyable == True):
			maya.cmds.setAttr(obj + '.' + attr, e=True, keyable=True)
		else:
			maya.cmds.setAttr(obj + '.' + attr, e=True, keyable=False, channelBox=True)
		#print('checkAttrExist :: newAttr = ' + str(newAttr) )
	else:
		if(replace == True):
			maya.cmds.deleteAttr(obj, at=attr)
			newAttr = maya.cmds.addAttr(obj, longName=attr, at=type, defaultValue=default, minValue=min, maxValue=max )

			if(keyable == True):
				maya.cmds.setAttr(obj + '.' + attr, e=True, keyable=True)
			else:
				maya.cmds.setAttr(obj + '.' + attr, e=True, keyable=False, channelBox=True)
			#print('checkAttrExist :: newAttr = ' + str(newAttr) )
	return (attrExist,newAttr)