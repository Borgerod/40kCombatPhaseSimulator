
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


root = tk.Tk()

root.title("Dice Rolling Simulator")
root.resizable(False, False)
root.geometry("1000x500")
root.configure(background='snow')

# -----------------THIS INCLUDES ALL OF THE TEXT THAT THE PROGRAM WILL DISPLAY------------------------
text = tk.Label(root, text="WELCOME TO MY DICE ROLLING MACHINE, ENTER VALUES BELOW", width=60, bg='snow', anchor='w'
                , font="Times 10 bold")
text.grid(row=0, column=0)
text.focus_set()

text1 = tk.Label(root, text="How many attacks are you rolling ", width=60, bg='snow', anchor='w')
text1.grid(row=1, column=0)
text1.focus_set()

text2 = tk.Label(root, text="What is the Ballistic skill/Weapon skill of the user ", width=60, bg='snow', anchor='w')
text2.grid(row=2, column=0)
text2.focus_set()

text3 = tk.Label(root, text="What is the strength of the user(modified with weapon) ", width=60, bg='snow', anchor='w')
text3.grid(row=3, column=0)
text3.focus_set()

text4 = tk.Label(root, text="What is the toughness of the target ", width=60, bg='snow', anchor='w')
text4.grid(row=4, column=0)
text4.focus_set()

text5 = tk.Label(root, text="What is the saving throw of the target ", width=60, bg='snow', anchor='w')
text5.grid(row=5, column=0)
text5.focus_set()

text6 = tk.Label(root, text="D", width=60, bg='snow', anchor='w')
text6.grid(row=6, column=0)
text6.focus_set()


text7 = tk.Label(root, text="AP", width=60, bg='snow', anchor='w')
text7.grid(row=7, column=0)
text7.focus_set()

result_row = tk.Label(root, text="Damage Dealt: ", width=60, bg='snow', anchor='w')
result_row.grid(row=8, column=0)
result_row.focus_set()

# ----------------------------------------------------------------------------------------------------------

# --------------------------------------------------ALL INPUT VALUES GO HERE--------------------------------
# The number at the end of the input corresponds to that of the number that follows the text objects above

n1 = tk.Entry(root, width=30)
n1.grid(row=1, column=1)
n1.focus_set()

n2 = tk.Entry(root, width=30)
n2.grid(row=2, column=1)
n2.focus_set()

n3 = tk.Entry(root, width=30)
n3.grid(row=3, column=1)
n3.focus_set()

n4 = tk.Entry(root, width=30)
n4.grid(row=4, column=1)
n4.focus_set()

n5 = tk.Entry(root, width=30)
n5.grid(row=5, column=1)
n5.focus_set()

n6 = tk.Entry(root, width=30)
n6.grid(row=6, column=1)
n6.focus_set()

n7 = tk.Entry(root, width=30)
n7.grid(row=7, column=1)
n7.focus_set()

# --------------------------------------------------ALL BUTTONS GO HERE--------------------------------

ComputeButton = tk.Button(root, text="Compute", command=runProgram, width=30, bg='snow')
ComputeButton.grid(row=9, column=1)
ComputeButton.focus_set()



# -----------------------------------------------------------------------------------------------------

root.mainloop()

