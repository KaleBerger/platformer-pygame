TITLE = "Platformer"
WIDTH = 480
HEIGHT = 600
FPS = 60
FONT_NAME = 'times new roman'
HS_FILE = "highscore.txt"
SPRITESHEET = "spritesheet_jumper.png"

#player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 22

#Game Properties
BOOST_POWER = 60
POW_SPAWN_PCT = 7
MOB_FREQ = 5000
PLAYER_LAYER = 2
PLATFORM_LAYER = 1
POW_LAYER = 1
MOB_LAYER = 2
CLOUD_LAYER = 0
#Starting Platfroms
PLATFORM_LIST = [(0, HEIGHT - 60),
                (WIDTH / 2 - 50, HEIGHT * 3/4),
                (350, 200),
                (175, 100)] 

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (85, 26, 139)
BGCOLOR = PURPLE
