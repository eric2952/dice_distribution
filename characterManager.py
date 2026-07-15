import sqlite3
import customtkinter as ctk
from customtkinter import IntVar
from customtkinter import StringVar
import pathlib

filepath = str(pathlib.Path(__file__).parent.resolve())
theDB = filepath + '/DB/GameDB.db'
addCharacterExtension = '/SQLStatements/addCharacter.sql'
characterListExtension = '/SQLStatements/characternameList.sql'
updateCharacterExtension = '/SQLStatements/updateCharacter.sql'

def grabScript(scriptExtension):
    with open(filepath + scriptExtension,"r",encoding="utf-8") as f:
        scriptText = f.read()
    return scriptText
def add_Character(character):
    with sqlite3.connect(theDB) as conn:
        cur = conn.cursor()
        cur.execute(grabScript(addCharacterExtension),character)
        conn.commit()
        return cur.lastrowid
def update_Character(character):
    with sqlite3.connect(theDB) as conn:
        cur = conn.cursor()
        cur.execute(grabScript(updateCharacterExtension),character)
        conn.commit()
        return cur.lastrowid
def generate_Character_List(filterParameter = None):
    with sqlite3.connect(theDB) as conn:
        cur = conn.cursor()
        cur.execute(grabScript(characterListExtension))
        names = [row[1] for row in cur.fetchall()]
        cur.execute(grabScript(characterListExtension))
        statblocks = cur.fetchall()
        return names, statblocks
def characterSelectMenu_callback(choice,theFrame,theFont):
    refreshCharacterManager(theFrame,theFont,choice)
def collectStatsNew(statEntryArray):
    statArray=[]
    for entry in statEntryArray:
        statArray.append(entry.get())
    print (statArray)
    character = tuple(statArray)
    add_Character(character)
def collectStatsUpdate(statEntryArray,CharacterMenu):
    statArray=[]
    for entry in statEntryArray:
        statArray.append(entry.get())
    statArray.append(CharacterMenu.get())
    print (statArray)
    character = tuple(statArray)
    update_Character(character)

def refreshCharacterManager(theFrame, theFont,characterName):
        labelArray = ['Name','Character Type','Max Hit Points','Armor Class','Initiative Bonus','Strength Score','Dexterity Score','Constitution Score','Intelligence Score','Wisdom Score','Charisma Score','Ability Selection']
        labelobjArray = []
        statEntryArray = []
        i = 0
        j = 0
        characterSelectMenuValues, characterStatValues = generate_Character_List()
        characterSelectMenu = ctk.CTkOptionMenu(theFrame,values=characterSelectMenuValues,command=lambda choice:characterSelectMenu_callback(choice,theFrame,theFont),fg_color="#6f2e6a")
        selectMenuLabel = ctk.CTkLabel(theFrame,text='Select Character')
        
        while characterStatValues[j][1] != characterName:
            j+=1
        selectMenuLabel.grid(row=0,column = 2,padx=15,pady=5)
        characterSelectMenu.grid(row=0,column = 3,padx = 5, pady = 5)
        characterSelectMenu.set(characterName)
        
        for label in labelArray:       
            statValue = characterStatValues[j][i+1]    
            labelobjArray.append(ctk.CTkLabel(theFrame,text=label,font=theFont))
            statEntryArray.append(ctk.CTkEntry(theFrame,textvariable=StringVar(theFrame,statValue)))
            labelobjArray[i].grid(row=i,column=0,padx=5,pady=5)
            statEntryArray[i].grid(row=i,column=1,padx=5,pady=5)
            i+=1
        addNewCharacter = ctk.CTkButton(theFrame,text='Add New Character',fg_color='#2e6f40',command= lambda: [collectStatsNew(statEntryArray), refreshCharacterManager(theFrame,theFont,statEntryArray[0].get())])
        addNewCharacter.grid(row=1,column=2,padx=15)
        UpdateCharacter = ctk.CTkButton(theFrame,text='Update Character',fg_color="#2e6f64",command= lambda: [collectStatsUpdate(statEntryArray,characterSelectMenu), refreshCharacterManager(theFrame,theFont,statEntryArray[0].get())])
        UpdateCharacter.grid(row=1,column=3,padx=15)

class CharacterManagement:
    def __init__(self,frame3,theFont):
        self.root = frame3
        characterSelectMenuValues, characterStatValues = generate_Character_List()
        defaultCharacter = characterSelectMenuValues[0]
        refreshCharacterManager(frame3,theFont,defaultCharacter)
