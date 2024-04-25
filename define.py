import os
from win32api import GetSystemMetrics

WINDOW_WIDTH            = 850
WINDOW_HEIGHT           = 490
WINDOW_POSITION_RIGHT   = int(GetSystemMetrics(0)/2 - WINDOW_WIDTH/2)
WINDOW_POSITION_DOWN    = int(GetSystemMetrics(1)/2 - WINDOW_HEIGHT/2)

COLOR_BLUE              = "#579CA7"
COLOR_BACKGROUND        = "#81AD4E"
COLOR_PINK              = "#FCE8E8"
COLOR_WHITE             = "#FFFAFA"
COLOR_ORANGE            = "#DE6723"
COLOR_YELLOW            = "#F5BB3C"

PATH_DIRECTORY      = os.path.dirname(__file__)
PATH_IMAGES         = os.path.join(PATH_DIRECTORY, 'images')

FONT_TEXT_SEARCH    = ('Roboto', 15,'bold')
FONT_LABEL_NAME     = ('Roboto', 15,'bold')
FONT_CITY           = ('Roboto', 19,'bold')
FONT_BUTTON_SEARCH  = ('Roboto', 10,'bold')
FONT_DAY_NAME       = ('Roboto', 35,'bold')
FONT_TEMP           = ('Roboto', 70,'bold')
FONT_INDEX          = ('Roboto', 30,'bold')


DEFAULT_CITY = "Ho Chi Minh"
