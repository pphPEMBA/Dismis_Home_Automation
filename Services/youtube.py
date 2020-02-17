#!/usr/bin/python3
import os
import webbrowser
import requests
from bs4 import BeautifulSoup
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
youtubeTTS_path = profile_data['youtubeTTS_path']
youtubeTTS = youtubeTTS_path + '/SpeechDriver/tts/ServicesTTS/youtubeTTS/'
#print(youtubeTTS)


def playFirstVid(voice_text, accept_path):
    os.system('play ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    try:
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
        time.sleep(1)
        query=voice_text
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print(voice_text + "function: playFirstVid")
        print(' ')
        print(' ')
        print('\t\t\t\tSkill: playFirstVid')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        query=query.replace(' ','+')
        url='https://www.youtube.com/results?search_query='+query
        source_code = requests.get(url, headers=headers, timeout=15)
        plain_text=source_code.text
        soup=BeautifulSoup(plain_text,"html.parser")
        songs=soup.findAll('div',{'class':'yt-lockup-video'})
        song=songs[0].contents[0].contents[0].contents[0]
        link=song['href']
        webbrowser.open('https://www.youtube.com'+link)
        result = query
        playFirstVid_txt = open('.txt','w+')
        playFirstVid_txt.write(result)
        os.system('gnome-terminal -x python3 ' + youtubeTTS + 'playFristVid__tts.py &')
        print(' ')

    except:
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print('Facing error PEMBA, please say again.')
        print(' ')
        print(' ')
        print('\t\t\t\tSkill: playFirstVid')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        result = 'Facing error PEMBA, please say again.'
        playFirstVid_txt = open('.txt','w+')
        playFirstVid_txt.write(result)
        os.system('gnome-terminal -x python3 ' + youtubeTTS + 'playFristVid__tts.py &')
        print(' ')
        
def searchVid(voice_text, accept_path):
    os.system('play ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(voice_text + "searching youtube")
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: searchVid')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    # Searches a youtube video
    search_phrase = voice_text.replace("youtube", "").replace("search", "").replace(" ", "+")
    webbrowser.open('https://www.youtube.com/results?search_query=' + search_phrase)
    result = search_phrase + 'on youtube'
    searchVid_txt = open('searchVid.txt','w+')
    searchVid_txt.write(result)
    os.system('gnome-terminal -x python3 ' + youtubeTTS + 'searchVid__tts.py &')
    print(' ')


"""
#Author:karim shoair (D4Vinci)
#Downloading youtube videos as mp4 and as mp3
import os,sys

try:
	Type = sys.argv[1]
	url  = sys.argv[2]
except:
	print("Error missing arguments!")
	print("yt.py (mp3/mp4) <url>")
	sys.exit(0)

if Type.lower()=="mp3":
	os.system("youtube-dl --exec 'ffmpeg -i {} -vn -ab 128k -ar 44100 -y {}.mp3' --extract-audio "+url)
elif Type.lower()=="mp4":
	os.system("youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' "+url)
else:
	print("Error unsupported format!")
"""