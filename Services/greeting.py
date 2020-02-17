import os 
import time, datetime
import smtplib
import random
import requests
import feedparser
from pyfiglet import Figlet
import json
import socket
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

from Core.main import *

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
slave_sender = profile_data['slave_sender']
slave_passwd = profile_data['slave_passwd']
receiver = profile_data['receiver']
greetingTTS_path = profile_data['greetingTTS_path']
greetingTTS = greetingTTS_path + '/SpeechDriver/tts/ServicesTTS/greetingTTS/'
#print(greetingTTS)

    


""" GREETING SKILL """
def banner(greetingMail):
    custom_fig = Figlet(font='graffiti')
    poster = custom_fig.renderText('Dismis-HA')
    #print(custom_fig.renderText('Dismis-HA'))
    d=open(greetingMail,'a+')
    d.write("\n" + poster)
def extractTime(greetingMail):
    import datetime
    now = str(datetime.datetime.now())
    d=open(greetingMail, "a+")
    d.write("\n Extracted time is: " + now + "\n ----------------------------------------------------------------------------------------- \n ----------------------------------------------------------------------------------------- \n")

def Jokes():
    res = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
    if res.status_code == requests.codes.ok:
        return str(res.json()["joke"])
def in_Dismis():
    jokes = [
        'What happens to a frogs car when it breaks down? It gets toad away.',
        'Why was six scared of seven? Because seven ate nine.',
        'Why are mountains so funny? Because they are hill areas.',
        'Have you ever tried to eat a clock?'
        'I hear it is very time consuming.',
        'What happened when the wheel was invented? A revolution.',
        'What do you call a fake noodle? An impasta!',
        'Did you hear about that new broom? It is sweeping the nation!',
        'What is heavy forward but not backward? Ton.',
        'No, I always forget the punch line.',
        'It’s hard to explain puns to kleptomaniacs because they always take things literally.',
        'A soldier survived mustard gas in battle, and then pepper spray by the police. He\'s now a seasoned veteran.'
        'What\'s the best thing about Switzerland? I don\'t know, but their flag is a huge plus.',
        'A Buddhist walks up to a hotdog stand and says, Make me one with everything.',
        'What\'s the difference between my ex and the titanic? The titanic only went down on 1,000 people.',
        'Two fish are sitting in a tank. One looks over at the other and says: Hey, do you know how to drive this thing?',
        'I told my doctor that I broke my arm in two places. He told me to stop going to those places.',
        'How do you keep an idiot in suspense?',
        'I hate Russian dolls...they\'re so full of themselves.',
        'My granddad has the heart of a lion and a lifetime ban from the San Diego Zoo.',
        'Rick Astley will let you borrow any movie from his Pixar collection, except one. He\'s never gonna give you up.',
        'There\'s no (I) in Denial.',
        'There are 10 types of people in the world: those who understand binary, and those who don\'t.',
        'What is red and smells like blue paint? Red Paint.',
        'What do you call bears with no ears? B',
        'I invented a new word! Plagiarism']
    return random.choice(jokes)
DismisJokeAPI = [Jokes, in_Dismis]
def tell_joke(greetingMail):
    dismis_jokes = random.choice(DismisJokeAPI)()
    #print(dismis_jokes)
    d=open(greetingMail,'a+')
    d.write ("\n\n" + dismis_jokes + "\n -----------------------------------------------------------------------------------------")
