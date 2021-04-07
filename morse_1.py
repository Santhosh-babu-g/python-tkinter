import tkinter
from tkinter import IntVar,END,DISABLED,NORMAL
from playsound import playsound
from PIL import Image,ImageTk

# defining window
root = tkinter.Tk()
root.title('Morse Code Translator')
root.geometry('500x350')
root.resizable(0,0)

# defining fonts and colors
button_font = ('SimSun',10)
root_color = '#778899'
frame_color = '#dcdcdc'
button_color = '#c0c0c0'
text_color = '#f8f8ff'
mor_font = ('Dela Gothic One',16)
root.config(bg=root_color)

# defining functions:
def convert():
    if language.get() == 1:
        get_morse()
    elif language.get() == 2:
        get_english()

def get_morse():
    morse_code = ""

    text = input_text.get('1.0',END)
    text = text.lower()

    err = ['~', '`', '#', '%', '^', '*', '{', '}', '[', ']', '\\', '<', '>']

    for i in err:
        if i in text:
            output_text.config(state=NORMAL)
            output_text.insert('1.0', 'These are undefined  ~  `  #  %  ^  *  {  }  [  ]  <  >  \\  in Morse-Code')
            output_text.config(state=DISABLED)
            return

    for letter in text:
        if letter not in english_to_morse.keys():
            text = text.replace(letter, '')

    word_list = text.split(' ')

    for word in word_list:
        letters = list(word)
        for letter in letters:
            morse_char = english_to_morse[letter]
            morse_code += morse_char
            morse_code += ' '
        morse_code += '|'
    output_text.config(state=NORMAL)
    output_text.insert('1.0', morse_code)
    output_text.config(state=DISABLED)



def get_english():
    english = ""

    text = input_text.get('1.0',END)

    for letter in text:
        if letter not in morse_to_english.keys():
            text = text.replace(letter,'')

    word_list = text.split('|')

    for word in word_list:
        letters = word.split(' ')
        for letter in letters:
            english_char = morse_to_english[letter]
            english += english_char
        english += ' '
    output_text.config(state=NORMAL)
    output_text.insert('1.0',english)
    output_text.config(state=DISABLED)


def clear():
    input_text.delete('1.0',END)
    output_text.config(state=NORMAL)
    output_text.delete('1.0',END)
    output_text.config(state=DISABLED)

def play():
    global text
    if language.get() == 1:
        text = output_text.get("1.0", END)
    elif language.get() == 2:
        text = input_text.get("1.0", END)


    for value in text:
        if value == ".":
            playsound('dot.mp3')
            root.after(100)
        elif value == "-":
            playsound('dash.mp3')
            root.after(200)
        elif value == " ":
            root.after(300)
        elif value == "|":
            root.after(700)

def show_guide():
    global morse
    global guide

    guide = tkinter.Toplevel()
    guide.overrideredirect(1)
    guide.geometry('350x380+'+str(root.winfo_x()+508)+'+'+str(root.winfo_y()))
    guide.config(bg='#5F6F7E')

    mor_label = tkinter.Label(guide,text='Morse Code Guide :',font=mor_font,bg='#5F6F7E',fg='white')
    mor_label.pack(padx=10,pady=(5,0),ipadx=5)

    morse = ImageTk.PhotoImage(Image.open('morse_chart.jpg'))
    label = tkinter.Label(guide, image=morse, bg=frame_color)
    label.pack(padx=10,pady=8,ipadx=5,ipady=5)

    close_button = tkinter.Button(guide,text='Close',font=button_font,bg=button_color,command=hide_guide)
    close_button.pack(padx=10,ipadx=40)

    guide_button.config(state=DISABLED)

def hide_guide():
    guide_button.config(state=NORMAL)
    guide.destroy()



# defining a dictionary for english to morse conversion
english_to_morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
                    'f': '..-.', 'g': '--.', 'h': '....','i': '..', 'j': '.---',
                    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
                    'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
                    'u': '..--', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
                    'z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                    '0': '-----', ' ':' ', '|':'|', "":"", '@':'.--.-.', '&':'.-...',
                    '(':'-.--.', ')':'-.--.-', '+':'.-.-.', '=':'-...-', ':':'---...',
                    "'":".----.", '"':'.-..-.', ',':'--..--', '/':'-..-.', '?':'..--..',
                    '$':'...-..-', '-':'-....-', '_':'..--.-', '.':'.-.-.-', '!':'-.-.--',
                    ';':'-.-.-.'}

# these are undefined  ~  `  #  %  ^  *  {  }  [  ]  <  >  \ in morse code.


# dictionary for morse to english conversion:
morse_to_english = dict([(value, key) for key, value in english_to_morse.items()])

# defining layout
input_frame = tkinter.LabelFrame(root,bg=frame_color)
output_frame = tkinter.LabelFrame(root,bg=frame_color)
input_frame.pack(padx=16,pady=(16,8))
output_frame.pack(padx=16,pady=(8,16))

# adding input box and buttons:
input_text = tkinter.Text(input_frame,height=8,width=30,bg=text_color)
input_text.grid(row=0,column=1,rowspan=3,padx=5,pady=5)

# using IntVar() to give specific values for thr radio buttons
language = IntVar()
language.set(1)
morse_button = tkinter.Radiobutton(input_frame,text='English ---> Morse Code',variable=language,value=1,font=button_font,bg=frame_color)
english_button = tkinter.Radiobutton(input_frame,text='Morse Code ---> English',variable=language,value=2,font=button_font,bg=frame_color)
guide_button = tkinter.Button(input_frame,text='Guide',font=button_font,bg=button_color,command=show_guide)

morse_button.grid(row=0,column=0,pady=(13,0))
english_button.grid(row=1,column=0)
guide_button.grid(row=2,column=0,padx=5,ipadx=62)

# defining output box
output_text = tkinter.Text(output_frame,height=8,width=30,bg=text_color,state=DISABLED,cursor='arrow')
output_text.grid(row=0,column=1,rowspan=4,padx=5,pady=5)

# defining additional buttons and inserting them into the window
convert_button = tkinter.Button(output_frame,text='Convert',font=button_font,bg=button_color,command=convert)
play_button = tkinter.Button(output_frame,text='Play',font=button_font,bg=button_color,command=play)
clear_button = tkinter.Button(output_frame,text='Clear',font=button_font,bg=button_color,command=clear)
quit_button = tkinter.Button(output_frame,text='Quit',font=button_font,bg=button_color,command=root.destroy)

convert_button.grid(row=0,column=0,padx=10,ipadx=55)
play_button.grid(row=1,column=0,padx=10,sticky='WE')
clear_button.grid(row=2,column=0,padx=10,sticky='WE')
quit_button.grid(row=3,column=0,padx=10,sticky='WE')

# calling the mainloop of the window
root.mainloop()
