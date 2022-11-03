
if __name__ == '__main__':
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib_colors import register_cmaps, colormaps
    
    register_cmaps()
    
    print(colormaps['premier_league'])
    
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    y = [x * x for x in x]
    plt.scatter(x, y, c=range(12), cmap='vibrant')  # Specify a new color name from matplotlib_colors
    
    print(plt.get_cmap('binary'))
    print(plt.get_cmap('premier_league'))

    plt.colorbar()
    plt.show()
    
    