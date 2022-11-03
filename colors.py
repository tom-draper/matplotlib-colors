
# RGB values
TEAM = [120, 211, 242]
OPPOSITION = [220, 58, 68]
CONTESTED = [211, 211, 211]

PL_WIN = [19, 205, 0]
PL_DRAW = [117, 117, 110]
PL_LOSE = [216, 25, 32]

PL_PURPLE = [55, 0, 60]
PL_GREEN = [0, 255, 135]
PL_BLUE = [2, 238, 255]
PL_PINK = [255, 40, 130]
PL_RED = [233, 0, 82]

ANALYST_RED = [224, 86, 95]
ANALYST_PURPLE = [121, 70, 205]
ANALYST_WHITE = [247, 247, 247]
ANALYST_PURPLE = [29, 10, 48]


colors = {var: list(map(lambda x: x/255, eval(var))) 
          for var in dir() 
          if not var.startswith('__')}
