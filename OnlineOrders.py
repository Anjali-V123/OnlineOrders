from tkinter import *
from PIL import ImageTk,Image
from tkinter.font import Font
root= Tk()
import pickle
item_name=[]
item_cost=[]
l=[]
m1=[]
m2=[]
n=0
nowrun=0
nowrun1=0
nowrun2=0
total=0
e=open("a.dat","ab")
pickle.dump("*",e)
e.close()
w=open("b.dat","ab")
pickle.dump("*",w)
w.close()
z=open("c.dat","wb")
choices=["1. use frequent customer coupon","2. Save to balance"]
pickle.dump(choices,z)
z.close()
q2=open("c2.dat","ab")
pickle.dump("*",q2)
q2.close()
q3=open("c3.dat","ab")
pickle.dump("*",q3)
q3.close()
fl=open("c4.dat","wb")
pickle.dump("*",fl)
fl.close()
f=open("c5.dat","wb")
l1=["1. Maddie's Margherita pizza-Rs 200","2. Farmhouse pizza -Rs 300","3. Veggie paradise pizza- Rs 300","4. Peppy paneer- Rs 450","5.Chicken dominator- Rs 350","6. Bloody mary pizza- Rs 250","7. Chocolava cake- Rs 55","8. Lasagna- Rs 300","9. Garlic Bread- Rs 150"]
pickle.dump(l1,f)
f.close()

fll=open("c6.dat","wb")
pickle.dump("*",fll)
fll.close()

