import matplotlib.pyplot as plt
import numpy as np
from colors import colors
from colormaps import colormaps


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [x * x for x in x]
norm = plt.Normalize(1, 150)

c = np.linspace(0, 80, 12)
plt.scatter(x, y, c=c, cmap='premier_league', norm=norm)
plt.colorbar()
plt.show()
