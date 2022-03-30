from tkinter import*
import tkinter.messagebox
import PtntDatabase
import random


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


if __name__ == '__main__':
    root = Tk()
    application = Dentist(root)
    root.mainloop()
