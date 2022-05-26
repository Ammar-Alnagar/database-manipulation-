import tkinter as tk
from tkinter import ttk
from tkinter import * 
import pyodbc 
import os


root = Tk()








# this is the function called when the button is clicked
def btnClickFunction1():
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=AMMAR\SQLEXPRESS;'
                      'Database=pharmacy_project;'
                      'Trusted_Connection=yes;')
        cursorr = conn.cursor()
        cursorr.execute(f'''
                select  * from patient 
        order by ssn
                ''' )        
        result =" "    
        for i in cursorr:
         result=result+"\n"+str(i) 
        result=result.replace('(','').replace(')','').replace(',','-').replace("'",'').replace("'",'').replace("Decimal","")
        a6 = Label(text=result)
        a6.pack()

  
  

		
  
  
  
  
  
def btnClickFunction2():        
        conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=AMMAR\SQLEXPRESS;'
                        'Database=pharmacy_project;'
                        'Trusted_Connection=yes;')
        cursora = conn.cursor()
        cursora.execute(f'''
                select * from patient 
        order by first_name
                ''')        
        result =" "    
        for i in cursora:
         result=result+"\n"+str(i) 
        result=result.replace('(','').replace(')','').replace(',','-').replace("'",'').replace("'",'').replace("Decimal","")
        a6 = Label(text=result)
        a6.pack()

            
            
            
            
            
            
def btnClickFunction3():
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=AMMAR\SQLEXPRESS;'
                      'Database=pharmacy_project;'
                      'Trusted_Connection=yes;')
        cursorb = conn.cursor()
        cursorb.execute(f'''
                select * from patient 
        order by last_name
                ''')    
        result =" "    
        for i in cursorb:
         result=result+"\n"+str(i) 
        result=result.replace('(','').replace(')','').replace(',','-').replace("'",'').replace("'",'').replace("Decimal","")
        a6 = Label(text=result)
        a6.pack()
            
            
def btnClickFunction4():
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=AMMAR\SQLEXPRESS;'
                      'Database=pharmacy_project;'
                      'Trusted_Connection=yes;')
        cursorc = conn.cursor()
        cursorc.execute('''
                SELECT patient.first_name , patient.last_name , patient.ssn , view_order.OID
                FROM patient 
                FULL OUTER JOIN view_order on patient.ssn = view_order.ssn
                ORDER by view_order.OID
                ''')    
        result =" "    
        for i in cursorc:
         result=result+"\n"+str(i) 
        result=result.replace('(','').replace(')','').replace(',','-').replace("'",'').replace("'",'').replace("Decimal","")
        a6 = Label(text=result)
        a6.pack()
            
		
  
def btnClickFunction5():
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=AMMAR\SQLEXPRESS;'
                      'Database=pharmacy_project;'
                      'Trusted_Connection=yes;')

        cursord = conn.cursor()
        cursord.execute('SELECT ssn,p_address FROM patient')    
        result =" "    
        for i in cursord:
         result=result+"\n"+str(i) 
        result=result.replace('(','').replace(')','').replace(',','-').replace("'",'').replace("'",'').replace("Decimal","")
        a6 = Label(text=result)
        a6.pack()
        


def btnClickFunction6():
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=AMMAR\SQLEXPRESS;'
                      'Database=pharmacy_project;'
                      'Trusted_Connection=yes;')
        cursore = conn.cursor()
        cursore.execute('''
        select count(drugid),sum(price)
        from drug 
        group by  trade_name
        having count(drugid)>1
                ''')    
        result =" "    
        for i in cursore:
         result=result+"\n"+str(i) 
        result=result.replace('(','').replace(')','').replace(',','-').replace("'",'').replace("'",'').replace("Decimal","")
        a6 = Label(text=result)
        a6.pack()
     





# This is the section of code which creates the main window
root.geometry('751x488')
root.configure(background='#F0F8FF')
root.title('Employee window')


# This is the section of code which creates a button
Button(root, text='view patients  by ssn', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction1).place(x=10, y=50)

Button(root, text='view patients by first name', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction2).place(x=10, y=100)

Button(root, text='view patients last name ', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction3).place(x=10, y=150)

Button(root, text='view patients order ID', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction4).place(x=10, y=200)

Button(root, text='view patients  Address', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction5).place(x=10, y=250)


Button(root, text='view count of drugs and the sum of the price grouped by trade name', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction6).place(x=10, y=300)



root.mainloop()
