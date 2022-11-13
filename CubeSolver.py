from Scrambler import scramble
from RubiksCube import RubiksCube
from MatrixOperations import swap_array
from Faces import *

rubiks_cube = RubiksCube()
scramble(rubiks_cube)
rubiks_cube.cube_status()
face_move_mapping = rubiks_cube.get_mapping()
moves = []
verify_white_corner = [(0, 0), (2, 0), (2, 2), (0, 2)]
yellow_corners = [(0, 2), (2, 2), (2, 0), (0, 0)]
leftSide = [2, 3, 4, 1]
rightSide = [4, 1, 2, 3]


def execute_cube_operation(command):
    moves.append(command)
    exec('rubiks_cube.' + command + '()')


#=================================================================================================================================================================================================================================
#constructing the white cross
whiteSide = [(0, 1), (1, 0), (2, 1), (1, 2)]
while True:
    for i in (TOP,LEFT,BOTTOM,RIGHT):
        while True:
            if (rubiks_cube.cube[i][1][0] == 'w'):
                movingNumbers = [3, 2, 1, 0]
                if (rubiks_cube.cube[leftSide[i - 1]][1][2] ==
                        rubiks_cube.cube[leftSide[i - 1]][1][1]):
                    execute_cube_operation(face_move_mapping[leftSide[i - 1]][0])
                else:
                    colorIndex = rubiks_cube.colors.index(
                        rubiks_cube.cube[leftSide[i - 1]][1][2])
                    for j in range(colorIndex - 1):
                        swap_array(movingNumbers)
                    for j in range(movingNumbers[i - 1]):
                        execute_cube_operation(face_move_mapping[FRONT][0])
                    execute_cube_operation(face_move_mapping[leftSide[i - 1]][0])
                    for j in range(movingNumbers[i - 1]):
                        execute_cube_operation(face_move_mapping[FRONT][1])
            elif (rubiks_cube.cube[i][0][1] == 'w'):
                execute_cube_operation(face_move_mapping[i][1])
            elif (rubiks_cube.cube[i][2][1] == 'w'):
                execute_cube_operation(face_move_mapping[i][0])
            elif (rubiks_cube.cube[i][1][2] == 'w'):
                for j in range(2):
                    execute_cube_operation(face_move_mapping[i][0])
            elif (rubiks_cube.cube[i][0][1] != 'w'
                  and rubiks_cube.cube[i][1][0] != 'w'
                  and rubiks_cube.cube[i][1][2] != 'w'
                  and rubiks_cube.cube[i][2][1] != 'w'):
                break
        if (rubiks_cube.cube[0][whiteSide[i - 1][0]][whiteSide[i - 1][1]]
                == 'w'
                and rubiks_cube.cube[i][2][1] != rubiks_cube.cube[i][1][1]):
            execute_cube_operation(face_move_mapping[i][0])
            execute_cube_operation(face_move_mapping[i][0])
    testMainList = []
    for i in (TOP,LEFT,BOTTOM,RIGHT):
        if (rubiks_cube.cube[i][0][1] != 'w'
                and rubiks_cube.cube[i][1][0] != 'w'
                and rubiks_cube.cube[i][1][2] != 'w'
                and rubiks_cube.cube[i][2][1] != 'w'):
            testMainList.append(1)
    if (len(testMainList) == 4):
        break
for i in range(2):
    rubiks_cube.rotate_cube_left()
    moves.append('RL')
fixedNumList = [(0, 1), (1, 0), (2, 1), (1, 2)]
while True:
    for i in (TOP,LEFT,BOTTOM,RIGHT):
        if (rubiks_cube.cube[0][fixedNumList[i - 1][0]][fixedNumList[i - 1][1]]
                == 'w'):
            if (rubiks_cube.cube[i][2][1] == rubiks_cube.cube[i][1][1]):
                for j in range(2):
                    execute_cube_operation(face_move_mapping[i][0])
            else:
                execute_cube_operation("f2")
    if (rubiks_cube.cube[0][0][1] != 'w' and rubiks_cube.cube[0][1][0] != 'w'
            and rubiks_cube.cube[0][1][2] != 'w'
            and rubiks_cube.cube[0][2][1] != 'w'):
        break
