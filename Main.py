from tkinter import *
import sqlite3
from email.message import EmailMessage
import ssl
import smtplib


#Window declaration
window_home=Tk()
window_admin=Tk()
window_employee=Tk()
window_employee_page=Tk()
window_admin_process=Tk()
window_admin_add=Tk()
window_admin_delete=Tk()
window_id_ask1=Tk()
window_employee_modify=Tk()
window_send_mail=Tk()

#Title
window_send_mail.title("Mail")
window_employee_modify.title("Modify employee")
window_admin_add.title("Add an employee")
window_admin_delete.title("Remove an employee")
window_employee_page.title("Employee details")
window_employee.title("Verification")
window_id_ask1.title("Verification")
window_admin_process.title("Admin home page")
window_home.title("Home")
window_admin.title("Verification")

#Hiding the windows
window_admin.withdraw()
window_employee.withdraw()
window_employee_page.withdraw()
window_admin_process.withdraw()
window_admin_add.withdraw()
window_admin_delete.withdraw()
window_id_ask1.withdraw()
window_employee_modify.withdraw()
window_send_mail.withdraw()

#Geometry declaration
window_admin.geometry("500x500")
window_home.geometry("500x500")
window_employee.geometry("500x500")
window_employee_page.geometry("500x500")
window_admin_process.geometry("500x500")
window_admin_add.geometry("500x500")
window_admin_delete.geometry("500x500")
window_id_ask1.geometry("500x500")
window_employee_modify.geometry("500x500")
window_send_mail.geometry("500x500")

#SQL Connection
con=sqlite3.connect('project.db')
cursor=con.cursor()

def send():
    sender = 'raiswapnil0601@gmail.com'
    password = 'njslecvrzmksvmfk'
    reciever = e17.get()
    subject = e18.get()
    body=t.get(1.0,"end-1c")
    em = EmailMessage()
    em['from'] = sender
    em['To'] = reciever
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, reciever, em.as_string())
        l37.config(text="Mail send", font=('Times New Roman', 15))
        l37.place(x=170, y=430)

    admin_process()
def mail_em():
    window_admin_process.withdraw()
    window_send_mail.deiconify()

    l34.config(text="Mail ID",font=('Times New Roman',15))
    l35.config(text="Subject",font=('Times New Roman',15))
    l36.config(text="write your mail",font=('Times New Roman',15))
    e17.config(borderwidth=5,width=35)
    e18.config(borderwidth=5,width=35)
    t.config(height=10,width=50)
    b25.config(text="Send",height=1,width=15,command=send)
    b26.config(text="back",height=1,width=15,command=admin_process)

    l34.place(x=20,y=50)
    l35.place(x=20, y=90)
    l36.place(x=20, y=130)
    e17.place(x=100,y=50)
    e18.place(x=100, y=90)
    t.place(x=20,y=200)
    lbg10.place(x=0,y=0,relwidth=1,relheight=1)
    b25.place(x=20, y=450)
    b26.place(x=350, y=450)

def mod():
    l=[e11.get(),int(e12.get()),int(e13.get()),e14.get(),e15.get(),e16.get()]
    update=f"UPDATE EMPLOYEE0 SET NAME=?,ID=?,SAL=?,DEPT=?,ROLE=?,MAIL=?"
    cursor.execute(update,l)

    l331.config(text="Employee's detalis modified ", font=('Times New Roman', 15))
    l331.place(x=130,y=450)

    e11.delete(0, END)
    e12.delete(0, END)
    e13.delete(0, END)
    e14.delete(0, END)
    e15.delete(0, END)
    e16.delete(0, END)
    con.commit()

