from email import message
import requests
from datetime import datetime, date
from define import DEFAULT_CITY
from tkinter import messagebox
from notify import *

def get_date(time_data, dayName):
    date_time_obj = datetime.strptime(time_data, '%Y-%m-%d %H:%M')
    weekday_name = date.weekday(date_time_obj)
    days = ['Thứ Hai', 'Thứ Ba', 'Thứ Tư', 'Thứ Năm', 'Thứ Sáu', 'Thứ Bảy', 'Chủ Nhật']
    dayName.config(text=days[weekday_name])

def get_weather(inputSearch, dayTemp, cityName, dayName, humidity, precip, wind_dir, wind_speed, visibility, uv_index):
    city = inputSearch.get() if len(inputSearch.get()) != 0 else DEFAULT_CITY

    params = {
        'access_key': '48acfc930cf3067c62fa96c8246b6fbd',
        'query': city
    }
    try:
        api_result = requests.get('http://api.weatherstack.com/current', params)
        api_response = api_result.json()

        get_date(api_response["location"]["localtime"], dayName)

        cityName.config(text=api_response["location"]["name"])
        dayTemp.config(text=str(api_response["current"]["temperature"]) + "°C")
        humidity.config(text=api_response["current"]["humidity"])
        precip.config(text=api_response["current"]["precip"])
        wind_dir.config(text=api_response["current"]["wind_dir"])
        wind_speed.config(text=api_response["current"]["wind_speed"])
        visibility.config(text=api_response["current"]["visibility"])
        uv_index.config(text=api_response["current"]["uv_index"])

    except:
        messagebox.showerror(NAME_ERROR_BOX, MESSAGE_ERROR_BOX)


    