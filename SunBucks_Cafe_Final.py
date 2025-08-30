from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import BOLD,ITALIC
import PIL.ImageTk as imtk
import PIL.Image as i
import mysql.connector
import smtplib
from prettytable import PrettyTable



## To create a database to save customer info
DB=mysql.connector.connect(host="localhost",user="root",passwd="")
SQLcursor=DB.cursor()

SQLcursor.execute("CREATE DATABASE if not exists Sunbucks_Cafe;")
SQLcursor.execute("USE Sunbucks_Cafe;")
SQLcursor.execute("CREATE TABLE if not exists login (Name varchar(50) not null,Mail_id varchar(60) not null);")

SQLcursor.execute("USE Sunbucks_Cafe;")
SQLcursor.execute("CREATE TABLE if not exists Bill (Item varchar(40) not null,Price int not null,Quantity int not null);")



## Opening & Welcoming Page
win=Tk()
win.title("SunBucks Cafe")
win.attributes("-fullscreen",True)
win.configure(background="black")


## Background Image 
bgimg=imtk.PhotoImage(file="0001.png")
label1=Label(win,image=bgimg)
label1.place(x=0,y=0)


## Welcome message
system_name_label=Label(win,text=" Welcome to SunBucks Cafe !!!",font=("Calibri",40,BOLD),bg="#800000")
system_name_label.place(x=440,y=90)


## Quote for welcoming page
wq=Label(win,text=" \"Charge your Brain and Heart with a strong coffee !!! \" ",font=("Bookman Old Style",25,ITALIC),bg="#0000ff" )
wq.place(x=320,y=600)


## To add SunBucks Logo to welcoming page
image=i.open("Logo.png")
img=image.resize((300,300))
mimg=imtk.PhotoImage(img)
imglabel=Label(win,image=mimg)
imglabel.place(x=600,y=200)



## For Loading comment
def fetching_application_status():
    loading=Label(win,text="Loading....",font=("Calibri",20))
    loading.place(x=1080,y=670)
    win.after(2000,loading.place_forget)

fetching_application_status()



