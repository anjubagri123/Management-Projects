from tkinter import *
from tkinter import ttk        #provide combobox
from PIL import Image,ImageTk     #install it for background with pip install pillow
import pymysql
from tkinter import messagebox
import datetime
import time
import random
def main():
     win=Tk()
     app=Login_Window(win)
     win.mainloop()


class Login_Window:
   def __init__(self,root):    # constructer initailize
        self.root=root           #initializing root
        self.root.title("Login")     # Title of our window
        self.root.geometry("1350x700+0+0")  

  
  #======All variables=========#

        # self.username_var=StringVar()    # IntVar we always use only for operational variable purpose
        # self.password_var=StringVar() 
         
        #=========background=========#
        bgimg = Image.open("C:\\Users\\BAGRI\\Desktop\\face_Recognition system\\college_image\\background1.jpg")
        bgimg = bgimg.resize((1354,710),Image.ANTIALIAS)
        self.photobgimg = ImageTk.PhotoImage(bgimg)

        bg_img = Label(self.root,image= self.photobgimg)
        bg_img.place(x=0,y=0,width=1354,height=710)

         #============black frame=================#

        frame=Frame(self.root,bg="black")
        frame.place(x=520,y=150,width=340,height=450)

        #===========top image of person===========#
        img1=Image.open("C:\\Users\\BAGRI\\Desktop\\face_Recognition system\\college_image\\person.png")
        img1 = img1.resize((100,100),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1) 

        img_1 = Label(image= self.photoimg1,bg="black",borderwidth=0)
        img_1.place(x=646,y=170,width=100,height=100)

        #==========label getstarted===========#

        get_Str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_Str.place(x=100,y=120)

        #===========Label==============#
        username_lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username_lbl.place(x=70,y=155)
           
        #===========text user===========#
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)


       #===========password label===========#
        Pass_lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        Pass_lbl.place(x=70,y=220)
 
         #===========text pass===============#
        self.txtpass=ttk.Entry(frame,show='*',font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=245,width=270)
        

        #===============Icons================#
            #=============person==================#
        img2=Image.open("C:\\Users\\BAGRI\\Desktop\\face_Recognition system\\college_image\\person.png")
        img2 = img2.resize((23,23),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2) 

        img_2 = Label(image= self.photoimg2,bg="black",borderwidth=0)
        img_2.place(x=562,y=304,width=23,height=23)

      #   #=============lock icons=================#
         
        img3=Image.open("C:\\Users\\BAGRI\\Desktop\\face_Recognition system\\college_image\\lock.png")
        img3 = img3.resize((23,23),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3) 

        img_3 = Label(image= self.photoimg3,bg="black",borderwidth=0)
        img_3.place(x=560,y=369,width=23,height=23)

      #   #============login button==================#
        login_btn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        login_btn.place(x=110,y=300,width=120,height=35)

          #============register button==================#
        Register_btn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",15,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        Register_btn.place(x=10,y=350,width=160)

        #============forget password button==================#
        forgetpass_btn=Button(frame,text="Forget password?",command=self.forget_password_window,font=("times new roman",15,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetpass_btn.place(x=10,y=378,width=160)
   
   #=======do work with registration button=========#
   def register_window(self):
        self.new_Window=Toplevel(self.root)
        self.app=Register(self.new_Window)

   def login (self):
        if self.txtuser.get() =="" or self.txtpass.get()=="":
             messagebox.showerror("Error","All Fields Required.")  
        elif self.txtuser.get()=="Aditi" and self.txtpass.get()=="Anju":
             
                #Anju == password, Aditi == Username====#
             messagebox.showinfo("Success","Welcome to Student Management Project")
        else:
             con=pymysql.connect(host="localhost",user="root",password="",database="stm")
             cur=con.cursor()  
             cur.execute("select * from register where email=%s and password=%s",(
                            self.txtuser.get(),
                            self.txtpass.get()

                  
                          ))
             row=cur.fetchone()
             if row==None:
                  messagebox.showerror("Error","Invalid Username & Password")
             else:
                  open_main=messagebox.askyesno("YesNo","Access only admin")
             if open_main>0:
                  self.new_Window=Toplevel(self.root)
                  self.app=Student(self.new_Window)
             else:
                  if not open_main:
                       return
             con.commit()
             con.close()


  #===================Reset Password Function================#
   def reset_pass(self):
        if self.combo_SQ.get()=="Select":
            messagebox.showerror("Error","Select Security Question",parent=self.root2)
        elif self.txt_SecurityAns_entry.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_NewPass_entry.get()=="":
             messagebox.showerror("Error","Please enter the new Password",parent=self.root2)
        else:
             con=pymysql.connect(host="localhost",user="root",password="",database="stm")
             cur=con.cursor()  
             query=("select * from register where email=%s and securityQ=%s and securityA=%s")
             value=(self.txtuser.get(),self.combo_SQ.get(),self.txt_SecurityAns_entry.get(),)
             cur.execute(query,value)
             row=cur.fetchone()
             if row==None:
                  messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
             else:
                  query=("update register set password=%s where email=%s")
                  value=(self.txt_NewPass_entry.get(),self.txtuser.get())
                  cur.execute(query,value)
                  con.commit()
                  con.close()
                  messagebox.showinfo("Info","Your Password has been Reset Successfully, Please Login with your new Password Next time.",parent=self.root2)
                  self.root2.destroy()     # to disappear (close) the forget window
             




#==============forget Password window==========================#
   def forget_password_window(self):
        if self.txtuser.get()=="":
             messagebox.showerror("Error","Please Enter the Email Address to reset password")
        else:
                con=pymysql.connect(host="localhost",user="root",password="",database="stm")
                cur=con.cursor()   
                query=("select * from register where email=%s")        
                value=(self.txtuser.get(),)

                cur.execute(query,value) 
                row=cur.fetchone()  
                # print(row)        it will print all the data for particular admin becoz he have forgot their password.  
                if row==None:
                     messagebox.showerror("My Error","Please enter the valid username")
                else:
                     con.close()
                     self.root2=Toplevel()
                     self.root2.title("Forgot Password")
                     self.root2.geometry("340x450+520+170")

                     l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),bg="white",fg="red")
                     l.place(x=0,y=10,relwidth=1)

                     #==========Select Security question===========#
#        #======================#
                     SecurityQues=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="Black")
                     SecurityQues.place(x=50,y=80)

                #=======combo box==========#
                     self.combo_SQ=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state='readonly')         #state readonly means user can't write
                     self.combo_SQ['values']=("Select","Your Birth Place","Your Favourite Flower","Your Favourite Colour")
                     self.combo_SQ.place(x=50,y=110,width=250)
                     self.combo_SQ.current(0)



        #==========Security Answer============#
                     SecurityAns=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                     SecurityAns.place(x=50,y=150)
        #=======entry==========#
                     self.txt_SecurityAns_entry=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                     self.txt_SecurityAns_entry.place(x=50,y=180,width=250) 

                     
                      #==========Security Answer============#
                     NewPass=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                     NewPass.place(x=50,y=220)
        #=======entry==========#
                     self.txt_NewPass_entry=ttk.Entry(self.root2,show='*',font=("times new roman",15,"bold"))
                     self.txt_NewPass_entry.place(x=50,y=250,width=250) 


                     btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),bg="dark green",fg="white")
                     btn.place(x=150,y=290)
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

#==========Variables==========#
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_chkbtn=IntVar()

 #=========background=========#
       

        bgimg = Image.open("C:\\Users\\BAGRI\\Desktop\\face_Recognition system\\college_image\\nature.jpg")
        bgimg = bgimg.resize((1354,710),Image.ANTIALIAS)
        self.photobgimg = ImageTk.PhotoImage(bgimg)

        bg_img = Label(self.root,image= self.photobgimg)
        bg_img.place(x=0,y=0,width=1354,height=710)