def modify_em():
    window_id_ask1.withdraw()
    window_employee_modify.deiconify()

    l=cursor.fetchone()

    l27.config(text="Modify The details: ", font=('Times New Roman', 30))
    l28.config(text="Name ", font=('Times New Roman', 15))
    l29.config(text="ID ", font=('Times New Roman', 15))
    l30.config(text="Salary ", font=('Times New Roman', 15))
    l31.config(text="Department ", font=('Times New Roman', 15))
    l32.config(text="Role ", font=('Times New Roman', 15))
    l33.config(text="Mail ID ", font=('Times New Roman', 15))
    e11.config(borderwidth=7)
    e12.config(borderwidth=7)
    e13.config(borderwidth=7)
    e14.config(borderwidth=7)
    e15.config(borderwidth=7)
    e16.config(borderwidth=7)
    e11.insert(0,l[0])
    e12.insert(0,l[1])
    e13.insert(0,l[2])
    e14.insert(0,l[3])
    e15.insert(0,l[4])
    e16.insert(0,l[5])
    b23.config(text="Modify", command=mod, height="1", width="15")
    b24.config(text="back", command=admin_process, height="1", width="15")

    l27.place(x=100,y=20)
    l28.place(x=20,y=100)
    l29.place(x=20,y=150)
    l30.place(x=20,y=200)
    l31.place(x=20,y=250)
    l32.place(x=20,y=300)
    l33.place(x=20,y=350)
    e11.place(x=150,y=100)
    e12.place(x=150,y=150)
    e13.place(x=150,y=200)
    e14.place(x=150,y=250)
    e15.place(x=150,y=300)
    e16.place(x=150,y=350)
    b23.place(x=20,y=400)
    b24.place(x=350,y=400)
    lbg9.place(x=0,y=0,relwidth=1,relheight=1)

def check3():
    a = int(e10.get())
    cursor.execute(f"SELECT * FROM EMPLOYEE0 WHERE ID={a}")
    l1 = cursor.fetchone()
    if (l1==None):
        l26.config(text="ID does not exists")
        l26.place(x=177, y=350)
        e10.delete(0, END)
    else:
        cursor.execute(f"SELECT * FROM EMPLOYEE0 WHERE ID={a}")
        modify_em()
        e10.delete(0, END)

def askiid1():

    window_admin_process.withdraw()
    window_id_ask1.deiconify()


    l24.config(text="        Welcome ", font=('Times New Roman', 30))
    l25.config(text="Employee ID", font=('Times New Roman', 20))

    e10.config(show="*", borderwidth=5)

    b21.config(text="Submit", command=check3, height="1", width="15")
    b22.config(text="Back",command=admin_process,height="1",width="15")

    l24.place(x=100, y=50)
    l25.place(x=175, y=150)
    e10.place(x=185, y=215)
    b21.place(x=190, y=280)
    b22.place(x=350, y=400)
    lbg8.place(x=0,y=0,relheight=1,relwidth=1)

def addem():
    a = 23232
    b = 2323
    if (len(e4.get()) > 0):
        a = int(e4.get())
    if (len(e5.get()) > 0):
        b = int(e5.get())
    l = [e3.get(), a, b, e6.get(), e7.get(), e8.get()]
    inserting = '''INSERT INTO EMPLOYEE0 (NAME, ID, SAL , DEPT, ROLE, MAIL) VALUES (?,?,?,?,?,?);'''
    cursor.execute(inserting, l)
    print(l)
    l22.config(text="Data added",font=('Times New Roman', 15))
    l22.place(x=180,y=400)
    e3.delete(0,END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    con.commit()

def deleteen():
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)


def dele():
    id=int(e9.get())
    cursor.execute(F"DELETE FROM EMPLOYEE0 WHERE ID={id}")
    e9.delete(0,END)
    l231.config(text="Employee Data deleted", font=('Times New Roman', 15))
    l231.place(x=150, y=400)
    con.commit()

def admin_delete():
    window_admin_process.withdraw()
    window_employee_page.withdraw()
    window_admin_delete.deiconify()

    l23.config(text="Enter the ID\nof employee", font=('Times New Roman', 30))
    e9.config(borderwidth=5)
    b17.config(text="Proceed",height="1",width="15",command=dele)
    b18.config(text="back",height="1",width="15",command=admin_process)

    b17.place(x=100,y=300)
    b18.place(x=300,y=300)
    e9.place(x=180,y=210)
    l23.place(x=150,y=50)
    lbg7.place(x=0,y=0,relheight=1,relwidth=1)

