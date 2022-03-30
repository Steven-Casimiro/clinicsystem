import random
import time
import datetime
from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import PtntDatabase
from tkcalendar import*
import os

def main():
    root = Tk()
    app = mainpage(root)
    root.mainloop()
#===================================================Login Page Setup============================================================
class mainpage:
    def __init__(self,master):
        self.master = master
        self.master.title("Clinic Management System")
        self.master.geometry("1280x750+0+0")
        self.frame = Frame(self.master)
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        global username_verify
        global password_verify

        self.username_verify = StringVar()
        self.password_verify = StringVar()

        self.LabelTitle = Label(self.frame, text="       Clinic Management System       ",font = ("calibri",40,"bold"),
                                bd = 10,relief = "sunken")
        self.LabelTitle.grid(row=0,column=0,columnspan=2,pady=20)

        self.Loginframe1 = Frame(self.frame, width = 1000, height = 300, bd = 10, relief = "groove")
        self.Loginframe1.grid(row=1, column=0)

        self.Loginframe2 = Frame(self.frame, width = 1000, height = 100, bd = 10, relief = "groove")
        self.Loginframe2.grid(row=2, column=0, pady = 15)

        self.Loginframe3 = Frame(self.frame, width = 1000, height = 200, bd = 10, relief = "groove")
        self.Loginframe3.grid(row=6, column=0, pady = 5)
# ===================================================Buttons for Other Pages============================================================
        self.button_reg = Button(self.Loginframe3, text = "Patient Records",state = DISABLED, font = ("calibri",15,"bold"),
                                 command = self.PatientReg_window)
        self.button_reg.grid(row = 0, column = 0, padx=10, pady=10)

        self.button_Dent = Button(self.Loginframe3, text = "Calendar",state = DISABLED, font = ("calibri",15,"bold"),
                                 command = self.calendar)
        self.button_Dent.grid(row = 1, column =0 , padx=10, pady=10)

        self.button_Pro = Button(self.Loginframe3, text = "Dentist Records",state = DISABLED, font = ("calibri",15,"bold"),
                                 command = self.Dentist_window)
        self.button_Pro.grid(row = 0, column = 1, padx=10, pady=10)

        # ===================================================Username + Password Entry Fields============================================================

        self.LabelUsername = Label(self.Loginframe1, text="Username", font = ("calibri",20,"bold"),bd=3)
        self.LabelUsername.grid(row = 0, column = 0)

        self.txtUsername = Entry(self.Loginframe1,font=("calibri",20,"bold"),bd = 3, textvariable = self.username_verify)
        self.txtUsername.grid(row = 0, column = 1, padx = 40, pady =15)

        self.txtPassword = Entry(self.Loginframe1, font=("calibri", 20, "bold"), bd=3, show = "*", textvariable=self.password_verify)
        self.txtPassword.grid(row=1, column=1, padx=40, pady=15)

        self.LabelPassword = Label(self.Loginframe1, text="Password", font=("calibri", 20, "bold"), bd=3)
        self.LabelPassword.grid(row=1, column=0)

#===================================================Login,Exit,Sign Up Buttons============================================================
        self.button_login = Button(self.Loginframe2, text = "Login", width = 20, font =("calibri",18,"bold"),
                                   command = self.login_verify)
        self.button_login.grid(row = 0,column =0, padx = 10, pady = 10)

        self.button_sign_up = Button(self.Loginframe2, text = "Sign Up", width = 20, font =("calibri",18,"bold"),
                                   command = self.sign_up_window)
        self.button_sign_up.grid(row = 0,column =1, padx = 10, pady = 10)

        self.button_exit = Button(self.Loginframe2, text = "Exit", width = 20, font =("calibri",18,"bold"),
                                   command = self.exit_btn)
        self.button_exit.grid(row = 0,column =3, padx = 10, pady = 10)



