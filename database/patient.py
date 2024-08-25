import tkinter as tk
from tkinter import ttk
from tkinter import * 
import pyodbc 
import os
root = Tk()









entry1 = Entry(root,width=50)
entry1.pack()
a1 = Label(text="1").place(x=175,y=3)

# this is the function called when the button is clicked
def btnClickFunction1():
        first_name=entry1.get()
        conn = pyodbc.connect('Driver={SQL Server};'
                'Server=name\SQLEXPRESS;'
                'Database=pharmacy_project;'
                'Trusted_Connection=yes;')
        cursorr = conn.cursor()
        cursorr.execute(f''' SELECT * FROM patient
                        WHERE first_name = '{first_name}' ''')    
        str1=str(cursorr.fetchone())
        a6 = Label(text=str1)
        a6.pack()

  
  

		
  
  
  
  
  
def btnClickFunction2():
        
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=name\SQLEXPRESS;'
                      'Database=pharmacy_project;'
                      'Trusted_Connection=yes;')
        cursora = conn.cursor()
        cursora.execute(''' Select first_name from patient
                        where ssn = 1212 ''')
        str1=str(cursora.fetchone())
        a6 = Label(text=str1)
        a6.pack()

            
            
            
            
            
            
def btnClickFunction3():
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=name\SQLEXPRESS;'
                      'Database=pharmacy_project;'
                      'Trusted_Connection=yes;')
        cursorb = conn.cursor()
        cursorb.execute('''
                SELECT last_name FROM patient
                WHERE ssn = 1212
                ''')        
        str1=str(cursorb.fetchone())
        a6 = Label(text=str1)
        a6.pack()

            
            
def btnClickFunction4():
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=name\SQLEXPRESS;'
                      'Database=pharmacy_project;'
                      'Trusted_Connection=yes;')
        cursorc = conn.cursor()
        cursorc.execute('''
                SELECT  patient.first_name ,view_order.OID , view_order.trade_name , view_order.payment_due 
                FROM patient 
                FULL OUTER JOIN view_order on patient.ssn = view_order.ssn
                where patient.ssn = 1212
                ''')        
        str1=str(cursorc.fetchone())
        a6 = Label(text=str1)
        a6.pack()

            
		
  
def btnClickFunction5():
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=name\SQLEXPRESS;'
                      'Database=pharmacy_project;'
                      'Trusted_Connection=yes;')

        cursord = conn.cursor()
        cursord.execute('SELECT * FROM drug')
        
        result =" "    
        for i in cursord:
         result=result+"\n"+str(i) 
        result=result.replace('(','').replace(')','').replace(',','-').replace("'",'').replace("'",'').replace("Decimal","")
        a6 = Label(text=result)
        a6.pack()

         
        

 
	
	





# This is the section of code which creates the main window
root.geometry('751x488')
root.configure(background='#F0F8FF')
root.title('Patient window')


# This is the section of code which creates a button
Button(root, text='view my information (patient)', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction1).place(x=10, y=50)

Button(root, text='view my first name', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction2).place(x=10, y=100)

Button(root, text='view  last name ', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction3).place(x=10, y=150)

Button(root, text='view my orders ', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction4).place(x=10, y=200)

Button(root, text='view drugs', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction5).place(x=10, y=250)



root.mainloop()
