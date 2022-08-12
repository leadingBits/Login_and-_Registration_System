
"""https://github.com/leadingBits | https://linkedin.com/in/wasiibrahimi"""

from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk

rootStructure = Tk()
rootStructure.title("Login and Registration System")

# **************************************************ROOT STRUCTURE******************************************************

width = 1220
height = 720
screen_width = rootStructure.winfo_screenwidth()
screen_height = rootStructure.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
rootStructure.geometry("%dx%d+%d+%d" % (width, height, x, y))
rootStructure.resizable(0, 0)
rootStructure.config(background='white')

WELCOMELB = Label(rootStructure, text="Welcome", bg='white', font=('Times New Roman', 100, 'bold'))
WELCOMELB.pack()
WELCOMELB1 = Label(rootStructure, text="to our", bg='white', font=('Times New Roman', 100, 'bold'))
WELCOMELB1.pack()
WELCOMELB2 = Label(rootStructure, text="Login and Registration", bg='white', font=('Times New Roman', 100, 'bold'))
WELCOMELB2.pack()
WELCOMELB3 = Label(rootStructure, text="System", bg='white', font=('Times New Roman', 100, 'bold'))
WELCOMELB3.pack()

# *******************************************************VARIABLES******************************************************

ADMINUSERNAME_ID_VAR = StringVar()
ADMINPASS_VAR = StringVar()
ADMINSEARCH_VAR = StringVar()

USERACCNO_VAR = StringVar()
USERPIN_VAR = StringVar()
USERSEARCH_VAR = StringVar()

CALC_VAR = IntVar()
CALC_FIRSTNUM = IntVar()
CALC_SECONDNUM = IntVar()
CALC_TOTAL = IntVar()

# ***************************************************DATABASE***********************************************************

def adminsysdb():
    global conn, cursor
    conn = sqlite3.connect("registrationsys.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `users` (acc_no INTEGER PRIMARY KEY NOT NULL, pin INTEGER NOT NULL)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `administrators` (user_id TEXT PIRMARY KEY NOT NULL, password TEXT NOT NULL)")
    cursor.execute("SELECT * FROM `administrators` WHERE `user_id` = 'root' AND `password` = 'root'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `administrators` (user_id, password) VALUES('root', 'root')")
        conn.commit()


# *****************************************************METHODS**********************************************************

