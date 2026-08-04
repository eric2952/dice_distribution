import random
import sqlite3
import customtkinter as ctk
from customtkinter import IntVar
from customtkinter import StringVar
from sqlManager import *
from Classes import ActorClass
import sqlManager as sqlm
import pathlib


#class InitiativeBoard:
#    def __init__(self,frame4,theFont):
#        self.root = frame4


CharacterList, characterStatValues = sqlm.generate_Character_List()
SkillList, SkillStats = sqlm.generate_Skill_List()
characterArray = []
i = 0
for character in CharacterList:
    CharacterSkillDBtuple = generate_Skill_Progress_List(characterStatValues[i][1])
    skillDictionary = {}
    
    for skill in CharacterSkillDBtuple:
        skillDictionary[skill[0]] = [skill[2],skill[3]]
    if not skillDictionary:
        for skill in SkillList:
            skillDictionary[skill] = [0,0]
    tempCharacter = ActorClass.Actor(characterStatValues[i][3],characterStatValues[i][4],characterStatValues[i][1],characterStatValues[i][5],characterType=characterStatValues[i][2],Skills=skillDictionary)
    characterArray.append(tempCharacter)
    #print(f'{tempCharacter.name} stats: {tempCharacter.Skills}')
    i+=1

def selectCharacter(selectedName,chr):
    for character in chr:
        if selectedName == character.name:
            return character

i=0
for character in characterArray:
    print(characterArray[i].name)
    i+=1
characterName = input('Select from the above List: ')
returnCharacter = selectCharacter(characterName,characterArray)
print(returnCharacter.name)
j = 0
for skill in returnCharacter.Skills:
    print(skill)
usedSkill = input('Select skill to use: ')
print(f'{usedSkill} level: {returnCharacter.Skills[usedSkill][0]}')
abilityUseExperience = input('Experience gained: ')
returnCharacter.addSkillExperience(usedSkill,int(abilityUseExperience))
print(f'{usedSkill} level: {returnCharacter.Skills[usedSkill][0]}, Exp: {returnCharacter.Skills[usedSkill][1]}')