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
line_01 = 'USE THE FOLLOWING BUTTONS TO CREATE CURVE CONTROLS:'
line_02 = 'THE RIGGING COLOUR STANDARDS ARE AS FOLLOWS:'
line_03 = 'ARRAY KEY ARE 0=Right, 1=Left, 2=Centre, 3=Misc'
line_04 = 'THE MAYA NODE "overrideColor" ATTRIBUTES VALUES ARE:'
line_05 = ' 1. IKcolour = [14,13,17]'
line_06 = ' 2. FKColour = [23,31,25]'
line_07 = ' 3. splineIKColour = [6,15,29]'
line_08 = ' 4. clothColour = [9,30,21]'
line_09 = ' 3. faceColour = [22,10,26]'
line_10 = ' 4. misc = [4,7,11]'
line_11 = 'GIVE A NAME TO THE CURVE CONTROL:'
line_12 = 'PICK A SOLVER TYPE: IK,  FK,  SplineIK,  Cloth,  Face,  OR  Misc:'
line_14 = 'PICK A SIDE PREFIX: RIght,  Middle,  Left, OR  Misc:'


ver = ' : ver 01.005 ' # This needs to be updated each time the script is updated or modified.
comment = 'FIxing indentation error.'
windowTitle = 'Create Control Curves for Rigs' + ver
rebuildWindowName = 'CreateCtrlCrvsRigging'

# Define Rigging Colour Standards
# 0=Right, 1=Left, 2=Centre, 3=Misc
IKcolour = [14,13,17]
FKcolour = [23,31,25]
splineIKcolour = [6,15,29]
clothColour = [9,30,21]
faceColour = [22,10,26]
misc = [4,7,11]

solverTypes = [IKcolour,FKcolour,splineIKcolour,clothColour,faceColour,misc]

axis = "y"
scale = 1

textAlign = 'left'


