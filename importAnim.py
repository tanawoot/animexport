import maya.cmds as mc
import maya.mel as mel


def selectionAttr():
	selection = mc.ls(selection = True)
	for obj in selection:
		timeInfo = ""
		attr = mc.listAttr(obj,k=True)
		for i in attr:
			timeInfo = setKeyAnimation(obj,i)
				
		print ('setkey : ',obj,timeInfo)

			
def setKeyAnimation(selection,attr):
	#get data
	timeList = [1.0,40.0]
	valueList = [1.3000000,2.67876540]
	inType = [2,2]
	inAngleList = [-1.649656,-9.047491]
	inW = [1.0,1.0]
	outType = [2,1]
	outAngleList = [-2.01625,-16.387891]
	outW = [1.0,1.0]
	timeLen = len(timeList)
	tangentType = ['auto','spline','linear','clamped','step','stepnext','flat','fixed','plateau']
	
	#frame range
	timeSlideBar = mel.eval('$tmpVar=$gPlayBackSlider')
	startTime = mc.timeControl(timeSlideBar,q=True,ra=True)[0]
	endTime =  mc.timeControl(timeSlideBar,q=True,ra=True)[1]
	noRange = (startTime-endTime)+1
	
	if noRange == 0:
		
	    startTime = mc.currentTime(q=True)
	    endTime = timeList[timeLen-1]+startTime-1
	
	else :
		startTime = startTime
		endTime = endTime
	
	
	startFrame = startTime
	endFrame = endTime
	curFrame = ''
	
	#set keyframe
	for i in range(timeLen):
		
		inTangent = tangentType[inType[i]-1]
		outTangent = tangentType[outType[i]-1]
		curFrame = float(timeList[i]+startFrame)-1
		if  curFrame <= endFrame:
			
			mc.setKeyframe( selection, value = float(valueList[i]), attribute = attr, time = curFrame)
			mc.keyTangent(selection,e=True,a=True,t = (curFrame,curFrame),itt = inTangent,inAngle = float(inAngleList[i]),inWeight=1,ott = outTangent,outAngle = float(outAngleList[i]),outWeight=1)
	
	return curFrame
	
selectionAttr()