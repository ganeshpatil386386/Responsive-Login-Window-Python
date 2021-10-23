from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox


def subm():
    if root.name.get()=="" :
        messagebox.showerror("Error","Name Required")
    elif root.fname.get()=="":
            messagebox.showerror("Error","Father must be Required")
    elif root.eno.get()=="":
            messagebox.showerror("Error","Enrollment must be Required")
    elif root.brn.get()=="":
            messagebox.showerror("Error","Branch must be Required")
    elif root.prs.get()=="":
            messagebox.showerror("Error","Percentage of SSC must be Required")
    elif root.prh.get()=="":
            messagebox.showerror("Error","Percentage of HSC must be Required")
    elif root.yrs.get()=="":
            messagebox.showerror("Error","Year f SSC Passed must be Required")
    elif root.yrh.get()=="":
            messagebox.showerror("Error","Year f HSC Passed must be Required")
    elif root.ntnl.get()=="":
            messagebox.showerror("Error","Nationality must be Required")
    elif root.gen.get()=="":
            messagebox.showerror("Error","Gender must be Required")
    elif root.st.get()=="":
            messagebox.showerror("Error","State must be Required")
    elif root.eml.get()=="":
            messagebox.showerror("Error","Email must be Required")
    elif root.mob.get()=="":
            messagebox.showerror("Error","Mobile must be Required")
    elif root.sc.get()=="":
            messagebox.showerror("Error","School must be Required")
    elif root.ht.get()=="":
            messagebox.showerror("Error","Hostel Type must be Required")
    elif root.add.get()=="":
            messagebox.showerror("Error","Address must be Required")
    else:
        f=open("files/"+str(root.name.get())+".txt","w")
        f.write(
                    str("Name:" +root.name.get())+"  \n"+
                    str("ather Name:"+root.fname.get())+"\n"+
                    str("Enrollment No:"+root.eno.get())+"\n"+
                    str("Branch"+root.brn.get())+"\n"+
                    str("Percentage of 10th:"+root.prs.get())+"\n"+
                    str("Percentage of 12th:"+root.prh.get())+"\n"+
                    str("Year passing of 10th:"+root.yrs.get())+"\n"+
                    str("Year passing of 12th:"+root.yrh.get())+"\n"+
                    str("Nationality:"+root.ntnl.get())+"\n"+
                    str("Gender:"+root.gen.get())+"\n"+
                    str("State:"+root.st.get())+"\n"+
                    str("Email:"+root.eml.get())+"\n"+
                    str("Mobile"+root.mob.get())+"\n"+
                    str("School"+root.sc.get())+"\n"+
                    str("Hostel"+root.ht.get())+"\n"+
                    str("Address"+root.add.get())
                )

        f.close()
        messagebox.showinfo("Success","Record has benn Saved successsfully..!!!")

def clr():
    
     root.name.set("")
     root.fname.set("")
     root.eno.set("")
     root.brn.set("")
     root.prs.set("")
     root.prh.set("")
     root.yrs.set("")
     root.yrh.set("")
     root.ntnl.set("")
     root.gen.set("")
     root.st.set("")
     root.eml.set("")
     root.mob.set("")
     root.sc.set("")
     root.ht.set("")
     root.add.set("")
     
def pay():
    messagebox.showinfo("Success","Payment Accepted")
    

    


    

    

