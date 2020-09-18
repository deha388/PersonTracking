import tkinter
import tkinter as tk
from mailbox import mbox
from random import random, randint
from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Personal Tracking System")
canvas = tk.Canvas(root, width=1250, height=850, )
canvas.pack()

rect = canvas.create_rectangle(1200, 700, 1, 1, fill="white", outline="black", width=3)

canvas.move(rect, 25, 25)

oval = canvas.create_oval(14, 14, 40, 40, fill="red", outline="black", width=2)
oval1 = canvas.create_oval(14, 14, 40, 40, fill="red", outline="black", width=2)
canvas.move(oval1, 0, 700)
oval2 = canvas.create_oval(14, 14, 40, 40, fill="red", outline="black", width=2)
canvas.move(oval2, 585, 695)
oval3 = canvas.create_oval(14, 14, 40, 40, fill="red", outline="black", width=2)
canvas.move(oval3, 1200, 695)
oval4 = canvas.create_oval(14, 14, 40, 40, fill="red", outline="black", width=2)
canvas.move(oval4, 586, 350)
oval5 = canvas.create_oval(14, 14, 40, 40, fill="red", outline="black", width=2)
canvas.move(oval5, 0, 348)
oval6 = canvas.create_oval(14, 14, 40, 40, fill="red", outline="black", width=2)
canvas.move(oval6, 1200, 348)
oval7 = canvas.create_oval(14, 14, 40, 40, fill="red", outline="black", width=2)
canvas.move(oval7, 1200, 0)
oval8 = canvas.create_oval(14, 14, 40, 40, fill="red", outline="black", width=2)
canvas.move(oval8, 586, 0)

a = canvas.create_line(40, 375, 1220, 375, dash=(5, 2))
a1 = canvas.create_line(312, 25, 312, 725, dash=(5, 2))
a2 = canvas.create_line(612, 25, 612, 720, dash=(5, 2))
a3 = canvas.create_line(915, 25, 915, 725, dash=(5, 2))

file1 = open('xyz.txt', 'r')
Lines = file1.readlines()

x = Text(root, height=5, width=5)
x.place(x=25,y=375)
y = Text(root, height=5, width=5)
y.place(x=95,y=375)
z = Text(root, height=5, width=5)
z.place(x=165,y=375)
t = Text(root, height=5, width=5)
t.place(x=235,y=375)



def onObjectClick(event,x):
    print('Got object click')
    messagebox.showinfo("PersonID", x)




