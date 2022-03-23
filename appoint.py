import random
import time
import datetime
from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import PtntDatabase



class AppointmentRegistration:
    def __init__(self,root):
        self.root = root
        self.root.title("Appointment Registration System")
        self.root.geometry("1350x750+0+0") #x axis, y axis, 0, 0
        self.root.configure(background = "white")

        #taking live time date using time module

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

# ============================================Functions==============================================================

        def exitbtt():
            exitbtt = tkinter.messagebox.askyesno("Appointment Registration Form", "Are you sure you want to clear Record?")
            if exitbtt > 0:
                root.destroy()
                return

        def resetbtt():
            Appointment_ID.set("")
            Station_Number.set("")
            Reason.set("")
            Fee.set("")
            Patient_ID.set("")
            Procedure.set("")
            var1.set("0")
            appt_paymetcmb.current(0)
        def resetbtt2():
            resetbtt2 = tkinter.messagebox.askokcancel("Appointment Registration Form", "You want to add as new Record?")
            if resetbtt2 > 0:
                resetbtt()
            elif resetbtt2 <= 0:
                resetbtt()
                detail_labeltxt.delete("1.0",END)
                return


        def ID_Number():
            rannumber = random.randint(10000000,99999999)
            randomnumber = str(rannumber)
            Appointment_ID.set(randomnumber)

        def Add():
            ID_Number()
            PtntDatabase.addAppointmentRec(Date_of_AppointmentReg.get(), Appointment_ID.get(), Station_Number.get(), Reason.get(),
                                           Procedure.get(), Fee.get(), appt_paymetcmb.get())
            detail_labeltxt.insert(END, "\t" +Date_of_AppointmentReg.get()+ "            \t" + Appointment_ID.get() + "                 \t" + Patient_ID.get() + "                         \t\t" +
                                   Station_Number.get() + "                                      \t" + Reason.get() + "                          \t" + Procedure.get()+ "    \t" +
            "  \t\t" + Fee.get() + "       \t\t" + appt_paymetcmb.get() + "\n")

        def Delete():
            PtntDatabase.deleteAppointmentRec(detail_labeltxt,)
            resetbtt()








 #============================================Title==============================================================

        title = Label(self.root, text = "Appointment Registration Form", font = ("calibri", 30, "bold"),bd = 5,
                      relief = GROOVE,bg ="white", fg = "#000000")
        title.pack(side=TOP, fill = X)
#============================================Patient Frame==============================================================

        Manage_Frame = Frame(self.root, bd = 4, relief = RIDGE, bg = "grey")
        Manage_Frame.place(x=20,y=100,width=450,height=630)
#============================================Detail Frame==============================================================

        detail_frame = Frame(self.root, relief = RIDGE,bg = "white")
        detail_frame.place(x=500,y=100,width=820,height=630)

        detail_label = Label(detail_frame,font = ("calibri",12,"bold"),pady=10,padx=2,width=105,
                             text = "Date\t Appointment ID\t   Patient ID     Station Number        Procedure Name       Reason       Fee       MOP")
        detail_label.grid(row=0,column=0,columnspan=6,sticky="w")
        detail_labeltxt = Text(detail_frame,width=123,height=34,font=("calibri",10))
        detail_labeltxt.grid(row=1,column=0,columnspan=6)

 # =========================================Listbox + Scrollbar===============================================
        scrollbar = Scrollbar(detail_frame)
        scrollbar.grid(row=0, column=1, sticky='ns')

        appointlist = Listbox(detail_labeltxt, width=65, height=16, font=('arial', 12, 'bold'),
                              yscrollcommand=scrollbar.set)
        appointlist.bind('<<ListboxSelect>>', AppointmentRec)
        appointlist.grid(row=0, column=0, padx=8)
        scrollbar.config(command=appointlist.yview)

 #============================================Button in Detail Frame==============================================================

        addbtn = Button(detail_frame, padx = 0, bd = 3, font =("calibri",12,"bold"),
                        bg = "grey", fg ="white", width = 10, text = "Add", command = Add)
        addbtn.grid(row = 2, column =0)

        resetbtn = Button(detail_frame, padx = 0, bd = 3, font =("calibri",12,"bold"),
                        bg = "grey", fg ="white", width = 10, text = "Clear", command = resetbtt2)
        resetbtn.grid(row = 2, column =1)

        deletebtn = Button(detail_frame, padx = 0, bd = 3, font =("calibri",12,"bold"),
                        bg = "grey", fg ="white", width = 10, text = "Delete", command = Delete)
        deletebtn.grid(row = 2, column =2)

        displaybtn = Button(detail_frame, padx = 0, bd = 3, font =("calibri",12,"bold"),
                        bg = "grey", fg ="white", width = 10, text = "Display")
        displaybtn.grid(row = 2, column =3)

        exitbtn = Button(detail_frame, padx = 0, bd = 3, font =("calibri",12,"bold"),
                        bg = "grey", fg ="white", width = 10, text = "Exit", command = exitbtt)
        exitbtn.grid(row = 2, column =4)



