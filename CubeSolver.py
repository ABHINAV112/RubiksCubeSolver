from Scrambler import ScramblingCube
from RubiksCube import Rubiks
from MatrixOperations import SwapArray
a = Rubiks()
ScramblingCube(a)
myMapping = a.ReturnMapping()
Moves = []
verifyWhiteCorner = [(0, 0), (2, 0), (2, 2), (0, 2)]
yellowCorners = [(0, 2), (2, 2), (2, 0), (0, 0)]
leftSide = [2, 3, 4, 1]
rightSide = [4, 1, 2, 3]
absolute='****************************'
def ExecCubeOperation(objectCube, command):
    Moves.append(command)
    exec(objectCube+'.'+command+'()')
#=================================================================================================================================================================================================================================
#constructing the white cross
whiteSide = [(0,1),(1,0),(2,1),(1,2)]
while True:
    for i in range(1,5):
        while True:
            if(a.cube[i][1][0] == 'w'):
                movingNumbers = [3,2,1,0]
                if(a.cube[leftSide[i-1]][1][2] == a.cube[leftSide[i-1]][1][1]):
                    ExecCubeOperation('a', myMapping[leftSide[i-1]][0])
                else:
                    colorIndex = a.colors.index(a.cube[leftSide[i-1]][1][2])
                    for j in range(colorIndex-1):
                        SwapArray(movingNumbers)
                    for j in range(movingNumbers[i-1]):
                        ExecCubeOperation("a",myMapping[0][0])
                    ExecCubeOperation("a", myMapping[leftSide[i-1]][0])
                    for j in range(movingNumbers[i-1]):
                        ExecCubeOperation("a",myMapping[0][1])
            elif(a.cube[i][0][1]=='w'):
                ExecCubeOperation("a",myMapping[i][1])
            elif(a.cube[i][2][1]=='w'):
                ExecCubeOperation("a",myMapping[i][0])
            elif(a.cube[i][1][2]=='w'):
                for j in range(2):
                    ExecCubeOperation("a",myMapping[i][0])
            elif(a.cube[i][0][1]!='w' and a.cube[i][1][0]!='w' and a.cube[i][1][2]!='w' and a.cube[i][2][1]!='w'):
                break
        if(a.cube[0][whiteSide[i-1][0]][whiteSide[i-1][1]]=='w' and a.cube[i][2][1]!=a.cube[i][1][1]):
            ExecCubeOperation("a", myMapping[i][0])
            ExecCubeOperation("a", myMapping[i][0])
    testMainList = []
    for i in range(1,5):
        if(a.cube[i][0][1] != 'w' and a.cube[i][1][0] != 'w' and a.cube[i][1][2] != 'w' and a.cube[i][2][1] != 'w'):
            testMainList.append(1)
    if(len(testMainList)==4):
        break
for i in range(2):
    a.RotateCubeLeft()
    Moves.append('RL')
fixedNumList = [(0,1),(1,0),(2,1),(1,2)]
while True:
    for i in range(1,5):
        if(a.cube[0][fixedNumList[i-1][0]][fixedNumList[i-1][1]]=='w'):
            if(a.cube[i][2][1]==a.cube[i][1][1]):
                for j in range(2):
                    ExecCubeOperation("a", myMapping[i][0])
            else:
                ExecCubeOperation("a","f2")
    if(a.cube[0][0][1] != 'w' and a.cube[0][1][0] != 'w' and a.cube[0][1][2] != 'w' and a.cube[0][2][1] != 'w'):
        break
for i in range(2):
    a.RotateCubeLeft()
    Moves.append('RL')
