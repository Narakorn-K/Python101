Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
>>> 
>>> GUI = Tk()
>>> GUI.title('Program Crypto')
''
>>> GUI.geometry('500x500')
''
>>> 
>>> L1 = Label(GUI,text='ETH',font=('Angsana New',30),fg='green')
>>> L1.place(x=30,y=20)
>>> 
>>> def Button2():
...     text = 'ตอนนี้เหลือเหรียญอยู่ 2 coin'
...     messagebox.showinfo('เหรียญในBNB',text)
... 
...     
>>> FB1 = Frame(GUI)
>>> FB1.place(x=100,y=80)
>>> B2 = ttk.Button(FB1,text='มีอยู่กี่เหรียญ',command=Button2)
>>> B2.pack(ipadx=20,ipady=20)
>>> 
def Button3():
    text = 'Python 101,Math'
    messagebox.showinfo('เรียนวันที่ 10 กพ 2566',text)

    
FB2 = Frame(GUI)
FB2.place(x=100,y=180)
B3 = ttk.Button(FB1,text='คลาสที่2 เรียนวิชาอะไร',command=Button3)
B3.pack(ipadx=20,ipady=20)

GUI.mainloop()

