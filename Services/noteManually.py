import subprocess
import os, time
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
noteManuallyTTS_path = profile_data['noteManuallyTTS_path']
noteManuallyTTS = noteManuallyTTS_path + '/SpeechDriver/tts/ServicesTTS/noteManuallyTTS/'
#print(noteManuallyTTS)


def note_manually(accept_path, noteManually_txt):
    ''' Opens 'noteManually.txt' using gedit to let users to set the appointments manually.
    Also displays the previous appointments. '''
    os.system('play ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('Pemba rember you\'ve to save it manually, And opening gedit.')
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: note_manually')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    result = 'Opening gedit, Pemba remeber you\'ve to save it manually'
    #os.system(['gedit', noteManually_txt])
    proc = subprocess.Popen(['gedit', noteManually_txt])
    proc.wait()
    note_manually_txt = open('note_manually.txt','w+')
    note_manually_txt.write(result)
    os.system('gnome-terminal -x python3 ' + noteManuallyTTS + 'note_manually__tts.py &')
    print(' ')



def readNote_manually(accept_path, noteManually_txt):
    ''' Reads the appointments line by line from noteManually.txt '''
    os.system('play ' + accept_path +' &')
    time.sleep(1)
    print(' ')
    print(' ')
    if(os.stat(noteManually_txt).st_size == 0):
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print("You don't have any notes.")
        print(' ')
        print(' ')
        print('\t\t\t\tSkill: readNote_manually')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        result = "You don't have any notes."
        readNoteManually_txt = open('readNoteManually.txt','w+')
        readNoteManually_txt.write(result)
        os.system('gnome-terminal -x python3 ' + noteManuallyTTS + 'readNoteManually__tts.py &')
        print(' ')
    else:
        with open(noteManually_txt) as f:
            no_of_tasks = sum(1 for _ in f)
            result = "You have "+str(no_of_tasks) + " notes."
            print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            print(' ')
            print(' ')
            Log_Time()
            print("You have "+str(no_of_tasks) + " notes.")
            print(' ')
        file = open(noteManually_txt, "r")
        for line in file:
            print(line)
            result(line)
        print(' ')
        print(' ')
        print('\t\t\t\tSkill: readNote_manually')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        readNoteManually_txt = open('readNoteManually.txt','w+')
        readNoteManually_txt.write(result)
        os.system('gnome-terminal -x python3 ' + noteManuallyTTS + 'readNoteManually__tts.py &')
        print(' ')
