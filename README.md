# Matplotlib Colors

A collection of curated colors and colormaps for matplotlib.

<p align="center">
	<img src="https://user-images.githubusercontent.com/41476809/199964030-433c8b4d-f191-47d3-ba23-7a30f41bc8fd.png">
</p>

## Installation

```bash
pip install matplotlib-colors
```

## Demo

[All colors and colormaps](matplotlib_colors/README.md)

## Examples

### Colormaps

Call the `register_cmaps` function to add the new colormaps to matplotlib. Then the desired colormap can be specified by name as the `cmap` argument.

```py
from matplotlib_colors import register_cmaps
register_cmaps()  # Adds new colormaps to matplotlib

# Build your data viz as normal with matplotlib
import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [x * x for x in x]
plt.scatter(x, y, c=range(12), cmap='analyst')  # Specify one of the new colormap names
plt.colorbar()
plt.show()
```

Alternatively, all new colormap objects can be accessed directly by importing the `colormaps` dict and specifying a colormap by name.

```py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib_colors import colormaps

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [x * x for x in x]
plt.scatter(x, y, c=range(12), cmap=colormaps['analyst'])  # Specify a colormap from colormaps dict
plt.colorbar()
plt.show()
```

The full list of colormap names can be found by importing the `colormap_names` list.

```py
from matplotlib_colors import colormap_names
```

### Colors

The package includes a large selection of colors that can be accessed directly by importing `colors` and specifying a color name.

```py
import matplotlib.pyplot as plt
from matplotlib_colors import colors

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [x * x for x in x]
plt.scatter(x, y, c=colors['PL_RED'])  # All points colored with PL_RED
plt.colorbar()
plt.show()
```

The full list of color names can be found by importing the `color_names` list.

```py
from matplotlib_colors import color_names
```