def quote(greetingMail):
    oftheday = feedparser.parse("https://www.brainyquote.com/link/quotebr.rss")     #QuoteOfTheDay
    Love = feedparser.parse("https://www.brainyquote.com/link/quotelo.rss")         #LoveQuoteOfTheDay
    Art = feedparser.parse("https://www.brainyquote.com/link/quotear.rss")          #ArtQuoteOfTheDay
    Funny = feedparser.parse("https://www.brainyquote.com/link/quotefu.rss")        #FunnyQuoteOfTheDay
    Natures = feedparser.parse("https://www.brainyquote.com/link/quotena.rss")      #NaturesQuoteOfTheDay
    quoteoftheday1 = oftheday['feed']['title']
    quoteoftheday2 = oftheday ["entries"][0]["description"]
    quoteoftheday2 = quoteoftheday2.replace('"', '')
    lovequote1 = Love['feed']['title']
    lovequote2 = Love["entries"][0]["description"]
    lovequote2 = lovequote2.replace('"', '')
    artquote1 = Art['feed']['title']
    artquote2 = Art["entries"][0]["description"]
    artquote2 = artquote2.replace('"', '')
    funnyquote1 = Funny['feed']['title']
    funnyquote2 = Funny["entries"][0]["description"]
    funnyquote2 = funnyquote2.replace('"', '')
    naturequote1 = Natures['feed']['title']
    naturequote2 =Natures["entries"][0]["description"]
    naturequote2 = naturequote2.replace('"', '')
    d=open(greetingMail,'a+')
    d.write("\n\n" + quoteoftheday1)
    d.write("\n" + quoteoftheday2 )
    d.write("\n\n" + lovequote1)
    d.write("\n" + lovequote2)
    d.write("\n\n" + artquote1)
    d.write("\n" + artquote2)
    d.write("\n\n" + funnyquote1)
    d.write("\n" + funnyquote2)
    d.write("\n\n" + naturequote1)
    d.write("\n" + naturequote2 + "\n -----------------------------------------------------------------------------------------")
    #print(output1)
    #print(output2)
def weather_DefaultCity(default_CityLocation, openweatherAPI, greetingMail):
    api_key = openweatherAPI
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + default_CityLocation 
    json_data=requests.get(complete_url).json()
    try:
        temp=json_data['main']
        temp=str(int(int(temp['temp'])-273.15))
        temp1=json_data['weather'][0]['description']
        wind_speed =json_data['wind']['speed']
        p = "Current Temperature in "+default_CityLocation+" is "+temp+" degree celsius with "+temp1+ " and " + 'Wind Speed is {} metre per second'.format(wind_speed)
        d=open(greetingMail,'a+')
        d.write ("\n\n" + p + "\n -----------------------------------------------------------------------------------------")
    except KeyError:
        print("Key invalid or city not found")
        we = "Key invalid or city not found"
        d=open(greetingMail,'a+')
        d.write ("\n\n" + we + "\n -----------------------------------------------------------------------------------------")
def Alert4(slave_sender, slave_passwd, receiver):
    try:
        fromaddr = slave_sender
        toaddr = receiver
        msg = MIMEMultipart() # instance of MIMEMultipart 
        msg['From'] = fromaddr    # storing the main_senders email address 
        msg['To'] = toaddr   # storing the receivers email address 
        msg['Subject'] = "GREETING MAIL DATA!"# storing the subject  
        body = ''    # string to store the body of the mail
        msg.attach(MIMEText(body, 'plain'))     # attach the body with the msg instance 
        filename = "greetingMail.txt"    # open the file to be sent  
        attachment = open("/home/d-slave1/d1_SuperDismis/Dismis_Home_Automation/SystemService/APIs/greetingMail.txt", "rb") 
        p = MIMEBase('application', 'octet-stream')     # instance of MIMEBase and named as p 
        p.set_payload((attachment).read())     # To change the payload into encoded form 
        encoders.encode_base64(p)     # encode into base64
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
        msg.attach(p)     # attach the instance 'p' to instance 'msg' 
        s = smtplib.SMTP('smtp.gmail.com', 587)     # creates SMTP session 
        s.starttls()     # start TLS for security 
        s.login(fromaddr, slave_passwd)     # Authentication 
        text = msg.as_string()     # Converts the Multipart msg into a string 
        s.sendmail(fromaddr, toaddr, text)     # sending the mail 
        s.quit()     # terminating the session 
    except socket.gaierror:
        pass
        
