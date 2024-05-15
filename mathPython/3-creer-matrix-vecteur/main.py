"""
TODO : learn matix and vector in math
    ! zeros : 0
    ! pour avoir le transpose : matrix.T, ex : A.T
    ! eye = I
    ? np.eye(l,c) si l == c, matrix rectangles
    ! linspace(1,2,8)  start end, number of pts
    ! (np.diag(xDiag,n)) pour cette matrix diag. on peut specifier la position du diag,avec n de Z entier
        default diag : center 0
        +------------+
        |  0 1 2 3 4 |
        | -1         |
        | -2         |
        | -3         |
        | -4         |
        +------------+
    ! ce quoi un matrix diag ? il faut de matrx carre, 
"""
import numpy as np
A = np.zeros(4)         #! vecteur de taille 4, [0,0,0,0]
B = np.zeros([7,2])     #! matrix (l,c) taille default value : 0
C = np.ones([5,2])      #! matrix (l,c) taille default value : 1
D = np.ones(2)          #! vector
I = np.eye(7,7)         #! matrix eye : I : identity matrix
J = np.eye(5)           #! matrix identity ito no tsara aminazy

# TODO: 2
a1 = np.linspace(1,2,8) #! on veur de 8pts reel dans [1,2]
x1 = np.arange(0,1,0.1) #! on veur de valeur dans [0,1[ pas (raison) = 0.1
xDiag = np.arange(0,1,0.2)
#print(f"{xDiag}\n")
x2 = np.diag(xDiag)    #! matrix diagonale that, the diagonal is the vector x2
#print(np.diag(xDiag))

# TODO: 3
x3 = np.diag(3*np.ones(3)) + np.diag(2*np.ones(2),-1) + np.diag(4*np.ones(2),1)
print(x3)