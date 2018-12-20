def ClockWiseRotation(Matrix): 
    for i in range(2):
        temp = Matrix[0][i]
        Matrix[0][i] = Matrix[2-i][0]
        Matrix[2-i][0] = Matrix[2][2-i]
        Matrix[2][2-i] = Matrix[i][2]
        Matrix[i][2] = temp
def AntiClockWiseRotation(Matrix): 
    for i in range(2):
        temp = Matrix[0][i]
        Matrix[0][i] = Matrix[i][2]
        Matrix[i][2] = Matrix[2][2-i]
        Matrix[2][2-i] = Matrix[2-i][0]
        Matrix[2-i][0] = temp
def SwapArray(Array):
        temp = Array[-1]
        for i in range(len(Array)-2,-1,-1):
                Array[i+1] = Array[i]
        Array[0] = temp
        return Array
def PrintMatrix(Matrix):
    for i in Matrix:
        for j in i:
            for k in j:
                print(k, end='')
            print()
        print()