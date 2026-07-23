import random
import sqlite3
import customtkinter as ctk
from customtkinter import IntVar
from customtkinter import StringVar
from sqlManager import *
from Classes import ActorClass
import pathlib


#class InitiativeBoard:
#    def __init__(self,frame4,theFont):
#        self.root = frame4
goblin1 = ActorClass.Actor(10,10,'Goblin',1)
Salinse = ActorClass.Actor(14,12,'Salinse',2)

attackRoll = 0
damageRoll = 0
while goblin1.hp > 0 and Salinse.hp > 0:
    if goblin1.InitiativeScore ==1:
        attackRoll = random.randint(1,20)
        if attackRoll >= Salinse.ac:
            damageRoll = random.randint(1,4)
            Salinse.apply_damage(damageRoll)
            print(f'{Salinse.name} took {damageRoll} damage! New HP is {Salinse.hp}')
        else:
            print(f'{goblin1.name} missed! {attackRoll} does not meet {Salinse.name}s AC: {Salinse.ac}')
        goblin1.updateInitiative(2)
        Salinse.updateInitiative(2)
    if Salinse.InitiativeScore ==1:
        attackRoll = random.randint(1,20)
        if attackRoll >= goblin1.ac:
            damageRoll = random.randint(1,4)
            goblin1.apply_damage(damageRoll)
            print(f'{goblin1.name} took {damageRoll} damage! New HP is {goblin1.hp}')
        else:
            print(f'{Salinse.name} missed! {attackRoll} does not meet {goblin1.name}s AC: {goblin1.ac}')
        goblin1.updateInitiative(2)
        Salinse.updateInitiative(2)

if Salinse.hp <= 0:
    print(f'{Salinse.name} is defeated. {goblin1.name} has {goblin1.hp} remaining')
if goblin1.hp <= 0:
    print(f'{goblin1.name} is defeated. {Salinse.name} has {Salinse.hp} remaining')