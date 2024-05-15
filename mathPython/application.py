import numpy as np

#TODO : extraction
A = np.linspace(1,2,5)
B = np.array([[1,2,3,4],[5,6,7,8],[9,1,0,2],[4,1,6,7]])
print (A)
print(f'shape of the matrix A:\n\t{A.shape}')
print(f'valeur 2 premier de A :\n\t{[A[0:2]]}')
print(f'valeur 3 premier de A :\n\t{[A[0:3]]}')
print('----------------------------------------\n\n')
print(f'matrix B:\n {B}')
print(f'extraction de B[0:3]\n {B[0:3]}\n')
print(f'extraction de B[0:3,0:3]\n {B[0:3,0:3]}\n')