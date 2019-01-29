# RubiksCubeSolver

Python learning project, backend required to generate the solution for a randomly shuffled rubiks cube. The code has been built entirely from scratch, and prints out an a list of how to solve a rubiks cube. The program uses object oriented programming to come up with a solution for the rubiks cube.

## Model of the Rubiks Cube stored in the program
The data of the Rubiks Cube is stored in a 3D List. When viewed from the front, the 0th element corresponds to the front face, the 1st, 2nd, 3rd and 4th element of the array correspond to the top, left, bottom and right face of the cube. the 5th element of the array corresponds to the back face. 
The front face of the Rubiks Cube is stored as seen from the outside, the faces top, left, bottom and right faces are stored such that the bottom of their corresponding 2D matrices is connected to the front face. The back face is connected just as it appears outside.

## Output

### Shuffled Cube
```
wrb
owr
ogw

ybw
orr
bgr

rgg
bbg
bwo

orb
ooy
gyy

oyg
ygb
wbr

gwr
oyw
ywy
```

### Solved Cube
```

www
www
www

rrr
rrr
rrr

bbb
bbb
bbb

ooo
ooo
ooo

ggg
ggg
ggg

yyy
yyy
yyy
```

### Generated Algorithm
```
['l1', 'b1', 'f1', 'f1', 'b1', 'f2', 'f2', 'f1', 'f1', 'l1',
'f2', 'f2', 'RL', 'RL', 'f2', 'f2', 'f2', 'r1', 'r1', 'RL',
'RL', 'l1', 'd1', 'd1', 'l2', 'l2', 'd2', 'l1', 'b1', 'd1',
'd1', 'b2', 'r1','d1', 'r2', 'd1', 'b2', 'd2', 'b1', 'd1',
't2', 'd2', 't1', 'd1', 'd1', 'd1', 'l2', 'd2', 'l1', 'd2',
'b2', 'd1', 'b1', 'd1', 'l1', 'd2', 'l2', 'd1', 't1', 'd1',
't2', 'd2', 'l2', 'd2', 'l1', 'b1', 'd1', 'b2', 'd2', 'r2',
'd2', 'r1', 'r1', 'd1', 'r2', 'd2', 't2', 'd2', 't1', 'd1',
'd1', 't1', 'd2', 't2', 'd2', 'l2', 'd1', 'l1', 'd1', 'd2',
't2', 'd1', 't1', 'd1', 'r1', 'd2', 'r2', 'b1', 'd1', 'b2',
'd2', 'r2', 'd2', 'r1', 'd2', 'r2', 'd1', 'r1', 'd1', 'b1',
'd2', 'b2', 'RL', 'RL', 'f1', 'b1', 'r1', 'f1', 'r2', 'f2',
'b2', 't1', 'f2', 'b2', 'f1', 't2', 'f2', 'b1', 'f1', 't1',
'd1', 't2', 'd2', 't1', 'd1', 't2', 'd2', 't1', 'd1', 't2',
'd2', 't1', 'd1', 't2', 'd2', 'f1', 't1', 'd1', 't2', 'd2',
't1', 'd1', 't2', 'd2', 't1', 'd1', 't2', 'd2', 't1', 'd1',
't2', 'd2', 'f1', 'f1', 't1', 'd1', 't2', 'd2', 't1', 'd1',
't2', 'd2', 't1', 'd1', 't2', 'd2', 't1', 'd1', 't2', 'd2',
'f1', 'RL', 'RL']
```
## Things I Learnt
* Object Oriented Programming in python.
* Making a model to represent a complicated object in code.
* Use of the exec function in python.
* Implementing an algorithm used to solve a complicated puzzle in code.
