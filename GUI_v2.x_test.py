
# -------------------------------------------
# NEW IMPORTS
from subphase import SubPhase, Dice 
import re
import traceback

# IMPORT STUFF HERE
from prefs import style, Widgets
import main as functions
import tkinter as tk
from tkinter import ttk
import customtkinter
from sheets import CharacterSheet, WeaponSheet

# -------------------------------------------

def seperator(self):
    separator = ttk.Separator(self, orient='horizontal')
    separator.pack(fill='x', pady=20)


def computeButton(self):
    compute_button = customtkinter.CTkButton(self, text="Compute", command=runCalculator, )

    # compute_button=tk.Button(
    #     self, text="Compute", 
    #     command=runCalculator, 
    #     width=10, 
    #     font=style.h2_, 

    #     foreground=style.fg_highlight,
        
    #     background=style.bg, 
    #     highlightcolor=style.fg,
    #     highlightbackground = style.bg_highlight,
    #     justify="left",

        # )
    compute_button.pack(anchor="w", padx=160,)
    compute_button.focus_set()



class App(tk.Tk):


    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        # main setup (Builds root of Framework)
        self.root


        # title 
        Widgets.h1(self, "Warhammer 40K Combat Phase Simulator").pack()#Title(self)
        
        seperator(self)
        
        # Character sheet input
        # for i in [['Attacker Character Sheet', 'character'],['Attacker Weapon Sheet', "weapon"], ['Defender Character Sheet','character'],]:
        #     sheet_name, type = i[0],i[1]
        #     sheetrow = WidgetFrame(self, sheet_name, type)
        #     sheetrow['style'] = "style_name.TLabel"
        #     sheetrow.pack(anchor='w')
        
        sheet_name = "attacker character sheet"
        # header = Widgets.h2(self, sheet_name)
        # header.grid(row=0, column=0, pady=(20,0))
        att_sheet = CharacterSheet(self, sheet_name).pack(anchor='w')
        
        # header['style'], att_sheet['style'] = "style_name.TLabel", "style_name.TLabel"
        # att_sheet.grid(row=1, column=0, )
        # att_sheet.pack()
        # att_weapon = WeaponSheet(self, "attacker weapon sheet").create_weapon_sheet()
        # att_weapon.pack()
        # def_sheet = CharacterSheet(self, "defender character sheet").create_character_sheet()
        # def_sheet.pack()
        # seperator(self)

        # Compute button
        computeButton(self)

        # Run
        self.run
    
    @property
    def root(self):
        self.title('Warhammer 40K Combat Phase Simulator')
        self.resizable(True, True)
        self.geometry("1000x500")
        self.configure(background=style.bg)
        style_ref = ttk.Style()
        style_ref.configure("style_name.TLabel", background=style.bg)

    @property
    def run(self):   
        self.mainloop() 



class Title(ttk.Frame):
     def __init__(self, parent) -> None:
        super().__init__(parent)
        Widgets.h1(self, "Warhammer 40K Combat Phase Simulator")#ttk.Label(self, background=style.bg, font=style.h1_, foreground='snow', text="Attacker Character Sheet")

        # ttk.Label(self, padding=20, background=style.bg, font=style.h1_, foreground=style.fg, text="Warhammer 40K Combat Phase Simulator").pack(expand=True, fill='both')
        # self.pack()


class WidgetFrame(ttk.Frame):
    def __init__(self, parent, sheet_name, type) -> None:
        super().__init__(parent)
        # self.columnconfigure()
        
        header = Widgets.h2(self, sheet_name)
        header.grid(row=0, column=0, pady=(20,0))
        print(type)
        attacker_character_sheet = CharacterSheet(self, type)
        
        header['style'], attacker_character_sheet['style'] = "style_name.TLabel", "style_name.TLabel"
        attacker_character_sheet.grid(row=1, column=0, )
        # self.grid(row=0, column=0)
        # self.grid(row=1, column=0)
        