#=================================================================================================================================================================================================================================================
#solving the first layer
for k in range(1000):
    for i in range(1,5):
        if(a.cube[i][0][2] == 'w'):
            if(a.cube[rightSide[i-1]][0][0] == a.cube[rightSide[i-1]][1][1]):
                ExecCubeOperation("a", myMapping[i][1])
                ExecCubeOperation("a", myMapping[5][1])
                ExecCubeOperation("a", myMapping[i][0])
            else:
                ExecCubeOperation("a", myMapping[5][0])
        elif(a.cube[i][0][0] == 'w'):
            if(a.cube[leftSide[i-1]][0][2] == a.cube[leftSide[i-1]][1][1]):
                ExecCubeOperation("a", myMapping[i][0])
                Moves.append(myMapping[5][0])
                ExecCubeOperation("a", myMapping[5][0])
                ExecCubeOperation("a",myMapping[i][1])                
            else:
                ExecCubeOperation("a",myMapping[5][0])            
        elif(a.cube[i][2][0]=='w'):
            ExecCubeOperation("a", myMapping[i][0])
            ExecCubeOperation("a", myMapping[5][0])
            ExecCubeOperation("a", myMapping[i][1])
        elif(a.cube[i][2][2]=='w'):
            ExecCubeOperation("a", myMapping[i][1])
            ExecCubeOperation("a", myMapping[5][1])
            ExecCubeOperation("a", myMapping[i][0])
        elif(a.cube[0][verifyWhiteCorner[i-1][0]][verifyWhiteCorner[i-1][1]] == 'w'):
            if(a.cube[i][2][0]!=a.cube[i][1][1]):
                ExecCubeOperation("a", myMapping[i][0])
                ExecCubeOperation("a", myMapping[5][0])
                ExecCubeOperation("a", myMapping[i][1])
        elif (a.cube[5][0][0] == 'w' or a.cube[5][0][2] == 'w' or a.cube[5][2][0] == 'w' or a.cube[5][2][2] == 'w'):
            for j in range(1,5):        
                if(a.cube[5][yellowCorners[j-1][0]][yellowCorners[j-1][1]]=='w'):
                    ExecCubeOperation("a", myMapping[j][0])
                    ExecCubeOperation("a", myMapping[5][0])
                    ExecCubeOperation("a", myMapping[5][0])
                    ExecCubeOperation("a", myMapping[j][1])
    ExitList = []
    for i in range(1,5):
        if(a.cube[0][0][0]=='w' and a.cube[0][0][2]=='w' and a.cube[0][2][0]=='w' and a.cube[0][2][2]=='w' and a.cube[i][2][0]==a.cube[i][1][1] and a.cube[i][1][1]==a.cube[i][2][2]):
            ExitList.append(1)
    if(len(ExitList)==4):
        break
#=================================================================================================================================================================================================================================================================================
#solving the second layer
middleLayer = [(0,1),(1,2),(2,1),(1,0)]
while True:
    for i in range(1,5):
        if(a.cube[i][0][1]==a.cube[i][1][1]):
            if(a.cube[5][middleLayer[i-1][0]][middleLayer[i-1][1]] == a.cube[leftSide[i-1]][1][1]):
                ExecCubeOperation("a", myMapping[5][1])
                ExecCubeOperation("a", myMapping[leftSide[i-1]][1])
                ExecCubeOperation("a", myMapping[5][0])
                ExecCubeOperation("a", myMapping[leftSide[i-1]][0])
                ExecCubeOperation("a", myMapping[5][0])
                ExecCubeOperation("a", myMapping[i][0])
                ExecCubeOperation("a", myMapping[5][1])
                ExecCubeOperation("a", myMapping[i][1])
            elif(a.cube[5][middleLayer[i-1][0]][middleLayer[i-1][1]] == a.cube[rightSide[i-1]][1][1]):
                ExecCubeOperation("a", myMapping[5][0])
                ExecCubeOperation("a", myMapping[rightSide[i-1]][0])
                ExecCubeOperation("a", myMapping[5][1])
                ExecCubeOperation("a", myMapping[rightSide[i-1]][1])
                ExecCubeOperation("a", myMapping[5][1])
                ExecCubeOperation("a", myMapping[i][1])
                ExecCubeOperation("a", myMapping[5][0])
                ExecCubeOperation("a", myMapping[i][0])
        elif(a.cube[5][middleLayer[i-1][0]][middleLayer[i-1][1]] != 'y' and a.cube[i][0][1]!='y'):
            ExecCubeOperation("a", myMapping[5][0])
    for i in range(1,5):
        if(a.cube[i][1][0] != a.cube[i][1][1] and a.cube[i][1][0]!='y'):
            ExecCubeOperation("a", myMapping[i][0])
            ExecCubeOperation("a", myMapping[5][0])
            ExecCubeOperation("a", myMapping[i][1])
            ExecCubeOperation("a",myMapping[5][1])
            ExecCubeOperation("a", myMapping[leftSide[i-1]][1])
            ExecCubeOperation("a", myMapping[5][1])
            ExecCubeOperation("a", myMapping[leftSide[i-1]][0])
    testList = []
    for i in range(1,5):
        if(a.cube[i][1][0] == a.cube[i][1][1] == a.cube[i][1][2]):
            testList.append(1)
    if(len(testList) == 4):
        break
