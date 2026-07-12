import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import customtkinter as ctk
from dmgPlotter import DamagePlotter
from customtkinter import CTkTabview
from diceRoller import theRoller

darkblue='#274f58'
rushred='#5c092d'
whitewords='#cdcdcd'
steelgrey='#353b45'
backgroundBlack='#20292f'


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def main():
    winwidth = 1020
    winheight = 940
    root = ctk.CTk()
    root.title('Game Master Suite')
    root.geometry(f'{winwidth}x{winheight}')

    thefont = ctk.CTkFont(family='Helvetica', size=12)
    notebook = CTkTabview(root)
    notebook.pack(expand=True,fill='both')


    tab1 = notebook.add('Damage Distribution')
    tab2 = notebook.add('Dice Roller')
    tab3 = notebook.add('Initiative Tracker')

    frame1 = ctk.CTkFrame(tab1,width=winwidth,height=winheight)
    frame2 = ctk.CTkFrame(tab2,width=winwidth,height=winheight)
    frame3 = ctk.CTkFrame(tab3,width=winwidth,height=winheight)
    frame1.pack(fill='both')
    frame2.pack(fill='both')
    frame3.pack(fill='both')

    DamagePlotter(frame1,thefont)
    theRoller(frame2,thefont)

    root.mainloop()

if __name__ == '__main__':
    main()