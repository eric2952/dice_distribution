import os
from PIL import Image, ImageTk
import customtkinter as ctk
import random
from functools import partial


'''diceRoller functions'''
def collectDice(theLabel):
    thediceCount=theLabel.cget("text")
    thediceCount+=1
    theLabel.configure(text=thediceCount)

def rolltheDice(theLabelArr,resultLabel,resultInfo):
    i =0
    diceTotal = 0
    diceCounts = []
    for lbl in theLabelArr:
        diceCounts.append(lbl.cget("text"))
        lbl.configure(text=0)
    
    diceTypes = [4,6,8,10,12,20]
    displayInfo = ''

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

class theRoller:
    def __init__(self,frame2,theFont):
        self.root = frame2
        imagePath = os.path.dirname(os.path.realpath(__file__)) + '/Images/'

        resultLabel = ctk.CTkLabel(frame2,text=0,font=theFont)
        resultInfoLabel = ctk.CTkLabel(frame2,text='',font=theFont)
        lblcount = 0
        labelArr = []
        imageArr = []
        buttonArr = []
        diceImageArr = ['d4.png','d6.png','d8.png','d10.png','d12.png','d20.png']
        while lblcount < 6:
            labelArr.append(ctk.CTkLabel(frame2,text=0,font=theFont))
            imageArr.append(ctk.CTkImage(Image.open(imagePath + diceImageArr[lblcount]), size=(80,80)))
            buttonArr.append(ctk.CTkButton(frame2,image=imageArr[lblcount],text='',corner_radius=240,command=partial(collectDice,labelArr[lblcount])))
            buttonArr[lblcount].grid(row=lblcount,column=0,padx=5,pady=5)
            labelArr[lblcount].grid(row=lblcount,column=1,padx=5,pady=5)
            lblcount+=1

        rollbutton = ctk.CTkButton(frame2,text='Roll Dice',corner_radius=20, command=lambda *args: rolltheDice(labelArr,resultLabel,resultInfoLabel))        
        rollbutton.grid(row=6,column=0,padx=5,pady=5)
        resultLabel.grid(row=6,column=1,padx=5,pady=5)
        resultInfoLabel.grid(row=6,column=2,padx=5,pady=5)