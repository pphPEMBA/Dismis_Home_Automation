#!/usr/bin/python3
from GoogleCore import googleCalender #, googleMail
from Services import conversation, date_time, greeting, internet, jokes_quote, noteManually, notes, rhythmbox_client_Controller, weather, youtube
from SocialController import FBlogin, Gcreate_account, Glogin, twitterlogin
from SystemService import infoSender, systemTask, appManager, updateSystem, volumeController
import os
import subprocess


def cmd(voice_text, name, default_CityLocation, openweatherAPI, main_sender, main_passwd, slave_sender, slave_passwd, receiver, personalMail, personalPasswd, accept_path, else_path, Ctoken_pickle, Ccredentials, noteManually_txt, memory_db, DISMIS_HA_path, BestfriendBirthdayProtocal_path, PersonalGmailNotify_path,chromeDriver_linux ,chromeDriver_win ,chromeDriver_mac ,greetingMail, schedule_path, movieList_path, laughSound1, laughSound2, moviesDirectory, conversationTTS_path, date_timeTTS_path, greetingTTS_path, internetTTS_path, jokes_quoteTTS_path, noteManuallyTTS_path, notesTTS_path, rhythmbox_client_ControllerTTS_path, weatherTTS_path, youtubeTTS_path, FBloginTTS_path, Gcreate_accountTTS_path, GloginTTS_path, twitterloginTTS_path, AI_TTS_path, PrimaryCredentialsTTS_path, appManagerTTS_path, infoSenderTTS_path, systemTaskTTS_path, updateSystemTTS_path, volumeControllerTTS_path):
    def check_message(check):
        """
         This function checks if the items in the list (specified in
        argument) are present in the user's input speech.
         """
        words_of_message = voice_text.split()
        if set(check).issubset(set(words_of_message)):
            return True
        else:
            return False

    if check_message(['milestone']) or check_message(['What','milestone','life']):
        conversation.milestone(accept_path)
    elif check_message(['what', 'things','do']) or check_message(['what','can','do']):
        conversation.whatthingcando(slave_sender, slave_passwd, accept_path)
    elif check_message(['daddy\'s', 'home']) or check_message(['i', 'home']) or check_message(['daddys', 'home']):
        conversation.welcome(accept_path)
    elif check_message(['baby']) or check_message(['auntie']) or check_message(['aunty']) or check_message(['online']) or check_message(['buddy']):
        conversation.online(accept_path)
    elif check_message(['who', 'are', 'you']): #error
        conversation.who_are_you(accept_path)
    elif check_message(['how', 'i', 'look']) or check_message(['how', 'am', 'i']):
        conversation.how_am_i(accept_path)
    elif check_message(['where', 'born']): #error
        conversation.where_born(accept_path)
    elif check_message(['why','exist']) or check_message(['why','here']): #error
        conversation.why_born(accept_path)
    elif check_message(['how', 'you']):
        conversation.how_are_you(accept_path)
    elif check_message(['what', 'age']) or check_message(['what\'s', 'age']):
        conversation.how_old_are_you(accept_path)
    elif check_message(['who', 'master']) or check_message(['who','coded','you']):
        conversation.who_made(accept_path)
    elif check_message(['what', 'doing']):
        conversation.what_doing(accept_path)
    elif check_message(['say', 'her']) or check_message(['greet','her']) or check_message(['welcome','her']):
        conversation.greet_her(accept_path)
    elif check_message(['say', 'him']) or check_message(['greet','him']) or check_message(['welcome','him']):
        conversation.greet_him(accept_path)
    elif check_message(['say', 'them']) or check_message(['greet','them']) or check_message(['welcome','them']):
        conversation.greet_them(accept_path)
    elif check_message(['wait']) or check_message(['waiting','for']):
        conversation.wait(accept_path)
    elif check_message(['thank','you']):
        conversation.thank_you(accept_path)
    elif check_message(['love', 'you']):
        conversation.love_you(accept_path)
    elif check_message(['are', 'tired']):
        conversation.tired(accept_path)
    elif check_message(['are', 'smart']):
        conversation.smart(accept_path)
    elif check_message(['are', 'tall']):
        conversation.tall(accept_path)
    elif check_message(['which', 'eye', 'color']) or check_message(['which', 'eyes', 'color']):
        conversation.coloreye(accept_path)
    elif check_message(['do','believe', 'ghost']):
        conversation.believeghost(accept_path)
    elif check_message(['be','ghost']) or check_message(['behave','ghost']) or check_message(['scare','me']) or check_message(['scare','them']):
        conversation.ghost(accept_path)
    elif check_message(['just','wanted','say', 'hi']):
        conversation.wantedtosayi(accept_path)
    elif check_message(['you', 'are', 'welcome']) or check_message(['you\'re','welcome']):
        conversation.urwelcome(accept_path)
    elif check_message(['you','are','beautiful']):
        conversation.urbeautiful(accept_path)
    elif check_message(['you','are','hot']):
        conversation.urhot(accept_path)
    elif check_message(['am','i', 'hot']): #error
        conversation.amihot(accept_path)
    elif check_message(['am','i', 'cool']): #error
        conversation.amicool(accept_path)
    elif check_message(['am','i', 'good','person']):
        conversation.amigoodperson(accept_path)
    elif check_message(['what','do','think','me']): 
        conversation.whatyouthinkme(accept_path)
    elif check_message(['do','you','love','me']):
        conversation.douloveme(accept_path)
    elif check_message(['you','are','best']):
        conversation.urbest(accept_path)
    elif check_message(['i','like','talking', 'you']):
        conversation.iliketalkingwithu(accept_path)
    elif check_message(['shall','we','best', 'friend']) or check_message(['will','you','best', 'friend']):
        conversation.shallbebestfriend(accept_path)
    elif check_message(['tell','secret']):
        conversation.tellsecret(accept_path)
    elif check_message(['first','crush']):
        conversation.firstcrush(accept_path)
    elif check_message(['i' ,'transferring', 'you']) or check_message(['i' ,'transferring', 'dismiss']): #error
        conversation.transferingDismis(accept_path)
    elif check_message(['laugh']) or check_message(['can','laugh']):
        conversation.dismisLaugh(accept_path, laughSound1, laughSound2)
    elif check_message(['which', 'service','control', 'alert','1']) or check_message(['which', 'service','control', 'alert','one']):
        conversation.alert1(accept_path)
    elif check_message(['which', 'service','control', 'alert','2']) or check_message(['which', 'service','control', 'alert','two']):
        conversation.alert2(accept_path)
    elif check_message(['which', 'service','control', 'alert','3']) or check_message(['which', 'service','control', 'alert','three']):
        conversation.alert3(accept_path)
    elif check_message(['which', 'service','control', 'alert','4']) or check_message(['which', 'service','control', 'alert','four']):
        conversation.alert4(accept_path)

        

    elif check_message(['what','do', 'have']) or check_message(['what','do', 'have','plans']) or check_message(['whats','schedule']) or check_message(['what\'s','schedule'])\
        or check_message(['do','have','anything']) or check_message(['what','day','look']):
        googleCalender.main(voice_text, accept_path)


    elif check_message(['what','date']) or check_message(['whats','date']) or check_message(['tell', 'date']): #error
        date_time.date(accept_path)
    elif check_message(['what', 'time']) or check_message(['whats', 'time']) or check_message(['tell', 'time']): #error
        date_time.currenttime(accept_path)

    elif check_message(['good','morning']) or check_message(['good','afternoon']) or check_message(['good','evening']) or check_message(['good','night']):
        greeting.Greeting(accept_path)
    elif check_message(['i','going','out']):
        greeting.imgoingout(accept_path)
        
    elif check_message(['search', 'google']) or check_message(['on', 'google']):
        internet.google(voice_text, accept_path)
    elif check_message(['show', 'picture']) or check_message(['search', 'picture'])\
         or check_message(['show', 'pictures']) or check_message(['search', 'pictures']):
        internet.search_pics(voice_text, accept_path)
    elif check_message(['internet']):
        internet.askinternet(voice_text, accept_path)
    elif check_message(['open']):
        internet.open_website(voice_text, accept_path)
    elif check_message(['where','is']) or check_message(['show','me','location']) or check_message(['find', 'place', 'name']):
        internet.location(voice_text, accept_path)
    elif check_message(['what','net', 'speed']) or check_message(['whats', 'net', 'speed']):
        internet.netspeed(accept_path)
    elif check_message(['tell', 'joke']) or check_message(['jokes']):
        jokes_quote.tell_joke(accept_path)
    elif check_message(['tell','quote']) or check_message(['what','day','quote']) or check_message(['whats','day','quote']):
        jokes_quote.quote(accept_path)
    #elif check_message(['news']):
        #news.
    elif check_message(['write','something']):
        noteManually.note_manually(accept_path, noteManually_txt)
    elif check_message(['read','manually','written','notes']) or check_message(['read','manually','written','note']):
        noteManually.readNote_manually(accept_path, noteManually_txt)
    elif check_message(['note', 'something']) or check_message(['take', 'note']) or check_message(['note','down'])\
         or check_message(['write','something']):
        notes.note_something(voice_text, accept_path, memory_db)
    elif check_message(['show','note']) or check_message(['look', 'note']) or check_message(['see', 'note']):
        notes.show_all_notes(accept_path, memory_db)
    elif check_message(['play', 'song']) or check_message(['pause']) or check_message(['toggle','song']):
        rhythmbox_client_Controller.toggle(accept_path)
    elif check_message(['stop']):
        rhythmbox_client_Controller.stop(accept_path)
    elif check_message(['next']):
        rhythmbox_client_Controller.next(accept_path)
    elif check_message(['previous']):
        rhythmbox_client_Controller.previous(accept_path)
    elif check_message(['what','playing']):
        rhythmbox_client_Controller.printplaying(accept_path)
    elif check_message(['repeat']):
        rhythmbox_client_Controller.repeat(accept_path)
    elif check_message(['stop','repeat']):
        rhythmbox_client_Controller.norepeat(accept_path)
    elif check_message(['shuffle']):
        rhythmbox_client_Controller.shuffle(accept_path)
    elif check_message(['stop','shuffle']):
        rhythmbox_client_Controller.noshuffle(accept_path)
    elif check_message(['tell', 'weather']) or check_message(['give','details','weather']) or check_message(['whats','weather']) or check_message(['give','detail','weather']) :
        weather.weather_DefaultCity(default_CityLocation, openweatherAPI, accept_path)
    elif check_message(['how', 'weather','in']) or check_message(['whats','weather']):
        weather.weather(openweatherAPI, accept_path)
    elif check_message(['youtube','play']) or check_message(['make','youtube','play']) or check_message(['tell','youtube','play']):
        youtube.playFirstVid(voice_text, accept_path)
    elif check_message(['youtube','search']) or check_message(['make','youtube','search']) or check_message(['tell','youtube','search']):
        youtube.searchVid(voice_text, accept_path)
        
    
    elif check_message(['login','facebook']) or check_message(['open','facebook']):
        FBlogin.login(accept_path, chromeDriver_linux)
    #elif check_message(['send','mail']) or check_message(['compose','mail']) or check_message(['create','gmail','enviroment']):
        #Gcompose.compose(accept_path)
    elif check_message(['create','gmail']) or check_message(['create', 'random','account']):
        Gcreate_account.createRandomAc(accept_path, chromeDriver_linux)
    elif check_message(['login','gmail']) or check_message(['open','personal','gmail']) or check_message(['show','my','mails']):
        Glogin.PersonalMail(accept_path, chromeDriver_linux) 
    elif check_message(['login','youtube','gmail']) or check_message(['open','youtube','gmail']) or check_message(['show','youtube','mails']):
        Glogin.YoutubeMail(accept_path, chromeDriver_linux) 
    elif check_message(['login','twitter']) or check_message(['open', 'twitter','account']):
        twitterlogin.login(accept_path, chromeDriver_linux)

   
    elif check_message(['send','details' ,'citizenship']) or check_message(['send','detail' ,'citizenship'])\
         or check_message(['give','details' ,'citizenship']) or check_message(['give','detail' ,'citizenship'])\
         or check_message(['provide','details' ,'citizenship']) or check_message(['provide','detail' ,'citizenship']):
        infoSender.citizenshipInfo(main_sender, main_passwd, receiver, accept_path)
    elif check_message(['send','folder','lock', 'password']) or check_message(['give','folder','lock', 'password'])\
         or check_message(['provide','folder','lock','password']):
        infoSender.folderlockpassInfo(main_sender, main_passwd, receiver, accept_path)
    elif check_message(['send','details','other', 'internet']) or check_message(['send','detail','other', 'internet'])\
         or check_message(['give','details','other', 'internet']) or check_message(['give','detail','other', 'internet'])\
         or check_message(['provide','details','other', 'internet']) or check_message(['provide','detail','other', 'internet']):
        infoSender.internetAccInfo(main_sender, main_passwd, receiver, accept_path)
    elif check_message(['send','others','gmail']) or check_message(['send','other','gmail'])\
         or check_message(['give','others','gmail']) or check_message(['give','other','gmail'])\
         or check_message(['provide','others','gmail']) or check_message(['provide','other','gmail']):
        infoSender.othersGmailInfo(main_sender, main_passwd, receiver, accept_path)
    elif check_message(['send', 'password','gmail']) or check_message(['send','code','gmail'])\
         or check_message(['give', 'password','gmail']) or check_message(['give','code','gmail'])\
         or check_message(['provide', 'password','gmail']) or check_message(['provide','code','gmail']):
        infoSender.PasswordGmailInfo(main_sender, main_passwd, receiver, accept_path)
    elif check_message(['send', 'details', 'payeer']) or check_message(['send', 'detail', 'payeer'])\
         or check_message(['give', 'details', 'payeer']) or check_message(['give', 'detail', 'payeer'])\
         or check_message(['provide', 'details', 'payeer']) or check_message(['provide', 'detail', 'payeer']):
        infoSender.payeerInfo(main_sender, main_passwd, receiver, accept_path)
    elif check_message(['send','details', 'payoneer', 'account']) or check_message(['send','detail', 'payoneer', 'account'])\
         or check_message(['give','details', 'payoneer', 'account']) or check_message(['give','detail', 'payoneer', 'account'])\
         or check_message(['provide','details', 'payoneer', 'account']) or check_message(['provide','detail', 'payoneer', 'account']):
        infoSender.payoneerInfo(main_sender, main_passwd, receiver, accept_path)
    elif check_message(['send','code','personal','gmail']) or check_message(['send','password','personal','gmail'])\
         or check_message(['send','codes','personal','gmail'])\
         or check_message(['give','code','personal','gmail']) or check_message(['give','password','personal','gmail'])\
         or check_message(['give','codes','personal','gmail'])\
         or check_message(['provide','code','personal','gmail']) or check_message(['provide','password','personal','gmail'])\
         or check_message(['provide','codes','personal','gmail']):
        infoSender.backupGmailCodeInfo(main_sender, main_passwd, receiver, accept_path)
    elif check_message(['send','details','personal','gmail']) or check_message(['send','detail','personal','gmail'])\
         or check_message(['give','details','personal','gmail']) or check_message(['give','detail','personal','gmail'])\
         or check_message(['provide','details','personal','gmail']) or check_message(['provide','detail','personal','gmail']):
        infoSender.personalGmailInfo(main_sender, main_passwd, receiver, accept_path)
    elif check_message(['send', 'details', 'twillio']) or check_message(['send', 'details', 'twillio'])\
         or check_message(['give', 'details', 'twillio']) or check_message(['give', 'details', 'twillio'])\
         or check_message(['provide', 'details', 'twillio']) or check_message(['provide', 'details', 'twillio']):
        infoSender.twillioinfo(main_sender, main_passwd, receiver, accept_path)


    elif check_message(['screen', 'off']):
        systemTask.screen_off__LINUX(accept_path)
    elif check_message(['display', 'information', 'operating','system']) or check_message(['details', 'system']):
        systemTask.Os__LINUX(accept_path)
    elif check_message(['shutdown','system']):
        systemTask.shutdown_LINUX(accept_path)
    elif check_message(['reboot','system']):
        systemTask.reboot_LINUX(accept_path)
    elif check_message(['hibernate','system']):
        systemTask.hibernate_LINUX(accept_path)
    elif check_message(['hybrid', 'sleep','system']):
        systemTask.hybridsleep_LINUX(accept_path)
    elif check_message(['suspend','system']):
        systemTask.suspend_LINUX(accept_path)

    elif check_message(['update','system']):
        updateSystem.update_system(accept_path)

    elif check_message(['close','chrome']) or check_message(['close','browser']) or check_message(['terminate','chrome']):
        appManager.chromeClose(accept_path)
    elif check_message(['launch','chrome']) or check_message(['launch','browser']):
        appManager.chromeOpen(accept_path)
    elif check_message(['close','code']) or check_message(['close','visual','studio']) or check_message(['terminate','visual','studio']): #it works but currently not using
        appManager.codeClose(accept_path)
    elif check_message(['launch','code']) or check_message(['launch','visual','studio']): #it works but currently not using
        appManager.codeOpen(accept_path)
    elif check_message(['close','files']) or check_message(['close','file']) or check_message(['terminate','files']) or check_message(['terminate','file']):
        appManager.filesClose(accept_path)
    elif check_message(['launch','files']) or check_message(['launch','file']):
        appManager.filesOpen(accept_path)
    elif check_message(['close','firefox']) or check_message(['terminate','firefox']):
        appManager.firefoxClose(accept_path)
    elif check_message(['launch','firefox']):
        appManager.firefoxOpen(accept_path)
    elif check_message(['close','terminal']) or check_message(['terminate','terminal']):
        appManager.terminalClose(accept_path) 
    elif check_message(['launch','terminal']):
        appManager.terminalOpen(accept_path) 

    elif check_message(['volume', '100', 'percent']) or check_message(['volume', 'hundred', 'percent'])\
        or check_message(['volume', '100']) or check_message(['volume', 'hundred']) or check_message(['volume','100%']):
        volumeController.volume100__Linux(accept_path)
    elif check_message(['volume', '90', 'percent']) or check_message(['volume', 'ninety', 'percent'])\
        or check_message(['volume', '90']) or check_message(['volume', 'ninety']) or check_message(['volume','90%']):
        volumeController.volume90__Linux(accept_path)
    elif check_message(['volume', '80', 'percent']) or check_message(['volume', 'eighty', 'percent'])\
        or check_message(['volume', '80']) or check_message(['volume', 'eighty']) or check_message(['volume','80%']):
        volumeController.volume80__Linux(accept_path)
    elif check_message(['volume', '70', 'percent']) or check_message(['volume', 'seventy', 'percent'])\
        or check_message(['volume', '70']) or check_message(['volume', 'seventy']) or check_message(['volume','70%']):
        volumeController.volume70__Linux(accept_path)
    elif check_message(['volume', '60', 'percent']) or check_message(['volume', 'sixty', 'percent'])\
        or check_message(['volume', '60']) or check_message(['volume', 'sixty']) or check_message(['volume','60%']):
        volumeController.volume60__Linux(accept_path)
    elif check_message(['volume', '50', 'percent']) or check_message(['volume', 'fifty', 'percent'])\
        or check_message(['volume', '50']) or check_message(['volume', 'fifty']) or check_message(['volume','50%']):
        volumeController.volume50__Linux(accept_path)
    elif check_message(['volume', '40', 'percent']) or check_message(['volume', 'fourty', 'percent'])\
        or check_message(['volume', '40']) or check_message(['volume', 'fourty']) or check_message(['volume','40%']):
        volumeController.volume40__Linux(accept_path)
    elif check_message(['volume', '30', 'percent']) or check_message(['volume', 'thirty', 'percent'])\
        or check_message(['volume', '30']) or check_message(['volume', 'thirty']) or check_message(['volume','30%']):
        volumeController.volume30__Linux(accept_path)
    elif check_message(['volume', '20', 'percent']) or check_message(['volume', 'twenty', 'percent'])\
        or check_message(['volume', '20']) or check_message(['volume', 'twenty']) or check_message(['volume','20%']):
        volumeController.volume20__Linux(accept_path)
    elif check_message(['volume', '10', 'percent']) or check_message(['volume', 'ten', 'percent'])\
        or  check_message(['volume', '10']) or check_message(['volume', 'ten']) or check_message(['volume','10%']):
        volumeController.volume10__Linux(accept_path)
    elif check_message(['volume', 'mute']) or check_message(['volume', '0', 'percent'])\
        or check_message(['volume', 'zero', 'percent'])\
        or check_message(['volume', 'mute']) or check_message(['volume', '0'])\
        or check_message(['volume', 'zero']) or check_message(['volume','0%']):
        volumeController.volumeMute__Linux(accept_path)
    #elif check_message(['what','current','volume']): #not working
        #volumeController.getCurrentVol__linux(accept_path)
    else:
        os.system('mpg123 /home/d-slave1/.Dismis-HA_slave1/SystemService/sound/else.mp3')
        #""" Ping google.com """ 
        #from urllib.request import urlopen
        #try:
        #    response = urlopen('https://www.google.com/', timeout=10)
        #    print('--- ONLINE! ---')
        #    # run() returns a CompletedProcess object if it was successful
        #    # errors in the created process are raised here too
        #    process = subprocess.run('perl SystemService/currentVol_perl.pl 0', shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
        #    PrevVolLevel = process.stdout
        #    print("***\nThe Previous Volume Level is: " + PrevVolLevel + "***")
        #    print(' ')
        #    d = open('PrevVolLevel.txt','w+')
        #    d.write(PrevVolLevel)
        #    d.close()
        #    os.system("pactl -- set-sink-volume 0 30%")
        #    os.system('mpg123 /home/d-slave1/.Dismis-HA_slave1/SystemService/sound/else.mp3')
        #    with open('PrevVolLevel.txt','r') as f:
        #        PrevVolLevel_txt = f.read()
        #        os.system("pactl -- set-sink-volume 0 " + str(PrevVolLevel_txt))
        #        os.system('rm PrevVolLevel.txt &')
        #except: 
        #    print("--- OFFLINE! ---")
        #    #os.system("pactl -- set-sink-volume 0 30%")
        #    os.system('mpg123 /home/d-slave1/.Dismis-HA_slave1/SystemService/sound/else.mp3')
        #    print(' ')

    
