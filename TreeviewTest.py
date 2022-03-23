from tkinter import *
from tkcalendar import *
import tkinter.messagebox
from datetime import datetime
from datetime import date, timedelta
from tkcalendar import DateEntry
import datetime
import time
import PtntDatabase
class calendar:
    def __init__(self,master):
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


if __name__ == '__main__':
    root = Tk()
    application = calendar(root)
    root.mainloop()