for line in Lines:
    buttons = []
    global flag
    flag = False

    x = line.split(",", 1)[0]

    if x == '2728' or x == "2530" or x == '2323' or x == '2531' or x == '2674' in line:
        print("başarılı")
        if 'd0' in line:
            print(line)

            asd = str(x)

            randomh = randint(25, 90)
            randomw = randint(375, 455)
            x=Text(root,height=20, width=30)
            x.place(25, 90)

            my_button1 = Button(root, bg="black", command=lambda asd=asd: onObjectClick(asd), height=1, width=2)
            buttons.append(my_button1)
            for i in buttons:
                i.place(x=randomh, y=randomw)

        elif 'd1' in line:

            x = line.split(",", 1)[0]
            print(line)
            asd1 = str(x)
            randomh = randint(95, 160)
            randomw = randint(455, 535)

            # tkinter.Button(root,image=photo1, command=lambda: onObjectClick(asd1)).place(x=randomh, y=randomw)
            my_button1 = Button(root, bg="black", command=lambda asd1=asd1: onObjectClick(asd1),height=1,width=2)
            buttons.append(my_button1)
            for i in buttons:
                i.place(x=randomh, y=randomw)


        elif 'd2' in line:
            x = line.split(",", 1)[0]
            print(line)
            asd2 = str(x)
            randomh = randint(165, 230)
            randomw = randint(535, 615)

            my_button1 = Button(root, bg="black", command=lambda asd2=asd2: onObjectClick(asd2),height=1,width=2)
            buttons.append(my_button1)
            for i in buttons:
                i.place(x=randomh, y=randomw)

        elif 'd3' in line:
            x = line.split(",", 1)[0]
            print(line)
            asd3 = str(x)
            randomh = randint(235, 300)
            randomw = randint(615, 695)

            my_button1 = Button(root, bg="black", command=lambda asd3=asd3: onObjectClick(asd3),height=1,width=2)
            buttons.append(my_button1)
            for i in buttons:
                i.place(x=randomh, y=randomw)

        elif 'c0' in line:
            x = line.split(",", 1)[0]
            print(line)
            asd4 = str(x)
            randomh = randint(25, 90)
            randomw = randint(455, 535)

            my_button1 = Button(root, bg="black", command=lambda asd4=asd4: onObjectClick(asd4),height=1,width=2)
            buttons.append(my_button1)
            for i in buttons:
                i.place(x=randomh, y=randomw)

        elif 'c1' in line:
            x = line.split(",", 1)[0]
            print(line)
            asd5 = str(x)
            randomh = randint(95, 160)
            randomw = randint(455, 535)

            my_button1 = Button(root, bg="black", command=lambda asd5=asd5: onObjectClick(asd5),height=1,width=2)
            buttons.append(my_button1)
            for i in buttons:
                i.place(x=randomh, y=randomw)
        elif 'c2' in line:
            x = line.split(",", 1)[0]
            print(line)
            asd6 = str(x)
            randomh = randint(165, 230)
            randomw = randint(455, 535)

            my_button1 = Button(root, bg="black", command=lambda asd6=asd6: onObjectClick(asd6),height=1,width=2)
            buttons.append(my_button1)
            for i in buttons:
                i.place(x=randomh, y=randomw)
        elif 'c3' in line:
            x = line.split(",", 1)[0]
            print(line)
            asd7 = str(x)
            randomh = randint(235, 300)
            randomw = randint(455, 535)

            my_button1 = Button(root, bg="black", command=lambda asd7=asd7: onObjectClick(asd7),height=1,width=2)
            buttons.append(my_button1)
            for i in buttons:
                i.place(x=randomh, y=randomw)
        elif 'b0' in line:
            x = line.split(",", 1)[0]
            print(line)
            asd8 = str(x)
            randomh = randint(25, 90)
            randomw = randint(535, 615)

            my_button1 = Button(root, bg="black", command=lambda asd8=asd8: onObjectClick(asd8),height=1,width=2)
            buttons.append(my_button1)
            for i in buttons:
                i.place(x=randomh, y=randomw)
        elif 'b1' in line:
            x = line.split(",", 1)[0]
            print(line)
            asd9 = str(x)
            randomh = randint(95, 160)
            randomw = randint(535, 615)

            my_button1 = Button(root, bg="black", command=lambda asd9=asd9: onObjectClick(asd9),height=1,width=2)
            buttons.append(my_button1)
            for i in buttons:
                i.place(x=randomh, y=randomw)
        elif 'b2' in line:
            x = line.split(",", 1)[0]
            print(line)
            asd10 = str(x)
            randomh = randint(165, 230)
            randomw = randint(535, 615)

            my_button1 = Button(root, bg="black", command=lambda asd10=asd10: onObjectClick(asd10),height=1,width=2)
            buttons.append(my_button1)
            for i in buttons:
                i.place(x=randomh, y=randomw)
        elif 'b3' in line:
            x = line.split(",", 1)[0]
            print(line)
            asd11 = str(x)
            randomh = randint(235, 300)
            randomw = randint(535, 615)

            my_button1 = Button(root, bg="black", command=lambda asd11=asd11: onObjectClick(asd11),height=1,width=2)
            buttons.append(my_button1)
            for i in buttons:
                i.place(x=randomh, y=randomw)
        elif 'a0' in line:
            x = line.split(",", 1)[0]
            print(line)
            asd12 = str(x)
            randomh = randint(25, 85)
            randomw = randint(615, 695)

            my_button1 = Button(root, bg="black", command=lambda asd12=asd12: onObjectClick(asd12),height=1,width=2)
            buttons.append(my_button1)
            for i in buttons:
                i.place(x=randomh, y=randomw)
        elif 'a1' in line:
            x = line.split(",", 1)[0]
            print(line)
            asd13 = str(x)
            randomh = randint(95, 155)
            randomw = randint(615, 695)

            my_button1 = Button(root, bg="black", command=lambda asd13=asd13: onObjectClick(asd13),height=1,width=2)
            buttons.append(my_button1)
            for i in buttons:
                i.place(x=randomh, y=randomw)
        elif 'a2' in line:
            x = line.split(",", 1)[0]
            print(line)
            asd14 = str(x)
            randomh = randint(165, 225)
            randomw = randint(615, 695)

            my_button1 = Button(root, bg="black", command=lambda asd14=asd14: onObjectClick(asd14),height=1,width=2)
            buttons.append(my_button1)
            for i in buttons:
                i.place(x=randomh, y=randomw)
        elif 'a3' in line:
            x = line.split(",", 1)[0]
            print(line)
            asd15 = str(x)
            randomh = randint(235, 295)
            randomw = randint(615, 695)

            my_button1 = Button(root, bg="black", command=lambda asd15=asd15: onObjectClick(asd15),height=1,width=2)
            buttons.append(my_button1)
            for i in buttons:
                i.place(x=randomh, y=randomw)
        else:
            pass
    else:
        pass

root.mainloop()
