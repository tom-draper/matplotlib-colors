
if __name__ == '__main__':
    import numpy as np
    import matplotlib.pyplot as plt
    from src import colormaps
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    y = [x * x for x in x]
    c = np.linspace(0, 100, 12)  # Where each point lands on the colour scale
    plt.scatter(x, y, c=c, cmap=colormaps['analyst'])  # Specify a new color name from matplotlib_colors
    plt.colorbar()
    plt.show()