def nw():
    
    book=Tk()
    book.geometry("600x600")
    

    book.title("Payment Management")
    
    lh=Label(book,text="Payment Management ",font=("Cambria",20,"bold"),bg="#F9D342")
    lh.place(x=10,y=10,w=580,h=50)
    
    
    
    l1=Label(book,text="Department",font=("Cambria",12,"bold"),fg="Black")
    l1.place(x=50,y=120)
    t1=Entry(book)
    t1.place(x=180,y=120,w=190,h=22)

    l1=Label(book,text="Enrollment",font=("Cambria",12,"bold"),fg="Black")
    l1.place(x=50,y=160)
    t2=Entry(book)
    t2.place(x=180,y=160,w=190,h=22)

   
       
            
    



           
    
    
    

   
    
    root.nm=StringVar()
    root.mb=StringVar()
    root.br=StringVar()
    root.pr=StringVar()
    root.ad=StringVar()
    root.pt=StringVar()
    

    

    NL=Label(book,text="Name",font=("cambria",12,"bold"),fg="Black").place(x=30,y=260,h=30,w=210)
    e1=Entry(book,relief=GROOVE,textvariable=root.nm).place(x=270,y=260,h=25,w=210)

    ML=Label(book,text="Mobile",font=("cambria",12,"bold"),fg="Black").place(x=30,y=310,h=30,w=210)
    e2=Entry(book,relief=GROOVE,textvariable=root.mb).place(x=270,y=310,h=25,w=210)
    
    BL=Label(book,text="Branch",font=("cambria",12,"bold"),fg="Black").place(x=30,y=360,h=30,w=210)
    e3=Entry(book,relief=GROOVE,textvariable=root.br).place(x=270,y=360,h=25,w=210)
    
    PL=Label(book,text="Percentage",font=("cambria",12,"bold"),fg="Black").place(x=30,y=410,h=30,w=210)
    e4=Entry(book,w=32,relief=GROOVE,textvariable=root.pr).place(x=270,y=410,h=25,w=210)

    AL=Label(book,text="Address",font=("cambria",12,"bold"),fg="Black").place(x=30,y=460,h=30,w=210)
    e5=Entry(book,w=32,relief=GROOVE,textvariable=root.ad).place(x=270,y=460,h=25,w=210)

    CL=Label(book,text="Fees",font=("cambria",12,"bold"),fg="Black").place(x=30,y=510,h=30,w=210)
    e6=Entry(book,w=32,relief=GROOVE,textvariable=root.pt).place(x=270,y=510,h=25,w=210)

    bs=Button(book,text="Pay-Fees",command=pay,font=("Cambria",13,"bold"),bg="#F9D342")
    bs.place(x=100,y=560,w=120,h=30)
    
    bc=Button(book,text="Cancel",font=("Cambria",13,"bold"),bg="#F9D342")
    bc.place(x=290,y=560,w=120,h=30)
    

    
    book.resizable(0,0)
    book.configure(bg="#292826")
    book.mainloop()

    
    
def net():
    root.destroy()
    
    

    top=Tk()
    
    top.title("Student Management System")
   
    top.geometry("800x600")


    root.name=StringVar()
    root.fname=StringVar()
    root.eno=StringVar()
    root.brn=StringVar()
    root.prs=StringVar()
    root.prh=StringVar()
    root.yrs=StringVar()
    root.yrh=StringVar()
    root.ntnl=StringVar()
    root.gen=StringVar()
    root.st=StringVar()
    root.eml=StringVar()
    root.mob=StringVar()
    root.sc=StringVar()
    root.ht=StringVar()
    root.add=StringVar()   

    

    lh=Label(top,text="Student Management System",font=("Cambria",20,"bold"),bg="#98FB98")
    lh.place(x=10,y=10,w=780,h=50)

    la=Label(top,bg="#00FFFF")
    la.place(x=10,y=70,w=780,h=520)

    l1=Label(la,text="Name of Student",font=("Cambria",12,"bold"))
    l1.place(x=10,y=10)
    e1=Entry(top,textvariable=root.name)
    e1.place(x=180,y=80,w=190,h=22)
    
    l2=Label(la,text="Name of Father",font=("Cambria",12,"bold"))
    l2.place(x=10,y=50)
    e2=Entry(top,textvariable=root.fname)
    e2.place(x=180,y=120,w=190,h=22)
    
    l3=Label(la,text="Enrollment No",font=("Cambria",12,"bold"))
    l3.place(x=10,y=90)
    e3=Entry(top,textvariable=root.eno)
    e3.place(x=180,y=160,w=190,h=22)
    
    l4=Label(la,text="Branch",font=("Cambria",12,"bold"))
    l4.place(x=10,y=130)
    combo=ttk.Combobox(top,width=20,state="readonly",textvariable=root.brn)
    combo['values']=("CSE","Mechanical","Civil","Electrical")
    combo.place(x=180,y=200,w=190,h=22)
    
    l5=Label(la,text="Percentage of 10",font=("Cambria",12,"bold"))
    l5.place(x=10,y=170)
    e5=Entry(top,textvariable=root.prs)
    e5.place(x=180,y=240,w=190,h=22)
    
    l6=Label(la,text="Percentage of 12",font=("Cambria",12,"bold"))
    l6.place(x=10,y=210)
    e6=Entry(top,textvariable=root.prh)
    e6.place(x=180,y=280,w=190,h=22)
    
    l7=Label(la,text="Year of 1o pass",font=("Cambria",12,"bold"))
    l7.place(x=10,y=250)
    e7=Entry(top,textvariable=root.yrs)
    e7.place(x=180,y=320,w=190,h=22)
    
    l8=Label(la,text="Year of 12 pass",font=("Cambria",12,"bold"))
    l8.place(x=10,y=290)
    e8=Entry(top,textvariable=root.yrh)
    e8.place(x=180,y=360,w=190,h=22)
    
    l9=Label(la,text="Nationality",font=("Cambria",12,"bold"))
    l9.place(x=10,y=330)
    combo=ttk.Combobox(top,width=20,state="readonly",textvariable=root.ntnl)
    combo['values']=("Indian")
    combo.place(x=180,y=400,w=190,h=22)
    
    l10=Label(la,text="Gender",font=("Cambria",12,"bold"))
    l10.place(x=10,y=370)
    combo=ttk.Combobox(top,width=20,state="readonly",textvariable=root.gen)
    combo['values']=("Male","Female","Other")
    combo.place(x=180,y=440,w=190,h=22)
    
    l11=Label(la,text="State",font=("Cambria",12,"bold"))
    l11.place(x=390,y=10)
    combo=ttk.Combobox(top,width=20,state="readonly",textvariable=root.st)
    combo['values']=("Delhi","Utter Pradesh","Rajasthan","Goa","Maharashtra","Gujrat")
    combo.place(x=490,y=80,w=210,h=22)

    l12=Label(la,text="Email ID",font=("Cambria",12,"bold"))
    l12.place(x=390,y=50)
    e12=Entry(top,textvariable=root.eml)
    e12.place(x=490,y=120,w=190,h=22)

    l13=Label(la,text="Mobile",font=("Cambria",12,"bold"))
    l13.place(x=390,y=90)
    e13=Entry(top,textvariable=root.mob)
    e13.place(x=490,y=160,w=190,h=22)

    l14=Label(la,text="School ",font=("Cambria",12,"bold"))
    l14.place(x=390,y=130)
    e14=Entry(top,textvariable=root.sc)
    e14.place(x=490,y=200,w=190,h=22)

    l15=Label(la,text="Hostel",font=("Cambria",12,"bold"))
    l15.place(x=390,y=170)
    e15=Entry(top,textvariable=root.ht)
    e15.place(x=490,y=240,w=190,h=22)

    l16=Label(la,text="Address",font=("Cambria",12,"bold"))
    l16.place(x=390,y=210)
    e16=Entry(top,textvariable=root.add)
    e16.place(x=470,y=320,w=240,h=120)
    

                        
    b1=Button(top,text="Submit",font=("Cambria",15,"bold"),command=subm)
    b1.place(x=30,y=530,w=130,h=35)

   

    b2=Button(top,text="Clear",font=("Cambria",15,"bold"),command=clr)
    b2.place(x=200,y=530,w=130,h=35)
    
    b3=Button(top,text="Logout",font=("Cambria",15,"bold"))
    b3.place(x=390,y=530,w=130,h=35)
    b4=Button(top,text="Pay-Fees",font=("Cambria",15,"bold"),command=nw)
    b4.place(x=560,y=530,w=130,h=35)


           

   
    
    






































    
    
  


    #top.configure(bg="#00FA9A")
    top.resizable(0,0)
    top.mainloop()

      


