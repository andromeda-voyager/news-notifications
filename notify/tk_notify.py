import tkinter as tk
from tkinter import *
import webbrowser
import guardian

def callback(url):
    webbrowser.open_new_tab(url)


def update():
    articles = guardian.check_for_new()
    for a in articles:
        notify(a)
    root.after(300000, update)


root = tk.Tk()
root.attributes("-alpha", 0.0)  # For icon
root.iconify()
w = 400  # width for the Tk root
h = 100  # height for the Tk root
ws = root.winfo_screenwidth()  # width of the screen
hs = root.winfo_screenheight()  # height of the screen

x = (0.99 * ws) - (w)
y = 0.04 * hs
root.withdraw()


def notify(article):
    window = tk.Toplevel(root, bg="white")
    window.geometry("600x100")  # Whatever size
    window.overrideredirect(1)  # Remove border
    window.geometry("%dx%d+%d+%d" % (w, h, x, y))
    link = Label(
        window,
        text=article.get_title(),
        justify=LEFT,
        wraplength=350,
        bg="white",
        cursor="hand2",
    )
    link.pack(fill="both", expand=True, padx=25, pady=25)
    close = tk.Button(
        window,
        text="x",
        bg="white",
        bd=0,
        font=("Sans", "10", "bold"),
        highlightthickness=0,
        activeforeground="red",
        command=lambda: window.destroy(),
    )
    close.update()
    wb = close.winfo_width()
    close.place(relx=1.0, y=0, anchor="ne")
    link.pack()
    link.bind("<Button-1>", lambda e: callback(article.get_link()))
    window.after(1, window.update())


update()
root.mainloop()
