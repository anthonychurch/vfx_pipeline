import sys


# Import Python and Maya modules
import maya.cmds
import random
import math


# Import custom modules
import utilities as utl # Generic utility functions that is meant to be used for multiply tasks in Maya.
import utilitiesCurves as uCrv # Maya Curve related utility functions.
import utilitiesRigging as uRig # Maya Rigging related utility functions.
import utilitiesUI as ui # Maya UI Element related utility functions.

#print(ui)

###############################################################################################
#   INSTRUCTIONS FOR USE.
#	TODO:	
#	1. TODO
#	2. TODO
#	3. TODO
###############################################################################################


# Define local UI Variables
line1 = '	USE THE FOLLOWING BUTTONS TO CREATE CURVE CONTROLS.'
line2 = '	THE RIGGING COLOUR STANDARDS ARE AS FOLLOWS:'
line3 = '	ARRAY KEY ARE 0=Right, 1=Left, 2=Centre, 3=Misc'
line4 = '	THE MAYA NODE "overrideColor" ATTRIBUTES VALUES ARE:'
line5 = '	1. IKcolour = [14,13,17]'
line6 = '	2. FKColour = [23,31,25]'
line7 = '	3. splineIKColour = [6,15,29]'
line8 = '	4. clothColour = [9,30,21]'
line9 = '	3. faceColour = [22,10,26]'
line10 = '	4. misc = [4,7,11]'


ver = ' : ver 01.001 ' # This needs to be updated each time the script is updated or modified.
windowTitle = 'Create Control Curves for Rigs' + ver
rebuildWindowName = 'CreateCtrlCrvsRigging'

# Define Rigging Colour Standards
# 0=Right, 1=Left, 2=Centre, 3=Misc
IKcolour = [14,13,17]
FKColour = [23,31,25]
splineIKColour = [6,15,29]
clothColour = [9,30,21]
faceColour = [22,10,26]
misc = [4,7,11]

textAlign = 'left'


# Define local functions
def buildWindow(thisModule,uiModule,windowName,windowTitle, line01, line02, line03, line04, line05, line06, line07, line08, line09, line10):
	questionButtonHeight=23
	maya.cmds.window( windowName, title= windowTitle, s=True, iconName='Short Name', widthHeight=(500, 600))
	
	maya.cmds.frameLayout(  windowName + '_frameLayout1', label=' ', borderStyle="in", lv=False, bv=False, mw=10, mh=10)
	maya.cmds.columnLayout(windowName + '_column1', adjustableColumn=True)

	maya.cmds.text( label= '   ' )

	maya.cmds.rowLayout(windowName + '_row1',numberOfColumns=3, columnWidth3=(80, 80, 80), adjustableColumn3=3, columnAlign3=('left','left','left'), columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)])
	
	maya.cmds.text( label= ' row1 C1 ' )
	maya.cmds.text( label= ' row1 C2 ' )
	maya.cmds.text( label= ' row1 C3 ' )
	maya.cmds.setParent('..')

	maya.cmds.text( label= '   ' )

	maya.cmds.frameLayout(windowName + '_formBase', label='Tabs', lv=False, labelAlign='top', borderStyle='in')
	#maya.cmds.rowLayout(windowName + '_row2',numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn2=2, columnAlign2=('left','left'), columnAttach=[(1, 'both', 0), (2, 'both', 0)])
	maya.cmds.rowColumnLayout(windowName + '_row2', numberOfColumns=2,columnWidth=[(1,450),(2,20)])
	
	# _row2 Column 1 
	#maya.cmds.setParent('..')
	maya.cmds.columnLayout(windowName + '_column1a', rowSpacing=3)
	
	maya.cmds.text( label= line02, align= textAlign )
	maya.cmds.text( label= line03, align= textAlign )
	maya.cmds.text( label= '', align= textAlign )
	maya.cmds.text( label= line04, align= textAlign )
	maya.cmds.text( label= line05, align= textAlign )
	maya.cmds.text( label= line06, align= textAlign )
	maya.cmds.text( label= line07, align= textAlign )
	maya.cmds.text( label= line08, align= textAlign )
	maya.cmds.text( label= line09, align= textAlign )
	maya.cmds.text( label= line10, align= textAlign )
	maya.cmds.text( label= '', align= textAlign )
	maya.cmds.text( label= line01, align= textAlign )
	maya.cmds.text( windowName + '_space1a', label='' )
	
	# _row2 Column 2 
	maya.cmds.setParent('..')
	maya.cmds.columnLayout(windowName + '_column1b', rowSpacing=3)
	
	maya.cmds.text( label= '' )
	maya.cmds.button(label='?', height = questionButtonHeight)
	maya.cmds.text( label= '' )
	maya.cmds.button(label='?', height = questionButtonHeight)
	maya.cmds.button(label='?', height = questionButtonHeight)
	maya.cmds.button(label='?', height = questionButtonHeight)
	maya.cmds.button(label='?', height = questionButtonHeight)
	maya.cmds.button(label='?', height = questionButtonHeight)
	maya.cmds.button(label='?', height = questionButtonHeight)
	maya.cmds.button(label='?', height = questionButtonHeight)
	maya.cmds.text( label= '' )
	maya.cmds.text( label= '' )
	maya.cmds.text( windowName + '_space1b', label='' )
	
	
	
	maya.cmds.setParent('..')

	
	

	maya.cmds.showWindow( windowName )


# Run the functions	
def runWindow(windowName):
	getSidePrefix = maya.cmds.textFieldButtonGrp( windowName + '_sidePrefix', q=True, text=True )
	sp = getSidePrefix.split()
	sidePrefix = ''
	if(len(sp) > 0):
		sidePrefix = sp[0] + '_'

	getJointType = maya.cmds.textFieldButtonGrp( windowName + '_jointType', q=True, text=True )
	jt = getJointType.split()
	jointType = ''
	if(len(jt) > 0):
		jointType = jt[0] + '_'

	prefix = sidePrefix + jointType
	
	# Retrieve selected joints as a String value
	getJoints = maya.cmds.textFieldButtonGrp( windowName + '_joints', q=True, text=True )
	jointsArray = getJoints.split()
	
	# Retrieve selected groups as a String value
	getGroups = maya.cmds.textFieldButtonGrp( windowName + '_groups', q=True, text=True )
	groupsArray = getGroups.split()
	
	ikJoints = uRig.duplicateSelectedJoints(getJoints,getSidePrefix,getJointType,getGroups)

	
# Run the functions	
# injectThisModule : String This parameter is this module injected into the buildWindow function so that the runWindow function can be called correctly
def run(injectThisModule,injectUIModule):
	# Clears the old instance of the window is it exists.
	ui.deleteWindow(rebuildWindowName) 
	
	# 
	buildWindow(injectThisModule,injectUIModule,rebuildWindowName,windowTitle,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10)
	
	
print("line 145 :: Imported uiRig_createControlCurves Module")