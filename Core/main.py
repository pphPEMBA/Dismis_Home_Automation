#!/usr/bin/python3
from pyfiglet import Figlet
import yaml, random
import sys
import os
import datetime
import time
from multiprocessing import Process, Queue

from SpeechDriver.tts.ttsdefault import speak
from Services import weather, jokes_quote
from . import textAnimation

""" Importing profile.py path """
from Core.profile import profile_path
profile = open(profile_path)
profile_data = yaml.safe_load(profile)
profile.close()
#Functioning Variables
name = profile_data['name']
default_CityLocation = profile_data['default_CityLocation']
openweatherAPI = profile_data['openweatherAPI']
main_sender = profile_data['main_sender']
main_passwd = profile_data['main_passwd']
slave_sender = profile_data['slave_sender']
slave_passwd = profile_data['slave_passwd']
receiver = profile_data['receiver']
personalMail = profile_data['personalMail']
personalPasswd = profile_data['personalPasswd']
accept_path = profile_data['accept_path']
else_path = profile_data['else_path']   #not using
Ctoken_pickle = profile_data['Ctoken_pickle'] 
Ccredentials = profile_data['Ccredentials'] 
noteManually_txt = profile_data['noteManually_txt'] 
memory_db = profile_data['memory_db']
DISMIS_HA_path = profile_data['DISMIS_HA_path']
BestfriendBirthdayProtocal_path = profile_data['BestfriendBirthdayProtocal_path']
PersonalGmailNotify_path = profile_data['PersonalGmailNotify_path']
flask_credentials_path = profile_data['flask_credentials_path']
Dismis_HA_wholesystemlog = profile_data['Dismis_HA_wholesystemlog'] # using in DISMIS-HA
exit_Dismis_HA_log = profile_data['exit_Dismis_HA_log'] # using in DISMIS-HA
initialize_Dismis_HA_log = profile_data['initialize_Dismis_HA_log'] # using in DISMIS-HA
voice_recognitionlog = profile_data['voice_recognitionlog'] # using in googleDefault
BestfriendBirthday_date = profile_data['BestfriendBirthday_date'] # using in BestfriendBirthdayProtocal
host_ip= profile_data['host_ip'] # using in PrimaryCredentials.flaskServer & in infosender
chromeDriver_linux = profile_data['chromeDriver_linux']
chromeDriver_win = profile_data['chromeDriver_win']
chromeDriver_mac = profile_data['chromeDriver_mac']
greetingMail = profile_data['greetingMail']
schedule_path = profile_data['schedule_path'] #using in schedule.py
movieList_path = profile_data['movieList_path'] #NOTUSING
moviesDirectory = profile_data['moviesDirectory'] #NOTUSING
laughSound1 = profile_data['laughSound1']
laughSound2 = profile_data['laughSound2']
conversationTTS_path = profile_data['conversationTTS_path']
date_timeTTS_path = profile_data['date_timeTTS_path']
greetingTTS_path = profile_data['greetingTTS_path']
internetTTS_path = profile_data['internetTTS_path']
jokes_quoteTTS_path = profile_data['jokes_quoteTTS_path']
noteManuallyTTS_path = profile_data['noteManuallyTTS_path']
notesTTS_path = profile_data['notesTTS_path']
rhythmbox_client_ControllerTTS_path  = profile_data['rhythmbox_client_ControllerTTS_path']
weatherTTS_path = profile_data['weatherTTS_path']
youtubeTTS_path = profile_data['youtubeTTS_path']
FBloginTTS_path = profile_data['FBloginTTS_path']
Gcreate_accountTTS_path = profile_data['Gcreate_accountTTS_path']
GloginTTS_path = profile_data['GloginTTS_path']
twitterloginTTS_path = profile_data['twitterloginTTS_path']
AI_TTS_path = profile_data['AI_TTS_path']
PrimaryCredentialsTTS_path = profile_data['PrimaryCredentialsTTS_path']
#tts_pico2wave_wav = profile_data['tts_pico2wave_wav']
#tts_main_wav = profile_data['tts_main_wav']
#tts_BestfriendBirthdayALERT_wav = profile_data['tts_BestfriendBirthdayALERT_wav']


#access_token = profile_data['twitter']['access_token']
#access_token_secret = profile_data['twitter']['access_token_secret']
#consumer_key = profile_data['twitter']['consumer_key']
#consumer_secret = profile_data['twitter']['consumer_secret']

"""
print("                                            ")
print("  ________  .__               .__           ")
print("  \______ \ |__| ______ _____ |__| ______   ")
print("   |    |  \|  |/  ___//     \|  |/  ___/   ")
print("   |    `   \  |\___ \|  Y Y  \  |\___ \    ")
print("  /_______  /__/____  >__|_|  /__/____  >   ")
print("          \/        \/      \/        \/    ")
print("                                            ")   """


""" Ping google.com """ #Current not using in main instead using in brain.
from urllib.request import urlopen
def internetExamine():
    while True:
        try:
            response = urlopen('https://www.google.com/', timeout=10)
            print('on')
            return True
        except: 
            print('false')
            return False


""" Greeting """
def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')
    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')
    if currentH >= 18 and currentH != 0:
        speak('Good Evening!')

""" MULTIPROCESSING """
def BestfriendBirthdayProtocal(BestfriendBirthdayProtocal_path):
    time.sleep(random.randint(1, 3))
    os.system("python3 " + BestfriendBirthdayProtocal_path + " &")
def PersonalGmailNotify(PersonalGmailNotify_path):
    time.sleep(random.randint(1, 3))
    os.system("python3 " + PersonalGmailNotify_path + " &")
def flask_credentials(flask_credentials_path):
    time.sleep(random.randint(1, 3))
    os.system("python3 " + flask_credentials_path + "&")
def schedule(schedule_path):
    time.sleep(random.randint(1, 3))
    os.system("python3 " + schedule_path + "&")

""" Desktop Notification """
"""
from gi.repository import Notify
# One time initialization of libnotify
Notify.init("Dismis-HA_slave1")
# Create the notification object
title = "Dismis-HA_slave1!"
body = "Meeting at 3PM!"
notification = Notify.Notification.new(
    title, body)
# Actually show on screen
notification.show() """
      

""" Booting """
def startup():
    """ Start Up """
    textAnimation.load_animation()
    time.sleep(0.30)
    print(' ')
    
    """ Dismis Banner """
    custom_fig = Figlet(font='graffiti')
    print(custom_fig.renderText('Dismis-HA'))
    
    """ Greeting """
    greetMe()
    #time.sleep(0.30)
    
    """ Weather of Default Location """
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        weather.weather_DefaultCity(default_CityLocation, openweatherAPI, accept_path)
        #time.sleep(0.30)
    
    """ Jokes """
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        jokes_quote.tell_joke(accept_path)
        #time.sleep(0.30)
    
    """ Quote of The Day """
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        jokes_quote.quote(accept_path)
        #time.sleep(0.30)



""" Running All Main Functions """
#startup()
time.sleep(1)
online = (['Now the Dismis system is fully online', 'I\'m ready to go','I have been activited fully'])
speak(random.choice(online))
""" Running Parallel Processes """
#chkMail = Process(target = PersonalGmailNotify(PersonalGmailNotify_path))
#chkMail.start()
#bffbirthday = Process(target = BestfriendBirthdayProtocal(BestfriendBirthdayProtocal_path))
#bffbirthday.start()
#credentials = Process(target = flask_credentials(flask_credentials_path))
#credentials.start()
#routine = Process(target = schedule(schedule_path))
#routine.start()
# if __name__ == '__main__':
    # while True:


