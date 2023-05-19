import tkinter
from tkinter import *
from tkinter import messagebox

q=tkinter.Tk()
q.title('venkatesh')
q.geometry('500x500')
#lable
label1=Label(q,text='Enter your name :',fg='blue',font=('Times new roman',14))
label1.grid(row=3,column=3)
label2=Label(q,text='Enter your age :',fg='green',font=('Times new roman',14))
label2.grid(row=4,column=3,sticky=E)

#empty lable
emptylabel1=Label(q,fg='blue',font=('Times new roman',14))
emptylabel1.grid(row=6,column=4,pady=10)
emptylabel2=Label(q,fg='blue',font=('Times new roman',14))
emptylabel2.grid(row=7,column=4,pady=10)
data1=IntVar()
data2=StringVar()

def myfunction1():
    emptylabel1.config(text='Your roll is : '+str(data1.get()))
def myfunction2():
    emptylabel2.config(text='Your name is : '+data2.get())

#button

b1=Button(q,command=myfunction1,text="Save1",bg="blue",font=('Arial',10),fg="white")
b1.grid(column=4,row=5,pady=10,padx=5,sticky=W)
b2=Button(q,command=myfunction2,text="Save2",bg="blue",font=('Arial',10),fg="white")
b2.grid(column=4,row=5,pady=10,padx=5,sticky=E)
#radio button
'''
r=Radiobutton(q,text='Venkatesh',value=1)
r.grid(column=3,row=0)
r1=Radiobutton(q,text='Aravind',value=2)
r1.grid(column=3,row=1)


#Text box(entrybox)
'''
e1=Entry(q,textvariable=data1,width=30)
e1.grid(column=4,row=4)
e2=Entry(q,textvariable=data2,width=30)
e2.grid(column=4,row=3)

'''
#message box
def Button1():
    messagebox.showinfo('status',' please login')
b=Button(q,text="VENKATESH",command=Button1)'''







q.mainloop()