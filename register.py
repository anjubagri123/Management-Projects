from tkinter import *
from tkinter import ttk        #provide combobox
from PIL import Image,ImageTk  
from tkinter import messagebox
import pymysql
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
       

        bgimg = Image.open("C:\\Users\\BAGRI\\Desktop\\face_Recognition system\\college_image\\state.jpg")
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

        b2=Button(frame,image=self.photoBtnimg_right,borderwidth=0,cursor="hand2",font=("times new roman",12,"bold"),bg="white",activebackground="white")

        
        b2.place(x=370,y=420,width=200)

#==============fUNCTION DECLARATION=============#
    def register_data(self):
           if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
                messagebox.showerror("Error","All fields are required")
           elif self.var_pass.get()!=self.var_confpass.get():
                messagebox.showerror("Error","Password & Confirm Password must be same.")
           elif self.var_chkbtn.get()==0:
                messagebox.showerror("Error","Please agree our terms and conditions.")
           else:
                con=pymysql.connect(host="localhost",user="root",password="",database="stm")
                cur=con.cursor()    #from this we add data to mysql
                query=("select * from register where email=%s")
                value=(self.var_email.get(),)
                cur.execute(query,value)
                row=cur.fetchone()
                if row!=None:
                     messagebox.showerror("Error","User already Exist,Please try another email")
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
                messagebox.showinfo("Success","Register Successfully.")
            
    
         



if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()