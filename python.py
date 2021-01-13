import tkinter
from tkinter import *
from tkinter import messagebox

root = tkinter.Tk()

def btn_is_clicked():
    messagebox.showinfo("info","THis is Info Window")
    

#title here 
root.title("Home Screen ")
root.resizable(0,0)
#geometry   (width x Height)
# root.geometry("400x400")
#height and Width of our home screen 
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

#our winows hegiht & width 
w=300
h=370

#define of axix of x & y 
x= int(ws/2-w/2)
y= int(hs/2-h/2)
# collculate data in geometry method 
data = str(w)+"x"+str(h)+"+"+str(x)+"+"+str(y)
#pass argument of geometry methid 
root.geometry(data)
#bg color
root.configure(background="#735328")


photo1 = PhotoImage(file ="P2.png")
#button here 
#btn1
btn1 = Button(
    root,
    # text="Button 1",
    bg="#000000",#bagground color
    fg="#ffffff",#text color 
    image = photo1,
    width=60,
    height = 40,
    command = btn_is_clicked,
).place(x=25,y=30)


#downText Here 
lableText = Label(
    root,
    text="Standerd \n Test",
    bg="#735328",
    fg = "#ffffff",
).place(x=25,y=80)

photo2 = PhotoImage(file ="P1.png")

#btn2
btn2 = Button(
    root,
    # text="Button 2",
    bg="#000000",#bagground color
    fg="#ffffff",#text color 
    image = photo2,
    width=60,
    height = 40,
    command = btn_is_clicked,
).place(x=120,y=30)

#down Text Here 
lableText = Label(
    root,
    text="Passive \n Test",
    bg="#735328",
    fg = "#ffffff"
).place(x=120,y=80)

photo3 = PhotoImage(file ="P2.png")

#btn3
btn3 = Button(
    root,
    # text="Button 3",
    bg="#000000",#bagground color
    fg="#ffffff",#text color 
    image = photo3,
    width=60,
    height = 40,
    command = btn_is_clicked,
).place(x=220,y=30)


#down Text Here 
lableText = Label(
    root,
    text="Record ",
    bg="#735328",
    fg = "#ffffff",
).place(x=220,y=80)


photo4 = PhotoImage(file ="P1.png")
# #btn4
btn4 = Button(
    root,
    # text="Button 4",
    bg="#000000",#bagground color
    fg="#ffffff",#text color 
    image = photo4,
    width=60,
    height = 40,
    command = btn_is_clicked,
).place(x=25,y=120)

#down Text Here 
lableText = Label(
    root,
    text="Calibration",
    bg="#735328",
    fg = "#ffffff",
).place(x=25,y=175)

photo5 = PhotoImage(file ="P2.png")
#btn5
btn5 = Button(
    root,
    # text="Button 5",
    bg="#000000",#bagground color
    fg="#ffffff",#text color 
    image = photo5,
    width=60,
    height = 40,
    command = btn_is_clicked,
).place(x=120,y=120)
#down Text Here 
lableText = Label(
    root,
    text="Setting ",
    bg="#735328",
    fg = "#ffffff",
).place(x=120,y=175)

photo6 = PhotoImage(file ="P1.png")
#btn6
btn6 = Button(
    root,
    # text="Button 6",
    bg="#000000",#bagground color
    fg="#ffffff",#text color 
    image = photo6,
    width=60,
    height = 40,
    command = btn_is_clicked,
).place(x=220,y=120)

#down Text Here 
lableText = Label(
    root,
    text="GPS",
    bg="#735328",
    fg = "#ffffff",
).place(x=220,y=175)

photo7 = PhotoImage(file ="P2.png")
#btn7
btn7 = Button(
    root,
    # text="Button 7",
    bg="#000000",#bagground color
    fg="#ffffff",#text color 
    image = photo7,
    width=60,
    height = 40,
    command = btn_is_clicked,
).place(x=25,y=220)
#down Text Here 
lableText = Label(
    root,
    text="3G/4G",
    bg="#735328",
    fg = "#ffffff",
).place(x=25,y=275)

photo8 = PhotoImage(file ="P1.png")
#btn8
btn8 = Button(
    root,
    # text="Button 8",
    bg="#000000",#bagground color
    fg="#ffffff",#text color 
    image = photo8,
    width=60,
    height = 40,
    command = btn_is_clicked,
).place(x=120,y=220)

#down Text Here 
lableText = Label(
    root,
    text="WIFI",
    bg="#735328",
    fg = "#ffffff",
).place(x=120,y=275)

#it main loop 
root.mainloop()