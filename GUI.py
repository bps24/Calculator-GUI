#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
from tkinter import *
import tkinter.font as font


root = Tk()
root.title("Calculator")

f = font.Font(size=22)
e = Entry(root, width = 18, borderwidth = 5, font=f, justify='right')
e.grid(row=0, column=0, columnspan=4, padx=0, ipady=10)
operation = False
operator = None
fnum=0
snum=0

def button_click(number):
    global operation
    if operation:
        e.delete(0, END)
        operation = False
    first = e.get()
    if number == "." and "." in first:
        return
    e.delete(0, END)
    e.insert(0, str(first) + str(number))

def button_op(o):
    global operator ,operation, fnum, snum
    if operator:
        calc()
    operator = None
    fnum = float(e.get())
    if operation:
        e.delete(0, END)
        e.insert(0,str(fnum))
    operation = True
    operator = o

def button_pm():
    fnum = e.get()
    if fnum == "" or fnum==" " :
        return
    fnum = float(fnum)
    e.delete(0, END)
    e.insert(0,fnum *(-1))

def button_percent():
    fnum = e.get()
    if fnum == "" or fnum==" ":
        return
    fnum = float(fnum)
    e.delete(0, END)
    e.insert(0,fnum /(100))

def button_clear():
    e.delete(0, END)

def button_equal():
    global operator, operation, fnum, snum
    print("equalizing")
    if e.get() == '' or operator == None:
        return
    calc()
    fnum=0
    operator = None

def calc():
    global snum, operation, fnum
    snum = float(e.get())
    e.delete(0, END)
    print("FNUM: " + str(fnum) + " Operator: " + str(operator) + " SNUM: " + str(snum))
    if operator == 'Add':
        print('Added')
        button_add.configure(background='orange')
        button_add.grid(row =4, column = 3)
        fnum=fnum+snum
    elif operator == 'Sub':
        print("SUBBUE")
        fnum=fnum-snum
    elif operator == 'Mult':
        fnum=fnum*snum
    elif operator == 'Div':
        if snum == 0:
            e.insert(0, "Div By 0 Error")
            operation = True
        else:
            fnum=fnum/snum

    e.insert(0, fnum)
    



button_1 = Button(root, text='1', width=7, height=4 , activebackground = 'red', command = lambda: button_click(1))
button_2 = Button(root, text='2', width=7, height=4 , bg = 'red', command = lambda: button_click(2))
button_3 = Button(root, text='3', width=7, height=4 , bg = 'blue', command = lambda: button_click(3))
button_4 = Button(root, text='4', width=7, height=4 , bg = 'green',command = lambda: button_click(4))
button_5 = Button(root, text='5', width=7, height=4 , command = lambda: button_click(5))
button_6 = Button(root, text='6', width=7, height=4 , command = lambda: button_click(6))
button_7 = Button(root, text='7', width=7, height=4 , command = lambda: button_click(7))
button_8 = Button(root, text='8', width=7, height=4 , command = lambda: button_click(8))
button_9 = Button(root, text='9', width=7, height=4 , command = lambda: button_click(9))
button_0 = Button(root, text='0', width=15, height=4 , command = lambda: button_click(0))
button_dot = Button(root, text='.', width=7, height=4 , command = lambda: button_click("."))


button_add = Button(root, text='+', width=7, height=4 , command = lambda: button_op('Add'))
button_sub = Button(root, text='-', width=7, height=4 , command = lambda: button_op('Sub'))
button_mult = Button(root, text='x', width=7, height=4 , command = lambda: button_op('Mult'))
button_div = Button(root, text='÷', width=7, height=4 , command = lambda: button_op('Div'))
button_equal = Button(root, text='=', width=7, height=4 , command = button_equal)
button_clear = Button(root, text='C', width=7, height=4 , command = button_clear)
button_plusminus = Button(root, text='+/-', width=7, height=4 , command = button_pm)
button_percent = Button(root, text="%", width=7, height=4, command = button_percent )

button_1.grid(row= 4,column= 0)
button_2.grid(row= 4,column= 1)
button_3.grid(row= 4,column= 2)
button_4.grid(row= 3,column= 0)
button_5.grid(row= 3,column= 1)
button_6.grid(row= 3,column= 2)
button_7.grid(row= 2 ,column= 0)
button_8.grid(row= 2,column= 1)
button_9.grid(row= 2,column= 2)
button_0.grid(row= 5 ,column= 0, columnspan=2)
button_dot.grid(row= 5,column= 2)
button_add.grid(row= 4,column= 3)
button_sub.grid(row= 3,column= 3)
button_mult.grid(row= 2,column= 3)
button_div.grid(row= 1,column= 3)
button_equal.grid(row= 5 ,column= 3)
button_clear.grid(row= 1 ,column= 0)
button_plusminus.grid(row = 1, column =1)
button_percent.grid(row = 1, column=2)

root.mainloop()