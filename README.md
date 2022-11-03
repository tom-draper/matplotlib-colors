# Matplotlib Colors

A collection of curated colors and colormaps for matplotlib.

## Examples

### Colormaps

All new color maps can be added to matplotlib simply by calling the `register_cmaps` function. The desired colormap can be specified by name with the cmap argument.

```py
from matplotlib_colors import register_cmaps

register_cmaps()  # Adds new colourmaps to matplotlib


# Build your data viz as normal with matplotlib...
import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [x * x for x in x]
c = np.linspace(0, 100, 12)  # Where each point lands on the colour scale
plt.scatter(x, y, c=c, cmap='analyst')  # Specify a new color name from matplotlib_colors
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
c = np.linspace(0, 100, 12)  # Where each point lands on the colour scale
plt.scatter(x, y, c=c, cmap=colormaps['analyst'])  # Specify a new color name from matplotlib_colors
plt.colorbar()
plt.show()
```

The full list of colormaps is available through the `color_names` list.

```py
from matplotlib_colors import colormap_names
print(colormap_names)
```

### Colors

The package includes a large selection of colors that can be accessed directly by importing `colors` and specifying a color name.

```py
import matplotlib.pyplot as plt
from matplotlib_colors import colors

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [x * x for x in x]

plt.scatter(x, y, c=colors['PL_RED'])
plt.colorbar()
plt.show()
```

The full list of color names is available through the `color_names` list.

```py
from matplotlib_colors import color_names
print(color_names)
```

