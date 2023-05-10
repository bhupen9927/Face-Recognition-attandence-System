from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 
from tkinter import messagebox
import mysql.connector
import cv2


class Attendance:
    def __init__(self,root):
        self.root=root 
        self.root.geometry("1530x790+0+0") 
        self.root.title("Face Recogniton System")

         #First Image
        img=Image.open(r"C:\Users\bhupe\Desktop\Face Recognization system\college_images\smart-attendance.jpg")  
        img=img.resize((800,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)

        #second Image
        img1=Image.open(r"C:\Users\bhupe\Desktop\Face Recognization system\college_images\iStock-182059956_18390_t12.jpg")   
        img1=img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)

        #BAckground Image
        img3=Image.open(r"C:\Users\bhupe\Desktop\Face Recognization system\college_images\p2551980.jpg")  
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45) 

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20 ,y=55,width=1480,height=600)

        # left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open(r"C:\Users\bhupe\Desktop\Face Recognization system\college_images\AdobeStock_303989091.jpeg")  
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        left_inside_frame=Frame(Left_frame,relief=RIDGE,bd=2,bg="white")
        left_inside_frame.place(x=0 ,y=135,width=720,height=300)

        #LAbels And entries
        #Attendance id
        AttendanceId_label=Label(left_inside_frame,text="Attendance_Id:",font=("comicsansns",13,"bold"),bg="white")
        AttendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        AttendanceId_entry=ttk.Entry(left_inside_frame,width=20,font=("comicsansns",13,"bold"))
        AttendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Roll
        rolllabel=Label(left_inside_frame,text="Roll:",font=("comicsansns",11,"bold"),bg="white")
        rolllabel.grid(row=0,column=2,padx=4,pady=8,sticky=W)

        Atten_roll=ttk.Entry(left_inside_frame,width=22,font=("comicsansns",11,"bold"))
        Atten_roll.grid(row=0,column=3,pady=8,sticky=W)

        #Name
        namelabel=Label(left_inside_frame,text="Name:",font=("comicsansns",11,"bold"),bg="white")
        namelabel.grid(row=1,column=0)

        Atten_roll=ttk.Entry(left_inside_frame,width=22,font=("comicsansns",11,"bold"))
        Atten_roll.grid(row=1,column=1,pady=8)

         #Department
        deplabel=Label(left_inside_frame,text="Department:",font=("comicsansns",11,"bold"),bg="white")
        deplabel.grid(row=1,column=2)

        Atten_dep=ttk.Entry(left_inside_frame,width=22,font=("comicsansns",11,"bold"))
        Atten_dep.grid(row=1,column=3,pady=8)

         #time
        timelabel=Label(left_inside_frame,text="Time:",font=("comicsansns",11,"bold"),bg="white")
        timelabel.grid(row=2,column=0)

        Atten_time=ttk.Entry(left_inside_frame,width=22,font=("comicsansns",11,"bold"))
        Atten_time.grid(row=2,column=1,pady=8)


        



        # Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Dtails",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)










if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()