# Define local functions
def buildWindow(thisModule,uiModule,windowName,windowTitle, line01, line02, line03, line04, line05, line06, line07, line08, line09, line10, line11):
	questionButtonHeight=23
	maya.cmds.window( windowName, title= windowTitle, s=True, iconName='Short Name', widthHeight=(500, 600))
	
	maya.cmds.frameLayout(  windowName + '_frameLayout1', label=' ', borderStyle="in", lv=False, bv=False, mw=10, mh=10)
	maya.cmds.columnLayout(windowName + '_column1', adjustableColumn=True)
	
	maya.cmds.text( label= '   ' )
	
	maya.cmds.rowLayout(windowName + '_row1',numberOfColumns=3, columnWidth3=(80, 80, 80), adjustableColumn3=3, columnAlign3=('left','left','left'), columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)])
	
	maya.cmds.text( label= '' )
	maya.cmds.text( label= '' )
	maya.cmds.text( label= '' )
	maya.cmds.setParent('..')
	
	maya.cmds.text( label= '   ' )
	
	maya.cmds.frameLayout(windowName + '_formBase', label='Tabs', lv=False, labelAlign='top', borderStyle='in')
	#maya.cmds.rowLayout(windowName + '_row2',numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn2=2, columnAlign2=('left','left'), columnAttach=[(1, 'both', 0), (2, 'both', 0)])
	#maya.cmds.rowColumnLayout(windowName + '_row2', numberOfColumns=2,columnWidth=[(1,450),(2,20)])
	
	# Column 1 
	maya.cmds.columnLayout(windowName + '_column1', rowSpacing=1)
	
	maya.cmds.rowLayout( windowName + '_row1_1a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	maya.cmds.text( windowName + '_descip1_1a', label= line02, height=questionButtonHeight, align=textAlign )
	maya.cmds.text( windowName + '_space1_1a', label='', height=questionButtonHeight)
	maya.cmds.setParent('..')
	
	
	maya.cmds.rowLayout( windowName + '_row1_2a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	maya.cmds.text( windowName + '_descip1_2a', label= line03, height=questionButtonHeight, align=textAlign )
	maya.cmds.button( windowName + '_help1_2a', label='?', height=questionButtonHeight)
	maya.cmds.setParent('..')
	
	
	maya.cmds.rowLayout( windowName + '_row1_3a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	maya.cmds.text( windowName + '_space1_3a', label='' )
	maya.cmds.text( windowName + '_space1_3b', label='' )
	maya.cmds.setParent('..')
	
	
	maya.cmds.rowLayout( windowName + '_row1_4a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	maya.cmds.text( windowName + '_descip1_4a', label= line04, height=questionButtonHeight, align=textAlign )
	maya.cmds.button( windowName + '_help1_4a', label='?', height=questionButtonHeight)
	maya.cmds.setParent('..')
	
	
	maya.cmds.rowLayout( windowName + '_row1_5a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	maya.cmds.text( windowName + '_descip1_5a', label= line05, height=questionButtonHeight, align=textAlign )
	maya.cmds.button( windowName + '_help1_5a', label='?', height=questionButtonHeight)
	maya.cmds.setParent('..')
	
	
	maya.cmds.rowLayout( windowName + '_row1_6a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	maya.cmds.text( windowName + '_descip1_6a', label= line06, height=questionButtonHeight, align=textAlign )
	maya.cmds.button( windowName + '_help1_6a', label='?', height=questionButtonHeight)
	maya.cmds.setParent('..')
	
	
	maya.cmds.rowLayout( windowName + '_row1_7a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	maya.cmds.text( windowName + '_descip1_7a', label= line07, height=questionButtonHeight, align=textAlign )
	maya.cmds.button( windowName + '_help1_7a', label='?', height=questionButtonHeight)
	maya.cmds.setParent('..')
	
	
	maya.cmds.rowLayout( windowName + '_row1_8a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	maya.cmds.text( windowName + '_descip1_8a', label= line08, height=questionButtonHeight, align=textAlign )
	maya.cmds.button( windowName + '_help1_8a', label='?', height=questionButtonHeight)
	maya.cmds.setParent('..')
	
	
	maya.cmds.rowLayout( windowName + '_row1_9a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	maya.cmds.text( windowName + '_descip1_9a', label= line09, height=questionButtonHeight, align=textAlign )
	maya.cmds.button( windowName + '_help1_9a', label='?', height=questionButtonHeight)
	maya.cmds.setParent('..')
	
	
	maya.cmds.rowLayout( windowName + '_row1_10a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	maya.cmds.text( windowName + '_descip1_10a', label= line10, height=questionButtonHeight, align=textAlign )
	maya.cmds.button( windowName + '_help1_10a', label='?', height=questionButtonHeight)
	maya.cmds.setParent('..')
	
	
	maya.cmds.rowLayout( windowName + '_row1_11a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	maya.cmds.text( windowName + '_space1_11a', label='' )
	maya.cmds.text( windowName + '_space1_11b', label='' )
	maya.cmds.setParent('..')
	
	
	maya.cmds.rowLayout( windowName + '_row1_12a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	maya.cmds.text( windowName + '_descip1_12a', label= line11, height=questionButtonHeight, align=textAlign )
	maya.cmds.text( windowName + '_space1_12a', label='' )
	maya.cmds.setParent('..')
	
	
	maya.cmds.rowLayout( windowName + '_row1_14a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left'))
	name = maya.cmds.textField( windowName + '_name1_14a', height=questionButtonHeight )
	maya.cmds.text( windowName + '_space1_14a', label='' )
	maya.cmds.setParent('..')
	
	
	maya.cmds.columnLayout( windowName + '_column2', rowSpacing=1 )
	maya.cmds.text( windowName + '_descip1_15a', label=line_12, height=questionButtonHeight, align=textAlign )
	maya.cmds.rowLayout( windowName + '_row1_15a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left') )
	#solverType = maya.cmds.textField( windowName + '_solverType1_15a', height=questionButtonHeight, placeholderText='IK', width=450 )
	#maya.cmds.button( windowName + '__help1_15a', label='?', height=questionButtonHeight)
	maya.cmds.rowColumnLayout( windowName + '_rowColumn1_15a', numberOfColumns=6 )
	collection_solverTypes = maya.cmds.radioCollection( windowName + '_collection_solverTypes1_15a' )
	st1 = maya.cmds.radioButton( label='IK' )
	st2 = maya.cmds.radioButton( label='FK' )
	st3 = maya.cmds.radioButton( label='SplineIK' )
	st4 = maya.cmds.radioButton( label='Cloth' )
	st5 = maya.cmds.radioButton( label='Face' )
	st6 = maya.cmds.radioButton( label='Misc' )
	maya.cmds.radioCollection( collection_solverTypes, edit=True, select=st1 )
	maya.cmds.setParent('..')
	maya.cmds.button( windowName + '__help1_15a', label='?', height=questionButtonHeight)
	maya.cmds.setParent('..')
	
	
	maya.cmds.columnLayout( windowName + '_column3', rowSpacing=1 )
	maya.cmds.text( windowName + '_descip1_16a', label=line_14, height=questionButtonHeight, align=textAlign )
	maya.cmds.rowLayout( windowName + '_row1_16a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left') )
	maya.cmds.rowColumnLayout( windowName + '_rowColumn1_16a', numberOfColumns=4 )
	collection_sidePrefix = maya.cmds.radioCollection( windowName + '_collection_sidePrefix1_16a' )
	sp1 = maya.cmds.radioButton( label='Right' )
	sp2 = maya.cmds.radioButton( label='Middle' )
	sp3 = maya.cmds.radioButton( label='Left' )
	sp4 = maya.cmds.radioButton( label='Misc', enable=False )
	maya.cmds.radioCollection( collection_sidePrefix, edit=True, select=sp3 )
	maya.cmds.setParent('..')
	maya.cmds.button( windowName + '__help1_16a', label='?', height=questionButtonHeight)
	maya.cmds.setParent('..')
	
	
	maya.cmds.rowLayout( windowName + '_row1_17a', numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn=1, columnAlign=(1, 'left') )
	maya.cmds.text( windowName + '_descip1_17a', label= line01, height=questionButtonHeight, align=textAlign )
	maya.cmds.text( windowName + '_space1_17a', label='', height=questionButtonHeight)
	maya.cmds.setParent('..')
	
	# Column 3
	#maya.cmds.columnLayout(windowName + '_column2', rowSpacing=1)
	#maya.cmds.rowLayout(windowName + '_column2')
	maya.cmds.rowColumnLayout(windowName + '_column2', numberOfRows=1)
	arg_createSquareArrowCtrl = [windowName,axis,scale]
	cmdRun_createSquareArrowCtrl = thisModule + '.runCreateSquareArrowCtrl("' + windowName + '",' + '"y"' + ',' + str(scale) + ')'
	#cmdRun_createSquareArrowCtrl = thisModule + '.runCreateSquareArrowCtrl(arg_createSquareArrowCtrl)'
	maya.cmds.button( windowName + '_CreateSquareArrowCtrl', label='Run Create Square Arrow Ctrl', command=cmdRun_createSquareArrowCtrl )
	#cmdRun_createDiamondStandCtrl = thisModule + '.runCreateSquareArrowCtrl("' + name + '")'
	#maya.cmds.button( windowName + '_CreateDiamondStandCtrl', label='Run create Diamond Stand Ctrl', command=cmdRun_createSquareArrowCtrl )
	
	#maya.cmds.textField( name, edit=True, enterCommand=( 'printName(\"' + name + '\")' ) )
	
	
	maya.cmds.showWindow( windowName )


# Run the functions
#def runCreateSquareArrowCtrl(windowName,colour,axis,scle):
def runCreateSquareArrowCtrl(windowName,axis,scle):
	tempName = '_temp_name_'
	#windowName = args[0]
	#axis = args[1]
	#scle = args[2]
	
	getName = maya.cmds.textField( windowName + '_name1_14a', q=True, text=True )
	if not getName:
		getName = tempName
		
	print getName
	
	getSolverType = maya.cmds.textField( windowName + '_solverType1_15a', q=True, text=True )
	#getSolverType = maya.cmds.textField( windowName + '_collection_solverTypes1_15a', query=True, select=True )
	colour = runGetSolverType(getSolverType,solverTypes)
	print colour
	
	#uCrv.createDiamondStandCtrl(getName,colour,axis,scle)

def runGetSolverType(type,solverTypes):
		result = solverTypes[0] #solverTypes[5]
		if( type.lower() == 'ik'):
			result = solverTypes[0]
		elif( type.lower() == 'fk'):
			result = solverTypes[1]
		elif( type.lower() == 'splineik'):
			result = solverTypes[2]
		elif( type.lower() == 'face'):
			result = solverTypes[3]
		elif( type.lower() == 'cloth'):
			result = solverTypes[4]
		else:
			result = solverTypes[5]
			
		return result
		
def runGetSidePrefix(type,solverTypes):
		
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
	buildWindow(injectThisModule,injectUIModule,rebuildWindowName,windowTitle,line_01,line_02,line_03,line_04,line_05,line_06,line_07,line_08,line_09,line_10,line_11)
	
	
print("line 162 :: Imported uiRig_createControlCurves Module")