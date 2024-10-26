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



###############################################################################################
#   INSTRUCTIONS FOR USE.
#	SELECT:	
#	1. SELECT THE ALL ADDITIONAL CLAW JOINTS FROM THE START TO END
#	2. SELECT roll_LOC
#	3. MAIN CONTROL
###############################################################################################


# Define local UI Variables
line1 = '	TYPE IN THE SIDE PREFIX ie: L or R:-'
line2 = '	TYPE IN THE NAME OF THE JOINT ie: IK or SPL:-'
line3 = '	SPECIFIY THE CONTROL AIM AXIS:-'
line4 = '	SPECIFIY THE JOINT AIM AXIS:-'
line5 = '	SELECT THE ALL ADDITIONAL CLAW JOINTS FROM THE START TO END:-'
line6 = '	SELECT roll LOCATOR:-'
line7 = '	SELECT MAIN CONTROL:-'

ver = ' : ver 03.001 ' # This needs to be updated each time the script is updated or modified.
windowTitle = 'Append Biped Foot Rig Add Claw' + ver
rebuildWindowName = 'AppendFootRigAddClaw'


# Define local functions
def buildWindow(windowName,windowTitle):
	questionButtonHeight=23
	maya.cmds.window( windowName, title= windowTitle, s=True, iconName='Short Name', widthHeight=(500, 600))
	maya.cmds.frameLayout(  windowName + '_frameLayout1', label=' ', borderStyle="in", lv=False, bv=False, mw=10, mh=10)
	maya.cmds.columnLayout(windowName + '_column1', adjustableColumn=True)

	maya.cmds.text( label= '   ' )

	maya.cmds.rowLayout(windowName + '_row1',numberOfColumns=3, columnWidth3=(80, 80, 80), adjustableColumn3=3, columnAlign3=('left','left','left'), columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)])
	
	maya.cmds.text( label= '   ' )
	maya.cmds.text( label= '   ' )
	maya.cmds.text( label= '   ' )
	maya.cmds.setParent('..')

	maya.cmds.text( label= '   ' )

	maya.cmds.frameLayout(windowName + '_formBase', label='Tabs', lv=False, labelAlign='top', borderStyle='in')
	maya.cmds.rowLayout(windowName + '_row2',numberOfColumns=2, columnWidth2=(450, 20), adjustableColumn2=2, columnAlign2=('left','left'), columnAttach=[(1, 'both', 0), (2, 'both', 0)])
	
	maya.cmds.columnLayout(windowName + '_global1a', rs=3)
	maya.cmds.text( label= line1 )
	maya.cmds.textFieldButtonGrp( windowName + '_sidePrefix', label='Get Side Prefix:', text='L', buttonLabel='Select', en=True, bc='editTxtGrpButtonArray("' + windowName + '_sidePrefix' + '","textFieldButtonGrp")' )
	maya.cmds.text( label= line2 )
	maya.cmds.textFieldButtonGrp( windowName + '_jointType', label='Get Joint Type:', text='IK', buttonLabel='Select', en=True, bc='editTxtGrpButtonArray("' + windowName + '_jointType' + '","textFieldButtonGrp")' )
	maya.cmds.text( label= line3 )	
	maya.cmds.radioButtonGrp( windowName + '_jointUpAxis', label='Joint Up Axis:', labelArray3=['x', 'y', 'z'], numberOfRadioButtons=3, en=True, sl=1 )
	maya.cmds.text( label= line4 )	
	maya.cmds.radioButtonGrp( windowName + '_jointAimAxis', label='Joint Aim Axis:', labelArray3=['x', 'y', 'z'], numberOfRadioButtons=3, en=True, sl=1 )
	maya.cmds.text( label= line5 )
	maya.cmds.textFieldButtonGrp( windowName + '_joints', label='Get Joints:', text='', buttonLabel='Select', en=True, bc='editTxtGrpButtonArray("' + windowName + '_joints' + '","textFieldButtonGrp")' )
	maya.cmds.text( label= line6 )
	maya.cmds.textFieldButtonGrp( windowName + '_rollLoc', label='Get Roll Locator:', text='', buttonLabel='Select', en=True, bc='editTxtGrpButtonArray("' + windowName + '_rollLoc' + '","textFieldButtonGrp")' )
	maya.cmds.text( label= line7 )
	maya.cmds.textFieldButtonGrp( windowName + '_mainCtrl', label='Get Main Control:', text='', buttonLabel='Select', cc='togglesystems("' + windowName + '")', bc='editTxtGrpButtonArray("' + windowName + '_mainCtrl' + '","textFieldButtonGrp")', en=True )
	maya.cmds.setParent('..')

	maya.cmds.columnLayout(windowName + '_global1b', rs=3)
	maya.cmds.text( label= '   ' )
	maya.cmds.button(label='?', height = questionButtonHeight)
	maya.cmds.text( label= '   ' )
	maya.cmds.button(label='?', height = questionButtonHeight)
	maya.cmds.text( label= '   ' )
	maya.cmds.setParent('..')
	
	maya.cmds.setParent('..')

	maya.cmds.text( windowName + '_space1', label='' )
	maya.cmds.text( windowName + '_space2', label='' )
	maya.cmds.button(windowName + '_CreateSystem', label='Run Script', c='runWindow("' + windowName + '")' )

	maya.cmds.showWindow( windowName )