# ===================================================Login System Code============================================================
    def login_verify(self):
        user = self.Username.get()
        pswd = self.Password.get()

        username1 = self.username_verify.get()
        password1 = self.password_verify.get()

        list_of_files = os.listdir()

        if username1 in list_of_files:
            file1 = open(username1, "r")
            verify = file1.read().splitlines()
            if password1 in verify:
                self.button_reg.config(state=NORMAL)
                #self.button_App.config(state=NORMAL)
                self.button_Dent.config(state=NORMAL)
                self.button_Pro.config(state=NORMAL)

            else:
                tkinter.messagebox.askyesno("Clinic Management System:", "Invalid Password")
                self.button_reg.config(state=DISABLED)
                #self.button_App.config(state=DISABLED)
                self.button_Dent.config(state=DISABLED)
                self.button_Pro.config(state=DISABLED)

        else:
            tkinter.messagebox.askyesno("Clinic Management System:", "Invalid Username")
            self.button_reg.config(state=DISABLED)
            #self.button_App.config(state=DISABLED)
            self.button_Dent.config(state=DISABLED)
            self.button_Pro.config(state=DISABLED)
            #if user name or password is incorrect it will be disabled

            self.username_verify.set("")
            self.password_verify.set("")
            self.txtUsername.focus()



    def exit_btn(self):
        self.exit_btn = tkinter.messagebox.askyesno("Clinic Management System", "Are you sure you want to exit?")
        if self.exit_btn > 0:
            self.master.destroy()
            return


# ===================================================Function to bring up certain window============================================================
    def PatientReg_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Patient(self.newWindow)

    def Dentist_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Dentist(self.newWindow)

    def calendar(self):
        self.newWindow = Toplevel(self.master)
        self.app = calendar(self.newWindow)

    def sign_up_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = sign_up(self.newWindow)


#===================================================Code for other windows============================================================

class sign_up:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign Up")
        self.root.geometry("300x250")
        self.root.config(bg="grey")

        username = StringVar()
        password = StringVar()
        global username_entry
        global password_entry

        def sign_in_user():
            username_info = username.get()
            password_info = password.get()

            file=open(username_info,"w")
            file.write(username_info+"\n")
            file.write(password_info)
            file.close()

            self.txtunm.delete(0, END)
            self.txtpswd.delete(0, END)

            self.pop = Label(self.root, text = "Sign Up Succesful", fg = "green", font = ("calibri",11)).pack()

        self.lblprmpt = Label(self.root, text="Please Enter Details Below", bg = "grey").pack()
        self.lblblank = Label(self.root, text="", font=("calibri", 12)).pack()
        self.lblunm = Label(self.root, text = "Username * ", bg = "grey").pack()
        username_entry = self.txtunm = Entry(self.root, textvariable = username)
        username_entry.pack()
        self.lblpswd = Label(self.root, text = "Password * ", bg = "grey").pack()
        password_entry = self.txtpswd = Entry(self.root, textvariable=password)
        password_entry.pack()
        self.button_sign_up = Button(self.root, text = "Sign Up", width = 10, height = 1, command = sign_in_user ).pack()




