from MatrixOperations import AntiClockWiseRotation, ClockWiseRotation, PrintMatrix

class Rubiks:
    # 0-front, 1-top, 2-left, 3-bottom, 4-right, 5-back
    #all the bottom edges are connected to the front face and all the top edges are connected to the back face
    def __init__(self):
        self.colors = ['w', 'r', 'b', 'o', 'g', 'y']
        self.cube = [] 
        for i in self.colors:
            self.cube.append([[i for j in range(3)] for k in range(3)])
        self.mapping = (('f1', 'f2'),('t1', 't2'),('l1', 'l2'),('b1', 'b2'),('r1', 'r2'),('d1','d2'))

    def CubeStatus(self):
        PrintMatrix(self.cube)
    
    def ReturnMapping(self):
        return self.mapping

    def f1(self):   
        ClockWiseRotation(self.cube[0])
        for i in range(3):
            temp = self.cube[1][2][i]
            self.cube[1][2][i] = self.cube[2][2][i]
            self.cube[2][2][i] = self.cube[3][2][i]
            self.cube[3][2][i] = self.cube[4][2][i]
            self.cube[4][2][i] = temp
    
    def f2(self):
        AntiClockWiseRotation(self.cube[0])
        for i in range(3):
            temp = self.cube[1][2][i]
            self.cube[1][2][i] = self.cube[4][2][i]
            self.cube[4][2][i] = self.cube[3][2][i]
            self.cube[3][2][i] = self.cube[2][2][i]
            self.cube[2][2][i] = temp
    
    def RotateCubeRight(self):
        #right-> front front->left left->back back->right
        temp = self.cube[4]
        self.cube[4] = self.cube[0]
        self.cube[0] = self.cube[2]
        self.cube[2] = self.cube[5]
        self.cube[5] = temp

        AntiClockWiseRotation(self.cube[0])
        AntiClockWiseRotation(self.cube[4])
        AntiClockWiseRotation(self.cube[1])
        ClockWiseRotation(self.cube[2])
        ClockWiseRotation(self.cube[5])
        ClockWiseRotation(self.cube[3])

    def RotateCubeLeft(self):
        #right->front front->left left->back back->right
        temp = self.cube[4]
        self.cube[4] = self.cube[5]
        self.cube[5] = self.cube[2]
        self.cube[2] = self.cube[0]
        self.cube[0] = temp

        ClockWiseRotation(self.cube[0])
        ClockWiseRotation(self.cube[2])
        ClockWiseRotation(self.cube[1])
        AntiClockWiseRotation(self.cube[5])
        AntiClockWiseRotation(self.cube[4])
        AntiClockWiseRotation(self.cube[3])
    
    def RotateCubeDown(self):
        #top->face face->bottom bottom->back back->top
        temp = self.cube[0]
        self.cube[0] = self.cube[1]
        self.cube[1] = self.cube[5]
        self.cube[5] = self.cube[3]
        self.cube[3] = temp

        ClockWiseRotation(self.cube[3])
        ClockWiseRotation(self.cube[3])
        AntiClockWiseRotation(self.cube[1])
        AntiClockWiseRotation(self.cube[1])
        ClockWiseRotation(self.cube[2])
        AntiClockWiseRotation(self.cube[4])
    
    def RotateCubeUp(self):
        #front->top top->back back->botton botton->face
        temp = self.cube[1]
        self.cube[1] = self.cube[0]
        self.cube[0] = self.cube[3]
        self.cube[3] = self.cube[5]
        self.cube[5] = temp

        ClockWiseRotation(self.cube[0])
        ClockWiseRotation(self.cube[0])
        AntiClockWiseRotation(self.cube[5])
        AntiClockWiseRotation(self.cube[5])
        AntiClockWiseRotation(self.cube[2])
        ClockWiseRotation(self.cube[4])

    def l1(self):
        self.RotateCubeRight()
        self.f1()
        self.RotateCubeLeft()

    def l2(self):
        self.RotateCubeRight()
        self.f2()
        self.RotateCubeLeft()

    def r1(self):
        self.RotateCubeLeft()
        self.f1()
        self.RotateCubeRight()

    def r2(self):
        self.RotateCubeLeft()
        self.f2()
        self.RotateCubeRight()

    def t1(self):
        self.RotateCubeDown()
        self.f1()
        self.RotateCubeUp()

    def t2(self):
        self.RotateCubeDown()
        self.f2()
        self.RotateCubeUp()

    def b1(self):
        self.RotateCubeUp()
        self.f1()
        self.RotateCubeDown()

    def b2(self):
        self.RotateCubeUp()
        self.f2()
        self.RotateCubeDown()

    def d1(self):
        self.RotateCubeUp()
        self.RotateCubeUp()
        self.f1()
        self.RotateCubeUp()
        self.RotateCubeUp()

    def d2(self):
        self.RotateCubeUp()
        self.RotateCubeUp()
        self.f2()
        self.RotateCubeUp()
        self.RotateCubeUp()
