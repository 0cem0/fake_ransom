import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("SYSTEM ALERT")
root.attributes("-fullscreen", True)
root.configure(bg="black")
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", lambda: None)

seconds = 30
running = True


def block_escape(event=None):
    if running:
        return "break"


root.bind_all("<Escape>", block_escape)
root.bind_all("<Control-KeyPress-c>", block_escape)
root.bind_all("<Alt-KeyPress-F4>", block_escape)
root.bind_all("<KeyPress>", block_escape)


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


def show_screamer():
    global running
    running = False

    root.unbind_all("<Escape>")
    root.unbind_all("<Control-KeyPress-c>")
    root.unbind_all("<Alt-KeyPress-F4>")
    root.unbind_all("<KeyPress>")
    root.protocol("WM_DELETE_WINDOW", root.destroy)

    screamer = tk.Toplevel(root)
    screamer.title("RANSOM END")
    screamer.attributes("-fullscreen", True)
    screamer.configure(bg="black")
    screamer.overrideredirect(True)

    big_text = tk.Label(
        screamer,
        text="😱\nBOOM!\nLOL",
        fg="red",
        bg="black",
        font=("Arial", 80, "bold")
    )
    big_text.pack(expand=True)

    screamer.after(3000, screamer.destroy)
    screamer.after(3000, root.destroy)


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
        show_screamer()


def escape(event=None):
    if running:
        return "break"
    root.destroy()


root.bind("<Escape>", escape)
root.bind("<Control-KeyPress-c>", escape)
root.bind("<Alt-KeyPress-F4>", escape)

timer()
root.mainloop()