class Patient:

    def __init__(self, root):
        self.root = root
        self.root.title("Patient Database")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="white")

        PtntID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        DoB = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()
        Allergies = StringVar()
        CM = StringVar()
        PM = StringVar()
        PS = StringVar()

        # =========================================Function Declaration================================================

        def iExit():
            iExit = tkinter.messagebox.askyesno("Patient Database", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def ClearData():
            self.txtPtntID.delete(0, END)
            self.txtfna.delete(0, END)
            self.txtsna.delete(0, END)
            self.txtDoB.delete(0, END)
            self.txtAge.delete(0, END)
            self.txtGender.delete(0, END)
            self.txtAdr.delete(0, END)
            self.txtMobile.delete(0, END)
            self.txtAll.delete(0, END)
            self.txtMC.delete(0, END)
            self.txtPM.delete(0, END)
            self.txtPS.delete(0, END)

        def addData():
            if (len(PtntID.get()) != 0):
                PtntDatabase.addPatientRec(PtntID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(),
                                      Address.get(), Mobile.get(), Allergies.get(), CM.get(), PM.get(), PS.get())
                patientlist.delete(0, END)
                patientlist.insert(END, (
                PtntID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(),
                Mobile.get()))

        def DisplayData():
            patientlist.delete(0, END)
            for row in PtntDatabase.viewData():
                patientlist.insert(END, row, str(""))

        def PatientRec(event):
            global pt
            searchPatient = patientlist.curselection() [0]
            pt = patientlist.get(searchPatient)

            self.txtPtntID.delete(0, END)
            self.txtPtntID.insert(END, pt[1])
            self.txtfna.delete(0, END)
            self.txtfna.insert(END, pt[2])
            self.txtsna.delete(0, END)
            self.txtsna.insert(END, pt[3])
            self.txtDoB.delete(0, END)
            self.txtDoB.insert(END, pt[4])
            self.txtAge.delete(0, END)
            self.txtAge.insert(END, pt[5])
            self.txtGender.delete(0, END)
            self.txtGender.insert(END, pt[6])
            self.txtAdr.delete(0, END)
            self.txtAdr.insert(END, pt[7])
            self.txtMobile.delete(0, END)
            self.txtMobile.insert(END, pt[8])
            self.txtAll.delete(0, END)
            self.txtAll.insert(END, pt[9])
            self.txtMC.delete(0, END)
            self.txtMC.insert(END, pt[10])
            self.txtPM.delete(0, END)
            self.txtPM.insert(END, pt[11])
            self.txtPS.delete(0, END)
            self.txtPS.insert(END, pt[12])

        def DeleteDate():
            if (len(PtntID.get()) != 0):
                PtntDatabase.deleteRec(pt[0])
                ClearData()
                DisplayData()

        def searchPatient():
            patientlist.delete(0,END)
            for row in PtntDatabase.searchData(PtntID.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(), \
                                               Gender.get(),Address.get(),Mobile.get(),Allergies.get(),CM.get(),PM.get(),PS.get()):
                patientlist.insert(END,row,str(""))


        def update():
            if (len(PtntID.get()) != 0):
                PtntDatabase.deleteRec(pt[0])
            if (len(PtntID.get()) != 0):
                PtntDatabase.addPatientRec(PtntID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(),
                                      Address.get(), Mobile.get(),Allergies.get(),CM.get(),PM.get(),PS.get())
                patientlist.delete(0, END)
                patientlist.insert(END, (
                PtntID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(),
                Mobile.get(),Allergies.get(),CM.get(),PM.get(),PS.get()))

        def PatientID_Number():
            rannumber = random.randint(10000,99999)
            randomnumber = str(rannumber)
            PtntID.set(randomnumber)

        # =========================================Frame================================================================
        MainFrame = Frame(self.root, bg="bisque")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="Ghost White", relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame, font=('arial', 47, 'bold'), text="Patient Database",
                            bg="Ghost White")
        self.lblTit.grid(sticky=W)

        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="Ghost White", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE, bg="white")
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, relief=RIDGE
                                   , font=('arial', 20, 'bold'), text="Patient Info\n", bg="Ghost White")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, relief=RIDGE
                                    , font=('arial', 20, 'bold'), bg="Ghost White")
        DataFrameRIGHT.pack(side=RIGHT)
        # =========================================Labels and Entrys===============================================
        self.lblPtntID = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Patient ID:", padx=2, pady=2,
                              bg="Ghost White")
        self.lblPtntID.grid(row=0, column=0, sticky=W)
        self.txtPtntID = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=PtntID, width=39)
        self.txtPtntID.grid(row=0, column=1)

        self.lblfna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Firstname:", padx=2, pady=2,
                            bg="Ghost White")
        self.lblfna.grid(row=1, column=0, sticky=W)
        self.txtfna = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Firstname, width=39)
        self.txtfna.grid(row=1, column=1)

        self.lblsna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Surname:", padx=2, pady=2,
                            bg="Ghost White")
        self.lblsna.grid(row=2, column=0, sticky=W)
        self.txtsna = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Surname, width=39)
        self.txtsna.grid(row=2, column=1)

        self.lblDoB = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Date of Birth:", padx=2, pady=3,
                            bg="Ghost White")
        self.lblDoB.grid(row=3, column=0, sticky=W)
        self.txtDoB = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=DoB, width=39)
        self.txtDoB.grid(row=3, column=1)

        self.lblAge = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Age:", padx=2, pady=3, bg="Ghost White")
        self.lblAge.grid(row=4, column=0, sticky=W)
        self.txtAge = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Age, width=39)
        self.txtAge.grid(row=4, column=1)

        self.lblGender = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Gender:", padx=2, pady=3,
                               bg="Ghost White")
        self.lblGender.grid(row=5, column=0, sticky=W)
        self.txtGender = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Gender, width=39)
        self.txtGender.grid(row=5, column=1)

        self.lblAdr = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Address:", padx=2, pady=3,
                            bg="Ghost White")
        self.lblAdr.grid(row=6, column=0, sticky=W)
        self.txtAdr = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Address, width=39)
        self.txtAdr.grid(row=6, column=1)

        self.lblMobile = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Mobile :", padx=2, pady=3,
                               bg="Ghost White")
        self.lblMobile.grid(row=7, column=0, sticky=W)
        self.txtMobile = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Mobile, width=39)
        self.txtMobile.grid(row=7, column=1)

        self.lblAll = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Allergies:", padx=2, pady=3,
                               bg="Ghost White")
        self.lblAll.grid(row=8, column=0, sticky=W)
        self.txtAll = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Allergies, width=39)
        self.txtAll.grid(row=8, column=1)

        self.lblMC = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Current Medications:", padx=2, pady=3,
                               bg="Ghost White")
        self.lblMC.grid(row=9, column=0, sticky=W)
        self.txtMC = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=CM, width=39)
        self.txtMC.grid(row=9, column=1)

        self.lblPM = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Past Medications:", padx=2, pady=3,
                               bg="Ghost White")
        self.lblPM.grid(row=10, column=0, sticky=W)
        self.txtPM = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=PM, width=39)
        self.txtPM.grid(row=10, column=1)

        self.lblPS = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Past Surgeries:", padx=2, pady=3,
                               bg="Ghost White")
        self.lblPS.grid(row=11, column=0, sticky=W)
        self.txtPS = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=PS, width=39)
        self.txtPS.grid(row=11, column=1)
        # =========================================Listbox and Scrollbar===============================================

        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')

        patientlist = Listbox(DataFrameRIGHT, width=41, height=16, font=('arial', 12, 'bold'),
                              yscrollcommand=scrollbar.set)
        patientlist.bind('<<ListboxSelect>>', PatientRec)
        patientlist.grid(row=0, column=0, padx=12)
        scrollbar.config(command=patientlist.yview)
        # =========================================Buttons Widget=====================================================
        self.btnApplyID = Button(ButtonFrame, text='Apply ID', font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                 command=PatientID_Number)
        self.btnApplyID.grid(row=0, column=0)

        self.btnAddData = Button(ButtonFrame, text='Add New', font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                 command=addData)
        self.btnAddData.grid(row=0, column=1)

        self.btnDisplayData = Button(ButtonFrame, text='Display', font=('arial', 20, 'bold'), height=1, width=10,
                                     bd=4, command=DisplayData)
        self.btnDisplayData.grid(row=0, column=2)

        self.btnClearData = Button(ButtonFrame, text='Clear', font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                   command=ClearData)
        self.btnClearData.grid(row=0, column=3)

        self.btnDeleteData = Button(ButtonFrame, text='Delete', font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                    command=DeleteDate)
        self.btnDeleteData.grid(row=0, column=4)

        self.btnSearchData = Button(ButtonFrame, text='Search', font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                    command=searchPatient)
        self.btnSearchData.grid(row=0, column=5)

        self.btnUpdateData = Button(ButtonFrame, text='Update', font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                    command=update)
        self.btnUpdateData.grid(row=0, column=6)

        self.btnExit = Button(ButtonFrame, text='Exit', font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                              command=iExit)
        self.btnExit.grid(row=0, column=7)



