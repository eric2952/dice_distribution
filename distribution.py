import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import customtkinter
from customtkinter import IntVar
from customtkinter import StringVar
import diceCalculations
from diceCalculations import *

darkblue='#274f58'
rushred='#5c092d'
whitewords='#cdcdcd'
steelgrey='#353b45'
backgroundBlack='#20292f'

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


'''
def MUn(n,s):
    return(.5*n*(s+1))
def sigSquared(n,s):
    MU1 = MUn(1,s)
    return(n*(((1/6)*(s+1)*((2*s)+1))-(MU1**2)))
def numberDistribution(x,sigma,MU):
    returnNumber = (1/(2*3.1415926*sigma))*(2.71828**(-.5*(((x-MU)/sigma)**2)))
    return(returnNumber)
def hitModifier(theDC,theSave):
    return((theDC-theSave-1)/20)
'''

class DamagePlotter:
    def __init__(self,root,theFont):
        self.root = root
        root.title('Predict Damage Output')

        self.DC_var = IntVar()
        self.SavingThrow = IntVar()
        self.DiceCount = IntVar()
        self.SidedDice = IntVar()
        self.rollMode = StringVar()

        inputFrame = customtkinter.CTkFrame(master=root)
        DCinput = customtkinter.CTkEntry(inputFrame,placeholder_text='DC Input',textvariable=self.DC_var)
        SaveBonusInput = customtkinter.CTkEntry(inputFrame,placeholder_text='Save Throw Bonus',textvariable=self.SavingThrow)
        numberofDiceInput = customtkinter.CTkEntry(inputFrame,placeholder_text='Number of Dice',textvariable=self.DiceCount)
        diceSidesInput = customtkinter.CTkEntry(inputFrame,placeholder_text='Number of Sides',textvariable=self.SidedDice)


        dclabel = customtkinter.CTkLabel(inputFrame,text="DC or AC",font=theFont)
        savelabel = customtkinter.CTkLabel(inputFrame,text="Save or Attack Bonus",font=theFont)
        numberdicelabel = customtkinter.CTkLabel(inputFrame,text='Number of Dice',font=theFont)
        numbersideslabel = customtkinter.CTkLabel(inputFrame,text='Sides of Dice',font=theFont)

        attackButton = customtkinter.CTkCheckBox(inputFrame,text='Saving Throw',variable=self.rollMode,onvalue='Save',offvalue='Attack')
        attackButton.deselect()

        attackButton.grid(row=0,column=2)
        DCinput.grid(row=0,column=1)
        SaveBonusInput.grid(row=1,column=1)
        numberofDiceInput.grid(row=2,column=1)
        diceSidesInput.grid(row=3,column=1)

        dclabel.grid(row=0,column=0)
        savelabel.grid(row=1,column=0)
        numberdicelabel.grid(row=2,column=0)
        numbersideslabel.grid(row=3,column=0)

        inputFrame.pack()

        load_button = customtkinter.CTkButton(self.root, text='Generate Odds', command=self.update_plot)
        load_button.pack()


        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master = self.root)
        self.widget = self.canvas.get_tk_widget()
        self.widget.pack(padx=10, pady=10)

    def load_parameters(self):
        pass

    def update_plot(self, event=None):

        #plot_type = self.plot_type_var
        DC_score = self.DC_var.get()
        savingThrow = self.SavingThrow.get()
        diceCount = self.DiceCount.get()
        sidedDice = self.SidedDice.get()
        checkType = self.rollMode.get()
        

        maxDamage = 1+(diceCount * sidedDice)
        damageDistribution = []
        DamageArray = [k for k in range(0, maxDamage+5)]
        sigHit = sigSquared(diceCount,sidedDice)**.5
        muHit = MUn(diceCount,sidedDice)

        if checkType == 'Save':
            hHit = hitModifier(DC_score,savingThrow)
            hMiss = 1-hHit
            muMiss = .5*muHit
            sigMiss = .5*sigHit
        else:
            hMiss = hitModifier(DC_score, savingThrow)
            hHit = 1-hMiss
            muMiss = 0
            sigMiss = 10

        for damage in DamageArray:
            damageDistribution.append((hMiss*numberDistribution(damage,sigMiss,muMiss))+(hHit*numberDistribution(damage,sigHit,muHit)))

        self.ax.clear()
        self.ax.plot(DamageArray,damageDistribution, label='Damage Probability Distribution')

        
        self.ax.set_xlabel('Damage')
        self.ax.set_ylabel('Likelyhood')
        self.canvas.draw()

if __name__ == '__main__':
    root = customtkinter.CTk()
    root.geometry("800x550")
    aFont = customtkinter.CTkFont('Helvetica',12)
    app = DamagePlotter(root,aFont)
    root.mainloop()