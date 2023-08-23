
class CharacterSheet():
    '''
        ----------------- CHARACTER SHEET ------------------------
    '''

    def __init__(self, parent, type, ) -> None:
        super().__init__(parent)
        if type=="weapon":
            create_weapon_sheet()

        # ttk.Label(self, background=style.bg, font=style.h1_, foreground='snow', text="Attacker Character Sheet").pack(expand=True, fill='both')
        self.place(x=.9,y=0.9,relwidth=0.6, relheight=.5)
        self.create_widget()


    def create_weapon_sheet(self):

        att_weapon_A = Widgets.label(self,"A")
        att_weapon_A.grid(row=0, column=1)
        att_weapon_A.focus_set()
        att_weapon_A = Widgets.entry(self)#Widgets.label()#(self, width=30)
        att_weapon_A.grid(row=1, column=1)

        att_weapon_BS = Widgets.label(self,"BS")# text="T", width=10, bg='snow', anchor='w')
        att_weapon_BS.grid(row=0, column=2)
        att_weapon_BS.focus_set()
        att_weapon_BS = Widgets.entry(self)#(self, width=30)
        att_weapon_BS.grid(row=1, column=2)

        att_weapon_S = Widgets.label(self,"S")# text="SV", width=10, bg='snow', anchor='w')
        att_weapon_S.grid(row=0, column=3)
        att_weapon_S.focus_set()
        att_weapon_S = Widgets.entry(self)#(self, width=30)
        att_weapon_S.grid(row=1, column=3)

        att_weapon_AP = Widgets.label(self,"AP")# text="W", width=10, bg='snow', anchor='w')
        att_weapon_AP.grid(row=0, column=4)
        att_weapon_AP.focus_set()
        att_weapon_AP = Widgets.entry(self)#(self, width=30)
        att_weapon_AP.grid(row=1, column=4)

        att_weapon_D = Widgets.label(self,"D")# text="LD", width=10, bg='snow', anchor='w')
        att_weapon_D.grid(row=0, column=5)
        att_weapon_D.focus_set()
        att_weapon_D = Widgets.entry(self)#(self, width=30)
        att_weapon_D.grid(row=1, column=5)










defender_sheet = CharacterSheet(type = "character")
attacker_sheet = CharacterSheet(type = "character")
weapon_sheet = CharacterSheet(type = "weapon")