#===========left image==============#

        bgimg_left = Image.open("C:\\Users\\BAGRI\\Desktop\\face_Recognition system\\college_image\\code.jpg")
        bgimg_left = bgimg_left.resize((1354,710),Image.ANTIALIAS)
        self.photobgimg_left = ImageTk.PhotoImage(bgimg_left)

        bg_imgleft = Label(self.root,image= self.photobgimg_left)
        bg_imgleft.place(x=50,y=100,width=470,height=550)

#==========White Main FRAME=============#
        
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=700,height=550)

#========label register here=====#
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="dark green",bg="white")
        register_lbl.place(x=20,y=20)

#============labels and entry fields========#
     #=========first name=========#
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)
#=======entry==========#
        self.txt_fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.txt_fname_entry.place(x=50,y=130,width=250)
    
    #===========Last name======#
        Lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        Lname.place(x=350,y=100)
#=======entry==========#
        self.txt_Lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_Lname_entry.place(x=350,y=130,width=250)


        #===========Contact ======#
        Contact=Label(frame,text="Contact No.",font=("times new roman",15,"bold"),bg="white")
        Contact.place(x=50,y=170)
#=======entry==========#
        self.txt_Contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_Contact_entry.place(x=50,y=200,width=250)

#==========Email============#
        Email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white")
        Email.place(x=350,y=170)
#=======entry==========#
        self.txt_Email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_Email_entry.place(x=350,y=200,width=250)


#==========Select Security question===========#
#        #======================#
        SecurityQues=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="Black")
        SecurityQues.place(x=50,y=240)

        #=======combo box==========#
        self.combo_SQ=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state='readonly')         #state readonly means user can't write
        self.combo_SQ['values']=("Select","Your Birth Place","Your Favourite Flower","Your Favourite Colour")
        self.combo_SQ.place(x=50,y=270,width=250)
        self.combo_SQ.current(0)



 #==========Security Answer============#
        SecurityAns=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        SecurityAns.place(x=350,y=240)
#=======entry==========#
        self.txt_SecurityAns_entry=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.txt_SecurityAns_entry.place(x=350,y=270,width=250) 


#==========Password============#
        Pass=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        Pass.place(x=50,y=310)
#=======entry==========#
        self.txt_Pass_entry=ttk.Entry(frame,show='*',textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_Pass_entry.place(x=50,y=340,width=250) 


#==========Confirm Password============#
        ConfirmPass=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white")
        ConfirmPass.place(x=350,y=310)
#=======entry==========#
        self.txt_ConfirmPass_entry=ttk.Entry(frame,show='*',textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.txt_ConfirmPass_entry.place(x=350,y=340,width=250) 
   
#================checkbutton==============#
        checkbtn = Checkbutton(frame,variable=self.var_chkbtn,text="I Agree the Terms and Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

#===========Button===============#
        Btnimg_left=Image.open("C:\\Users\\BAGRI\\Desktop\\face_Recognition system\\college_image\\registernow.png")
        Btnimg_left= Btnimg_left.resize((200,50),Image.ANTIALIAS)
        self.photoBtnimg_left = ImageTk.PhotoImage(Btnimg_left)

        b1=Button(frame,image=self.photoBtnimg_left,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),bg="white",activebackground="white")

        
        b1.place(x=10,y=420,width=200)

#===========Login Button===============#
        Btnimg_right=Image.open("C:\\Users\\BAGRI\\Desktop\\face_Recognition system\\college_image\\login.jpg")
        Btnimg_right= Btnimg_right.resize((200,50),Image.ANTIALIAS)
        self.photoBtnimg_right = ImageTk.PhotoImage(Btnimg_right)

        b2=Button(frame,command=self.return_login,image=self.photoBtnimg_right,borderwidth=0,cursor="hand2",font=("times new roman",12,"bold"),bg="white",activebackground="white")

        
        b2.place(x=370,y=420,width=200)

#==============fUNCTION DECLARATION=============#
    def register_data(self):
           if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
                messagebox.showerror("Error","All fields are required",parent=self.root)
           elif self.var_pass.get()!=self.var_confpass.get():
                messagebox.showerror("Error","Password & Confirm Password must be same.",parent=self.root)
           elif self.var_chkbtn.get()==0:
                messagebox.showerror("Error","Please agree our terms and conditions.",parent=self.root)
           else:
                con=pymysql.connect(host="localhost",user="root",password="",database="stm")
                cur=con.cursor()    #from this we add data to mysql
                query=("select * from register where email=%s")
                value=(self.var_email.get(),)
                cur.execute(query,value)
                row=cur.fetchone()
                if row!=None:
                     messagebox.showerror("Error","User already Exist,Please try another email",parent=self.root)
                else:
                     cur.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                        self.var_fname.get(),
                                        self.var_lname.get(),
                                        self.var_contact.get(),
                                        self.var_email.get(),
                                        self.var_securityQ.get(),
                                        self.var_securityA.get(),
                                        self.var_pass.get()

                                          ))
                con.commit()
                con.close()
                messagebox.showinfo("Success","Register Successfully.",parent=self.root)
                
                
                
    def return_login(self):
            self.root.destroy()
    
