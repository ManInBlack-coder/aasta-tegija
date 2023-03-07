from tkinter import *
from tkinter import ttk
import tkinter as tk
import customtkinter

#____________________________________________

customtkinter.set_appearance_mode("Green")

#____________________________________________

def Riina_kommentaar():
    RIINA_ENTRY.delete(0,END)
    
    #if ans =


SKOOR = 0    

def Vastus():
    global SKOOR
    selection = var.get()
    label1 = ttk.Label(text="")
    
    if selection == 1:
        SKOOR += 5
        KONTROLL.delete(0,END)
        ans = "Õige"
        KONTROLL.insert(0,ans)
        label1.pack(side=RIGHT)
        label1.configure(text="Sinu skoorile liideti 5 punkti!",
                         font=("Arial",15),
                         foreground="green")
        label1.pack(side=RIGHT)
        label1.place(x=410,y=150)
        
    elif selection == 2:
        SKOOR -= 1
        KONTROLL.delete(0,END)
        ans = "Vale"
        KONTROLL.insert(0,ans)
        label1.configure(text="                                                   ")
        label1.configure(text="Sinu skoorilt kaotati 1 punkt!",
                         font=("Arial",15),
                         foreground="red")
        label1.pack(side=RIGHT)
        label1.place(x=410,y=300)
    
    elif selection == 3:
        SKOOR -= 1
        
        
        KONTROLL.delete(0,END)
        ans = "Vale"
        KONTROLL.insert(0,ans)
        label1.configure(text="Sinu skoorilt kaotati 1 punkt!",
                         font=("Arial",15),
                         foreground="red")
        label1.pack(side=RIGHT)
        label1.place(x=410,y=450)
    
    elif selection == 4:
        SKOOR -= 1
        
        KONTROLL.delete(0,END)
        ans = "Vale"
        KONTROLL.insert(0,ans)
        label1.configure(text="Sinu skoorilt kaotati 1 punkt!",
                         font=("Arial",15),
                         foreground="red")
        label1.pack(side=RIGHT)
        label1.place(x=410,y=600)
        
    
            
    print(SKOOR)
    if SKOOR in range(4):
        print(SKOOR.sum())
#____________________________________________


valikud = ["Kissell","Piim","Juust","Hapukoor"]

window = Tk()
window.geometry("1400x1000")
window.title("Bioloogia küsimus")

notebook = ttk.Notebook(window)
notebook.pack(fill="both")
#____________________________________________


label = ttk.Label(text="Milline neist ei sisalda laktoosi?",font=("Arial",25))
label.pack(side=LEFT)
label.place(x=150,y=50)


selected = tk.StringVar()
var = tk.IntVar()

KissellPhoto = PhotoImage(file="./Kissell3.png")
PiimPhoto = PhotoImage(file="./Piim2.png")
JuustPhoto = PhotoImage(file="./Juust2.png")
HapukoorPhoto = PhotoImage(file="./Hapukoor1.png")

r1 = ttk.Radiobutton(window,text="Kissell",value=1,variable=var,image= KissellPhoto)
r2 = ttk.Radiobutton(window,text="Piim",value=2,variable=var,image= PiimPhoto)
r3 = ttk.Radiobutton(window,text="Juust",value=3,variable=var, image = JuustPhoto)
r4 = ttk.Radiobutton(window,text="Hapukoor",value=4,variable=var,image = HapukoorPhoto)

r1.pack(side=LEFT)
r1.place(x=150,y=150)

r2.pack(side=LEFT)
r2.place(x=150,y=300)


r3.pack(side=LEFT)
r3.place(x=150,y=450)

r4.pack(side=LEFT)
r4.place(x=150,y=600)

KONTROLL = Entry(window,font=("Arial",25))
KONTROLL.pack(side=LEFT)
KONTROLL.place(x=80,y=850)

SUBMIT = Button(window,text="Vastus",font=("Impact"), command=Vastus)
SUBMIT.pack(side=RIGHT)
SUBMIT.place(x=80, y=800)

RIINA_SUBMIT = Button(window,text= "Küsi hinnangut",font=("Arial"),command = Riina_kommentaar)
RIINA_SUBMIT.pack(side= RIGHT)
RIINA_SUBMIT.place(x=800,y=350)

RIINA_ENTRY = Entry(window,font= ("Arial",25))
RIINA_ENTRY.pack(side=LEFT)
RIINA_ENTRY.place(x=800,y=450)

RiinaImage = PhotoImage(file ="./Õp_Riina1.png")
RiinaLabel = ttk.Label(window, image = RiinaImage)
PhotoImage(file = "./Õp_Riina1.png")
RiinaLabel.pack(side=RIGHT)
RiinaLabel.place(x=800,y=150)

window.mainloop()