def runWindow(windowName):

	getSidePrefix = maya.cmds.textFieldButtonGrp( windowName + '_sidePrefix', q=True, text=True )
	sp = getSidePrefix.split()
	sidePrefix = ''
	if(len(sp) > 0):
		sidePrefix = sp[0] + '_'
	#print ('sidePrefix = ' + str(sidePrefix))
	#print('runWindow() :: sidePrefix = ' + str(sidePrefix))
	getJointType = maya.cmds.textFieldButtonGrp( windowName + '_jointType', q=True, text=True )
	jt = getJointType.split()
	jointType = ''
	if(len(jt) > 0):
		jointType = jt[0] + '_'
	#print ('jointType = ' + str(jointType))
	prefix = sidePrefix + jointType

	getRollLoc = maya.cmds.textFieldButtonGrp( windowName + '_rollLoc', q=True, text=True )
	rl = getRollLoc.split()
	rollLoc = ''
	if(len(rl) > 0):
		rollLoc = rl[0]
	#print ('rollLoc = ' + str(rollLoc))


	jua = maya.cmds.radioButtonGrp( windowName + '_jointUpAxis', q=True, sl=True )
	jointUpAxis = whichAxis(jua)
	jaa = maya.cmds.radioButtonGrp( windowName + '_jointAimAxis', q=True, sl=True )
	jointAimAxis = whichAxis(jaa)
	getJoints = maya.cmds.textFieldButtonGrp( windowName + '_joints', q=True, text=True )
	jointsArray = getJoints.split()
	getCtrl = maya.cmds.textFieldButtonGrp( windowName + '_mainCtrl', q=True, text=True )
	ctrl = getCtrl.split()
	mainCtrl = ''
	if(len(ctrl) > 0):
		mainCtrl = ctrl[0]
	#print ('mainCtrl = ' + str(mainCtrl))
	
	ikFootJoints = []
	for j in range(0,len(jointsArray)-2,1):
		ikFootJoints.append(jointsArray[j])

	#print('rollLoc = ' + str(rollLoc))
	#print('mainCtrl = ' + str(mainCtrl))

	uRig.addClaw(prefix,jointsArray,rollLoc,jointAimAxis[0],jointUpAxis[0],mainCtrl)


# Run the functions	
def run():
	# Clears the old instance of the window is it exists.
	ui.deleteWindow(rebuildWindowName) 

	# 
	buildWindow(rebuildWindowName,windowTitle)

print("line 0152 :: Imported uiRig_AppendBipedFootRigAddClaws Module")