class Dentist:

    def __init__(self, root):
        self.root = root
        self.root.title("Dentist Database")
        self.root.geometry("1450x850+0+0")
        self.root.config(bg="white")

        DentistID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        DoB = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()

        # =========================================Function Declaration================================================

        def iExitDentist():
            iExit = tkinter.messagebox.askyesno("Dentist Database", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def ClearDentistData():
            self.txtDentID.delete(0, END)
            self.txtfna.delete(0, END)
            self.txtsna.delete(0, END)
            self.txtDoB.delete(0, END)
            self.txtAge.delete(0, END)
            self.txtGender.delete(0, END)
            self.txtAdr.delete(0, END)
            self.txtMobile.delete(0, END)

        def addDentistData():
            if (len(DentistID.get()) != 0):
                PtntDatabase.addDentistRec(DentistID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(),
                                      Address.get(), Mobile.get())
                dentistlist.delete(0, END)
                dentistlist.insert(END, (
                DentistID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(),
                Mobile.get()))

        def DisplayDentistData():
            dentistlist.delete(0, END)
            for row in PtntDatabase.viewDentistData():
                dentistlist.insert(END, row, str(""))

        def DentistRec(event):
            global dt
            searchDent = dentistlist.curselection()[0]
            dt = dentistlist.get(searchDent)

            self.txtDentID.delete(0, END)
            self.txtDentID.insert(END, dt[1])
            self.txtfna.delete(0, END)
            self.txtfna.insert(END, dt[2])
            self.txtsna.delete(0, END)
            self.txtsna.insert(END, dt[3])
            self.txtDoB.delete(0, END)
            self.txtDoB.insert(END, dt[4])
            self.txtAge.delete(0, END)
            self.txtAge.insert(END, dt[5])
            self.txtGender.delete(0, END)
            self.txtGender.insert(END, dt[6])
            self.txtAdr.delete(0, END)
            self.txtAdr.insert(END, dt[7])
            self.txtMobile.delete(0, END)
            self.txtMobile.insert(END, dt[8])

        def DeleteDentistData():
            if (len(DentistID.get()) != 0):
                PtntDatabase.deleteDentistRec(dt[0])
                ClearDentistData()
                DisplayDentistData()

        def searchDentistDatabase():
            dentistlist.delete(0, END)
            for row in PtntDatabase.searchDentistData(DentistID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(),
                                              Gender.get(), Address.get(), Mobile.get()):
                dentistlist.insert(END, row, str(""))

        def Dentistupdate():
            if (len(DentistID.get()) != 0):
                PtntDatabase.deleteDentistRec(dt[0])
            if (len(DentistID.get()) != 0):
                PtntDatabase.addDentistRec(DentistID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(),
                                      Address.get(), Mobile.get())
                dentistlist.delete(0, END)
                dentistlist.insert(END, (
                DentistID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(),
                Mobile.get()))

        def DentistID_Random():
            rannumber = random.randint(10000, 99999)
            randomnumber = str(rannumber)
            DentistID.set(randomnumber)

        # =========================================Frame================================================================
        MainFrame = Frame(self.root, bg="white")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="Ghost White", relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame, font=('arial', 47, 'bold'), text="Dentist Database",
                            bg="Ghost White")
        self.lblTit.grid(sticky=W)

        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="Ghost White", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE, bg="white")
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000, height=1000, padx=20, relief=RIDGE
                                   , font=('arial', 30, 'bold'), text="Dentist Info\n", bg="Ghost White")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=650, height=300, padx=31, pady=3, relief=RIDGE
                                    , font=('arial', 20, 'bold'), bg="Ghost White")
        DataFrameRIGHT.pack(side=RIGHT)
        # =========================================Labels and Entrys===============================================
        self.lblDentID = Label(DataFrameLEFT, font=('arial', 25, 'bold'), text="Dentist ID:", padx=2, pady=2,
                              bg="Ghost White")
        self.lblDentID.grid(row=0, column=0, sticky=W)
        self.txtDentID = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=DentistID, width=39)
        self.txtDentID.grid(row=0, column=1)

        self.lblfna = Label(DataFrameLEFT, font=('arial', 25, 'bold'), text="Firstname:", padx=2, pady=2,
                            bg="Ghost White")
        self.lblfna.grid(row=1, column=0, sticky=W)
        self.txtfna = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Firstname, width=39)
        self.txtfna.grid(row=1, column=1)

        self.lblsna = Label(DataFrameLEFT, font=('arial', 25, 'bold'), text="Surname:", padx=2, pady=2,
                            bg="Ghost White")
        self.lblsna.grid(row=2, column=0, sticky=W)
        self.txtsna = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Surname, width=39)
        self.txtsna.grid(row=2, column=1)

        self.lblDoB = Label(DataFrameLEFT, font=('arial', 25, 'bold'), text="Date of Birth:", padx=2, pady=3,
                            bg="Ghost White")
        self.lblDoB.grid(row=3, column=0, sticky=W)
        self.txtDoB = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=DoB, width=39)
        self.txtDoB.grid(row=3, column=1)

        self.lblAge = Label(DataFrameLEFT, font=('arial', 25, 'bold'), text="Age:", padx=2, pady=3, bg="Ghost White")
        self.lblAge.grid(row=4, column=0, sticky=W)
        self.txtAge = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Age, width=39)
        self.txtAge.grid(row=4, column=1)

        self.lblGender = Label(DataFrameLEFT, font=('arial', 25, 'bold'), text="Gender:", padx=2, pady=3,
                               bg="Ghost White")
        self.lblGender.grid(row=5, column=0, sticky=W)
        self.txtGender = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Gender, width=39)
        self.txtGender.grid(row=5, column=1)

        self.lblAdr = Label(DataFrameLEFT, font=('arial', 25, 'bold'), text="Address:", padx=2, pady=3,
                            bg="Ghost White")
        self.lblAdr.grid(row=6, column=0, sticky=W)
        self.txtAdr = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Address, width=39)
        self.txtAdr.grid(row=6, column=1)

        self.lblMobile = Label(DataFrameLEFT, font=('arial', 25, 'bold'), text="Mobile :", padx=2, pady=3,
                               bg="Ghost White")
        self.lblMobile.grid(row=7, column=0, sticky=W)
        self.txtMobile = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Mobile, width=39)
        self.txtMobile.grid(row=7, column=1)
        # =========================================Listbox and Scrollbar===============================================

        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')

        dentistlist = Listbox(DataFrameRIGHT, width=65, height=16, font=('arial', 12, 'bold'),
                              yscrollcommand=scrollbar.set)
        dentistlist.bind('<<ListboxSelect>>', DentistRec)
        dentistlist.grid(row=0, column=0, padx=8)
        scrollbar.config(command=dentistlist.yview)
        # =========================================Buttons=====================================================
        self.btnApplyID = Button(ButtonFrame, text='Apply ID', font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                 command=DentistID_Random)
        self.btnApplyID.grid(row=0, column=0)

        self.btnAddData = Button(ButtonFrame, text='Add New', font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                 command=addDentistData)
        self.btnAddData.grid(row=0, column=1)

        self.btnDisplayData = Button(ButtonFrame, text='Display', font=('arial', 20, 'bold'), height=1, width=10,
                                     bd=4, command=DisplayDentistData)
        self.btnDisplayData.grid(row=0, column=2)

        self.btnClearData = Button(ButtonFrame, text='Clear', font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                   command=ClearDentistData)
        self.btnClearData.grid(row=0, column=3)

        self.btnDeleteData = Button(ButtonFrame, text='Delete', font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                    command=DeleteDentistData)
        self.btnDeleteData.grid(row=0, column=4)

        self.btnSearchData = Button(ButtonFrame, text='Search', font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                    command=searchDentistDatabase)
        self.btnSearchData.grid(row=0, column=5)

        self.btnUpdateData = Button(ButtonFrame, text='Update', font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                    command=Dentistupdate)
        self.btnUpdateData.grid(row=0, column=6)

        self.btnExit = Button(ButtonFrame, text='Exit', font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                              command=iExitDentist)
        self.btnExit.grid(row=0, column=7)






