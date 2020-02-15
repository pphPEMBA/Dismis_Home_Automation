""" Importing Profiles """
import yaml, os, time

profile = open('/home/pemba/d1_SuperDismis/Dismis-HA_GUI/SystemService/APIs/profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()
#Functioning Variables
conversationTTS_path = profile_data['conversationTTS_path']
accept_path = profile_data['accept_path']
slave_sender = profile_data['slave_sender']
slave_passwd = profile_data['slave_passwd']
receiver = profile_data['receiver']
conversationTTS = conversationTTS_path + '/SpeechDriver/ServicesTTS/conversationTTS/'

def whatthingcando(slave_sender, slave_passwd, accept_path):
    os.system('play ' + accept_path +' &')
    time.sleep(1)
    result = "I can\'t say everything instead I could send you a mail of what I can do. For that type your email below."
    whatthingcando_txt = open('whatthingcando.txt','a+')
    whatthingcando_txt.write(result)
    os.system('gnome-terminal -x python3 ' + conversationTTS + 'whatthingcando__tts.py')
    #print('python3 /home/pemba/d1_SuperDismis/Dismis-HA_GUI/SpeechDriver/ServicesTTS/conversationTTS/whatthingcando__tts.py')
    #print('python3 ' + conversationTTS + 'whatthingcando__tts.py')

whatthingcando(slave_sender, slave_passwd, accept_path)