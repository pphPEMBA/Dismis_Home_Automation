#!/usr/bin/python3
import requests
import os
import time

#from tkinter import *

from SpeechDriver.tts.ttsdefault import speak


""" GLOBAL FUNCTION """
def Log_Time():
    import datetime
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

""" Importing Profiles """
import yaml
from Core.profile import profile_path
profile = open(profile_path)
profile_data = yaml.safe_load(profile)
profile.close()
#Functioning Variables
weatherTTS_path = profile_data['weatherTTS_path']
weatherTTS = weatherTTS_path + '/SpeechDriver/tts/ServicesTTS/weatherTTS/'
#print(weatherTTS)


def weather_DefaultCity(default_CityLocation, openweatherAPI, accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    #city_name= "kakarbhitta"
    speak('Extracting weather')
    #weather1 = Tk()
    #weather1.geometry('1150x300+120+0')
    #weather1.title("Dismis's Weather")
    api_key = openweatherAPI
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + default_CityLocation 
    json_data=requests.get(complete_url).json()
    try:
        temp=json_data['main']
        temp=str(int(int(temp['temp'])-273.15))
        temp1=json_data['weather'][0]['description']
        wind_speed =json_data['wind']['speed']
        d =" Current Temperature in "+default_CityLocation+" is "+temp+" degree celsius with "+temp1+ " and " + 'Wind Speed is {} metre per second'.format(wind_speed)
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print("city you said is",default_CityLocation)
        print(d)
        print(' ')
        print(' ')
        print('\t\t\t\tSkill: weather_DefaultCity')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        result = d
        #Label(weather1 , padx = 3000, pady = 3000, compound=CENTER, text=result, bg="#171717", fg = "white", font='times 15 bold').pack()
        #speak(d)
        #weather1.after(5000, lambda: weather1.destroy())
        #weather1.mainloop()
        weather_txt = open('weather.txt','w+')
        weather_txt.write(result)
        os.system('gnome-terminal -x python3 ' + weatherTTS + 'weather_DefaultCity__tts.py &')
        print(' ')
    except KeyError:
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        print("Key invalid or city not found")
        print(' ')
        print(' ')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        result = "Key invalid or city not found"
        #weatherlabel22 = Label(weather1 , padx = 3000, pady = 3000, compound=CENTER, text=result, bg="#171717", fg = "white", font='times 15 bold').pack()
        #speak("key invalid or city not found")
        #weather1.after(5000, lambda: weather1.destroy())
        #weather1.mainloop()   
        weather_txt = open('weather.txt','w+')
        weather_txt.write(result)
        os.system('gnome-terminal -x python3 ' + weatherTTS + 'weather_DefaultCity__tts.py &')
        print(' ')

def weather(openweatherAPI, accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    city_name=input("enter city name to confirm:  ")
    speak('Extracting weather')
    #weather2 = Tk()
    #weather2.geometry('1150x300+120+0')
    #weather2.title("Dismis's Weather")
    ##speak("city you said is",city_name) #print ra speak lakda chaldana
    api_key = openweatherAPI
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
    json_data=requests.get(complete_url).json()
    try:
        temp=json_data['main']
        temp=str(int(int(temp['temp'])-273.15))
        temp1=json_data['weather'][0]['description']
        wind_speed =json_data['wind']['speed']
        weather = json_data['weather'] [0] ['main'] 
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print("city you said is",city_name)
        d =" Current Temperature in "+city_name+" is "+temp+" degree celsius with "+temp1+ " and " + 'Wind Speed is {} metre per second'.format(wind_speed)
        print(d)
        print(' ')
        print(' ')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        result = d
        #Label(weather2 , padx = 3000, pady = 3000, compound=CENTER, text=result, bg="#171717", fg = "white", font='times 15 bold').pack()
        #speak(d)
        #weather2.after(5000, lambda: weather2.destroy())
        #weather2.mainloop()
        weather2_txt = open('weather2.txt','w+')
        weather2_txt.write(result)
        os.system('gnome-terminal -x python3 ' + weatherTTS + 'weather__tts.py &')
        print(' ')
    except KeyError:
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        print("Key invalid or city not found")
        print(' ')
        print(' ')
        print('\t\t\t\tSkill: weather')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        result = "Key invalid or city not found" 
        #Label(weather2 , padx = 3000, pady = 3000, compound=CENTER, text=result, bg="#171717", fg = "white", font='times 15 bold').pack()
        #speak("key invalid or city not found")
        #weather2.after(5000, lambda: weather2.destroy())
        #weather2.mainloop()
        weather2_txt = open('weather2.txt','w+')
        weather2_txt.write(result)
        os.system('gnome-terminal -x python3 ' + weatherTTS + 'weather__tts.py &')

#cca979ed5fb2c8d3a9c99594191482f9
