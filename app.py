from define import *
import os

class App():
    def __init__(self, window) -> None:
        # Thiết lập Width Height Position
        # .geometry("window width x window height + position right + position down")
        
        # Gets both half the screen width/height and window width/height
        window.geometry("{}x{}+{}+{}".format(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_POSITION_RIGHT, WINDOW_POSITION_DOWN))
        window.resizable(False, False)
        
        # Title
        window.title("Weather")

        # Icon
        window.iconbitmap(os.path.join(PATH_IMAGES, 'icon.ico'))

        # Background
        window['background']= COLOR_BACKGROUND

        # window.resizable(False, False) 
        window.minsize(400, 100)