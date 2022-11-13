from MatrixOperations import anti_clock_wise_rotation, clock_wise_rotation

class RubiksCube:
    # 0-front, 1-top, 2-left, 3-bottom, 4-right, 5-back
    #all the bottom edges are connected to the front face and all the top edges are connected to the back face
    def __init__(self):
        self.colors = ['w', 'r', 'b', 'o', 'g', 'y']
        self.cube = [] 
        for i in self.colors:
            self.cube.append([[i for j in range(3)] for k in range(3)])
        self.mapping = (('f1', 'f2'),('t1', 't2'),('l1', 'l2'),('b1', 'b2'),('r1', 'r2'),('d1','d2'))

    def cube_status(self):
        for i in self.cube:
            for j in i:
                for k in j:
                    print(k, end='')
                print()
            print()
    
    def get_mapping(self):
        return self.mapping

    def f1(self):   
        clock_wise_rotation(self.cube[0])
        for i in range(3):
            temp = self.cube[1][2][i]
            self.cube[1][2][i] = self.cube[2][2][i]
            self.cube[2][2][i] = self.cube[3][2][i]
            self.cube[3][2][i] = self.cube[4][2][i]
            self.cube[4][2][i] = temp
    
    def f2(self):
        anti_clock_wise_rotation(self.cube[0])
        for i in range(3):
            temp = self.cube[1][2][i]
            self.cube[1][2][i] = self.cube[4][2][i]
            self.cube[4][2][i] = self.cube[3][2][i]
            self.cube[3][2][i] = self.cube[2][2][i]
            self.cube[2][2][i] = temp
    
    def rotate_cube_right(self):
        #right-> front front->left left->back back->right
        temp = self.cube[4]
        self.cube[4] = self.cube[0]
        self.cube[0] = self.cube[2]
        self.cube[2] = self.cube[5]
        self.cube[5] = temp

        anti_clock_wise_rotation(self.cube[0])
        anti_clock_wise_rotation(self.cube[4])
        anti_clock_wise_rotation(self.cube[1])
        clock_wise_rotation(self.cube[2])
        clock_wise_rotation(self.cube[5])
        clock_wise_rotation(self.cube[3])

    def rotate_cube_left(self):
        #right->front front->left left->back back->right
        temp = self.cube[4]
        self.cube[4] = self.cube[5]
        self.cube[5] = self.cube[2]
        self.cube[2] = self.cube[0]
        self.cube[0] = temp

        clock_wise_rotation(self.cube[0])
        clock_wise_rotation(self.cube[2])
        clock_wise_rotation(self.cube[1])
        anti_clock_wise_rotation(self.cube[5])
        anti_clock_wise_rotation(self.cube[4])
        anti_clock_wise_rotation(self.cube[3])
    
    def rotate_cube_down(self):
        #top->face face->bottom bottom->back back->top
        temp = self.cube[0]
        self.cube[0] = self.cube[1]
        self.cube[1] = self.cube[5]
        self.cube[5] = self.cube[3]
        self.cube[3] = temp

        clock_wise_rotation(self.cube[3])
        clock_wise_rotation(self.cube[3])
        anti_clock_wise_rotation(self.cube[1])
        anti_clock_wise_rotation(self.cube[1])
        clock_wise_rotation(self.cube[2])
        anti_clock_wise_rotation(self.cube[4])
    
    def rotate_cube_up(self):
        #front->top top->back back->botton botton->face
        temp = self.cube[1]
        self.cube[1] = self.cube[0]
        self.cube[0] = self.cube[3]
        self.cube[3] = self.cube[5]
        self.cube[5] = temp

        clock_wise_rotation(self.cube[0])
        clock_wise_rotation(self.cube[0])
        anti_clock_wise_rotation(self.cube[5])
        anti_clock_wise_rotation(self.cube[5])
        anti_clock_wise_rotation(self.cube[2])
        clock_wise_rotation(self.cube[4])

    def l1(self):
        self.rotate_cube_right()
        self.f1()
        self.rotate_cube_left()

    def l2(self):
        self.rotate_cube_right()
        self.f2()
        self.rotate_cube_left()

    def r1(self):
        self.rotate_cube_left()
        self.f1()
        self.rotate_cube_right()

    def r2(self):
        self.rotate_cube_left()
        self.f2()
        self.rotate_cube_right()

    def t1(self):
        self.rotate_cube_down()
        self.f1()
        self.rotate_cube_up()

    def t2(self):
        self.rotate_cube_down()
        self.f2()
        self.rotate_cube_up()

    def b1(self):
        self.rotate_cube_up()
        self.f1()
        self.rotate_cube_down()

    def b2(self):
        self.rotate_cube_up()
        self.f2()
        self.rotate_cube_down()

    def d1(self):
        self.rotate_cube_up()
        self.rotate_cube_up()
        self.f1()
        self.rotate_cube_up()
        self.rotate_cube_up()

    def d2(self):
        self.rotate_cube_up()
        self.rotate_cube_up()
        self.f2()
        self.rotate_cube_up()
        self.rotate_cube_up()
