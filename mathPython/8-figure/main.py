import numpy as np
import matplotlib.pyplot as plt

# TODO: preparer la figure
fig, ax = plt.subplots()

# TODO: preparer la fonction
x = np.linspace(-1, 1,200)
y = np.sin(x)

# TODO: dessigner y en fonction de x

ax.plot(x, y)

# TODO: afficher la figure

plt.show()