def checkout():
    root3=Tk()
    root3.geometry(f"{width}x{height}+{0}+{0}")
    total=0
    MyLabel2112=Label(root3,text="                                    
                                                                     
                                                                     
      ")
    MyLabel2112.grid(row=0,column=0)
    Font22=Font(family="chiller",size=100,slant="roman")
    MyLabel41=Label(root3,text="\n\n\n\n\n Saltiez
Pizzeria",font=Font22)
    MyLabel41.grid(row=0,column=1)
    MyLabel2299=Label(root3,text="                                    
                                                                     
                                      ")
    MyLabel2299.grid(row=1,column=0)
    MyLabel42=Label(root3,text="Date:")
    MyLabel42.grid(row=1,column=1)
    MyLabel43=Label(root3,text=date1)
    MyLabel43.grid(row=1,column=2)
    for i in range(len(m1)):
        MyLabel3333=Label(root3,text="                                
                                                                     
                                      ")
        MyLabel3333.grid(row=i+2,column=0)
        MyLabel44=Label(root3,text=i+1)
        MyLabel44.grid(row=i+2,column=1)
        MyLabel45=Label(root3,text=item_name[i])
        MyLabel45.grid(row=i+2,column=2)
        bc="Rs"+str(item_cost[i])
        MyLabel46=Label(root3,text=bc)
        MyLabel46.grid(row=i+2,column=3)
        total=total+item_cost[i]
    MyLabel4444=Label(root3,text="                                    
                                                                     
                                                                     
      ")
    MyLabel4444.grid(row=len(m1)+3,column=0)
    a="Total cost= Rs"+str(total)
    MyLabel47=Label(root3,text=a)

    MyLabel47.grid(row=len(m1)+2,column=1)
    MyLabel5555=Label(root3,text="                                    
                                                                     
                                                                     
      ")
    MyLabel5555.grid(row=len(m1)+3,column=0)
    MyLabel48=Label(root3,text="Thank you, please visit again")
    MyLabel48.grid(row=len(m1)+3,column=1)

def freq():
    root3=Tk()
    root3.geometry(f"{width}x{height}+{0}+{0}")
    total=0
    e=open("a.dat","rb")
    ss=pickle.load(e)
    e.close()
    if ss=="*":
        Font22=Font(family="chiller",size=100,slant="roman")
        MyLabel41=Label(root3,text="\n\n\n\n Saltiez
Pizzeria",font=Font22)
        MyLabel41.grid(row=0,column=1)
        MyLabel2299=Label(root3,text="                                
                                                                     
                                          ")
        MyLabel2299.grid(row=1,column=0)
        MyLabel42=Label(root3,text="Date:")
        MyLabel42.grid(row=1,column=1)
        MyLabel43=Label(root3,text=date1)
        MyLabel43.grid(row=1,column=2)
        for i in range(len(m1)):
            MyLabel3333=Label(root3,text="                            
                                                                     
                                          ")
            MyLabel3333.grid(row=i+2,column=0)
            MyLabel44=Label(root3,text=i+1)
            MyLabel44.grid(row=i+2,column=1)
            MyLabel45=Label(root3,text=item_name[i])
            MyLabel45.grid(row=i+2,column=2)
            bc="Rs"+str(item_cost[i])
            MyLabel46=Label(root3,text=bc)
            MyLabel46.grid(row=i+2,column=3)
            total=total+item_cost[i]
        MyLabel4444=Label(root3,text="                                
                                                                     

                                                                     
          ")
        MyLabel4444.grid(row=len(m1)+3,column=0)
        total=total-(10/100)*total
        a="Total cost= Rs"+str(total)
        MyLabel47=Label(root3,text=a)
        MyLabel47.grid(row=len(m1)+2,column=1)
        MyLabel5555=Label(root3,text="                                
                                                                     
                                                                     
          ")
        MyLabel5555.grid(row=len(m1)+3,column=0)
        MyLabel48=Label(root3,text="Thank you, please visit again")
        MyLabel48.grid(row=len(m1)+3,column=1)
    else:
        MyLabel26=Label(root3,text="Do you want to use the money in
your balance account:")
        MyLabel26.pack()
        e9=Entry(root3,width=50)
        e9.pack()
        def click7():
            total=0
            choice2=e9.get()
            if choice2=="y":
                root70=Tk()
                root70.geometry(f"{width}x{height}+{0}+{0}")
                Font22=Font(family="chiller",size=100,slant="roman")
                MyLabel41=Label(root70,text="\n\n\n\n Saltiez
Pizzeria",font=Font22)
                MyLabel41.grid(row=0,column=1)
                MyLabel2299=Label(root70,text="                      
                                                                     
                                                    ")
                MyLabel2299.grid(row=1,column=0)
                MyLabel42=Label(root70,text="Date:")
                MyLabel42.grid(row=1,column=1)
                MyLabel43=Label(root70,text=date1)
                MyLabel43.grid(row=1,column=2)
                m2.append(1)
                for i in range(len(m1)):
                    MyLabel3333=Label(root70,text="                  
                                                                     
                                                    ")
                    MyLabel3333.grid(row=i+2,column=0)
                    MyLabel44=Label(root70,text=i+1)
                    MyLabel44.grid(row=i+2,column=1)

                    MyLabel45=Label(root70,text=item_name[i])
                    MyLabel45.grid(row=i+2,column=2)
                    bc="Rs"+str(item_cost[i])
                    MyLabel46=Label(root70,text=bc)
                    MyLabel46.grid(row=i+2,column=3)
                    total=total+item_cost[i]
                MyLabel4444=Label(root70,text="                      
                                                                     
                                                                     
                    ")
                MyLabel4444.grid(row=len(m1)+3,column=0)
                gg=int(ss)
                total=total-gg
                e=open("a.dat","wb")
                pickle.dump("*",e)
                e.close()
                a="Total cost= Rs"+str(total)
                MyLabel47=Label(root70,text=a)
                MyLabel47.grid(row=len(m1)+2,column=1)
                MyLabel5555=Label(root70,text="                      
                                                                     
                                                                     
                    ")
                MyLabel5555.grid(row=len(m1)+3,column=0)
                MyLabel48=Label(root70,text="Thank you, please visit
again")
                MyLabel48.grid(row=len(m1)+3,column=1)
                root70.mainloop()
            else:
                root70=Tk()
                root70.geometry(f"{width}x{height}+{0}+{0}")
                Font22=Font(family="chiller",size=100,slant="roman")
                MyLabel41=Label(root70,text="\n\n\n\n Saltiez
Pizzeria",font=Font22)
                MyLabel41.grid(row=0,column=1)
                MyLabel2299=Label(root70,text="                      
                                                                     
                                                    ")
                MyLabel2299.grid(row=1,column=0)
                MyLabel42=Label(root70,text="Date:")
                MyLabel42.grid(row=1,column=1)
                MyLabel43=Label(root70,text=date1)
                MyLabel43.grid(row=1,column=2)
                for i in range(len(m1)):

                    MyLabel3333=Label(root70,text="                  
                                                                     
                                                    ")
                    MyLabel3333.grid(row=i+2,column=0)
                    MyLabel44=Label(root70,text=i+1)
                    MyLabel44.grid(row=i+2,column=1)
                    MyLabel45=Label(root70,text=item_name[i])
                    MyLabel45.grid(row=i+2,column=2)
                    bc="Rs"+str(item_cost[i])
                    MyLabel46=Label(root70,text=bc)
                    MyLabel46.grid(row=i+2,column=3)
                    total=total+item_cost[i]
                MyLabel4444=Label(root70,text="                      
                                                                     
                                                                     
                    ")
                MyLabel4444.grid(row=len(m1)+3,column=0)
                a="Total cost= Rs"+str(total)
                MyLabel47=Label(root70,text=a)
                MyLabel47.grid(row=len(m1)+2,column=1)
                MyLabel5555=Label(root70,text="                      
                                                                     
                                                                     
                    ")
                MyLabel5555.grid(row=len(m1)+3,column=0)
                MyLabel48=Label(root70,text="Thank you, please visit
again")
                MyLabel48.grid(row=len(m1)+3,column=1)
                root70.mainloop()
        MyButton17=Button(root3,text="checkout",command=click7)
        MyButton17.pack()
        root3.mainloop()
def previous():
    pr=open("c7.dat","ab")
    pickle.dump("*",pr)
    pr.close()
    try:
        pr=open("c7.dat","rb")
        m=pickle.load(pr)
        pr.close()
        if m=="*":
            root5=Tk()
            root5.geometry(f"{width}x{height}+{0}+{0}")
            global nowrun
            nowrun+=1

            c=open("c1.dat","wb")
            pickle.dump(nowrun,c)
            c.close()
            MyLabel171=Label(root5,text="\n\n\n\n\n Sorry no coupons
are available right now")
            MyLabel171.pack()
            pr=open("c7.dat","wb")
            pickle.dump(l,pr)
            pr.close()
            def click109():
                root5.destroy()
            MyButton173=Button(root5,text="Home
Page",command=click109)
            MyButton173.pack()
            MyButton777=Button(root5,text="checkout",command=checkout)
            MyButton777.pack()
            root5.mainloop()
        else:
            c=open("c1.dat","rb")
            jj=pickle.load(c)
            c.close()
            jj+=1
            nowrun=jj
            c=open("c1.dat","wb")
            pickle.dump(nowrun,c)
            c.close()
            if nowrun==2:
                root6=Tk()
                root6.geometry(f"{width}x{height}+{0}+{0}")
                MyLabel172=Label(root6,text="\n\n\n\n\n Sorry no
coupons are available right now")
                MyLabel172.pack()
                def click112():
                    root6.destroy()
                MyButton174=Button(root6,text="Home
Page",command=click112)
                MyButton174.pack()
                MyButton778=Button(root6,text="checkout",command=check
out)
                MyButton778.pack()
                root6.mainloop()
            elif nowrun&gt;2:
                w=open("b.dat","rb")
                kl=pickle.load(w)
                w.close()
                if kl=="*":

                    q3=open("c3.dat","rb")
                    mn=pickle.load(q3)
                    q3.close()
                    if mn=="*":
                        root3=Tk()
                        root3.geometry(f"{width}x{height}+{0}+{0}")
                        MyLabel7=Label(root3,text="\n\n\n\n\n you are
a frequent customer")
                        MyLabel7.pack()
                        MyLabel8=Label(root3,text="showing your
choices:")
                        MyLabel8.pack()
                        try:
                            z=open("c.dat","rb")
                            qwe=pickle.load(z)
                            for x in qwe:
                                MyLabel9=Label(root3,text=x)
                                MyLabel9.pack()
                        except EOFError:
                            z.close()
                        MyLabel14=Label(root3,text="enter your choice-
1/2:")
                        MyLabel14.pack()
                        e8=Entry(root3,width=50)
                        e8.pack()
                        def click5():
                            choice1=e8.get()
                            q4=open(&#39;c8.dat&#39;,&#39;wb&#39;)
                            pickle.dump(choice1,q4)
                            q4.close()
                            q3=open("c3.dat","wb")
                            pickle.dump("##",q3)
                            q3.close()
                            q4=open("c8.dat",&#39;rb&#39;)
                            mk=pickle.load(q4)
                            ms=int(mk)
                            q4.close()
                            if ms==1:
                                freq()
                                w=open("b.dat","wb")
                                pickle.dump("used",w)
                                w.close()
                            else:
                                global total
                                for i in range(len(m1)):
                                    total=total+item_cost[i]

                                total=(10/100)*total
                                e=open("a.dat","wb")
                                pickle.dump(total,e)
                                e.close()
                                root25=Tk()
                                root25.geometry(f"{width}x{height}+{0}
+{0}")
                                MyLabel10=Label(root25,text="\n\n\n\n\
n saving to your balance")
                                MyLabel10.pack()
                                MyButton9999=Button(root25,text="click
to look at final details",command=checkout)
                                MyButton9999.pack()
                                root25.mainloop()
                        MyButton111=Button(root3,text="checkout",comma
nd=click5)
                        MyButton111.pack()
                        root3.mainloop()
                    else:
                        freq()
                        if len(m2)==1:
                            w=open("b.dat","wb")
                            pickle.dump("used",w)
                            w.close()
                        else:
                            q2=open("c2.dat","rb")
                            ds=pickle.load(q2)
                            q2.close()
                            if ds=="*":
                                q2=open("c2.dat","wb")
                                pickle.dump("*",q2)
                                q2.close()
                            else:
                               freq()
                else:
                    root7=Tk()
                    root7.geometry(f"{width}x{height}+{0}+{0}")
                    MyLabel17221=Label(root7,text="\n\n\n\n\n Sorry no
coupons are available right now")
                    MyLabel17221.pack()
                    MyButton779=Button(root7,text="checkout",command=c
heckout)
                    MyButton779.pack()
                    root7.mainloop()
    except EOFError:
        pr.close()

def no():
    pr2=open("c9.dat","wb")
    pickle.dump(l,pr2)
    pr2.close()
def previous2():
    global nowrun1
    pr2=open("c9.dat","ab")
    pickle.dump("*",pr2)
    pr2.close()
    try:
            pr2=open("c9.dat","rb")
            m=pickle.load(pr2)
            pr2.close()
            if m=="*":
                root7=Tk()
                root7.geometry(f"{width}x{height}+{0}+{0}")
                nowrun1+=1
                pr2=open("c9.dat","wb")
                pickle.dump(l,pr2)
                pr2.close()
                font221=Font(family="Banschrift",size=20,slant="roman"
)
                MyLabel21=Label(root7,text="\n\n\n\n\n\n Welcome New
Customer!",font=font221)
                MyLabel21.pack()
                def click122():
                    root7.destroy()
                MyButton177=Button(root7,text="Home
Page",command=click122)
                MyButton177.pack()
                root7.mainloop()
            else:
                root4=Tk()
                root4.geometry(f"{width}x{height}+{0}+{0}")
                MyLabel11=Label(root4,text="\n\n\n\n\n Showing your
previous orders:")
                MyLabel11.pack()
                pr2=open("c9.dat","rb")
                oo=pickle.load(pr2)
                for y in oo:
                    MyLabel12=Label(root4,text=y)
                    MyLabel12.pack()
                pr2.close()
                pr2=open("c9.dat","wb")

                pickle.dump(l,pr2)
                pr2.close()
                def click123():
                    root4.destroy()
                MyButton178=Button(root4,text="Home
Page",command=click123)
                MyButton178.pack()
                root4.mainloop()
    except EOFError:
            pr2.close()
def final():
    root3=Tk()
    root3.geometry(f"{width}x{height}+{0}+{0}")
    MyLabel50=Label(root3,text="\n\n\n\n\n Do you want to see your
previous orders?")
    MyLabel50.pack()
    def click100():
        previous2()
    def click101():
        root66=Tk()
        root66.geometry(f"{width}x{height}+{0}+{0}")
        MyLabel222=Label(root66,text="\n\n\n\n\n\n\n\n\n\n ok,please
visit again")
        MyLabel222.pack()
        def click345():
            root66.destroy()
        MyButton9990009=Button(root66,text="Home
Page",command=click345)
        MyButton9990009.pack()
        no()
    MyButton990=Button(root3,text="yes",command=click100)
    MyButton990.pack()
    MyButton991=Button(root3,text="no",command=click101)
    MyButton991.pack()
    MyLabel11000=Label(root3,text="Please check for available coupons
before proceeding to checkout:")
    MyLabel11000.pack()
    def click102():
        previous()
    MyButton992=Button(root3,text="coupons",command=click102)
    MyButton992.pack()
    root3.mainloop()

import datetime as dt

date1=dt.date.today()
width=1280
height=720
root.geometry(f"{width}x{height}+{0}+{0}")

def something():
    root1=Tk()
    def comm():
        rootcart=Tk()
        rootcart.geometry(f"{width}x{height}+{0}+{0}")
        try:
            fll=open("c6.dat","rb")
            rr=pickle.load(fll)
        except EOFError:
            fll.close()
        if rr=="*":
            MyLabel5=Label(rootcart,text="\n\n\n\n\n\n\n\n\n you have
no items in your cart yet")
            MyLabel5.pack()
        else:
            for i in rr:
                MyLabel4=Label(rootcart,text=i)
                MyLabel4.pack()
        def click172():
            rootcart.destroy()
        MyButton2221=Button(rootcart,text="Home
Page",command=click172)
        MyButton2221.pack()
        rootcart.mainloop()
    Buttoncart=Button(root1,text="cart",command=comm)
    Buttoncart.grid(row=0,column=0)
    MyLabel771=Label(root1,text="                                    
                                                                     
                                                ")
    MyLabel771.grid(row=1,column=1)
    fl=open("c4.dat","rb")
    kk=pickle.load(fl)
    fl.close()
    Font2=Font(family="Times",size=10)
    root1.geometry(f"{width}x{height}+{0}+{0}")
    if kk=="*":
        root.destroy()
        fl=open("c4.dat","wb")

        pickle.dump("##",fl)
        fl.close()
        MyLabel1=Label(root1, text="Do you want to start adding to
cart- y/n:",font=Font2)
        MyLabel1.grid(row=2,column=2)
        MyLabel333=Label(root1,text="\n")
        MyLabel333.grid(row=2,column=0)
        e1= Entry(root1, width=30)
        e1.grid(row=3,column=2)
        def click():
            ord=e1.get()
            if ord=="y":
                MyLabel2=Label(root1, text="Showing your options:")
                MyLabel2.grid(row=5,column=2)
                try:
                    f=open("c5.dat","rb")
                    d=pickle.load(f)
                    m=len(d)
                    for i in range(0,m):
                        MyLabel3=Label(root1, text=d[i])
                        MyLabel3.grid(row=i+6,column=2)
                except EOFError:
                    f.close()
                for i in range(0,1):
                    MyLabel3=Label(root1,text="Enter the number of the
desired item : ")
                    MyLabel3.grid(row=m+7,column=2)
                    e2= Entry(root1, width=50)
                    e2.grid(row=m+8,column=2)
                    def click2():
                        choice=e2.get()
                        if choice=="1":
                            global n
                            Label1=Label(root1,text="added to cart")
                            Label1.grid(row=m+10,column=2)
                            item_name.append("Maddie&#39;s Margherita
pizza")
                            item_cost.append(200)
                            l.append("Maddie&#39;s Margherita pizza-Rs
200")
                            fll=open("c6.dat","wb")
                            pickle.dump(l,fll)
                            fll.close()
                            n=n+1
                            m1.append(n)

                            MyLabel5=Label(root1,text="Do you want to
order more- pls enter y/n:")
                            MyLabel5.grid(row=m+11,column=2)
                            e3= Entry(root1,width=50)
                            e3.grid(row=m+12,column=2)
                            def click3():
                                n1= e3.get()
                                if n1=="y":
                                    something()
                                else:
                                    final()
                            MyButton3=Button(root1,text="Submit",comma
nd=click3)
                            MyButton3.grid(row=m+13,column=2)
                        elif choice=="2":
                            Label2=Label(root1,text="added to cart")
                            Label2.grid(row=m+10,column=2)
                            item_name.append("Farmhouse pizza")
                            item_cost.append(300)
                            l.append("Farmhouse pizza-Rs 300")
                            n=n+1
                            m1.append(n)
                            fll=open("c6.dat","wb")
                            pickle.dump(l,fll)
                            fll.close()
                            MyLabel6=Label(root1,text="Do you want to
order more- pls enter y/n:")
                            MyLabel6.grid(row=m+11,column=2)
                            e4= Entry(root1,width=50)
                            e4.grid(row=m+12,column=2)
                            def click4():
                                n2=e4.get()
                                if n2=="y":
                                    something()
                                else:
                                    final()
                            MyButton4=Button(root1,text="submit",comma
nd=click4)
                            MyButton4.grid(row=m+13,column=2)
                        elif choice=="3":
                            Label3=Label(root1,text="added to cart")
                            Label3.grid(row=m+10,column=2)
                            item_name.append("Veggie paradise pizza")
                            item_cost.append(300)
                            l.append("Veggie paradise pizza-Rs 300")
                            n=n+1

                            m1.append(n)
                            MyLabel6=Label(root1,text="Do you want to
order more- pls enter y/n:")
                            MyLabel6.grid(row=m+11,column=2)
                            fll=open("c6.dat","wb")
                            pickle.dump(l,fll)
                            fll.close()
                            e5= Entry(root1,width=50)
                            e5.grid(row=m+12,column=2)
                            def click5():
                                n3=e5.get()
                                if n3=="y":
                                    something()
                                else:
                                    final()
                            MyButton5=Button(root1,text="submit",comma
nd=click5)
                            MyButton5.grid(row=m+13,column=2)
                        elif choice=="4":
                            Label4=Label(root1,text="added to cart")
                            Label4.grid(row=m+10,column=2)
                            item_name.append("Peppy paneer")
                            item_cost.append(450)
                            l.append("Peppy paneer-Rs 450")
                            n=n+1
                            m1.append(n)
                            MyLabel6=Label(root1,text="Do you want to
order more- pls enter y/n:")
                            MyLabel6.grid(row=m+11,column=2)
                            fll=open("c6.dat","wb")
                            pickle.dump(l,fll)
                            fll.close()
                            e6= Entry(root1,width=50)
                            e6.grid(row=m+12,column=2)
                            def click6():
                                nmm=e6.get()
                                if nmm=="y":
                                    something()
                                else:
                                    final()
                            MyButton6=Button(root1,text="submit",comma
nd=click6)
                            MyButton6.grid(row=m+13,column=2)
                        elif choice=="5":
                            Label5=Label(root1,text="added to cart")
                            Label5.grid(row=m+10,column=2)

                            item_name.append("Chicken dominator")
                            item_cost.append(350)
                            l.append("Chicken dominator-Rs 350")
                            n=n+1
                            m1.append(n)
                            MyLabel6=Label(root1,text="Do you want to
order more- pls enter y/n:")
                            MyLabel6.grid(row=m+11,column=2)
                            fll=open("c6.dat","wb")
                            pickle.dump(l,fll)
                            fll.close()
                            e7= Entry(root1,width=50)
                            e7.grid(row=m+12,column=2)
                            def click7():
                                nmm=e7.get()
                                if nmm=="y":
                                    something()
                                else:
                                    final()
                            MyButton7=Button(root1,text="submit",comma
nd=click7)
                            MyButton7.grid(row=m+13,column=2)
                        elif choice=="6":
                            Label6=Label(root1,text="added to cart")
                            Label6.grid(row=m+10,column=2)
                            item_name.append("Bloody mary pizza")
                            item_cost.append(250)
                            l.append("Bloody mary pizza-Rs 250")
                            n=n+1
                            m1.append(n)
                            MyLabel6=Label(root1,text="Do you want to
order more- pls enter y/n:")
                            MyLabel6.grid(row=m+11,column=2)
                            fll=open("c6.dat","wb")
                            pickle.dump(l,fll)
                            fll.close()
                            e8= Entry(root1,width=50)
                            e8.grid(row=m+12,column=2)
                            def click8():
                                nmm=e8.get()
                                if nmm=="y":
                                    something()
                                else:
                                    final()
                            MyButton8=Button(root1,text="submit",comma
nd=click8)

                            MyButton8.grid(row=m+13,column=2)
                        elif choice=="7":
                            Label7=Label(root1,text="added to cart")
                            Label7.grid(row=m+10,column=2)
                            item_name.append("Choco lava cake")
                            item_cost.append(55)
                            l.append("Choco lava cake-Rs 55")
                            n=n+1
                            m1.append(n)
                            MyLabel6=Label(root1,text="Do you want to
order more- pls enter y/n:")
                            MyLabel6.grid(row=m+11,column=2)
                            fll=open("c6.dat","wb")
                            pickle.dump(l,fll)
                            fll.close()
                            e9= Entry(root1,width=50)
                            e9.grid(row=m+12,column=2)
                            def click9():
                                nmm=e9.get()
                                if nmm=="y":
                                    something()
                                else:
                                    final()
                            MyButton9=Button(root1,text="submit",comma
nd=click9)
                            MyButton9.grid(row=m+13,column=2)
                        elif choice=="8":
                            Label8=Label(root1,text="added to cart")
                            Label8.grid(row=m+10,column=2)
                            item_name.append("Lasagna")
                            item_cost.append(300)
                            l.append("Lasagna-Rs 300")
                            n=n+1
                            m1.append(n)
                            MyLabel6=Label(root1,text="Do you want to
order more- pls enter y/n:")
                            MyLabel6.grid(row=m+11,column=2)
                            fll=open("c6.dat","wb")
                            pickle.dump(l,fll)
                            fll.close()
                            e10= Entry(root1,width=50)
                            e10.grid(row=m+12,column=2)
                            def click10():
                                nmm=e10.get()
                                if nmm=="y":
                                    something()

                                else:
                                    final()
                            MyButton10=Button(root1,text="submit",comm
and=click10)
                            MyButton10.grid(row=m+13,column=2)
                        elif choice=="9":
                            Label9=Label(root1,text="added to cart")
                            Label9.grid(row=m+10,column=2)
                            item_name.append("Garlic bread")
                            item_cost.append(150)
                            l.append("Garlic bread-Rs 150")
                            n=n+1
                            m1.append(n)
                            MyLabel6=Label(root1,text="Do you want to
order more- pls enter y/n:")
                            MyLabel6.grid(row=m+11,column=2)
                            fll=open("c6.dat","wb")
                            pickle.dump(l,fll)
                            fll.close()
                            e11= Entry(root1,width=50)
                            e11.grid(row=m+12,column=2)
                            def click11():
                                nmm=e11.get()
                                if nmm=="y":
                                    something()
                                else:
                                    final()
                            MyButton11=Button(root1,text="submit",comm
and=click11)
                            MyButton11.grid(row=m+13,column=2)
                    MyButton30=Button(root1,text="add to
cart",command=click2)
                    MyButton30.grid(row=m+9,column=2)
            elif ord==n:
                MyLabel4=Label(root1,text="Thank you, please visit
again")
                MyLabel4.grid(row=4,column=0)
            else:
                MyLabel700=Label(root1,text="wrong entry")
                MyLabel700.pack()
        MyButton=Button(root1,text="Submit",command=click)
        MyButton.grid(row=4,column=2)
    else:
        MyLabel2=Label(root1,text="Showing your options:")
        MyLabel2.grid(row=2,column=2)
        try:

            f=open("c5.dat","rb")
            d=pickle.load(f)
            m=len(d)
            for i in range(0,m):
                MyLabel3=Label(root1, text=d[i])
                MyLabel3.grid(row=i+3,column=2)
        except EOFError:
            f.close()
        for i in range(0,1):
            MyLabel3=Label(root1,text="Enter the number of the desired
item : ")
            MyLabel3.grid(row=m+4,column=2)
            e2= Entry(root1, width=50)
            e2.grid(row=m+5,column=2)
            def click2():
                choice=e2.get()
                if choice=="1":
                    global n
                    Label1=Label(root1,text="added to cart")
                    Label1.grid(row=m+7,column=2)
                    item_name.append("Maddie&#39;s Margherita pizza")
                    item_cost.append(200)
                    l.append("Maddie&#39;s Margherita pizza-rs 200")
                    n=n+1
                    m1.append(n)
                    fll=open("c6.dat","wb")
                    pickle.dump(l,fll)
                    fll.close()
                    MyLabel5=Label(root1,text="Do you want to order
more- pls enter y/n:")
                    MyLabel5.grid(row=m+8,column=2)
                    e3= Entry(root1,width=50)
                    e3.grid(row=m+9,column=2)
                    def click3():
                        nm= e3.get()
                        if nm=="y":
                            something()
                        else:
                            final()
                    MyButton3=Button(root1,text="Submit",command=click
3)
                    MyButton3.grid(row=m+10,column=2)
                elif choice=="2":
                    Label2=Label(root1,text="added to cart")
                    Label2.grid(row=m+7,column=2)
                    item_name.append("Farmhouse pizza")

                    item_cost.append(300)
                    l.append("Farmhouse pizza-Rs 300")
                    n=n+1
                    m1.append(n)
                    fll=open("c6.dat","wb")
                    pickle.dump(l,fll)
                    fll.close()
                    MyLabel6=Label(root1,text="Do you want to order
more- pls enter y/n:")
                    MyLabel6.grid(row=m+8,column=2)
                    e4= Entry(root1,width=50)
                    e4.grid(row=m+9,column=2)
                    def click4():
                        nmm=e4.get()
                        if nmm=="y":
                            something()
                        else:
                            final()
                    MyButton4=Button(root1,text="submit",command=click
4)
                    MyButton4.grid(row=m+10,column=2)
                elif choice=="3":
                    Label3=Label(root1,text="added to cart")
                    Label3.grid(row=m+7,column=2)
                    item_name.append("Veggie paradise pizza")
                    item_cost.append(300)
                    l.append("Veggie Paradise Pizza-Rs 300")
                    n=n+1
                    m1.append(n)
                    MyLabel6=Label(root1,text="Do you want to order
more- pls enter y/n:")
                    MyLabel6.grid(row=m+8,column=2)
                    e5= Entry(root1,width=50)
                    e5.grid(row=m+9,column=2)
                    def click5():
                        n3=e4.get()
                        if n3=="y":
                            something()
                        else:
                            final()
                elif choice=="4":
                            Label4=Label(root1,text="added to cart")
                            Label4.grid(row=m+7,column=2)
                            item_name.append("Peppy paneer")
                            item_cost.append(450)
                            l.append("Peppy paneer-Rs 450")

                            n=n+1
                            m1.append(n)
                            MyLabel6=Label(root1,text="Do you want to
order more- pls enter y/n:")
                            MyLabel6.grid(row=m+8,column=2)
                            fll=open("c6.dat","wb")
                            pickle.dump(l,fll)
                            fll.close()
                            e6= Entry(root1,width=50)
                            e6.grid(row=m+9,column=2)
                            def click6():
                                nmm=e6.get()
                                if nmm=="y":
                                    something()
                                else:
                                    final()
                            MyButton6=Button(root1,text="submit",comma
nd=click6)
                            MyButton6.grid(row=m+10,column=2)
                elif choice=="5":
                            Label5=Label(root1,text="added to cart")
                            Label5.grid(row=m+7,column=2)
                            item_name.append("Chicken dominator")
                            item_cost.append(350)
                            l.append("Chicken dominator-Rs 350")
                            n=n+1
                            m1.append(n)
                            MyLabel6=Label(root1,text="Do you want to
order more- pls enter y/n:")
                            MyLabel6.grid(row=m+8,column=2)
                            fll=open("c6.dat","wb")
                            pickle.dump(l,fll)
                            fll.close()
                            e7= Entry(root1,width=50)
                            e7.grid(row=m+9,column=2)
                            def click7():
                                nmm=e7.get()
                                if nmm=="y":
                                    something()
                                else:
                                    final()
                            MyButton7=Button(root1,text="submit",comma
nd=click7)
                            MyButton7.grid(row=m+10,column=2)
                elif choice=="6":
                            Label6=Label(root1,text="added to cart")

                            Label6.grid(row=m+7,column=2)
                            item_name.append("Bloody mary pizza")
                            item_cost.append(250)
                            l.append("Bloody mary pizza-Rs 250")
                            n=n+1
                            m1.append(n)
                            MyLabel6=Label(root1,text="Do you want to
order more- pls enter y/n:")
                            MyLabel6.grid(row=m+8,column=2)
                            fll=open("c6.dat","wb")
                            pickle.dump(l,fll)
                            fll.close()
                            e8= Entry(root1,width=50)
                            e8.grid(row=m+9,column=2)
                            def click8():
                                nmm=e8.get()
                                if nmm=="y":
                                    something()
                                else:
                                    final()
                            MyButton8=Button(root1,text="submit",comma
nd=click8)
                            MyButton8.grid(row=m+10,column=2)
                elif choice=="7":
                            Label7=Label(root1,text="added to cart")
                            Label7.grid(row=m+7,column=2)
                            item_name.append("Choco lava cake")
                            item_cost.append(55)
                            l.append("Choco lava cake-Rs 55")
                            n=n+1
                            m1.append(n)
                            MyLabel6=Label(root1,text="Do you want to
order more- pls enter y/n:")
                            MyLabel6.grid(row=m+8,column=2)
                            fll=open("c6.dat","wb")
                            pickle.dump(l,fll)
                            fll.close()
                            e9= Entry(root1,width=50)
                            e9.grid(row=m+9,column=2)
                            def click9():
                                nmm=e9.get()
                                if nmm=="y":
                                    something()
                                else:
                                    final()

                            MyButton9=Button(root1,text="submit",comma
nd=click9)
                            MyButton9.grid(row=m+10,column=2)
                elif choice=="8":
                            Label8=Label(root1,text="added to cart")
                            Label8.grid(row=m+7,column=2)
                            item_name.append("Lasagna")
                            item_cost.append(300)
                            l.append("Lasagna-Rs 300")
                            n=n+1
                            m1.append(n)
                            MyLabel6=Label(root1,text="Do you want to
order more- pls enter y/n:")
                            MyLabel6.grid(row=m+8,column=2)
                            fll=open("c6.dat","wb")
                            pickle.dump(l,fll)
                            fll.close()
                            e10= Entry(root1,width=50)
                            e10.grid(row=m+9,column=2)
                            def click10():
                                nmm=e10.get()
                                if nmm=="y":
                                    something()
                                else:
                                    final()
                            MyButton10=Button(root1,text="submit",comm
and=click10)
                            MyButton10.grid(row=m+10,column=2)
                elif choice=="9":
                            Label9=Label(root1,text="added to cart")
                            Label9.grid(row=m+7,column=2)
                            item_name.append("Garlic bread")
                            item_cost.append(150)
                            l.append("Garlic bread-Rs 150")
                            n=n+1
                            m1.append(n)
                            MyLabel6=Label(root1,text="Do you want to
order more- pls enter y/n:")
                            MyLabel6.grid(row=m+8,column=2)
                            fll=open("c6.dat","wb")
                            pickle.dump(l,fll)
                            fll.close()
                            e11= Entry(root1,width=50)
                            e11.grid(row=m+9,column=2)
                            def click11():
                                nmm=e11.get()

                                if nmm=="y":
                                    something()
                                else:
                                    final()
                            MyButton11=Button(root1,text="submit",comm
and=click11)
                            MyButton11.grid(row=m+10,column=2)
               
            MyButton30=Button(root1,text="add to cart",command=click2)
            MyButton30.grid(row=m+6,column=2)
    root1.mainloop()

bg=Image.open("pii5.png")
resized=bg.resize((1280,720), Image.Resampling.LANCZOS)
bg=ImageTk.PhotoImage(resized)
MyCanvas=Canvas(root,width=1280,height=720)
MyCanvas.pack(fill="both",expand=True)
MyCanvas.create_image(0,0,image=bg,anchor="nw")
BigFont=
Font(family="gabriola",size=42,weight="bold",slant="roman",underline=0
,overstrike=0)
MyCanvas.create_text(680,360,text="Hello! Welcome to Saltiez
Pizzeria.",font=BigFont,fill="white")
OrderButton=Button(root,text="ORDER
NOW",padx=20,command=something,fg="#000000")
OrderButton_window=MyCanvas.create_window(620,450,anchor="nw",window=O
rderButton)

root.mainloop()
from tkinter import *
from PIL import ImageTk,Image
from tkinter.font import Font
root= Tk()
import pickle
item_name=[]
item_cost=[]
l=[]
m1=[]
m2=[]
n=0
nowrun=0

nowrun1=0
nowrun2=0
total=0
e=open("a.dat","ab")
pickle.dump("*",e)
e.close()
w=open("b.dat","ab")
pickle.dump("*",w)
w.close()
z=open("c.dat","wb")
choices=["1. use frequent customer coupon","2. Save to balance"]
pickle.dump(choices,z)
z.close()
q2=open("c2.dat","ab")
pickle.dump("*",q2)
q2.close()
q3=open("c3.dat","ab")
pickle.dump("*",q3)
q3.close()
fl=open("c4.dat","wb")
pickle.dump("*",fl)
fl.close()
f=open("c5.dat","wb")
l1=["1. Maddie&#39;s Margherita pizza-Rs 200","2. Farmhouse pizza -Rs
300","3. Veggie paradise pizza- Rs 300","4. Peppy paneer- Rs 450","5.
Chicken dominator- Rs 350","6. Bloody mary pizza- Rs 250","7. Choco
lava cake- Rs 55","8. Lasagna- Rs 300","9. Garlic Bread- Rs 150"]
pickle.dump(l1,f)
f.close()
fll=open("c6.dat","wb")
pickle.dump("*",fll)
fll.close()

def checkout():
    root3=Tk()
    root3.geometry(f"{width}x{height}+{0}+{0}")
    total=0
    MyLabel2112=Label(root3,text="                                    
                                                                     
                                                                     
      ")
    MyLabel2112.grid(row=0,column=0)
    Font22=Font(family="chiller",size=100,slant="roman")

    MyLabel41=Label(root3,text="\n\n\n\n\n Saltiez
Pizzeria",font=Font22)
    MyLabel41.grid(row=0,column=1)
    MyLabel2299=Label(root3,text="                                    
                                                                     
                                      ")
    MyLabel2299.grid(row=1,column=0)
    MyLabel42=Label(root3,text="Date:")
    MyLabel42.grid(row=1,column=1)
    MyLabel43=Label(root3,text=date1)
    MyLabel43.grid(row=1,column=2)
    for i in range(len(m1)):
        MyLabel3333=Label(root3,text="                                
                                                                     
                                      ")
        MyLabel3333.grid(row=i+2,column=0)
        MyLabel44=Label(root3,text=i+1)
        MyLabel44.grid(row=i+2,column=1)
        MyLabel45=Label(root3,text=item_name[i])
        MyLabel45.grid(row=i+2,column=2)
        bc="Rs"+str(item_cost[i])
        MyLabel46=Label(root3,text=bc)
        MyLabel46.grid(row=i+2,column=3)
        total=total+item_cost[i]
    MyLabel4444=Label(root3,text="                                    
                                                                     
                                                                     
      ")
    MyLabel4444.grid(row=len(m1)+3,column=0)
    a="Total cost= Rs"+str(total)
    MyLabel47=Label(root3,text=a)
    MyLabel47.grid(row=len(m1)+2,column=1)
    MyLabel5555=Label(root3,text="                                    
                                                                     
                                                                     
      ")
    MyLabel5555.grid(row=len(m1)+3,column=0)
    MyLabel48=Label(root3,text="Thank you, please visit again")
    MyLabel48.grid(row=len(m1)+3,column=1)

def freq():
    root3=Tk()
    root3.geometry(f"{width}x{height}+{0}+{0}")
    total=0
    e=open("a.dat","rb")

    ss=pickle.load(e)
    e.close()
    if ss=="*":
        Font22=Font(family="chiller",size=100,slant="roman")
        MyLabel41=Label(root3,text="\n\n\n\n Saltiez
Pizzeria",font=Font22)
        MyLabel41.grid(row=0,column=1)
        MyLabel2299=Label(root3,text="                                
                                                                     
                                          ")
        MyLabel2299.grid(row=1,column=0)
        MyLabel42=Label(root3,text="Date:")
        MyLabel42.grid(row=1,column=1)
        MyLabel43=Label(root3,text=date1)
        MyLabel43.grid(row=1,column=2)
        for i in range(len(m1)):
            MyLabel3333=Label(root3,text="                            
                                                                     
                                          ")
            MyLabel3333.grid(row=i+2,column=0)
            MyLabel44=Label(root3,text=i+1)
            MyLabel44.grid(row=i+2,column=1)
            MyLabel45=Label(root3,text=item_name[i])
            MyLabel45.grid(row=i+2,column=2)
            bc="Rs"+str(item_cost[i])
            MyLabel46=Label(root3,text=bc)
            MyLabel46.grid(row=i+2,column=3)
            total=total+item_cost[i]
        MyLabel4444=Label(root3,text="                                
                                                                     
                                                                     
          ")
        MyLabel4444.grid(row=len(m1)+3,column=0)
        total=total-(10/100)*total
        a="Total cost= Rs"+str(total)
        MyLabel47=Label(root3,text=a)
        MyLabel47.grid(row=len(m1)+2,column=1)
        MyLabel5555=Label(root3,text="                                
                                                                     
                                                                     
          ")
        MyLabel5555.grid(row=len(m1)+3,column=0)
        MyLabel48=Label(root3,text="Thank you, please visit again")
        MyLabel48.grid(row=len(m1)+3,column=1)
    else:

        MyLabel26=Label(root3,text="Do you want to use the money in
your balance account:")
        MyLabel26.pack()
        e9=Entry(root3,width=50)
        e9.pack()
        def click7():
            total=0
            choice2=e9.get()
            if choice2=="y":
                root70=Tk()
                root70.geometry(f"{width}x{height}+{0}+{0}")
                Font22=Font(family="chiller",size=100,slant="roman")
                MyLabel41=Label(root70,text="\n\n\n\n Saltiez
Pizzeria",font=Font22)
                MyLabel41.grid(row=0,column=1)
                MyLabel2299=Label(root70,text="                      
                                                                     
                                                    ")
                MyLabel2299.grid(row=1,column=0)
                MyLabel42=Label(root70,text="Date:")
                MyLabel42.grid(row=1,column=1)
                MyLabel43=Label(root70,text=date1)
                MyLabel43.grid(row=1,column=2)
                m2.append(1)
                for i in range(len(m1)):
                    MyLabel3333=Label(root70,text="                  
                                                                     
                                                    ")
                    MyLabel3333.grid(row=i+2,column=0)
                    MyLabel44=Label(root70,text=i+1)
                    MyLabel44.grid(row=i+2,column=1)
                    MyLabel45=Label(root70,text=item_name[i])
                    MyLabel45.grid(row=i+2,column=2)
                    bc="Rs"+str(item_cost[i])
                    MyLabel46=Label(root70,text=bc)
                    MyLabel46.grid(row=i+2,column=3)
                    total=total+item_cost[i]
                MyLabel4444=Label(root70,text="                      
                                                                     
                                                                     
                    ")
                MyLabel4444.grid(row=len(m1)+3,column=0)
                gg=int(ss)
                total=total-gg
                e=open("a.dat","wb")
                pickle.dump("*",e)

                e.close()
                a="Total cost= Rs"+str(total)
                MyLabel47=Label(root70,text=a)
                MyLabel47.grid(row=len(m1)+2,column=1)
                MyLabel5555=Label(root70,text="                      
                                                                     
                                                                     
                    ")
                MyLabel5555.grid(row=len(m1)+3,column=0)
                MyLabel48=Label(root70,text="Thank you, please visit
again")
                MyLabel48.grid(row=len(m1)+3,column=1)
                root70.mainloop()
            else:
                root70=Tk()
                root70.geometry(f"{width}x{height}+{0}+{0}")
                Font22=Font(family="chiller",size=100,slant="roman")
                MyLabel41=Label(root70,text="\n\n\n\n Saltiez
Pizzeria",font=Font22)
                MyLabel41.grid(row=0,column=1)
                MyLabel2299=Label(root70,text="                      
                                                                     
                                                    ")
                MyLabel2299.grid(row=1,column=0)
                MyLabel42=Label(root70,text="Date:")
                MyLabel42.grid(row=1,column=1)
                MyLabel43=Label(root70,text=date1)
                MyLabel43.grid(row=1,column=2)
                for i in range(len(m1)):
                    MyLabel3333=Label(root70,text="                  
                                                                     
                                                    ")
                    MyLabel3333.grid(row=i+2,column=0)
                    MyLabel44=Label(root70,text=i+1)
                    MyLabel44.grid(row=i+2,column=1)
                    MyLabel45=Label(root70,text=item_name[i])
                    MyLabel45.grid(row=i+2,column=2)
                    bc="Rs"+str(item_cost[i])
                    MyLabel46=Label(root70,text=bc)
                    MyLabel46.grid(row=i+2,column=3)
                    total=total+item_cost[i]
                MyLabel4444=Label(root70,text="                      
                                                                     
                                                                     
                    ")
                MyLabel4444.grid(row=len(m1)+3,column=0)

                a="Total cost= Rs"+str(total)
                MyLabel47=Label(root70,text=a)
                MyLabel47.grid(row=len(m1)+2,column=1)
                MyLabel5555=Label(root70,text="                      
                                                                     
                                                                     
                    ")
                MyLabel5555.grid(row=len(m1)+3,column=0)
                MyLabel48=Label(root70,text="Thank you, please visit
again")
                MyLabel48.grid(row=len(m1)+3,column=1)
                root70.mainloop()
        MyButton17=Button(root3,text="checkout",command=click7)
        MyButton17.pack()
        root3.mainloop()
def previous():
    pr=open("c7.dat","ab")
    pickle.dump("*",pr)
    pr.close()
    try:
        pr=open("c7.dat","rb")
        m=pickle.load(pr)
        pr.close()
        if m=="*":
            root5=Tk()
            root5.geometry(f"{width}x{height}+{0}+{0}")
            global nowrun
            nowrun+=1
            c=open("c1.dat","wb")
            pickle.dump(nowrun,c)
            c.close()
            MyLabel171=Label(root5,text="\n\n\n\n\n Sorry no coupons
are available right now")
            MyLabel171.pack()
            pr=open("c7.dat","wb")
            pickle.dump(l,pr)
            pr.close()
            def click109():
                root5.destroy()
            MyButton173=Button(root5,text="Home
Page",command=click109)
            MyButton173.pack()
            MyButton777=Button(root5,text="checkout",command=checkout)
            MyButton777.pack()
            root5.mainloop()

        else:
            c=open("c1.dat","rb")
            jj=pickle.load(c)
            c.close()
            jj+=1
            nowrun=jj
            c=open("c1.dat","wb")
            pickle.dump(nowrun,c)
            c.close()
            if nowrun==2:
                root6=Tk()
                root6.geometry(f"{width}x{height}+{0}+{0}")
                MyLabel172=Label(root6,text="\n\n\n\n\n Sorry no
coupons are available right now")
                MyLabel172.pack()
                def click112():
                    root6.destroy()
                MyButton174=Button(root6,text="Home
Page",command=click112)
                MyButton174.pack()
                MyButton778=Button(root6,text="checkout",command=check
out)
                MyButton778.pack()
                root6.mainloop()
            elif nowrun&gt;2:
                w=open("b.dat","rb")
                kl=pickle.load(w)
                w.close()
                if kl=="*":
                    q3=open("c3.dat","rb")
                    mn=pickle.load(q3)
                    q3.close()
                    if mn=="*":
                        root3=Tk()
                        root3.geometry(f"{width}x{height}+{0}+{0}")
                        MyLabel7=Label(root3,text="\n\n\n\n\n you are
a frequent customer")
                        MyLabel7.pack()
                        MyLabel8=Label(root3,text="showing your
choices:")
                        MyLabel8.pack()
                        try:
                            z=open("c.dat","rb")
                            qwe=pickle.load(z)
                            for x in qwe:
                                MyLabel9=Label(root3,text=x)

                                MyLabel9.pack()
                        except EOFError:
                            z.close()
                        MyLabel14=Label(root3,text="enter your choice-
1/2:")
                        MyLabel14.pack()
                        e8=Entry(root3,width=50)
                        e8.pack()
                        def click5():
                            choice1=e8.get()
                            q4=open(&#39;c8.dat&#39;,&#39;wb&#39;)
                            pickle.dump(choice1,q4)
                            q4.close()
                            q3=open("c3.dat","wb")
                            pickle.dump("##",q3)
                            q3.close()
                            q4=open("c8.dat",&#39;rb&#39;)
                            mk=pickle.load(q4)
                            ms=int(mk)
                            q4.close()
                            if ms==1:
                                freq()
                                w=open("b.dat","wb")
                                pickle.dump("used",w)
                                w.close()
                            else:
                                global total
                                for i in range(len(m1)):
                                    total=total+item_cost[i]
                                total=(10/100)*total
                                e=open("a.dat","wb")
                                pickle.dump(total,e)
                                e.close()
                                root25=Tk()
                                root25.geometry(f"{width}x{height}+{0}
+{0}")
                                MyLabel10=Label(root25,text="\n\n\n\n\
n saving to your balance")
                                MyLabel10.pack()
                                MyButton9999=Button(root25,text="click
to look at final details",command=checkout)
                                MyButton9999.pack()
                                root25.mainloop()
                        MyButton111=Button(root3,text="checkout",comma
nd=click5)
                        MyButton111.pack()

                        root3.mainloop()
                    else:
                        freq()
                        if len(m2)==1:
                            w=open("b.dat","wb")
                            pickle.dump("used",w)
                            w.close()
                        else:
                            q2=open("c2.dat","rb")
                            ds=pickle.load(q2)
                            q2.close()
                            if ds=="*":
                                q2=open("c2.dat","wb")
                                pickle.dump("*",q2)
                                q2.close()
                            else:
                               freq()
                else:
                    root7=Tk()
                    root7.geometry(f"{width}x{height}+{0}+{0}")
                    MyLabel17221=Label(root7,text="\n\n\n\n\n Sorry no
coupons are available right now")
                    MyLabel17221.pack()
                    MyButton779=Button(root7,text="checkout",command=c
heckout)
                    MyButton779.pack()
                    root7.mainloop()
    except EOFError:
        pr.close()
def no():
    pr2=open("c9.dat","wb")
    pickle.dump(l,pr2)
    pr2.close()
def previous2():
    global nowrun1
    pr2=open("c9.dat","ab")
    pickle.dump("*",pr2)
    pr2.close()
    try:
            pr2=open("c9.dat","rb")
            m=pickle.load(pr2)
            pr2.close()
            if m=="*":
                root7=Tk()

                root7.geometry(f"{width}x{height}+{0}+{0}")
                nowrun1+=1
                pr2=open("c9.dat","wb")
                pickle.dump(l,pr2)
                pr2.close()
                font221=Font(family="Banschrift",size=20,slant="roman"
)
                MyLabel21=Label(root7,text="\n\n\n\n\n\n Welcome New
                Customer!",font=font221)
                MyLabel21.pack()
                def click122():
                    root7.destroy()
                MyButton177=Button(root7,text="Home
Page",command=click122)
                MyButton177.pack()
                root7.mainloop()
            else:
                root4=Tk()
                root4.geometry(f"{width}x{height}+{0}+{0}")
                MyLabel11=Label(root4,text="\n\n\n\n\n Showing your
previous orders:")
                MyLabel11.pack()
                pr2=open("c9.dat","rb")
                oo=pickle.load(pr2)
                for y in oo:
                    MyLabel12=Label(root4,text=y)
                    MyLabel12.pack()
                pr2.close()
                pr2=open("c9.dat","wb")
                pickle.dump(l,pr2)
                pr2.close()
                def click123():
                    root4.destroy()
                MyButton178=Button(root4,text="Home
Page",command=click123)
                MyButton178.pack()
                root4.mainloop()
    except EOFError:
            pr2.close()
def final():
    root3=Tk()
    root3.geometry(f"{width}x{height}+{0}+{0}")
    MyLabel50=Label(root3,text="\n\n\n\n\n Do you want to see your
previous orders?")
    MyLabel50.pack()

    def click100():
        previous2()
    def click101():
        root66=Tk()
        root66.geometry(f"{width}x{height}+{0}+{0}")
        MyLabel222=Label(root66,text="\n\n\n\n\n\n\n\n\n\n ok,please
visit again")
        MyLabel222.pack()
        def click345():
            root66.destroy()
        MyButton9990009=Button(root66,text="Home
Page",command=click345)
        MyButton9990009.pack()
        no()
    MyButton990=Button(root3,text="yes",command=click100)
    MyButton990.pack()
    MyButton991=Button(root3,text="no",command=click101)
    MyButton991.pack()
    MyLabel11000=Label(root3,text="Please check for available coupons
before proceeding to checkout:")
    MyLabel11000.pack()
    def click102():
        previous()
    MyButton992=Button(root3,text="coupons",command=click102)
    MyButton992.pack()
    root3.mainloop()

import datetime as dt
date1=dt.date.today()
width=1280
height=720
root.geometry(f"{width}x{height}+{0}+{0}")

def something():
    root1=Tk()
    def comm():
        rootcart=Tk()
        rootcart.geometry(f"{width}x{height}+{0}+{0}")
        try:
            fll=open("c6.dat","rb")
            rr=pickle.load(fll)
        except EOFError:

            fll.close()
        if rr=="*":
            MyLabel5=Label(rootcart,text="\n\n\n\n\n\n\n\n\n you have
            no items in your cart yet")
            MyLabel5.pack()
        else:
            for i in rr:
                MyLabel4=Label(rootcart,text=i)
                MyLabel4.pack()
        def click172():
            rootcart.destroy()
        MyButton2221=Button(rootcart,text="Home
Page",command=click172)
        MyButton2221.pack()
        rootcart.mainloop()
    Buttoncart=Button(root1,text="cart",command=comm)
    Buttoncart.grid(row=0,column=0)
    MyLabel771=Label(root1,text="                                    
                                                                     
                                                ")
    MyLabel771.grid(row=1,column=1)
    fl=open("c4.dat","rb")
    kk=pickle.load(fl)
    fl.close()
    Font2=Font(family="Times",size=10)
    root1.geometry(f"{width}x{height}+{0}+{0}")
    if kk=="*":
        root.destroy()
        fl=open("c4.dat","wb")
        pickle.dump("##",fl)
        fl.close()
        MyLabel1=Label(root1, text="Do you want to start adding to
cart- y/n:",font=Font2)
        MyLabel1.grid(row=2,column=2)
        MyLabel333=Label(root1,text="\n")
        MyLabel333.grid(row=2,column=0)
        e1= Entry(root1, width=30)
        e1.grid(row=3,column=2)
        def click():
            ord=e1.get()
            if ord=="y":
                MyLabel2=Label(root1, text="Showing your options:")
                MyLabel2.grid(row=5,column=2)
                try:
                    f=open("c5.dat","rb")
                    d=pickle.load(f)

                    m=len(d)
                    for i in range(0,m):
                        MyLabel3=Label(root1, text=d[i])
                        MyLabel3.grid(row=i+6,column=2)
                except EOFError:
                    f.close()
                for i in range(0,1):
                    MyLabel3=Label(root1,text="Enter the number of the
desired item : ")
                    MyLabel3.grid(row=m+7,column=2)
                    e2= Entry(root1, width=50)
                    e2.grid(row=m+8,column=2)
                    def click2():
                        choice=e2.get()
                        if choice=="1":
                            global n
                            Label1=Label(root1,text="added to cart")
                            Label1.grid(row=m+10,column=2)
                            item_name.append("Maddie&#39;s Margherita
pizza")
                            item_cost.append(200)
                            l.append("Maddie&#39;s Margherita pizza-Rs
200")
                            fll=open("c6.dat","wb")
                            pickle.dump(l,fll)
                            fll.close()
                            n=n+1
                            m1.append(n)
                            MyLabel5=Label(root1,text="Do you want to
order more- pls enter y/n:")
                            MyLabel5.grid(row=m+11,column=2)
                            e3= Entry(root1,width=50)
                            e3.grid(row=m+12,column=2)
                            def click3():
                                n1= e3.get()
                                if n1=="y":
                                    something()
                                else:
                                    final()
                            MyButton3=Button(root1,text="Submit",comma
nd=click3)
                            MyButton3.grid(row=m+13,column=2)
                        elif choice=="2":
                            Label2=Label(root1,text="added to cart")
                            Label2.grid(row=m+10,column=2)
                            item_name.append("Farmhouse pizza")

                            item_cost.append(300)
                            l.append("Farmhouse pizza-Rs 300")
                            n=n+1
                            m1.append(n)
                            fll=open("c6.dat","wb")
                            pickle.dump(l,fll)
                            fll.close()
                            MyLabel6=Label(root1,text="Do you want to
order more- pls enter y/n:")
                            MyLabel6.grid(row=m+11,column=2)
                            e4= Entry(root1,width=50)
                            e4.grid(row=m+12,column=2)
                            def click4():
                                n2=e4.get()
                                if n2=="y":
                                    something()
                                else:
                                    final()
                            MyButton4=Button(root1,text="submit",comma
nd=click4)
                            MyButton4.grid(row=m+13,column=2)
                        elif choice=="3":
                            Label3=Label(root1,text="added to cart")
                            Label3.grid(row=m+10,column=2)
                            item_name.append("Veggie paradise pizza")
                            item_cost.append(300)
                            l.append("Veggie paradise pizza-Rs 300")
                            n=n+1
                            m1.append(n)
                            MyLabel6=Label(root1,text="Do you want to
order more- pls enter y/n:")
                            MyLabel6.grid(row=m+11,column=2)
                            fll=open("c6.dat","wb")
                            pickle.dump(l,fll)
                            fll.close()
                            e5= Entry(root1,width=50)
                            e5.grid(row=m+12,column=2)
                            def click5():
                                n3=e5.get()
                                if n3=="y":
                                    something()
                                else:
                                    final()
                            MyButton5=Button(root1,text="submit",comma
nd=click5)
                            MyButton5.grid(row=m+13,column=2)

                        elif choice=="4":
                            Label4=Label(root1,text="added to cart")
                            Label4.grid(row=m+10,column=2)
                            item_name.append("Peppy paneer")
                            item_cost.append(450)
                            l.append("Peppy paneer-Rs 450")
                            n=n+1
                            m1.append(n)
                            MyLabel6=Label(root1,text="Do you want to
order more- pls enter y/n:")
                            MyLabel6.grid(row=m+11,column=2)
                            fll=open("c6.dat","wb")
                            pickle.dump(l,fll)
                            fll.close()
                            e6= Entry(root1,width=50)
                            e6.grid(row=m+12,column=2)
                            def click6():
                                nmm=e6.get()
                                if nmm=="y":
                                    something()
                                else:
                                    final()
                            MyButton6=Button(root1,text="submit",comma
nd=click6)
                            MyButton6.grid(row=m+13,column=2)
                        elif choice=="5":
                            Label5=Label(root1,text="added to cart")
                            Label5.grid(row=m+10,column=2)
                            item_name.append("Chicken dominator")
                            item_cost.append(350)
                            l.append("Chicken dominator-Rs 350")
                            n=n+1
                            m1.append(n)
                            MyLabel6=Label(root1,text="Do you want to
order more- pls enter y/n:")
                            MyLabel6.grid(row=m+11,column=2)
                            fll=open("c6.dat","wb")
                            pickle.dump(l,fll)
                            fll.close()
                            e7= Entry(root1,width=50)
                            e7.grid(row=m+12,column=2)
                            def click7():
                                nmm=e7.get()
                                if nmm=="y":
                                    something()
                                else:

                                    final()
                            MyButton7=Button(root1,text="submit",comma
nd=click7)
                            MyButton7.grid(row=m+13,column=2)
                        elif choice=="6":
                            Label6=Label(root1,text="added to cart")
                            Label6.grid(row=m+10,column=2)
                            item_name.append("Bloody mary pizza")
                            item_cost.append(250)
                            l.append("Bloody mary pizza-Rs 250")
                            n=n+1
                            m1.append(n)
                            MyLabel6=Label(root1,text="Do you want to
order more- pls enter y/n:")
                            MyLabel6.grid(row=m+11,column=2)
                            fll=open("c6.dat","wb")
                            pickle.dump(l,fll)
                            fll.close()
                            e8= Entry(root1,width=50)
                            e8.grid(row=m+12,column=2)
                            def click8():
                                nmm=e8.get()
                                if nmm=="y":
                                    something()
                                else:
                                    final()
                            MyButton8=Button(root1,text="submit",comma
nd=click8)
                            MyButton8.grid(row=m+13,column=2)
                        elif choice=="7":
                            Label7=Label(root1,text="added to cart")
                            Label7.grid(row=m+10,column=2)
                            item_name.append("Choco lava cake")
                            item_cost.append(55)
                            l.append("Choco lava cake-Rs 55")
                            n=n+1
                            m1.append(n)
                            MyLabel6=Label(root1,text="Do you want to
order more- pls enter y/n:")
                            MyLabel6.grid(row=m+11,column=2)
                            fll=open("c6.dat","wb")
                            pickle.dump(l,fll)
                            fll.close()
                            e9= Entry(root1,width=50)
                            e9.grid(row=m+12,column=2)
                            def click9():

                                nmm=e9.get()
                                if nmm=="y":
                                    something()
                                else:
                                    final()
                            MyButton9=Button(root1,text="submit",comma
nd=click9)
                            MyButton9.grid(row=m+13,column=2)
                        elif choice=="8":
                            Label8=Label(root1,text="added to cart")
                            Label8.grid(row=m+10,column=2)
                            item_name.append("Lasagna")
                            item_cost.append(300)
                            l.append("Lasagna-Rs 300")
                            n=n+1
                            m1.append(n)
                            MyLabel6=Label(root1,text="Do you want to
order more- pls enter y/n:")
                            MyLabel6.grid(row=m+11,column=2)
                            fll=open("c6.dat","wb")
                            pickle.dump(l,fll)
                            fll.close()
                            e10= Entry(root1,width=50)
                            e10.grid(row=m+12,column=2)
                            def click10():
                                nmm=e10.get()
                                if nmm=="y":
                                    something()
                                else:
                                    final()
                            MyButton10=Button(root1,text="submit",comm
and=click10)
                            MyButton10.grid(row=m+13,column=2)
                        elif choice=="9":
                            Label9=Label(root1,text="added to cart")
                            Label9.grid(row=m+10,column=2)
                            item_name.append("Garlic bread")
                            item_cost.append(150)
                            l.append("Garlic bread-Rs 150")
                            n=n+1
                            m1.append(n)
                            MyLabel6=Label(root1,text="Do you want to
order more- pls enter y/n:")
                            MyLabel6.grid(row=m+11,column=2)
                            fll=open("c6.dat","wb")
                            pickle.dump(l,fll)

                            fll.close()
                            e11= Entry(root1,width=50)
                            e11.grid(row=m+12,column=2)
                            def click11():
                                nmm=e11.get()
                                if nmm=="y":
                                    something()
                                else:
                                    final()
                            MyButton11=Button(root1,text="submit",comm
and=click11)
                            MyButton11.grid(row=m+13,column=2)
                    MyButton30=Button(root1,text="add to
cart",command=click2)
                    MyButton30.grid(row=m+9,column=2)
            elif ord==n:
                MyLabel4=Label(root1,text="Thank you, please visit
again")
                MyLabel4.grid(row=4,column=0)
            else:
                MyLabel700=Label(root1,text="wrong entry")
                MyLabel700.pack()
        MyButton=Button(root1,text="Submit",command=click)
        MyButton.grid(row=4,column=2)
    else:
        MyLabel2=Label(root1,text="Showing your options:")
        MyLabel2.grid(row=2,column=2)
        try:
            f=open("c5.dat","rb")
            d=pickle.load(f)
            m=len(d)
            for i in range(0,m):
                MyLabel3=Label(root1, text=d[i])
                MyLabel3.grid(row=i+3,column=2)
        except EOFError:
            f.close()
        for i in range(0,1):
            MyLabel3=Label(root1,text="Enter the number of the desired
item : ")
            MyLabel3.grid(row=m+4,column=2)
            e2= Entry(root1, width=50)
            e2.grid(row=m+5,column=2)
            def click2():
                choice=e2.get()
                if choice=="1":
                    global n

                    Label1=Label(root1,text="added to cart")
                    Label1.grid(row=m+7,column=2)
                    item_name.append("Maddie&#39;s Margherita pizza")
                    item_cost.append(200)
                    l.append("Maddie&#39;s Margherita pizza-rs 200")
                    n=n+1
                    m1.append(n)
                    fll=open("c6.dat","wb")
                    pickle.dump(l,fll)
                    fll.close()
                    MyLabel5=Label(root1,text="Do you want to order
more- pls enter y/n:")
                    MyLabel5.grid(row=m+8,column=2)
                    e3= Entry(root1,width=50)
                    e3.grid(row=m+9,column=2)
                    def click3():
                        nm= e3.get()
                        if nm=="y":
                            something()
                        else:
                            final()
                    MyButton3=Button(root1,text="Submit",command=click
3)
                    MyButton3.grid(row=m+10,column=2)
                elif choice=="2":
                    Label2=Label(root1,text="added to cart")
                    Label2.grid(row=m+7,column=2)
                    item_name.append("Farmhouse pizza")
                    item_cost.append(300)
                    l.append("Farmhouse pizza-Rs 300")
                    n=n+1
                    m1.append(n)
                    fll=open("c6.dat","wb")
                    pickle.dump(l,fll)
                    fll.close()
                    MyLabel6=Label(root1,text="Do you want to order
more- pls enter y/n:")
                    MyLabel6.grid(row=m+8,column=2)
                    e4= Entry(root1,width=50)
                    e4.grid(row=m+9,column=2)
                    def click4():
                        nmm=e4.get()
                        if nmm=="y":
                            something()
                        else:
                            final()

                    MyButton4=Button(root1,text="submit",command=click
4)
                    MyButton4.grid(row=m+10,column=2)
                elif choice=="3":
                    Label3=Label(root1,text="added to cart")
                    Label3.grid(row=m+7,column=2)
                    item_name.append("Veggie paradise pizza")
                    item_cost.append(300)
                    l.append("Veggie Paradise Pizza-Rs 300")
                    n=n+1
                    m1.append(n)
                    MyLabel6=Label(root1,text="Do you want to order
more- pls enter y/n:")
                    MyLabel6.grid(row=m+8,column=2)
                    e5= Entry(root1,width=50)
                    e5.grid(row=m+9,column=2)
                    def click5():
                        n3=e4.get()
                        if n3=="y":
                            something()
                        else:
                            final()
                elif choice=="4":
                            Label4=Label(root1,text="added to cart")
                            Label4.grid(row=m+7,column=2)
                            item_name.append("Peppy paneer")
                            item_cost.append(450)
                            l.append("Peppy paneer-Rs 450")
                            n=n+1
                            m1.append(n)
                            MyLabel6=Label(root1,text="Do you want to
order more- pls enter y/n:")
                            MyLabel6.grid(row=m+8,column=2)
                            fll=open("c6.dat","wb")
                            pickle.dump(l,fll)
                            fll.close()
                            e6= Entry(root1,width=50)
                            e6.grid(row=m+9,column=2)
                            def click6():
                                nmm=e6.get()
                                if nmm=="y":
                                    something()
                                else:
                                    final()
                            MyButton6=Button(root1,text="submit",comma
nd=click6)

                            MyButton6.grid(row=m+10,column=2)
                elif choice=="5":
                            Label5=Label(root1,text="added to cart")
                            Label5.grid(row=m+7,column=2)
                            item_name.append("Chicken dominator")
                            item_cost.append(350)
                            l.append("Chicken dominator-Rs 350")
                            n=n+1
                            m1.append(n)
                            MyLabel6=Label(root1,text="Do you want to
order more- pls enter y/n:")
                            MyLabel6.grid(row=m+8,column=2)
                            fll=open("c6.dat","wb")
                            pickle.dump(l,fll)
                            fll.close()
                            e7= Entry(root1,width=50)
                            e7.grid(row=m+9,column=2)
                            def click7():
                                nmm=e7.get()
                                if nmm=="y":
                                    something()
                                else:
                                    final()
                            MyButton7=Button(root1,text="submit",comma
nd=click7)
                            MyButton7.grid(row=m+10,column=2)
                elif choice=="6":
                            Label6=Label(root1,text="added to cart")
                            Label6.grid(row=m+7,column=2)
                            item_name.append("Bloody mary pizza")
                            item_cost.append(250)
                            l.append("Bloody mary pizza-Rs 250")
                            n=n+1
                            m1.append(n)
                            MyLabel6=Label(root1,text="Do you want to
order more- pls enter y/n:")
                            MyLabel6.grid(row=m+8,column=2)
                            fll=open("c6.dat","wb")
                            pickle.dump(l,fll)
                            fll.close()
                            e8= Entry(root1,width=50)
                            e8.grid(row=m+9,column=2)
                            def click8():
                                nmm=e8.get()
                                if nmm=="y":
                                    something()

                                else:
                                    final()
                            MyButton8=Button(root1,text="submit",comma
nd=click8)
                            MyButton8.grid(row=m+10,column=2)
                elif choice=="7":
                            Label7=Label(root1,text="added to cart")
                            Label7.grid(row=m+7,column=2)
                            item_name.append("Choco lava cake")
                            item_cost.append(55)
                            l.append("Choco lava cake-Rs 55")
                            n=n+1
                            m1.append(n)
                            MyLabel6=Label(root1,text="Do you want to
order more- pls enter y/n:")
                            MyLabel6.grid(row=m+8,column=2)
                            fll=open("c6.dat","wb")
                            pickle.dump(l,fll)
                            fll.close()
                            e9= Entry(root1,width=50)
                            e9.grid(row=m+9,column=2)
                            def click9():
                                nmm=e9.get()
                                if nmm=="y":
                                    something()
                                else:
                                    final()
                            MyButton9=Button(root1,text="submit",comma
nd=click9)
                            MyButton9.grid(row=m+10,column=2)
                elif choice=="8":
                            Label8=Label(root1,text="added to cart")
                            Label8.grid(row=m+7,column=2)
                            item_name.append("Lasagna")
                            item_cost.append(300)
                            l.append("Lasagna-Rs 300")
                            n=n+1
                            m1.append(n)
                            MyLabel6=Label(root1,text="Do you want to
order more- pls enter y/n:")
                            MyLabel6.grid(row=m+8,column=2)
                            fll=open("c6.dat","wb")
                            pickle.dump(l,fll)
                            fll.close()
                            e10= Entry(root1,width=50)
                            e10.grid(row=m+9,column=2)

                            def click10():
                                nmm=e10.get()
                                if nmm=="y":
                                    something()
                                else:
                                    final()
                            MyButton10=Button(root1,text="submit",comm
and=click10)
                            MyButton10.grid(row=m+10,column=2)
                elif choice=="9":
                            Label9=Label(root1,text="added to cart")
                            Label9.grid(row=m+7,column=2)
                            item_name.append("Garlic bread")
                            item_cost.append(150)
                            l.append("Garlic bread-Rs 150")
                            n=n+1
                            m1.append(n)
                            MyLabel6=Label(root1,text="Do you want to
order more- pls enter y/n:")
                            MyLabel6.grid(row=m+8,column=2)
                            fll=open("c6.dat","wb")
                            pickle.dump(l,fll)
                            fll.close()
                            e11= Entry(root1,width=50)
                            e11.grid(row=m+9,column=2)
                            def click11():
                                nmm=e11.get()
                                if nmm=="y":
                                    something()
                                else:
                                    final()
                            MyButton11=Button(root1,text="submit",comm
and=click11)
                            MyButton11.grid(row=m+10,column=2)
               
            MyButton30=Button(root1,text="add to cart",command=click2)
            MyButton30.grid(row=m+6,column=2)
    root1.mainloop()

bg=Image.open("pii5.png")
resized=bg.resize((1280,720), Image.Resampling.LANCZOS)
bg=ImageTk.PhotoImage(resized)
MyCanvas=Canvas(root,width=1280,height=720)

MyCanvas.pack(fill="both",expand=True)
MyCanvas.create_image(0,0,image=bg,anchor="nw")
BigFont=
Font(family="gabriola",size=42,weight="bold",slant="roman",underline=0
,overstrike=0)
MyCanvas.create_text(680,360,text="Hello! Welcome to Saltiez
Pizzeria.",font=BigFont,fill="white")
OrderButton=Button(root,text="ORDER
NOW",padx=20,command=something,fg="#000000")
OrderButton_window=MyCanvas.create_window(620,450,anchor="nw",window=O
rderButton)

root.mainloop()