def EXIT():
    result = tkMessageBox.askquestion('Login and Registration System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        exit()

def adminlogout():
    result = tkMessageBox.askquestion('Login and Registration System', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes':
        adminmainmenuStructure.destroy()
        rootStructure.deiconify()
        adminloginmenu()


def userlogout():
    result = tkMessageBox.askquestion('Login and Registration System', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes':
        usermainmenuStructure.destroy()
        rootStructure.deiconify()
        userloginmenu()


# **************************************************SUCCESS MESSAGES****************************************************
def loginsuccess():
    tkMessageBox._show("Log in", 'Logged in successfully!')

def registersuccess():
    tkMessageBox._show("Register", 'Registered successfully!')


# **************************************************ADMIN LOGIN MENU****************************************************

def adminmainmenu():
    global adminmainmenuStructure
    adminmainmenuStructure = Tk()
    adminmainmenuStructure.title("Login and Registration System/Admin Main Menu")
    width = 1024
    height = 720
    screen_width = adminmainmenuStructure.winfo_screenwidth()
    screen_height = adminmainmenuStructure.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    adminmainmenuStructure.geometry("%dx%d+%d+%d" % (width, height, x, y))
    adminmainmenuStructure.resizable(0, 0)
    TOPFRAME = Frame(adminmainmenuStructure, relief=SOLID)
    TOPFRAME.pack(pady=10)
    MAINMENULB = Label(TOPFRAME, bg='white', text="Admin Tasks", font=('Times New Roman', 80))
    MAINMENULB.pack()
    adminmainmenuStructure.config(bg="white")

    ADMINMENUBAR = Menu(adminmainmenuStructure)
    FILECASCADE = Menu(ADMINMENUBAR, tearoff=0)
    REGISTRATIONCASCADE = Menu(ADMINMENUBAR, tearoff=0)
    VIEWUSERINFOCASCADE = Menu(ADMINMENUBAR, tearoff=0)
    VIEWADMININFOCASCADE = Menu(ADMINMENUBAR, tearoff=0)

    FILECASCADE.add_command(label="Log out", command=adminlogout)
    FILECASCADE.add_command(label="Exit", command=EXIT)
    REGISTRATIONCASCADE.add_command(label="Register A User", command=userregistermenu)
    REGISTRATIONCASCADE.add_command(label="Register An Admin", command=adminregistermenu)
    VIEWUSERINFOCASCADE.add_command(label="View User Accounts", command=userviewmainmenu)
    VIEWADMININFOCASCADE.add_command(label="View Admin Accounts", command=adminviewmainmenu)

    ADMINMENUBAR.add_cascade(label="File", menu=FILECASCADE)
    ADMINMENUBAR.add_cascade(label="Account Registration", menu=REGISTRATIONCASCADE)
    ADMINMENUBAR.add_cascade(label="User Accounts", menu=VIEWUSERINFOCASCADE)
    ADMINMENUBAR.add_cascade(label="Admin Accounts", menu=VIEWADMININFOCASCADE)

    adminmainmenuStructure.config(menu=ADMINMENUBAR)


def adminloginmenu():
    global adminloginformStructure
    adminloginformStructure = Toplevel()
    adminloginformStructure.title("Login and Registration System/Admin Account Login")
    width = 600
    height = 500
    screen_width = adminloginformStructure.winfo_screenwidth()
    screen_height = adminloginformStructure.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    adminloginformStructure.resizable(0, 0)
    adminloginformStructure.geometry("%dx%d+%d+%d" % (width, height, x, y))
    adminloginformStructure.config(bg='white')
    adminloginformcomponents()


def adminloginformcomponents():
    global RESULTLB
    TOPFORM = Frame(adminloginformStructure, bg='white', width=600, height=100, relief=SOLID)
    TOPFORM.pack(side=TOP, pady=10)
    ADMINLB = Label(TOPFORM, text="Admin Log in", bg='white', font=('Times New Roman', 60), width=600)
    ADMINLB.pack(fill=X)
    MIDDLEFRAME = Frame(adminloginformStructure, bg='white', width=600)
    MIDDLEFRAME.pack(side=TOP, pady=50)
    USERNAME_ID_LB = Label(MIDDLEFRAME, text="Username\ID:", bg='white', font=('Times New Roman', 30))
    USERNAME_ID_LB.grid(row=0)
    PASSLB = Label(MIDDLEFRAME, text="Password:", bg='white', font=('Times New Roman', 30))
    PASSLB.grid(row=1)
    RESULTLB = Label(MIDDLEFRAME, text="", bg='white', font=('Times New Roman', 28))
    RESULTLB.grid(row=5, columnspan=2)
    USERNAME_ID_ENTRY = Entry(MIDDLEFRAME, textvariable=ADMINUSERNAME_ID_VAR, font=('Times New Roman', 30), width=16, bd=10)
    USERNAME_ID_ENTRY.grid(row=0, column=1)
    PASS_ENTRY = Entry(MIDDLEFRAME, textvariable=ADMINPASS_VAR, font=('Times New Roman', 30), width=16, bd=10, show="*")
    PASS_ENTRY.grid(row=1, column=1)
    LOGINBT = Button(MIDDLEFRAME, text="Login", bg='white', font=('Times New Roman', 30), width=22, bd=10,command=adminlogin)
    LOGINBT.grid(row=4, columnspan=2)
    LOGINBT.bind('<Return>', adminlogin)


def adminlogin(event=None):
    global admin_id
    adminsysdb()
    if ADMINUSERNAME_ID_VAR.get == "" or ADMINPASS_VAR.get() == "":
        RESULTLB.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `administrators` WHERE `user_id` = ? AND `password` = ?",
                       (ADMINUSERNAME_ID_VAR.get(), ADMINPASS_VAR.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `administrators` WHERE `user_id` = ? AND `password` = ?",
                           (ADMINUSERNAME_ID_VAR.get(), ADMINPASS_VAR.get()))
            data = cursor.fetchone()
            admin_id = data[0]
            ADMINUSERNAME_ID_VAR.set("")
            ADMINPASS_VAR.set("")
            RESULTLB.config(text="")
            loginsuccess()
            adminloginformStructure.destroy()
            rootStructure.withdraw()
            adminmainmenu()

        else:
            RESULTLB.config(text="Invalid username/id or password", fg="red")
            ADMINUSERNAME_ID_VAR.set("")
            ADMINPASS_VAR.set("")
    cursor.close()
    conn.close()
# **************************************************VIEW/CHANGE ADMIN INFO***********************************************

def adminviewmainmenu():
    global adminviewmenuStructure
    adminviewmenuStructure = Toplevel()
    adminviewmenuStructure.title("Login and Registration System/Admin Accounts")
    width = 600
    height = 500
    screen_width = adminviewmenuStructure.winfo_screenwidth()
    screen_height = adminviewmenuStructure.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    adminviewmenuStructure.geometry("%dx%d+%d+%d" % (width, height, x, y))
    adminviewmenuStructure.resizable(0, 0)
    adminviewmenuStructure.config(bg='white')
    adminviewmainmenucomponents()


def adminviewmainmenucomponents():
    global adminTree
    TOPFRAME = Frame(adminviewmenuStructure, bg='white', width=600, relief=SOLID)
    TOPFRAME.pack(side=TOP, fill=X, pady=5)
    BOTTOMFRAME = Frame(adminviewmenuStructure, bg='white')
    BOTTOMFRAME.pack(side=BOTTOM, fill=Y)

    lbl_text = Label(TOPFRAME, text="Admin Accounts", bg='white', font=('Times New Roman', 60))
    lbl_text.grid(row=0, columnspan=7)
    lbl_txtsearch = Label(TOPFRAME, text="Search", bg='white', font=('Times New Roman', 25))
    lbl_txtsearch.grid(row=1, columnspan=7)
    search = Entry(TOPFRAME, textvariable=ADMINSEARCH_VAR, bg='white', font=('Times New Roman', 20), width=30, bd=10)
    search.grid(row=2, columnspan=3, padx=8)
    btn_search = Button(TOPFRAME, text="Search", bg='white', font=('Times New Roman', 20), bd=5, width=8,command=adminsearch)
    btn_search.grid(row=2, column=4)
    btn_reset = Button(TOPFRAME, text="Reset", bg='white', font=('Times New Roman', 20), bd=5, width=28,command=adminsearchreset)
    btn_reset.grid(row=3, column=2)
    btn_delete = Button(TOPFRAME, text="Delete", bg='white', font=('Times New Roman', 20), bd=5, width=28,command=admindelete)
    btn_delete.grid(row=4, column=2)

    scrollbarx = Scrollbar(BOTTOMFRAME, orient=HORIZONTAL)
    scrollbary = Scrollbar(BOTTOMFRAME, orient=VERTICAL)

    adminTree = ttk.Treeview(BOTTOMFRAME, columns=("Admin Username\ID", "Password"), selectmode="extended", height=20,yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=adminTree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=adminTree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    adminTree.heading('Admin Username\ID', text="Admin Username\ID", anchor=W)
    adminTree.heading('Password', text="Password", anchor=W)
    adminTree.column('#0', stretch=NO, minwidth=0, width=0)
    adminTree.column('#1', stretch=NO, minwidth=0, width=280)
    adminTree.column('#2', stretch=NO, minwidth=0, width=280)
    adminTree.pack()
    admindisplaydata()

def admindisplaydata():
    adminsysdb()
    cursor.execute("SELECT * FROM `administrators`")
    fetch = cursor.fetchall()
    for data in fetch:
        adminTree.insert('', 'end', values=data)
    cursor.close()
    conn.close()


def adminsearch():
    if ADMINSEARCH_VAR.get() != "":
        adminTree.delete(*adminTree.get_children())
        adminsysdb()
        cursor.execute("SELECT * FROM `administrators` WHERE `user_id` LIKE ?", ('%' + str(ADMINSEARCH_VAR.get()) + '%',))
        fetch = cursor.fetchall()
        for data in fetch:
            adminTree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

def adminsearchreset():
    adminTree.delete(*adminTree.get_children())
    admindisplaydata()
    ADMINSEARCH_VAR.set("")

def admindelete():
    if not adminTree.selection():
        tkMessageBox._show("Login and Registration System", "Please select a user name or ID!")
        adminviewmenuStructure.deiconify()
    else:
        result = tkMessageBox.askquestion('Login and Registration System', 'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            curItem = adminTree.focus()
            contents = (adminTree.item(curItem))
            selecteditem = contents['values']
            adminTree.delete(curItem)
            adminsysdb()
            cursor.execute("DELETE FROM `administrators` WHERE `user_id` = %s" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()
            adminviewmenuStructure.deiconify()
            rootStructure.withdraw()





# *************************************************ADMIN REGISTRATION*****************************************************


def adminregistermenu():
    global adminaddnewStructure
    adminaddnewStructure = Toplevel()
    adminaddnewStructure.title("Login and Registration System/Register ")
    width = 600
    height = 500
    screen_width = adminaddnewStructure.winfo_screenwidth()
    screen_height = adminaddnewStructure.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    adminaddnewStructure.geometry("%dx%d+%d+%d" % (width, height, x, y))
    adminaddnewStructure.resizable(0, 0)
    adminaddnewStructure.config(bg='white')
    adminregistermenucomponents()


def adminregistermenucomponents():
    global REGISTERRESULTLB
    TOPFRAME = Frame(adminaddnewStructure, bg='white', width=600, height=100, relief=SOLID)
    TOPFRAME.pack(side=TOP, pady=30)
    lbl_text = Label(TOPFRAME, text="Add New Admin", bg='white', font=('Times New Roman', 56), width=600)
    lbl_text.pack(fill=X)
    MIDDLEFRAME = Frame(adminaddnewStructure, bg='white', width=600)
    MIDDLEFRAME.pack(side=TOP, pady=5)
    ACCNO_LB = Label(MIDDLEFRAME, text="Admin ID:", bg='white', font=('Times New Roman', 28), bd=10)
    ACCNO_LB.grid(row=0, sticky=W)
    PIN_LB = Label(MIDDLEFRAME, text="Password:", bg='white', font=('Times New Roman', 30), bd=10)
    PIN_LB.grid(row=1, sticky=W)
    REGISTERRESULTLB = Label(MIDDLEFRAME, text="", bg='white', font=('Times New Roman', 30))
    REGISTERRESULTLB.grid(row=5, columnspan=2)
    USERNAME_ID_ENTRY = Entry(MIDDLEFRAME, textvariable=ADMINUSERNAME_ID_VAR, bg='white', font=('Times New Roman', 25), width=18, bd='10')
    USERNAME_ID_ENTRY.grid(row=0, column=1)
    PASS_ENTRY = Entry(MIDDLEFRAME, textvariable=ADMINPASS_VAR, bg='white', font=('Times New Roman', 25), width=18, bd='10', show="*")
    PASS_ENTRY.grid(row=1, column=1)
    btn_add = Button(MIDDLEFRAME, text="Register", bg='white', font=('Times New Roman', 30), width=24, bd='10',command=adminregisterindb)
    btn_add.grid(row=3, columnspan=2, pady=20)


def adminregisterindb():
    adminsysdb()
    if ADMINUSERNAME_ID_VAR.get == "" or ADMINPASS_VAR.get() == "":
        REGISTERRESULTLB.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("INSERT INTO `administrators` (user_id, password) VALUES(?, ?)", (int(ADMINUSERNAME_ID_VAR.get()), str(ADMINPASS_VAR.get())))
        conn.commit()
        ADMINUSERNAME_ID_VAR.set("")
        ADMINPASS_VAR.set("")
        cursor.close()
        conn.close()
        registersuccess()
        adminaddnewStructure.deiconify()

# *************************************************USER REGISTRATION*****************************************************


def userregistermenu():
    global addnewStructure
    addnewStructure = Toplevel()
    addnewStructure.title("Login and Registration System/Register ")
    width = 600
    height = 500
    screen_width = addnewStructure.winfo_screenwidth()
    screen_height = addnewStructure.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    addnewStructure.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewStructure.resizable(0, 0)
    addnewStructure.config(bg='white')
    userregistermenucomponents()


def userregistermenucomponents():
    global REGISTERRESULTLB
    TOPFRAME = Frame(addnewStructure, bg='white', width=600, height=100, relief=SOLID)
    TOPFRAME.pack(side=TOP, pady=30)
    lbl_text = Label(TOPFRAME, text="Add New Account", bg='white', font=('Times New Roman', 56), width=600)
    lbl_text.pack(fill=X)
    MIDDLEFRAME = Frame(addnewStructure, bg='white', width=600)
    MIDDLEFRAME.pack(side=TOP, pady=5)
    ACCNO_LB = Label(MIDDLEFRAME, text="Account No:", bg='white', font=('Times New Roman', 28), bd=10)
    ACCNO_LB.grid(row=0, sticky=W)
    PIN_LB = Label(MIDDLEFRAME, text="PIN:", bg='white', font=('Times New Roman', 30), bd=10)
    PIN_LB.grid(row=1, sticky=W)
    REGISTERRESULTLB = Label(MIDDLEFRAME, text="", bg='white', font=('Times New Roman', 30))
    REGISTERRESULTLB.grid(row=5, columnspan=2)
    ACCNO_ENTRY = Entry(MIDDLEFRAME, textvariable=USERACCNO_VAR, bg='white', font=('Times New Roman', 25), width=18, bd='10')
    ACCNO_ENTRY.grid(row=0, column=1)
    PIN_ENTRY = Entry(MIDDLEFRAME, textvariable=USERPIN_VAR, bg='white', font=('Times New Roman', 25), width=18, bd='10', show="*")
    PIN_ENTRY.grid(row=1, column=1)
    btn_add = Button(MIDDLEFRAME, text="Register", bg='white', font=('Times New Roman', 30), width=24, bd='10',command=userregisterindb)
    btn_add.grid(row=3, columnspan=2, pady=20)


def userregisterindb():
    adminsysdb()
    if USERACCNO_VAR.get == "" or USERPIN_VAR.get() == "":
        REGISTERRESULTLB.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("INSERT INTO `users` (acc_no, pin) VALUES(?, ?)", (int(USERACCNO_VAR.get()), int(USERPIN_VAR.get())))
        conn.commit()
        USERACCNO_VAR.set("")
        USERPIN_VAR.set("")
        cursor.close()
        conn.close()
        registersuccess()
        addnewStructure.deiconify()


# **************************************************VIEW/CHANGE USER INFO***********************************************
def userviewmainmenu():
    global userviewmenuStructure
    userviewmenuStructure = Toplevel()
    userviewmenuStructure.title("Login and Registration System/User Accounts")
    width = 600
    height = 500
    screen_width = userviewmenuStructure.winfo_screenwidth()
    screen_height = userviewmenuStructure.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    userviewmenuStructure.geometry("%dx%d+%d+%d" % (width, height, x, y))
    userviewmenuStructure.resizable(0, 0)
    userviewmenuStructure.config(bg='white')
    userviewmainmenucomponents()


def userviewmainmenucomponents():
    global tree
    TOPFRAME = Frame(userviewmenuStructure, bg='white', width=600, relief=SOLID)
    TOPFRAME.pack(side=TOP, fill=X, pady=5)
    BOTTOMFRAME = Frame(userviewmenuStructure, bg='white')
    BOTTOMFRAME.pack(side=BOTTOM, fill=Y)

    lbl_text = Label(TOPFRAME, text="User Accounts", bg='white', font=('Times New Roman', 60))
    lbl_text.grid(row=0, columnspan=7)
    lbl_txtsearch = Label(TOPFRAME, text="Search", bg='white', font=('Times New Roman', 25))
    lbl_txtsearch.grid(row=1, columnspan=7)
    search = Entry(TOPFRAME, textvariable=USERSEARCH_VAR, bg='white', font=('Times New Roman', 20), width=30, bd=10)
    search.grid(row=2, columnspan=3, padx=8)
    btn_search = Button(TOPFRAME, text="Search", bg='white', font=('Times New Roman', 20), bd=5, width=8,command=usersearch)
    btn_search.grid(row=2, column=4)
    btn_reset = Button(TOPFRAME, text="Reset", bg='white', font=('Times New Roman', 20), bd=5, width=28,command=usersearchreset)
    btn_reset.grid(row=3, column=2)
    btn_delete = Button(TOPFRAME, text="Delete", bg='white', font=('Times New Roman', 20), bd=5, width=28,command=userdelete)
    btn_delete.grid(row=4, column=2)

    scrollbarx = Scrollbar(BOTTOMFRAME, orient=HORIZONTAL)
    scrollbary = Scrollbar(BOTTOMFRAME, orient=VERTICAL)

    tree = ttk.Treeview(BOTTOMFRAME, columns=("Account No", "PIN"), selectmode="extended", height=20,yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Account No', text="Account No", anchor=W)
    tree.heading('PIN', text="PIN", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=280)
    tree.column('#2', stretch=NO, minwidth=0, width=280)

    tree.pack()
    userdisplaydata()


def userdisplaydata():
    adminsysdb()
    cursor.execute("SELECT * FROM `users`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


def usersearch():
    if USERSEARCH_VAR.get() != "":
        tree.delete(*tree.get_children())
        adminsysdb()
        cursor.execute("SELECT * FROM `users` WHERE `acc_no` LIKE ?", ('%' + str(USERSEARCH_VAR.get()) + '%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()


def usersearchreset():
    tree.delete(*tree.get_children())
    userdisplaydata()
    USERSEARCH_VAR.set("")


def userdelete():
    if not tree.selection():
        tkMessageBox._show("Login and Registration System", "Please select an account no!")
        userviewmenuStructure.deiconify()
    else:
        result = tkMessageBox.askquestion('Login and Registration System', 'Are you sure you want to delete this record?',icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            adminsysdb()
            cursor.execute("DELETE FROM `users` WHERE `acc_no` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()
            userviewmenuStructure.deiconify()
            rootStructure.withdraw()




# ********************************************************USER LOGIN****************************************************
def usermainmenu():
    global usermainmenuStructure
    usermainmenuStructure = Tk()
    usermainmenuStructure.title("Login and Registration System/Main Menu")
    width = 1024
    height = 720
    screen_width = usermainmenuStructure.winfo_screenwidth()
    screen_height = usermainmenuStructure.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    usermainmenuStructure.geometry("%dx%d+%d+%d" % (width, height, x, y))
    usermainmenuStructure.resizable(0, 0)
    usermainmenuStructure.config(bg='white')
    TOPFRAME = Frame(usermainmenuStructure, bg='white', relief=SOLID)
    TOPFRAME.pack(pady=10)
    LEFTSIDEFRAME = Frame(usermainmenuStructure, bg='white', width=600, height=600, relief=SOLID)
    LEFTSIDEFRAME.pack(side=LEFT)
    RIGHTSIDEFRAME = Frame(usermainmenuStructure, bg='white', width=400, height=600, relief=SOLID)
    RIGHTSIDEFRAME.pack(side=RIGHT)

    MAINMENULB = Label(TOPFRAME, bg='white', text="User Tasks", font=('Times New Roman', 80))
    MAINMENULB.pack()

    menubar = Menu(RIGHTSIDEFRAME)
    fileCascade = Menu(menubar, tearoff=0)
    calculatorCascade = Menu(menubar, tearoff=0)
    fileCascade.add_command(label="Log out", command=userlogout)
    fileCascade.add_command(label="Exit", command=EXIT)
    calculatorCascade.add_command(label="Calculator", command=calculator)
    menubar.add_cascade(label="File", font=('Times New Roman', 30), menu=fileCascade)
    menubar.add_cascade(label="Calculator", font=('Times New Roman', 30), menu=calculatorCascade)
    usermainmenuStructure.config(menu=menubar)


def userloginmenu():
    global userloginformStructure
    userloginformStructure = Toplevel()
    userloginformStructure.title("Login and Registration System/User Account Login")
    width = 600
    height = 500
    screen_width = userloginformStructure.winfo_screenwidth()
    screen_height = userloginformStructure.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    userloginformStructure.resizable(0, 0)
    userloginformStructure.geometry("%dx%d+%d+%d" % (width, height, x, y))
    userloginformStructure.config(bg='white')
    userloginformcomponents()


def userloginformcomponents():
    global USERLBRESULT
    USERTOPLOGINFORM = Frame(userloginformStructure, bg='white', width=600, height=100, relief=SOLID)
    USERTOPLOGINFORM.pack(side=TOP)
    USERLOGINLB = Label(USERTOPLOGINFORM, text="User Login", bg='white', font=('Times New Roman', 60), width=600)
    USERLOGINLB.pack(fill=X, pady=20)
    USERMIDLOGINFORM = Frame(userloginformStructure, bg='white', width=600)
    USERMIDLOGINFORM.pack(side=TOP)
    ACCOUNTNOLB = Label(USERMIDLOGINFORM, text="Account No:", bg='white', font=('Times New Roman', 30), bd=18)
    ACCOUNTNOLB.grid(row=0)
    PINLB = Label(USERMIDLOGINFORM, text="PIN:", bg='white', font=('Times New Roman', 30), bd=18)
    PINLB.grid(row=1)
    USERLBRESULT = Label(USERMIDLOGINFORM, text="", bg='white', font=('Times New Roman', 30))
    USERLBRESULT.grid(row=3, columnspan=2)
    USERNAME_ID_ENTRY = Entry(USERMIDLOGINFORM, textvariable=USERACCNO_VAR, bg='white', font=('Times New Roman', 30), width=15,bd=10)
    USERNAME_ID_ENTRY.grid(row=0, column=1)
    PIN_ENTRY = Entry(USERMIDLOGINFORM, textvariable=USERPIN_VAR, bg='white', font=('Times New Roman', 30), width=15,show="*", bd=10)
    PIN_ENTRY.grid(row=1, column=1)
    LOGINBT = Button(USERMIDLOGINFORM, text="Login", bg='white', font=('Times New Roman', 30), width=25, bd=10,command=userlogin)
    LOGINBT.grid(row=2, columnspan=2)
    LOGINBT.bind('<Return>', userlogin)


def userlogin(event=None):
    global user_Identification
    adminsysdb()

    if USERACCNO_VAR.get == "" or USERPIN_VAR.get() == "":
        USERLBRESULT.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `users` WHERE `acc_no` = ? AND `pin` = ?", (USERACCNO_VAR.get(), USERPIN_VAR.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `users` WHERE `acc_no` = ? AND `pin` = ?", (USERACCNO_VAR.get(), USERPIN_VAR.get()))
            data = cursor.fetchone()
            user_Identification = data[0]
            USERACCNO_VAR.set("")
            USERPIN_VAR.set("")
            USERLBRESULT.config(text="")
            loginsuccess()
            userloginformStructure.destroy()
            rootStructure.withdraw()
            usermainmenu()


        else:
            USERLBRESULT.config(text="Invalid account no or pin", fg="red")
            USERACCNO_VAR.set("")
            USERPIN_VAR.set("")
    cursor.close()
    conn.close()

# **************************************************CALCULATOR**********************************************************

def calculator():
    global calculatorStructure
    calculatorStructure = Toplevel()
    calculatorStructure.title("Login and Registration System/Calculator")
    width = 1000
    height = 620
    screen_width = calculatorStructure.winfo_screenwidth()
    screen_height = calculatorStructure.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    calculatorStructure.resizable(0, 0)
    calculatorStructure.geometry("%dx%d+%d+%d" % (width, height, x, y))
    calculatorStructure.config(bg='white')
    calculatorcomponents()


def calculatorcomponents():
    TopFrame = Frame(calculatorStructure, bg='white', pady=0)
    TopFrame.pack(side=TOP)
    RightFrame = Frame(calculatorStructure, bg='white', padx=20, pady=0)
    RightFrame.pack(side=RIGHT, anchor=E)
    LeftFrame = Frame(calculatorStructure, bg='white', padx=20, pady=0)
    LeftFrame.pack(side=LEFT)

    rb1 = Radiobutton(LeftFrame, text="Addition", bg='white', variable=CALC_VAR, value=1, font=('Times New Roman', 30), )
    rb1.grid(row=0, column=0, sticky=W)
    rb2 = Radiobutton(LeftFrame, text="Subtraction", bg='white', variable=CALC_VAR, value=2, font=('Times New Roman', 30))
    rb2.grid(row=1, column=0, sticky=W)
    rb3 = Radiobutton(LeftFrame, text="Multiplication", bg='white', variable=CALC_VAR, value=3, font=('Times New Roman', 30))
    rb3.grid(row=2, column=0, sticky=W)
    rb4 = Radiobutton(LeftFrame, text="Division", bg='white', variable=CALC_VAR, value=4, font=('Times New Roman', 30))
    rb4.grid(row=3, column=0, sticky=W)
    rb5 = Radiobutton(LeftFrame, text="Modulus", bg='white', variable=CALC_VAR, value=5, font=('Times New Roman', 30))
    rb5.grid(row=0, column=1, sticky=W)
    rb6 = Radiobutton(LeftFrame, text="Exponent", bg='white', variable=CALC_VAR, value=6, font=('Times New Roman', 30))
    rb6.grid(row=1, column=1, sticky=W)
    rb7 = Radiobutton(LeftFrame, text="Floor Division", bg='white', variable=CALC_VAR, value=7, font=('Times New Roman', 30))
    rb7.grid(row=2, column=1, sticky=W)

    titleCalculator = Label(TopFrame, bg='white', font=('Times New Roman', 90), text="Calculator")
    titleCalculator.grid(row=5, columnspan=2)
    lblFirstnum = Label(LeftFrame, bg='white', font=('Times New Roman', 30), text="Enter First Number : ")
    lblFirstnum.grid(row=4, column=0, sticky=W)
    txtFirstnum = Entry(LeftFrame, bg='white', font=('Times New Roman', 30), bd=10, width=13, textvariable=CALC_FIRSTNUM)
    txtFirstnum.grid(row=4, column=1)
    lblSecondnum = Label(LeftFrame, bg='white', font=('Times New Roman', 30), text="Enter Second Number: ")
    lblSecondnum.grid(row=5, column=0, sticky=W)
    txtSecondnum = Entry(LeftFrame, bg='white', font=('Times New Roman', 30), bd=10, width=13, textvariable=CALC_SECONDNUM)
    txtSecondnum.grid(row=5, column=1)
    lblTotal = Label(LeftFrame, bg='white', font=('Times New Roman', 30), text="The result:")
    lblTotal.grid(row=6, column=0, sticky=W)
    lblAnswer = Entry(LeftFrame, font=('Times New Roman', 30), bg="white", bd=10, width=13, textvariable=CALC_TOTAL)
    lblAnswer.grid(row=6, column=1, sticky=W)

    Button(RightFrame, bd=10, fg="white", font=('Times New Roman', 30), width=10, height=1, text="FutureUse",bg='white').pack()
    Button(RightFrame, bd=10, fg="white", font=('Times New Roman', 30), width=10, height=1, text="FutureUse",bg='white').pack()
    Button(RightFrame, bd=10, fg='white', font=('Times New Roman', 30), width=10, height=1, text="FutureUse",bg='white').pack()
    CalcbtnReset = Button(RightFrame, bd=10, fg="black", font=('Times New Roman', 30), width=10, height=1, text="Reset",bg="white", command=calculatorreset)
    CalcbtnReset.pack()
    CalcbtnTotal = Button(RightFrame, bd=10, fg="black", font=('Times New Roman', 30), width=10, height=1, text="Calculate",bg="white", command=calculatorfuncs)
    CalcbtnTotal.pack()


def calculatorreset():
    CALC_FIRSTNUM.set("0")
    CALC_SECONDNUM.set("0")
    CALC_TOTAL.set("0")


def calculatorfuncs():
    if CALC_VAR.get() == 1:
        first = float(CALC_FIRSTNUM.get())
        second = float(CALC_SECONDNUM.get())
        Sumpup = first + second
        CALC_TOTAL.set(Sumpup)
    elif CALC_VAR.get() == 2:
        first = float(CALC_FIRSTNUM.get())
        second = float(CALC_SECONDNUM.get())
        Sumpup = first - second
        CALC_TOTAL.set(Sumpup)
    elif CALC_VAR.get() == 3:
        first = float(CALC_FIRSTNUM.get())
        second = float(CALC_SECONDNUM.get())
        Sumpup = first * second
        CALC_TOTAL.set(Sumpup)
    elif CALC_VAR.get() == 4:
        first = float(CALC_FIRSTNUM.get())
        second = float(CALC_SECONDNUM.get())
        Sumpup = first / second
        CALC_TOTAL.set(Sumpup)
    elif CALC_VAR.get() == 5:
        first = float(CALC_FIRSTNUM.get())
        second = float(CALC_SECONDNUM.get())
        Sumpup = first % second
        CALC_TOTAL.set(Sumpup)
    elif CALC_VAR.get() == 6:
        first = float(CALC_FIRSTNUM.get())
        second = float(CALC_SECONDNUM.get())
        Sumpup = first ** second
        CALC_TOTAL.set(Sumpup)
    elif CALC_VAR.get() == 7:
        first = float(CALC_FIRSTNUM.get())
        second = float(CALC_SECONDNUM.get())
        Sumpup = first // second
        CALC_TOTAL.set(Sumpup)
    else:
        CALC_TOTAL.set("Select an option")


# **************************************************ROOT CASCADE MENUS**************************************************

ROOTMENUBAR = Menu(rootStructure)
userLOGINCASCADE = Menu(ROOTMENUBAR, tearoff=0)
adminLOGINCASCADE = Menu(ROOTMENUBAR, tearoff=0)
fileCASCADE = Menu(rootStructure, tearoff=0)
userLOGINCASCADE.add_command(label="User Log in", command=userloginmenu)
adminLOGINCASCADE.add_command(label="Admin Log in", command=adminloginmenu)
fileCASCADE.add_command(label="Exit", command=EXIT)

ROOTMENUBAR.add_cascade(label="File", menu=fileCASCADE)
ROOTMENUBAR.add_cascade(label="Admin", menu=adminLOGINCASCADE)
ROOTMENUBAR.add_cascade(label="User", menu=userLOGINCASCADE)
rootStructure.config(menu=ROOTMENUBAR)

rootStructure.mainloop()
