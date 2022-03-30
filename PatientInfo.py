from tkinter import*
import tkinter.messagebox
import PtntDatabase
import random

# Frontend


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


if __name__ == '__main__':
    root = Tk()
    application = Patient(root)
    root.mainloop()
