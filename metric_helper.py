import tkinter
from tkinter import ttk,END,NORMAL,DISABLED

# defining the window
root = tkinter.Tk()
root.title('Metric Helper')
root.resizable(0,0)

# defining the colors and fonts
field_font = ('Cambria',10)
bg_color = '#ABFAA9'
button_color = '#82D173'
root.config(bg=bg_color)

# defining functions:
def split(word):
    return [char for char in word]


def converts(s):
    # initialization of string to ""
    new = ""

    # traverse in the string
    for x in s:
        new += x

        # return string
    return new

def hi(x):
    y = x * 0
    return y

def convert():
    metric_value = {
        'femto':10**-15,
        'pico':10**-12,
        'nano':10**-9,
        'micro':10**-6,
        'milli':10**-3,
        'centi':10**-2,
        'deci':10**-1,
        'base value':10**0,
        'deca':10**1,
        'hecto':10**2,
        'kilo':10**3,
        'mega':10**6,
        'giga':10**9,
        'tera':10**12,
        'peta':10**15
    }
    output_field.delete(0,END)

    try:
        start_value = float(input_field.get())
        hi(start_value)
    except Exception:
        output_field.config(state=NORMAL)
        output_field.insert(0, "ERROR")
        output_field.config(state=DISABLED)
    start_value = float(input_field.get())
    start_prefix = input_Combobox.get()
    end_prefix = output_Combobox.get()

    base_value = start_value*metric_value[start_prefix]
    end_value = base_value/metric_value[end_prefix]
    out_value = str(end_value)
    output_value = split(out_value)
    outs_value = converts(output_value)
    if len(outs_value) > 21:
        outss_value = outs_value[:21]
    else:
        outss_value = outs_value
    output_field.config(state=NORMAL)
    output_field.insert(0,str(outss_value))
    output_field.config(state=DISABLED)

    input_Combobox.config(state=DISABLED)
    output_Combobox.config(state=DISABLED)

def clear():
    input_field.delete(0,END)
    output_field.config(state=NORMAL)
    output_field.delete(0,END)
    output_field.config(state=DISABLED)
    input_Combobox.set('base value')
    output_Combobox.set('base value')
    input_Combobox.config(state=NORMAL)
    output_Combobox.config(state=NORMAL)

def de_focus(event):
    event.widget.master.focus_set()

# defining frames for layout
input_label = tkinter.Label(root, text='INPUT:', bg=bg_color)
empty_label = tkinter.Label(root, text='  ', bg=bg_color)
output_label = tkinter.Label(root, text='OUTPUT:', bg=bg_color)

input_label.grid(row=0,column=0,pady=(10,0))
empty_label.grid(row=0,column=1)
output_label.grid(row=0,column=2, pady=(10,0))

# defining input and output fields
input_field = tkinter.Entry(root, width=20, font=field_font,borderwidth=3,justify='right')
output_field = tkinter.Entry(root, width=20, font=field_font,borderwidth=3,state=DISABLED,cursor='arrow',disabledforeground='black',justify='right')
equal_label = tkinter.Label(root, text='=', font=field_font, bg=bg_color)

input_field.grid(row=1,column=0,padx=10,pady=(0,10))
equal_label.grid(row=1,column=1,padx=10,pady=10)
output_field.grid(row=1,column=2,padx=10,pady=(0,10))

if type(input_field.get()) == 'string':
     output_field.config(state=NORMAL)
     output_field.insert(0, "ERROR")
     output_field.config(state=DISABLED)

# defining a list which contains the values for the dropdowns
metric_list = ['femto','pico','nano','micro','milli','centi','deci','base value','deca','hecto','kilo','mega','giga','tera','peta']

# defining the combobox
input_Combobox = ttk.Combobox(root, value=metric_list, font=field_font, justify='center',state='readonly')
output_Combobox = ttk.Combobox(root, value=metric_list, font=field_font, justify='center',state='readonly')
to_label = tkinter.Label(root, text='to', font=field_font, bg=bg_color)

# adding features into the combobox
root.option_add('*TCombobox*Listbox.selectBackground', '#71c9ce')
root.option_add('*TCombobox*Listbox.selectForeground', 'black')
input_Combobox.bind("<FocusIn>", de_focus)
output_Combobox.bind("<FocusIn>", de_focus)

input_Combobox.grid(row=2,column=0,padx=10,pady=10)
to_label.grid(row=2,column=1,padx=10, pady=10)
output_Combobox.grid(row=2,column=2,padx=10,pady=10)

input_Combobox.set('base value')
output_Combobox.set('base value')

# Standard dropdown box code commented for reference:
# input_choice = StringVar()
# output_choice = StringVar()
# input_dropdown = tkinter.OptionMenu(root, input_choice, *metric_list)
# output_dropdown = tkinter.OptionMenu(root, output_choice, *metric_list)


# defining buttons
convert_button = tkinter.Button(root, text='Convert', bg=button_color, font=field_font, command=convert)
convert_button.grid(row=3,column=0,columnspan=3,padx=10,pady=10,ipadx=50)

clear_button = tkinter.Button(root, text='Clear', bg=button_color, font=field_font, command=clear)
clear_button.grid(row=4,column=0,columnspan=3,padx=10,pady=10,ipadx=50)

# calling the mainloop for the window
root.mainloop()
