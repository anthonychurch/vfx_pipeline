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
#	TODO:	
#	1. TODO
#	
#	
###############################################################################################

# Define local UI Variables
line00 = '	SPECIFIY THE CONTROL AIM AXIS:-'
line01 = '	SELECT MASTER CONTROL :-'  #TYPE PREFIX :-'
line02 = '	SELECT OBJECT TO CONNECT TO :-'


ver = ' : ver 01.001 ' # This needs to be updated each time the script is updated or modified.
windowTitle = 'Connects Master Scale Attribute to Translate'
rebuildWindowName = 'connectMasterScleToTrans'


# Define Global Variables
gSrcAttr = 'scale'
gDestAttr = 'translate'


# Define Local Functions
def getSetSelectSource(wndwName,fieldType):
	# Get the selected objects.
	arr = []
	sel = maya.cmds.ls(selection=True)
	if sel:
		arr.append(sel[0])
	print arr
	
	fieldAxis = wndwName + '_ctrlAimAxis'
	fieldName = wndwName + '_masterCtrl'
	
	errorTxt = ''
	
	# Get the axis to check the if the objects have the correct attribute
	caa = maya.cmds.radioButtonGrp( fieldAxis, q=True, sl=True )
	ctrlAimAxis = utl.whichAxis(caa)
	
	# To check to make sure the attribute exists
	checkAttr = gSrcAttr + ctrlAimAxis[1] # example 'sx' or 'tz'
	hasCorrectAttribute = True
	
	# Test to make sure the correct type of objects are selected.
	if not arr:
		errorTxt = 'ERROR : Nothing is selected. Select objects to connect to.'
		print(errorTxt)
		ui.editTxtGrpButton(errorTxt,fieldName,fieldType)
	else:
		for a in arr:
			attrExist = maya.cmds.attributeQuery(checkAttr, node=a, exists=True) # example maya.cmds.attributeQuery('tx', node='pCube1', exists=True)
			print attrExist
			# Test if selection has the correct attribute to be connected to has the correct attribute
			if hasCorrectAttribute:
				if not attrExist:
					errorTxt = 'ERROR : Selected object '+ str(a) + ' does not have the following attribute ' + str(checkAttr) + '. All selected objects must has attribute ' + str(checkAttr)
					print( errorTxt )
					hasCorrectAttribute = False
			
		if hasCorrectAttribute:
			ui.editTxtGrpButtonArray(arr,fieldName,fieldType)
		else:
			ui.editTxtGrpButton(errorTxt,fieldName,fieldType)
			

def getSetSelectDestination(wndwName,fieldType):
	# Get the selected objects.
	arr = maya.cmds.ls(selection=True)
	
	fieldAxis = wndwName + '_ctrlAimAxis'
	fieldName = wndwName + '_destCtrl'
	
	errorTxt = ''
	
	# Get the axis to check the if the objects have the correct attribute
	caa = maya.cmds.radioButtonGrp( fieldAxis, q=True, sl=True )
	ctrlAimAxis = utl.whichAxis(caa)
	
	# To check to make sure the attribute exists
	checkAttr = gDestAttr + ctrlAimAxis[1] # example 'tx' or 'ry'
	hasCorrectAttribute = True
	
	# Test to make sure the correct type of objects are selected.
	if not arr:
		errorTxt = 'ERROR : Nothing is selected. Select objects to connect to.'
		print(errorTxt)
		ui.editTxtGrpButton(errorTxt,fieldName,fieldType)
	else:
		for a in arr:
			attrExist = maya.cmds.attributeQuery(checkAttr, node=a, exists=True) # example maya.cmds.attributeQuery('tx', node='pCube1', exists=True)
			# Test if selection has the correct attribute to be connected to has the correct attribute
			if hasCorrectAttribute:
				if not attrExist:
					errorTxt = 'ERROR : Selected object '+ str(a) + ' does not have the following attribute ' + str(checkAttr) + '. All selected objects must has attribute ' + str(checkAttr)
					print( errorTxt )
					hasCorrectAttribute = False
			
		if hasCorrectAttribute:
			ui.editTxtGrpButtonArray(arr,fieldName,fieldType)
		else:
			ui.editTxtGrpButton(errorTxt,fieldName,fieldType)
			

