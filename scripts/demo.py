import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib_colors import register_cmaps, colormap_names

register_cmaps()


def plot_cmaps():
    N_ROWS, N_COLS = 8, 4 # 13, 13 <-- for all in one figure 
    HEIGHT, WIDTH = 9, 16
            
    _, axes = plt.subplots(N_ROWS, N_COLS, figsize=(WIDTH, HEIGHT))
    
    idx = 0
    for row in range(N_ROWS):
        for col in range(N_COLS):
            ax = axes[row, col]
            cmap_id = colormap_names[idx]
            mpl.colorbar.ColorbarBase(ax, cmap=cmap_id, orientation='horizontal')
            ax.set_title(cmap_id, fontsize=8)
            ax.tick_params(left=False, right=False, labelleft=False, 
                           labelbottom=False, bottom=False)
            
            if idx >= len(colormap_names) - 1:
                plt.tight_layout()
                plt.show()
                return
            idx += 1

plot_cmaps()