def admin_add():
    window_admin_process.withdraw()
    window_admin_add.deiconify()

    l15.config(text="Add employee details:", font=('Times New Roman', 30))
    l16.config(text="Name: ", font=('Times New Roman', 15))
    l17.config(text="Id: ", font=('Times New Roman', 15))
    l18.config(text="Salary: ", font=('Times New Roman', 15))
    l19.config(text="Department: ", font=('Times New Roman', 15))
    l20.config(text="Role: ", font=('Times New Roman', 15))
    l21.config(text="Mail id: ", font=('Times New Roman', 15))
    e3.config(borderwidth=5,width=35)
    e4.config(borderwidth=5,width=35)
    e5.config(borderwidth=5,width=35)
    e6.config(borderwidth=5,width=35)
    e7.config(borderwidth=5,width=35)
    e8.config(borderwidth=5,width=35)
    b14.config(text="add", command=addem, height="1", width="15")
    b15.config(text="delete", command=deleteen, height="1", width="15")
    b16.config(text="Back", command=admin_process, height="1", width="15")

    l15.place(x=80, y=20)
    l16.place(x=20, y=100)
    l17.place(x=20, y=150)
    l18.place(x=20, y=200)
    l19.place(x=20, y=250)
    l20.place(x=20, y=300)
    l21.place(x=20, y=350)
    e3.place(x=150,y=100)
    e4.place(x=150, y=150)
    e5.place(x=150, y=200)
    e6.place(x=150, y=250)
    e7.place(x=150, y=300)
    e8.place(x=150, y=350)
    b14.place(x=50, y=450)
    b15.place(x=200, y=450)
    b16.place(x=350,y=450)
    lbg6.place(x=0,y=0,relheight=1,relwidth=1)



def admin_process():
    window_admin.withdraw()
    window_admin_add.withdraw()
    window_admin_delete.withdraw()
    window_employee_modify.withdraw()
    window_send_mail.withdraw()
    window_id_ask1.withdraw()
    window_admin_process.deiconify()

    b8.config(text="Add employee",height=1,width="15",command=admin_add)
    b9.config(text="Remove an employee", height=1, width="15",command=admin_delete)
    b10.config(text="modify an employee", height=1, width="15",command=askiid1)
    b11.config(text="view employee", height=1, width="15",command=employee)
    b12.config(text="Mail employee", height=1, width="15",command=mail_em)
    b13.config(text="Back",height="1",width="15",command=admin)

    b8.place(x=50,y=150)
    b9.place(x=200,y=150)
    b10.place(x=350,y=150)
    b11.place(x=140,y=300)
    b12.place(x=290,y=300)
    b13.place(x=350,y=400)
    lbg5.place(x=0,y=0,relwidth=1,relheight=1)


def check1():
    cursor.execute('''SELECT * FROM password''')
    l1 = cursor.fetchone()
    if(e1.get()!=l1[0]):
        l4.config(text="The password is incorrect")
        l4.place(x=177,y=350)
        e1.delete(0,END)
    else:
        admin_process()
        e1.delete(0,END)
def admin():
    #Removing the previous window
    window_home.withdraw()
    window_admin_process.withdraw()
    #Showing the current window

    window_admin.deiconify()

    l2.config(text="Welcome admin", font=('Times New Roman', 30))
    l3.config(text="Password", font=('Times New Roman', 20))

    e1.config(show="*",borderwidth=5)

    b3.config(text="Submit",command=check1,height="1",width="15")
    b4.config(text="Back",command=home,height=1,width="15")

    l3.place(x=195, y=150)
    l2.place(x=120, y=50)
    e1.place(x=185,y=210)
    b3.place(x=190,y=280)
    b4.place(x=350,y=400)
    lbg2.place(x=0,y=0,relwidth=1,relheight=1)
def employee_page():
    window_employee.withdraw()
    window_admin_delete.withdraw()
    window_employee_page.deiconify()

    b = cursor.fetchone()

    l8.config(text="Employee details:",font=('Times New Roman',30))
    l9.config(text="Name: ",font=('Times New Roman', 15))
    l10.config(text="Id: ",font=('Times New Roman', 15))
    l11.config(text="Salary: ", font=('Times New Roman', 15))
    l12.config(text="Department: ", font=('Times New Roman', 15))
    l13.config(text="Role: ", font=('Times New Roman', 15))
    l14.config(text="Mail id: ", font=('Times New Roman', 15))
    ld1.config(text=b[0],font=('Times New Roman',15))
    ld2.config(text=b[1], font=('Times New Roman', 15))
    ld3.config(text=b[2], font=('Times New Roman', 15))
    ld4.config(text=b[3], font=('Times New Roman', 15))
    ld5.config(text=b[4], font=('Times New Roman', 15))
    ld6.config(text=b[5], font=('Times New Roman', 15))
    b7.config(text="Back",command=employee,height="1",width="15")


    l8.place(x=100,y=20)
    l9.place(x=20, y=100)
    ld1.place(x=130,y=100)
    l10.place(x=20,y=150)
    ld2.place(x=130,y=150)
    l11.place(x=20, y=200)
    ld3.place(x=130, y=200)
    l12.place(x=20, y=250)
    ld4.place(x=130, y=250)
    l13.place(x=20, y=300)
    ld5.place(x=130, y=300)
    l14.place(x=20, y=350)
    ld6.place(x=130, y=350)
    b7.place(x=350, y=400)
    lbg4.place(x=0,y=0,relwidth=1,relheight=1)

