from tkinter import *
import os

def delete():
    wn.destroy()
def delete1():
    wn1.destroy()
def delete2():
    wn2.destroy()
def delete3():
    wn3.destroy()

def form2():
    global wn5
    wn5=Toplevel(wn3)
    wn5.title("Department form")
    wn5.geometry("300x300")
    global department_id
    global department_id_entry
    global department_name
    global department_name_entry
    department_id=StringVar()
    department_name=StringVar()
    Label(wn5,text="fill the form").place(x=40,y=20)
    Label(wn5,text="Department Id").place(x=50,y=80)
    department_id_entry=Entry(wn5,textvariable=department_id)
    department_id_entry.place(x=160,y=80)
    Label(wn5,text="Department Name").place(x=50,y=130)
    department_name_entry=Entry(wn5,textvariable=department_name)
    department_name_entry.place(x=160,y=130)

def form1():
    global wn4
    wn4=Toplevel(wn3)
    wn4.title("Employee Form")
    wn4.geometry("400x400")
    global employee_id
    global employee_id_entry
    global name
    global name_entry
    global age
    global age_entry
    global address
    global address_entry
    global contact
    global contact_entry
    global department
    global department_entry
    employee_id=StringVar()
    name=StringVar()
    age=StringVar()
    address=StringVar()
    contact=StringVar()
    department=StringVar()
    Label(wn4,text="please enter the details below",width=30,height=2).place(x=40,y=20)
    Label(wn4,text="Employee Id").place(x=80,y=80)
    employee_id_entry=Entry(wn4,textvariable=employee_id)
    employee_id_entry.place(x=160,y=80)
    Label(wn4,text="Name").place(x=80,y=110)
    name_entry=Entry(wn4,textvariable=name)
    name_entry.place(x=160,y=110)
    Label(wn4,text="Age").place(x=80,y=140)
    age_entry=Entry(wn4,textvariable=age)
    age_entry.place(x=160,y=140)
    Label(wn4,text="Address").place(x=80,y=170)
    address_entry=Entry(wn4,textvariable=address)
    address_entry.place(x=160,y=170)
    Label(wn4,text="Contact").place(x=80,y=200)
    contact_entry=Entry(wn4,textvariable=contact)
    contact_entry.place(x=160,y=200)
    Label(wn4,text="Department").place(x=80,y=230)
    department_entry=Entry(wn4,textvariable=department)
    department_entry.place(x=160,y=230)
    Button(wn4, text="back", width=10, height=2).place(x=20, y=280)
    Button(wn4, text="Reset", width=10, height=2).place(x=160, y=280)
    Button(wn4, text="Submit", width=10, height=2).place(x=280, y=280)

def dashboard():
    global wn3
    wn3=Toplevel(wn1)
    wn3.title("Dashboard")
    wn3.geometry("350x350")
    Label(wn3,text="Please fill the details below",width=20,height=2).place(x=40,y=20)
    Button(wn3,text="Add employee",width=30,height=2,command=form1).place(x=80,y=50)
    Button(wn3,text="Add department",width=30,height=2,command=form2).place(x=80,y=100)
    Button(wn3,text="View employee",width=30,height=2).place(x=80,y=150)
    Button(wn3,text="View department",width=30,height=2).place(x=80,y=200)
    Button(wn3,text="Exit",width=30,height=2,command=delete3).place(x=80,y=280)

def register():
    global wn2
    wn2=Toplevel(wn)
    wn2.title("Register form")
    wn2.geometry("300x300")
    global username
    global username_entry
    global password
    global password_entry
    username=StringVar()
    password=StringVar()
    Label(wn2,text="Welcome to register session",width=30,height=2).place(x=40,y=20)
    Label(wn2,text="Username").place(x=80,y=80)
    username_entry=Entry(wn2,textvariable=username)
    username_entry.place(x=140,y=80)
    Label(wn2,text="Password").place(x=80,y=120)
    password_entry=Entry(wn2,textvariable=password,show="*")
    password_entry.place(x=140,y=120)
    Button(wn2,text="Register",width=10,height=2,command=register_user).place(x=40,y=180)
    Button(wn2,text="Exit",width=10,height=2,command=delete2).place(x=170,y=180)

def login():
    global wn1
    wn1=Toplevel(wn)
    wn1.title("Login form")
    wn1.geometry("300x300")
    global username_verify
    global username_entry1
    global password_verify
    global password_entry1
    username_verify=StringVar()
    password_verify=StringVar()
    Label(wn1,text="Welcome to the login session",width=30,height=2).place(x=50,y=10)
    Label(wn1,text="Username").place(x=80,y=80)
    username_entry1=Entry(wn1,textvariable=username_verify)
    username_entry1.place(x=140,y=80)
    Label(wn1,text="Password").place(x=80,y=120)
    password_entry1=Entry(wn1,textvariable=password_verify,show="*")
    password_entry1.place(x=140,y=120)
    Button(wn1,text="Login",width=10,height=2,command=dashboard).place(x=40,y=180)
    Button(wn1,text="Exit",width=10,height=2,command=delete1).place(x=170,y=180)

wn=Tk()
wn.title("Form")
wn.geometry("300x300")
Label(wn,text="Please enter the details below",fg="blue",font=("calibri",15)).place(x=35,y=20)
Label(wn,text="").place()
Button(wn,text="Login",width=20,height=2,command=login).place(x=80,y=80)
Label(wn,text="").place()
Button(wn,text="Register",width=20,height=2,command=register).place(x=80,y=140)
Button(wn,text="Exit",width=10,height=2,command=delete).place(x=120,y=190)
wn.mainloop()