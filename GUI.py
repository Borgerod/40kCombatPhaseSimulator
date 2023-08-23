
# -------------------------------------------
# NEW IMPORTS
from subphase import SubPhase, Dice 

# IMPORT STUFF HERE
import main as functions
import tkinter as tk
# -------------------------------------------


def runProgram():
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
    num_wounds = functions.check_wounds(T, S, wound_rolls)
    num_not_saved, num_saved = functions.saving_throws(num_wounds, SV, AP)
    damage_delt = SubPhase().damage_roll(D, num_not_saved)
    damage_result = tk.Label(root, text=(damage_delt), width=10, bg='snow', fg='red')
    damage_result.grid(row=8, column=1)
    damage_result.focus_set()
    results = f"""
num_attacks: {num_attacks}
num_hits: {num_hits}
num_wounds: {num_wounds}
num_saved: {num_saved}
num_not_saved: {num_not_saved}
damage_delt: {damage_delt}"""
    print(results)


root = tk.Tk()

root.title("Dice Rolling Simulator")
root.resizable(False, False)
root.geometry("1000x500")
root.configure(background='snow')

# -----------------INTRO / HEADER ------------------------

# text = tk.Label(root, text="WELCOME TO MY DICE ROLLING MACHINE, ENTER VALUES BELOW", width=30, bg='snow', anchor='w'
#                 , font="Times 10 bold")
# text.grid(row=0, column=0)
# text.focus_set()

spacer=tk.Label().grid(row=1, column=0)
text = tk.Label(root, text="Attackers Character Sheet", width=30, bg='snow', anchor='w'
                , font="Times 10 bold")
text.grid(row=2, column=0)
text.focus_set()

spacer=tk.Label().grid(row=3, column=0)
text = tk.Label(root, text="Attackers weapon", width=30, bg='snow', anchor='w'
                , font="Times 10 bold")
text.grid(row=4, column=0)
text.focus_set()

spacer=tk.Label().grid(row=5, column=0)
text = tk.Label(root, text="Defenders Character Sheet", width=30, bg='snow', anchor='w'
                , font="Times 10 bold")
text.grid(row=6, column=0)
text.focus_set()

# -----------------ATTACKERS CHARACTER SHEET ------------------------
att_Char_1 = tk.Label(root, text="M", width=10, bg='snow', anchor='w')
att_Char_1.grid(row=1, column=1)
att_Char_1.focus_set()
att_Char_2 = tk.Label(root, text="T", width=10, bg='snow', anchor='w')
att_Char_2.grid(row=1, column=2)
att_Char_2.focus_set()
att_Char_3 = tk.Label(root, text="SV", width=10, bg='snow', anchor='w')
att_Char_3.grid(row=1, column=3)
att_Char_3.focus_set()
att_Char_4 = tk.Label(root, text="W", width=10, bg='snow', anchor='w')
att_Char_4.grid(row=1, column=4)
att_Char_4.focus_set()
att_Char_5 = tk.Label(root, text="LD", width=10, bg='snow', anchor='w')
att_Char_5.grid(row=1, column=5)
att_Char_5.focus_set()
att_Char_6 = tk.Label(root, text="OC", width=10, bg='snow', anchor='w')
att_Char_6.grid(row=1, column=6)
att_Char_6.focus_set()


# -----------------ATTACKERS WEAPON ------------------------
att_weapon_1 = tk.Label(root, text="A", width=10, bg='snow', anchor='w')
att_weapon_1.grid(row=3, column=1)
att_weapon_1.focus_set()
att_weapon_2 = tk.Label(root, text="BS", width=10, bg='snow', anchor='w')
att_weapon_2.grid(row=3, column=2)
att_weapon_2.focus_set()
att_weapon_3 = tk.Label(root, text="S", width=10, bg='snow', anchor='w')
att_weapon_3.grid(row=3, column=3)
att_weapon_3.focus_set()
att_weapon_4 = tk.Label(root, text="AP", width=10, bg='snow', anchor='w')
att_weapon_4.grid(row=3, column=4)
att_weapon_4.focus_set()
att_weapon_5 = tk.Label(root, text="D", width=10, bg='snow', anchor='w')
att_weapon_5.grid(row=3, column=5)
att_weapon_5.focus_set()


# -----------------DEFENDERS CHARACTER SHEET ------------------------
def_Char_1 = tk.Label(root, text="M", width=10, bg='snow', anchor='w')
def_Char_1.grid(row=5, column=1)
def_Char_1.focus_set()
def_Char_2 = tk.Label(root, text="T", width=10, bg='snow', anchor='w')
def_Char_2.grid(row=5, column=2)
def_Char_2.focus_set()
def_Char_3 = tk.Label(root, text="SV", width=10, bg='snow', anchor='w')
def_Char_3.grid(row=5, column=3)
def_Char_3.focus_set()
def_Char_4 = tk.Label(root, text="W", width=10, bg='snow', anchor='w')
def_Char_4.grid(row=5, column=4)
def_Char_4.focus_set()
def_Char_5 = tk.Label(root, text="LD", width=10, bg='snow', anchor='w')
def_Char_5.grid(row=5, column=5)
def_Char_5.focus_set()
def_Char_6 = tk.Label(root, text="OC", width=10, bg='snow', anchor='w')
def_Char_6.grid(row=5, column=6)
def_Char_6.focus_set()


