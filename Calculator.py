import tkinter
from tkinter import RIGHT,END,DISABLED,NORMAL

# defining the window
root = tkinter.Tk()
root.title('Calculator')
root.geometry('325x440')
root.resizable(0,0)

# defining the colors and fonts
root_color = '#FDE74C'
button_color = '#F93943'
func_color = '#80A4ED'
num_color = '#9BC53D'
button_font = ('Arial',20,)
display_font = ('Arial',30)
root.config(bg=root_color)

# defining functions of buttons
def submit_number(number):
    display.config(state=NORMAL)
    display.insert(END, number)
    display.config(state=DISABLED)

    if '.' in display.get():
        decimal_button.config(state=DISABLED)

def operate(operator):
    clear_button.config(state=DISABLED)
    global first_number
    global operation

    operation = operator
    first_number = display.get()
    display.config(state=NORMAL)
    display.delete(0,END)
    display.config(state=DISABLED)

    add_button.config(state=DISABLED)
    subtract_button.config(state=DISABLED)
    multiply_button.config(state=DISABLED)
    divide_button.config(state=DISABLED)
    exponent_button.config(state=DISABLED)
    inverse_button.config(state=DISABLED)
    square_button.config(state=DISABLED)

    decimal_button.config(state=NORMAL)

def equal():
    global value
    if operation == 'add':
        value = float(first_number)+float(display.get())
    elif operation == 'subtract':
        value = float(first_number) - float(display.get())
    elif operation == 'multiply':
        value = float(first_number) * float(display.get())
    elif operation == 'divide':
        if display.get() == '0':
            value = 'ERROR'
        else:
            value = float(first_number) / float(display.get())
    elif operation == 'exponent':
        value = float(first_number) ** float(display.get())

    display.config(state=NORMAL)
    display.delete(0,END)
    display.insert(0,value)
    display.config(state=DISABLED)
    clear_button.config(state=NORMAL)
    enable_buttons()

def enable_buttons():
    x = display.get()
    if '.' in x:
        decimal_button.config(state=DISABLED)
    else:
        decimal_button.config(state=NORMAL)
    add_button.config(state=NORMAL)
    subtract_button.config(state=NORMAL)
    multiply_button.config(state=NORMAL)
    divide_button.config(state=NORMAL)
    exponent_button.config(state=NORMAL)
    inverse_button.config(state=NORMAL)
    square_button.config(state=NORMAL)

def clear():
    display.config(state=NORMAL)
    display.delete(0,END)
    display.config(state=DISABLED)
    clear_button.config(state=DISABLED)
    enable_buttons()

def inverse():
    global valu
    if display.get() == '0':
        valu = 'ERROR'
    else:
        valu = 1/float(display.get())

    clear_button.config(state=NORMAL)
    display.config(state=NORMAL)
    display.delete(0,END)
    display.insert(0,valu)
    display.config(state=DISABLED)

def square():
    val = float(display.get()) ** 2
    display.config(state=NORMAL)
    display.delete(0,END)
    display.insert(0,val)
    display.config(state=DISABLED)
    clear_button.config(state=NORMAL)

def negate():
    va = -1 * float(display.get())
    display.config(state=NORMAL)
    display.delete(0, END)
    display.insert(0, va)
    display.config(state=DISABLED)

# defining frames for layout
display_frame = tkinter.Frame(root)
button_frame = tkinter.Frame(root)
display_frame.pack(pady=(0,20))
button_frame.pack()

# defining and packing the entry widget
display = tkinter.Entry(display_frame, width=50, font=display_font, bg='#C5DECD',borderwidth=5, justify=RIGHT,state=DISABLED,disabledforeground='Black',cursor='arrow')
display.pack(padx=8,pady=8)

# defining buttons
clear_button = tkinter.Button(button_frame,text='Clear',bg=button_color,font=button_font,command=clear,state=DISABLED)
quit_button = tkinter.Button(button_frame,text='Quit',bg=button_color,font=button_font,command=root.destroy)

