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
line_01 = '	TYPE IN THE SIDE PREFIX ie: L or R:-'
line_02 = '	TYPE IN THE NAME OF THE JOINT ie: IK or SPL:-'
line_03 = '	SELECT THE START JOINT IN THE JOINT CHAIN:-'
line_04 = '	SELECT THE MIDDLE JOINT IN THE JOINT CHAIN:-'
line_05 = '	(The Pole Vecotr Constraint will be attached this joint)'
line_06 = '	SELECT THE END JOINT IN THE JOINT CHAIN:-'
line_07 = '	SELECT THE MAIN CONTROL:-'
line_08 = '	SELECT THE CONTROL FOR THE POLE VECTOR:-'



ver = ' : ver 01.002 ' # This needs to be updated each time the script is updated or modified.
comment = 'Started with the appendBipedFootRigAddClaws tool, now fixing it up.'
windowTitle = 'create Main IK Handles' + ver
rebuildWindowName = 'createMainIKhandles'

# Declare Variables
sidePrefix = 'L_'
jointType = 'IK_'
limbTypeName = 'leg_'
prefix = sidePrefix + jointType
pvDistance = 0
howManyTweenJoints = 0


# Declare Window format Variables
axis = "y"
scale = 1
textAlign = 'left'



# Define local functions
def buildWindow(thisModule,uiModule,windowName,windowTitle, line01, line02, line03, line04, line05, line06, line07):
	questionButtonHeight=23
	maya.cmds.window( windowName, title= windowTitle, s=True, iconName='Short Name', widthHeight=(500, 600))
	
	maya.cmds.frameLayout(windowName + '_frameLayout1', label=' ', borderStyle="in", lv=False, bv=False, mw=10, mh=10)
	maya.cmds.columnLayout(windowName + '_column1', adjustableColumn=True)
	
	maya.cmds.text( label= '   ' )
	
	maya.cmds.rowLayout(windowName + '_row1',numberOfColumns=3, columnWidth3=(80, 80, 80), adjustableColumn3=3, columnAlign3=('left','left','left'), columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)])
	
	maya.cmds.text( label= '' )
	maya.cmds.text( label= '' )
	maya.cmds.text( label= '' )
	maya.cmds.setParent('..')
	
	maya.cmds.text( label= '   ' )
	
	maya.cmds.frameLayout(windowName + '_formBase', label='Tabs', lv=False, labelAlign='top', borderStyle='in')

	
	# Column 1 
	maya.cmds.columnLayout(windowName + '_column1', rowSpacing=1)
	
	# Description for Prefix
	maya.cmds.rowLayout( windowName + '_row1_1a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	maya.cmds.text( windowName + '_descip1_1a', label= line01, height=questionButtonHeight, align=textAlign )
	maya.cmds.text( windowName + '_space1_1a', label='', height=questionButtonHeight)
	maya.cmds.setParent('..')
	# Input field for Prefix
	maya.cmds.rowLayout( windowName + '_row1_2a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	cmdBc01 = uiModule + '.' + 'editTxtGrpButtonSelection("' + windowName + '_sidePrefix' + '",' + '"textFieldButtonGrp")'
	maya.cmds.textFieldButtonGrp( windowName + '_sidePrefix', label='Get Side Prefix:', text='L', buttonLabel='Select', en=True, bc=cmdBc01 )
	maya.cmds.button( windowName + '_help1_2a', label='?', height=questionButtonHeight)
	maya.cmds.setParent('..')
	
	
	# Description for Joint Type
	maya.cmds.rowLayout( windowName + '_row1_3a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	maya.cmds.text( windowName + '_descip1_3a', label= line02, height=questionButtonHeight, align=textAlign )
	maya.cmds.text( windowName + '_space1_3a', label='', height=questionButtonHeight)
	maya.cmds.setParent('..')
	# Input field for Joint Type
	maya.cmds.rowLayout( windowName + '_row1_4a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	cmdBc02 = uiModule + '.' + 'editTxtGrpButtonSelection("' + windowName + '_jointType' + '",' + '"textFieldButtonGrp")'
	maya.cmds.textFieldButtonGrp( windowName + '_jointType', label='Get Joint Type:', text='IK', buttonLabel='Select', en=True, bc=cmdBc02 )
	maya.cmds.button( windowName + '_help1_4a', label='?', height=questionButtonHeight)
	maya.cmds.setParent('..')
	
	
	# Description for Get Start Joint
	maya.cmds.rowLayout( windowName + '_row1_5a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	maya.cmds.text( windowName + '_descip1_5a', label= line03, height=questionButtonHeight, align=textAlign )
	maya.cmds.text( windowName + '_space1_5a', label='', height=questionButtonHeight)
	maya.cmds.setParent('..')
	# Input field for Get Start Joint
	maya.cmds.rowLayout( windowName + '_row1_6a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	cmdBc05 = uiModule + '.' + 'editTxtGrpButtonSelection("' + windowName + '_startJoint' + '","textFieldButtonGrp")'
	maya.cmds.textFieldButtonGrp( windowName + '_startJoint', label='Get Start Joint:', text='', buttonLabel='Select', en=True, bc=cmdBc05 )
	maya.cmds.button( windowName + '_help1_6a', label='?', height=questionButtonHeight)
	maya.cmds.setParent('..')
	
	
	# Description for Get Middle Joint
	maya.cmds.rowLayout( windowName + '_row1_7a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	maya.cmds.text( windowName + '_descip1_7a', label= line04, height=questionButtonHeight, align=textAlign )
	maya.cmds.text( windowName + '_space1_7a', label='', height=questionButtonHeight)
	maya.cmds.setParent('..')
	maya.cmds.text( windowName + '_descip1_7b', label= line05, height=questionButtonHeight, align=textAlign )
	# Input field for Get Middle Joint
	maya.cmds.rowLayout( windowName + '_row1_8a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	cmdBc06 = uiModule + '.' + 'editTxtGrpButtonSelection("' + windowName + '_middleJoint' + '","textFieldButtonGrp")'
	maya.cmds.textFieldButtonGrp( windowName + '_middleJoint', label='Get Middle Joint:', text='', buttonLabel='Select', en=True, bc=cmdBc06 )
	maya.cmds.button( windowName + '_help1_8a', label='?', height=questionButtonHeight)
	maya.cmds.setParent('..')
	
	
	# Description for Get End Joint
	maya.cmds.rowLayout( windowName + '_row1_9a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	maya.cmds.text( windowName + '_descip1_9a', label= line06, height=questionButtonHeight, align=textAlign )
	maya.cmds.text( windowName + '_space1_9a', label='', height=questionButtonHeight)
	maya.cmds.setParent('..')
	# Input field for Get End Joint
	maya.cmds.rowLayout( windowName + '_row1_10a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	cmdBc07 = uiModule + '.' + 'editTxtGrpButtonSelection("' + windowName + '_endJoint' + '","textFieldButtonGrp")'
	maya.cmds.textFieldButtonGrp( windowName + '_endJoint', label='Get End Joint:', text='', buttonLabel='Select', en=True, bc=cmdBc07 )
	maya.cmds.button( windowName + '_help1_10a', label='?', height=questionButtonHeight)
	maya.cmds.setParent('..')
	
	
	# Description for Main Ctrl
	maya.cmds.rowLayout( windowName + '_row1_13a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	maya.cmds.text( windowName + '_descip1_13a', label= line07, height=questionButtonHeight, align=textAlign )
	maya.cmds.text( windowName + '_space1_13a', label='', height=questionButtonHeight)
	maya.cmds.setParent('..')
	# Input field for Main Ctrl
	maya.cmds.rowLayout( windowName + '_row1_14a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	cmdBc07 = uiModule + '.' + 'editTxtGrpButtonSelection("' + windowName + '_mainCtrl' + '","textFieldButtonGrp")'
	maya.cmds.textFieldButtonGrp( windowName + '_mainCtrl', label='Get Main Control:', text='', buttonLabel='Select', bc=cmdBc07, en=True )
	maya.cmds.button( windowName + '_help1_14a', label='?', height=questionButtonHeight)
	maya.cmds.setParent('..')
	
	
	# Description for Pole Vector Ctrl
	maya.cmds.rowLayout( windowName + '_row1_15a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	maya.cmds.text( windowName + '_descip1_15a', label= line07, height=questionButtonHeight, align=textAlign )
	maya.cmds.text( windowName + '_space1_15a', label='', height=questionButtonHeight)
	maya.cmds.setParent('..')
	# Input field for Pole Vector Ctrl
	maya.cmds.rowLayout( windowName + '_row1_16a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	cmdBc08 = uiModule + '.' + 'editTxtGrpButtonSelection("' + windowName + '_polveVectorCtrl' + '","textFieldButtonGrp")'
	maya.cmds.textFieldButtonGrp( windowName + '_polveVectorCtrl', label='Get Pole Vector Control:', text='', buttonLabel='Select', bc=cmdBc08, en=True )
	maya.cmds.button( windowName + '_help1_16a', label='?', height=questionButtonHeight)
	maya.cmds.setParent('..')
	

	maya.cmds.text( windowName + '_space1', label='' )
	maya.cmds.text( windowName + '_space2', label='' )

	
	cmdRun = thisModule + '.runWindow("' + windowName + '")'
	maya.cmds.button(windowName + '_CreateSystem', label='Run Script', c=cmdRun )
	
	
	maya.cmds.showWindow( windowName )



	
# Run the functions	
# injectThisModule : String This parameter is this module injected into the buildWindow function so that the runWindow function can be called correctly
def run(injectThisModule,injectUIModule):
	# Clears the old instance of the window is it exists.
	ui.deleteWindow(rebuildWindowName) 
	
	# 
	buildWindow(injectThisModule,injectUIModule,rebuildWindowName,windowTitle,line_01,line_02,line_03,line_04,line_05,line_06,line_07)
	
	
print("line 162 :: Imported uiRig_createControlCurves Module")