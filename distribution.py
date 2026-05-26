import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import customtkinter
import dmgPlotter
from dmgPlotter import DamagePlotter

darkblue='#274f58'
rushred='#5c092d'
whitewords='#cdcdcd'
steelgrey='#353b45'
backgroundBlack='#20292f'

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

if __name__ == '__main__':
    root = customtkinter.CTk()
    root.geometry("800x550")
    aFont = customtkinter.CTkFont('Helvetica',12)
    app = DamagePlotter(root,aFont)
    root.mainloop()