# # -----------------THIS INCLUDES ALL OF THE TEXT THAT THE PROGRAM WILL DISPLAY------------------------
# text = tk.Label(root, text="WELCOME TO MY DICE ROLLING MACHINE, ENTER VALUES BELOW", width=10, bg='snow', anchor='w'
#                 , font="Times 10 bold")
# text.grid(row=0, column=0)
# text.focus_set()

# text1 = tk.Label(root, text="How many attacks are you rolling ", width=10, bg='snow', anchor='w')
# text1.grid(row=1, column=0)
# text1.focus_set()

# text2 = tk.Label(root, text="What is the Ballistic skill/Weapon skill of the user ", width=10, bg='snow', anchor='w')
# text2.grid(row=1, column=0)
# text2.focus_set()

# text3 = tk.Label(root, text="What is the strength of the user(modified with weapon) ", width=10, bg='snow', anchor='w')
# text3.grid(row=3, column=0)
# text3.focus_set()

# text4 = tk.Label(root, text="What is the toughness of the target ", width=10, bg='snow', anchor='w')
# text4.grid(row=3, column=0)
# text4.focus_set()

# text5 = tk.Label(root, text="What is the saving throw of the target ", width=10, bg='snow', anchor='w')
# text5.grid(row=5, column=0)
# text5.focus_set()

# text6 = tk.Label(root, text="D", width=10, bg='snow', anchor='w')
# text6.grid(row=5, column=0)
# text6.focus_set()


# text7 = tk.Label(root, text="AP", width=10, bg='snow', anchor='w')
# text7.grid(row=7, column=0)
# text7.focus_set()

result_row = tk.Label(root, text="Damage Dealt: ", width=10, bg='snow', anchor='w')
result_row.grid(row=8, column=0)
result_row.focus_set()

# ----------------------------------------------------------------------------------------------------------

# --------------------------------------------------ALL INPUT VALUES GO HERE--------------------------------
# The number at the end of the input corresponds to that of the number that follows the text objects above

att_chat_input_1 = tk.Entry(root, width=10)
att_chat_input_1.grid(row=2, column=1)
att_chat_input_1.focus_set()

att_chat_input_2 = tk.Entry(root, width=10)
att_chat_input_2.grid(row=2, column=2)
att_chat_input_2.focus_set()

att_chat_input_3 = tk.Entry(root, width=10)
att_chat_input_3.grid(row=2, column=3)
att_chat_input_3.focus_set()

att_chat_input_4 = tk.Entry(root, width=10)
att_chat_input_4.grid(row=2, column=4)
att_chat_input_4.focus_set()

att_chat_input_5 = tk.Entry(root, width=10)
att_chat_input_5.grid(row=2, column=5)
att_chat_input_5.focus_set()

att_chat_input_6 = tk.Entry(root, width=10)
att_chat_input_6.grid(row=2, column=6)
att_chat_input_6.focus_set()


# _________________________________ATTACKER WEAPON INPUT ___________________________________
att_weapon_input_1 = tk.Entry(root, width=10)
att_weapon_input_1.grid(row=4, column=1)
att_weapon_input_1.focus_set()

att_weapon_input_2 = tk.Entry(root, width=10)
att_weapon_input_2.grid(row=4, column=2)
att_weapon_input_2.focus_set()

att_weapon_input_3 = tk.Entry(root, width=10)
att_weapon_input_3.grid(row=4, column=3)
att_weapon_input_3.focus_set()

att_weapon_input_4 = tk.Entry(root, width=10)
att_weapon_input_4.grid(row=4, column=4)
att_weapon_input_4.focus_set()

att_weapon_input_5 = tk.Entry(root, width=10)
att_weapon_input_5.grid(row=4, column=5)
att_weapon_input_5.focus_set()

# ____________________________ DEFENDER CHARACTER SHEET INPUT ____________________________________
def_chat_input_1 = tk.Entry(root, width=10)
def_chat_input_1.grid(row=6, column=1)
def_chat_input_1.focus_set()

def_chat_input_2 = tk.Entry(root, width=10)
def_chat_input_2.grid(row=6, column=2)
def_chat_input_2.focus_set()

def_chat_input_3 = tk.Entry(root, width=10)
def_chat_input_3.grid(row=6, column=3)
def_chat_input_3.focus_set()

def_chat_input_4 = tk.Entry(root, width=10)
def_chat_input_4.grid(row=6, column=4)
def_chat_input_4.focus_set()

def_chat_input_5 = tk.Entry(root, width=10)
def_chat_input_5.grid(row=6, column=5)
def_chat_input_5.focus_set()

def_chat_input_6 = tk.Entry(root, width=10)
def_chat_input_6.grid(row=6, column=6)
def_chat_input_6.focus_set()











# n7 = tk.Entry(root, width=10)
# n7.grid(row=7, column=1)
# n7.focus_set()

# --------------------------------------------------ALL BUTTONS GO HERE--------------------------------

ComputeButton = tk.Button(root, text="Compute", command=runProgram, width=10, bg='snow')
ComputeButton.grid(row=9, column=1)
ComputeButton.focus_set()



# -----------------------------------------------------------------------------------------------------

root.mainloop()

