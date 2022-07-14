#Author - Sahil Suman
from tkinter import *
import re
root = Tk()
root.title("Simple Calculator")
root.geometry("400x600")
root.resizable(width=False,height=False)
root.configure(bg = 'black')

#button_funcitonality
expression,equation = "",StringVar()
def onclick(num):
    global expression
    expression += str(num)
    equation.set(expression)
def rem_Zero(num):
    count = 0
    for i in range(len(num)):
        if num[i] == '0':
            count += 1
            continue
        else:
            if num[i] == ".":
                num = num[0:i+1].replace("0","") + num[i+1:len(num)+1]
                break
            if count >= 1:
                num = num[0:i+1].replace("0","") + num[i+1:len(num)+1]
                break
    return num
def myeval():
    global expression
    #saving_operator_sequence
    ops = ""
    for ele in expression:
        if ele not in "0123456789.":
            ops += ele
    #changing_expression_for_eval
    i = 0 
    temp = ""
    s_ls = re.split('\+|-|\*|\/',expression)
    for j in range(len(s_ls)-1):
        temp += rem_Zero(s_ls[j]) + ops[i]
        i+=1
    else:
        temp += rem_Zero(s_ls[len(s_ls)-1])
    #evaluation
    expression = temp
    total = str(eval(expression))
    equation.set(total)
    expression = ""
def clear():
    global expression
    expression = ""
    equation.set("")
def jaise():
    global expression
    expression = expression[:-1]
    equation.set(expression)

# def onkeypress(num):
#     global expression
#     expression += str(num)
#     equation.set(expression)

#UIElements
txtbox = Entry(root,font = ("Bahnschrift",30),bd=10,bg = "black",fg = 'light green',textvariable = equation)
b7 = Button(root,text = '7',font = ("Bahnschrift",30),width = 4,bd=5,command=lambda:onclick('7'),bg = "black",fg = 'red')
b8 = Button(root,text = '8',font = ("Bahnschrift",30),width = 4,bd=5,command=lambda:onclick('8'),bg = "black",fg = 'green')
b9 = Button(root,text = '9',font = ("Bahnschrift",30),width = 4,bd=5,command=lambda:onclick('9'),bg = "black",fg = 'blue')
bplus = Button(root,text = '+',font = ("Bahnschrift",30),width = 4,bd=5,command=lambda:onclick('+'),bg = "black",fg = 'yellow')
b4 = Button(root,text = '4',font = ("Bahnschrift",30),width = 4,bd=5,command=lambda:onclick('4'),bg = "black",fg = 'green')
b5 = Button(root,text = '5',font = ("Bahnschrift",30),width = 4,bd=5,command=lambda:onclick('5'),bg = "black",fg = 'blue')
b6 = Button(root,text = '6',font = ("Bahnschrift",30),width = 4,bd=5,command=lambda:onclick('6'),bg = "black",fg = 'red')
bmin = Button(root,text = '-',font = ("Bahnschrift",30),width = 4,bd=5,command=lambda:onclick('-'),bg = "black",fg = 'yellow')
b1 = Button(root,text = '1',font = ("Bahnschrift",30),width = 4,bd=5,command=lambda:onclick('1'),bg = "black",fg = 'blue')
b2 = Button(root,text = '2',font = ("Bahnschrift",30),width = 4,bd=5,command=lambda:onclick('2'),bg = "black",fg = 'red')
b3 = Button(root,text = '3',font = ("Bahnschrift",30),width = 4,bd=5,command=lambda:onclick('3'),bg = "black",fg = 'green')
bmul = Button(root,text = 'x',font = ("Bahnschrift",30),width = 4,bd=5,command=lambda:onclick('*'),bg = "black",fg = 'yellow')
b0 = Button(root,text = '0',font = ("Bahnschrift",30),width = 4,bd=5,command=lambda:onclick('0'),bg = "black",fg = 'yellow')
bclear = Button(root,text = 'C',font = ("Bahnschrift",30),width = 4,bd=5,command=clear,bg = "black",fg = 'yellow')
beq = Button(root,text = '=',font = ("Bahnschrift",30),width = 4,bd=5,command=myeval,bg = "black",fg = 'yellow')
bdiv = Button(root,text = '/',font = ("Bahnschrift",30),width = 4,bd=5,command=lambda:onclick('/'),bg = "black",fg = 'yellow')
bdot = Button(root,text = '.',font = ("Bahnschrift",30),width = 4,bd=5,command=lambda:onclick('.'),bg = "black",fg = 'yellow')
b_bk_sp = Button(root,text = '\u232b',font = ("Bahnschrift",30),width = 13,bd=5,command=lambda:jaise(),bg = "black",fg = 'yellow')

#placement
txtbox.place(x=1,y=10)
b7.place(x= 1 , y = 100)
b8.place(x= 101 , y = 100)
b9.place(x= 201 , y = 100)
bplus.place(x= 301 , y = 100)
b4.place(x= 1 , y = 200)
b5.place(x= 101 , y = 200)
b6.place(x= 201 , y = 200)
bmin.place(x= 301 , y = 200)
b1.place(x= 1 , y = 300)
b2.place(x= 101 , y = 300)
b3.place(x= 201 , y = 300)
bmul.place(x= 301 , y = 300)
b0.place(x= 1 , y = 400)
bclear.place(x= 101 , y = 400)
beq.place(x= 201 , y = 400)
bdiv.place(x= 301 , y = 400)
b_bk_sp.place(x = 0,y = 500)
bdot.place(x = 301,y = 500)
root.mainloop()