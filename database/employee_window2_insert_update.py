import pyodbc 
import tkinter as tk
from tkinter import ttk
from tkinter import * 
import pyodbc 
import os

root = Tk()
entry1 = Entry(root,width = 50)
entry1.pack()
entry2 = Entry(root,width = 50)
entry2.pack()
entry3 = Entry(root,width = 50)
entry3.pack()
entry4 = Entry(root,width=50)
entry4.pack()
entry5 = Entry(root,width = 50)
entry5.pack()
###############################################
a1 = Label(text="1").place(x=175,y=3)
a2 = Label(text="2").place(x=175,y=18)
a3 = Label(text="3").place(x=175,y=40)
a4 = Label(text="4").place(x=175,y=60)
a5 = Label(text="5").place(x=175,y=75)
###############################################


        




def btnClickFunction1():
    drugid=entry1.get()
    trade_name=entry2.get()
    production_date=entry3.get()
    expiration_date=entry4.get()
    price=entry5.get()
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=name\SQLEXPRESS;'
                      'Database=pharmacy_project;'
                      'Trusted_Connection=yes;')

    cursorr = conn.cursor()
    cursorr.execute(f'''
                INSERT INTO drug (drugid, trade_name , production_date , expiration_date , price)
                VALUES
                ({drugid},'{trade_name}','{production_date}','{expiration_date}' , {price})
                ''')
    conn.commit()


    
def btnClickFunction2():
    ssn =entry1.get()
    first_name=entry2.get()
    last_name=entry3.get()
    gender=entry4.get()
    p_address=entry5.get()
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=name\SQLEXPRESS;'
                      'Database=pharmacy_project;'
                      'Trusted_Connection=yes;')
    cursorr = conn.cursor()
    cursorr.execute(f'''
            INSERT INTO patient (ssn, first_name , last_name , gender , p_address)
            VALUES
            ({ssn},'{first_name}','{last_name}','{gender}','{p_address}')
            ''')
    conn.commit()
  
    


def btnClickFunction3():
    updatefirst_namename=entry1.get()
    updatessn=entry2.get() 
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=name\SQLEXPRESS;'
                      'Database=pharmacy_project;'
                      'Trusted_Connection=yes;')
    cursorr = conn.cursor()
    cursorr.execute(f'''
            UPDATE patient 
            SET first_name = '{updatefirst_name}'
            WHERE SSN = {updatessn}
            ''')
    conn.commit()
    
    
    
    
    
def btnClickFunction4():
    updatelast_name=entry1.get()
    updatessn=entry2.get() 
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=name\SQLEXPRESS;'
                      'Database=pharmacy_project;'
                      'Trusted_Connection=yes;')
    cursorr = conn.cursor()
    cursorr.execute(f'''
        UPDATE patient 
        SET last_name = '{updatelast_name}'
        WHERE SSN = {updatessn}
        ''')
    conn.commit()
    
    
    
def btnClickFunction5():
    updatenationality=entry1.get()
    updateDid=entry2.get()
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=name\SQLEXPRESS;'
                      'Database=pharmacy_project;'
                      'Trusted_Connection=yes;')
    cursorr = conn.cursor()
    cursorr.execute(f'''
        UPDATE doctor 
        SET nationality = '{updatenationality}'
        WHERE Did = {updateDid}        
        ''')
    conn.commit()
  
  
  
  
  
  
  
  
def btnClickFunction6():
    delssn=entry1.get()
    
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=AMMAR\SQLEXPRESS;'
                      'Database=pharmacy_project;'
                      'Trusted_Connection=yes;')
    cursorr = conn.cursor()
    cursorr.execute(f'''
        delete from patient 
        WHERE ssn = {delssn}        
        ''')
    conn.commit()
    
    
    
    
def btnClickFunction7():
    deldrugid=entry1.get()
    deltrade_name=entry2.get()
    conn = pyodbc.connect('Driver={SQL Server};'
                    'Server=AMMAR\SQLEXPRESS;'
                    'Database=pharmacy_project;'
                    'Trusted_Connection=yes;')
    cursorr = conn.cursor()
    cursorr.execute(f'''
        delete from drug 
        WHERE drugid = {deldrugid}  AND trade_name = '{deltrade_name}'
        ''')
    conn.commit()
  


# This is the section of code which creates the main window
root.geometry('751x488')
root.configure(background='#F0F8FF')
root.title('Employee window 2')


# This is the section of code which creates a button
Button(root, text='insert new drug ', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction1).place(x=10, y=50)

Button(root, text='insert new patient', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction2).place(x=10, y=100)

Button(root, text='Update patient first name  ', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction3).place(x=10, y=150)

Button(root, text='Update patient last name ', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction4).place(x=10, y=200)

Button(root, text='Update doctor nationality ', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction5).place(x=10, y=250)

Button(root, text='delete patient by ssn ', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction6).place(x=10, y=300)

Button(root, text='delete drug by drugid and trade_name ', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction6).place(x=10, y=350)


root.mainloop()
