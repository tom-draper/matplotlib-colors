import matplotlib.pyplot as plt
from src.colors import colors
import matplotlib.colors as mcolors


# Colors maps
wld = mcolors.ListedColormap([colors['PL_LOSE'], colors['PL_DRAW'], colors['PL_WIN']])
premier_league = mcolors.ListedColormap([colors['PL_PINK'], colors['PL_BLUE'], colors['PL_GREEN']])
team = mcolors.ListedColormap([colors['OPPOSITION'], colors['CONTESTED'], colors['TEAM']])
analyst = mcolors.ListedColormap([colors['OPPOSITION'], colors['CONTESTED'], colors['TEAM']])


excluded_vars = {'colormaps', 'colors', 'plt', 'mcolors', 'excluded_vars', 'var', 'register_cmaps'}
colormaps = {var: eval(var) for var in dir() if not var.startswith('__') and var not in excluded_vars}
colormap_names = list(colormaps.keys())

def register_cmaps():
    for var, val in globals().items():
        if not var.startswith('__') and var not in excluded_vars:
            val.name = var
            plt.colormaps.register(val)
    print(plt.colormaps)
