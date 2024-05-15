import numpy as np

"""
    ! il faut comprendre la notion de la poiteur
"""
a = 2
b = 3

print(f'a = {a} b = {b}\n')
tmp = a
a =b
b = tmp
print(f'a = {a} b = {b}\n')

M = np.array([[1,2],[3,4]])

print(f'on a la matrix M :\n{M}')
print(f'M[0] :==> {M[0,:]}')
print(f'M[1] :==> {M[1,:]}')

# !tmp = M[0,:]
# !print(tmp)
# !M[0,:] = M[1,:]
# !M[1,:] = tmp
# !print(tmp)
tmp = np.copy(M[0,:])
M[0,:] = M[1,:]
M[1,:] = tmp
print(tmp)
print(f'on a la matrix M :\n{M}')
print(f'M[0] :==> {M[0,:]}')
print(f'M[1] :==> {M[1,:]}')