def log():
    user=StringVar()
    pssd=StringVar()
    user = ule.get()
    pssd = ulp.get()
    
    
    if user=="" or pssd=="":
        net()
    elif user=="a" and pssd=="b":
        messagebox.showerror("Error","username and password Ruquired")
        
    else:
        messagebox.showerror("Error","Incorrect username or password")   
        

    
root=Tk()
root.title("New Versioon")
root.geometry("700x400")
root.configure(bg="#FFB1C6")


lb=Label(root,text="Login",font=("Cambria",20,"bold"),bg="#98FB98")
lb.place(x=0,y=0,w=700)



ul=Label(root,text="Username",font=("Cambria",13,"bold"),bg="orange")
ul.place(x=160,y=100)
ule=Entry(root)
ule.place(x=290,y=100,w=190,h=24)


pl=Label(root,text="Password",font=("Cambria",13,"bold"),bg="orange")
pl.place(x=160,y=160)
ulp=Entry(root,show="*")
ulp.place(x=290,y=160,w=190,h=24)

img = ImageTk.PhotoImage(file="login.jpg")
logo = Label(root, image=img)
logo.place(x=510,y=70,h=150,w=150)


b1=Button(root,text="Login",font=("Cambria",13,"bold"),bg="#FF4500",relief=GROOVE,command=log)
b1.place(x=150,y=270,w=150,h=32)

b2=Button(root,text="Register",font=("Cambria",13,"bold"),bg="#FFA70A",relief=GROOVE)
b2.place(x=360,y=270,w=150,h=32)
b2=Button(root,text="Forgot passwd",font=("Cambria",13,"bold"),bg="#98FB98",relief=GROOVE)
b2.place(x=250,y=320,w=150,h=32)
#lx=Label(lb,text="Login",font=("Cambria",18,"bold"))
#lb.place(x=250,y=10)

root.resizable(0,0)
root.mainloop()
