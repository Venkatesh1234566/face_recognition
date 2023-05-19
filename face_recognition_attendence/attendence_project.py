import os
import numpy as np
import face_recognition as fr
import cv2
from datetime import datetime
import tkinter
from tkinter import *
from PIL import Image,ImageTk


#loc="C:\\Users\\VENKATESH\OneDrive\\Documents\\python program\\Recognition_projects\\face_recognition_attendence\\images"


t=Tk()
t.geometry("700x640")
t.title("Face Recognition Attendance")
def took():
    f2=Frame()
    f2.place(width=700,height=640)
    label1=Label(text="CAMERA",fg="green",font=('Times new roman',20))
    label1.pack()

#f1=LabelFrame(root,bg="green")
#f1.pack()
    l1=Label(f2,bg="green")
    l1.pack()
    name=names.get()
    cap=cv2.VideoCapture(0)
    loc="C:\\Users\\VENKATESH\\OneDrive\\Documents\\python program\\Recognition_projects\\face_recognition_attendence\\images"
    def photo():
        imag=Image.fromarray(img1)
        imag.save(os.path.join(loc,f"{name}.jpg"))
    #imag.save("venkatesh.jpeg")
   # Button(f2,text="TAKE PICTURE",font=("Times new roman",10),fg="red",command=photo).pack(pady=20)
    b1=Button(f2,command=photo,text="TAKE PICTURE",font=('times new roman',20),fg="red",bg="white")
    b1.place(y=520,x=130)
    b2=Button(f2,command=interface,text="GO BACK",font=('times new roman',20),fg="green",bg="white")
    b2.place(y=520,x=425)
    #Button(f2,text="GO BACK",font=("Times new roman",10),fg="orange",command=interface).place(pady=10)
#root.mainloop()
#cv2.imwrite(os.path.join(loc,f"{names}.jpg"),img)
    while True:
        img=cap.read()[1]
        img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img=ImageTk.PhotoImage(Image.fromarray(img1))
        l1['image']=img
     # cv2.imwrite(os.path.join(loc,f"{names}.jpg"),img)
        f2.update()
    cap.release()



def register():
    f2=Frame(bg="orange")
    f2.place(width=700,height=640)
    '''e1=Entry(f2,textvariable=names,width=30)
    e1.place(x=170,y=110)
    e2=Entry(f2,textvariable=rollno,width=30)
    e2.place(x=170,y=150)'''
   # e1=Entry(f2,textvariable=names,width=30)
    #e1.place(x=170,y=110)
   # e2=Entry(f2,textvariable=rollno,width=30)
    #e2.place(x=170,y=150)
    label3=Label(f2,text="Register",bg="sky blue",font=('Times new roman',30),fg="white")
    label3.place(x=180,y=160)
    label3=Label(f2,text="Student name",font=('Times new roman',13))
    label3.place(x=180,y=240)
    label3=Label(f2,text="Roll number ",font=('Times new roman',13))
    label3.place(x=180,y=300)
    global names
    names=StringVar()
    rollno=StringVar()
    e1=Entry(f2,textvariable=names,width=30)
    e1.place(x=300,y=240)
    e2=Entry(f2,textvariable=rollno,width=30)
    e2.place(x=300,y=300)
    emptylabel1=Label(f2,fg='green',font=('Times new roman',14),bg="orange")
    emptylabel1.pack()
    '''def myfunction():
        area=names.get()*rollno.get()
        emptylabel1.config(text='Saved :' +str(area))'''
    def myfunction():
        emptylabel1.config(text='Saved Successfully')
    ''' e1=Entry(f2)
    e1.pack()
    e2=Entry(f2)
    e2.pack()'''
    b2=Button(f2,text="Save",command=myfunction,pady=10,padx=10,font=('Times new roman',10),bg="light green")
    b2.place(x=300,y=350)
    b3=Button(f2,text="Take photo",command=took,pady=10,padx=10,font=('Times new roman',10),bg="light blue")
    b3.place(x=400,y=350)
