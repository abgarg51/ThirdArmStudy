import os
from matplotlib import pyplot
import math

#Indexes for data
LH = 0
RH = 1
LF = 2
RF = 3
HEAD = 4
EULER = 5
DATE = 6
TIME = 7

LIMB_NAMES = ['LeftHand', 'RightHand', 'LeftFoot', 'RightFoot']

NUM_MIN = 9

def dist(p1, p2):
        return math.sqrt(math.pow(p2[0] - p1[0], 2) + math.pow(p2[1] - p1[1], 2))

def makeLine(limb):
        lines = []
        pyplot.clf()
        currMin = 0
        for i in range(len(strLines)-2):
                lines.append(eval(strLines[i]))
        prevTime = lines[0][TIME]
        for i in range(len(strLines)-2):
            if (currMin < 10):
                y = [0, dist(lines[i][limb], lines[(i + 1)][limb])]
                x = [i, i]
                pyplot.plot(x,y)
                v = [0, 35000, 0, .5]
                pyplot.axis(v)
                if lines[i][TIME] > (prevTime + 60):
                    currMin += 1
                    prevTime = prevTime + 60
        pyplot.savefig(dirPre + "NewDataPlots/" + fileName.split('.')[0] + "_As_Spikes" + LIMB_NAMES[limb] + "_Plot.png") 	
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
                makeLine(LF)
                makeLine(LH)
                makeLine(RF)
                makeLine(RH)
                
                print "Finished!"
                

        



                        
                
                
                        
                
                        
                
        

