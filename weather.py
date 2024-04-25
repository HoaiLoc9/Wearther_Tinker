from tkinter import *
from define import *
from app import App
from my_function import *
from my_class import *

window = Tk()
app = App(window)

#Create Frame
frameWeather = Frame(window, bg=COLOR_PINK)
frameWeather.grid(column=0, row=0)

frameLeft = MyFrame(frameWeather, bg=COLOR_BLUE)
frameLeft.grid(column=0)

frameRight = MyFrame(frameWeather, bg=COLOR_PINK)
frameRight.grid(column=1)

#FrameLeft
frameSearch = Frame(frameLeft, bg=COLOR_BLUE)
frameSearch.pack(side=TOP)

inputSearch = Entry(frameSearch, font=FONT_TEXT_SEARCH, width=13, relief=FLAT)
inputSearch.pack(side=LEFT)

buttonSearch = Button(frameSearch, text="Tìm kiếm", bg=COLOR_ORANGE, fg=COLOR_WHITE, 
    font=FONT_BUTTON_SEARCH, width=10, relief=FLAT, 
    command=lambda:get_weather(inputSearch, dayTemp, cityName, dayName, humidity, precip, wind_dir, wind_speed, visibility, uv_index))

buttonSearch.pack(side=RIGHT)

cityName = LabelLeft(frameLeft, text=DEFAULT_CITY, font=FONT_CITY)
cityName.pack(pady=(20, 30))

dayName = LabelLeft(frameLeft, text="Thứ năm", font=FONT_DAY_NAME)
dayName.pack(pady=(0, 20))

dayTemp = LabelLeft(frameLeft, text="25°C", font=FONT_TEMP)
dayTemp.pack()

#FrameRight
humidity = LabelIndex(frameRight)
humidity.grid(column=0, row=0)
precip = LabelIndex(frameRight)
precip.grid(column=1, row=0)
wind_dir = LabelIndex(frameRight)
wind_dir.grid(column=2, row=0)

wind_speed = LabelIndex(frameRight)
wind_speed.grid(column=0, row=2)
visibility = LabelIndex(frameRight)
visibility.grid(column=1, row=2)
uv_index = LabelIndex(frameRight)
uv_index.grid(column=2, row=2)

def createLabelRow1(text, col):
    LabelName(frameRight, text=text).grid(column=col, row=1, pady=(10,30))

def createLabelRow3(text, col):
    LabelName(frameRight, text=text).grid(column=col, row=3, pady=(10,0))

createLabelRow1("Độ ẩm",     0)
createLabelRow1("Lượng mưa", 1)
createLabelRow1("Hướng gió", 2)

createLabelRow3("Tốc độ gió", 0)
createLabelRow3("Tầm nhìn",   1)
createLabelRow3("Chỉ số UV",  2)

get_weather(inputSearch, dayTemp, cityName, dayName, humidity, precip, wind_dir, wind_speed, visibility, uv_index)

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

window.mainloop()