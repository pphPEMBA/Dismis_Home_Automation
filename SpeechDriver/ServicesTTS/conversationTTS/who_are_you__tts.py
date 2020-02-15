#!/usr/bin/python3
import os,yaml
import sys, time


def speak(message): #ALSO USING IN || BestfriendBirthdayALERT_ai.py | schedule_ai.py | googleMailNotify ||
   """This function takes a message as an argument and converts it to speech depending on the OS.  """
   if sys.platform == 'darwin':
      tts_engine = 'say'
      return os.system(tts_engine + ' ' + message)
   elif sys.platform == 'Linux' or sys.platform == 'linux' or sys.platform == 'Ubuntu':
      #espeak
      """tts_engine = 'espeak'
      print(tts_engine + ' "' + message + '"')
      return os.system(tts_engine + ' "' + message + '"')"""
      #pico2wave
      print(' ')
      tts_engine = 'pico2wave -w tts_pico2wave.wav '
      print(' ')
      return os.system(tts_engine + ' "' + message + '"' + '&& aplay tts_pico2wave.wav && rm tts_pico2wave.wav')

with open('who_are_you.txt', 'r') as who_are_you_txt:
   tts = who_are_you_txt.read()
   print(tts)
   speak(tts)
#who_are_you_txt = open('who_are_you.txt','r')
#tts = who_are_you_txt.read()
#speak(tts)
#print('error')
#os.system('rm who_are_you.txt')