#==========================================================================================================================================================================================================================================================================================
#yellow cross
Moves.append('RL')
a.RotateCubeLeft()
Moves.append('RL')
a.RotateCubeLeft() 
while True:
    exitCondition = a.cube[0][0][1] == 'y' and a.cube[0][1][0] == 'y' and a.cube[0][1][2] == 'y' and a.cube[0][2][1] == 'y'
    if(a.cube[0][1][0] == 'y' and a.cube[0][1][2] == 'y' and not(exitCondition)):
        ExecCubeOperation("a", myMapping[3][0])
        ExecCubeOperation("a", myMapping[4][0])
        ExecCubeOperation("a", myMapping[0][0])
        ExecCubeOperation("a", myMapping[4][1])
        ExecCubeOperation("a",myMapping[0][1])
        ExecCubeOperation("a", myMapping[3][1])
    elif(a.cube[0][0][1] == 'y' and a.cube[0][1][0] == 'y' and not(exitCondition)):
        ExecCubeOperation("a", myMapping[3][0])
        ExecCubeOperation("a", myMapping[0][0])
        ExecCubeOperation("a", myMapping[4][0])
        ExecCubeOperation("a", myMapping[0][1])
        ExecCubeOperation("a", myMapping[4][1])
        ExecCubeOperation("a", myMapping[3][1])
    elif(a.cube[0][0][1] != 'y' and a.cube[0][1][0] != 'y' and a.cube[0][1][2] != 'y' and a.cube[0][2][1] != 'y'):
        ExecCubeOperation("a", myMapping[3][0])
        ExecCubeOperation("a", myMapping[4][0])
        ExecCubeOperation("a", myMapping[0][0])
        ExecCubeOperation("a", myMapping[4][1])
        ExecCubeOperation("a", myMapping[0][1])
        ExecCubeOperation("a", myMapping[3][1])
    elif(not(exitCondition)):
        ExecCubeOperation("a", myMapping[0][0])
    elif(exitCondition):
        break
#=================================================================================================================================================================================================================================================================================================================
#correct yellow cross
case = 0
perfect = ('r','g','o','b')
alternatives = [('g','o','b','r'),('o','b','r','g'),('b','r','g','o')]
matchings = [('b','r'),('r','g'),('g','o'),('o','b')] 
opposites = [('b','g'),('g','b'),('r','o'),('o','r')]
while True:
    if((a.cube[1][2][1], a.cube[2][2][1], a.cube[3][2][1], a.cube[4][2][1]) == perfect):
        case = 1
        break
    elif((a.cube[1][2][1], a.cube[2][2][1], a.cube[3][2][1], a.cube[4][2][1]) in alternatives):
        ExecCubeOperation("a",myMapping[0][0])
    elif(  (a.cube[4][2][1],a.cube[1][2][1]) in matchings):#correct
        case = 2
        break
    elif(   (a.cube[1][2][1],a.cube[3][2][1]) in opposites):#correct
        case = 3
        break
    else:
        ExecCubeOperation("a", myMapping[0][0])
if(case == 2):
    ExecCubeOperation("a", myMapping[4][0])
    ExecCubeOperation("a", myMapping[0][0])
    ExecCubeOperation("a", myMapping[4][1])
    ExecCubeOperation("a", myMapping[0][0])
    ExecCubeOperation("a", myMapping[4][0])
    ExecCubeOperation("a", myMapping[0][0])
    ExecCubeOperation("a", myMapping[0][0])
    ExecCubeOperation("a", myMapping[4][1])
