import numpy as np
#! 1
V =  np.array([5,8,9,8,6])
V = np.arange(1,14,2) # TODO (start, end, pas)
for val in V:
    print(f'val = {val}')
print('fin du boucle\n\n')

#! 2
fruits = ['apple', 'orange','mangue','potato','banana']
for fruit in fruits:
    print(f'fruit = {fruit}')