# defining arithmetic buttons
inverse_button = tkinter.Button(button_frame,text='1/x',bg=func_color,font=button_font, command=inverse)
square_button = tkinter.Button(button_frame,text='x^2',bg=func_color,font=button_font, command=square)
exponent_button = tkinter.Button(button_frame,text='x^n',bg=func_color,font=button_font,command=lambda:operate('exponent'))
divide_button = tkinter.Button(button_frame,text='/',bg=func_color,font=button_font,command=lambda:operate('divide'))
multiply_button = tkinter.Button(button_frame,text='*',bg=func_color,font=button_font,command=lambda:operate('multiply'))
subtract_button = tkinter.Button(button_frame,text='-',bg=func_color,font=button_font,command=lambda:operate('subtract'))
add_button = tkinter.Button(button_frame,text='+',bg=func_color,font=button_font,command=lambda:operate('add'))
equal_button = tkinter.Button(button_frame,text='=',bg=button_color,font=button_font,command=equal)
decimal_button = tkinter.Button(button_frame,text='.',bg=num_color,font=button_font,command=lambda:submit_number('.'))
negate_button = tkinter.Button(button_frame,text='+/-',bg=num_color,font=button_font, command=negate)

# defining numbers as buttons
nine_button = tkinter.Button(button_frame,text='9',font=button_font,bg=num_color,command=lambda:submit_number(9))
eight_button = tkinter.Button(button_frame,text='8',font=button_font,bg=num_color,command=lambda:submit_number(8))
seven_button = tkinter.Button(button_frame,text='7',font=button_font,bg=num_color,command=lambda:submit_number(7))
six_button = tkinter.Button(button_frame,text='6',font=button_font,bg=num_color,command=lambda:submit_number(6))
five_button = tkinter.Button(button_frame,text='5',font=button_font,bg=num_color,command=lambda:submit_number(5))
four_button = tkinter.Button(button_frame,text='4',font=button_font,bg=num_color,command=lambda:submit_number(4))
three_button = tkinter.Button(button_frame,text='3',font=button_font,bg=num_color,command=lambda:submit_number(3))
two_button = tkinter.Button(button_frame,text='2',font=button_font,bg=num_color,command=lambda:submit_number(2))
one_button = tkinter.Button(button_frame,text='1',font=button_font,bg=num_color,command=lambda:submit_number(1))
zero_button = tkinter.Button(button_frame,text='0',font=button_font,bg=num_color,command=lambda:submit_number(0))

# packing the buttons into layout
# first row
clear_button.grid(row=0,column=0,columnspan=2,sticky='WE')
quit_button.grid(row=0,column=2,columnspan=2,sticky='WE')

# second row
inverse_button.grid(row=1,column=0,pady=1,sticky='WE')
square_button.grid(row=1,column=1,pady=1,sticky='WE')
exponent_button.grid(row=1,column=2,pady=1,sticky='WE')
divide_button.grid(row=1,column=3,pady=1,sticky='WE')
# third row
seven_button.grid(row=2,column=0,pady=1,sticky='WE',ipadx=20)
eight_button.grid(row=2,column=1,pady=1,sticky='WE',ipadx=20)
nine_button.grid(row=2,column=2,pady=1,sticky='WE',ipadx=20)
multiply_button.grid(row=2,column=3,pady=1,sticky='WE',ipadx=20)
# fourth row
four_button.grid(row=3,column=0,pady=1,sticky='WE',ipadx=20)
five_button.grid(row=3,column=1,pady=1,sticky='WE',ipadx=20)
six_button.grid(row=3,column=2,pady=1,sticky='WE',ipadx=20)
subtract_button.grid(row=3,column=3,pady=1,sticky='WE',ipadx=20)
# fifth row
one_button.grid(row=4,column=0,pady=1,sticky='WE',ipadx=20)
two_button.grid(row=4,column=1,pady=1,sticky='WE',ipadx=20)
three_button.grid(row=4,column=2,pady=1,sticky='WE',ipadx=20)
add_button.grid(row=4,column=3,pady=1,sticky='WE',ipadx=20)
# sixth row
negate_button.grid(row=5,column=0,pady=1,sticky='WE',ipadx=14)
zero_button.grid(row=5,column=1,pady=1,sticky='WE',ipadx=20)
decimal_button.grid(row=5,column=2,pady=1,sticky='WE',ipadx=20)
equal_button.grid(row=5,column=3,pady=1,sticky='WE',ipadx=20)

# Calling the window's mainloop
root.mainloop()
