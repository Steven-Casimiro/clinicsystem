import sqlite3
con = sqlite3.connect('clinic.db')
cur = con.cursor()
con.execute("PRAGMA foreign_keys = 1")



# backend


def patientData():
    con = sqlite3.connect("clinic.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS patient (PtntID INTEGER PRIMARY KEY,Firstname text,Surname text,DoB text, \
        Age text,Gender text,Address text,Mobile text,Allergies text,CM text,PM text,PS text)")
    con.commit()
    con.close()


def addPatientRec(PtntID, Firstname, Surname, DoB, Age, Gender, Address, Mobile, Allergies,CM,PM,PS):
    con = sqlite3.connect("clinic.db")
    cur = con.cursor()
    cur.execute("INSERT INTO patient VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?)", \
                (PtntID, Firstname, Surname, DoB, Age, Gender, Address, Mobile,Allergies,CM,PM,PS))
    con.commit()
    con.close()


def viewData():
    con = sqlite3.connect("clinic.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM patient")
    rows = cur.fetchall()
    con.close
    return rows


def deleteRec(id):
    con = sqlite3.connect("clinic.db")
    cur = con.cursor()
    cur.execute("DELETE FROM patient WHERE id=?", (id,))
    con.commit()
    con.close


def searchData(PtntID="", Firstname="", Surname="", DoB="", Age="", Gender="", Address="", Mobile="", Allergies="",CM="",PM="",PS=""):
    con = sqlite3.connect("clinic.db")
    cur = con.cursor()
    cur.execute(
        "SELECT * FROM patient WHERE PtntID=? OR Firstname=? OR Surname=? OR DoB=? OR Age=? OR Gender=? OR Address=? OR Mobile=? OR\
         Allergies=? OR CM=? OR PM=? OR PS=?", \
        (PtntID, Firstname, Surname, DoB, Age, Gender, Address, Mobile, Allergies, CM, PM, PS))
    rows = cur.fetchall()
    con.close()
    return rows


def dataUpdate(id, PtntID="", Firstname="", Surname="", DoB="", Age="", Gender="", Address="", Mobile="",Allergies="",CM="",PM="",PS=""):
    con = sqlite3.connect("clinic.db")
    cur = con.cursor()
    cur.execute(
        "UPDATE patient SET PtntID=?, Firstname=?,Surname=?,DoB=?, Age=?,Gender=?, Address=?, Mobile=?, Allergies=?, CM=?, PM=?, PS=? WHERE id=?", \
        (PtntID, Firstname, Surname, DoB, Age, Gender, Address, Mobile, Allergies, CM, PM, PS, id))
    con.commit()
    con.close()

#===============================================================================Dentist Page Table and Functions================================================================

def dentistData():
    con = sqlite3.connect("clinic.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS dentist (DentID INTEGER PRIMARY KEY,Firstname text,Surname text,DoB text, \
        Age text,Gender text,Address text,Mobile text)")
    con.commit()
    con.close()


def addDentistRec(DentID, Firstname, Surname, DoB, Age, Gender, Address, Mobile):
    con = sqlite3.connect("clinic.db")
    cur = con.cursor()
    cur.execute("INSERT INTO dentist VALUES (NULL,?,?,?,?,?,?,?,?)", \
                (DentID, Firstname, Surname, DoB, Age, Gender, Address, Mobile))
    con.commit()
    con.close()


def viewDentistData():
    con = sqlite3.connect("clinic.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM dentist")
    rows = cur.fetchall()
    con.close
    return rows


def deleteDentistRec(id):
    con = sqlite3.connect("clinic.db")
    cur = con.cursor()
    cur.execute("DELETE FROM dentist WHERE id=?", (id,))
    con.commit()
    con.close


def searchDentistData(DentID="", Firstname="", Surname="", DoB="", Age="", Gender="", Address="", Mobile=""):
    con = sqlite3.connect("clinic.db")
    cur = con.cursor()
    cur.execute(
        "SELECT * FROM dentist WHERE DentID=? OR Firstname=? OR Surname=? OR DoB=? OR Age=? OR Gender=? OR Address=? OR Mobile=?",
        (DentID, Firstname, Surname, DoB, Age, Gender, Address, Mobile))
    rows = cur.fetchall()
    con.close()
    return rows


def dataDentistUpdate(id, DentID="", Firstname="", Surname="", DoB="", Age="", Gender="", Address="", Mobile=""):
    con = sqlite3.connect("clinic.db")
    cur = con.cursor()
    cur.execute(
        "UPDATE dentist SET DentID=?, Firstname=?,Surname=?,DoB=?, Age=?,Gender=?, Address=?, Mobile=?, WHERE id=?",
        (DentID, Firstname, Surname, DoB, Age, Gender, Address, Mobile, id))
    con.commit()
    con.close()


#===============================================================================Appointments================================================================

def appointmentData():
    con = sqlite3.connect("clinic.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS appointment (ApptID INTEGER PRIMARY KEY, Station_Num integer,Reason text,Procedure_Name text, \
         apptFee text, payMet text, PtntID integer, FOREIGN KEY(PtntID) REFERENCES patient(PtntID))")
    con.commit()
    con.close()


def addAppointmentRec(ApptDate, ApptID,PtntID, Station_Num,Reason,Procedure_Name,apptFee, payMet):
    con = sqlite3.connect("clinic.db")
    cur = con.cursor()
    cur.execute("INSERT INTO appointment VALUES (NULL,?,?,?,?,?,?,?,?)", \
                (ApptDate, ApptID,PtntID, Station_Num,Reason,Procedure_Name,apptFee, payMet))
    con.commit()
    con.close()


def deleteAppointmentRec(id):
    con = sqlite3.connect("clinic.db")
    cur = con.cursor()
    cur.execute("DELETE FROM appointment WHERE id=?", (id,))
    con.commit()
    con.close

def viewAppointmentData():
    con = sqlite3.connect("clinic.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM appointment")
    rows = cur.fetchall()
    con.close
    return rows

def searchAppointmentData(ApptDate="", ApptID="" ,PtntID="", Station_Num="",Reason="",Procedure_Name="",apptFee="", payMet=""):
    con = sqlite3.connect("clinic.db")
    cur = con.cursor()
    cur.execute(
        "SELECT * FROM appointment WHERE DentID=? OR Firstname=? OR Surname=? OR DoB=? OR Age=? OR Gender=? OR Address=? OR Mobile=?",
        (ApptDate, ApptID,PtntID, Station_Num, Reason, Procedure_Name, apptFee, payMet))
    rows = cur.fetchall()
    con.close()
    return rows

def dataAppointmentUpdate(id, ApptDate="", ApptID="",PtntID="", Station_Num="",Reason="",Procedure_Name="",apptFee="", payMet=""):
    con = sqlite3.connect("clinic.db")
    cur = con.cursor()
    cur.execute(
        "UPDATE appointment SET DentID=?, Firstname=?,Surname=?,DoB=?, Age=?,Gender=?, Address=?, Mobile=?, WHERE id=?",
        (ApptDate, ApptID,PtntID, Station_Num, Reason, Procedure_Name, apptFee, payMet, id))
    con.commit()
    con.close()


patientData()
dentistData()
appointmentData()