if(case == 3):
    ExecCubeOperation("a", myMapping[4][0])
    ExecCubeOperation("a", myMapping[0][0])
    ExecCubeOperation("a", myMapping[4][1])
    ExecCubeOperation("a", myMapping[0][0])
    ExecCubeOperation("a", myMapping[4][0])
    ExecCubeOperation("a", myMapping[0][0])
    ExecCubeOperation("a", myMapping[0][0])
    ExecCubeOperation("a", myMapping[4][1])
    ExecCubeOperation("a", myMapping[0][1])
    ExecCubeOperation("a", myMapping[4][0])
    ExecCubeOperation("a", myMapping[0][0])
    ExecCubeOperation("a", myMapping[4][1])
    ExecCubeOperation("a", myMapping[0][0])
    ExecCubeOperation("a", myMapping[4][0])
    ExecCubeOperation("a", myMapping[0][0])
    ExecCubeOperation("a", myMapping[0][0])
    ExecCubeOperation("a", myMapping[4][1])
while (a.cube[1][2][1], a.cube[2][2][1], a.cube[3][2][1], a.cube[4][2][1]) != perfect:
    ExecCubeOperation("a", myMapping[0][0])
#=================================================================================================================================================================================================================================================================================================================
#correcting edge pieces
yellowCorners = [(0,0),(2,0),(2,2),(0,2)]
backSide = [3,4,1,2]
while True:
    side  = []
    for i in range(1,5):
        if(a.cube[i][2][0] in [a.cube[i][1][1] , a.cube[leftSide[i-1]][1][1] , a.cube[0][1][1]]):
            if(a.cube[leftSide[i-1]][2][2] in [a.cube[i][1][1], a.cube[leftSide[i-1]][1][1], a.cube[0][1][1]]):
                if(  a.cube[0] [yellowCorners[i-1][0]] [yellowCorners[i-1][1]] in [a.cube[i][1][1], a.cube[leftSide[i-1]][1][1], a.cube[0][1][1]]):
                    side.append(i)
    if(len(side) == 4):
        case = 'perfect'
    elif(len(side)==0):
        case = 0 
    elif(len(side) == 1):
        case = side[0] 
    if(case == 0):
        ExecCubeOperation("a", myMapping[4][0])
        ExecCubeOperation("a", myMapping[0][1])
        ExecCubeOperation("a", myMapping[2][1])
        ExecCubeOperation("a", myMapping[0][0])
        ExecCubeOperation("a", myMapping[4][1])
        ExecCubeOperation("a", myMapping[0][1])
        ExecCubeOperation("a", myMapping[2][0])
        ExecCubeOperation("a", myMapping[0][0])
    elif(case!='perfect'):
        ExecCubeOperation("a", myMapping[backSide[case-1]][0])
        ExecCubeOperation("a", myMapping[0][1])
        ExecCubeOperation("a", myMapping[case][1])
        ExecCubeOperation("a", myMapping[0][0])
        ExecCubeOperation("a", myMapping[backSide[case-1]][1])
        ExecCubeOperation("a", myMapping[0][1])
        ExecCubeOperation("a", myMapping[case][0])
        ExecCubeOperation("a", myMapping[0][0])
    if(case == 'perfect'):
        break
#=================================================================================================================================================================================================================================================================================================================
#finshing yellow layer
algoTimes = []
for i in range(1,5):
    if(a.cube[0][yellowCorners[i-1][0]][yellowCorners[i-1][1]] =='y'):
        algoTimes.append(0)
    elif(a.cube[i][2][0]=='y'):
        algoTimes.append(1)
    else:
        algoTimes.append(2)
for i in range(1,5):
    for j in range(algoTimes[i-1]):
        ExecCubeOperation("a", myMapping[1][0])
        ExecCubeOperation("a", myMapping[5][0])
        ExecCubeOperation("a", myMapping[1][1])
        ExecCubeOperation("a", myMapping[5][1])
        ExecCubeOperation("a", myMapping[1][0])
        ExecCubeOperation("a", myMapping[5][0])
        ExecCubeOperation("a", myMapping[1][1])
        ExecCubeOperation("a", myMapping[5][1])
    ExecCubeOperation("a", myMapping[0][0])
for i in range(2):
    Moves.append('RL')
    a.RotateCubeLeft()
#=================================================================================================================================================================================================================================================================================================================
a.CubeStatus()
print(Moves)