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

CELL_FILL_CHAR = '▩'
BOARD_LINING_CHAR = '.'
LINE_CLEAR_CHAR = '▒'

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

# COLOR_GROUPS_REF = ['REDS', 'ORANGES', 'YELLOWS', 'LIGHT-GREENS', 'GREENS', 'LIGHT-BLUES', 'BLUES', 'DARK-BLUES', 'PURPLES', 'PINKS', 'MONOCHROMES']

COLOR_GROUPS = [
    ['#f78b8b', "#cc4444", '#871818'],
    ['#e3aa71', '#f5902c', "#a75401"],
    ['#f2e299', '#f5d33b', '#997f0e'],
    ['#dbf086', '#c4ed1f', '#6d8707'],
    ['#88f27e', '#41ed32', '#0f6307'],
    ['#83f2cd', '#16c78c', "#198f68"],
    ['#7fd2f5', '#2bb3ed', '#105978'],
    ["#85aaee", '#3673e3', '#153c85'],
    ["#ba94ee", '#721ee8', '#380d75'],
    ['#e07bcb', '#f02bc5', '#8a0c6f'],
    ['#eeeeee', '#777777', '#222222']
]

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