from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root 
        self.root.geometry("1530x790+0+0") 
        self.root.title("Face Recogniton System")


        #variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_section=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_contact=StringVar()
        self.var_padd=StringVar()
        self.var_cadd=StringVar()


        #First Image
        img=Image.open(r"C:\Users\bhupe\Desktop\Face Recognization system\college_images\face-recognition.png")  
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #second Image
        img1=Image.open(r"C:\Users\bhupe\Desktop\Face Recognization system\college_images\smart-attendance.jpg")   
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #Third Image
        img2=Image.open(r"C:\Users\bhupe\Desktop\Face Recognization system\college_images\iStock-182059956_18390_t12.jpg")  
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        
        #BAckground Image
        img3=Image.open(r"C:\Users\bhupe\Desktop\Face Recognization system\college_images\p2551980.jpg")  
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45) 

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20 ,y=50,width=1480,height=600)

        # left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Dtails",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open(r"C:\Users\bhupe\Desktop\Face Recognization system\college_images\AdobeStock_303989091.jpeg")  
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)
        #current course information
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=125)

        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","Computer Science","IT","Civil","Mechanical","Management","Electrical","Science","Fashion Design")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="readonly")
        course_combo["values"]=("Select Course","B.Tech","BCA","BBA","B.Sc","MCA","MBA","M.Tech","M.Sc")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="readonly")
        year_combo["values"]=("Select Year","2019-2020","2020-2021","2021-2022","2022-2023","2023-2024","2024-2025")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        sem_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=17,state="readonly")
        sem_combo["values"]=("Select Semester","1","2","3","4","5","6","7","8")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class Student information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width=720,height=300)


        #Student id
        studentId_label=Label(class_student_frame,text="Student Id:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,sticky=W)

        #Student name
        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        
        #Student Section
        studentSection_label=Label(class_student_frame,text="Section:",font=("times new roman",12,"bold"),bg="white")
        studentSection_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        #studentSection_entry=ttk.Entry(class_student_frame,textvariable=self.var_section,width=20,font=("times new roman",13,"bold"))
        #studentSection_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        studentSection_combo=ttk.Combobox(class_student_frame,textvariable=self.var_section,font=("times new roman",12,"bold"),width=20,state="readonly")
        studentSection_combo["values"]=("Select Section","A","B","C","D","E","F","G","H","I")
        studentSection_combo.current(0)
        studentSection_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        #Student Rollno
        studentRoll_label=Label(class_student_frame,text="Class Roll No.:",font=("times new roman",12,"bold"),bg="white")
        studentRoll_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        studentRoll_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        studentRoll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        
        #Student Gender
        studentGender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        studentGender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        #studentGender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",13,"bold"))
        #studentGender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        studentGender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=20,state="readonly")
        studentGender_combo["values"]=("Select Gender","Male","Female","Other")
        studentGender_combo.current(0)
        studentGender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        
        #Student DOB
        studentdob_label=Label(class_student_frame,text="Date of Birth:",font=("times new roman",12,"bold"),bg="white")
        studentdob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        studentdob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        studentdob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        
        #Student phone no
        studentphone_label=Label(class_student_frame,text="Contact Number:",font=("times new roman",12,"bold"),bg="white")
        studentphone_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        studentphone_entry=ttk.Entry(class_student_frame,textvariable=self.var_contact,width=20,font=("times new roman",13,"bold"))
        studentphone_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        
        #Student Email
        studentEmail_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        studentEmail_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        studentEmail_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        studentEmail_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        
        #Student address
        studentAdd_label=Label(class_student_frame,text="Permanent Address:",font=("times new roman",12,"bold"),bg="white")
        studentAdd_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        studentAdd_entry=ttk.Entry(class_student_frame,textvariable=self.var_padd,width=20,font=("times new roman",13,"bold"))
        studentAdd_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        
        #Student cadd
        studentCadd_label=Label(class_student_frame,text="Current Address:",font=("times new roman",12,"bold"),bg="white")
        studentCadd_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        studentCadd_entry=ttk.Entry(class_student_frame,textvariable=self.var_cadd,width=20,font=("times new roman",13,"bold"))
        studentCadd_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        radiobutton1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobutton1.grid(row=6,column=0)

        radiobutton2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobutton2.grid(row=6,column=1)

        # buttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn=Button(btn_frame,command=self.add_data,text="Save",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        updatebtn=Button(btn_frame,command=self.update_data,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        updatebtn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,command=self.delete_data,text="Delete",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)
        

        takephoto_btn=Button(btn_frame1,command=self.generate_dataset,text="Take photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        takephoto_btn.grid(row=0,column=0)

        updatephoto_btn=Button(btn_frame1,text="Update photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        updatephoto_btn.grid(row=0,column=1)

        # Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Dtails",font=("times new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=690,height=580)

        img_right=Image.open(r"C:\Users\bhupe\Desktop\Face Recognization system\college_images\gettyimages-1022573162.jpg")  
        img_right=img_right.resize((720,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)

        #search System.........
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=680,height=70)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        
        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=15,state="readonly")  
        search_combo["values"]=("Select","Roll No","Phone No.")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


        search_btn=Button(search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        
        showAll_btn=Button(search_frame,text="Show All",width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        #table frame.............
        table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=680,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","Course","year","Sem","Id","Name","Section","Roll","Gender","DOB","Email","Contact","Padd","Cadd","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("Id",text="Student Id")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Section",text="Section")
        self.student_table.heading("Roll",text="Roll No.")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="Date of Birth")
        self.student_table.heading("Email",text="Email Id")
        self.student_table.heading("Contact",text="Contact No.")
        self.student_table.heading("Padd",text="Permanent Address")
        self.student_table.heading("Cadd",text="Current Address")
        self.student_table.heading("Photo",text="Photo Sample Status")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100) 
        self.student_table.column("Course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("Id",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Section",width=100)
        self.student_table.column("Roll",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Contact",width=100)
        self.student_table.column("Padd",width=100)
        self.student_table.column("Cadd",width=100)
        self.student_table.column("Photo",width=100)   

        self.student_table.pack(fill=BOTH, expand=1) 
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #function declaration
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()==""or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Singh@123#",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_std_id.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_section.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_contact.get(),
                                                                                                            self.var_padd.get(),
                                                                                                            self.var_cadd.get(),
                                                                                                            self.var_radio1.get()
                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","stdent details has been added Sccessfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    #fetch data Function
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Singh@123#",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # get cursor function
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_section.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_contact.set(data[11]),
        self.var_padd.set(data[12]),
        self.var_cadd.set(data[13]),
        self.var_radio1.set(data[14])


    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()==""or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                upadate=messagebox.askyesno("Update","Do You Want TO Update This student details",parent=self.root)
                if upadate>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Singh@123#",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Section=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Padd=%s,Cadd=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                        self.var_section.get(),
                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                        self.var_contact.get(),
                                                                                                                                                                                        self.var_padd.get(),
                                                                                                                                                                                        self.var_cadd.get(),
                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                        self.var_std_id.get()
                                                                                                                                                                                    ))
                else:
                    if not upadate:
                        return
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root) 
                conn.commit()
                self.fetch_data()
                conn.close() 
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this Student data",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Singh@123#",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    #reset   function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_section.set("Select Section")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_contact.set("")
        self.var_padd.set("")
        self.var_cadd.set("")
        self.var_radio1.set("")   

    # Generate data set or take photo samples
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()==""or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Singh@123#",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall() 
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Section=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Padd=%s,Cadd=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                        self.var_section.get(),
                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                        self.var_contact.get(),
                                                                                                                                                                                        self.var_padd.get(),
                                                                                                                                                                                        self.var_cadd.get(),
                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                        self.var_std_id.get()==id+1
                                                                                                                                                                                    ))           
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #load predefined data on face frontals from opencv

                face_classifier=cv2.CascadeClassifier(r"C:\Users\bhupe\Desktop\Face Recognization system\haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimun neighbor=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame)is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed !!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)     
           



        













        
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()   