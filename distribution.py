import customtkinter as ctk
from dmgPlotter import DamagePlotter
from customtkinter import CTkTabview
from diceRoller import theRoller
from characterManager import CharacterManagement
#from InitiativeTracker import InitiativeBoard
from abilityManager import abilityManagement
from skillManager import SkillManagement

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
    tab3 = notebook.add('Character Manager')
    tab4 = notebook.add('Initiative Tracker')
    tab5 = notebook.add('Ability Managment')
    tab6 = notebook.add('Skill Manager')

    frame1 = ctk.CTkFrame(tab1,width=winwidth,height=winheight)
    frame2 = ctk.CTkFrame(tab2,width=winwidth,height=winheight)
    frame3 = ctk.CTkFrame(tab3,width=winwidth,height=winheight)
    frame4 = ctk.CTkFrame(tab4,width=winwidth,height=winheight)
    frame5 = ctk.CTkFrame(tab5,width=winwidth,height=winheight)
    frame6 = ctk.CTkFrame(tab6,width=winwidth,height=winheight)
    frame1.pack(fill='both')
    frame2.pack(fill='both')
    frame3.pack(fill='both')
    frame4.pack(fill='both')
    frame5.pack(fill='both')
    frame6.pack(fill='both')

    DamagePlotter(frame1,thefont)
    theRoller(frame2,thefont)
    CharacterManagement(frame3,thefont)
#    InitiativeBoard(frame4,thefont)
    abilityManagement(frame5,thefont)
    SkillManagement(frame6,thefont)


    root.mainloop()

if __name__ == '__main__':
    main()