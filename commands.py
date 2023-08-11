from tkinter.filedialog import askopenfile 

#extract epub from url
def callback(link): 
    print(link.get()) 

def upload():
    path = askopenfile(mode='r', filetypes=[('ePub File', '*epub')])