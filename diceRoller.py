import os
from PIL import Image, ImageTk
import customtkinter as ctk
import random


'''diceRoller functions'''
def collectDice(theLabel):
    thediceCount=theLabel.cget("text")
    thediceCount+=1
    theLabel.configure(text=thediceCount)

def rolltheDice(d4label,d6label,d8label,d10label,d12label,d20label,resultLabel,resultInfo):
    i =0
    diceTotal = 0
    diceCounts = [d4label.cget("text"),d6label.cget("text"),d8label.cget("text"),d10label.cget("text"),d12label.cget("text"),d20label.cget("text")]
    diceTypes = [4,6,8,10,12,20]
    displayInfo = ''
    d4label.configure(text=0)
    d6label.configure(text=0)
    d8label.configure(text=0)
    d10label.configure(text=0)
    d12label.configure(text=0)
    d20label.configure(text=0)
    for dice in diceCounts:
        j = 0
        while j < dice:
            thisRoll = 0
            thisRoll = random.randint(1,diceTypes[i])
            diceTotal+= thisRoll
            displayInfo+= f' d{diceTypes[i]} result: {thisRoll}'
            j+=1
        i+=1
    resultLabel.configure(text=diceTotal)
    resultInfo.configure(text=displayInfo)
    #while i <= thediceCount:
        #diceTotal+=random.randint(1,diceType)

class theRoller:
    def __init__(self,frame2,theFont):
        self.root = frame2
        imagePath = os.path.dirname(os.path.realpath(__file__)) + '/Images/'

        resultLabel = ctk.CTkLabel(frame2,text=0,font=theFont)
        resultInfoLabel = ctk.CTkLabel(frame2,text='',font=theFont)
        d4CountLabel = ctk.CTkLabel(frame2,text=0,font=theFont)
        d6CountLabel = ctk.CTkLabel(frame2,text=0,font=theFont)
        d8CountLabel = ctk.CTkLabel(frame2,text=0,font=theFont)
        d10CountLabel = ctk.CTkLabel(frame2,text=0,font=theFont)
        d12CountLabel = ctk.CTkLabel(frame2,text=0,font=theFont)
        d20CountLabel = ctk.CTkLabel(frame2,text=0,font=theFont)

        d4image = ctk.CTkImage(Image.open(imagePath + 'd4.png'), size=(80,90))
        d4button = ctk.CTkButton(frame2,image=d4image,text='',corner_radius=240,command=lambda *args: collectDice(d4CountLabel))
        d6image = ctk.CTkImage(Image.open(imagePath + 'd6.png'), size=(80,80))
        d6button = ctk.CTkButton(frame2,image=d6image,text='',corner_radius=240,command=lambda *args: collectDice(d6CountLabel))
        d8image = ctk.CTkImage(Image.open(imagePath + 'd8.png'), size=(80,80))
        d8button = ctk.CTkButton(frame2,image=d8image,text='',corner_radius=240,command=lambda *args: collectDice(d8CountLabel))
        d10image = ctk.CTkImage(Image.open(imagePath + 'd10.png'), size=(80,80))
        d10button = ctk.CTkButton(frame2,image=d10image,text='',corner_radius=240,command=lambda *args: collectDice(d10CountLabel))
        d12image = ctk.CTkImage(Image.open(imagePath + 'd12.png'), size=(80,80))
        d12button = ctk.CTkButton(frame2,image=d12image,text='',corner_radius=240,command=lambda *args: collectDice(d12CountLabel))
        d20image = ctk.CTkImage(Image.open(imagePath + 'd20.png'), size=(80,80))
        d20button = ctk.CTkButton(frame2,image=d20image,text='',corner_radius=240,command=lambda *args: collectDice(d20CountLabel))
        rollbutton = ctk.CTkButton(frame2,text='Roll Dice',corner_radius=20, command=lambda *args: rolltheDice(d4CountLabel,d6CountLabel,d8CountLabel,d10CountLabel,d12CountLabel,d20CountLabel,resultLabel,resultInfoLabel))

        d4button.grid(row=0,column=0,padx=5,pady=5)
        d4CountLabel.grid(row=0,column=1,padx=5,pady=5)
        d6button.grid(row=1,column=0,padx=5,pady=5)
        d6CountLabel.grid(row=1,column=1,padx=5,pady=5)
        d8button.grid(row=2,column=0,padx=5,pady=5)
        d8CountLabel.grid(row=2,column=1,padx=5,pady=5)
        d10button.grid(row=3,column=0,padx=5,pady=5)
        d10CountLabel.grid(row=3,column=1,padx=5,pady=5)
        d12button.grid(row=4,column=0,padx=5,pady=5)
        d12CountLabel.grid(row=4,column=1,padx=5,pady=5)
        d20button.grid(row=5,column=0,padx=5,pady=5)
        d20CountLabel.grid(row=5,column=1,padx=5,pady=5)
        rollbutton.grid(row=6,column=0,padx=5,pady=5)
        resultLabel.grid(row=6,column=1,padx=5,pady=5)
        resultInfoLabel.grid(row=6,column=2,padx=5,pady=5)