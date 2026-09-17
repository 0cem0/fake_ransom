import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("SYSTEM ALERT")
root.attributes("-fullscreen", True)
root.configure(bg="black")


title = tk.Label(
    root,
    text="⚠ YOUR FILES HAVE BEEN ENCRYPTED ⚠",
    fg="red",
    bg="black",
    font=("Arial", 36, "bold")
)
title.pack(pady=80)

message = tk.Label(
    root,
    text="Toutes vos données sont désormais inaccessibles.\n"
         "Ne paniquez pas... 😈",
    fg="white",
    bg="black",
    font=("Arial", 22)
)
message.pack(pady=30)

countdown = tk.Label(
    root,
    text="Temps restant : 00:30",
    fg="red",
    bg="black",
    font=("Arial", 28)
)
countdown.pack(pady=30)

seconds = 30

def timer():
    global seconds
    if seconds > 0:
        seconds -= 1
        countdown.config(text=f"Temps restant : 00:{seconds:02d}")
        root.after(1000, timer)
    else:
        messagebox.showinfo(
            "😂 TROLL",
            "Bonne nouvelle : tes fichiers n'ont absolument rien.\n"
            "C'était juste une blague !"
        )
        root.destroy()

def escape(event=None):
    root.destroy()

root.bind("<Escape>", escape)

timer()
root.mainloop() 
