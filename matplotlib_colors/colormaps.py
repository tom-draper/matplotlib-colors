import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib_colors.colors import colors


# Colors maps
wld = mcolors.ListedColormap([colors['PL_LOSE'], colors['PL_DRAW'], colors['PL_WIN']])
premier_league = mcolors.ListedColormap([colors['PL_PINK'], colors['PL_BLUE'], colors['PL_GREEN']])
team = mcolors.ListedColormap([colors['OPPOSITION'], colors['CONTESTED'], colors['TEAM']])
analyst = mcolors.ListedColormap([colors['OPPOSITION'], colors['CONTESTED'], colors['TEAM']])


excluded_vars = {'colormaps', 'colors', 'plt', 'mcolors', 'excluded_vars', 'var', 'cmap', 'register_cmaps'}

colormaps = {}
for var in dir():
    if not var.startswith('__') and var not in excluded_vars:
        cmap = eval(var)
        cmap.name = var  # Assign variable name as colormap name
        colormaps[var] = cmap
colormap_names = list(colormaps.keys())

def register_cmaps():
    for var, val in globals().items():
        if not var.startswith('__') and var not in excluded_vars:
            plt.colormaps.register(val)