def runCalculator():
    a_input = str(n1.get())
    BS = str(n2.get()).replace("+", "")
    S = str(n3.get())
    T = str(n4.get())
    SV = str(n5.get()).replace("+", "")
    D =  str(n6.get()).replace("+", "")
    AP = str(n7.get()).replace("-", "")
    num_attacks = SubPhase().attack_roll(a_input)
    #i = functions.roll_dice(a_input)
    num_hits = functions.check_hits(BS, num_attacks)
    
    wound_rolls = functions.roll_dice(num_hits)
    print(wound_rolls)
    num_wounds = functions.check_wounds(T, S, wound_rolls)
    num_not_saved, num_saved = functions.saving_throws(num_wounds, SV, AP)
    damage_delt = SubPhase().damage_roll(D, num_not_saved)
    damage_result = tk.Label(root, text=(damage_delt), width=60, bg='snow', fg='red')
    damage_result.grid(row=8, column=1)
    damage_result.focus_set()
    results = f"""
num_attacks: {num_attacks}
num_hits: {num_hits}, 
num_wounds: {num_wounds},  {wound_rolls}
num_saved: {num_saved}
num_not_saved: {num_not_saved}
damage_delt: {damage_delt}"""
    print(results)



        # button_1 = ttk.Button(self, text="Button 1")
        # toggle_frame = ttk.Frame(self)
        # entry = ttk.Entry(self)
        
        # # create grid 
        # self.columnconfigure((0,1,2), weight=1, uniform='a')
        # self.rowconfigure((0,1,2,4,5), weight=1, uniform='a')

        # # place elements in grid 
        # button_1.grid(row=0, column=0, sticky='nwse', columnspan=2)

        # # entry layout
        # entry.place(relx=0.5, rely=0.95, relheight=0.9, anchor='center')


    # def __init__(self, ):
    #     self.M = self.getElement("M")
    #     self.T = self.getElement("T")
    #     self.SV = self.getElement("SV")
    
    #     self.W = self.getElement("W")
    #     self.LD = self.getElement("LD")
    #     self.OC = self.getElement("OC")























# class FrameWork(ttk.Frame):
#     def __init__(self, parent) -> None:
#         super().__init__(parent)
#         self.build()
#         # self.title = Title(self)

#     def build(self):
#         frame = self.frame()

#         Title(self)
#         frame = self.pack(expand=True, fill='both')   

    



#     def frame(self):
#         frame = ttk.Label(self, background='red').pack(expand=True, fill='both')# text="M", width=10, anchor='w')
          
#         return frame



# n1 = Widgets.label()#(self, width=30)
# n1.grid(row=1, column=1)
# n1.focus_set()
# att_M = Widgets.label(self,"M")# text="M", width=10, bg='snow', anchor='w')
# att_M.grid(row=1, column=1)
# att_M.focus_set()











# class CharacterSheet(ttk.Frame):
#     '''
#         ----------------- CHARACTER SHEET ------------------------
#     '''


#     def __init__(self, ):
#         self.M = self.getElement("M")
#         self.T = self.getElement("T")
#         self.SV = self.getElement("SV")
#         self.W = self.getElement("W")
#         self.LD = self.getElement("LD")
#         self.OC = self.getElement("OC")

#     def getElement(self, name): #Grid Item
#         # name=self.getVarName(var)
#         grid_item = Widgets.label(self,"M")# text=name, width=10, bg='snow', anchor='w')
#         grid_item.grid(row=1, column=1)
#         grid_item.focus_set()
#         return grid_item

#     def getVarName(self, var):
#         ''' returns the original variable name from __init__'''
#         return re.compile(r'\((.*?)\).*$').search(traceback.extract_stack()[-3][3]).groups()[0].strip("self.")
    
        
#     def foo(self, ):
#         # for i in æ
#         self.getElement(self.M)
#         '''
#             some_descr
#         '''
#         pass


if __name__ == '__main__':
    App()
    
