from tkinter import*
from tkinter import ttk  #Button, Label, Entry, Frame, etc.
from PIL import Image, ImageTk ,ImageDraw                     

 #PIL stands for Python Imaging Library — it's a library in Python that adds image processing capabilities to your Python interpreter.
import cv2

from tkinter import messagebox  # this import messagebox so we can use in showing error
import mysql.connector


class Student :
    def __init__(self,root): #The __init__ method in Python is a special method used to initialize objects when a class is instantiated.(created from a class)

        self.root=root
        self.root.geometry("1536x790+0+0")
        self.root.title("Student Section Manager")

        #================Defining Variable for Storing Data ======

        self.var_department=StringVar()
        self.var_courses=StringVar()
        self.var_years=StringVar()
        self.var_Semester=StringVar()
        self.var_StudentId=StringVar()
        self.var_Student_Name=StringVar()
        self.var_Division=StringVar()
        self.var_Roll_No=StringVar()
        self.var_Gender=StringVar()
        self.var_DOB=StringVar()
        self.var_Email=StringVar() 
        self.var_Phone_No=StringVar()
        self.var_Address=StringVar()
        self.var_Teacher=StringVar()

       # Giving BACKGROUND IMAGE
        image1=Image.open(r"C:\Users\risha\Desktop\Python Project\Images\back.jpg")
        image1=image1.resize((1536,790),Image.Resampling.LANCZOS)
        self.backimg=ImageTk.PhotoImage(image1)
        
        placewin=Label(self.root,image=self.backimg)
        placewin.place(x=0,y=0)

        
        ##GIVING HEADING
        Heading=Label(placewin,text="S T U D E N T   M A N A G E M E N T   S Y S T E M",
                      font=("MonoLisa",40,"bold"),
                      bg="white",
                      fg="black")
        Heading.place(x=0,y=50,width=1530)
       

       
# MakinG Frame Inside placewin

        F_rame=Frame(placewin,bd=5)
        F_rame.place(x=70,y=150, width=1400, height=600) 

        #Here we Create Two label Frame in which we can give title (Can Give Title)

        lF_rame1=LabelFrame(F_rame,bd=2,relief=SUNKEN,text="STUDENT INFORMATION",font=("Arial",15,"bold"),fg="red")
        lF_rame1.place(x=0,y=0,width=605,height=590)


        lF_rame2=LabelFrame(F_rame,bd=2,relief=SUNKEN,text="FETCH--STUDENT DETAILS",font=("Arial",15,"bold"),fg="red")
        lF_rame2.place(x=610,y=20,width=780,height=570)


