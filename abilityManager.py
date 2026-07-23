import sqlite3
import customtkinter as ctk
from customtkinter import IntVar
from customtkinter import StringVar
import pathlib
import sqlManager as sqlm

filepath = str(pathlib.Path(__file__).parent.resolve())
theDB = filepath + '/DB/GameDB.db'
addAbilityExtension = '/SQLStatements/addAbility.sql'
AbilityListExtension = '/SQLStatements/AbilitynameList.sql'
updateAbilityExtension = '/SQLStatements/updateAbility.sql'

def abilitySelectMenu_callback(choice,theFrame,theFont):
    refreshabilityManager(theFrame,theFont,choice)

def refreshabilityManager(theFrame, theFont,abilityName):
        labelArray = ['Name', 'Primary Attribute','Secondary Attribute','Requisit Skill','SkillMinLevel','Ability Type','Dice Count','Dice Sides','Description']
        labelobjArray = []
        statEntryArray = []
        i = 0
        j = 0
        abilitySelectMenuValues, abilityStatValues = sqlm.generate_Ability_List()
        SkillSelectMenuValues, SkillStatValues = sqlm.generate_Skill_List()
        abilitySelectMenu = ctk.CTkOptionMenu(theFrame,values=abilitySelectMenuValues,command=lambda choice:abilitySelectMenu_callback(choice,theFrame,theFont),fg_color="#6f2e6a")
        selectMenuLabel = ctk.CTkLabel(theFrame,text='Select Ability')

        while abilityStatValues[j][0] != abilityName:
            j+=1
        selectMenuLabel.grid(row=0,column = 2,padx=15,pady=5)
        abilitySelectMenu.grid(row=0,column = 3,padx = 5, pady = 5)
        abilitySelectMenu.set(abilityName)
        
        for label in labelArray:       
            statValue = abilityStatValues[j][i]
            thewidth = 120
            theheight = 28
            if 'Description' in label:
                 thewidth = 500
            if 'Attribute' in label:
                statEntryArray.append(ctk.CTkOptionMenu(theFrame,values=['Intellect','Conscious','Coordination','Physique'],width=thewidth,height=theheight))
                statEntryArray[i].grid(row=i,column=1,padx=5,pady=5)            
                statEntryArray[i].set(statValue)  
            elif 'Requisit' in label:
                statEntryArray.append(ctk.CTkOptionMenu(theFrame,values=SkillSelectMenuValues,width=thewidth,height=theheight))
                statEntryArray[i].grid(row=i,column=1,padx=5,pady=5)            
                statEntryArray[i].set(statValue)  
            else:
                statEntryArray.append(ctk.CTkEntry(theFrame,textvariable=StringVar(theFrame,statValue),width=thewidth,height=theheight))
                statEntryArray[i].grid(row=i,column=1,padx=5,pady=5)
            labelobjArray.append(ctk.CTkLabel(theFrame,text=label,font=theFont))
            labelobjArray[i].grid(row=i,column=0,padx=5,pady=5)

            i+=1
        addNewability = ctk.CTkButton(theFrame,text='Add New ability',fg_color='#2e6f40',command= lambda: [sqlm.collectAbilityStatsNew(statEntryArray), refreshabilityManager(theFrame,theFont,statEntryArray[0].get())])
        addNewability.grid(row=1,column=2,padx=15)
        Updateability = ctk.CTkButton(theFrame,text='Update ability',fg_color="#2e6f64",command= lambda: [sqlm.collectAbilityStatsUpdate(statEntryArray,abilitySelectMenu), refreshabilityManager(theFrame,theFont,statEntryArray[0].get())])
        Updateability.grid(row=1,column=3,padx=15)

class abilityManagement:
    def __init__(self,frame3,theFont):
        self.root = frame3
        abilitySelectMenuValues, abilityStatValues = sqlm.generate_Ability_List()
        defaultability = abilitySelectMenuValues[0]
        refreshabilityManager(frame3,theFont,defaultability)
