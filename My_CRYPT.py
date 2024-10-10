from tkinter import *
from tkinter import messagebox
import base64
import os
from tkinter import ttk

def decr():
    password = pas.get()
    if password == "":
        messagebox.showerror("Decryption", "Input Password")
    elif password == "Aadithya":
        screen2 = Toplevel(screen)
        screen2.title("Encrypted Text")
        screen2.geometry("400x200")
        screen2.configure(bg="lightgreen")

        mess = intext.get(1.0, END)
        encode = mess.encode("ascii")
        base = base64.b64decode(encode)
        encrypt = base.decode("ascii")

        Label(screen2, text="Encrypt", font="arial 14", fg="white", bg="lightgreen").place(x=10, y=0)
        intext2 = Text(screen2, font="Roboto 16", fg="black", bg="white", relief=GROOVE, wrap=WORD)
        intext2.place(x=10, y=40, width=380, height=150)
        intext2.insert(END, encrypt)
    else:
        messagebox.showerror("Decryption", "Invalid Password")

def enc():
    password = pas.get()
    if password == "":
        messagebox.showerror("Encryption", "Input Password")
    elif password == "Aadithya":
        screen1 = Toplevel(screen)
        screen1.title("Encrypted Text")
        screen1.geometry("400x200")
        screen1.configure(bg="salmon")

        mess = intext.get(1.0, END)
        encode = mess.encode("ascii")
        base = base64.b64encode(encode)
        encrypt = base.decode("ascii")

        Label(screen1, text="Encrypt", font="arial 14", fg="white", bg="salmon").place(x=10, y=0)
        intext2 = Text(screen1, font="Roboto 16", fg="black", bg="white", relief=GROOVE, wrap=WORD)
        intext2.place(x=10, y=40, width=380, height=150)
        intext2.insert(END, encrypt)
    else:
        messagebox.showerror("Encryption", "Invalid Password")

def main_screen():
    global screen
    global pas
    global intext

    screen = Tk()
    screen.geometry("400x400")
    screen.configure(bg="lightgray")

    
    screen.title("My CRYPT")

    def reset():
        pas.set("")
        intext.delete(1.0, END)

    Label(text="Enter text for Encrypt or Decrypt", fg="black", font=("calibri", 13), bg="lightgray").place(x=10, y=10)
    intext = Text(font="Roboto 16", fg="black", bg="white", relief=GROOVE, wrap=WORD)
    intext.place(x=10, y=50, width=380, height=100)

    Label(text="Enter your passcode", fg="black", font=("calibri", 13), bg="lightgray").place(x=10, y=170)
    pas = StringVar()
    Entry(textvariable=pas, width=19, bd=0, font=("arial", 25), show=" ").place(x=10, y=200)

    ttk.Button(text="Encrypt", command=enc).place(x=10, y=250, width=180, height=50)
    ttk.Button(text="Decrypt", command=decr).place(x=210, y=250, width=180, height=50)
    ttk.Button(text="Reset", command=reset).place(x=10, y=310, width=380, height=40)

    screen.mainloop()

main_screen()