#Now Working Inside lF_rame1 (ONEE)

        #Putting A Image
        lF_rame1_img=Image.open(r"C:\Users\risha\Desktop\Python Project\Images\info.jpg")
        lF_rame1_img=lF_rame1_img.resize((580,100),Image.Resampling.LANCZOS)

        self.frameimg=ImageTk.PhotoImage(lF_rame1_img)

        frame1=Label(lF_rame1,image=self.frameimg)
        frame1.place(x=6,y=0,)

        #Making Two label Frame Inside The farme 1
        
        #Current Course Info
        in_frame1=LabelFrame(lF_rame1,bd=2,text="Current Course Information",font=("Arial",10,"bold"),fg="grey",relief=RIDGE )
        in_frame1.place(x=0,y=100 ,width=700,height=100)

           #-------Making Boxes that is Grid

        department=Label(in_frame1,text="Department:", font=("times new roman",12,"bold"))
        department.grid(row=0,column=0,padx=10) #[0,0]
        department_combobox=ttk.Combobox(in_frame1,textvariable=self.var_department,font=("times new roman",12,),width=17, state="readonly")
        department_combobox["values"]=("Select Department","Computer-Science","Mechanical-Branch","Electrical-Branch","Computer-Applications","Medical-Branch")
        department_combobox.current(0)
        department_combobox.grid(row=0,column=1,padx=10,pady=10,sticky=W) #[0,1] first column hai to aage aajyega


        courses=Label(in_frame1,text="Courses:", font=("times new roman",12,"bold"))
        courses.grid(row=0,column=2)
        courses_combobox=ttk.Combobox(in_frame1,textvariable=self.var_courses,font=("times new roman",12,),width=17,state="readonly")
        courses_combobox["values"]=("Select Courses","Course-1","Course-2","Course-3","Course-4")
        courses_combobox.current(0)
        courses_combobox.grid(row=0, column=3,padx=10,pady=10,sticky=W)



        Year=Label(in_frame1,text="Year:", font=("times new roman",12,"bold"))
        Year.grid(row=1,column=0) 
        Year_combobox=ttk.Combobox(in_frame1,textvariable=self.var_years,font=("times new roman",12,),width=17,state="readonly")
        Year_combobox["values"]=("Select-Year","2021-24","2024-27","2027-30","2030-33","2033-36")
        Year_combobox.current(0)
        Year_combobox.grid(row=1,column=1,padx=10,sticky=W)
        

          
        Semester=Label(in_frame1,text="Semester:", font=("times new roman",12,"bold"))
        Semester.grid(row=1,column=2) 
        Semester_combobox=ttk.Combobox(in_frame1,textvariable=self.var_Semester,font=("times new roman",12,),width=17,state="readonly")
        Semester_combobox["values"]=("Select-Semester","First-Prof","Second-Prof","Third-Prof","Fourth-Prof","Fifth-Prof","Sixth-Prof")
        Semester_combobox.current(0)
        Semester_combobox.grid(row=1,column=3,padx=10,sticky=W)


        #Student class Information
        in_frame2=LabelFrame(lF_rame1,bd=2,text="Student Class Information",font=("Arial",10,"bold"),fg="grey",relief=RIDGE)
        in_frame2.place(x=0,y=200 ,width=700,height=300)


        Student_id=Label(in_frame2,text="Student-ID :",font=("times new roman",12,"bold"))
        Student_id.grid(row=0,column=0,padx=10,pady=10)
        Student_id_entry=ttk.Entry(in_frame2,textvariable=self.var_StudentId,font=("times new roman",12,),width=20)
        Student_id_entry.grid(row=0,column=1,sticky=W)

        
        Student_Name=Label(in_frame2,text="Student-Name :",font=("times new roman",12,"bold"))
        Student_Name.grid(row=0,column=2,padx=10,pady=10)
        Student_Name_entry=ttk.Entry(in_frame2,textvariable=self.var_Student_Name,font=("times new roman",12,),width=20)
        Student_Name_entry.grid(row=0,column=3,sticky=W)

        
        
        Class_Division=Label(in_frame2,text="Class-Division :",font=("times new roman",12,"bold"))
        Class_Division.grid(row=1,column=0,padx=10,pady=10)
        Class_Division_combobox=ttk.Combobox(in_frame2,textvariable=self.var_Division,font=("times new roman",12,),width=18,state="readonly")
        Class_Division_combobox["values"]=("Division","Ist","2nd","4th","5th","6th")
        Class_Division_combobox.current(0)
        Class_Division_combobox.grid(row=1,column=1,sticky=W)

         
        Roll_NO=Label(in_frame2,text="Roll.NO :",font=("times new roman",12,"bold"))
        Roll_NO.grid(row=1,column=2,padx=10,pady=10)
        Roll_NO_entry=ttk.Entry(in_frame2,textvariable=self.var_Roll_No,font=("times new roman",12,),width=20)
        Roll_NO_entry.grid(row=1,column=3,sticky=W)


        Gender=Label(in_frame2,text="Gender :",font=("times new roman",12,"bold"))
        Gender.grid(row=3,column=0,padx=10,pady=10)
        Gender_combobox=ttk.Combobox(in_frame2,textvariable=self.var_Gender,font=("times new roman",12,),width=18,state="readonly")
        Gender_combobox["values"]=("Select-Gender","Male","Female")
        Gender_combobox.current(0)
        Gender_combobox.grid(row=3,column=1,sticky=W)
       
        
        DOB=Label(in_frame2,text="DOB:",font=("times new roman",12,"bold"))
        DOB.grid(row=3,column=2,padx=10,pady=10)
        DOB_entry=ttk.Entry(in_frame2,textvariable=self.var_DOB,font=("times new roman",12,),width=20)
        DOB_entry.grid(row=3,column=3,sticky=W)
       
        Email=Label(in_frame2,text="Email-ID :",font=("times new roman",12,"bold"))
        Email.grid(row=4,column=0,padx=10,pady=10)
        Email_entry=ttk.Entry(in_frame2,textvariable=self.var_Email,font=("times new roman",12,),width=20)
        Email_entry.grid(row=4,column=1,sticky=W)


        Phonenumber=Label(in_frame2,text="Phone-Number:",font=("times new roman",12,"bold"))
        Phonenumber.grid(row=4,column=2,padx=10,pady=10)
        Phonenumber_entry=ttk.Entry(in_frame2,textvariable=self.var_Phone_No,font=("times new roman",12,),width=20)
        Phonenumber_entry.grid(row=4,column=3,sticky=W)


        Adress=Label(in_frame2,text="Adress :",font=("times new roman",12,"bold"))
        Adress.grid(row=5,column=0,padx=10,pady=10)
        Adress_entry=ttk.Entry(in_frame2,textvariable=self.var_Address,font=("times new roman",12,),width=20)
        Adress_entry.grid(row=5,column=1,sticky=W)


        Teacher=Label(in_frame2,text="Teacher-Name :",font=("times new roman",12,"bold"))
        Teacher.grid(row=5,column=2,padx=10,pady=10)
        Teacher_entry=ttk.Entry(in_frame2,textvariable=self.var_Teacher,font=("times new roman",12,),width=20)
        Teacher_entry.grid(row=5,column=3,sticky=W)


        #Creating radio BUtton
        self.var_radio=StringVar()
        Radiobutton1_select=ttk.Radiobutton(in_frame2,command=self.Generate_Datasheet,variable=self.var_radio,text="Take Photo Sample",value="Yes")
        Radiobutton1_select.grid(row=6,column=0,pady=20)

        
        Radiobutton2_select=ttk.Radiobutton(in_frame2,variable=self.var_radio,text="NO Photo Sample",value="No")
        Radiobutton2_select.grid(row=6,column=1)


        #image
        Right_Frame=LabelFrame(in_frame2,bd=2,relief=RIDGE,bg="white")
        Right_Frame.place(x=300,y=220,width="300",height="60")

        


        #Making Buttons Inside lf_rame1
        
        b1=Button(lF_rame1,text="Save",command=self.Add_Data,font=("Arial",10,"bold"),bg="black",fg="white")
        b1.place(x=0,y=501,width="149")
        
        b2=Button(lF_rame1,text="Delete",command=self.Deleting_Data,font=("Arial",10,"bold"),bg="black",fg="white")
        b2.place(x=150,y=501,width="149")
        
        b3=Button(lF_rame1,text="Update",command=self.Update_info,font=("Arial",10,"bold"),bg="black",fg="white")
        b3.place(x=300,y=501,width="149")
        
        b4=Button(lF_rame1,text="Reset",command=self.Reset_Fill,font=("Arial",10,"bold"),bg="black",fg="white")
        b4.place(x=450,y=501,width="149")
        
        b5=Button(lF_rame1,text="ADD Photo Sample",font=("Arial",10,"bold"),bg="black",fg="white")
        b5.place(x=0,y=530,width="300")

        b6=Button(lF_rame1,text="Update Photo Sample",font=("Arial",10,"bold"),bg="black",fg="white")
        b6.place(x=300,y=530,width="300")



