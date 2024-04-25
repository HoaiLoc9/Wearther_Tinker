from tkinter import Frame, Label
from define import *

class MyFrame(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self['pady']    = 50
        self['padx']    = 20

        self.grid(row=0)

class LabelName(Label):
    def __init__(self, *args, **kwargs):
        Label.__init__(self, *args, **kwargs)
        self['font']    = FONT_LABEL_NAME
        self['fg']      = COLOR_ORANGE
        self['bg']      = COLOR_PINK

class LabelIndex(Label):
    def __init__(self, *args, **kwargs):
        Label.__init__(self, *args, **kwargs)
        self['font']    = FONT_INDEX
        self['fg']      = COLOR_WHITE
        self['bg']      = COLOR_YELLOW
        self['width']   = 4
        self['height']  = 2
        self['text']    = 0
        
        self.grid(padx=20)

class LabelLeft(Label):
    def __init__(self, *args, **kwargs):
        Label.__init__(self, *args, **kwargs)
        self['fg']      = COLOR_WHITE
        self['bg']      = COLOR_BLUE