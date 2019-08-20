#!/usr/local/bin/python
import random
import string
import sys
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import backend_functions
from getpass import getpass

###----------------------- Initial window with Master Password -------------------###

popup = Tk()

class initialWindow(object):

    loop = False
    attempts = 0

    def __init__(self):
        popup.wm_title("PyPass")
        popup.geometry("480x200")
        popup.configure(background='#222936')
        label = Label(popup, text="Enter Master Key", font=('Times', 14), justify=CENTER, bg='#222936', fg='#9ABCB7')
        label.pack(fill=X, padx=5, pady=15)
        self.entry = Entry(popup, show='*', width=30)
        self.entry.pack(padx=7, pady=7)
        self.button = Button(popup, text='Unlock', command=self.cleanup, highlightbackground='#222936')
        self.button.pack()
        popup.mainloop()

    def cleanup(self):
        self.value = self.entry.get()
        access = 'bob'
        if self.value == access:
            self.loop = True
            popup.destroy()
        else:
            self.attempts += 1
            if self.attempts == 5:
                popup.destroy()
            self.entry.delete(0, 'end')
            messagebox.showerror('Incorrect Password', 'Incorrect password, attempts remaining: ' + str(5 - self.attempts))


m = initialWindow()
popup.mainloop()




###-------------------------------------- Main Window ---------------------------------###




# ============== Global Variables ==================

backgroundColor = '#222936'# '#222936'
labelTextColor = '#89A3BA' # '#9ABCB7'


# ================== Functions =======================

def quit():
    quit = messagebox.askyesno ("PyPass", "Are you sure you want to quit?")
    if quit > 0:
        window.destroy()
        return

def clear():
    title.delete(0,END)
    username.delete(0,END)
    password.delete(0,END)
    url.delete(0,END)

def addData():
    if(len(title.get()) !=0):
        backend_functions.add_entry(title.get(), username.get(), password.get(), url.get())
        listbox.delete(0,END)
        listbox.insert(END, (title.get(), username.get(), password.get(), url.get()))
    clear()

def record(event):
    global sd
    searchEntry = listbox.curselection()[0]
    sd = listbox.get(searchEntry)

    title.delete(0,END)
    title.insert(END,sd[1])
    username.delete(0,END)
    username.insert(END,sd[2])
    password.delete(0,END)
    password.insert(END,sd[3])
    url.delete(0,END)
    url.insert(END,sd[4])

def deleteData():
    if(len(title.get()) !=0):
        backend_functions.delete_entry(sd[0])
        clear()
        viewAllData()

def searchData():
    listbox.delete(0,END)
    for row in backend_functions.search_entry(title.get(), username.get(), password.get(), url.get()):
        listbox.insert(END,row,str(""))

def updateData():
    if(len(title.get()) !=0):
        backend_functions.delete_entry(sd[0])
        backend_functions.add_entry(title.get(), username.get(), password.get(), url.get())
        listbox.delete(0,END)
        listbox.insert(END, (title.get(), username.get(), password.get(), url.get()))


def viewAllData():
    listbox.delete(0,END)
    for row in backend_functions.show_all():
        listbox.insert(END,row,str(""))

def checkbox_status():
    if checkboxValue.get() == True:
        viewAllData()
    else:
        listbox.delete(0, END)


# ===================== FrontEnd / Window Configuration =====================



window = Tk()
window.geometry("800x600")
window.title("PyPass")
window.config(bg=backgroundColor)
window.resizable(False, False)

title = StringVar()
username = StringVar()
passwd = StringVar()
url = StringVar()
checkboxValue = BooleanVar()
scalerValue = StringVar()






label_appname = Label(window, text="PyPass Password Manager Version1.0", font=("Times", 20), fg=labelTextColor, bg=backgroundColor).place(relx=0.97, rely=0.08, anchor='se')
label_appname = Label(window, text="Copyright PyPass 2019", font=("Times", 15), fg=labelTextColor, bg=backgroundColor).place(relx=0.59, rely=1, anchor='se')

