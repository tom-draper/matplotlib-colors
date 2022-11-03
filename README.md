# Matplotlib Colors

A collection of curated colors and colormaps for matplotlib.

![final](https://user-images.githubusercontent.com/41476809/199849510-071eea79-ff5e-4324-b7f0-5ae8d502aa01.jpg)


## Installation

```bash
python3 -m pip install matplotlib-colors
```

## Examples

### Colormaps

New colormaps can be added to matplotlib by calling the `register_cmaps` function. Then the desired colormap can be specified by name as the `cmap` argument.

```py
from matplotlib_colors import register_cmaps

register_cmaps()  # Adds new colormaps to matplotlib


# Build your data viz as normal with matplotlib...
import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [x * x for x in x]
plt.scatter(x, y, c=range(12), cmap='analyst')  # Specify a new color name from matplotlib_colors
plt.colorbar()
plt.show()
```

Alternatively, new colormap objects can be accessed directly by importing `colormaps` and specifying a colormap by name.

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

The full list of colormaps can be found by `color_names` list.

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