def buildWindow(inj, windowName, windowTitle, line00, line01, line02):
	
	#arr = ['1','2','3'] # Temp for testing, needs to be removed
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
	maya.cmds.text( label= line00 )	
	maya.cmds.radioButtonGrp( windowName + '_ctrlAimAxis', label='Control Aim Axis:', labelArray3=['x', 'y', 'z'], numberOfRadioButtons=3, en=True, sl=1 )
	maya.cmds.text( label= line01 )
	#cmd1 = inj + '.getSetSelectSource("' + windowName + '_masterCtrl' + '","textFieldButtonGrp")'
	cmd1 = inj + '.getSetSelectSource("' + windowName + '","textFieldButtonGrp")'
	maya.cmds.textFieldButtonGrp( windowName + '_masterCtrl', label='Get Master Control:', text='', buttonLabel='Select', cc='togglesystems("' + windowName + '")', bc=cmd1, en=True )
	maya.cmds.text( label= line02 )
	#maya.cmds.textFieldButtonGrp( windowName + '_destCtrl', label='Destination Controls:', text='', buttonLabel='Select', cc='togglesystems("' + windowName + '")', bc='ui.editTxtGrpButtonArray("' + windowName + '_destCtrl' + '","textFieldButtonGrp")', en=True )
	#cmd2 = inj + '.getSetSelectDestination("' + windowName + '_destCtrl' + '","textFieldButtonGrp")'
	cmd2 = inj + '.getSetSelectDestination("' + windowName + '","textFieldButtonGrp")'
	maya.cmds.textFieldButtonGrp( windowName + '_destCtrl', label='Destination Controls:', text='', buttonLabel='Select', cc='togglesystems("' + windowName + '")', bc=cmd2, en=True )
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
	
	cmd3 = inj + '.runWindow("' + windowName + '")'
	maya.cmds.button(windowName + '_CreateSystem', label='Run Script', c=cmd3 )

	maya.cmds.showWindow( windowName )


def runWindow(windowName):
	caa = maya.cmds.radioButtonGrp( windowName + '_ctrlAimAxis', q=True, sl=True )
	ctrlAimAxis = utl.whichAxis(caa)
	#getMasterCtrl = maya.cmds.textFieldButtonGrp( windowName + '_masterCtrl', q=True, text=True )
	#mCtrl = getMasterCtrl.split()[0]
	#print( "mCtrl = " + str(mCtrl) )
	print( "ctrlAimAxis = " + str(ctrlAimAxis) )
	"""
	getCtrl = maya.cmds.textFieldButtonGrp( windowName + '_ctrl', q=True, text=True )
	ctrlArray = getCtrl.split()
	cntrl = ctrlArray[0]

	getCurveInfo = maya.cmds.textFieldButtonGrp( windowName + '_curveInfo', q=True, text=True )
	ci = getCurveInfo.split()
	curveInfoNode = ci[0]

	getMultNode = maya.cmds.textFieldButtonGrp( windowName + '_multNode', q=True, text=True )
	mn = getMultNode.split()
	multiplyNode = mn[0]

	getPrefix = maya.cmds.textFieldGrp( windowName + '_prefix', q=True, text=True )
	p = getPrefix.split()
	prefix = p[0]

	getAttr = maya.cmds.textFieldGrp( windowName + '_attr', q=True, text=True )
	a = getAttr.split()
	stretchIKAttr = a[0]
	"""
	#uRig.connectSplineIkStretchAttr(prefix, cntrl,stretchIKAttr,multiplyNode,curveInfoNode)
	#print "Run Window"




# Run the functions	
def run(inject):
	# Clears the old instance of the window is it exists.
	ui.deleteWindow(rebuildWindowName) 

	# 
	buildWindow(inject,rebuildWindowName,windowTitle,line00,line01,line02)

print("line 0127 :: Imported uiRig_connectMasterScaleToTranlate Module")