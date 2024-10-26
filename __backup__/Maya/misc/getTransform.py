def getWStransform(obj):
	transform = maya.cmds.xform( obj, q=True, ws=True, t=True )
	return transform