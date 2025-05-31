# Here we are importing GUI libraries for better User Interface (toolkit interface)
from tkinter import *
from tkinter import ttk

import math




# For uploading image, we need to import pillow libraries
from PIL import Image, ImageTk ,ImageDraw 

# Creation of the main window class
class Face_Recognition_System:
    def __init__(self, root):
        self.root = root  # self.root will store the root window inside the class, making it accessible for any function inside the class
       
        self.root.geometry("1536x790+0+0")  #1530x790 → width = 1530, height = 790
                                            #+0+0 → place the window at position (0, 0) on the screen

        self.root.title("Face Recognition System By Rishabh")  # Set the window Title..

         # Get screen width inside the __init__ method
        width= self.root.winfo_screenwidth()
        height= self.root.winfo_screenheight()
        print(f"Screen Width: {width}, {height}")




        #  NOW Adding the image in the Window


        # ------------Setting BAckground Image

        img1 = Image.open(r"C:\Users\risha\Desktop\Python Project\Images\Background-pica.png")
        img1=img1.resize((1536,780),Image.Resampling.LANCZOS)

        # Storing Image In Variable
        self.photoimg = ImageTk.PhotoImage(img1) #This line converts a PIL image (img) into a format Tkinter can display, and stores it in the self.photoimg variable.

        #Set Image In  window through label
        f_lbl=Label(self.root,image=self.photoimg) # self.root parent conatiner where label appear
        f_lbl.place(x = 0, y = 0, width = 1536, height = 790)


        #------------Setting Another image and giving Shape 

        img2=Image.open(r"C:\Users\risha\Desktop\Python Project\Images\college.jpg")

        img2=img2.resize((150,150),Image.Resampling.LANCZOS).convert("RGBA")

        # Create circular mask
        mask = Image.new("L", (150, 150), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, 150, 150), fill=255)

        # Apply circular mask to image
        img2.putalpha(mask)

        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl2=Label(self.root,image=self.photoimg2 ,bg="black")

        f_lbl2.place(x=0, y=6,width=150 ,height=150)




        #  -------Giving The Title

        title_label=Label(f_lbl,text="[FACE] RECOGNITION ATTENDENCE SYSTEM SOFTWARE "
                          ,font=("Verdana",30,"bold"),
                          bg="black",
                          fg="red")

        title_label.place(x=50,y=87 ,width=1600,height=70)



        # ---NOW Making The Button Image
        

        # Button one--

        student=Image.open(r"C:\Users\risha\Desktop\Python Project\Images\student.jpg")
        student=student.resize((200,200),Image.Resampling.LANCZOS)
        self.stdudentimage= ImageTk.PhotoImage(student)

        b1=Button(f_lbl,image=self.stdudentimage,cursor="hand2",bg="#a8c0ff")
        b1.place(x=200,y=200,width=220,height=220)


        student_label =Button(f_lbl, text="STUDENT DETAILS", 
                              cursor="hand2", 
                              font=("Verdana", 12, "bold"),
                                bg="black" 
                                ,fg="red")
        student_label.place(x=200, y=430 ,width=220, height=30)  # Adjust the position as needed   



 # Button Two--
        
        detect_face=Image.open(r"C:\Users\risha\Desktop\Python Project\Images\detect.jpg")

        detect_face=detect_face.resize((200,200),Image.Resampling.LANCZOS)

        self.store=ImageTk.PhotoImage(detect_face)


        b2=Button(f_lbl,image=self.store,bg="#a8c0ff",cursor="hand2")
        b2.place(x=200,y=500,width=220,height=220)


        text2=Button(f_lbl,text="FACE DETECTOR" ,bg="black" ,fg="red",font=("Verdana", 12, "bold"),)
        text2.place(x=200, y=730,width=220, height=30)


        #button --3

        Attendence=Image.open(r"C:\Users\risha\Desktop\Python Project\Images\attendence.jpg")

        Attendence=Attendence.resize((200,200),Image.Resampling.LANCZOS)

        self.storeattendence=ImageTk.PhotoImage(Attendence)

        b3=Button(f_lbl,image=self.storeattendence,bg="#a8c0ff",cursor="hand2")
        b3.place(x=500,y=200,width=220,height=220)

        text3=Button(f_lbl,text="ATTENDENCE" ,bg="black" ,fg="red",font=("Verdana", 12, "bold"),)
        text3.place(x=500, y=430,width=220, height=30)




  #button --4 TRAIN DATA

        T_D=Image.open(r"C:\Users\risha\Desktop\Python Project\Images\train data.jpg")

        T_D=T_D.resize((200,200),Image.Resampling.LANCZOS)

        self.storeaT_D=ImageTk.PhotoImage(T_D)

        b4=Button(f_lbl,image=self.storeaT_D,bg="#a8c0ff",cursor="hand2")
        b4.place(x=800,y=200,width=220,height=220)

        text4=Button(f_lbl,text="TRAIN DATA" ,bg="black" ,fg="red",font=("Verdana", 12, "bold"),)
        text4.place(x=800, y=430,width=220, height=30) 



          #button --5 STUDENT PHOTOS

        photos=Image.open(r"C:\Users\risha\Desktop\Python Project\Images\gallery.webp")

        photos=photos.resize((200,200),Image.Resampling.LANCZOS)

        self.storeaph=ImageTk.PhotoImage(photos)

        b5=Button(f_lbl,image=self.storeaph,bg="#a8c0ff",cursor="hand2")
        b5.place(x=1100,y=200,width=220,height=220)

        text5=Button(f_lbl,text="STUDENT PHOTOS" ,bg="black" ,fg="red",font=("Verdana", 12, "bold"),)
        text5.place(x=1100, y=430,width=220, height=30) 




  #button --6 DEVELOPER DETAILS

        D_P=Image.open(r"C:\Users\risha\Desktop\Python Project\Images\developer.jpg")

        D_P= D_P.resize((200,200),Image.Resampling.LANCZOS)

        self.storeaD_P=ImageTk.PhotoImage(D_P)

        b6=Button(f_lbl,image=self.storeaD_P,bg="#a8c0ff",cursor="hand2")
        b6.place(x=500,y=500,width=220,height=220)

        text6=Button(f_lbl,text="DVELOPER" ,bg="black" ,fg="red",font=("Verdana", 12, "bold"),)
        text6.place(x=500, y=730,width=220, height=30) 



          #button --7 HELP

        heLP=Image.open(r"C:\Users\risha\Desktop\Python Project\Images\help.jpg")

        heLP=heLP.resize((200,200),Image.Resampling.LANCZOS)

        self.storeaheLP=ImageTk.PhotoImage(heLP)

        b7=Button(f_lbl,image=self.storeaheLP,bg="#a8c0ff",cursor="hand2")
        b7.place(x=800,y=500,width=220,height=220)

        text7=Button(f_lbl,text="HELP" ,bg="black" ,fg="red",font=("Verdana", 12, "bold"),)
        text7.place(x=800, y=730,width=220, height=30) 





          #button --8 EXIT

        EXIT=Image.open(r"C:\Users\risha\Desktop\Python Project\Images\EXIT.jpg")

        EXIT=EXIT.resize((200,200),Image.Resampling.LANCZOS)

        self.storeaEXIT=ImageTk.PhotoImage(EXIT)

        b8=Button(f_lbl,image=self.storeaEXIT,bg="#a8c0ff",cursor="hand2")
        b8.place(x=1100,y=500,width=220,height=220)

        text8=Button(f_lbl,text="EXIT" ,bg="black" ,fg="red",font=("Verdana", 12, "bold"),)
        text8.place(x=1100, y=730,width=220, height=30) 


# -------------------------------------------------------------------









  # Running and Creating the window

if __name__ == "__main__": # Condition check wether the script is being run directly or imported
    
    root =Tk()  # Creates The Main Windows Tkinter GUI

    obj= Face_Recognition_System(root) #  # Create an instance of your class

    root.mainloop() #Start the Tkinterloop and Window is Created







    







