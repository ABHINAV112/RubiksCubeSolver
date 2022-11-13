from random import randint
def scramble(myCube):   
    myMapping = myCube.get_mapping()
    noShuffle = 10000
    shuffleMoves = []
    shuffleMovesIndex = []
    for _ in range(noShuffle):
        MoveIndex = (randint(0,4),randint(0,1))
        Move = myMapping[MoveIndex[0]][MoveIndex[1]]
        shuffleMovesIndex.append(MoveIndex)
        shuffleMoves.append(Move)
        exec('myCube.'+Move+'()')