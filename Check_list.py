import tkinter
from tkinter import END,ANCHOR
import os

# defining the window
root = tkinter.Tk()
root.title('Check List')
root.geometry('480x400')
root.resizable(0,0)

# defining the fonts and colors to be used in the program
my_font = ('Noto Sans', 12)
root_color = '#05B2DC'
button_color = '#FEE440'
root.config(bg=root_color)

# defining functions
def add_item():
    my_listbox.insert(END,input_entry.get())
    input_entry.delete(0,END)

def remove_item():
    my_listbox.delete(ANCHOR)

def clear_list():
    my_listbox.delete(0,END)

def save_list():
    with open('checklist.txt', 'w')as f:
        list_tuple = my_listbox.get(0,END)
        for item in list_tuple:
            if item.endswith('\n'):
                f.write(item)
            else:
                f.write(item + '\n')

def open_list():
    try:
        with open('checklist.txt', 'r') as f:
            for line in f:
                my_listbox.insert(END,line)
    except:
        return

def delete_list():
    global f
    if os.path.exists("checklist.txt"):
        os.remove("checklist.txt")


# defining the layout of the window
input_frame = tkinter.Frame(root,bg=root_color)
output_frame = tkinter.Frame(root,bg=root_color)
button_frame = tkinter.Frame(root,bg=root_color)

input_frame.pack()
output_frame.pack()
button_frame.pack()


# adding input box and buttons:
input_entry = tkinter.Entry(input_frame, width=38, borderwidth=3, font=my_font)
list_add_button = tkinter.Button(input_frame, text='Add Item', borderwidth=2, font=my_font, bg=button_color, command=add_item)

input_entry.grid(row=0,column=0,padx=10,pady=10)
list_add_button.grid(row=0,column=1,padx=10,pady=10,ipadx=5)


# adding a scrollbar for the textbox and connecting it with the list box
my_scrollbar = tkinter.Scrollbar(output_frame)
my_listbox = tkinter.Listbox(output_frame, width=48, height=15, borderwidth=3, font=my_font, yscrollcommand=my_scrollbar.set)

my_scrollbar.config(command=my_listbox.yview)
my_listbox.grid(row=0,column=0)
my_scrollbar.grid(row=0,column=1, sticky='NS')


# defining the buttons:
list_remove_button = tkinter.Button(button_frame, text='Remove Item',borderwidth=2,font=my_font,bg=button_color, command=remove_item)
list_clear_button = tkinter.Button(button_frame, text='Clear List',borderwidth=2,font=my_font, bg=button_color, command=clear_list)
list_save_button = tkinter.Button(button_frame, text='Save List',borderwidth=2,font=my_font, bg=button_color, command=save_list)
list_quit_button = tkinter.Button(button_frame, text='Quit',borderwidth=2,font=my_font, bg=button_color, command=root.destroy)
list_delete_button = tkinter.Button(button_frame, text='Delete List',borderwidth=2,font=my_font, bg=button_color, command=delete_list)

list_remove_button.grid(row=0,column=0,padx=2,pady=10,ipadx=5)
list_clear_button.grid(row=0,column=1,padx=2,pady=10,ipadx=5)
list_save_button.grid(row=0,column=2,padx=2,pady=10,ipadx=5)
list_delete_button.grid(row=0,column=3,padx=2,pady=10,ipadx=5)
list_quit_button.grid(row=0,column=4,padx=2,pady=10,ipadx=6)


# calling the open function to try to open a text file if it exists:
open_list()

# calling the mainloop of the window
root.mainloop()