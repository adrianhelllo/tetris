BOARD_WIDTH = 10
BOARD_HEIGHT = 20

ROTATE_BIND = 'r'
RIGHT_BIND = 'd'
LEFT_BIND = 'a'
DOWN_BIND = 's'

TICK_RATE = 0.01

SOFT_DROP_INTERVAL = TICK_RATE * 5
BASE_DROP_INTERVAL = 48 # frames / row
FAST_DROP_INTERVAL = 6 # frames / row


SOFT_DROP_VALUE = 1 # / cell held down on
LINE_CLEAR_VALUES = [40, 100, 300, 1200]

INFO_SHORTHANDS = ['LINES', 'NXT', 'LVL', 'PTS']

PIECES = {
    'I': [[1, 1, 1, 1]],

    'O': [[1, 1],
          [1, 1]],

    'S': [[0, 1, 1],
          [1, 1, 0]],

    'Z': [[1, 1, 0],
          [0, 1, 1]],

    'L': [[1, 0],
          [1, 0],
          [1, 1]],

    'J': [[0, 1],
          [0, 1],
          [1, 1]],

    'T': [[1, 1, 1],
          [0, 1, 0]]
}

LARGEST_PIECE_WIDTH = max(len(row) for piece in PIECES.values() for row in piece)

RESET = '\033[0m'

COLORS = {
    'I' : '\033[91m',  # red
    'O' : '\033[92m',  # green
    'S' : '\033[93m',  # yellow
    'Z' : '\033[94m',  # blue
    'L' : '\033[95m',  # magenta
    'J' : '\033[96m',  # cyan
    'T': '\033[33m'  # orange-ish
}

GAME_OVER_MESSAGE = r"""
 $$$$$$\                                           $$$$$$\                                 
$$  __$$\                                         $$  __$$\                                
$$ /  \__| $$$$$$\  $$$$$$\$$$$\   $$$$$$\        $$ /  $$ |$$\    $$\  $$$$$$\   $$$$$$\  
$$ |$$$$\  \____$$\ $$  _$$  _$$\ $$  __$$\       $$ |  $$ |\$$\  $$  |$$  __$$\ $$  __$$\ 
$$ |\_$$ | $$$$$$$ |$$ / $$ / $$ |$$$$$$$$ |      $$ |  $$ | \$$\$$  / $$$$$$$$ |$$ |  \__|
$$ |  $$ |$$  __$$ |$$ | $$ | $$ |$$   ____|      $$ |  $$ |  \$$$  /  $$   ____|$$ |      
\$$$$$$  |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$\        $$$$$$  |   \$  /   \$$$$$$$\ $$ |      
 \______/  \_______|\__| \__| \__| \_______|       \______/     \_/     \_______|\__|      
"""