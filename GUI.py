
# -------------------------------------------
# IMPORT STUFF HERE
import main as functions
import tkinter as tk
# -------------------------------------------


def runProgram():
    n1_str = str(n1.get())
    n2_str = str(n2.get())
    n3_str = str(n3.get())
    n4_str = str(n4.get())
    n5_str = str(n5.get())
    i = functions.roll_dice(n1_str)
    t = functions.check_hits(n2_str, i)
    a = functions.roll_dice(t)
    b = functions.check_wounds(n4_str, n3_str, a)

    answer = functions.saving_throws(b, n5_str)
    text7 = tk.Label(root, text=str(answer), width=60, bg='snow', anchor='w')
    text7.grid(row=7, column=1)
    text7.focus_set()


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

text6 = tk.Label(root, text="This is the total amount of wounds and saves respectively: ", width=60, bg='snow', anchor='w')
text6.grid(row=7, column=0)
text6.focus_set()
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


# --------------------------------------------------ALL BUTTONS GO HERE--------------------------------

ComputeButton = tk.Button(root, text="Compute", command=runProgram, width=30, bg='snow')
ComputeButton.grid(row=6, column=1)
ComputeButton.focus_set()

ExitButton = tk.Button(root, text="Exit", command=root.destroy, width=30, bg='snow')
ExitButton.grid(row=8, column=0)
ExitButton.focus_set()

# -----------------------------------------------------------------------------------------------------

root.mainloop()

