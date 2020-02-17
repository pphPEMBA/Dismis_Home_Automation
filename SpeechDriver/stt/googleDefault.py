#!/usr/bin/python3
import speech_recognition as sr
import datetime, socket
from os import system

from Core.main import *
from Core.brainstem import cmd

""" GLOBAL FUNCTION """
def Log_Time():
    import datetime
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

speech = sr.Recognizer()
def read_voice_cmd():
    voice_text = ''
    print(datetime.datetime.now().ctime() + '  Listening...')
    try:
        with sr.Microphone() as source:
            #speech.energy_threshold = 4000
            #speech.adjust_for_ambient_noise(source)
            audio = speech.listen(source=source, timeout=10, phrase_time_limit=5)
        voice_text = speech.recognize_google(audio).lower().replace("'", "")
        print(' ')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print('**************************************************************************************************************************************************************************************')
        Log_Time()
        print("DISMIS thinks you said '" + voice_text + "'")
        print('**************************************************************************************************************************************************************************************')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        try:
            """ Notification of what Dismis had listen """
            from gi.repository import Notify
            # One time initialization of libnotify
            Notify.init("Dismis-HA_slave1")
            # Create the notification object
            title = "Dismis-HA_slave1"
            body = "DISMIS thinks you said '" + voice_text + "'"
            notification = Notify.Notification.new(title,body)
            # Actually show on screen
            notification.show()
        except:
            pass
        """ Write voice recognize log """
        d=open(voice_recognitionlog,'a+')
        d.write(datetime.datetime.now().ctime())
        d.write (" DISMIS thinks you said '" + voice_text + "'" + "\n")
    except sr.UnknownValueError:
        #pass
        listen = read_voice_cmd()
        return listen
        #voice_text = str(input('Command: '))
    except sr.WaitTimeoutError:
        pass
    except sr.RequestError as e:
        print('//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        print('Network error')
        print('//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
    except ConnectionResetError:
        pass
    else:
        time.sleep(0.45)
        # Close notification immediately
        notification.close()
    cmd(voice_text, name, default_CityLocation, openweatherAPI, main_sender, main_passwd, slave_sender, slave_passwd, receiver, personalMail, personalPasswd, accept_path, else_path, Ctoken_pickle, Ccredentials, noteManually_txt, memory_db, DISMIS_HA_path, BestfriendBirthdayProtocal_path, PersonalGmailNotify_path,chromeDriver_linux ,chromeDriver_win ,chromeDriver_mac, greetingMail, schedule_path, movieList_path,  laughSound1, laughSound2, moviesDirectory, conversationTTS_path, date_timeTTS_path, greetingTTS_path, internetTTS_path, jokes_quoteTTS_path, noteManuallyTTS_path, notesTTS_path, rhythmbox_client_ControllerTTS_path, weatherTTS_path, youtubeTTS_path, FBloginTTS_path, Gcreate_accountTTS_path, GloginTTS_path, twitterloginTTS_path, AI_TTS_path, PrimaryCredentialsTTS_path, appManagerTTS_path, infoSenderTTS_path, systemTaskTTS_path, updateSystemTTS_path, volumeControllerTTS_path)