#====================================== Buttons ======================================
btnAdd = Button(window, text='Add', highlightbackground=backgroundColor, padx=1, pady=1, width=10, command=addData).place(relx=0.92, rely=0.67, anchor='se')
btnSearch = Button(window, text='Search', highlightbackground=backgroundColor, padx=1, pady=1, width=10, command=searchData).place(relx=0.62, rely=0.9, anchor='se')
btnDelete = Button(window, text='Delete', highlightbackground=backgroundColor, padx=1, pady=1, width=10, command=deleteData).place(relx=0.73, rely=0.9, anchor='se')
btnUpdate = Button(window, text='Update', highlightbackground=backgroundColor, padx=1, pady=1, width=10, command=updateData).place(relx=0.84, rely=0.9, anchor='se')
btnClose = Button(window, text='Close', highlightbackground=backgroundColor, width=10, padx=1, pady=1, command=quit, relief=RIDGE).place(relx=0.95, rely=0.9, anchor='se')
#====================================================================================



separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=42)




# ----------------------- Input Entry --------------------------


label_title = Label(window, text="Title", font=("Times", 15), fg=labelTextColor, bg=backgroundColor).place(relx=0.81, rely=0.25, anchor='se')
title = Entry(window, font=("Times", 15), background=labelTextColor, highlightthickness=0)
title.place(relx=0.97, rely=0.3, anchor='se')

label_username = Label(window, text="Username", font=("Times", 15), fg=labelTextColor, bg=backgroundColor).place(relx=0.85, rely=0.35, anchor='se')
username = Entry(window, font=("Times", 15), background=labelTextColor, highlightthickness=0)
username.place(relx=0.97, rely=0.4, anchor='se')

label_password = Label(window, text="Password", font=("Times", 15), fg=labelTextColor, bg=backgroundColor).place(relx=0.85, rely=0.45, anchor='se')
password = Entry(window, font=("Times", 15), background=labelTextColor, highlightthickness=0)
password.place(relx=0.97, rely=0.5, anchor='se')

label_url = Label(window, text="URL", font=("Times", 15), fg=labelTextColor, bg=backgroundColor).place(relx=0.81, rely=0.55, anchor='se')
url = Entry(window, font=("Times", 15), background=labelTextColor, highlightthickness=0)
url.place(relx=0.97, rely=0.6, anchor='se')




clear_data = Button(window, text="Clear", font=15, highlightbackground=backgroundColor, padx=1, pady=1, width=10, command=clear).place(relx=0.51, rely=0.9, anchor='se')
show_hide = Checkbutton(window, text="Show Database", font=15, bg=backgroundColor, fg=labelTextColor, var=checkboxValue,  command=checkbox_status)
show_hide.place(relx=0.2, rely=0.65, anchor='se')

# ============================ Data Frame ==========================



listbox = Listbox(window, background='#222936', bd=1, font="Times", fg='#89A3BA', selectbackground="#393B45", highlightcolor="Red", relief=FLAT, height=13, width=75)
listbox.bind('<<ListboxSelect>>', record)
listbox.place(relx=0.7, rely=0.6, anchor='se')

scrollbar = Scrollbar(listbox, command=listbox.yview, bg=labelTextColor, troughcolor=labelTextColor, width=1)
listbox.config(yscrollcommand = scrollbar.set)
scrollbar.place(relx=1, rely=0.21, anchor='se')
# scrollbar.grid(row=5, column=1)


# ============================ Password Generator =================



scale_label = Label(window, text="Generate Password", font=("Times", 15), fg=labelTextColor, bg=backgroundColor).place(relx=0.28, rely=0.85, anchor='se')
scalebar = Scale(window, from_=8, to=64, orient=HORIZONTAL, bg=backgroundColor, troughcolor=labelTextColor, highlightcolor=labelTextColor, var=scalerValue)
scalebar.set(32)
scalebar.place(relx=0.2, rely=0.9, anchor='se')


def scaleStatus():
    lenght = int(scalerValue.get())
    newstring = ''
    for i in range(lenght):
        x = random.randint(0,94)
        newstring += string.printable[x]

    password.delete(0,END)
    password.insert(END,newstring)


password_lenght_btn = Button(window, text='Generate', highlightbackground=backgroundColor, padx=1, pady=1, width=10, command=scaleStatus).place(relx=0.35, rely=0.9, anchor='se')




window.mainloop()
