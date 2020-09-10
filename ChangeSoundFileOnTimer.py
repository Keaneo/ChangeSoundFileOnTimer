import os
import time
import threading
import random
import shutil
import glob

#This is in seconds
amountOfTimeToWait = 1

#The file extension for the sounds you have. This only supports one file type at a time, but could be modified to do more in the future
fileType = ".txt"

#Find the current directory the script is in
curDirectory = os.path.dirname(__file__)

#Check if the SoundFiles folder exists, otherwise make it and carry on (Chances are neither it or the next folder exist on the first run)
#This isn't perfect code since it doesn't cope with any... "Undocumented" circumstances, i.e it's not very flexible, but it does the job if the steps are followed
fileDir = os.path.join(curDirectory, 'SoundFiles')
if os.path.exists(fileDir):
    print("File path exists, check")
else:
    print("SoundFiles folder didn't exist, please add your files and run again")
    os.mkdir(fileDir)

#Check if the SoundToPlay folder exists, otherwise make it and close the program
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

    if len(soundFiles) == 0:
        print("There are no files matching the set filetype, exiting...")
        exit()
    
    #Pick a random number that's different from the previous
    index = random.randint(0, len(soundFiles) - 1)
    if len(soundFiles) != 1:
        while index == lastindex:
            index = random.randint(0, len(soundFiles) - 1)
    
    #Copy the file to the destination folder.
    shutil.copyfile(os.path.join(fileDir, soundFiles[index]), os.path.join(destination, "playthis" + fileType))

    #Increment the counter so next time we write a new sentence
    lastindex = index

    #If the amountOfTimeToWait is 0, then just close the program
    if amountOfTimeToWait == 0:
        exit()

    #Wait a certain amount of time and then call this again
    time.sleep(amountOfTimeToWait)
    updateSoundFile()

#Actually run the program
updateSoundFile()


