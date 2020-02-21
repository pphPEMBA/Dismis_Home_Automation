#!/usr/bin/python3
import datetime
import time
import os

#from tkinter import *

from SpeechDriver.tts.ttsdefault import speak


""" Importing Profiles """
import yaml
from Core.profile import profile_path
profile = open(profile_path)
profile_data = yaml.safe_load(profile)
profile.close()
#Functioning Variables
date_timeTTS_path = profile_data['date_timeTTS_path']
date_timeTTS = date_timeTTS_path + '/SpeechDriver/tts/ServicesTTS/date_timeTTS_path/'
#print(date_timeTTS)

""" GLOBAL FUNCTION """
def Log_Time():
    import datetime
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))


def date(accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    #root = Tk()
    #root.geometry('1150x300+120+0')
    #root.title("Dismis's Date")
    currentdate = datetime.datetime.now()
    result = currentdate.strftime("%d %b %Y %A")
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: date')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    #Label(root, padx = 3000, pady = 3000, compound=CENTER, text=result, bg="#171717", fg = "white", font='times 15 bold').pack()
    #root.after(2800, lambda: root.destroy())
     #root.mainloop()
    speak(result)
    date_txt = open('date.txt','w+')
    date_txt.write(result)
    os.system('gnome-terminal -x python3 ' + date_timeTTS + 'date__tts.py &')

def currenttime(accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    #root = Tk()
    #root.geometry('1150x300+120+0')
    #root.title("Dismis's Time")
    Hours = datetime.datetime.now().strftime('%H')
    Hours = int(Hours) % 12
    Minutes = datetime.datetime.now().strftime('%M')
    Seconds = datetime.datetime.now().strftime('%S')
    currentT = (str(Hours) + ' hours ' + str(Minutes) + ' minutes ' + str(Seconds) + ' seconds ')
    result = currentT
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: currenttime')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    speak(result)
    #Label(root, padx = 3000, pady = 3000, compound=CENTER, text=result, bg="#171717", fg = "white", font='roots 15 bold').pack()
    #root.after(2800, lambda: root.destroy())
    #root.mainloop()
    currenttime_txt = open('currenttime.txt','w+')
    currenttime_txt.write(result)
    os.system('gnome-terminal -x python3 ' + date_timeTTS + 'currenttime__tts.py &')

