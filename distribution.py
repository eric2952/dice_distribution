import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import Frame
from tkinter import IntVar
from tkinter import StringVar

darkblue='#274f58'
rushred='#5c092d'
whitewords='#cdcdcd'
steelgrey='#353b45'
backgroundBlack='#20292f'


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


class DamagePlotter:
    def __init__(self,root):
        self.root = root
        root.title('Predict Damage Output')

        self.DC_var = IntVar()
        self.SavingThrow = IntVar()
        self.DiceCount = IntVar()
        self.SidedDice = IntVar()
        self.rollMode = StringVar()
        

        inputFrame = Frame(self.root)
        DCinput = tk.Entry(inputFrame,text='DC Input',textvariable=self.DC_var)
        SaveBonusInput = tk.Entry(inputFrame,text='Save Throw Bonus',textvariable=self.SavingThrow)
        numberofDiceInput = tk.Entry(inputFrame,text='Number of Dice',textvariable=self.DiceCount)
        diceSidesInput = tk.Entry(inputFrame,text='Number of Sides',textvariable=self.SidedDice)

        attackButton = tk.Checkbutton(inputFrame,text='Saving Throw',variable=self.rollMode,onvalue='Save',offvalue='Attack')
        attackButton.deselect()

        attackButton.grid(row=1,column=0)
        DCinput.grid(row=0,column=0)
        SaveBonusInput.grid(row=0,column=1)
        numberofDiceInput.grid(row=0,column=2)
        diceSidesInput.grid(row=0,column=3)
        
        
        inputFrame.pack()

        load_button = tk.Button(self.root, text='Generate Odds', command=self.update_plot)
        load_button.pack(padx=10,pady=10)


        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master = self.root)
        self.widget = self.canvas.get_tk_widget()
        self.widget.pack(padx=10, pady=10)

        self.df = None

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
    root = tk.Tk()
    app = DamagePlotter(root)
    root.mainloop()