for i in range(2):
    rubiks_cube.rotate_cube_left()
    moves.append('RL')
#=================================================================================================================================================================================================================================================
#solving the first layer
for k in range(1000):
    for i in (TOP,LEFT,BOTTOM,RIGHT):
        if (rubiks_cube.cube[i][0][2] == 'w'):
            if (rubiks_cube.cube[rightSide[i - 1]][0][0] == rubiks_cube.cube[
                    rightSide[i - 1]][1][1]):
                execute_cube_operation(face_move_mapping[i][1])
                execute_cube_operation(face_move_mapping[BACK][1])
                execute_cube_operation(face_move_mapping[i][0])
            else:
                execute_cube_operation(face_move_mapping[BACK][0])
        elif (rubiks_cube.cube[i][0][0] == 'w'):
            if (rubiks_cube.cube[leftSide[i - 1]][0][2] == rubiks_cube.cube[
                    leftSide[i - 1]][1][1]):
                execute_cube_operation(face_move_mapping[i][0])
                moves.append(face_move_mapping[BACK][0])
                execute_cube_operation(face_move_mapping[BACK][0])
                execute_cube_operation(face_move_mapping[i][1])
            else:
                execute_cube_operation(face_move_mapping[BACK][0])
        elif (rubiks_cube.cube[i][2][0] == 'w'):
            execute_cube_operation(face_move_mapping[i][0])
            execute_cube_operation(face_move_mapping[BACK][0])
            execute_cube_operation(face_move_mapping[i][1])
        elif (rubiks_cube.cube[i][2][2] == 'w'):
            execute_cube_operation(face_move_mapping[i][1])
            execute_cube_operation(face_move_mapping[BACK][1])
            execute_cube_operation(face_move_mapping[i][0])
        elif (rubiks_cube.cube[0][verify_white_corner[i - 1][0]][
                verify_white_corner[i - 1][1]] == 'w'):
            if (rubiks_cube.cube[i][2][0] != rubiks_cube.cube[i][1][1]):
                execute_cube_operation(face_move_mapping[i][0])
                execute_cube_operation(face_move_mapping[BACK][0])
                execute_cube_operation(face_move_mapping[i][1])
        elif (rubiks_cube.cube[5][0][0] == 'w'
              or rubiks_cube.cube[5][0][2] == 'w'
              or rubiks_cube.cube[5][2][0] == 'w'
              or rubiks_cube.cube[5][2][2] == 'w'):
            for j in range(1, 5):
                if (rubiks_cube.cube[5][yellow_corners[j - 1][0]][
                        yellow_corners[j - 1][1]] == 'w'):
                    execute_cube_operation(face_move_mapping[j][0])
                    execute_cube_operation(face_move_mapping[BACK][0])
                    execute_cube_operation(face_move_mapping[BACK][0])
                    execute_cube_operation(face_move_mapping[j][1])
    ExitList = []
    for i in (TOP,LEFT,BOTTOM,RIGHT):
        if (rubiks_cube.cube[FRONT][0][0] == 'w'
                and rubiks_cube.cube[FRONT][0][2] == 'w'
                and rubiks_cube.cube[FRONT][2][0] == 'w'
                and rubiks_cube.cube[FRONT][2][2] == 'w'
                and rubiks_cube.cube[i][2][0] == rubiks_cube.cube[i][1][1]
                and rubiks_cube.cube[i][1][1] == rubiks_cube.cube[i][2][2]):
            ExitList.append(1)
    if (len(ExitList) == 4):
        break
