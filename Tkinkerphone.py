from cgitb import text
from fileinput import close
from msilib.schema import ListBox
from os import kill

from struct import pack
from textwrap import fill
import tkinter as tk
from tkinter.ttk import Entry
from turtle import bgcolor, color, width
from venv import create
import PhonebookSearch as Search
import pymysql
import config as cf


# the main window to be create
# eventually we will use classes and self._init_ for this one
master = tk.Tk()
master.title("Phone_book App")
w = tk.Canvas(master, width=350, height=600)
w.configure(bg='white')

first_name = tk.StringVar()
last_name = tk.StringVar()
phoneNumber = tk.IntVar()
Birthday = tk.StringVar()
entry = tk.StringVar()

# taehoon can delete this part as we dont need it if we have an sql database as our for loop for contact creation
master.counter = 0
# connect mysql and Python
conn = pymysql.connect(host=cf.host, user=cf.user,
                       password=cf.password, db=cf.database)
cur = conn.cursor()

contacts = []


# add contact bar and search bar with button for creating new contacts
def contact():
    new = tk.Toplevel(w)
    new.geometry("350x450")

    new.title("Add Contact")

    newContact_sect = tk.Canvas(
        new, width="350", background="#7ED957", height=120)
    newContact_sect.create_text(
        175, 60, text="ADD CONTACT", fill="white", font="Helvetica 22 bold")

    # FIRST NAME AND LAST NAME SECTION
    newContact_sect2 = tk.Canvas(
        new, width="350", background="white", height=320)

    newContact_sect2.create_text(
        65, 40, text="First Name", fill="grey", font="Helvetica 15 bold")
    firstName_entry = tk.Entry(new, width="20", background="white", foreground="black", highlightbackground="grey",
                               highlightcolor='grey', highlightthickness=4, textvariable=first_name).place(x=14, y=180)

    newContact_sect2.create_text(
        260, 40, text='Last Name', fill="grey", font="Helvetica 15 bold")
    lastName_entry = tk.Entry(new, width='20', background='white', foreground="black", highlightcolor="grey",
                              highlightbackground='grey', highlightthickness=4, textvariable=last_name).place(x=200, y=180)

    newContact_sect2.create_text(
        90, 110, text="Phone Number", fill='grey', font='Helvetica 15 bold')
    phoneNumber_entry = tk.Entry(new, background='white', foreground="black", highlightcolor="grey",
                                 highlightbackground='grey', highlightthickness=4, text=phoneNumber).place(x=14, y=250, width=300)

    newContact_sect2.create_text(
        80, 180, text="BIRTHDAY", fill="grey", font="Helvetica 15 bold")
    birthday_entry = tk.Entry(new, background='white', foreground="black", highlightcolor="grey",
                              highlightbackground='grey', highlightthickness=4, textvariable=Birthday).place(x=14, y=320, width=300)

    # this button kills the page and calls the make_contact function that puts our contact on the home page
    Submit_button = tk.Button(new, width='20', text="Enter", bg='#008037', height=2, command=lambda: [
                              makingContacts(), new.destroy()]).place(x=14, y=355)

    newContact_sect.pack()
    newContact_sect2.pack()


def search():
    print(entry.get())
    res = Search.searchData(str(entry.get()))

    """ make new list that stores first and last name for the contact display function """
    #contacts_sect.create_text(70, 50+(i*20), text = str(res[i]), fill = "green", font = "Helvetica 15 bold", justify = 'left')
    display_button = tk.Button(contacts_sect, text=res[0], fg='green', activebackground='green', activeforeground='red',
                               height=1, command=searchDisplay, borderwidth=0, font="Helvetica 15 bold").place(x=15, y=38)


new_w = tk.Canvas(master, width=350, height=60)
new_w.configure(bg="#7ed957")
# green_label = tk.Label(new_w, text="Add Contact",background="green",foreground="white").place(x =160, y = 20)
add_button = tk.Button(new_w, text="Add contact", activebackground="green",
                       activeforeground="red", height=1, command=contact).place(x=210, y=20)
enter_label = tk.Entry(new_w, width="20", background="white",
                       foreground="blue", textvariable=entry).place(x=30, y=20)
search_button = tk.Button(new_w, text="Search", activebackground="green",
                          activeforeground="red", height=1, command=search).place(x=160, y=20)


# Owner window that contains details about the owner, including number and birthday
Me_sect = tk.Canvas(master, width=350, height=80)
Me_sect.configure(bg="#DDF1D4")