## Login Page
def log():
     
    ## For Background Image
    global filename_img
    filename_img = PhotoImage(file="0002.png")
    background_label = Label(win, image=filename_img)
    background_label.place(x=0,y=0)

    ## Instruction for Entering Mail-ID
    messagebox.showinfo("Instrucation.....","Please enter FULL VALID Mail-id. \nEnter mail like eg:examplemail123@gmail.com")

    lm=Label(win,text=" Login to continue.....",font=("Times New Roman",35,ITALIC),bg="#0000CD")
    lm.place(x=550,y=90)

    ## For Getting Name as Input
    Name=Label(win,text="Name:",font=("Calibri",25,BOLD),bg="#7DFDFE")
    Name.place(x=500,y=220)    
    Name_entry=Entry(win,width=15,font=("Calibri",25,BOLD))
    Name_entry.place(x=650,y=220)

    ## For Getting Mail-ID as Input
    Mail=Label(win,text="Mail:",font=("Calibri",25,BOLD),bg="#7DFEFE")
    Mail.place(x=520,y=320)
    Mail_entry=Entry(win,width=25,font=("Calibri",25,BOLD))
    Mail_entry.place(x=650,y=320)

    ## For Uploading the data into SQL table
    def log_upload():
        sql="INSERT INTO login VALUES('{}','{}')".format((Name_entry.get()),(Mail_entry.get()))
        SQLcursor.execute(sql)
    

    def nb():
        log_upload()
        sd.place_forget()

        ## To remove all the contents of the second page
        def forget2():
            lm.place_forget()
            Name.place_forget()
            Name_entry.place_forget()
            Mail.place_forget()
            Mail_entry.place_forget()
            submit.place_forget()
        
        def mb():
            forget2()
                
            messagebox.showinfo("Success","Details are Saved.")      ##To display message


            #For Background of menu page
            global BG
            BG=PhotoImage(file="0003.png")
            BL= Label(win, image=BG)
            BL.place(x=0,y=0)

            h=Label(win,text="Main Menu",font=("Copperplate Gothic",55,BOLD,ITALIC),bg="#5499c7")
            h.place(x=520,y=0)
            z=Label(win,text="Life is like a coffee Bean,",font=("Consolas",30,BOLD,ITALIC),bg="#5d6d7e")
            z.place(x=445,y=350)
            z1=Label(win,text="Grind it Hard !!!,",font=("Consolas",30,BOLD,ITALIC),bg="#5d6d7e")
            z1.place(x=505,y=400)
            
            

            def forget3():
                coffee.place_forget()
                cm.place_forget()
                snacks.place_forget()
                sm.place_forget()
                merchandise.place_forget()
                mm.place_forget()
                bestseller.place_forget()
                bm.place_forget()

                

            ##For Coffee Page
            def co():
                forget3()
                

                ## For Background Image
                global cobg
                cobg=PhotoImage(file="0004.png")
                cb=Label(win,image=cobg)
                cb.place(x=0,y=0)

                messagebox.showinfo("Loading","Loading..., Please wait till system checks for available items!!!!")

                #Cold Brew Black
                global a
                a=PhotoImage(file="9.png")
                al= Label(win, image=a)
                al.place(x=0,y=0)
                
                am=Label(win,text="Cold Brew Black",font=("Congenial",20,BOLD),bg="#aeb6b7")
                am.place(x=0,y=175)
                s=Label(win,text="₹",font=("Congenial",15,BOLD),bg="#aeb6b7")
                s.place(x=20,y=215)
                ap=Label(win,text="120",font=("Congenial",15,BOLD),bg="#aeb6b7")
                ap.place(x=37,y=215)

                
                aqty=Label(win,text="Qty:",font=("Congenial",15),bg="#c0a98e")
                aqty.place(x=20,y=255)
                aqb=ttk.Combobox(win,width=10,font=("Congenial",15),values=("0","1","2","3","4","5","6","7","8")) ## For getting quantity
                aqb.current(0)
                aqb.place(x=70,y=255)

                global abil
                def abil():
                    sql="INSERT INTO bill VALUES('{}',{},{})".format(am.cget("text"),ap.cget("text"),aqb.get())
                    SQLcursor.execute(sql)
                



                #Caramel Latte
                global b
                b=PhotoImage(file="10.png")
                bl= Label(win, image=b)
                bl.place(x=434,y=0)
                bm=Label(win,text="Caramel Latte",font=("Congenial",20,BOLD),bg="#aeb6b7")
                bm.place(x=434,y=175)
                s=Label(win,text="₹",font=("Congenial",15,BOLD),bg="#aeb6b7")
                s.place(x=454,y=215)
                bp=Label(win,text="150",font=("Congenial",15,BOLD),bg="#aeb6b7")
                bp.place(x=471,y=215)

            
                bqty=Label(win,text="Qty:",font=("Congenial",15),bg="#c0a98e")
                bqty.place(x=474,y=255) 
                bqb=ttk.Combobox(win,width=10,font=("Congenial",15),values=("0","1","2","3","4","5","6","7","8"))   ## For getting quantity
                bqb.current(0)
                bqb.place(x=524,y=255)

                global bbil
                def bbil():
                    sql="INSERT INTO bill VALUES('{}',{},{})".format(bm.cget("text"),bp.cget("text"),bqb.get())
                    SQLcursor.execute(sql)
                    

                #Cappuccino
                global c
                c=PhotoImage(file="11.png")
                cl= Label(win, image=c)
                cl.place(x=868,y=0)
                cm=Label(win,text="Cappuccino",font=("Congenial",20,BOLD),bg="#aeb6b7")
                cm.place(x=868,y=175)
                s=Label(win,text="₹",font=("Congenial",15,BOLD),bg="#aeb6b7")
                s.place(x=888,y=215)
                cp=Label(win,text="135",font=("Congenial",15,BOLD),bg="#aeb6b7")
                cp.place(x=905,y=215)

                
                cqty=Label(win,text="Qty:",font=("Congenial",15),bg="#c0a98e")
                cqty.place(x=895,y=255)
                cqb=ttk.Combobox(win,width=10,font=("Congenial",15),values=("0","1","2","3","4","5","6","7","8"))   ## For getting quantity
                cqb.current(0)
                cqb.place(x=945,y=255)

                global cbil
                def cbil():
                    sql="INSERT INTO bill VALUES('{}',{},{})".format(cm.cget("text"),cp.cget("text"),cqb.get())
                    SQLcursor.execute(sql)
                    

                    
                

                #Espresso
                global d
                d=PhotoImage(file="12.png")
                dl= Label(win, image=d)
                dl.place(x=1300,y=0)
                dm=Label(win,text="Espresso",font=("Congenial",20,BOLD),bg="#aeb6b7")
                dm.place(x=1320,y=175)
                s=Label(win,text="₹",font=("Congenial",15,BOLD),bg="#aeb6b7")
                s.place(x=1340,y=215)
                dp=Label(win,text="145",font=("Congenial",15,BOLD),bg="#aeb6b7")
                dp.place(x=1357,y=215)

               
                dqty=Label(win,text="Qty:",font=("Congenial",15),bg="#c0a98e")
                dqty.place(x=1270,y=255)
                dqb=ttk.Combobox(win,width=10,font=("Congenial",15),values=("0","1","2","3","4","5","6","7","8"))    ## For getting quantity
                dqb.current(0)
                dqb.place(x=1320,y=255)

                global dbil
                def dbil():
                    sql="INSERT INTO bill VALUES('{}',{},{})".format(dm.cget("text"),dp.cget("text"),dqb.get())
                    SQLcursor.execute(sql)


                #Black coffee
                global e
                e=PhotoImage(file="13.png")
                el= Label(win, image=e)
                el.place(x=0,y=405)
                em=Label(win,text="Black Coffee",font=("Congenial",20,BOLD),bg="#aeb6b7")
                em.place(x=0,y=580)
                s=Label(win,text="₹",font=("Congenial",15,BOLD),bg="#aeb6b7")
                s.place(x=20,y=620)
                ep=Label(win,text="150",font=("Congenial",15,BOLD),bg="#aeb6b7")
                ep.place(x=37,y=620)

               
                eqty=Label(win,text="Qty:",font=("Congenial",15),bg="#c0a98e")
                eqty.place(x=20,y=660)
                eqb=ttk.Combobox(win,width=10,font=("Congenial",15),values=("0","1","2","3","4","5","6","7","8"))    ## For getting quantity
                eqb.current(0)
                eqb.place(x=70,y=660)

                global ebil
                def ebil():
                    sql="INSERT INTO bill VALUES('{}',{},{})".format(em.cget("text"),ep.cget("text"),eqb.get())
                    SQLcursor.execute(sql)


                #Dark chocolate mocha
                global f
                f=PhotoImage(file="14.png")
                fl= Label(win, image=f)
                fl.place(x=434,y=405)
                fm=Label(win,text="Chocolate Mocha",font=("Congenial",20,BOLD),bg="#aeb6b7")
                fm.place(x=434,y=580)
                s=Label(win,text="₹",font=("Congenial",15,BOLD),bg="#aeb6b7")
                s.place(x=454,y=620)
                fp=Label(win,text="160",font=("Congenial",15,BOLD),bg="#aeb6b7")
                fp.place(x=471,y=620)

                
                fqty=Label(win,text="Qty:",font=("Congenial",15),bg="#c0a98e")
                fqty.place(x=474,y=660)
                fqb=ttk.Combobox(win,width=10,font=("Congenial",15),values=("0","1","2","3","4","5","6","7","8"))    ## For getting quantity
                fqb.current(0)
                fqb.place(x=524,y=660)

                global fbil
                def fbil():
                    sql="INSERT INTO bill VALUES('{}',{},{})".format(fm.cget("text"),fp.cget("text"),fqb.get())
                    SQLcursor.execute(sql)


                #Iced coffee
                global g
                g=PhotoImage(file="15.png")
                gl= Label(win, image=g)
                gl.place(x=868,y=405)
                gm=Label(win,text="Iced Coffee",font=("Congenial",20,BOLD),bg="#aeb6b7")
                gm.place(x=868,y=580)
                s=Label(win,text="₹",font=("Congenial",15,BOLD),bg="#aeb6b7")
                s.place(x=888,y=620)
                gp=Label(win,text="125",font=("Congenial",15,BOLD),bg="#aeb6b7")
                gp.place(x=905,y=620)

                
                gqty=Label(win,text="Qty:",font=("Congenial",15),bg="#c0a98e")
                gqty.place(x=895,y=660)
                gqb=ttk.Combobox(win,width=10,font=("Congenial",15),values=("0","1","2","3","4","5","6","7","8"))    ## For getting quantity
                gqb.current(0)
                gqb.place(x=945,y=660)

                global gbil
                def gbil():
                    sql="INSERT INTO bill VALUES('{}',{},{})".format(gm.cget("text"),gp.cget("text"),gqb.get())
                    SQLcursor.execute(sql)
                    
                    


                #Flat White
                global h
                h=PhotoImage(file="16.png")
                hl= Label(win, image=h)
                hl.place(x=1300,y=405)
                hm=Label(win,text="Flat White",font=("Congenial",20,BOLD),bg="#aeb6b7")
                hm.place(x=1300,y=580)
                s=Label(win,text="₹",font=("Congenial",15,BOLD),bg="#aeb6b7")
                s.place(x=1320,y=620)
                hp=Label(win,text="150",font=("Congenial",15,BOLD),bg="#aeb6b7")
                hp.place(x=1337,y=620)

                
                hqty=Label(win,text="Qty:",font=("Congenial",15),bg="#c0a98e")
                hqty.place(x=1270,y=660)
                hqb=ttk.Combobox(win,width=10,font=("Congenial",15),values=("0","1","2","3","4","5","6","7","8"))   ## For getting quantity
                hqb.current(0)
                hqb.place(x=1320,y=660)

                global hbil
                def hbil():
                    sql="INSERT INTO bill VALUES('{}',{},{})".format(hm.cget("text"),hp.cget("text"),hqb.get())
                    SQLcursor.execute(sql)
                

                #For returning to main menu
                re=Button(win,text="Return to Main Menu",font=("Calibri",20,BOLD),bg="#ff2c2c",command=mb)
                re.place(x=605,y=0)



                ## To save details of orders made in Coffee Page
                def save7():
                    abil()
                    bbil()
                    cbil()
                    dbil()
                    ebil()
                    fbil()
                    gbil()
                    hbil()
                    messagebox.showinfo("Success","Your Order info have been saved!!!")
                save7=Button(win,text="Save Orders",font=("Calibri",35,BOLD,ITALIC),bg="#ff2c2c",command=save7)
                save7.place(x=600,y=300)
                


            #For Coffee Button
            global c
            c=PhotoImage(file="4.png")
            cl=Label(win,image=c)
            coffee=Button(win,image=c,command=co)
            coffee.place(x=20,y=20)
            cm=Label(win,text="Coffee",font=("Times New Roman",25,BOLD,ITALIC),bg="#223377")
            cm.place(x=100,y=325)


            ##For Snacks page
            def so():
                forget3()

                global BG3
                BG3=PhotoImage(file="0007.png")
                BL3= Label(win, image=BG3)
                BL3.place(x=0,y=0)

                messagebox.showinfo("Loading","Loading..., Please wait till system checks for available items!!!!")
                

                ##Chocolates
                global j
                j=PhotoImage(file="24.png")
                jl= Label(win, image=j)
                jl.place(x=0,y=0)
                jm=Label(win,text="Chocolates",font=("Congenial",20,BOLD),bg="#aeb6b7")
                jm.place(x=300,y=40)
                s=Label(win,text="₹",font=("Congenial",15,BOLD),bg="#aeb6b7")
                s.place(x=320,y=80)
                jp=Label(win,text="140",font=("Congenial",15,BOLD),bg="#aeb6b7")
                jp.place(x=337,y=80)

                
                jqty=Label(win,text="Qty:",font=("Congenial",15),bg="#c0a98e")
                jqty.place(x=300,y=120)
                jqb=ttk.Combobox(win,width=10,font=("Congenial",15),values=("0","1","2","3","4","5","6","7","8"))    ## For getting quantity
                jqb.current(0)
                jqb.place(x=350,y=120)

                global jbil
                def jbil():
                    sql="INSERT INTO bill VALUES('{}',{},{})".format(jm.cget("text"),jp.cget("text"),jqb.get())
                    SQLcursor.execute(sql)
                    

                

                ##Chicken Sandwich
                global k
                k=PhotoImage(file="23.png")
                kl= Label(win, image=k)
                kl.place(x=0,y=538)
                km=Label(win,text="Chicken sandwich",font=("Congenial",20,BOLD),bg="#aeb6b7")
                km.place(x=300,y=578)
                s=Label(win,text="₹",font=("Congenial",15,BOLD),bg="#aeb6b7")
                s.place(x=350,y=618)
                kp=Label(win,text="190",font=("Congenial",15,BOLD),bg="#aeb6b7")
                kp.place(x=367,y=618)

                
                kqty=Label(win,text="Qty:",font=("Congenial",15),bg="#c0a98e")
                kqty.place(x=300,y=658)
                kqb=ttk.Combobox(win,width=10,font=("Congenial",15),values=("0","1","2","3","4","5","6","7","8"))     ## For getting quantity
                kqb.current(0)
                kqb.place(x=350,y=658)

                global kbil
                def kbil():
                    sql="INSERT INTO bill VALUES('{}',{},{})".format(km.cget("text"),kp.cget("text"),kqb.get())
                    SQLcursor.execute(sql)



                ##Cookies
                global l
                l=PhotoImage(file="25.png")
                ll= Label(win, image=l)
                ll.place(x=1190,y=0)
                lm=Label(win,text="Cookies",font=("Congenial",20,BOLD),bg="#aeb6b7")
                lm.place(x=1040,y=40)
                s=Label(win,text="₹",font=("Congenial",15,BOLD),bg="#aeb6b7")
                s.place(x=1050,y=80)
                lp=Label(win,text="160",font=("Congenial",15,BOLD),bg="#aeb6b7")
                lp.place(x=1067,y=80)

            
                lqty=Label(win,text="Qty:",font=("Congenial",15),bg="#c0a98e")
                lqty.place(x=1000,y=120)
                lqb=ttk.Combobox(win,width=10,font=("Congenial",15),values=("0","1","2","3","4","5","6","7","8"))     ## For getting quantity
                lqb.current(0)
                lqb.place(x=1050,y=120)

                global lbil
                def lbil():
                    sql="INSERT INTO bill VALUES('{}',{},{})".format(lm.cget("text"),lp.cget("text"),lqb.get())
                    SQLcursor.execute(sql)


                ##Veg Sandwich
                global m
                m=PhotoImage(file="26.png")
                ml= Label(win, image=m)
                ml.place(x=1190,y=538)
                mm=Label(win,text="Veg Sandwhich",font=("Congenial",20,BOLD),bg="#aeb6b7")
                mm.place(x=970,y=578)
                s=Label(win,text="₹",font=("Congenial",15,BOLD),bg="#aeb6b7")
                s.place(x=1020,y=618)
                mp=Label(win,text="170",font=("Congenial",15,BOLD),bg="#aeb6b7")
                mp.place(x=1037,y=618)

                
                mqty=Label(win,text="Qty:",font=("Congenial",15),bg="#c0a98e")
                mqty.place(x=1000,y=658)
                mqb=ttk.Combobox(win,width=10,font=("Congenial",15),values=("0","1","2","3","4","5","6","7","8"))    ## For getting quantity
                mqb.current(0)
                mqb.place(x=1050,y=658)

                global mbil
                def mbil():
                    sql="INSERT INTO bill VALUES('{}',{},{})".format(mm.cget("text"),mp.cget("text"),mqb.get())
                    SQLcursor.execute(sql)

                


                ##Croissant
                global n
                n=PhotoImage(file="27.png")
                nl= Label(win, image=n)
                nl.place(x=600,y=85)
                nm=Label(win,text="Croissant",font=("Congenial",20,BOLD),bg="#aeb6b7")
                nm.place(x=640,y=375)
                s=Label(win,text="₹",font=("Congenial",15,BOLD),bg="#aeb6b7")
                s.place(x=660,y=415)
                np=Label(win,text="150",font=("Congenial",15,BOLD),bg="#aeb6b7")
                np.place(x=677,y=415)

                nqty=Label(win,text="Qty:",font=("Congenial",15),bg="#c0a98e")
                nqty.place(x=620,y=455)
                nqb=ttk.Combobox(win,width=10,font=("Congenial",15),values=("0","1","2","3","4","5","6","7","8"))   ## For getting quantity
                nqb.current(0)
                nqb.place(x=670,y=455)

                global nbil
                def nbil():
                    sql="INSERT INTO bill VALUES('{}',{},{})".format(nm.cget("text"),np.cget("text"),nqb.get())
                    SQLcursor.execute(sql)

               

                #For returning to main menu
                re=Button(win,text="Return to Main Menu",font=("Calibri",20,BOLD),bg="#ff2c2c",command=mb)
                re.place(x=605,y=0)

                ## To Save Orders made in Snacks Page
                def save2():
                    jbil()
                    kbil()
                    lbil()
                    mbil()
                    nbil()
                    messagebox.showinfo("Success","Your Order info have been saved!!!")
                save=Button(win,text="Save Orders",font=("Calibri",35,BOLD,ITALIC),bg="#ff2c2c",command=save2)
                save.place(x=605,y=650)
           
            #For Snacks Button
            global s
            s=PhotoImage(file="5.png")
            sl=Label(win,image=s)
            snacks=Button(win,image=s,command=so)
            snacks.place(x=20,y=500)
            sm=Label(win,text="Snacks & QuickBites",font=("Times New Roman",25,BOLD,ITALIC),bg="#00766d")
            sm.place(x=25,y=458)




            ##For Merchandise Page
            def mo():
                forget3()
                
                global BG2
                BG2=PhotoImage(file="0008.png")
                BL2= Label(win, image=BG2)
                BL2.place(x=0,y=0)

                messagebox.showinfo("Loading","Loading..., Please wait till system checks for available items!!!!")     

                global m2
                m2=PhotoImage(file="18.png")
                mo1=Label(win, image=m2)
                mo1.place(x=20,y=20)
                mm2=Label(win,text="Oil painted Cup",font=("Times New Roman",20,ITALIC,BOLD),bg="#aeb6b7")
                mm2.place(x=320,y=30)
                s=Label(win,text="₹",font=("Congenial",20,BOLD),bg="#aeb6b7")
                s.place(x=320,y=80)
                mp2=Label(win,text="350",font=("Times New Roman",20,ITALIC),bg="#aeb6b7")
                mp2.place(x=337,y=80)
                
                mqty=Label(win,text="Qty:",font=("Congenial",15),bg="#c0a98e")
                mqty.place(x=320,y=120)
                mqb=ttk.Combobox(win,width=10,font=("Congenial",15),values=("0","1","2","3","4","5","6","7","8"))    ## For getting quantity
                mqb.current(0)
                mqb.place(x=370,y=120)

                    
                global m2bil
                def m2bil():
                    sql="INSERT INTO bill VALUES('{}',{},{})".format(mm2.cget("text"),mp2.cget("text"),mqb.get())
                    SQLcursor.execute(sql)
                        
                


                global n2
                n2=PhotoImage(file="20.png")
                mo2= Label(win, image=n2)
                mo2.place(x=20,y=500)
                nm2=Label(win,text="Bikers Cup",font=("Times New Roman",20,ITALIC,BOLD),bg="#aeb6b7")
                nm2.place(x=320,y=530)
                s=Label(win,text="₹",font=("Congenial",20,BOLD),bg="#aeb6b7")
                s.place(x=320,y=580)
                np2=Label(win,text="500",font=("Times New Roman",20,ITALIC),bg="#aeb6b7")
                np2.place(x=337,y=580)

                
                nqty=Label(win,text="Qty:",font=("Congenial",15),bg="#c0a98e")
                nqty.place(x=320,y=620)
                nqb=ttk.Combobox(win,width=10,font=("Congenial",15),values=("0","1","2","3","4","5","6","7","8"))     ## For getting quantity
                nqb.current(0)
                nqb.place(x=370,y=620)

                global n2bil
                def n2bil():
                    sql="INSERT INTO bill VALUES('{}',{},{})".format(nm2.cget("text"),np2.cget("text"),nqb.get())
                    SQLcursor.execute(sql)
                    
               
                

                global o
                o=PhotoImage(file="19.png")
                mo3=Label(win, image=o)
                mo3.place(x=1150,y=20)
                om=Label(win,text="Plain-White Mug",font=("Times New Roman",20,ITALIC,BOLD),bg="#aeb6b7")
                om.place(x=940,y=30)
                s=Label(win,text="₹",font=("Congenial",20,BOLD),bg="#aeb6b7")
                s.place(x=980,y=80)
                op=Label(win,text="350",font=("Times New Roman",20,ITALIC),bg="#aeb6b7")
                op.place(x=997,y=80)

               
                oqty=Label(win,text="Qty:",font=("Congenial",15),bg="#c0a98e")
                oqty.place(x=950,y=120)
                oqb=ttk.Combobox(win,width=10,font=("Congenial",15),values=("0","1","2","3","4","5","6","7","8"))     ## For getting quantity
                oqb.current(0)
                oqb.place(x=1000,y=120)

                global obil
                def obil():
                    sql="INSERT INTO bill VALUES('{}',{},{})".format(om.cget("text"),op.cget("text"),oqb.get())
                    SQLcursor.execute(sql)
                     
                    

                global p
                p=PhotoImage(file="21.png")
                mo4=Label(win, image=p)
                mo4.place(x=1150,y=500)
                pm=Label(win,text="Workout Mug",font=("Times New Roman",20,ITALIC,BOLD),bg="#aeb6b7")
                pm.place(x=940,y=530)
                s=Label(win,text="₹",font=("Congenial",20,BOLD),bg="#aeb6b7")
                s.place(x=1000,y=580)
                pp=Label(win,text="500",font=("Times New Roman",20,ITALIC),bg="#aeb6b7")
                pp.place(x=1017,y=580)

                
                pqty=Label(win,text="Qty:",font=("Congenial",15),bg="#c0a98e")
                pqty.place(x=950,y=620)
                pqb=ttk.Combobox(win,width=10,font=("Congenial",15),values=("0","1","2","3","4","5","6","7","8"))   ## For getting quantity
                pqb.current(0)
                pqb.place(x=1000,y=620)

                global pbil
                def pbil():
                    sql="INSERT INTO bill VALUES('{}',{},{})".format(pm.cget("text"),pp.cget("text"),pqb.get())
                    SQLcursor.execute(sql)
                
                
                #For returning to main menu
                re=Button(win,text="Return to Main Menu",font=("Calibri",20,BOLD),bg="#ff2c2c",command=mb)
                re.place(x=605,y=0)


                ## To Save Orders made in Merch Page
                def save3():
                    m2bil()
                    n2bil()
                    obil()
                    pbil()
                    messagebox.showinfo("Success","Your Order info have been saved!!!")
                save4=Button(win,text="Save Orders",font=("Calibri",35,BOLD,ITALIC),bg="#ff2c2c",command=save3)
                save4.place(x=600,y=350)

            #For Merchandise Button
            global m
            m=PhotoImage(file="6.png")
            ml=Label(win,image=m)
            merchandise=Button(win,image=m,command=mo)
            merchandise.place(x=1100,y=20)
            mm=Label(win,text="Merchandise",font=("Times New Roman",25,BOLD,ITALIC),bg="#ca660c")
            mm.place(x=1165,y=325)


            def bo():
                forget3()

                global BG4
                BG4=PhotoImage(file="0009.png")
                BL4= Label(win, image=BG4)
                BL4.place(x=0,y=0)

                messagebox.showinfo("Loading","Loading..., Please wait till system checks for available items!!!!")

                ##Combo-1
                global q
                q=PhotoImage(file="29.png")
                qp=Label(win, image=q)
                qp.place(x=20,y=0)
                global p
                p=PhotoImage(file="30.png")
                pp=Label(win, image=p)
                pp.place(x=160,y=0)
                pn=Label(win,text="Cold Brew & Veg. Sandwich",font=("Times New Roman",20,BOLD,ITALIC),bg="#aeb6b7")
                pn.place(x=20,y=150)
                s=Label(win,text="₹",font=("Congenial",20,BOLD),bg="#aeb6b7")
                s.place(x=60,y=190)
                pp=Label(win,text="250",font=("Times New Roman",20,ITALIC,BOLD),bg="#aeb6b7")
                pp.place(x=77,y=190)

                
                pqty=Label(win,text="Qty:",font=("Congenial",15),bg="#c0a98e")
                pqty.place(x=40,y=230)
                pqb=ttk.Combobox(win,width=10,font=("Congenial",15),values=("0","1","2","3","4","5","6","7","8"))      ## For getting quantity
                pqb.current(0)
                pqb.place(x=90,y=230)

                global p2bil
                def p2bil():
                    sql="INSERT INTO bill VALUES('{}',{},{})".format(pn.cget("text"),pp.cget("text"),pqb.get())
                    SQLcursor.execute(sql)



                ##Combo-2
                global r
                r=PhotoImage(file="31.png")
                rp=Label(win, image=r)
                rp.place(x=20,y=480)
                global s2
                s2=PhotoImage(file="32.png")
                sp=Label(win, image=s2)
                sp.place(x=160,y=480)
                sn=Label(win,text="Iced Coffee & Chicken Sandwich",font=("Times New Roman",20,BOLD,ITALIC),bg="#aeb6b7")
                sn.place(x=20,y=630)
                sy=Label(win,text="₹",font=("Congenial",20,BOLD),bg="#aeb6b7")
                sy.place(x=60,y=670)
                sp=Label(win,text="280",font=("Times New Roman",20,ITALIC,BOLD),bg="#aeb6b7")
                sp.place(x=77,y=670)

                
                sqty=Label(win,text="Qty:",font=("Congenial",15),bg="#c0a98e")
                sqty.place(x=40,y=710)
                sqb=ttk.Combobox(win,width=10,font=("Congenial",15),values=("0","1","2","3","4","5","6","7","8"))     ## For getting quantity
                sqb.current(0)
                sqb.place(x=90,y=710)

                global sbil
                def sbil():
                    sql="INSERT INTO bill VALUES('{}',{},{})".format(sn.cget("text"),sp.cget("text"),sqb.get())
                    SQLcursor.execute(sql)



                ##Combo-3
                global t
                t=PhotoImage(file="33.png")
                tp=Label(win, image=t)
                tp.place(x=1070,y=0)
                global u
                u=PhotoImage(file="34.png")
                up=Label(win, image=u)
                up.place(x=1210,y=0)
                un=Label(win,text="Caramel Latte & Croissant",font=("Times New Roman",20,BOLD,ITALIC),bg="#aeb6b7")
                un.place(x=1070,y=150)
                s=Label(win,text="₹",font=("Congenial",20,BOLD),bg="#aeb6b7")
                s.place(x=1110,y=190)
                up=Label(win,text="275",font=("Times New Roman",20,ITALIC,BOLD),bg="#aeb6b7")
                up.place(x=1127,y=190)

                
                uqty=Label(win,text="Qty:",font=("Congenial",15),bg="#c0a98e")
                uqty.place(x=1090,y=230)
                uqb=ttk.Combobox(win,width=10,font=("Congenial",15),values=("0","1","2","3","4","5","6","7","8"))      ## For getting quantity
                uqb.current(0)
                uqb.place(x=1140,y=230)

                global ubil
                def ubil():
                    sql="INSERT INTO bill VALUES('{}',{},{})".format(un.cget("text"),up.cget("text"),uqb.get())
                    SQLcursor.execute(sql)
                

                ##Combo-4
                global v
                v=PhotoImage(file="35.png")
                vp=Label(win, image=v)
                vp.place(x=1070,y=480)
                global w
                w=PhotoImage(file="36.png")
                wp=Label(win, image=w)
                wp.place(x=1210,y=480)
                wn=Label(win,text="Flat White & Chocolates",font=("Times New Roman",20,BOLD,ITALIC),bg="#aeb6b7")
                wn.place(x=1070,y=630)
                s=Label(win,text="₹",font=("Congenial",20,BOLD),bg="#aeb6b7")
                s.place(x=1110,y=670)
                wp=Label(win,text="250",font=("Times New Roman",20,ITALIC,BOLD),bg="#aeb6b7")
                wp.place(x=1127,y=670)

               
                wqty=Label(win,text="Qty:",font=("Congenial",15),bg="#c0a98e")
                wqty.place(x=1090,y=710)
                wqb=ttk.Combobox(win,width=10,font=("Congenial",15),values=("0","1","2","3","4","5","6","7","8"))    ## For getting quantity
                wqb.current(0)
                wqb.place(x=1140,y=710)

                global wbil
                def wbil():
                    sql="INSERT INTO bill VALUES('{}',{},{})".format(wn.cget("text"),wp.cget("text"),wqb.get())
                    SQLcursor.execute(sql)
                


                ##Combo-5
                global x
                x=PhotoImage(file="37.png")
                xp=Label(win, image=x)
                xp.place(x=550,y=240)
                global y
                y=PhotoImage(file="38.png")
                yp=Label(win, image=y)
                yp.place(x=690,y=240)
                yn=Label(win,text="Espresso & Cookies",font=("Times New Roman",20,BOLD,ITALIC),bg="#aeb6b7")
                yn.place(x=550,y=390)
                s=Label(win,text="₹",font=("Congenial",20,BOLD),bg="#aeb6b7")
                s.place(x=590,y=430)
                yp=Label(win,text="275",font=("Times New Roman",20,ITALIC,BOLD),bg="#aeb6b7")
                yp.place(x=607,y=430)

            
                yqty=Label(win,text="Qty:",font=("Congenial",15),bg="#c0a98e")
                yqty.place(x=570,y=470)
                yqb=ttk.Combobox(win,width=10,font=("Congenial",15),values=("0","1","2","3","4","5","6","7","8"))    ## For getting quantity
                yqb.current(0)
                yqb.place(x=620,y=470)

                global ybil
                def ybil():
                    sql="INSERT INTO bill VALUES('{}',{},{})".format(yn.cget("text"),yp.cget("text"),yqb.get())
                    SQLcursor.execute(sql)
                        
                
                #For returning to main menu
                re=Button(win,text="Return to Main Menu",font=("Calibri",20,BOLD),bg="#ff2c2c",command=mb)
                re.place(x=605,y=0)

                def save5():
                    p2bil()
                    sbil()
                    ubil()
                    ybil()
                    messagebox.showinfo("Success","Your Order info have been saved!!!")
                save6=Button(win,text="Save Orders",font=("Calibri",35,BOLD,ITALIC),bg="#ff2c2c",command=save5)
                save6.place(x=600,y=600)
                


            #For Combos Button
            global b
            b=PhotoImage(file="7.png")
            bl=Label(win,image=b)
            bestseller=Button(win,image=b,command=bo)
            bestseller.place(x=1100,y=500)
            bm=Label(win,text="Combos",font=("Times New Roman",25,BOLD,ITALIC),bg="#7f0000")
            bm.place(x=1180,y=460)


            def forget4():
                coffee.place_forget()
                cm.place_forget()
                snacks.place_forget()
                sm.place_forget()
                merchandise.place_forget()
                mm.place_forget()
                bestseller.place_forget()
                bm.place_forget()
                bill.place_forget()
                h.place_forget()
                z.place_forget()
                z1.place_forget()
                


            ## For Billing 
            def bill2():
                forget4()
                
                ## For Background Image
                global BG5
                BG5=PhotoImage(file="0010.png")
                BL5= Label(win, image=BG5)
                BL5.place(x=0,y=0)

                ##To get the total amount of bill
                sql2="alter table bill add column Amount int ;"
                SQLcursor.execute(sql2)

                sql3="update bill set amount=price*quantity;"
                SQLcursor.execute(sql3)

                ## To store the ordered items into a variable to print
                sql="select item,quantity,price,Amount from bill where Quantity != 0 ;"
                SQLcursor.execute(sql)
                data=SQLcursor.fetchall()
                flag=False
                s=[]
                for i in data:
                    s.append(i)
                    flag=True            
                if flag==False:
                    x="No Record Found !!!"


                ##For Displaying the orders in tkinter window
                frame = Frame(win, width=400, height=200)
                frame.place(x=20,y=250)
                style = ttk.Style()
                style.theme_use('classic')
                l=len(data)
                tree = ttk.Treeview(frame, column=("Item", "Price", "Quantity"), show='headings',height=l)
                tree.column("# 1", anchor=CENTER)
                tree.heading("# 1", text="Item")
                tree.column("# 2", anchor=CENTER)
                tree.heading("# 2", text="Price")
                tree.column("# 3", anchor=CENTER)
                tree.heading("# 3", text="Quantity")
                for i in data:                                   ## To Add Data into the Tree
                    tree.insert('', 'end', text="1", values=i)
                tree.pack()

                    

                ##To print the bill as a table
                t= PrettyTable(['Item','Quantity','Price','Amount'])  ## To Add column Names
                for i in s:
                    t.add_row(i) ## To add Rows of Data


            
                z2=Label(win,text="Your Orders are :",font=("Times New Roman",50,BOLD,ITALIC),bg="#154360")
                z2.place(x=50,y=40)

                z3=Label(win,text="Your Total amount is :",font=("Times New Roman",30,BOLD,ITALIC),bg="#2236e1")
                z3.place(x=850,y=520)


                ## To Display QR-code to Pay
                z5=Label(win,text="---Pay here-->",font=("Times New Roman",40,BOLD,ITALIC),bg="#F1C40F")
                z5.place(x=700,y=240)

                global z6
                z6=PhotoImage(file="40.png")
                z6p=Label(win, image=z6)
                z6p.place(x=1050,y=140)

                       
                sql4="select sum(amount) from bill;"
                SQLcursor.execute(sql4)
                data2=SQLcursor.fetchall()
                s2=''
                for i in data2:
                    x=str(i)
                    s2+=x
                    flag=True
                if flag==False:
                    x="No Record Found !!!"
               
                

                ## To print the total amount
                z4=Label(win,text=data2,font=("Times New Roman",30,BOLD,ITALIC),bg="#2236e1")
                z4.place(x=1250,y=520)

                def mb2():
                    sql="DELETE from bill;"
                    SQLcursor.execute(sql)
                    mb()

                    sqla="alter table bill DROP column amount;"
                    SQLcursor.execute(sqla)
                  

                #For returning to main menu in order to change the orders made 
                re=Button(win,text="Order From First !!!",font=("Calibri",25,BOLD),bg="#ff2c2c",command=mb2)
                re.place(x=100,y=700)


                ## for bill as txt-file
                def print_bill():

                    messagebox.showinfo("Pls Wait...","Please wait system till system prepares the bill !!!")

                    
                    f="SunBucks_cafe_Bill_"+str(Name_entry.get())+".txt"
                    fh=open(f,'w')
                    fh.write("Customer Name :\t")
                    fh.write(Name_entry.get()+"\n")
                    fh.write("Customer Mail :\t")
                    fh.write(Mail_entry.get()+"\n")
                    fh.write("_______________________________________________________________\n")
                    fh.write("Your Orders are :\n")
                    fh.write(str(t))
                    fh.write("\n_______________________________________________________________\n")
                    fh.write("Grand Total :\t")
                    fh.write(s2)

                    sqla="DROP table bill;"
                    SQLcursor.execute(sqla)



                    ## To send bill in e-mail
                    ms=smtplib.SMTP('smtp.gmail.com',587)
                    ms.starttls()
                    ms.login("sunbuckscafepro@gmail.com","rzqh iyib lomt dgcm")   ## Sender's ID & App Password
                    fh=open(f,'r')
                    c=fh.read()
                    message="\n Your Bill : \n\n"+c
                    ms.sendmail("sunbuckscafepro@gmail.com",Mail_entry.get(),message)   ## To send mail (Sender's ID , Reciever's ID , Content to be sent)
                    ms.quit()
                                     

                    ## To print bill 
                    print("Your Orders are :\n")
                    print(t)
                    print("\n Your Total amount is : ",s2)
                    print("\n Your Bill is sent to your Mail ! ! !")
                    

                    messagebox.showinfo(" Success Order Placed","Your Order Have been placed !!! \n Thanks for choosing SunBucks Cafe !!!  Enjoy your drink !!! \n \n !! Please Close the application !! \n \n Bill is sent to your mail and can also be found in File Explorer !!")

                    win.destroy()

                    
                ## Too print the bill and mail it
                pb=Button(win,text="Print Bill-->",font=("Calibri",25,BOLD),bg="#ff2c2c",command=print_bill)
                pb.place(x=900,y=700)
                    

            ## For Billing part
            bill=Button(win,text="---Continue --->",font=("Calibri",30,BOLD,ITALIC),bg="#145A32",command=bill2)
            bill.place(x=600,y=560)
            

        submit=Button(win,text="--ORDER-->",font=("Times New Roman",30,BOLD),bg="#E3242B",command=mb) 
        submit.place(x=580,y=670)

    sd=Button(win,text="Save details",font=("Times New Roman",25,BOLD,ITALIC),bg="#c0c0c0",command=nb)
    sd.place(x=680,y=470)
    
    
    

## To remove all the contents of first page
def forget():
    system_name_label.place_forget()
    wq.place_forget()
    imglabel.place_forget()
    login.place_forget()
    log()
    
## For login Button
login=Button(win,text="Login",font=("Times New Roman",25,BOLD),bg="#f48e3b",command=forget)
login.place(x=700,y=520)

win.mainloop()   
