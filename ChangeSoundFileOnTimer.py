import os
import time
import threading
import random
import shutil
import glob

#This is in seconds
amountOfTimeToWait = 10

#The file extension for the sounds you have. This only supports one file type at a time, but could be modified to do more in the future
fileType = ".wav"

curDirectory = os.path.dirname(__file__)

#This part opens the file that is being read from.
#The file being read from should be filled with text before running.
fileDir = os.path.join(curDirectory, 'SoundFiles')
if os.path.exists(fileDir):
    print("File path exists, check")
else:
    print("SoundFiles folder didn't exist, please add your files and run again")
    os.mkdir(fileDir)

destination = os.path.join(curDirectory, 'SoundToPlay')
if os.path.exists(destination):
    print('File path exists, check')
else:
    print("SoundToPlay folder didn't exist, recreating... Please run again")
    os.mkdir(destination)
    exit()

#This keeps track of the previously chosen sentence (just picked a random number to start, this won't ever be the first one chosen)
lastindex=3

#This gets called by itself after the amount of time set, on a loop
def updateSoundFile():   
    #Let this method know we need that variable between calls
    global lastindex

    for root, dirs, files in os.walk(destination):
        for file in files:
            os.remove(os.path.join(root,file))

    #Get the number of the files in the folder (This is dynamic* so files can be added while program is running)
    #*dynamic just means it updates itself when this method is called, so it's always accurate
    soundFiles = glob.glob1(fileDir, "*"+fileType)
    
    index = random.randint(0, len(soundFiles) - 1)
    while index == lastindex:
        index = random.randint(0, len(soundFiles) - 1)
    

    shutil.copyfile(os.path.join(fileDir, soundFiles[index]), os.path.join(destination, soundFiles[index]))

    #Increment the counter so next time we write a new sentence
    lastindex = index

    #Wait a certain amount of time and then call this again
    time.sleep(amountOfTimeToWait)
    updateSoundFile()

#Actually run the program
updateSoundFile()


