from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import PtntDatabase
import random
import time


class Dentist:

    def __init__(self, root):
        self.root = root
        self.root.title("Appointment Registration")
        self.root.geometry("1450x850+0+0")
        self.root.config(bg="white")

        Date_of_AppointmentReg = StringVar()
        Date_of_AppointmentReg.set(time.strftime("%d/%m/%y"))
        Appointment_ID = StringVar()
        Station_Number = StringVar()
        Patient_ID = StringVar()
        Fee = StringVar()
        Reason = StringVar()
        Procedure = StringVar()

        var1 = StringVar()

        Appointment = StringVar()
        Appointment.set("0")

        # =========================================Function Declaration================================================

        def iExitAppointment():
            iExit = tkinter.messagebox.askyesno("Appointment Registration", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def ClearAppointmentData():
            self.txtApptID.delete(0, END)
            self.txtpat.delete(0, END)
            self.txtsn.delete(0, END)
            self.txtrsn.delete(0, END)
            self.txtpname.delete(0, END)
            self.txtfee.delete(0, END)
            var1.set("0")
            self.appt_paymetcmb.current(0)

        def addAppointmentData():
            if (len(Appointment_ID.get()) != 0):
                PtntDatabase.addAppointmentRec(Appointment_ID.get(), Station_Number.get(), Patient_ID.get(), Fee.get(), Reason.get(), Procedure.get(), var1.get())
                appointmentlist.delete(0, END)
                appointmentlist.insert(END, (
                Appointment_ID.get(), Station_Number.get(), Patient_ID.get(), Fee.get(), Reason.get(), Procedure.get(), var1.get()))

        def DisplayAppointmentData():
            appointmentlist.delete(0, END)
            for row in PtntDatabase.viewAppointmentData():
                appointmentlist.insert(END, row, str(""))

        def AppointmentRec(event):
            global at
            searchAppt = appointmentlist.curselection()[0]
            at = appointmentlist.get(searchAppt)

            self.txtApptID.delete(0, END)
            self.txtApptID.insert(END, at[1])
            self.txtpat.delete(0, END)
            self.txtpat.insert(END, at[2])
            self.txtsn.delete(0, END)
            self.txtsn.insert(END, at[3])
            self.txtrsn.delete(0, END)
            self.txtrsn.insert(END, at[4])
            self.txtpname.delete(0, END)
            self.txtpname.insert(END, at[5])
            self.txtfee.delete(0, END)
            self.txtfee.insert(END, at[6])
            self.appt_paymetcmb.delete(0, END)
            self.appt_paymetcmb.insert(END, at[7])

        def DeleteAppointmentData():
            if (len(Appointment_ID.get()) != 0):
                PtntDatabase.deleteAppointmentRec(at[0])
                ClearAppointmentData()
                DisplayAppointmentData()

        def searchDentistDatabase():
            appointmentlist.delete(0, END)
            for row in PtntDatabase.searchAppointmentData(Appointment_ID.get(), Station_Number.get(), Patient_ID.get(), Fee.get(), Reason.get(), Procedure.get(),var1.get() ):
                appointmentlist.insert(END, row, str(""))

        def Dentistupdate():
            if (len(Appointment_ID.get()) != 0):
                PtntDatabase.deleteAppointmentRec(at[0])
            if (len(Appointment_ID.get()) != 0):
                PtntDatabase.addAppointmentRec(Appointment_ID.get(), Station_Number.get(), Patient_ID.get(), Fee.get(), Reason.get(), Procedure.get(), var1.get())
                appointmentlist.delete(0, END)
                appointmentlist.insert(END, (
                Appointment_ID.get(), Station_Number.get(), Patient_ID.get(), Fee.get(), Reason.get(), Procedure.get(), var1.get()))

        def DentistID_Random():
            rannumber = random.randint(10000, 99999)
            randomnumber = str(rannumber)
            Appointment_ID.set(randomnumber)

        # =========================================Frame================================================================
        MainFrame = Frame(self.root, bg="white")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="grey", relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame, font=('arial', 47, 'bold'), text="Appointment Registration",
                            bg="grey")
        self.lblTit.grid(sticky=W)

        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="Ghost White", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE, bg="white")
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000, height=1000, padx=20, relief=RIDGE
                                   , font=('arial', 40, 'bold'), text="Appointment Details\n", bg="grey")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=650, height=300, padx=31, pady=3, relief=RIDGE
                                    , font=('arial', 20, 'bold'), bg="Ghost White")
        DataFrameRIGHT.pack(side=RIGHT)
        # =========================================Labels and Entrys===============================================
        self.lbldate = Label(DataFrameLEFT, font=('arial', 18, 'bold'), text="Date:", padx=2, pady=2,
                              bg="grey")
        self.lbldate.grid(row=0, column=0, sticky=W)
        self.txtdate = Entry(DataFrameLEFT, font=('arial', 18, 'bold'), textvariable=Date_of_AppointmentReg, width=39)
        self.txtdate.grid(row=0, column=1)

        self.lblApptID = Label(DataFrameLEFT, font=('arial', 18, 'bold'), text="Appointment ID:", padx=2, pady=2,
                              bg="grey")
        self.lblApptID.grid(row=1, column=0, sticky=W)
        self.txtApptID = Entry(DataFrameLEFT, font=('arial', 18, 'bold'), textvariable=Appointment_ID, width=39)
        self.txtApptID.grid(row=1, column=1)

        self.lblpat = Label(DataFrameLEFT, font=('arial', 18, 'bold'), text="Patient ID:", padx=2, pady=2,
                            bg="grey")
        self.lblpat.grid(row=2, column=0, sticky=W)
        self.txtpat = Entry(DataFrameLEFT, font=('arial', 18, 'bold'), textvariable=Patient_ID, width=39)
        self.txtpat.grid(row=2, column=1)

        self.lblsn = Label(DataFrameLEFT, font=('arial', 18, 'bold'), text="Station Number:", padx=2, pady=2,
                            bg="grey")
        self.lblsn.grid(row=3, column=0, sticky=W)
        self.txtsn = Entry(DataFrameLEFT, font=('arial', 18, 'bold'), textvariable=Station_Number, width=39)
        self.txtsn.grid(row=3, column=1)

        self.lblrsn = Label(DataFrameLEFT, font=('arial', 18, 'bold'), text="Reason:", padx=2, pady=3,
                            bg="grey")
        self.lblrsn.grid(row=4, column=0, sticky=W)
        self.txtrsn = Entry(DataFrameLEFT, font=('arial', 18, 'bold'), textvariable=Reason, width=39)
        self.txtrsn.grid(row=4, column=1)

        self.lblpname = Label(DataFrameLEFT, font=('arial', 18, 'bold'), text="Procedure Name:", padx=2, pady=3, bg="grey")
        self.lblpname.grid(row=5, column=0, sticky=W)
        self.txtpname = Entry(DataFrameLEFT, font=('arial', 18, 'bold'), textvariable=Procedure, width=39)
        self.txtpname.grid(row=5, column=1)

        self.lblfee = Label(DataFrameLEFT, font=('arial', 18, 'bold'), text="Fee:", padx=2, pady=3,
                               bg="grey")
        self.lblfee.grid(row=6, column=0, sticky=W)
        self.txtfee = Entry(DataFrameLEFT, font=('arial', 18, 'bold'), textvariable=Fee, width=39)
        self.txtfee.grid(row=6, column=1)

        self.lblappt_paymet = Label(DataFrameLEFT, font=('arial', 18, 'bold'), text="Method of Payment:", padx=2, pady=3,
                            bg="grey")
        self.lblappt_paymet.grid(row=7, column=0, sticky=W)
        self.appt_paymetcmb = ttk.Combobox(DataFrameLEFT, text = var1, state = "readonly", font =("calibri", 18, "bold"),
                                           width = 29)
        self.appt_paymetcmb['values'] = ("", "Debit", "Credit", "Cash")
        self.appt_paymetcmb.current(0)
        self.appt_paymetcmb.grid(row=7, column = 1, pady = 20, padx = 10, sticky = "w")


        # =========================================Listbox and Scrollbar===============================================

        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')

        appointmentlist = Listbox(DataFrameRIGHT, width=65, height=16, font=('arial', 12, 'bold'),
                              yscrollcommand=scrollbar.set)
        appointmentlist.bind('<<ListboxSelect>>', AppointmentRec)
        appointmentlist.grid(row=0, column=0, padx=8)
        scrollbar.config(command=appointmentlist.yview)
        # =========================================Buttons=====================================================
        self.btnApplyID = Button(ButtonFrame, text='Apply ID', font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                 command=DentistID_Random, bg="grey")
        self.btnApplyID.grid(row=0, column=0)

        self.btnAddData = Button(ButtonFrame, text='Add New', font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                 command=addAppointmentData, bg="grey")
        self.btnAddData.grid(row=0, column=1)

        self.btnDisplayData = Button(ButtonFrame, text='Display', font=('arial', 20, 'bold'), height=1, width=10,
                                     bd=4, command=DisplayAppointmentData, bg="grey")
        self.btnDisplayData.grid(row=0, column=2)

        self.btnClearData = Button(ButtonFrame, text='Clear', font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                   command=ClearAppointmentData, bg="grey")
        self.btnClearData.grid(row=0, column=3)

        self.btnDeleteData = Button(ButtonFrame, text='Delete', font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                    command=DeleteAppointmentData, bg="grey")
        self.btnDeleteData.grid(row=0, column=4)

        self.btnSearchData = Button(ButtonFrame, text='Search', font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                    command=searchDentistDatabase, bg="grey")
        self.btnSearchData.grid(row=0, column=5)

        self.btnUpdateData = Button(ButtonFrame, text='Update', font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                    command=Dentistupdate, bg="grey")
        self.btnUpdateData.grid(row=0, column=6)

        self.btnExit = Button(ButtonFrame, text='Exit', font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                              command=iExitAppointment, bg="grey")
        self.btnExit.grid(row=0, column=7)


if __name__ == '__main__':
    root = Tk()
    application = Dentist(root)
    root.mainloop()