class Student:
    def __init__(self,root):    # constructer initailize
        self.root = root           #initializing root
        self.root.title("Student Management System")     # Title of our window
        self.root.geometry("1350x700+0+0")      # boundary size

        title = Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="blue",fg="black")       # bg=background colour , fg= forground colour (text colour), relief means border style
        title.pack(side=TOP,fill=X)   #fill=x means full top fill with label 

        #===============All Variables=============#
        self.Roll_No_var=StringVar()    # IntVar we always use only for operational variable purpose
        self.name_var=StringVar() 
        self.email_var=StringVar() 
        self.gender_var=StringVar() 
        self.contact_var=StringVar() 
        self.dob_var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()

        

#======================Manage Frame========================#
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="dark blue")
        Manage_Frame.place(x=20,y=100,width=450,height=598)
  
        #===========label manage student========#
        m_title=Label(Manage_Frame,text="Manage Students",bg="dark blue",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)
        
        #==========label rollno==============#
        lbl_roll=Label(Manage_Frame,text="Roll No.",bg="dark blue",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,padx=20,pady=10,sticky="w")
         
        #========textbox for rollno===========#
        txt_Roll=Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")


      
        
        #==========label name==============#
        lbl_name=Label(Manage_Frame,text="Name",bg="dark blue",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,padx=20,pady=10,sticky="w")
         
        #========textbox for name===========#
        txt_Name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        
        
        #==========label email==============#
        lbl_email=Label(Manage_Frame,text="Email",bg="dark blue",fg="white",font=("times new roman",20,"bold"))
        lbl_email.grid(row=3,column=0,padx=20,pady=10,sticky="w")
         
        #========textbox for email===========#
        txt_Email=Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=3,column=1,pady=10,padx=20,sticky="w")
        


        #==========label gender==============#
        lbl_gender=Label(Manage_Frame,text="Gender",bg="dark blue",fg="white",font=("times new roman",20,"bold"))
        lbl_gender.grid(row=4,column=0,padx=20,pady=10,sticky="w")
         
        #==========combobox for gender========#
        combo_Gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",13,"bold"),state='readonly')         #state readonly means user can't write
        combo_Gender['values']=("Select","Male","Female","Other")
        combo_Gender.grid(row=4,column=1,padx=20,pady=10)
        combo_Gender.current(0)

        
        
        #==========label contact==============#
        lbl_contact=Label(Manage_Frame,text="Contact",bg="dark blue",fg="white",font=("times new roman",20,"bold"))
        lbl_contact.grid(row=5,column=0,padx=20,pady=10,sticky="w")
         
        #========textbox for contact===========#
        txt_Contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        
        #==========label D.O.B==============#
        lbl_dob=Label(Manage_Frame,text="D.O.B.",bg="dark blue",fg="white",font=("times new roman",20,"bold"))
        lbl_dob.grid(row=6,column=0,padx=20,pady=10,sticky="w")
         
        #========textbox for D.O.B===========#
        txt_DOB=Entry(Manage_Frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_DOB.grid(row=6,column=1,pady=10,padx=20,sticky="w")

         
        
        #==========label Address==============#
        lbl_address=Label(Manage_Frame,text="Address",bg="dark blue",fg="white",font=("times new roman",20,"bold"))
        lbl_address.grid(row=7,column=0,padx=20,pady=10,sticky="w")
         
        # #========textbox for Address===========#
        self.txt_Address=Text(Manage_Frame,width=25,bd=4,height=4)
        self.txt_Address.grid(row=7,column=1,pady=10,padx=20,sticky="w")


        #==================button Frame==============#
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="dark blue")
        btn_Frame.place(x=10,y=525,width=425)

        #==============buttons: Add , Update , Delete , Clear ===========#
        Addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_students).grid(row=0,column=1,padx=10,pady=10)
        Updatebtn=Button(btn_Frame,text="Update",width=10,command=self.update_data).grid(row=0,column=2,padx=10,pady=10)
        Deletebtn=Button(btn_Frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=3,padx=10,pady=10)
        Clearbtn=Button(btn_Frame,text="Clear",width=10,command=self.clear).grid(row=0,column=4,padx=10,pady=10)


