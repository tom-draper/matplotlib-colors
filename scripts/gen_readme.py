import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.insert(0, parent + '/matplotlib_colors')
from colors import colors, color_names
from colormaps import register_cmaps, colormap_names

import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.patches import Rectangle
import matplotlib.patches as mpatch

register_cmaps()


def title():
    return """# Showcase"""

def plot_colortable(path, sort_colors=True, emptycols=0):
    cell_width = 250
    cell_height = 22
    swatch_width = 48
    margin = 12

    # Sort colors by hue, saturation, value and name.
    if sort_colors is True:
        by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgb(color))), name)
                        for name, color in colors.items())
        names = [name for _, name in by_hsv]
    else:
        names = list(colors)

    ncols = 4 - emptycols
    nrows = len(names) // ncols + int(len(names) % ncols > 0)

    width = cell_width * 4 + 2 * margin
    height = cell_height * nrows + 2 * margin
    dpi = 72

    fig, ax = plt.subplots(figsize=(width / dpi, height / dpi), dpi=dpi)
    fig.subplots_adjust(margin/width, margin/height,
                        (width-margin)/width, (height-margin)/height)
    ax.set_xlim(0, cell_width * 4)
    ax.set_ylim(cell_height * (nrows-0.5), -cell_height/2.)
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    ax.set_axis_off()

    for i, name in enumerate(names):
        row = i % nrows
        col = i // nrows
        y = row * cell_height

        swatch_start_x = cell_width * col
        text_pos_x = cell_width * col + swatch_width + 7

        ax.text(text_pos_x, y, name, fontsize=13,
                horizontalalignment='left',
                verticalalignment='center')

        ax.add_patch(
            Rectangle(xy=(swatch_start_x, y-9), width=swatch_width,
                      height=18, facecolor=colors[name], edgecolor='0.7')
        )
    
    if path is not None:
        plt.savefig(path)

def plot_colors(path: str):
    fig = plt.figure(figsize=(9, 5))
    ax = fig.add_axes([0, 0, 1, 1])

    n_groups = 3
    n_rows = len(color_names) // n_groups + 1

    for j, color_name in enumerate(sorted(color_names)):
        color = colors[color_name]

        # Pick text colour based on perceived luminance.
        rgba = mcolors.to_rgba_array([color])
        luma = 0.299 * rgba[:, 0] + 0.587 * rgba[:, 1] + 0.114 * rgba[:, 2]
        text_color = 'k' if luma[0] > 0.5 else 'w'

        _hex = mcolors.rgb2hex(color)

        shift = 2
        col_shift = (j // n_rows) * shift
        y_pos = j % n_rows
        text_args = dict(fontsize=10)
        ax.add_patch(mpatch.Rectangle(
            (0 + col_shift, y_pos), 1, 1, color=color))
        ax.text(0.5 + col_shift, y_pos + .7, _hex,
                color=text_color, ha='center', **text_args)
        ax.text(1 + col_shift, y_pos + .7, f'  {color_name}', **text_args)

    for g in range(n_groups):
        ax.hlines(range(n_rows), shift*g, shift *
                  g + 2.8, color='0.7', linewidth=1)
        ax.text(0.5 + shift*g, -0.3, 'Color', ha='center')

    ax.set_xlim(0, 2 * n_groups)
    ax.set_ylim(n_rows, -1)
    ax.axis('off')

    if path is not None:
        plt.savefig(path)


def _colors():
    path = 'img/colors.png'
    plot_colortable(path)
    return f'## Colors\n\n<p align="center"><img src="../{path}"></p>'


def plot_cmaps(path: str):
    N_COLS = 4
    N_ROWS = math.ceil(len(colormap_names) / N_COLS)
    HEIGHT, WIDTH = N_ROWS, 9

    _, axes = plt.subplots(N_ROWS, N_COLS, figsize=(WIDTH, HEIGHT))

    idx = 0
    for row in range(N_ROWS):
        for col in range(N_COLS):
            ax = axes[row, col]
            if idx > len(colormap_names)-1:
                ax.get_xaxis().set_visible(False)
                ax.get_yaxis().set_visible(False)
                for spine in ['top', 'right', 'left', 'bottom']:
                    ax.spines[spine].set_visible(False)
            else:
                cmap_id = colormap_names[idx]
                mpl.colorbar.ColorbarBase(
                    ax, cmap=cmap_id, orientation='horizontal')
                ax.set_title(cmap_id, fontsize=9)
                ax.tick_params(left=False, right=False, labelleft=False,
                            labelbottom=False, bottom=False)

                if idx >= len(colormap_names) - 1:
                    plt.tight_layout()
            idx += 1

    if path is not None:
        plt.savefig(path)


def colormaps():
    path = 'img/colormaps.png'
    plot_cmaps(path)
    return f'## Colormaps\n\n<p align="center"><img src="../{path}"></p>'


def source():
    return """## Source\n\nA small portion of these color themes were sourced from color design websites, including <a href="https://coolors.co/">coolors.co</a> and <a href="https://www.canva.com/">canva.com</a>. Thanks!"""


def notice():
    return """---\n???? This file was autogenerated by `scripts/gen_readme.py`."""


def build_readme():
    readme = '\n\n'.join(
        [title(), _colors(),  colormaps(), source(), notice()])
    return readme


if __name__ == '__main__':
    readme = build_readme()
    with open('matplotlib_colors/README.md', 'w', encoding="utf-8") as f:
        f.write(readme)
