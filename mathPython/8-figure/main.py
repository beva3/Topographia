import numpy as np
import matplotlib.pyplot as plt

# TODO: preparer la figure
fig, ax = plt.subplots()

# TODO: preparer la fonction
x = np.linspace(-5, 5,200)  #TODO: creat table value of x : [-5 , 5]
y = np.sin(x)

# TODO: dessigner y en fonction de x

ax.plot(x, y)
# TODO: afficher la figure

plt.show()