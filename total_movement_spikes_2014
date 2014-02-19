import os
from matplotlib import pyplot
import math

#Indexes for data
LH = 0
RH = 1
HEAD_PPT_POS = 2
HEAD_PPT_EULER = 3
LH_PPT_EULER = 4
RH_PPT_EULER = 5
DATE = 6
TIME = 7

YAW = 1
PITCH = 2
ROLL = 3

LIMB_NAMES = ['LeftHand', 'RightHand', 'HeadPosition', 'HeadEuler', 'LeftHandEuler', 'RightHandEuler']

NUM_MIN = 9

def dist(p1, p2, orientation):
    if orientation == 0:
        return math.sqrt(math.pow(p2[0] - p1[0], 2) + math.pow(p2[1] - p1[1], 2) + math.pow(p2[2] - p1[2],2))#squarerrot((x1-x2)^2+(y1-y2)^2+(z1-z2)^2)
    else:
        distanceCalculated = abs(p2[orientation - 1] - p1[orientation - 1])
        if distanceCalculated > 180:
            return 360 - distanceCalculated
        else:
            return distanceCalculated
#uses a different distance function to calculate changes in position for the intersense

#limb describes part of body (lefthand, righthand, leftintersense, rightintersense)
#orientiaton describest the following:
ORIENTATIONS = ['', 'YAW' ,'PITCH', 'ROLL']#0 means orientation not applicable
#outputs a graph to the file with the given limb and orientation movement graph
def makeLine(limb, orientation):
        lines = []
        pyplot.clf()
        currMin = 0
        for i in range(len(strLines)-2):#this will make sure we don't read the last two lines which are information about the fire
                lines.append(eval(strLines[i]))
        prevTime = lines[0][TIME]
        for i in range(len(strLines)-4):#does -4 so it doesnt go out of bounds and hit information about the fire
            if (currMin < 10):
                y = [0, dist(lines[i][limb], lines[(i + 1)][limb], orientation)]
                x = [i, i]
                pyplot.plot(x,y)
                if orientation == 0:
                    v = [0, 15000, 0, .5]
                else:
                    v = [0, 15000, 0, 20]
                pyplot.axis(v)
                if lines[i][TIME] > (prevTime + 60):
                    currMin += 1
                    prevTime = prevTime + 60
        pyplot.savefig(dirPre + "NewDataPlots/" + fileName.split('.')[0] + "_As_Spikes" + LIMB_NAMES[limb] + "_" + 
            ORIENTATIONS[orientation] + "_Plot.png")    
dirList = os.listdir(os.path.curdir)
dirPre = ""
if not os.path.exists(dirPre + "NewDataPlots"):
        os.mkdir(dirPre + "NewDataPlots")
        
for fileName in dirList:
        if fileName.endswith(".dat"):
                print "Plotting " + fileName + "..."
                file = open(fileName, 'r')
                strLines = file.readlines()
                
                if len(strLines) == 0:
                        print "File " + fileName + " empty, on to next!"
                        continue 
                makeLine(RH,0)
                makeLine(LH,0)
                makeLine(LH_PPT_EULER,YAW)
                makeLine(RH_PPT_EULER,YAW)
                makeLine(LH_PPT_EULER,PITCH)
                makeLine(RH_PPT_EULER,PITCH)
                makeLine(LH_PPT_EULER,ROLL)
                makeLine(RH_PPT_EULER,ROLL)
                
                print "Finished!"
                

        



                        
                
                
                        
                
                        
                
        