#============================================text, label, comboboxes in manage frame==============================================================
        Cus_title = Label(Manage_Frame,text="Appointment Details",font =("calibri",20,"bold"),bg="grey",fg = "white")
        Cus_title.grid(row = 0, columnspan=2, pady=20)

        appt_datelbl = Label(Manage_Frame,text="Date",font = ("calibri",15,"bold"), bg ="grey", fg = "white")
        appt_datelbl.grid(row = 1, column = 0, pady = 20, padx=15, sticky = "w")
        appt_datetxt = Entry(Manage_Frame, font = ("calibri",15,"bold"), textvariable = Date_of_AppointmentReg)
        appt_datetxt.grid(row = 1, column = 1, pady = 20, padx = 15, sticky = "w")


        appt_reflbl = Label(Manage_Frame, text = "Appointment ID", font = ("calibri",15,"bold"), bg = "grey",
                               fg = "white")
        appt_reflbl.grid(row = 2, column = 0, pady = 20, padx = 10, sticky = "w")
        appt_reftxt = Entry(Manage_Frame, font = ("calibri",15,"bold"), state = DISABLED, text = Appointment_ID)
        appt_reftxt.grid(row = 2, column = 1, pady = 20, padx = 10, sticky = "w")

        appt_patlbl = Label(Manage_Frame, text = "Patient ID", font = ("calibri",15,"bold"), bg = "grey",
                               fg = "white")
        appt_patlbl.grid(row = 3, column = 0, pady = 20, padx = 10, sticky = "w")
        appt_pattxt = Entry(Manage_Frame, font = ("calibri",15,"bold"), text = Patient_ID)
        appt_pattxt.grid(row = 3, column = 1, pady = 20, padx = 10, sticky = "w")


        appt_snlbl = Label(Manage_Frame, text="Station Number", font=("calibri", 15, "bold"), bg="grey", fg="white")
        appt_snlbl.grid(row=4, column=0, pady=20, padx=10, sticky="w")
        appt_sntxt = Entry(Manage_Frame, font=("calibri", 15, "bold"), textvariable=Station_Number)
        appt_sntxt.grid(row=4, column=1, pady=20, padx=10, sticky="w")


        appt_rsnlbl = Label(Manage_Frame, text="Reason", font=("calibri", 15, "bold"), bg="grey", fg="white")
        appt_rsnlbl.grid(row=5, column=0, pady=20, padx=10, sticky="w")
        appt_rsntxt = Entry(Manage_Frame, font=("calibri", 15, "bold"), textvariable=Reason)
        appt_rsntxt.grid(row=5, column=1, pady=20, padx=10, sticky="w")


        appt_pnamelbl = Label(Manage_Frame, text="Procedure Name", font=("calibri", 15, "bold"), bg="grey", fg="white")
        appt_pnamelbl.grid(row=6, column=0, pady=20, padx=10, sticky="w")
        appt_pnametxt = Entry(Manage_Frame, font=("calibri", 15, "bold"), textvariable=Procedure)
        appt_pnametxt.grid(row=6, column=1, pady=20, padx=10, sticky="w")


        appt_costlbl = Label(Manage_Frame, text="Appointment Fee", font=("calibri", 15, "bold"), bg="grey", fg="white")
        appt_costlbl.grid(row=7, column=0, pady=20, padx=10, sticky="w")
        appt_costtxt = Entry(Manage_Frame, font=("calibri", 15, "bold"), textvariable= Fee)
        appt_costtxt.grid(row=7, column=1, pady=20, padx=10, sticky="w")


        appt_paymetlbl = Label(Manage_Frame, text="Method of Payment", font=("calibri", 15, "bold"), bg="grey", fg="white")
        appt_paymetlbl.grid(row=8, column=0, pady=20, padx=5, sticky="w")
        appt_paymetcmb = ttk.Combobox(Manage_Frame, text = var1, state = "readonly", font =("calibri",15,"bold"),
                              width = 19)
        appt_paymetcmb['values'] = ("", "Debit", "Credit", "Cash")
        appt_paymetcmb.current(0)
        appt_paymetcmb.grid(row = 8, column = 1, pady = 20, padx = 10, sticky = "w")




if __name__=="__main__":
    root = Tk()
    app = AppointmentRegistration(root)
    root.mainloop()