#=================================================================================================================================================================================================================================================================================
#solving the second layer
middleLayer = [(0, 1), (1, 2), (2, 1), (1, 0)]
while True:
    for i in (TOP,LEFT,BOTTOM,RIGHT):
        if (rubiks_cube.cube[i][0][1] == rubiks_cube.cube[i][1][1]):
            if (rubiks_cube.cube[5][middleLayer[i - 1][0]][middleLayer[
                    i - 1][1]] == rubiks_cube.cube[leftSide[i - 1]][1][1]):
                execute_cube_operation(face_move_mapping[BACK][1])
                execute_cube_operation(face_move_mapping[leftSide[i - 1]][1])
                execute_cube_operation(face_move_mapping[BACK][0])
                execute_cube_operation(face_move_mapping[leftSide[i - 1]][0])
                execute_cube_operation(face_move_mapping[BACK][0])
                execute_cube_operation(face_move_mapping[i][0])
                execute_cube_operation(face_move_mapping[BACK][1])
                execute_cube_operation(face_move_mapping[i][1])
            elif (rubiks_cube.cube[5][middleLayer[i - 1][0]][middleLayer[
                    i - 1][1]] == rubiks_cube.cube[rightSide[i - 1]][1][1]):
                execute_cube_operation(face_move_mapping[BACK][0])
                execute_cube_operation(face_move_mapping[rightSide[i - 1]][0])
                execute_cube_operation(face_move_mapping[BACK][1])
                execute_cube_operation(face_move_mapping[rightSide[i - 1]][1])
                execute_cube_operation(face_move_mapping[BACK][1])
                execute_cube_operation(face_move_mapping[i][1])
                execute_cube_operation(face_move_mapping[BACK][0])
                execute_cube_operation(face_move_mapping[i][0])
        elif (rubiks_cube.cube[5][middleLayer[i - 1][0]][middleLayer[i - 1][1]]
              != 'y' and rubiks_cube.cube[i][0][1] != 'y'):
            execute_cube_operation(face_move_mapping[BACK][0])
    for i in (TOP,LEFT,BOTTOM,RIGHT):
        if (rubiks_cube.cube[i][1][0] != rubiks_cube.cube[i][1][1]
                and rubiks_cube.cube[i][1][0] != 'y'):
            execute_cube_operation(face_move_mapping[i][0])
            execute_cube_operation(face_move_mapping[BACK][0])
            execute_cube_operation(face_move_mapping[i][1])
            execute_cube_operation(face_move_mapping[BACK][1])
            execute_cube_operation(face_move_mapping[leftSide[i - 1]][1])
            execute_cube_operation(face_move_mapping[BACK][1])
            execute_cube_operation(face_move_mapping[leftSide[i - 1]][0])
    testList = []
    for i in (TOP,LEFT,BOTTOM,RIGHT):
        if (rubiks_cube.cube[i][1][0] == rubiks_cube.cube[i][1][1] ==
                rubiks_cube.cube[i][1][2]):
            testList.append(1)
    if (len(testList) == 4):
        break
#==========================================================================================================================================================================================================================================================================================
#yellow cross
moves.append('RL')
rubiks_cube.rotate_cube_left()
moves.append('RL')
rubiks_cube.rotate_cube_left()
while True:
    exitCondition = rubiks_cube.cube[0][0][1] == 'y' and rubiks_cube.cube[0][
        1][0] == 'y' and rubiks_cube.cube[0][1][2] == 'y' and rubiks_cube.cube[
            0][2][1] == 'y'
    if (rubiks_cube.cube[0][1][0] == 'y' and rubiks_cube.cube[0][1][2] == 'y'
            and not (exitCondition)):
        execute_cube_operation(face_move_mapping[BOTTOM][0])
        execute_cube_operation(face_move_mapping[RIGHT][0])
        execute_cube_operation(face_move_mapping[FRONT][0])
        execute_cube_operation(face_move_mapping[RIGHT][1])
        execute_cube_operation(face_move_mapping[FRONT][1])
        execute_cube_operation(face_move_mapping[BOTTOM][1])
    elif (rubiks_cube.cube[0][0][1] == 'y' and rubiks_cube.cube[0][1][0] == 'y'
          and not (exitCondition)):
        execute_cube_operation(face_move_mapping[BOTTOM][0])
        execute_cube_operation(face_move_mapping[FRONT][0])
        execute_cube_operation(face_move_mapping[RIGHT][0])
        execute_cube_operation(face_move_mapping[FRONT][1])
        execute_cube_operation(face_move_mapping[RIGHT][1])
        execute_cube_operation(face_move_mapping[BOTTOM][1])
    elif (rubiks_cube.cube[0][0][1] != 'y' and rubiks_cube.cube[0][1][0] != 'y'
          and rubiks_cube.cube[0][1][2] != 'y'
          and rubiks_cube.cube[0][2][1] != 'y'):
        execute_cube_operation(face_move_mapping[BOTTOM][0])
        execute_cube_operation(face_move_mapping[RIGHT][0])
        execute_cube_operation(face_move_mapping[FRONT][0])
        execute_cube_operation(face_move_mapping[RIGHT][1])
        execute_cube_operation(face_move_mapping[FRONT][1])
        execute_cube_operation(face_move_mapping[BOTTOM][1])
    elif (not (exitCondition)):
        execute_cube_operation(face_move_mapping[FRONT][0])
    elif (exitCondition):
        break
