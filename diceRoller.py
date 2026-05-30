import customtkinter
from customtkinter import IntVar
from customtkinter import StringVar
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os
from PIL import Image, ImageTk
import customtkinter as ctk

class theRoller:
    def __init__(self,frame2,theFont):
        self.root = frame2
        imagePath = os.path.dirname(os.path.realpath(__file__)) + '/Images/'

        d4image = ctk.CTkImage(Image.open(imagePath + 'd4.png'), size=(80,90))
        d4button = ctk.CTkButton(frame2,image=d4image,text='',corner_radius=240)
        d6image = ctk.CTkImage(Image.open(imagePath + 'd6.png'), size=(80,80))
        d6button = ctk.CTkButton(frame2,image=d6image,text='',corner_radius=240)
        d8image = ctk.CTkImage(Image.open(imagePath + 'd8.png'), size=(80,80))
        d8button = ctk.CTkButton(frame2,image=d8image,text='',corner_radius=240)
        d10image = ctk.CTkImage(Image.open(imagePath + 'd10.png'), size=(80,80))
        d10button = ctk.CTkButton(frame2,image=d10image,text='',corner_radius=240)
        d12image = ctk.CTkImage(Image.open(imagePath + 'd12.png'), size=(80,80))
        d12button = ctk.CTkButton(frame2,image=d12image,text='',corner_radius=240)
        d20image = ctk.CTkImage(Image.open(imagePath + 'd20.png'), size=(80,80))
        d20button = ctk.CTkButton(frame2,image=d20image,text='',corner_radius=240)
        rollbutton = ctk.CTkButton(frame2,text='Roll Dice',corner_radius=20)
        d4button.pack()
        d6button.pack()
        d8button.pack()
        d10button.pack()
        d12button.pack()
        d20button.pack()
        rollbutton.pack()