""" Main Greeting SKILLS """
def Greeting(accept_path):
    os.system('play ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    banner(greetingMail)
    extractTime(greetingMail)
    tell_joke(greetingMail)
    quote(greetingMail)
    weather_DefaultCity(default_CityLocation, openweatherAPI,greetingMail)
    Alert4(slave_sender, slave_passwd, receiver)
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')
    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')
    if currentH >= 18 and currentH != 0:
        speak('Good Evening!')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('Greeting mail sent accomplish')
    d=open(greetingMail,'r')
    greetingData = d.read()
    print(greetingData)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: Greeting')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    os.system('gnome-terminal -x python3 ' + greetingMail + 'greeting__tts.py &')
    os.system('rm ' + greetingMail + ' &')
    print(' ')



def imgoingout(accept_path):
    os.system('play ' + accept_path +' &')
    time.sleep(1)
    result = 'PEMBA please check the schedule before going out.'
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: imgoingout')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    speak(result)
    #imgoingout_txt = open('imgoingout.txt','w+')
    #imgoingout_txt.write(result)
    #os.system('gnome-terminal -x python3 ' + conversationTTS + 'imgoingout__tts.py &')
    import smtplib, socket
    from email.mime.multipart import MIMEMultipart 
    from email.mime.text import MIMEText 
    from email.mime.base import MIMEBase 
    from email import encoders 
    try:
        fromaddr = slave_sender
        toaddr = receiver
        msg = MIMEMultipart() # instance of MIMEMultipart 
        msg['From'] = fromaddr    # storing the main_senders email address 
        msg['To'] = toaddr   # storing the receivers email address 
        msg['Subject'] = "SCHEDULE AND GOOGLE CALENDAR's EVENTS!"# storing the subject  
        body = 'no body'   # string to store the body of the mail
        msg.attach(MIMEText(body, 'plain'))     # attach the body with the msg instance 
        filename = "schedule_Gcalendar.txt"    # open the file to be sent  
        attachment = open("/home/d-slave1/d1_SuperDismis/Dismis_Home_Automation/SystemService/APIs/schedule_Gcalendar.txt", "rb") 
        p = MIMEBase('application', 'octet-stream')     # instance of MIMEBase and named as p 
        p.set_payload((attachment).read())     # To change the payload into encoded form 
        encoders.encode_base64(p)     # encode into base64
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
        msg.attach(p)     # attach the instance 'p' to instance 'msg' 
        s = smtplib.SMTP('smtp.gmail.com', 587)     # creates SMTP session 
        s.starttls()     # start TLS for security 
        s.login(fromaddr, slave_passwd)     # Authentication 
        text = msg.as_string()     # Converts the Multipart msg into a string 
        s.sendmail(fromaddr, toaddr, text)     # sending the mail 
        s.quit()     # terminating the session 
        speak('Schedule sent successfully in your primary mail')
    except socket.gaierror:
        pass

#still testing
""" CONVERTING *.txt > *.pdf """
from fpdf import FPDF 
def txt_to_pdf():
    time.sleep(2)
    #writing_textFile()
    # save FPDF() class into 
    # a variable pdf 
    pdf = FPDF() 
    # Add a page 
    pdf.add_page() 
    # set style and size of font 
    # that you want in the pdf 
    pdf.set_font("Arial", size = 15) 
    # open the text file in read mode 
    f = open("/home/pemba/d1_SuperDismis/Dismis-HA_GUI/Services/test.txt", "r") 
    # insert the texts in pdf 
    pdf.image("/home/pemba/d1_SuperDismis/Dismis-HA_GUI/Services/test.jpg", 50, 50)
    for x in f: 
        pdf.cell(200, 10, txt = x, ln = 1, align = 'C') 
    # save the pdf with name .pdf 
    pdf.output("/home/pemba/d1_SuperDismis/Dismis-HA_GUI/Services/mygfg.pdf") 
