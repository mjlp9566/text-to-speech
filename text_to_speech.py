import playsound as pl
from gtts import gTTS
import random
from tkinter import *
window=Tk()   #creating main window
window.geometry('300x100')  #window resolution

label=Label(window,text="Enter your word here",font=("didot",10))  #creating label widget
label.pack() #packing(adding) the label to the window

word=Entry(window,width=40,border=5) #creating input box
word.pack() #adding inputbox to the window

def voice():
    result=word.get() #getting the string value from th inputbox
    tts=gTTS(result)
    iint=random.randint(0,100)
    file_name="hello"+str(iint)+".mp3"
    tts.save(file_name)
    pl.playsound(file_name)
button=Button(window,text="Speak",command=voice,bg="orange",fg="white") #creating button and calling the voice function when the button is clicked
button.pack() #adding button to the window

window.mainloop()

    