def check2():
    a=int(e2.get())
    cursor.execute(f"SELECT * FROM EMPLOYEE0 WHERE ID={a}")
    l1=cursor.fetchone()
    if (l1==None):
        l7.config(text="The ID does not exists")
        l7.place(x=190, y=350)
        e2.delete(0, END)
    else:
        cursor.execute(f"SELECT * FROM EMPLOYEE0 WHERE ID={a}")
        employee_page()
        e2.delete(0, END)

def employee():

    window_home.withdraw()
    window_employee_page.withdraw()
    window_admin_process.withdraw()
    window_employee.deiconify()



    l6.config(text="        Welcome ", font=('Times New Roman', 30))
    l5.config(text="Employee ID", font=('Times New Roman', 20))

    e2.config(show="*", borderwidth=5)

    b5.config(text="Submit", command=check2, height="1", width="15")
    b6.config(text="Back",command=home,height="1",width="15")

    l6.place(x=100, y=50)
    l5.place(x=175, y=150)
    e2.place(x=185, y=215)
    b5.place(x=190, y=280)
    b6.place(x=350, y=400)
    lbg3.place(x=0,y=0,relwidth=1,relheight=1)

def home():

    window_home.deiconify()
    window_admin.withdraw()
    window_employee.withdraw()

    l1.config(text="Welcome",font=('Times New Roman',50),bg='#95dabe')
    lbg1.config(bg='#95dabe')
    b1=Button(text="Login as admin",font=('Times New Roman',15),command=admin,borderwidth=5)
    b2=Button(text="Login as employee",font=('Times New Roman',15),command=employee,borderwidth=5)

    l1.place(x=130,y=50)
    b1.place(x=185,y=200)
    b2.place(x=170,y=300)
    lbg1.place(x=0,y=0,relwidth=1,relheight=1)

#All widget declaration

    #Home
lbg1=Label(window_home)
l1=Label(window_home)

    #admim
lbg2=Label(window_admin,bg='#95dabe')
l2=Label(window_admin,bg='#95dabe')
l3=Label(window_admin,bg='#95dabe')
l4=Label(window_admin,bg='#95dabe')

    #Employee
lbg3=Label(window_employee,bg='#95dabe')
l5=Label(window_employee,bg='#95dabe')
l6=Label(window_employee,bg='#95dabe')
l7=Label(window_employee,bg='#95dabe')

    #Employee_page
lbg4=Label(window_employee_page,bg='#95dabe')
l8=Label(window_employee_page,bg='#95dabe')
l9=Label(window_employee_page,bg='#95dabe')
l10=Label(window_employee_page,bg='#95dabe')
l11=Label(window_employee_page,bg='#95dabe')
l12=Label(window_employee_page,bg='#95dabe')
l13=Label(window_employee_page,bg='#95dabe')
l14=Label(window_employee_page,bg='#95dabe')
ld1=Label(window_employee_page,bg='#95dabe')
ld2=Label(window_employee_page,bg='#95dabe')
ld3=Label(window_employee_page,bg='#95dabe')
ld4=Label(window_employee_page,bg='#95dabe')
ld5=Label(window_employee_page,bg='#95dabe')
ld6=Label(window_employee_page,bg='#95dabe')

    #Admin process
lbg5=Label(window_admin_process,bg='#95dabe')

    #Admin_add
lbg6=Label(window_admin_add,bg='#95dabe')
l15=Label(window_admin_add,bg='#95dabe')
l16=Label(window_admin_add,bg='#95dabe')
l17=Label(window_admin_add,bg='#95dabe')
l18=Label(window_admin_add,bg='#95dabe')
l19=Label(window_admin_add,bg='#95dabe')
l20=Label(window_admin_add,bg='#95dabe')
l21=Label(window_admin_add,bg='#95dabe')
l22=Label(window_admin_add,bg='#95dabe')

    #Admin_delete
