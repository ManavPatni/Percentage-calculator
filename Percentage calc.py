import tkinter as tk
from tkinter import Button, Grid, Label, Entry, StringVar


#Starting of the software interface 

window = tk.Tk()

#window title and icon
window.title("Percentage calc")
window.iconbitmap('D:\\manav\\Python\\Percentage calc\\logo.ico')
#main

#calculate button function & formual
def click():
    marks = float(marks1.get())
    totalmarks = float(totalmarks1.get())
    percent = marks / totalmarks * 100
    percent = str(percent)
    result_my.set("Your percentage is "+ percent + " %")

#input from user

#no. of subject
label_totalsub = Label(window, text="Enter number of subject").grid(padx=15,pady=5)
total = StringVar()
total = Entry(window, textvariable=total).grid(padx=15,pady=5)

#your marks
label_your_marks = Label(window, text="Enter your marks").grid(padx=15,pady=5)
marks1 = StringVar()
marks = Entry(window, textvariable=marks1).grid(padx=15,pady=5)


#total marks
label_totalmarks = Label(window, text="Enter total marks").grid(padx=15,pady=5)
totalmarks1 = StringVar()
totalmarks = Entry(window, textvariable=totalmarks1).grid(padx=15,pady=5)

#button
calculate = Button(window, text="Calculate", command=click).grid(padx=15,pady=5)

#result
result_my = StringVar()
label_result = Label(window, text="", textvariable = result_my).grid(padx=15,pady=5)


#resizing of the window 
canvas = tk.Canvas(window, width=300, height=20)
canvas.grid()

#endline text 
endline = tk.Label(window, text="COPYRIGHT © FIREFRAME - ALL RIGHTS RESERVED.")
endline.grid()

window.mainloop()

#Ending of the software interface

