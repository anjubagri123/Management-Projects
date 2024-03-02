import datetime as dt
from tkinter import *
from tkinter import ttk        #provide combobox
import pymysql
import time
from tkinter import messagebox
class Student:
    def __init__(self,root):    # constructer initailize
        self.root = root           #initializing root
        self.root.title("Student Management System")     # Title of our window
        self.root.geometry("1350x700+0+0")      # boundary size

        # title = Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="blue",fg="black")       # bg=background colour , fg= forground colour (text colour), relief means border style
        # title.pack(side=TOP,fill=X)   #fill=x means full top fill with label 


#==========Timing System==============
 #=============CLOCK==============#
        T_frame = Frame(self.root, bd=10, relief=RIDGE, bg="dark blue")
        T_frame.place(x=0, y=0, width=1349, height=100)
        I_lb1 = Label(T_frame, text=f"{dt.datetime.now():%a, %b %d %Y}", fg="white",bg="dark blue",font=("times new roman", 15, "bold"),
                       bd=0).place(x=10, y=7)

        def clock():
            G_time = time.strftime("%H:%M:%S")
            clock_lb3.config(text=G_time)
            clock_lb3.after(1000, clock)

        clock_lb3 = Label(T_frame, font=("times new roman", 17, "bold"), fg='white',bg="dark blue", bd=0)
        clock_lb3.place(x=1200, y=7)
        clock()
        # ..............................................................................................................................................
        I_lb2 = Label(T_frame, text="Student Management System", font=("times new roman", 40, "bold"), bg='dark blue',
                      fg='white', bd=0).place(x=315, y=4)
        #=========end top time frame===============#
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
            messagebox.showerror("Error","All Fields are required!!!")
        
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
        messagebox.showinfo("Success","Record has been inserted.")
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
        root = Tk()
        ob = Student(root)      #object creation
        root.mainloop()
