
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

class CharacterSheet(ttk.Frame):
    '''
        ----------------- CHARACTER SHEET ------------------------
    '''

    def __init__(self, parent, sheet_name) -> None:
        super().__init__(parent)

        self.M = None
        self.T = None
        self.SV = None
        self.W = None
        self.LD = None
        self.OC = None
        self.create_character_sheet()


    def create_character_sheet(self):

        self.M = Widgets.label(self,"M")
        self.M.grid(row=0, column=1, padx=5,)
        self.M.focus_set()
        
        self.T = Widgets.label(self,"T")
        self.T.grid(row=0, column=2, padx=5,)
        self.T.focus_set()

        self.SV = Widgets.label(self,"SV")
        self.SV.grid(row=0, column=3, padx=5,)
        self.SV.focus_set()

        self.W = Widgets.label(self,"W")
        self.W.grid(row=0, column=4, padx=5,)
        self.W.focus_set()

        self.LD = Widgets.label(self,"LD")
        self.LD.grid(row=0, column=5, padx=5,)
        self.LD.focus_set()

        self.OC = Widgets.label(self,"OC")
        self.OC.grid(row=0, column=6, padx=5,)
        self.OC.focus_set()

        self.M = Widgets.entry(self) 
        self.M.grid(row=1, column=1, padx=5,)

        self.T = Widgets.entry(self)
        self.T.grid(row=1, column=2, padx=5,)

        self.SV = Widgets.entry(self)
        self.SV.grid(row=1, column=3, padx=5,)

        self.W = Widgets.entry(self)
        self.W.grid(row=1, column=4, padx=5,)

        self.LD = Widgets.entry(self)
        self.LD.grid(row=1, column=5, padx=5,)

        self.OC = Widgets.entry(self)
        self.OC.grid(row=1, column=6, padx=5,)


class WeaponSheet(ttk.Frame):
    '''
        ----------------- CHARACTER SHEET ------------------------
    '''

    def __init__(self, parent,sheet_name) -> None:
        super().__init__(parent)

        self.A = None
        self.BS = None
        self.S = None
        self.AP = None
        self.D = None
        # header = Widgets.h2(self, sheet_name)
        # header.grid(row=0, column=0, pady=(20,0))
        # print(type)
        # attacker_character_sheet = self.create_weapon_sheet()
        
        # header['style'], attacker_character_sheet['style'] = "style_name.TLabel", "style_name.TLabel"
        # attacker_character_sheet.grid(row=1, column=0, )

    def create_weapon_sheet(self):

        att_weapon_A = Widgets.label(self,"A")
        att_weapon_A.grid(row=0, column=1, padx=5,)
        att_weapon_A.focus_set()
        att_weapon_A = Widgets.entry(self)
        att_weapon_A.grid(row=1, column=1, padx=5,)

        att_weapon_BS = Widgets.label(self,"BS")
        att_weapon_BS.grid(row=0, column=2, padx=5,)
        att_weapon_BS.focus_set()
        att_weapon_BS = Widgets.entry(self)
        att_weapon_BS.grid(row=1, column=2, padx=5,)

        att_weapon_S = Widgets.label(self,"S")
        att_weapon_S.grid(row=0, column=3, padx=5,)
        att_weapon_S.focus_set()
        att_weapon_S = Widgets.entry(self)
        att_weapon_S.grid(row=1, column=3, padx=5,)

        att_weapon_AP = Widgets.label(self,"AP")
        att_weapon_AP.grid(row=0, column=4, padx=5,)
        att_weapon_AP.focus_set()
        att_weapon_AP = Widgets.entry(self)
        att_weapon_AP.grid(row=1, column=4, padx=5,)

        att_weapon_D = Widgets.label(self,"D")
        att_weapon_D.grid(row=0, column=5, padx=5,)
        att_weapon_D.focus_set()
        att_weapon_D = Widgets.entry(self)
        att_weapon_D.grid(row=1, column=5, padx=5,)