lbg7=Label(window_admin_delete,bg='#95dabe')
l23=Label(window_admin_delete,bg='#95dabe')
l231=Label(window_admin_delete,bg='#95dabe')

    #Asking ID 1
lbg8=Label(window_id_ask1,bg='#95dabe')
l24=Label(window_id_ask1,bg='#95dabe')
l25=Label(window_id_ask1,bg='#95dabe')
l26=Label(window_id_ask1,bg='#95dabe')

    #Employee mofify
lbg9=Label(window_employee_modify,bg='#95dabe')
l27=Label(window_employee_modify,bg='#95dabe')
l28=Label(window_employee_modify,bg='#95dabe')
l29=Label(window_employee_modify,bg='#95dabe')
l30=Label(window_employee_modify,bg='#95dabe')
l31=Label(window_employee_modify,bg='#95dabe')
l32=Label(window_employee_modify,bg='#95dabe')
l33=Label(window_employee_modify,bg='#95dabe')
l331=Label(window_employee_modify,bg='#95dabe')

    #Send mail
lbg10=Label(window_send_mail,bg='#95dabe')
l34=Label(window_send_mail,bg='#95dabe')
l35=Label(window_send_mail,bg='#95dabe')
l36=Label(window_send_mail,bg='#95dabe')
l37=Label(window_send_mail,bg='#95dabe')

#Buttons
    #Home
b1=Button(window_home,borderwidth=5)
b2=Button(window_home,borderwidth=5)

    #admin
b3=Button(window_admin,borderwidth=5)
b4=Button(window_admin,borderwidth=5)

    #Employee
b5=Button(window_employee,borderwidth=5)
b6=Button(window_employee,borderwidth=5)

    #Employee_Page
b7=Button(window_employee_page,borderwidth=5)

    #Admin_process
b8=Button(window_admin_process,borderwidth=5)
b9=Button(window_admin_process,borderwidth=5)
b10=Button(window_admin_process,borderwidth=5)
b11=Button(window_admin_process,borderwidth=5)
b12=Button(window_admin_process,borderwidth=5)
b13=Button(window_admin_process,borderwidth=5)

    #Admin_add
b14=Button(window_admin_add,borderwidth=5)
b15=Button(window_admin_add,borderwidth=5)
b16=Button(window_admin_add,borderwidth=5)

    #Admin_delete
b17=Button(window_admin_delete,borderwidth=5)
b18=Button(window_admin_delete,borderwidth=5)
b19=Button(window_employee_page,borderwidth=5)
b20=Button(window_employee_page,borderwidth=5)

    #Asking ID 1
b21=Button(window_id_ask1,borderwidth=5)
b22=Button(window_id_ask1,borderwidth=5)

    #Employee modify
b23=Button(window_employee_modify,borderwidth=5)
b24=Button(window_employee_modify,borderwidth=5)

    #Send mail
b25=Button(window_send_mail,borderwidth=5)
b26=Button(window_send_mail,borderwidth=5)
b27=Button(window_send_mail,borderwidth=5)

#Entries
    #admin
e1=Entry(window_admin)

    #Employee
e2=Entry(window_employee)

    #Admin_add
e3=Entry(window_admin_add)
e4=Entry(window_admin_add)
e5=Entry(window_admin_add)
e6=Entry(window_admin_add)
e7=Entry(window_admin_add)
e8=Entry(window_admin_add)

    #Admin_delete
e9=Entry(window_admin_delete)

    #Asking ID 1
e10=Entry(window_id_ask1)

    #Employee modify
e11=Entry(window_employee_modify)
e12=Entry(window_employee_modify)
e13=Entry(window_employee_modify)
e14=Entry(window_employee_modify)
e15=Entry(window_employee_modify)
e16=Entry(window_employee_modify)

    #Send mail
e17=Entry(window_send_mail)
e18=Entry(window_send_mail)

#Text field
    #Send mail
t=Text(window_send_mail)

home()

#All the window mainloops
window_home.mainloop()
window_admin.mainloop()
window_employee.mainloop()
window_employee_page.mainloop()
window_admin_process.mainloop()
window_admin_add.mainloop()
window_admin_delete.mainloop()
window_id_ask1.mainloop()
window_employee_modify.mainloop()
window_send_mail.mainloop()