#Now Working Inside lF_rame2 (Twoo)

        lF_rame2_img=Image.open(r"C:\Users\risha\Desktop\Python Project\Images\4905827.jpg")
        lF_rame2_img=lF_rame2_img.resize((800,220),Image.Resampling.LANCZOS)

        self.frameimg2=ImageTk.PhotoImage(lF_rame2_img)

        frame2=Label(lF_rame2,image=self.frameimg2)
        frame2.place(x=1,y=0,)

        in_frame3=LabelFrame(lF_rame2,bd=2,text="View Student Details and Search System ",font=("Arial",10,"bold"),fg="grey",relief=RIDGE)
        in_frame3.place(x=0,y=220 ,width=790,height=80)

       #--
        Search_by=Label(in_frame3,text="SEARCH BY--",font=("Arial",12,"bold"),bg="Green",fg="WHite")
        Search_by.place(x=10,y=10)
       
        Select_option=ttk.Combobox(in_frame3,font=("times new roman",12,),height=80,state="readonly")
        Select_option["value"]=("Select-Option","Student-ID","Rollno","Email-ID","Student-Name","Class-Division","Phone-Number")
        Select_option.current(0)
        Select_option.place(x=150,y=10)

        Empty_box=ttk.Entry(in_frame3,font=("times new roman",12,))
        Empty_box.place(x=350,y=10)

        b_search=Button(in_frame3,text="Search",font=("Arial",12,"bold"),width="10",bg="black",fg="white",)
        b_search.place(x=520,y=6,height="30")

        
        b_showALl=Button(in_frame3,text="Show-All",font=("Arial",12,"bold"),width="10",bg="black",fg="white")
        b_showALl.place(x=640,y=6,height="30")


        #Making table Frame For Store Data And Fetch Data---------------------------------------------------------

        table_frame=Frame(lF_rame2,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=3,y=302,width="770",height="240")

        #making SCrollbar inide Frame
        Scrol_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        Scrol_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

       #This Treeview belongs to this object (self) so I can use it anywhere else inside the class methods Thats why Self Use here."

       
       # xscrollcommand = Scrol_x.set
