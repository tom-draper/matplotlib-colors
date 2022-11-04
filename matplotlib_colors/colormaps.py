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
forest = mcolors.ListedColormap([
    colors['timberwolf'], colors['laurel_green'], colors['fern_green'], 
    colors['hunter_green'], colors['brunswick_green']])
energy = mcolors.ListedColormap([
    colors['xiketic'], colors['dark_sienna'], colors['rosewood'], colors['dark_red'], 
    colors['rosso_corsa'], colors['vermilion'], colors['persimmon'], colors['tangerine'], 
    colors['orange_web'], colors['selective_yellow']])
turquoise = mcolors.ListedColormap(
    [colors['nyanza'], colors['turquoise_green'], colors['turquoise_green'],
     colors['ocean_green'], colors['mint'], colors['illuminating_emerald'],
     colors['bottle_green'], colors['msu_green'], colors['dark_jungle_green']])
noir = mcolors.ListedColormap(
    [colors['cultured'], colors['cultured'], colors['gainsboro'], colors['light_gray'],
     colors['cadet_blue_crayola'], colors['sonic_silver'], colors['davys_grey'],
     colors['onyx'], colors['eerie_black']])
red_blue = mcolors.ListedColormap(
    [colors['amaranth_purple'], colors['jazzberry_jam'], colors['amaranth_m_p'],
     colors['byzantium'], colors['cyber_grape'], colors['bdazzled_blue'],
     colors['cg_blue'], colors['cg_blue'], colors['blue_munsell']])
orange_purple = mcolors.ListedColormap(
    [colors['safety_orange_blaze_orange'], colors['safety_orange'], colors['orange'],
     colors['yellow_orange_color_wheel'], colors['orange_peel'], colors['russian_violet'],
     colors['persian_indigo'], colors['purple'], colors['french_violet'], colors['amethyst']])
space_cadet = mcolors.ListedColormap(
    [colors['space_cadet'], colors['manatee'], colors['cultured'],
     colors['imperial_red'], colors['crimson']])
astro = mcolors.ListedColormap(
    [colors['flickr_pink'], colors['byzantine'], colors['purple'], colors['purple_2'], 
     colors['trypan_blue'], colors['trypan_blue_2'], colors['persian_blue'], 
     colors['ultramarine_blue'], colors['dodger_blue'], colors['vivid_sky_blue']])
skin = mcolors.ListedColormap(
    [colors['antique_white'], colors['peach_puff'], colors['gold_crayola'],
     colors['tan_crayola'], colors['camel'], colors['cafe_au_lait'],
     colors['coyote_brown'], colors['sepia'], colors['pullman_brown_ups_brown'],
     colors['pullman_brown_ups_brown_2']])
purples = mcolors.ListedColormap(
    [colors['russian_violet_2'], colors['russian_violet'], colors['persian_indigo'],
     colors['purple'], colors['french_violet'], colors['amethyst'], colors['heliotrope'],
     colors['mauve']])
green_blue = mcolors.ListedColormap(
    [colors['yellow_green_crayola'], colors['yellow_green_crayola'],
     colors['granny_smith_apple'], colors['ocean_green'], colors['keppel'],
     colors['viridian_green'], colors['blue_munsell'], colors['cg_blue'],
     colors['lapis_lazuli'], colors['yale_blue']])


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
            