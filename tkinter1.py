import tkinter as tk
from tkinter import ttk,messagebox
import mysql.connector
from tkinter import *
from tkinter.ttk import Combobox

def GetValue(event):
    e1.delete(0,END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id=listbox.selection()[0]
    select=listbox.set(row_id)
    e1.insert(0,select['sname'])
    e2.insert(0, select['eid'])
    e3.insert(0, select['mobile'])
    e4.insert(0, select['country'])


def add():
    stname=e1.get()
    eid = e2.get()
    mobile = e3.get()
    country = e4.get()

    mysqldb=mysql.connector.connect(host="localhost",user="root",password="Army@777",database='student')
    mycursor=mysqldb.cursor()

    try:
        sql="Insert Into registration1(sname,eid,mobile,country) VALUES(%s,%s,%s,%s)"
        val=(stname,eid,mobile,country)
        mycursor.execute(sql,val)
        mysqldb.commit()
        lastid=mycursor.lastrowid
        messagebox.showinfo("Information"," Student registered  Successfully...")
        e1.delete(0,END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

def update():
    stname = e1.get()
    eid = e2.get()
    mobile = e3.get()
    country = e4.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="Army@777", database='student')
    mycursor=mysqldb.cursor()
    try:
        sql="Update registration1 set sname=%s,eid=%s,country=%s where mobile=%s"
        val=(stname,eid,country,mobile)
        mycursor.execute(sql,val)
        mysqldb.commit()
        lastid=mycursor.lastrowid
        messagebox.showinfo("Information","Record Updated Successfully...")
        e1.delete(0,END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


def delete():
    mobile = e3.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="Army@777", database='student')
    mycursor = mysqldb.cursor()
    try:
        sql = "delete from registration1 where mobile=%s"
        val = (mobile,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("Information", "Record Deleted Successfully...")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

def show():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="Army@777", database='student')
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT sname,eid,mobile,country FROM registration1")
    records=mycursor.fetchall()
    print(records)

    for i, (sname,eid,mobile,country) in enumerate(records,start=1):
        listbox.insert("","end",values=(sname,eid,mobile,country))
        mysqldb.close()

ok=Tk()

ok.geometry("800x750")
global e1
global e2
global e3
global e4

var=StringVar()
li=["India","Australia","England","south Africa"]


ok.title("Registration.form")
Label(ok,text="Birla College",fg='orange',font=(None,30)).place(x=300,y=5)
Label(ok,text="Full Name",bg='black',fg='white').place(x=10,y=10)
Label(ok,text="Email-Id",bg='black',fg='white').place(x=10,y=40)
Label(ok,text="Mobile No",bg='black',fg='white').place(x=10,y=70)
Label(ok,text="country",bg='black',fg='white').place(x=10,y=100)


e1=Entry(ok)
e1.place(x=140,y=10)

e2=Entry(ok)
e2.place(x=140,y=40)

e3=Entry(ok)
e3.place(x=140,y=70)

e4=Combobox(ok,values=li,font=('Arial',15))
e4.place(x=140,y=100)


Button(ok,text="Add",command=add,height=3,width=13,bg='grey').place(x=40,y=130)
Button(ok,text="Update",command=update,height=3,width=13,bg='grey').place(x=140,y=130)
Button(ok,text="Delete",command=delete,height=3,width=13,bg='grey').place(x=250,y=130)

cols=('sname','eid','mobile','country')
listbox=ttk.Treeview(ok,columns=cols,show='headings')

for col in cols:
    listbox.heading(col,text=col)
    listbox.grid(row=1,column=0,columnspan=2)
    listbox.place(x=10,y=200)
show()
listbox.bind('<Double-Button-1>',GetValue)

ok.mainloop()