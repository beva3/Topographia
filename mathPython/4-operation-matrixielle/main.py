"""
    ! en python il faut faire attention pour le produit matricielle
        ! il y a une produit par coeff,
        ! il le produit matricielle loi mathematics
            TODO : np.matmul(A,B) <=> A.B
            TODO : np.linalg.matrix_power(A,n) <=> A.A ... A
    ! le produit matrixielle n'est pas commucatif
    ! pour le matrix invers, il y a des condition pour qu'une matrix soit inversible
    ! B*inv(B) = I
    ! on peut faire l'extraction du matrice 
    ?   shape taille
"""
import numpy as np

#TODO: data
A = np.array([[1,2,3],
             [4,5,6],
             [7,8,9]])

B = np.array([[-1,0,2],
             [5,0,-4],
             [8,-7,0]])

print(f'{A}\n')
print(f'{B}\n')
print(f'taille de la matrix : A : {A.shape}\n')

#TODO : classic
# print(f'somme de  A & B:\n{A+B}\n')
# print(f'produit coeff par coeff de A & B:\n{A*B}\n')
# print(f'produit coeff par coeff de B & A:\n{B*A}\n')
# print(f'produit matricielle  de A par B:\n{np.matmul(A,B)}\n')
# print(f'produit matricielle  de B par A:\n{np.matmul(B,A)}\n')

#TODO: vaovao amiko
print(f'np.matmul(A,A)\n{np.matmul(A,A)}\n')
print(f'np.linalg.matrix_power(A,2)\n{np.linalg.matrix_power(A,2)}\n')
print(f'invers de A\n{np.linalg.inv(B)}')
print(f'B * inv (B)\n{np.matmul(np.linalg.inv(B),B)}')
print(f'Transpose de  : B * inv (B)\n{np.matmul(np.linalg.inv(B),B).T}')

#TODO: matrix randomization
C = np.random.rand(4,4)
print(f'matrix random\n{C}\n')

#TODO: extract matrix
print(f'extract matrix\n{B[0:2,0:2]}\n') #TODO 0:2 <=> [0,2[