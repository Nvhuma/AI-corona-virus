from tkinter import *
import os

coro = Tk()
coro.title("Coronavirus Tracker")
coro.geometry('800x500+200+100')
coro.configure(bg='#046173')

# Check if the icon file exists before setting it
icon_path = 'corona.ico'
if os.path.exists(icon_path):
    coro.iconbitmap(icon_path)
else:
    print(f"Warning: {icon_path} not found. Icon not set.")

#labels

mainlabel = Label(coro, text="Coronavirus Live Tracker", font=('Arial', 30, 'bold'), bg='#046173', fg='white'
				  , width=33, bd = 5)
mainlabel.place(x=0, y = 0)

label1 = Label(coro, text="Country Name", font=('Arial', 20, 'bold'), bg='#046173', fg='white', width=33, bd=5)

label1.place(x=15, y=100)

label2 = Label(coro, text="Download File in", font=('Arial', 20, 'bold'), bg='#046173', fg='white', width=33, bd=5)

label2.place(x=15, y=200)

cntdata = StringVar()

Entry1 = Entry(coro, textvariable = cntdata , font = ("times 20 bold", 20, "italic bold"), relief= RIDGE, bd = 2, width = 32)
Entry1.place(x=280, y=100)