#➜ Connects the horizontal scrollbar (Scrol_x) to the widget  like treeview.

      #yscrollcommand = Scrol_y.set
# ➜ Connects the vertical scrollbar (Scrol_y) to the widget.


# pack()----It automatically arranges the widget inside its parent (like a frame or the main window), either top to bottom, left to right, or based on the options you give.

        self.student_table=ttk.Treeview(table_frame,columns=("Department","Course","Year","Semester","ID","Name","Division","ROll","Gender","DOB","Email","Phone","Adress","Teacher","Photo"), xscrollcommand=Scrol_x.set , yscrollcommand=Scrol_y.set)

        #Managing The column width
        self.student_table.column("ID", width=100)
        self.student_table.column("Department" ,width=100)
        self.student_table.column("Course",width="100")
       

        Scrol_x.pack(side=BOTTOM,fill=X)
        Scrol_y.pack(side=RIGHT,fill=Y)

        Scrol_x.config(command=self.student_table.xview)
        #👉 You're telling the horizontal scrollbar (Scrol_x) to control the horizontal scrolling of the Treeview widget (self.student_table).
        Scrol_y.config(command=self.student_table.yview)

        #Working on Treeview
        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("ID",text="ID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Division",text="Division")
        self.student_table.heading("ROll",text="ROll.NO")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email-ID")
        self.student_table.heading("Phone",text="Phone-NO")
        self.student_table.heading("Adress",text="Address")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Photo",text="Photo")
        self.student_table["show"]="headings"

        

        #setting column width Aise hi sabme set kr sakte width set
        #self.student_table.column("Department",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.Edit_data)
        self.fetch_data()
        
        #fill=BOTH → Fills the available space.
        #expand=1 → Expands when the window is resized.





