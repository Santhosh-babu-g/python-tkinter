import tkinter
from tkinter import StringVar,ttk,IntVar,scrolledtext,END,messagebox,filedialog,PhotoImage
from PIL import Image,ImageTk

# defining the window
root = tkinter.Tk()
# positioning the window to the center of the screen
w = 600
h = 600
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title('Notepad+')
root.resizable(0,0)

# defining the fonts and colors to be used in the program
text_color = '#fffacd'
menu_color = '#dbd9db'
root_color = '#6c809a'
root.config(bg=root_color)

# defining functions
def change_font(event: object):
    global my_font
    if font_opt.get() == 'none':
        my_font = (font_famil.get(),font_sz.get())
    else:
        my_font = (font_famil.get(),font_sz.get(),font_opt.get())

    input_text.config(font=my_font)

def new_note():
    question = messagebox.askyesno("New Note",'Are you sure you want to start a new note?')
    if question == 1:
        input_text.delete(1.0,END)

def close_note():
    question = messagebox.askyesno('Close Note','Are you sure you want to close your note?')
    if question == 1:
        root.destroy()

def save_note():
    save_name = filedialog.asksaveasfilename(initialdir='./',title='Save Note',filetypes=(('Text Files','.txt'),('All files','*.*')))
    with open(save_name, 'w')as f:
        f.write(font_famil.get()+'\n')
        f.write(str(font_sz.get())+'\n')
        f.write(font_opt.get()+'\n')

        f.write(input_text.get('1.0',END))

def open_note():
    open_name = filedialog.askopenfilename(initialdir='./',title='Open Note',filetypes=(('All files','*.*'),('Text Files','.txt')))
    with open(open_name, 'r') as f:

        font_famil.set(f.readline().strip())
        font_sz.set(int(f.readline().strip()))
        font_opt.set(f.readline().strip())

        change_font(1)

        text = f.read()
        input_text.insert('1.0',text)

# defining the layout of the window
menu_frame = tkinter.Frame(root, bg=menu_color)
text_frame = tkinter.Frame(root, bg=text_color)
menu_frame.pack(padx=5,pady=5)
text_frame.pack(padx=5,pady=5)


# defining (new,open,save,close,font_family,font_size,font_option) buttons with their properties and inserting them to the window
new_image = ImageTk.PhotoImage(Image.open('new.png'))
new_button = tkinter.Button(menu_frame, image=new_image, command=new_note)
new_button.grid(row=0,column=0,padx=5,pady=5)

open_image = ImageTk.PhotoImage(Image.open('open.png'))
open_button = tkinter.Button(menu_frame, image=open_image, command=open_note)
open_button.grid(row=0,column=1,padx=5,pady=5)

save_image = ImageTk.PhotoImage(Image.open('save.png'))
save_button = tkinter.Button(menu_frame, image=save_image,command=save_note)
save_button.grid(row=0,column=2,padx=5,pady=5)

close_image = ImageTk.PhotoImage(Image.open('close.png'))
close_button = tkinter.Button(menu_frame, image=close_image, command=close_note)
close_button.grid(row=0,column=3,padx=5,pady=5)

# defining the font family dropdown
font_fam = ['Arial','Calibri','Cambria','Candara','MS Gothic','Segoe UI','Fixedsys','Terminal','Modern','Roman','Script','Courier','MS Serif','Small Fonts','Marlett','Tahoma','Verdana','Webdings']
font_famil = StringVar()
font_family = tkinter.OptionMenu(menu_frame, font_famil, *font_fam,command=change_font)
font_family.config(width=10)
font_famil.set(font_fam[0])
font_family.grid(row=0,column=4,padx=5,pady=5)

# defining the font size dropdown
font_siz = [8,9,10,11,12,14,16,18,20,24,26,28,36,48,72]
font_sz = IntVar()
font_size = tkinter.OptionMenu(menu_frame, font_sz,*font_siz,command=change_font)
font_sz.set(font_siz[4])
font_size.grid(row=0,column=5,padx=5,pady=5)

# defining font style dropdown
font_op = ['none','bold','italic']
font_opt = StringVar()
font_option = tkinter.OptionMenu(menu_frame, font_opt,*font_op,command=change_font)
font_opt.set(font_op[0])
font_option.grid(row=0,column=6,padx=5,pady=5)

# declaring a global font variable
my_font = (font_famil.get(),font_sz.get())

# defining a input box with scrollbar
input_text = tkinter.scrolledtext.ScrolledText(text_frame,width=1000,height=100,bg=text_color,font=my_font)
input_text.pack()

root.mainloop()