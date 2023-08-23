from tkinter import ttk
import tkinter as tk
import customtkinter



class Style:
    def __init__(self) -> None:
        self.bg_highlight = "DarkSeaGreen1"
        self.fg_highlight = "light blue"
        self.bg = "grey21"
        self.bg2 = "grey50"
        self.fg = "snow"
        self.h1_ = ('Helvetica', 16)
        self.h2_ = ('Helvetica', 12)
        self.text = ()

class Widgets(ttk.Frame):
    def __init__(self, parent) -> None:
        super().__init__(parent)


        
class Widgets:
        
    def h1(self, text):
        return ttk.Label(self, padding=20, background=style.bg, font=style.h1_, foreground='snow', text=text)#.pack(expand=True, fill='both')

    def h2(self, text):
        return ttk.Label(self, background=style.bg, font=style.h2_, foreground=style.fg, text=text, anchor='w')#.pack(expand=True, fill='both')

    def label(self, text):
        return tk.Label(self, background=style.bg, foreground='snow', text=text, width=10,)

    def entry(self):
        return customtkinter.CTkEntry(self, bg_color =style.bg, fg_color=style.bg2, width=60, text_color=style.fg,border_width=0,  )


        # return tk.Label(self, background=style.bg2, font=style.h1_, foreground='snow', text=text, width=10, anchor='w')
        # return tk.Entry(self, background=style.bg2, foreground='snow', width=10)
    
    # def button(self, text):
        # return tk.Button(self, text=text, command=runCalculator, width=10, bg='snow')

    

style = Style()
# widgets = Widgets()