#=========================NOW HERE WE DEFINE THE FUNCTION TO STORE THE DATABASES  IN MY SQL====================
 
 
    def Add_Data(self):
     if self.var_department.get()=="Select Department" or self.var_courses.get()=="" or self.var_years.get()=="" or self.var_Semester=="" or self.var_StudentId.get()=="" or self.var_Student_Name.get()=="" or self.var_Division.get()=="Division" or self.var_Roll_No.get()=="" or self.var_Gender.get()=="Gender" or self.var_DOB.get()=="" or self.var_Email.get()=="" or self.var_Phone_No.get()=="" or self.var_Address.get()=="" or self.var_Teacher.get()=="" or self.var_radio.get()=="":
      messagebox.showerror("Error","ALL Fields are Required",parent=self.root)
      
      # This parent self root help taht error not show in other Window..
     
     else:
         try:
                #now here we connect the sql to this class or we can say to python
                conn=mysql.connector.connect(host="localhost",username="Rishabh",password="Alfa@123456789",database="face_recognition_data")


                #creating cursor
                create_cursor=conn.cursor()
                #here jo query likhte mysql me usko cursor ki help se execute krenge
                create_cursor.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_department.get(),
                                                                                                                self.var_courses.get(),
                                                                                                                self.var_years.get(),
                                                                                                                self.var_Semester.get(),
                                                                                                                self.var_StudentId.get(),
                                                                                                                self.var_Student_Name.get(),
                                                                                                                self.var_Division.get(),
                                                                                                                self.var_Roll_No.get(),
                                                                                                                self.var_Gender.get(),
                                                                                                                self.var_DOB.get(),
                                                                                                                self.var_Email.get(),
                                                                                                                self.var_Phone_No.get(),
                                                                                                                self.var_Address.get(),
                                                                                                                self.var_Teacher.get(),
                                                                                                                self.var_radio.get()
                                                                                                                

                                                                                                                ))
        
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details Added Successfully",parent=self.root)          
         except Exception as es:
             messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)   





 #===================================Fetching The Data We Make Another Function.... To show in other frame after saving in sql================

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="Rishabh",password="Alfa@123456789",database="face_recognition_data")
        my_cursor=conn.cursor() #here using cursor to fetch data
        my_cursor.execute("select * from students") # select all data that fetched
        storingdata=my_cursor.fetchall() #storing inside it

        if len(storingdata)!=0: #Checks if storingdata is not empty.
             self.student_table.delete(*self.student_table.get_children())

             for i in storingdata:
                 self.student_table.insert("",END,values=i)
             conn.commit()  
        conn.close()
         
 #================================== We Make Another Function.... To Edit The Data after click in the treeview================
    def Edit_data(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        Data=content["values"]

        self.var_department.set(Data[0]) 
        self.var_courses.set(Data[1])
        self.var_years.set(Data[2])
        self.var_Semester.set(Data[3])
        self.var_StudentId.set(Data[4])
        self.var_Student_Name.set(Data[5])
        self.var_Division.set(Data[6])
        self.var_Roll_No.set(Data[7])
        self.var_Gender.set(Data[8])
        self.var_DOB.set(Data[9])
        self.var_Email.set(Data[10]) 
        self.var_Phone_No.set(Data[11])
        self.var_Address.set(Data[12])
        self.var_Teacher.set(Data[13])
        self.var_radio.set(Data[14])

     #================================== Working On Update So Make A fucntion============================================   

    def Update_info(self):
         if self.var_department.get()=="Select Department" or self.var_courses.get()=="" or self.var_years.get()=="" or self.var_Semester=="" or self.var_StudentId.get()=="" or self.var_Student_Name.get()=="" or self.var_Division.get()=="Division" or self.var_Roll_No.get()=="" or self.var_Gender.get()=="Gender" or self.var_DOB.get()=="" or self.var_Email.get()=="" or self.var_Phone_No.get()=="" or self.var_Address.get()=="" or self.var_Teacher.get()=="" or self.var_radio.get()=="":
            messagebox.showerror("Error","ALL Fields are Required",parent=self.root)
      
         else:
             try:
                 Update=messagebox.askyesno("Upadte","Do You Want to Update This student Details",parent=self.root)
                 if Update>0:
                      conn=mysql.connector.connect(host="localhost",username="Rishabh",password="Alfa@123456789",database="face_recognition_data")
                      my_cursor=conn.cursor()
                      my_cursor.execute("update students set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll_No=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Adress=%s,Teacher=%s,PhotoSample=%s where Student_ID=%s",(
                                                                                                                self.var_department.get(),
                                                                                                                self.var_courses.get(),
                                                                                                                self.var_years.get(),
                                                                                                                self.var_Semester.get(),
                                                                                                                self.var_Student_Name.get(),
                                                                                                                self.var_Division.get(),
                                                                                                                self.var_Roll_No.get(),
                                                                                                                self.var_Gender.get(),
                                                                                                                self.var_DOB.get(),
                                                                                                                self.var_Email.get(),
                                                                                                                self.var_Phone_No.get(),
                                                                                                                self.var_Address.get(),
                                                                                                                self.var_Teacher.get(),
                                                                                                                self.var_radio.get(),
                                                                                                                self.var_StudentId.get(),
                                     
                      ))
                     
                 else:
                     if  not Update:
                         return
                 messagebox.showinfo("Success","Student Deatil succefully Completed",parent=self.root)
                 conn.commit()
                 self.fetch_data()
                 conn.close()

             except Exception as es:
                 messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

           
           
                      #================================== Working On Another BUtton That Is Delete ============================================ 

#for deletng whole data We select Student_Id..
    def Deleting_Data(self):
        if self.var_StudentId.get()=="":
            messagebox("Error","Student Id Must be required",parent=self.root)
        else:
            try:
                Delete=messagebox.askyesno("Student Delete Page","Do You Want To Delete This Student Data",parent=self.root)
                if Delete>0:
                   conn=mysql.connector.connect(host="localhost",username="Rishabh",password="Alfa@123456789",database="face_recognition_data")
                   my_cursor=conn.cursor()

 #writing queries for sql 
                   sql="delete from students where Student_ID=%s"
                   value=(self.var_StudentId.get(),)
                   my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Deleted","Successfuly Deleted Student Details",parent=self.root)       
                     
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)        


        
      #================================== Working On Another BUtton That Is Reset ============================================ 
    def Reset_Fill(self):
        self.var_department.set("Select Department")
        self.var_courses.set("Select Course")
        self.var_years.set("Select Year")
        self.var_Semester.set("Select Semester")
        self.var_StudentId.set("")
        self.var_Student_Name.set("")
        self.var_Division.set("Select Division")
        self.var_Roll_No.set("")
        self.var_Gender.set("Select Gender")
        self.var_DOB.set("")
        self.var_Email.set("")
        self.var_Phone_No.set("")
        self.var_Address.set("")
        self.var_Teacher.set("")
        self.var_radio.set("")



        #===================Genrating A photo Sample====================

    def Generate_Datasheet(self):
        if self.var_department.get()=="Select Department" or self.var_courses.get()=="" or self.var_years.get()=="" or self.var_Semester=="" or self.var_StudentId.get()=="" or self.var_Student_Name.get()=="" or self.var_Division.get()=="Division" or self.var_Roll_No.get()=="" or self.var_Gender.get()=="Gender" or self.var_DOB.get()=="" or self.var_Email.get()=="" or self.var_Phone_No.get()=="" or self.var_Address.get()=="" or self.var_Teacher.get()=="" or self.var_radio.get()=="":
               
         messagebox.showerror("Error","ALL Fields are Required",parent=self.root)
        else:
            try:
                    conn=mysql.connector.connect(host="localhost",username="Rishabh",password="Alfa@123456789",database="face_recognition_data" )
                    my_cursor=conn.cursor()
                    my_cursor.execute("select * from students")
                    my_result=my_cursor.fetchall()

                    id=0
                    for x in my_result:
                        id+=1
                    my_cursor.execute("update students set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll_No=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Adress=%s,Teacher=%s,PhotoSample=%s where Student_ID=%s",(
                                                                                                                self.var_department.get(),
                                                                                                                self.var_courses.get(),
                                                                                                                self.var_years.get(),
                                                                                                                self.var_Semester.get(),
                                                                                                                self.var_Student_Name.get(),
                                                                                                                self.var_Division.get(),
                                                                                                                self.var_Roll_No.get(),
                                                                                                                self.var_Gender.get(),
                                                                                                                self.var_DOB.get(),
                                                                                                                self.var_Email.get(),
                                                                                                                self.var_Phone_No.get(),
                                                                                                                self.var_Address.get(),
                                                                                                                self.var_Teacher.get(),
                                                                                                                self.var_radio.get(),
                                                                                                                self.var_StudentId.get()
                                     
                      ))    
                    

                    conn.commit()
                    self.fetch_data()
                    self.Reset_Fill()
                    conn.close()



                    # Getting xml file or Loading xml file  from python location  only for face frontal 
                    face_classiefier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
             
                    
                    def face_cropped(img):
                        #!Convert colourfull to grayscale coz it have one shade not like RGB 3-shades easy to detect
                        # This line converts a color image (img) from BGR (Blue, Green, Red) format to Grayscale format, and stores the result in the variable gray.
                        grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

                        #!Detect faces
                        # This line is using OpenCV’s Haar Cascade classifier to detect faces in the grayscale image.
                        #Scalebehaviour=1.3=30% shrink to 24*24---fast but not precise
                        #minneighbors=5 =means 5 overlapping in one place so it is face
                        face=face_classiefier.detectMultiScale(grey,1.3,5)

                        #!Making rectangle for Face
                        for(x,y,w,h) in face:
                            face_cropped=img[y : y+h, x : x+w]
                            return face_cropped
                        
                        #open a camera
                    camera=cv2.VideoCapture(0)#opens a camera 0-for default camera for other camera write 1

                    #jab bhi capture krein images ko then it stored in this variable
                    img_id=0
                    while True:# Agar Img_id 1 hua to true hoga aur run krega

                        ret,my_frames=camera.read() # idhar My_frames me jo click kiyein wo stored hoga  

                        if face_cropped(my_frames) is not None: # agra ye khali nhi hua to aage jayega
                                    
                                    img_id+=1

                                        #cropping image that we taken
                                    crop_image=cv2.resize(face_cropped(my_frames),(450,450)) 

                                    #now again convert BGR to grey Scale
                                    crop_image=cv2.cvtColor(crop_image,cv2.COLOR_BGR2GRAY)

                                    #Storing Image In file
                                    image_file_path="/Face Recognition System/Images_Data "+str(id)+"."+str(img_id)+".jpg"
                                    
                                    # Final Saving Step (you probably have this later):
                                    cv2.imwrite(image_file_path,crop_image)

                                    #This function overlays text on an image or video frame.
                                    cv2.putText(crop_image,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)

                                    #Show Camera
                                    cv2.imshow("Cropped Face",crop_image)

                        #limit the capture 
                        if cv2.waitKey(1)==13 or int(img_id)==100:#total image lega 100
                            break

                    camera.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Generating Data Set Completed")    


                        

                    


            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}", parent=self.root)    
                   
     
















if __name__== "__main__":
        root=Tk() # create The main window
        obj=Student(root) #This creates an object named obj from the Student class, and passes the root window into it.
        root.mainloop()



    