Me_sect.create_text(35, 20, text="ME", fill="green", font="Helvetica 15 bold")
Me_sect.create_line(22, 35, 350, 35, fill="green", width=1)
Me_sect.create_text(70, 50, text="COOL GAL", fill="green",
                    font="Helvetica 15 bold ")
Me_sect.create_line(22, 65, 350, 65, fill="green", width=1)


# contacts section that will have list of contacts
contacts_sect = tk.Canvas(master, width=350, height=500)
contacts_sect.create_text(90, 20, text='MY CONTACTS',
                          fill="green", font="Helvetica 15 bold")
contacts_sect.create_line(22, 35, 350, 35, fill="green", width=1)


def makingContacts():

    firstContact_button = tk.Button(contacts_sect, text=(first_name.get(), last_name.get(
    )), activebackground="green", activeforeground="red", height=1, command=displayContact).place(x=20, y=40)

# if add_button(is)


def displayContact():
    new2 = tk.Toplevel(w)
    new2.geometry = ("350x450")
    display_sect = tk.Canvas(
        new2, width="350", background="#7ED957", height=120)
    display_sect.create_text(175, 60, text=(
        first_name.get(), last_name.get()), fill="white", font="Helvetica 22 bold")

    display_sect2 = tk.Canvas(
        new2, width="350", background="white", height=320)

    display_sect2.create_text(
        90, 40, text="PHONE NUMBER", fill='grey', font="Helvetica 15 bold")
    phoneNumber_entry = tk.Entry(display_sect2, background="white",
                                 highlightbackground="grey", highlightthickness=4, foreground="black")
    phoneNumber_entry.place(x=40, y=70, width=200)
    phoneNumber_entry.insert(0, "Filler Number")

    display_sect2.create_text(70, 120, text="BIRTHDAY",
                              fill="grey", font="Helvetica 15 bold")
    birthday_entry = tk.Entry(display_sect2, background="white",
                              highlightbackground="grey", highlightthickness=4, foreground="black")
    birthday_entry.place(x=40, y=150, width=200)
    birthday_entry.insert(0, "Filler Birthday")

    edit_contact = tk.Button(new2, text="EDIT CONTACT", fg="white", activebackground="green",
                             bg='#008037', activeforeground="red", height=1).place(x=40, y=350)
    delete_contact = tk.Button(new2, text="DELETE CONTACT", fg="red", activebackground='green',
                               bg='#008037', activeforeground='red', height=1).place(x=230, y=350)
    # phoneNumber_entry.

    display_sect.pack()
    display_sect2.pack()


def searchDisplay():

    new2 = tk.Toplevel(w)
    new2.geometry = ("350x450")
    display_sect = tk.Canvas(
        new2, width="350", background="#7ED957", height=120)
    display_sect.create_text(175, 60, text=(
        "Filler"), fill="white", font="Helvetica 22 bold")

    display_sect2 = tk.Canvas(
        new2, width="350", background="white", height=320)

    display_sect2.create_text(90, 40, text="Filler",
                              fill='grey', font="Helvetica 15 bold")
    phoneNumber_entry = tk.Entry(display_sect2, background="white",
                                 highlightbackground="grey", highlightthickness=4, foreground="black")
    phoneNumber_entry.place(x=40, y=70, width=200)
    phoneNumber_entry.insert(0, phoneNumber.get())

    display_sect2.create_text(70, 120, text="Filler",
                              fill="grey", font="Helvetica 15 bold")
    birthday_entry = tk.Entry(display_sect2, background="white",
                              highlightbackground="grey", highlightthickness=4, foreground="black")
    birthday_entry.place(x=40, y=150, width=200)
    birthday_entry.insert(0, Birthday.get())

    edit_contact = tk.Button(new2, text="EDIT CONTACT", fg="white", activebackground="green",
                             bg='#008037', activeforeground="red", height=1).place(x=40, y=350)
    delete_contact = tk.Button(new2, text="DELETE CONTACT", fg="red", activebackground='green',
                               bg='#008037', activeforeground='red', height=1).place(x=230, y=350)
    # phoneNumber_entry.

    display_sect.pack()
    display_sect2.pack()


# running all the sections and windows created
# i noticed that the order in which you call the pack function matters
new_w.pack()
Me_sect.pack()
contacts_sect.pack()

w.pack()
master.mainloop()
