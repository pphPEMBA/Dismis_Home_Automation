import subprocess, os, random
from pprint import pprint


#print(directory)
#dir = os.path.relpath(__file__)
##.realpath(__file__)
#print(dir)
#conversationTTS = directory + '/SpeechDriver/ServicesTTS/conversationTTS/'

def main():
    d = (['I am Dismis, A simple but efficient virtual assistant made by a 17 year old programmer in the winter of 2018', 'I am your godmother stupid', 'I am Dismis,I said that a ton of times already',
          'I am the one who needs no gun to get respect from no one on the street', 'Dismis, didnt I tell you before?', 'You ask that so many times! I am Dismis'])
    result = random.choice(d)
    who_are_you_txt = open("who_are_you.txt", "w+")
    who_are_you_txt.write(result)

#main()
os.system('gnome-terminal -x python3 /home/pemba/d1_SuperDismis/SpeechDriver/ServicesTTS/conversationTTS/how_are_you__tts.py')
os.system('gnome-terminal -x python3 /home/pemba/d1_SuperDismis/Dismis-HA_GUI/SpeechDriver/ServicesTTS/conversationTTS/how_are_you__tts.py')