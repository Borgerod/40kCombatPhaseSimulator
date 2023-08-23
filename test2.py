
# -------------------------------------------
# NEW IMPORTS
from subphase import SubPhase, Dice 
import re
import traceback

# IMPORT STUFF HERE
import main as functions
import tkinter as tk
from tkinter import ttk

# -------------------------------------------

class App(tk.Tk):


    def __init__(self, ):#title, size):
        super().__init__()
        self.title('Warhammer 40K Combat Phase Simulator')
        self.resizable(True, True)
        self.geometry("1000x500")
        self.configure(background='snow')
        
        # main setup (Builds root of Framework)
        # self.root

        self.menu = Menu(self)
        
        # Run
        self.run
    
    @property
    def root(self):
        self.title('Warhammer 40K Combat Phase Simulator')
        self.resizable(True, True)
        self.geometry("1000x500")
        self.configure(background='snow')


    @property
    def run(self):   
        self.mainloop() 

class Menu(ttk.Frame):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        # att_Char_1 = tk.Label(self, text="M", width=10, bg='snow', anchor='w')
        ttk.Label(self, background='red').pack(expand=True, fill='both')# text="M", width=10, anchor='w')
        self.pack()
        # att_Char_1.grid(row=1, column=1)
        # att_Char_1.focus_set()




if __name__ == '__main__':
    App()