#=================================================================================================================================================================================================================================================================================================================
#correct yellow cross
case = 0
perfect = ('r', 'g', 'o', 'b')
alternatives = [('g', 'o', 'b', 'r'), ('o', 'b', 'r', 'g'),
                ('b', 'r', 'g', 'o')]
matchings = [('b', 'r'), ('r', 'g'), ('g', 'o'), ('o', 'b')]
opposites = [('b', 'g'), ('g', 'b'), ('r', 'o'), ('o', 'r')]
while True:
    if ((rubiks_cube.cube[1][2][1], rubiks_cube.cube[2][2][1],
         rubiks_cube.cube[3][2][1], rubiks_cube.cube[4][2][1]) == perfect):
        break
    elif ((rubiks_cube.cube[1][2][1], rubiks_cube.cube[2][2][1],
           rubiks_cube.cube[3][2][1], rubiks_cube.cube[4][2][1])
          in alternatives):
        execute_cube_operation(face_move_mapping[FRONT][0])
    elif ((rubiks_cube.cube[4][2][1], rubiks_cube.cube[1][2][1])
          in matchings):  #correct
        execute_cube_operation(face_move_mapping[RIGHT][0])
        execute_cube_operation(face_move_mapping[FRONT][0])
        execute_cube_operation(face_move_mapping[RIGHT][1])
        execute_cube_operation(face_move_mapping[FRONT][0])
        execute_cube_operation(face_move_mapping[RIGHT][0])
        execute_cube_operation(face_move_mapping[FRONT][0])
        execute_cube_operation(face_move_mapping[FRONT][0])
        execute_cube_operation(face_move_mapping[RIGHT][1])
        break
    elif ((rubiks_cube.cube[1][2][1], rubiks_cube.cube[3][2][1])
          in opposites):  #correct
        execute_cube_operation(face_move_mapping[RIGHT][0])
        execute_cube_operation(face_move_mapping[FRONT][0])
        execute_cube_operation(face_move_mapping[RIGHT][1])
        execute_cube_operation(face_move_mapping[FRONT][0])
        execute_cube_operation(face_move_mapping[RIGHT][0])
        execute_cube_operation(face_move_mapping[FRONT][0])
        execute_cube_operation(face_move_mapping[FRONT][0])
        execute_cube_operation(face_move_mapping[RIGHT][1])
        execute_cube_operation(face_move_mapping[FRONT][1])
        execute_cube_operation(face_move_mapping[RIGHT][0])
        execute_cube_operation(face_move_mapping[FRONT][0])
        execute_cube_operation(face_move_mapping[RIGHT][1])
        execute_cube_operation(face_move_mapping[FRONT][0])
        execute_cube_operation(face_move_mapping[RIGHT][0])
        execute_cube_operation(face_move_mapping[FRONT][0])
        execute_cube_operation(face_move_mapping[FRONT][0])
        execute_cube_operation(face_move_mapping[RIGHT][1])
        break
    else:
        execute_cube_operation(face_move_mapping[FRONT][0])

