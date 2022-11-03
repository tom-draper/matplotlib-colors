import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib_colors.colors import colors


# Colors maps
win_lose_draw = mcolors.ListedColormap([colors['PL_LOSE'], colors['PL_DRAW'], colors['PL_WIN']])
premier_league = mcolors.ListedColormap([colors['PL_PINK'], colors['PL_BLUE'], colors['PL_GREEN']])
team = mcolors.ListedColormap([colors['OPPOSITION'], colors['CONTESTED'], colors['TEAM']])
analyst = mcolors.ListedColormap([colors['ANALYST_RED'], colors['ANALYST_WHITE'], colors['ANALYST_BLUE']])
vibrant = mcolors.ListedColormap([colors['DUKE_BLUE'], colors['JAZZBERRY_JAM'], colors['RADICAL_RED'], colors['ORANGE_PANTONE'], colors['AMBER']])
asteroid = mcolors.ListedColormap([colors['RICH_BLACK_FOGRA_29'], colors['BLUE_SAPPHIRE'], colors['VIRIDIAN_GREEN'], colors['MIDDLE_BLUE_GREEN'], colors['MEDIUM_CHAMPAGNE'], colors['GAMBOGE'], colors['ALLOY_ORANGE'], colors['RUST'], colors['RUFOUS'], colors['RUBY_RED']])
steel = mcolors.ListedColormap([colors['RICH_BLACK_FOGRA_29'], colors['OXFORD_BLUE'], colors['BDAZZLED_BLUE'], colors['SHADOW_BLUE'], colors['PLATINUM']])
vibrant2 = mcolors.ListedColormap([colors['FLICKR_PINK'], colors['PURPLE'], colors['TRYPAN_BLUE'], colors['ULTRAMARINE_BLUE'], colors['VIVID_SKY_BLUE']])


excluded_vars = {'colormaps', 'colors', 'plt', 'mcolors', 'excluded_vars', 
                 'colormap_names', 'color_names', 'var', 'cmap', 'register_cmaps'}

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
            