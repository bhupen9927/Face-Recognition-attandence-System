from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self,root):
        self.root=root 
        self.root.geometry("1530x790+0+0") 
        self.root.title("Face Recogniton System")

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45) 

        #first image
        img_top=Image.open(r"C:\Users\bhupe\Desktop\Face Recognization system\college_images\face_detector1.jpg")  
        img_top=img_top.resize((650,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)

        #second image
        img_bottom=Image.open(r"C:\Users\bhupe\Desktop\Face Recognization system\college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")  
        img_bottom=img_bottom.resize((950,700),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width=950,height=700)

                #button
        b1_1=Button(f_lbl,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",18,"bold"),bg="darkgreen",fg="white")
        b1_1.place(x=375,y=615,width=200,height=40)


    #Attedence.......
    def Mark_attendence(self,i,r,n,d):
        with open("bhupendra.csv","r+",newline="\n")as f:
            myDataList=f.readline()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
    #face recognition function...

    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="Singh@123#",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                print(n)
                if n is not None:
                    n="+".join(str(x) for x in n)
                else:
                    n = ""

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                print(r)
                if r is not None:
                    r="+".join(str(x) for x in r)
                else:
                    r = ""
                

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                print(d)
                if d is not None:
                    d="+".join(str(x) for x in d)
                else:
                    d = ""

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                print(d)
                if i is not None:
                    i="+".join(str(x) for x in i)
                else:
                    i = ""
                


                if confidence>77:
                    cv2.putText(img,f"S_id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.Mark_attendence(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unkown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord
        
        def recognize(img,clf,faceCascade):                 #25
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier(r"C:\Users\bhupe\Desktop\Face Recognization system\haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)
        try:
            while True:
                ret,img=video_cap.read()
                img=recognize(img,clf,faceCascade)
                cv2.imshow("Welcome To Face Recognition",img)

                if cv2.waitKey(1)==13:
                    break
                if cv2.getWindowProperty("Welcome To Face Recognition", cv2.WND_PROP_VISIBLE) < 1:
                    break
            video_cap.release()
            cv2.destroyAllWindows()
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)











        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()  