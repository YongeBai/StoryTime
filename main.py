import tkinter as tk
import customtkinter as ct


from tkinter import ttk
from customtkinter import CTkButton, CTkEntry, CTkLabel, CTkFont
from commands import upload, callback

window = ct.CTk()
window.geometry("540x400")
window.resizable(False,False)
window.title("audible")
window.eval('tk::PlaceWindow . center')

epub_upload = CTkButton(window, text ='Upload an ePub (.epub)', command = lambda:upload())

link = CTkEntry(window, width=300)
label = CTkLabel(window, text="Paste Link to ePub:", anchor='center')
or_txt = CTkLabel(window, text="or ", anchor='center', font=CTkFont(slant="italic"))
submit = CTkButton(window, text="Submit", anchor='center', width=10, command=lambda:callback(link))

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


window.mainloop()