#!/usr/bin/python3
from selenium import webdriver
import wikipedia
import wolframalpha
import re
import webbrowser
import os
import time

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
internetTTS_path = profile_data['internetTTS_path']
internetTTS = internetTTS_path + '/SpeechDriver/tts/ServicesTTS/internetTTS/'
#print(internetTTS)

#search google
def google(voice_text, accept_path):
    os.system('aplay ' + accept_path +' &')
    
    webbrowser.open('https://www.google.com/search?q={}'.format(voice_text))
    result = 'opening sir' + voice_text + 'in google search'
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: google')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    google_txt = open('google.txt','w+')
    google_txt.write(result)
    os.system('gnome-terminal -x python3 ' + internetTTS + '__tts.py &')
    print(' ')


def search_pics(voice_text, accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(0.28)
    #voice_text = input('name of picture: ')
    url = "https://www.google.com/search?tbm=isch&q={}".format(
        voice_text.replace("of", ""))
    webbrowser.open(url)
    result = 'show in the pictures of' + voice_text
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('show in the pictures of' + voice_text)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: search_pics')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    _txt = open('.txt','w+')
    _txt.write(result)
    os.system('gnome-terminal -x python3 ' + internetTTS + '__tts.py &')
    print(' ')

def askinternet(voice_text, accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    reg_ex = re.search('internet(.+)', voice_text)
    if reg_ex:
        domain = reg_ex.group(1)
        result = 'extracting your query'
        try:
            app_id = "Q6Y3UQ-6T4J3423V7"
            client = wolframalpha.Client(app_id)
            res = client.query(domain)
            answer = next(res.results).text
            print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            print(' ')
            print(' ')
            Log_Time()
            print(answer + '> Function: askinternet extract from wolframalpha')
            print(' ')
            print(' ')
            print('\t\t\t\tSkill: askinternet')
            print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            result = answer
            askinternet_txt = open('askinternet.txt','w+')
            askinternet_txt.write(result)
            os.system('gnome-terminal -x python3 ' + internetTTS + 'askinternet__tts.py &')
            print(' ')
        except:
            print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            print(' ')
            print(' ')
            Log_Time()
            print(wikipedia.summary(domain, sentences=2) + '> Function: askinternet extract from wolframalpha')
            print(' ')
            print(' ')
            print('\t\t\t\tSkill: askinternet')
            print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            result = wikipedia.summary(domain, sentences=2)
            askinternet_txt = open('askinternet.txt','w+')
            askinternet_txt.write(result)
            os.system('gnome-terminal -x python3 ' + internetTTS + 'askinternet__tts.py &')
            print(' ')
        else:
            print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            print(' ')
            print(' ')
            Log_Time()
            print("Does not match any pages or query. Say again!")
            print(' ')
            print(' ')
            print('\t\t\t\tSkill: askinternet')
            print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            result = "Does not match any pages or query. Say again!"
            askinternet_txt = open('askinternet.txt','w+')
            askinternet_txt.write(result)
            os.system('gnome-terminal -x python3 ' + internetTTS + 'askinternet__tts.py &')
            print(' ')
                


def open_website(voice_text, accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    reg_ex = re.search('open (.+)', voice_text)
    if reg_ex:
        domain = reg_ex.group(1)
        result = 'aye aye captain'
        url = 'https://www.' + domain + '.com'
        webbrowser.open(url)
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print('user: ' + voice_text + '\n opening > Function: open_website')
        print(' ')
        print(' ')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        result = 'Openned sir' + voice_text
        open_website_txt = open('open_website.txt','w+')
        open_website_txt.write(result)
        os.system('gnome-terminal -x python3 ' + internetTTS + 'open_website__tts.py &')
        print(' ')
    else:
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print('try again')
        print(' ')
        print(' ')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        result = 'try again'
        open_website_txt = open('open_website.txt','w+')
        open_website_txt.write(result)
        os.system('gnome-terminal -x python3 ' + internetTTS + 'open_website__tts.py &')
        print(' ')


def location(voice_text, accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    data = voice_text.split(" ")
    location = ""
    location = location.split(" ")
    for i in range(2, len(data)):
        location.append(data[i])
    str1 = "  ".join(location)
    result = "Hold on sir, I will show you where " + str1 + " is."
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('Hold on sir, I will show you where' + str1 + 'is > Function: location')
    print(' ')
    print(' ')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    webbrowser.open("https://www.google.nl/maps/place/" + str1)
    location_txt = open('location.txt','w+')
    location_txt.write(result)
    os.system('gnome-terminal -x python3 ' + internetTTS + 'location__tts.py &')
    print(' ')


def netspeed(accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    url = 'http://speedtest.googlefiber.net/'
    webbrowser.open(url)
    result = 'checking net speed > Function: netspeed'
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    netspeed_txt = open('netspeed.txt','w+')
    netspeed_txt.write(result)
    os.system('gnome-terminal -x python3 ' + internetTTS + 'netspeed__tts.py &')
    print(' ')
