import sqlite3
import customtkinter as ctk
from customtkinter import IntVar
from customtkinter import StringVar
import pathlib
import sqlManager as sqlm

filepath = str(pathlib.Path(__file__).parent.resolve())
theDB = filepath + '/DB/GameDB.db'
addCharacterExtension = '/SQLStatements/addCharacter.sql'
characterListExtension = '/SQLStatements/characternameList.sql'
updateCharacterExtension = '/SQLStatements/updateCharacter.sql'

def characterSelectMenu_callback(choice,theFrame,theFont):
    refreshCharacterManager(theFrame,theFont,choice)

def refreshCharacterManager(theFrame, theFont,characterName):
        labelArray = ['Name','Character Type','Max Hit Points','Armor Class','Initiative Bonus','Movement Speed','Intellect Score','Conscious Score','Coordination Score','Physique Score']
        labelobjArray = []
        statEntryArray = []
        skillLabelArray = []
        skillEntryArray = []
        abilityLabelArray = []
        i = 0
        j = 0
        characterSelectMenuValues, characterStatValues = sqlm.generate_Character_List()
        abilitySelectMenuValues, abilityStatValues = sqlm.generate_Ability_List()
        SkillSelectMenuValues, SkillStatValues = sqlm.generate_Skill_List()
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
        skillsLabel = ctk.CTkLabel(theFrame,text='Skills',font=theFont)
        AbilitiesLabel = ctk.CTkLabel(theFrame,text='Abilities')
        skillsLabel.grid(row=i,column=0,padx=5,pady=5)
        AbilitiesLabel.grid(row=i,column=2,padx=5,pady=5)
        k = i+1
        i = 0
        j = 0    

        for skill in SkillStatValues:
            theSkill = skill[0]
            skillLabelArray.append(ctk.CTkLabel(theFrame,text = theSkill, font=theFont))
            skillLabelArray[i].grid(row=k,column=0,padx=5,pady=5)
            i+=1
            k+=1
        addNewCharacter = ctk.CTkButton(theFrame,text='Add New Character',fg_color='#2e6f40',command= lambda: [sqlm.collectStatsNew(statEntryArray), refreshCharacterManager(theFrame,theFont,statEntryArray[0].get())])
        addNewCharacter.grid(row=1,column=2,padx=15)
        UpdateCharacter = ctk.CTkButton(theFrame,text='Update Character',fg_color="#2e6f64",command= lambda: [sqlm.collectStatsUpdate(statEntryArray,characterSelectMenu), refreshCharacterManager(theFrame,theFont,statEntryArray[0].get())])
        UpdateCharacter.grid(row=1,column=3,padx=15)

class CharacterManagement:
    def __init__(self,frame3,theFont):
        self.root = frame3
        characterSelectMenuValues, characterStatValues = sqlm.generate_Character_List()
        defaultCharacter = characterSelectMenuValues[0]
        refreshCharacterManager(frame3,theFont,defaultCharacter)
