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




conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=AMMAR\SQLEXPRESS;'
                      'Database=pharmacy_project;'
                      'Trusted_Connection=yes;')

cursorr = conn.cursor()

#cursorr.execute(f'''
 #               INSERT INTO {op3} (ssn, first_name , last_name , gender , p_address)
   #             VALUES
       #         ({op1},'{op2}','{op4}','{op5}','{op6}')
         #       ''')
#conn.commit()



def btnClickFunction1():
    drugid=entry1.get()
    trade_name=entry2.get()
    ssn=entry3.get()
    OID=entry4.get()
    payment_due=entry5.get()
    cursorr.execute(f'''
                INSERT INTO view_order (drugid, trade_name , ssn , OID,payment_due)
                VALUES
                ({drugid},'{trade_name}',{ssn},{OID},{payment_due})
                ''')
    conn.commit()


def btnClickFunction2():
    delOID=entry1.get()
    conn = pyodbc.connect('Driver={SQL Server};'
                    'Server=AMMAR\SQLEXPRESS;'
                    'Database=pharmacy_project;'
                    'Trusted_Connection=yes;')
    cursorr = conn.cursor()
    cursorr.execute(f'''
        delete from view_order 
        WHERE OID = {delOID}
        ''')
    conn.commit()
  
    

def btnClickFunction3():
    cursorr.execute(f'''
                INSERT INTO view_order (drugid, trade_name , ssn , OID,payment_due)
                VALUES
                ({drugid},'{trade_name}',{ssn},{OID},{payment_due})
                ''')
    conn.commit()
    
    
    
    

  


# This is the section of code which creates the main window
root.geometry('751x488')
root.configure(background='#F0F8FF')
root.title('patient window 2')


# This is the section of code which creates a button
Button(root, text='insert new order  ', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction1).place(x=10, y=50)

Button(root, text='delete order w OID ', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction2).place(x=10, y=100)

Button(root, text='insert new order 3  ', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction3).place(x=10, y=150)




root.mainloop()
