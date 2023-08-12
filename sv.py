import tkinter as tk
import customtkinter as ct
import sv_ttk

from tkinter import ttk
from customtkinter import CTkFont
from commands import upload, callback, center

window = tk.Tk()

window.eval('tk::PlaceWindow . center')
window.geometry("640x500")
window.resizable(False,False)
window.title("audible")

sv_ttk.set_theme("dark")

label = ttk.Label(window, text="Paste Link to an ePub:", font=CTkFont(slant="roman",size=20), anchor='center')
link = ttk.Entry(window, width=40)
submit = ttk.Button(window, text="Submit", command=lambda:callback(link))
or_txt = ttk.Label(window, text=" or ", anchor='center', font=CTkFont(slant="italic",size=16))
epub_upload = ttk.Button(window, text='Upload an ePub (.epub)', command=lambda:upload())

label.place(
            relx=.5,
            rely=.3, 
            anchor='center'
           )

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

epub_upload.place(relx=.5,
                  rely=.68, 
                  anchor='center'
                 )

center(window)
window.mainloop()