def opcamera():
    f4=Frame(bg="sky blue")
    f4.place(width=700,height=640)
    l3=Label(f4,text="NOTE",bg="sky blue",font=('Times new roman',30),fg="RED")
    l3.pack(pady=20)
    l4=Label(f4,text="Press 'e' to exit after recognition ",font=('Times new roman',30),fg="black")
    l4.pack(pady=20)

    
    b4=Button(f4,text="OPEN CAMERA",command=take,font=('Times new roman',20),fg='blue')
    b4.pack(pady=20)
    b5=Button(f4,text="GO BACK",command=interface,font=('Times new roman',20),fg='green')
    b5.pack(pady=20)




def take():
    path='images'
    images_frame_name=[]
    img_name=[]
    image_name_list=os.listdir(path)
    #print(image_name_list)
    for name in image_name_list:
        cur_frame=cv2.imread(f'{path}/{name}')
        images_frame_name.append(cur_frame)
        img_name.append(os.path.splitext(name)[0])
      #print(cur_frame)
       #print(img_name)
        #print(images_frame_name)

       #performing encoding 
    def findEncoding(images_frame_name):
        encodelist=[]
        for img in images_frame_name:
            img_color=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            encode=fr.face_encodings(img_color)[0]
            encodelist.append(encode)
        return encodelist

    encodelistknow= findEncoding(images_frame_name)
# Attendence 

    def markAttendence(name):
        f=open("attendance.csv",'r+')
        mydata_list=f.readlines()
        #print(mydata_list)
        name_list=[]
        for line in mydata_list:
            entry=line.split(',')
            name_list.append(entry[0])
        if name not in name_list:
            now=datetime.now()
            dtString=now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')
  #print(len(encodelistknow))

            #Getting the image run time to campare

    cap=cv2.VideoCapture(0)
    while True:
        success, frame=cap.read()
        frame_Small=cv2.resize(frame,(0,0),None,0.25,0.25)
        frame_Small=cv2.cvtColor(frame_Small,cv2.COLOR_BGR2RGB)
        frame_detect=fr.face_locations(frame_Small)
        #name="unknown"
        frame_encode=fr.face_encodings(frame_Small,frame_detect)
        for encodeFace,face_loc in zip(frame_encode,frame_detect):
            face_compare=fr.compare_faces(encodelistknow,encodeFace)
            faces_distance=fr.face_distance(encodelistknow,encodeFace)
            #best_match_index=np.argmin(faces_distance)
            #print(faces_distance)
            matchIndex=np.argmin(faces_distance)
            if face_compare[matchIndex]:
                name=img_name[matchIndex].upper()
                y1,x2,y2,x1=face_loc
                y1, x2, y2, x1=y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(frame,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(frame,name,(x1+6,y2-6),cv2.FONT_HERSHEY_PLAIN,1,(255,255,255),2)
                markAttendence(name)
            else:
                names="unknown".upper()
                y1,x2,y2,x1=face_loc
                y1, x2, y2, x1=y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(frame,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(frame,names,(x1+6,y2-6),cv2.FONT_HERSHEY_PLAIN,1,(255,255,255),2)
                # markAttendence(name)
            

        cv2.imshow('webcam',frame)
        if cv2.waitKey(1) & 0xFF == ord('e'):
            break
    
    #cv2.imwrite(,frame)
    
    cap.release()

    cv2.destroyAllWindows()

def interface():
    f1=Frame(bg="light blue")
    f1.place(width=700,height=640)
    label1=Label(f1,text="ATTENDANCE",bg="sky blue",font=('Times new roman',30),fg="black")
    label1.place(x=230,y=30)
    label2=Label(f1,text="Already Registered !",bg="silver",font=('times new roman',15))
    label2.place(x=280,y=180)
    b1=Button(f1,text="Take Attendance!!",command=opcamera,bg="light green",font=('times new roman',15))
    b1.place(x=285,y=250)
    label=Label(f1,text="Don't You Registered !",bg="silver",font=('times new roman',15))
    label.place(x=275,y=350)
    b1=Button(f1,text="Register!!",command=register,bg="yellow",font=('times new roman',15))
    b1.place(x=320,y=420)

   # b1=Button(f1,text="Click!!",command=login)
   # b1.pack(side='left',anchor='e',padx=50)#''',padx=20,expand=True'''
    #b2=Button(f1,text="Click!!",command=login)
   # b2.pack(side='right',anchor='e',padx=100)#'''expand=True'''
interface()
t.mainloop()