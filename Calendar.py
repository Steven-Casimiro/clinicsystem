from tkinter import*
from tkcalendar import*
import tkinter as ttk
import tkinter.messagebox

class revenue:

    def __init__(self, screen):
        self.screen = screen
        self.screen.geometry("800x700+300+0")
        self.screen.title("Monthly Calendar")
        self.screen.configure(bg="white")
# ==================================================Functions===============================================================
        #def selectDate():
            #myDate = myCal.get_date()
            #print(myDate)

# ==================================================Frames===============================================================

        MainFrame = Frame(self.screen, bd=10,width=770,height=700,relief=RIDGE, bg="white")
        MainFrame.grid()

        TopFrame3 = Frame(MainFrame, bd=5, width=770, height =500, relief=RIDGE)
        TopFrame3.grid(row=1, column=0)

        RevenueFrame = Frame(MainFrame, bd=7, width=770, height=75, relief=RIDGE)
        RevenueFrame.grid(row=0,column=0)

        LeftFrame = Frame(TopFrame3, bd=5, width=770, height=400, padx=2, bg="white", relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame, bd=5, width=600, height=180, padx=2,pady=4,relief=RIDGE)
        LeftFrame1.pack(side=TOP,padx=0,pady=0)

        RightFrame1 = Frame(TopFrame3, bd=5, width=100, height=400, padx=2, bg="white", relief=RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1, bd=5, width=90, height=300, padx=2, pady=2, relief=RIDGE)
        RightFrame1a.pack(side=TOP)

#==================================================Calendar===============================================================
        #myCal = Calendar(MainFrame, setmode = 'day', date_pattern = 'd/m/yy')
        #myCal.pack(pady=30)

#=================================================Treeview==================================================================

        scroll_y=Scrollbar(LeftFrame, orient = HORIZONTAL)

        self.calendar_records = ttk.Treeview(LeftFrame, height=12,columns=("PatientID","Fee"),yscrollcommand=scroll_y.set)

        scroll_y.pack(side=RIGHT, fill=Y)

        self.calendar_records.heading("PatientID", text = "Patient ID")
        self.calendar_records.heading("Fee", text="Fee")

        self.calendar_records['show']='headings'

        self.calendar_records.column("PatientID", width=120)
        self.calendar_records.column("Fee", width=120)

        self.calendar_records.pack(fill =BOTH, expand=1)


#=================================================Buttons================================================================

        #openCal = Button(Main, text = "Select Date", command = selectDate, bd = 5, relief = RIDGE)
        #openCal.pack(pady=50)

if __name__ == '__main__':
    screen = Tk()
    application = revenue(screen)
    screen.mainloop()

