from ctypes import windll
from curses import window
from tkinter import Tk, Label
window = Tk()
window.title("Digital Clock")
window.geometry("600x300")

label = Label(window, text="Welcome!", font=("Arial Black", 78, "bold"), bg="steelblue", fg="white")
label.pack(pady=100)

window.mainloop()