#======================Detail Frame========================#
 
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="dark blue")
        Detail_Frame.place(x=500,y=100,width=820,height=598)

        lbl_search=Label(Detail_Frame,text="Search By:",bg="dark blue",fg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        #==========combobox for Search========#
        combo_Search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')         #state readonly means user can't write
        combo_Search['values']=("Select","Roll_no","Name","Contact")
        combo_Search.grid(row=0,column=1,padx=20,pady=10)
        combo_Search.current(0)

        #========textbox for Search===========#
        txt_Search=Entry(Detail_Frame,textvariable=self.search_txt,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn=Button(Detail_Frame,text="Search",width=10,pady=5,command=self.Search_data).grid(row=0,column=3,padx=10,pady=10)
        Showallbtn=Button(Detail_Frame,text="Show All",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)


#==============table Frame====================#
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="dark blue")
        Table_Frame.place(x=10,y=70,width=790,height=510)

        #==================scrollbar X And Y =================#
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll",text="Roll No.")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("dob",text="D.O.B")
        self.Student_table.heading("address",text="Address")
        self.Student_table['show']='headings'
        self.Student_table.column("roll",width=100)
        self.Student_table.column("name",width=100)
        self.Student_table.column("email",width=100)
        self.Student_table.column("gender",width=100)
        self.Student_table.column("contact",width=100)
        self.Student_table.column("dob",width=100)
        self.Student_table.column("address",width=150)


        self.Student_table.pack(fill=BOTH,expand=1)      # fill= Both means do white in full frame and expand for truly done the functionality
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_students(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","All Fields are required!!!",parent=self.root)
        
        else:

            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                         self.name_var.get(),
                                                                         self.email_var.get(),
                                                                         self.gender_var.get(),
                                                                         self.contact_var.get(),
                                                                         self.dob_var.get(),
                                                                         self.txt_Address.get('1.0',END) #1.0 means line no and end tak data ko get krle
                                                                         ))
        
    
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Success","Record has been inserted.",parent=self.root)
    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if (rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children()) #delete the child element of that row
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()
    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_Address.delete("1.0",END)

    def get_cursor(self,ev):     #ev means Event
        curosor_row=self.Student_table.focus()
        contents=self.Student_table.item(curosor_row)
        row=contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_Address.delete("1.0",END)
        self.txt_Address.insert(END,row[6])

    def update_data(self): 
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
                                                                         self.name_var.get(),
                                                                         self.email_var.get(),
                                                                         self.gender_var.get(),
                                                                         self.contact_var.get(),
                                                                         self.dob_var.get(),
                                                                         self.txt_Address.get('1.0',END), #1.0 means line no and end tak data ko get krle
                                                                         self.Roll_No_var.get()
                                                                         ))
        
    
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()   

    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("delete from students where roll_no=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()


    def Search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()

        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children()) #delete the child element of that row
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()






if __name__ == "__main__":
      main()