class calendar:
    def __init__(self,root):
        self.master = root
        self.master.title('Monthly Calendar')
        self.master.geometry("986x700+0+0")

        MainFrame = Frame(root, bd=10, width=1350, height=700, relief=RIDGE, bg="white")
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=7, width=1340, height=100, relief=RIDGE)
        TitleFrame.grid(row=0, column=0)

        TopFrame3 = Frame(MainFrame, bd=5, width=1340, height=500, relief=RIDGE)
        TopFrame3.grid(row=1, column=0)

        LeftFrame = Frame(TopFrame3, bd=5, width=1340, height=400, padx=2, bg="white", relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame, bd=5, width=600, height=180, padx=2, pady=4, relief=RIDGE)
        LeftFrame1.pack(side=TOP, padx=10, pady=14)

        RightFrame1 = Frame(TopFrame3, bd=8, width=320, height=400, padx=2, bg="white", relief=RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1, bd=5, width=310, height=300, padx=2, pady=2, relief=RIDGE)
        RightFrame1a.pack(side=TOP)

        lblTitle = Label(TitleFrame, font=('Calibri', 40, 'bold'), text="Calendar", bd=7)
        lblTitle.grid(row=0, column=0, padx=66)  # 28

        FieldFrame = Frame(LeftFrame1, bd=2, width=400, height=20, padx=2, pady=10, bg="Ghost White", relief=RIDGE)
        FieldFrame.grid(row=2,column=0)


        cal = Calendar(LeftFrame1, selectmode="day", date_pattern='dd/mm/y',
                       font=('calibri', 12, 'bold'))
        cal.grid(row=0, column=0, padx=10)

        def iExit():
            iExit = tkinter.messagebox.askyesno("Monthly Calendar", "Confirm if you want to exit")
            if iExit > 0:
                self.master.destroy()
                return

        # ===================================================Buttons================================================


        btnExit = Button(RightFrame1a, padx=18, bd=7, font=('Helvetica', 12, 'bold'), width=17, command=iExit,
                         text="Exit", bg="white")
        btnExit.grid(row=2, column=0, padx=10, pady=2)


if __name__ =="__main__":
    main()