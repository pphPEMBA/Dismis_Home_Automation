import os, time

""" Other Dependencies For Dismis-Home Automation """
#pyaudio
os.system('apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0')
time.sleep(1)
#pico2wav
os.system('apt-get install libttspico-utils')
time.sleep(1)
#google
os.system('pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib')
time.sleep(1)
#sox
os.system('apt-get install sox libsox-fmt-mp3')

""" Python3 Libraries """
os.system('pip3 install -r requirement.txt')