from tkinter import *
from tkinter import messagebox
import cryptography as crypto
from src import DBManipulation

action = DBManipulation
root = Tk()  # root is the window
root.geometry('700x500')
root.resizable(0, 0)
root.wm_iconbitmap('img/registration.ico')  # the img for the root, metel favicon
root.title('REGISTRATION PAGE')
root.configure(bg='#D3D3D3')
welcomeLabel = Label(root, text='WELCOME TO OUR\nFACE RECOGNITION APP', font=('normal', 25, 'bold'), bg='#D3D3D3')
welcomeLabel.place(x=150, y=50)

# Labels
fnameLabel = Label(root, text='FIRSTNAME', font=('arial', 14, 'bold'), bg='#D3D3D3')
fnameLabel.place(x=150, y=180)

lnameLabel = Label(root, text='LASTNAME', font=('arial', 14, 'bold'), bg='#D3D3D3')
lnameLabel.place(x=150, y=230)

unameLabel = Label(root, text='USERNAME*', font=('arial', 14, 'bold'), bg='#D3D3D3')
unameLabel.place(x=150, y=280)

passwordLabel = Label(root, text='PASSWORD*', font=('arial', 14, 'bold'), bg='#D3D3D3')
passwordLabel.place(x=150, y=330)

confpasswordLabel = Label(root, text='CONFIRM PASSWORD*', font=('arial', 14, 'bold'), bg='#D3D3D3')
confpasswordLabel.place(x=150, y=380)
# Storing Variables
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()
# Entry
fnameEntry = Entry(root, width=20, font=('normal', 15), bd=3, textvariable=var1)
fnameEntry.place(x=420, y=180)

lnameEntry = Entry(root, width=20, font=('normal', 15), bd=3, textvariable=var2)
lnameEntry.place(x=420, y=230)

unameEntry = Entry(root, width=20, font=('normal', 15), bd=3, textvariable=var3)
unameEntry.place(x=420, y=280)

passwordEntry = Entry(root, width=20, font=('normal', 15), bd=3, textvariable=var4, show='*')  # to hide the password
passwordEntry.place(x=420, y=330)

confpasswordEntry = Entry(root, width=20, font=('normal', 15), bd=3, textvariable=var5, show='*')
confpasswordEntry.place(x=420, y=380)

action.__init__(action)
action.openCon(action)


def submit():
    fname = var1.get()
    lname = var2.get()
    uname = var3.get()
    passwd = var4.get()
    confpasswd = var5.get()
    # action.createAdmin(fname, lname, uname, passwd)
    # For testing
    # print('Firstname: ', fname)
    # print('Lastname: ', lname)
    # print('Username: ', uname)
    # print('Password: ', passwd)
    # print('Confirm Password: ', confpasswd)


registerButton = Button(root, text='REGISTER', font=('normal', 15), bd=3, command=submit)
registerButton.place(x=260, y=420)
# action.closeCon(action.connection)
root.mainloop()
