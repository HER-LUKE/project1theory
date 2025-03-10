##Luke Herron
##2/13/2025
##Assignment P1

import tkinter as tk
from tkinter import ttk

def show_french_number(number):
    french_numbers = {1: "Un", 2: "Deux", 3: "Trois", 4: "Quatre", 5: "Cinq"} ##Dictionary for french numbers
    lbl_french.config(text=french_numbers[number])

def close_app():
    root.destroy()

root = tk.Tk()  ##Main Windows
root.title("French Numbers") ##Title
root.geometry("500x300") ##Window Size
root.resizable(False, False)  ##Disable min-max
root.attributes('-toolwindow', True)  ##Removed min-maxs buttons

lbl_instructions = ttk.Label(root, text="Click a number to see the French word:") ##Instructions label
lbl_instructions.pack(pady=10) ##Stacks label in main window with 10 pixels vertical padding

lbl_french = ttk.Label(root, text="", font=("Arial", 14)) ##Number Display lmber
lbl_french.pack(pady=20) ##Stacks label in main window 20 pixels of vertical padding

btn_frame = tk.Frame(root) ##Create frame for buttons
btn_frame.pack() ##Pack frame into window

for i in range(1, 6): #Loops between 1-5
    btn = ttk.Button(btn_frame, text=str(i), command=lambda i=i: show_french_number(i)) ##Puts buttons in the frame for each i(1-5)
    ##also giving lambda command for when buttons is pressed to call show_french_number function
    btn.grid(row=0, column=i-1, padx=5, pady=5) ##Places buttons on spefic row, and changes column with i

btn_exit = ttk.Button(root, text="Exit", command=close_app) ##Exits main window and closes app
btn_exit.pack(pady=10) ##packs exit button into window and pads it with 10 pixels

root.mainloop() ##run Application
