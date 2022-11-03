from colors import colors
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt


# Colors maps
wld = mcolors.ListedColormap([colors['PL_LOSE'], colors['PL_DRAW'], colors['PL_WIN']])
premier_league = mcolors.ListedColormap([colors['PL_PINK'], colors['PL_BLUE'], colors['PL_GREEN']])
team = mcolors.ListedColormap([colors['OPPOSITION'], colors['CONTESTED'], colors['TEAM']])
analyst = mcolors.ListedColormap([colors['OPPOSITION'], colors['CONTESTED'], colors['TEAM']])


excluded_vars = {'colormaps', 'colors', 'plt', 'mcolors', 'excluded_vars', 'var', 'register_cmaps'}
colormaps = {var: eval(var) for var in dir() if not var.startswith('__') and var not in excluded_vars}

def register_cmaps():
    for var, val in globals().items():
        if not var.startswith('__') and var not in excluded_vars:
            val.name = var
            print(var, val)
            plt.colormaps.register(val)
