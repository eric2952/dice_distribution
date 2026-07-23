import sqlite3
import customtkinter as ctk
from customtkinter import IntVar
from customtkinter import StringVar
import pathlib
import sqlManager as sqlm

filepath = str(pathlib.Path(__file__).parent.resolve())
theDB = filepath + '/DB/GameDB.db'
addSkillExtension = '/SQLStatements/addSkill.sql'
SkillListExtension = '/SQLStatements/SkillnameList.sql'
updateSkillExtension = '/SQLStatements/updateSkill.sql'

def SkillSelectMenu_callback(choice,theFrame,theFont):
    refreshSkillManager(theFrame,theFont,choice)

def refreshSkillManager(theFrame, theFont,SkillName):
        labelArray = ['Skill Name','Required Attribute']
        labelobjArray = []
        statEntryArray = []
        i = 0
        j = 0
        SkillSelectMenuValues, SkillStatValues = sqlm.generate_Skill_List()
        SkillSelectMenu = ctk.CTkOptionMenu(theFrame,values=SkillSelectMenuValues,command=lambda choice:SkillSelectMenu_callback(choice,theFrame,theFont),fg_color="#6f2e6a")
        selectMenuLabel = ctk.CTkLabel(theFrame,text='Select Skill')

        while SkillStatValues[j][0] != SkillName:
            j+=1
        selectMenuLabel.grid(row=0,column = 2,padx=15,pady=5)
        SkillSelectMenu.grid(row=0,column = 3,padx = 5, pady = 5)
        SkillSelectMenu.set(SkillName)
        
        for label in labelArray:       
            statValue = SkillStatValues[j][i]
            thewidth = 120
            theheight = 28
            if 'Attribute' in label:
                statEntryArray.append(ctk.CTkOptionMenu(theFrame,values=['Intellect','Conscious','Coordination','Physique'],width=thewidth,height=theheight))
                statEntryArray[i].grid(row=i,column=1,padx=5,pady=5)            
                statEntryArray[i].set(statValue)    
            else:
                statEntryArray.append(ctk.CTkEntry(theFrame,textvariable=StringVar(theFrame,statValue),width=thewidth,height=theheight))
                statEntryArray[i].grid(row=i,column=1,padx=5,pady=5)
            labelobjArray.append(ctk.CTkLabel(theFrame,text=label,font=theFont))
            labelobjArray[i].grid(row=i,column=0,padx=5,pady=5)

            i+=1
        addNewSkill = ctk.CTkButton(theFrame,text='Add New Skill',fg_color='#2e6f40',command= lambda: [sqlm.collectSkillStatsNew(statEntryArray), refreshSkillManager(theFrame,theFont,statEntryArray[0].get())])
        addNewSkill.grid(row=1,column=2,padx=15)
        UpdateSkill = ctk.CTkButton(theFrame,text='Update Skill',fg_color="#2e6f64",command= lambda: [sqlm.collectSkillStatsUpdate(statEntryArray,SkillSelectMenu), refreshSkillManager(theFrame,theFont,statEntryArray[0].get())])
        UpdateSkill.grid(row=1,column=3,padx=15)

class SkillManagement:
    def __init__(self,frame3,theFont):
        self.root = frame3
        SkillSelectMenuValues, SkillStatValues = sqlm.generate_Skill_List()
        defaultSkill = SkillSelectMenuValues[0]
        refreshSkillManager(frame3,theFont,defaultSkill)
