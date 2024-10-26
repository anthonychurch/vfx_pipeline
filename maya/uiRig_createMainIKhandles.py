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



ver = ' : ver 01.003 ' # This needs to be updated each time the script is updated or modified.
comment = 'Adding radio buttons.'
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
	

	# Description for Joint Type
	maya.cmds.columnLayout( windowName + '_column2', rowSpacing=1 )
	maya.cmds.text( windowName + '_descip1_1a', label= line02, height=questionButtonHeight, align=textAlign )
	maya.cmds.rowLayout( windowName + '_row1_1a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left') )
	# Radio buttons for selecting the Joint Type
	maya.cmds.rowColumnLayout( windowName + '_rowColumn1_2a', numberOfColumns=6 )
	name_solverTypes = windowName + '_collection_solverTypes'
	collection_solverTypes = maya.cmds.radioCollection( name_solverTypes )
	st1 = maya.cmds.radioButton( 'ik', label='IK' )
	st2 = maya.cmds.radioButton( 'fk', label='FK' )
	st3 = maya.cmds.radioButton( 'spl', label='SplineIK' )
	st4 = maya.cmds.radioButton( 'clth', label='Cloth' )
	st5 = maya.cmds.radioButton( 'fce', label='Face' )
	st6 = maya.cmds.radioButton( 'msc', label='Misc' )
	maya.cmds.radioCollection( collection_solverTypes, edit=True, select=st1 )
	maya.cmds.setParent('..')
	maya.cmds.button( windowName + '__help1_2a', label='?', height=questionButtonHeight)
	maya.cmds.setParent('..')
	
	
	# Description for Prefix
	maya.cmds.columnLayout( windowName + '_column3', rowSpacing=1 )
	maya.cmds.text( windowName + '_descip1_3a', label=line_01, height=questionButtonHeight, align=textAlign )
	maya.cmds.rowLayout( windowName + '_row1_3a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left') )
	maya.cmds.rowColumnLayout( windowName + '_rowColumn1_3a', numberOfColumns=4 )
	# Radio buttons for selecting the Prefix
	name_sidePrefix = windowName + '_collection_sidePrefix'
	collection_sidePrefix = maya.cmds.radioCollection( name_sidePrefix )
	sp1 = maya.cmds.radioButton( '_left', label='Left' )
	sp2 = maya.cmds.radioButton( '_right', label='Right' )
	sp3 = maya.cmds.radioButton( '_centre', label='Centre' )
	sp4 = maya.cmds.radioButton( '_misc', label='Misc', enable=False )
	maya.cmds.radioCollection( collection_sidePrefix, edit=True, select=sp3 )
	maya.cmds.setParent('..')
	maya.cmds.button( windowName + '__help1_3a', label='?', height=questionButtonHeight)
	maya.cmds.setParent('..')
	

	# Description for Get Start Joint
	maya.cmds.rowLayout( windowName + '_row1_5a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	maya.cmds.text( windowName + '_descip1_5a', label= line03, height=questionButtonHeight, align=textAlign )
	maya.cmds.text( windowName + '_space1_5a', label='', height=questionButtonHeight)
	maya.cmds.setParent('..')
	# Input field for Get Start Joint
	maya.cmds.rowLayout( windowName + '_row1_6a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	name_startJoint = windowName + '_startJoint'
	cmdBc05 = uiModule + '.' + 'editTxtGrpButtonSelection("' + name_startJoint + '","textFieldButtonGrp")'
	maya.cmds.textFieldButtonGrp( name_startJoint, label='Get Start Joint:', text='', buttonLabel='Select', en=True, bc=cmdBc05 )
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
	name_middleJoint = windowName + '_middleJoint'
	cmdBc06 = uiModule + '.' + 'editTxtGrpButtonSelection("' + name_middleJoint + '","textFieldButtonGrp")'
	maya.cmds.textFieldButtonGrp( name_middleJoint, label='Get Middle Joint:', text='', buttonLabel='Select', en=True, bc=cmdBc06 )
	maya.cmds.button( windowName + '_help1_8a', label='?', height=questionButtonHeight)
	maya.cmds.setParent('..')
	
	
	# Description for Get End Joint
	maya.cmds.rowLayout( windowName + '_row1_9a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	maya.cmds.text( windowName + '_descip1_9a', label= line06, height=questionButtonHeight, align=textAlign )
	maya.cmds.text( windowName + '_space1_9a', label='', height=questionButtonHeight)
	maya.cmds.setParent('..')
	# Input field for Get End Joint
	maya.cmds.rowLayout( windowName + '_row1_10a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	name_endJoint = windowName + '_endJoint'
	cmdBc07 = uiModule + '.' + 'editTxtGrpButtonSelection("' + name_endJoint + '","textFieldButtonGrp")'
	maya.cmds.textFieldButtonGrp( name_endJoint, label='Get End Joint:', text='', buttonLabel='Select', en=True, bc=cmdBc07 )
	maya.cmds.button( windowName + '_help1_10a', label='?', height=questionButtonHeight)
	maya.cmds.setParent('..')
	
	
	# Description for Main Ctrl
	maya.cmds.rowLayout( windowName + '_row1_13a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	maya.cmds.text( windowName + '_descip1_13a', label= line07, height=questionButtonHeight, align=textAlign )
	maya.cmds.text( windowName + '_space1_13a', label='', height=questionButtonHeight)
	maya.cmds.setParent('..')
	# Input field for Main Ctrl
	maya.cmds.rowLayout( windowName + '_row1_14a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	name_mainCtrl = windowName + '_mainCtrl'
	cmdBc07 = uiModule + '.' + 'editTxtGrpButtonSelection("' + name_mainCtrl + '","textFieldButtonGrp")'
	maya.cmds.textFieldButtonGrp( name_mainCtrl, label='Get Main Control:', text='', buttonLabel='Select', bc=cmdBc07, en=True )
	maya.cmds.button( windowName + '_help1_14a', label='?', height=questionButtonHeight)
	maya.cmds.setParent('..')
	
	
	# Description for Pole Vector Ctrl
	maya.cmds.rowLayout( windowName + '_row1_15a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	maya.cmds.text( windowName + '_descip1_15a', label= line07, height=questionButtonHeight, align=textAlign )
	maya.cmds.text( windowName + '_space1_15a', label='', height=questionButtonHeight)
	maya.cmds.setParent('..')
	# Input field for Pole Vector Ctrl
	maya.cmds.rowLayout( windowName + '_row1_16a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	name_poleVectorCtrl = windowName + '_polveVectorCtrl'
	cmdBc08 = uiModule + '.' + 'editTxtGrpButtonSelection("' + name_poleVectorCtrl + '","textFieldButtonGrp")'
	maya.cmds.textFieldButtonGrp( name_poleVectorCtrl, label='Get Pole Vector Control:', text='', buttonLabel='Select', bc=cmdBc08, en=True )
	maya.cmds.button( windowName + '_help1_16a', label='?', height=questionButtonHeight)
	maya.cmds.setParent('..')
	

	maya.cmds.text( windowName + '_space17a', label='' )
	maya.cmds.text( windowName + '_space17b', label='' )

	
	args = [name_solverTypes, name_sidePrefix, name_startJoint, name_middleJoint, name_endJoint, name_mainCtrl, name_poleVectorCtrl]
	cmdRun = thisModule + '.runWindow(' + str( args ) + ')'
	maya.cmds.button(windowName + '_runWindow', label='Run Script', command=cmdRun )


	maya.cmds.showWindow( windowName )


# Run the functions
def runWindow(arg_array):
	solverType = maya.cmds.radioCollection( arg_array[0], query=True, select=True )
	solverType = solverType.upper() + "_"
	sidePrefix = maya.cmds.radioCollection( arg_array[1], query=True, select=True )
	sidePrefix = sidePrefix[1].upper() + "_"
	
	startJoint = maya.cmds.textFieldButtonGrp( arg_array[2], query=True,  text=True )
	startJoint = startJoint.split()[0]
	
	middleJoint = maya.cmds.textFieldButtonGrp( arg_array[3], query=True,  text=True )
	middleJoint = middleJoint.split()[0]
	
	endJoint = maya.cmds.textFieldButtonGrp( arg_array[4], query=True,  text=True )
	endJoint = endJoint.split()[0]
	
	mainCtrl = maya.cmds.textFieldButtonGrp( arg_array[5], query=True,  text=True )
	mainCtrl = mainCtrl.split()[0]
	
	poleVectorCtrl = maya.cmds.textFieldButtonGrp( arg_array[6], query=True,  text=True )
	poleVectorCtrl = poleVectorCtrl.split()[0]
	print mainCtrl
	print poleVectorCtrl
	
	# Select Joint Chain 
	selJointChain = maya.cmds.select( startJoint, hierarchy=True )
	getJointChain = maya.cmds.ls( selection=True )
	maya.cmds.select( clear=True )
	
	ikJoints = []
	for g in getJointChain:
		if(g != endJoint):
			ikJoints.append(g)
		else:
			ikJoints.append(g)
			break
	# Check if only the IK chain joints are selected
	for i in ikJoints:
		#print i
		maya.cmds.select( i, add=True )
		
	uRig.setupPolVector(poleVectorCtrl,middleJoint,pvDistance,'z')
	ikHandleType = 'ikSCsolver'
	if maya.cmds.objExists(pvCtrl):
		ikHandleType = 'ikRPsolver'
		
	mainIkhandle = uRig.createIKhandles(sidePrefix,solverType,ikHandleType,ikJoints[0],endJoint,poleVectorCtrl,None,None)

	maya.cmds.parent(mainIkhandle[0],mainCtrl,a=True)

	#Add Control over the stiffness of the IK joints
	print('masterCreateIK :: howManyTweenJoints = ' + str(howManyTweenJoints))
	ikTweenJoints = uRig.getTweenJointsAuto(ikJoints,'joint')
	print('masterCreateIK :: ikTweenJoints = ' + str(ikTweenJoints))
	uRig.addStiffness2(sidePrefix + jointType + limbTypeName,ikTweenJoints,mainCtrl)
	

# Run the functions	
# injectThisModule : String This parameter is this module injected into the buildWindow function so that the runWindow function can be called correctly
def run(injectThisModule,injectUIModule):
	# Clears the old instance of the window is it exists.
	ui.deleteWindow(rebuildWindowName) 
	
	# 
	buildWindow(injectThisModule,injectUIModule,rebuildWindowName,windowTitle,line_01,line_02,line_03,line_04,line_05,line_06,line_07)
	
	
print("line 162 :: Imported uiRig_createControlCurves Module")