while (rubiks_cube.cube[1][2][1], rubiks_cube.cube[2][2][1],
       rubiks_cube.cube[3][2][1], rubiks_cube.cube[4][2][1]) != perfect:
    execute_cube_operation(face_move_mapping[FRONT][0])
#=================================================================================================================================================================================================================================================================================================================
#correcting edge pieces
yellow_corners = [(0, 0), (2, 0), (2, 2), (0, 2)]
backSide = [3, 4, 1, 2]
while True:
    side = []
    for i in (TOP,LEFT,BOTTOM,RIGHT):
        if (rubiks_cube.cube[i][2][0] in [
                rubiks_cube.cube[i][1][1],
                rubiks_cube.cube[leftSide[i - 1]][1][1],
                rubiks_cube.cube[0][1][1]
        ]):
            if (rubiks_cube.cube[leftSide[i - 1]][2][2] in [
                    rubiks_cube.cube[i][1][1],
                    rubiks_cube.cube[leftSide[i - 1]][1][1],
                    rubiks_cube.cube[0][1][1]
            ]):
                if (rubiks_cube.cube[0][yellow_corners[i - 1][0]][
                        yellow_corners[i - 1][1]] in [
                            rubiks_cube.cube[i][1][1],
                            rubiks_cube.cube[leftSide[i - 1]][1][1],
                            rubiks_cube.cube[0][1][1]
                        ]):
                    side.append(i)
    if (len(side) == 4):
        case = 'perfect'
    elif (len(side) == 0):
        case = 0
    elif (len(side) == 1):
        case = side[0]
    if (case == 0):
        execute_cube_operation(face_move_mapping[RIGHT][0])
        execute_cube_operation(face_move_mapping[FRONT][1])
        execute_cube_operation(face_move_mapping[LEFT][1])
        execute_cube_operation(face_move_mapping[FRONT][0])
        execute_cube_operation(face_move_mapping[RIGHT][1])
        execute_cube_operation(face_move_mapping[FRONT][1])
        execute_cube_operation(face_move_mapping[LEFT][0])
        execute_cube_operation(face_move_mapping[FRONT][0])
    elif (case != 'perfect'):
        execute_cube_operation(face_move_mapping[backSide[case - 1]][0])
        execute_cube_operation(face_move_mapping[FRONT][1])
        execute_cube_operation(face_move_mapping[case][1])
        execute_cube_operation(face_move_mapping[FRONT][0])
        execute_cube_operation(face_move_mapping[backSide[case - 1]][1])
        execute_cube_operation(face_move_mapping[FRONT][1])
        execute_cube_operation(face_move_mapping[case][0])
        execute_cube_operation(face_move_mapping[FRONT][0])
    if (case == 'perfect'):
        break
#=================================================================================================================================================================================================================================================================================================================
#finshing yellow layer
algo_times = []
for i in (TOP,LEFT,BOTTOM,RIGHT):
    if (rubiks_cube.cube[0][yellow_corners[i - 1][0]][yellow_corners[i - 1][1]]
            == 'y'):
        algo_times.append(0)
    elif (rubiks_cube.cube[i][2][0] == 'y'):
        algo_times.append(1)
    else:
        algo_times.append(2)
for i in (TOP,LEFT,BOTTOM,RIGHT):
    for j in range(algo_times[i - 1]):
        execute_cube_operation(face_move_mapping[TOP][0])
        execute_cube_operation(face_move_mapping[BACK][0])
        execute_cube_operation(face_move_mapping[TOP][1])
        execute_cube_operation(face_move_mapping[BACK][1])
        execute_cube_operation(face_move_mapping[TOP][0])
        execute_cube_operation(face_move_mapping[BACK][0])
        execute_cube_operation(face_move_mapping[TOP][1])
        execute_cube_operation(face_move_mapping[BACK][1])
    execute_cube_operation(face_move_mapping[FRONT][0])
for i in range(2):
    moves.append('RL')
    rubiks_cube.rotate_cube_left()
#=================================================================================================================================================================================================================================================================================================================
print(moves)
rubiks_cube.cube_status()