import os.path
import datetime
from tkinter import *

gui = Tk()
gui.title('Emotion Diary')
gui.minsize(width=600, height=600)
gui.maxsize(width=800, height=800)
fileStorePath = "diaryRecords.txt"

# Mood selection variable
mood = StringVar()
desc = StringVar()

# Final Screen
def diaryRecordScreen(gui, diaryEntry):
    diaryEntriesLabel = None
    restartButton = None

    def restart():
        diaryEntriesLabel.pack_forget()
        restartButton.pack_forget()
        startMoodSelectionScreen(gui)
    
    # if file does not exist create it
    def writeToFileStore(fileStorePath, line):
        if os.path.isfile(fileStorePath) == False:
            newFileStore = open(fileStorePath, "w+")
            newFileStore.close()
        fileStore = open(fileStorePath, "a+")
        currentDate = datetime.datetime.now()
        fileStore.write(line + "\r\n")
        fileStore.close()

    def readFromFileStore(fileStorePath):
        fileStore = open(fileStorePath, "r")
        contents = fileStore.read()
        fileStore.close()
        return contents
    
    # Write mood and description to file
    fileStore = writeToFileStore(fileStorePath, diaryEntry)
    # Read lines from file as a String
    fileStoreContents = readFromFileStore(fileStorePath)
    # Display string on gui
    diaryEntriesLabel = Label(gui,
                              text = fileStoreContents)
    diaryEntriesLabel.pack( anchor = W )

    restartButton = Button(gui,
                           text = "Restart",
                           command = restart)
    restartButton.pack( anchor = W )
    
# Screen 4
def startDescriptionInputScreen(gui):
    descLabel = None
    descInput = None
    descEnter = None
    
    def descriptionInputHandler():
        global desc
        descLabel.pack_forget()
        descInput.pack_forget()
        descEnter.pack_forget()
        desc = descInput.get()
        currentDate = datetime.datetime.now()
        diaryEntry = "On " + currentDate.strftime("%d %m %Y %H:%M:%S") + " you were feeling: " + mood + ". Because: " + desc
        diaryRecordScreen(gui, diaryEntry)

    var = StringVar()

    descLabel = Label(gui,
                      text = "Description:")
    descLabel.pack( anchor = CENTER )

    descInput = Entry(gui,
                      textvariable = desc)
    
    descInput.pack( anchor = CENTER )

    descEnter = Button(gui,
                       text = "Enter:",
                       command = descriptionInputHandler)
    descEnter.pack( anchor = CENTER )
        
    

# Screen 3
def startMoodSelectionScreen(gui):
    R1 = None
    R2 = None
    R3 = None
    

    def moodSelectionHandler():
        global mood
        if var.get() == 1:
            mood = "Happy"
        elif var.get() == 2:
            mood = "Content"
        elif var.get() == 3:
            mood = "Sad"
        R1.pack_forget()
        R2.pack_forget()
        R3.pack_forget()
        startDescriptionInputScreen(gui)

    var = IntVar()

    happyImage = PhotoImage(file = "Smiley.PNG")
    R1 = Radiobutton(gui,
                     variable = var,
                     value = 1,
                     command = moodSelectionHandler)
    R1.config(image = happyImage,
              width="120",
              height="120",
              bd=0)
    R1.image = happyImage
    R1.pack( anchor = CENTER )


    contentImage = PhotoImage(file = "Content.png")
    R2 = Radiobutton(gui,
                     variable = var,
                     value = 2,
                     command = moodSelectionHandler)
    R2.config(image = contentImage,
              width="120",
              height="120",
              bd=0)
    R2.image = contentImage
    R2.pack( anchor = CENTER )
    
    SadImage = PhotoImage(file = "Sad.png")
    R3 = Radiobutton(gui,
                     variable = var,
                     value = 3,
                     command = moodSelectionHandler)
    R3.config(image = SadImage,
              width="120",
              height="120",
              bd=0)
    R3.image = SadImage
    R3.pack( anchor = CENTER )
    
startMoodSelectionScreen(gui)                     


gui.mainloop()
