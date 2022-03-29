import socket
import threading
import datetime, time
from tkinter import *

now = datetime.datetime.now()


PORT = 5050
SERVER = "192.168.1.215"
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"

client = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
client.connect(ADDRESS)


def window_nick():
    windownick = Tk()
    windownick.title("Введение ника")
    windownick.resizable(0, 0)
    windownick.geometry('270x110')

    nicklabel = Label(text='Введите ник:', font='Arial 14')
    nicklabel.place(anchor=NW, x=10, y=10)

    usernick = StringVar()

    nickentry = Entry(windownick, width=15, font='Arial 16', textvariable=usernick)
    nickentry.place(anchor=W, x=10, y=55)

    def next_window():
        nickname = usernick.get()
        windownick.destroy()
        window_chat(nickname)

    nickbut = Button(windownick, text='Ввести', font='Arial 11', command=next_window)
    nickbut.place(anchor=E, x=260, y=55)

    windownick.mainloop()


def window_chat(nickname):


    def save_msg():
        chatlog = open("chatlog.txt", "a+")
        timeuser = now.strftime("[%d.%m/%H:%M] ")
        chatlog.write(timeuser + nickname + ": " + message.get() + "\n")
        chatlog.close
        usermsg.delete(0, END)

    def update_chat():
        chatexit = open("chatlog.txt", "r")
        chat = chatexit.read()
        chatbox.delete(1.0, END)
        chatbox.insert(1.0, chat)
        chatexit.close()
        windowchat.after(250, update_chat)

    windowchat = Tk()
    windowchat.title("Общий чат")
    windowchat.resizable(0, 0)
    windowchat.geometry('600x400')

    chatbox = Text(width=15, height=10, font='Arial 16')
    chatbox.place(anchor=NW, x=10, y=10, relheight=0.85, relwidth=0.92, width=1)

    scroll = Scrollbar(command=chatbox.yview)
    scroll.place(anchor=NE, x=590, y=10, relheight=0.85)

    chatbox.config(yscrollcommand=scroll.set)

    message = StringVar()
    usermsg = Entry(windowchat, textvariable=message, width=10, font='Arial 16')
    usermsg.place(anchor=SW, x=10, y=390, relwidth=0.80)

    sendmsg = Button(windowchat, text="Отправить", font='Arial 11', command=save_msg)
    sendmsg.place(anchor=SE, x=590, y=390)

    windowchat.after(250, update_chat)
    windowchat.mainloop()


window_nick()