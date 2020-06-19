from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pyttsx3 as pp
import speech_recognition as sr
import threading

engine = pp.init()
voices=engine.getProperty("voices")
print(voices)

engine.setProperty("voices",voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()

bot=ChatBot("BOT")

conv=["Hi",
      "What is your name?",
      "My name is Bot. ",
      "How are you?",
      "I am doing Great.",
      "Where do you live?",
      "I live in mumbai.",
      "How was your day?",
      "Thank you",
      "You are welcome",
      "That's good to here"

]

trainer = ListTrainer(bot)

trainer.train(conv)

main = Tk() 

#take_query : it takes audio as input from user and converts it to string
def take_query():
    s=sr.Recognizer()
    s.pause_threshold=1
    print("your bot is listening")
    with sr.Microphone() as m :
        try:
            audio=s.listen(m)
            query=s.recognize_google(audio,language='eng-in')
            print(query)
            textfd.delete(0,END)
            textfd.insert(0,query)
            ask()
        except Exception as e:
            print(e)
            print("Not Recognized")

def ask():
    query=textfd.get()
    answer=str(bot.get_response(query))
    msg.insert(END,"You: "+query)
    msg.insert(END,"Bot: "+answer)
    speak(answer)
    textfd.delete(0,END)
    msg.yview(END)


main.geometry("500x650")
main.title("CHATBOT")
img = PhotoImage(file = "D:\\Python3.7\\r.png")
photoL = Label(main,image=img)
photoL.pack(pady=5)
frame=Frame(main)
sc=Scrollbar(frame)

msg =Listbox(frame,width=80,height=20,yscrollcommand=sc.set)
msg.pack(side=LEFT,fill=BOTH,pady=10)
sc.pack(side=RIGHT,fill=Y)
frame.pack()
textfd=Entry(main)
textfd.pack(fill=X,pady=10)
btn=Button(main,text="Ask",command=ask)
btn.pack()

#creating a function 
def enter(event):
    btn.invoke()

#going to bind main window with enter key  

main.bind('<Return>',enter)

def rep_Listen():
    while True:
        take_query()

t=threading.Thread(target=rep_Listen)
t.start()

main.mainloop()