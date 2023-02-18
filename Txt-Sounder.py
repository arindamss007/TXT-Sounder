"""
MIT License

Copyright (c) 2023 Arindam Saha

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from tkinter import BOTTOM, INSERT, LEFT, RAISED, RIGHT, Entry, Label, OptionMenu, StringVar, Button, Frame, Text, ttk
import tkinter
import gtts
from playsound import playsound

# UI frames & tkinter window
top = tkinter.Tk()
top.geometry("550x225")
frame = Frame(top)
frame.pack()
frame2=Frame(top)
frame2.pack()
frame3=Frame(top)
frame3.pack()
frame4=Frame(top)
frame4.pack()
frame5=Frame(top)
frame5.pack()

#Temporary and Parmanent Variables
txt = Text()
txt1=""
txt2 = """NOTE* : It is possible to take a while to Generate audio file according to Size."""
txt3= StringVar()
txt3.set("us")
text=""

#voice accents
accents = [ "us", 
            "com.au", 
            "co.in", 
            "co.uk", 
            "ca", 
            "ie", 
            "co.za" ]

#TOP Level Heading -> TXT-Sounder
var1 = StringVar()
label1 = Label( frame, textvariable=var1, relief=RAISED, height=5, width=70)
var1.set("TxT-SOUNDER v0.1")
label1.pack(side="top")

#Status updating Label
var3 = StringVar()
label3 = Label( frame2, textvariable=var3, relief=RAISED, height=2, width=70)
label3.pack()

#Label to indicate
var2 = StringVar()
label2 = Label( frame3, textvariable=var2, relief=RAISED, height=1, width=18)
var2.set("Enter your text :")
label2.pack(side=LEFT)

#Entry for input text
E1 = Entry(frame3,width=52)
E1.pack(side=LEFT)

#Function for text to audio generation
def generate() :
    txt1 = E1.get()
    txt ="Generating...."
    var3.set(txt)
    audio = gtts.gTTS(text=txt1, lang="en", tld=txt3.get())
    audio.save("myaudio.mp3")
    txt="Generated Succsessfully...."
    var3.set(txt)

#Play the saved audio
def play() :
    txt="Playing....."
    var3.set(txt)
    playsound("myaudio.mp3")
    txt="Played Successful...."
    var3.set(txt)

#clear function to clear the Entry
def clear() :
    E1.delete(first=0,last=100000)

# *Note instruction Lebel
var4 = StringVar()
var4.set(txt2)
label4 = Label( frame4, textvariable=var4, relief=RAISED, anchor="center", height=2, width=70)
label4.pack()

#Generate Button
button1 = Button(frame5,text ="GENERATE", height=1, width=8, justify="center", command=generate)
button1.pack(side=RIGHT)

#Play button
button2 = Button(frame5,text ="PLAY", height=1, width=5,justify="center", command=play)
button2.pack(side=RIGHT)

#Clear
button3 = Button(frame5, text ="CLEAR", height=1, width=5,justify="center", command=clear)
button3.pack(side=LEFT)

# Combo Box for selection of Voice Accent
opt = StringVar()
new_cb = ttk.Combobox(frame5, textvariable=opt)

new_cb['values'] = (accents)
new_cb['state'] = 'readonly'
new_cb.current(2)
new_cb.pack(fill=tkinter.X, padx=5, pady=5)

def accent_change(event) :
    text = new_cb.get()
    txt3.set(text)

new_cb.bind('<<ComboboxSelected>>', accent_change)

top.mainloop()