import tkinter as tk
import customtkinter as ct
import sv_ttk

from tkinter import ttk
from commands import upload, callback, center

window = tk.Tk()
style = ttk.Style()

window.eval('tk::PlaceWindow . center')
window.geometry("640x500")
window.resizable(False,False)
window.title("audible")

sv_ttk.set_theme("dark")

label = ttk.Label(window, text="Paste Link to an ePub:", style="label.TLabel", anchor='center')
link = ttk.Entry(window, width=40)
submit = ttk.Button(window, text="Submit", style="Accent.TButton", command=lambda:callback(link))
or_txt = ttk.Label(window, text="or", anchor='center', style="label.TLabel" )
epub_upload = ttk.Button(window, text='Upload an ePub (.epub)', style="Accent.TButton", command=lambda:upload())

style.configure('submit.TButton', font=('Consolas', 12))
style.configure('label.TLabel', font=('Consolas', 16))

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
