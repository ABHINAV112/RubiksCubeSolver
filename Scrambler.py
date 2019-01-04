from RubiksCube import Rubiks
from random import randint
def ScramblingCube(myCube):   
    myMapping = myCube.ReturnMapping()
    noShuffle = 10000
    shuffleMoves = []
    shuffleMovesIndex = []
    for i in range(noShuffle):
        MoveIndex = (randint(0,4),randint(0,1))
        Move = myMapping[MoveIndex[0]][MoveIndex[1]]
        shuffleMovesIndex.append(MoveIndex)
        shuffleMoves.append(Move)
        exec('myCube.'+Move+'()')