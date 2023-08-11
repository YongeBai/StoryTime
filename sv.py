import tkinter as tk
import customtkinter as ct
import sv_ttk

from tkinter import ttk
from customtkinter import CTkFont


window = tk.Tk()
window.geometry("540x400")
window.resizable(False,False)
window.title("audible")
window.eval('tk::PlaceWindow . center')

link = ttk.Entry(window)
submit = ttk.Button(window, text="Submit")
or_txt = ttk.Label(window, text=" or ", anchor='center', font=CTkFont(slant="italic"))

link.place(relx=.5,
           rely=.4,
           anchor='center'
          )
submit.place(relx=.5,
             rely=.52, 
             anchor='center'
            )

or_txt.place(relx=.5,
             rely=.60,
             anchor='center'
            )
sv_ttk.set_theme("dark")

window.mainloop()