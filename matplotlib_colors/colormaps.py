import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib_colors.colors import colors


# Colors maps
win_lose_draw = mcolors.ListedColormap([
    colors['pl_lose'], colors['pl_draw'], colors['pl_win']])
premier_league = mcolors.ListedColormap([
    colors['pl_pink'], colors['pl_blue'], colors['pl_green']])
team = mcolors.ListedColormap([
    colors['opposition'], colors['contested'], colors['team']])
analyst = mcolors.ListedColormap([
    colors['analyst_red'], colors['analyst_white'], colors['analyst_blue']])
vibrant = mcolors.ListedColormap([
    colors['duke_blue'], colors['jazzberry_jam'], colors['radical_red'], 
    colors['orange_pantone'], colors['amber']])
asteroid = mcolors.ListedColormap([
    colors['rich_black_fogra_29'], colors['blue_sapphire'], colors['viridian_green'], 
    colors['middle_blue_green'], colors['medium_champagne'], colors['gamboge'], 
    colors['alloy_orange'], colors['rust'], colors['rufous'], colors['ruby_red']])
steel = mcolors.ListedColormap([
    colors['rich_black_fogra_29'], colors['oxford_blue'], colors['bdazzled_blue'], 
    colors['shadow_blue'], colors['platinum']])
vibrant2 = mcolors.ListedColormap([
    colors['flickr_pink'], colors['purple'], colors['trypan_blue'], 
    colors['ultramarine_blue'], colors['vivid_sky_blue']])


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
            