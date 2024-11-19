from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import ttk
import random
import datetime
from tkinter import messagebox
import mysql.connector
class MainPage:
    def __init__(self, root, username):
        self.root = root
        
        # Display the username on the main program window
       
        
        self.root.title("Finance Management System")
        self.root.geometry("1540x800+0+0")
        
        self.date=StringVar()
        self.asset_id=IntVar()
        self.asset_name=StringVar()
        self.asset_type=StringVar()
        self.asset_value=DoubleVar()
        self.liab_id=IntVar()
        self.liab_name=StringVar()
        self.liab_type=StringVar()
        self.liab_value=DoubleVar()
        
        
        
        lbltitle=Label(self.root,bd=5,relief=RIDGE,text="Finance Management System",fg="red",bg="Yellow",
                                                                                                        font=("times new roman",35,"bold"))
        lbltitle.pack(side=TOP,fill=X)
        
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=70,width=1300,height=350)
        
        DataFrameLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("arial",12,"bold"),text="Data Entry",fg="black",bg="#FAEED1")
        DataFrameLeft.place(x=0,y=0,width=900,height=330)
    
        DataFrameRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=5,
                                font=("arial",12,"bold"),text="Balance Sheet",bg="green",fg="white")
        DataFrameRight.place(x=440,y=0,width=900,height=330)
        
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=430,width=1300,height=100)
        
        btn_logout = Button(root, text="Logout", command=self.logout,bg="#00FFAB",font=("arial",20,"bold"))
        btn_logout.place(x=1160,y=5)
        
        iDetailsframe=Frame(self.root,bd=20,relief=RIDGE)
        iDetailsframe.place(x=0,y=500,width=650,height=150)
        lDetailsframe=Frame(self.root,bd=20,relief=RIDGE)
        lDetailsframe.place(x=650,y=500,width=620,height=150)
        
        lblasset=Label(DataFrameLeft,text="Asset ",font=("arial",15,"bold"),fg="brown",padx=0,pady=4,bg="#FAEED1")
        lblasset.grid(row=0,column=0, sticky=W)
        
        lblassetname=Label(DataFrameLeft,font=("arial",12,"bold"),text="Asset name: ",padx=2,bg="#FAEED1")
        lblassetname.grid(row=1,column=0,sticky=W)
        txtassetname=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.asset_name,width=31)
        txtassetname.grid(row=1,column=1)
        
        lblassettype=Label(DataFrameLeft,font=("arial",12,"bold"),text="Asset Type: ",padx=2,pady=2,bg="#FAEED1")
        lblassettype.grid(row=3,column=0,sticky=W)
        comNametablet=ttk.Combobox(DataFrameLeft,textvariable=self.asset_type,font=("times new roman",12,"bold"),width=33)
        comNametablet["values"]=("Cash & Cash Equivanlent", "Accounts Recievable", "Inventory", "Prepaid Expenses", "Property, Plant & Equipment", "Intangible Assets", "Investments", "Long-Term Recievables", "Deferred Tax Assets")
        comNametablet.current(0)
        comNametablet.grid(row=3,column=1)
        
        lblassetvalue=Label(DataFrameLeft,font=("arial",12,"bold"),text="Asset Value: ",padx=2,pady=2,bg="#FAEED1")
        lblassetvalue.grid(row=4,column=0,sticky=W)
        txtassetvalue=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.asset_value,width=31)
        txtassetvalue.grid(row=4,column=1)
        
        lblassetdate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date: ",padx=2,pady=2,bg="#FAEED1")
        lblassetdate.grid(row=5,column=0,sticky=W)
        txtassetdate=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.date,width=31)
        txtassetdate.grid(row=5,column=1)
        
       
        lblliabname=Label(DataFrameLeft,font=("arial",15,"bold"),text="Liability ",fg="brown",padx=0,pady=4,bg="#FAEED1")
        lblliabname.grid(row=6,column=0,sticky=W)
        
        lblliabname=Label(DataFrameLeft,font=("arial",12,"bold"),text="Liab Name: ",padx=2,bg="#FAEED1")
        lblliabname.grid(row=7,column=0,sticky=W)
        txtliabname=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.liab_name,width=31)
        txtliabname.grid(row=7,column=1)
       
        lblliabtype=Label(DataFrameLeft,font=("arial",12,"bold"),text="Liab Type: ",padx=2,pady=2,bg="#FAEED1")
        lblliabtype.grid(row=8,column=0,sticky=W)
        comNametablet=ttk.Combobox(DataFrameLeft,textvariable=self.liab_type,font=("times new roman",12,"bold"),width=33)
        comNametablet["values"]=("Accounts Payable", "Short-Term Loans", "Accured Liabilities", "Current Portion of Long-Term Debt", "Long-term Debt", "Deferred", "Pension Obligations", "Lease Obligation", "Contingent Liabilities")
        comNametablet.current(0)
        comNametablet.grid(row=8,column=1)
    
        lblliabvalue=Label(DataFrameLeft,font=("arial",12,"bold"),text="Liab Value: ",padx=2,pady=2,bg="#FAEED1")
        lblliabvalue.grid(row=9,column=0,sticky=W)
        txtliabvalue=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.liab_value,width=31)
        txtliabvalue.grid(row=9,column=1)
        
        lblliabdate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date: ",padx=2,pady=2,bg="#FAEED1")
        lblliabdate.grid(row=10,column=0,sticky=W)
        txtliabdate=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.date,width=31)
        txtliabdate.grid(row=10,column=1)
        
        
       
        self.txtPrescription=Text(DataFrameRight,font=("arial",12,"bold"),width=700,height=15,bg="#FECD70",padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)
        
       
        btnPrescriptiondata=Button(Buttonframe,command=self.assetinsert,text="Add Asset ",bg="red",fg="white",font=("arial",14,"bold"),padx=2,pady=6)
        btnPrescriptiondata.grid(row=0,column=2)
        
        btnupdate=Button(Buttonframe,command=self.update_data,text="Update Asset",bg="red",fg="white",font=("arial",14,"bold"),pady=6)
        btnupdate.grid(row=0,column=4)
        
        btndelete=Button(Buttonframe,command=self.idelete,text="Delete Asset",bg="red",fg="white",font=("arial",14,"bold"),pady=6)
        btndelete.grid(row=0,column=6)
        
        btnlaibilityinsert=Button(Buttonframe,command=self.liabilityinsert,text="Add Liability",bg="red",fg="white",font=("arial",14,"bold"),padx=2,pady=6)
        btnlaibilityinsert.grid(row=0,column=8)
        
        btnlupdate=Button(Buttonframe,command=self.lupdate_data,text="Update Liability",bg="red",fg="white",font=("arial",14,"bold"),pady=6)
        btnlupdate.grid(row=0,column=10)
        
        btnldelete=Button(Buttonframe,command=self.ldelete,text="Delete Liability",bg="red",fg="white",font=("arial",14,"bold"),pady=6)
        btnldelete.grid(row=0,column=12)
        
        btnclear=Button(Buttonframe,command=self.iclear,text="Clear",bg="red",fg="white",font=("arial",14,"bold"),pady=6)
        btnclear.grid(row=0,column=14)
        
        btnExit=Button(Buttonframe,command=self.iexit,text="Exit",bg="red",fg="white",font=("arial",14,"bold"),pady=6)
        btnExit.grid(row=0,column=16)
        
        btnCal=Button(Buttonframe,command=self.icalculate,text="Balance Sheet",bg="red",fg="white",font=("arial",14,"bold"),padx=2,pady=6)
        btnCal.grid(row=0,column=18)
        
        btnsearch=Button(Buttonframe,command=self.search,text="search",bg="red",fg="white",font=("arial",14,"bold"),padx=2,pady=6)
        btnsearch.grid(row=0,column=20)
        
        btnshow=Button(Buttonframe,command=self.show,text="(•)",bg="red",fg="white",font=("arial",14,"bold"),padx=2,pady=6)
        btnshow.grid(row=0,column=22)
        
       
       

        
        
        
        
        scroll_x=ttk.Scrollbar(iDetailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(iDetailsframe,orient=VERTICAL)
        self.asset_table=ttk.Treeview(iDetailsframe,columns=("date","asset_id","asset_name","asset_type","asset_value"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x=ttk.Scrollbar(command=self.asset_table.xview)
        scroll_y=ttk.Scrollbar(command=self.asset_table.yview)

        self.asset_table.heading("date",text="date")        
        self.asset_table.heading("asset_id",text="asset_id")        
        self.asset_table.heading("asset_name",text="asset_name")
        self.asset_table.heading("asset_type",text="asset_type")
        self.asset_table.heading("asset_value",text="asset_value")
        
        self.asset_table["show"]="headings"
        self.asset_table.pack(fill=BOTH,expand=1)
        
        self.asset_table.column("date",width=45)
        self.asset_table.column("asset_id",width=45)
        self.asset_table.column("asset_name",width=45)
        self.asset_table.column("asset_type",width=45)
        self.asset_table.column("asset_value",width=45)
        
        
        self.asset_table.pack(fill=BOTH,expand=1)
        self.asset_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fatch_data()
        
        
        
        scroll_x=ttk.Scrollbar(lDetailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(lDetailsframe,orient=VERTICAL)
        self.liability_table=ttk.Treeview(lDetailsframe,columns=("date","liab_id","liab_name","liab_type","liab_value"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x=ttk.Scrollbar(command=self.liability_table.xview)
        scroll_y=ttk.Scrollbar(command=self.liability_table.yview)

        self.liability_table.heading("date",text="date")        
        self.liability_table.heading("liab_id",text="liab_id")        
        self.liability_table.heading("liab_name",text="liab_name")
        self.liability_table.heading("liab_type",text="liab_type")
        self.liability_table.heading("liab_value",text="liab_value")
        
        self.liability_table["show"]="headings"
        self.liability_table.pack(fill=BOTH,expand=1)
        
        self.liability_table.column("date",width=45)
        self.liability_table.column("liab_id",width=45)
        self.liability_table.column("liab_name",width=45)
        self.liability_table.column("liab_type",width=45)
        self.liability_table.column("liab_value",width=45)
        
        self.liability_table.pack(fill=BOTH,expand=1)
        self.liability_table.bind("<ButtonRelease-1>",self.lget_cursor)
        self.lfatch_data()
        
        



    def assetinsert(self):
        if self.asset_name.get()=="":
            messagebox.showerror("Error","All fields are rquired")   
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Karan@123",database="karan")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into asset(date,asset_name,asset_type,asset_value) values(%s,%s,%s,%s)",(
                                                                                                
                                                                                                self.date.get(),
                                                                                                self.asset_name.get(),
                                                                                                self.asset_type.get(),
                                                                                                self.asset_value.get(),
        ))
        conn.commit()
        self.fatch_data()
        conn.close()
        messagebox.showinfo("Success","Record has been inserted")
                 
    
    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Karan@123",database="karan")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from asset")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.asset_table.delete(*self.asset_table.get_children())
            for i in rows:
                self.asset_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
        
    def get_cursor(self,event=""):
        cursor_row=self.asset_table.focus()
        content=self.asset_table.item(cursor_row)
        row=content["values"]
        self.date.set(row[0])
        self.asset_id.set(row[1])
        self.asset_name.set(row[2])
        self.asset_type.set(row[3])
        self.asset_value.set(row[4])
        
        
        
        
 
        
    def update_data(self):
        if self.asset_name.get()=="" or self.asset_type.get()=="" or self.date=="":
            messagebox.showerror("Error","All fields are rquired")   
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Karan@123",database="karan")
            my_cursor=conn.cursor()
            my_cursor.execute("update asset set asset_name=%s,asset_type=%s,asset_value=%s where asset_id=%s ",(
                                                                                                    self.asset_name.get(),
                                                                                                    self.asset_type.get(),
                                                                                                    self.asset_value.get(),
                                                                                                    self.asset_id.get(),
                                                                                                    
            ))
            conn.commit()
            conn.close()
            self.fatch_data()
        
            messagebox.showinfo("update","asset record has been update successfully")  
          
    def idelete(self):
        if self.asset_name.get()=="" or self.asset_type.get()=="" or self.date=="":
            messagebox.showerror("Error","All fields are rquired")   
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Karan@123",database="karan")
            my_cursor=conn.cursor()
            query="delete from asset where asset_name=%s and asset_type=%s and date=%s"
            value=(self.asset_name.get(),self.asset_type.get(),self.date.get())
            my_cursor.execute(query,value)
            
            conn.commit()
            self.fatch_data()
            conn.close()
            
            messagebox.showinfo("delete","asset Entry has been deleted successfully")
        
        
    def iclear(self):
        self.asset_id.set("")
        self.asset_name.set("")
        self.asset_type.set("")
        self.asset_value.set("")
        self.liab_id.set("")
        self.liab_name.set("")
        self.liab_type.set("")
        self.liab_value.set("")
        
                
    def iexit(self):
        iexit=messagebox.askyesno("Finance management System","Confirm you want to exit")
        if iexit>0:
            self.root.destroy()
            return
                 
        
    def icalculate(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Karan@123",database="karan")
        my_cursor=conn.cursor()
        my_cursor.execute("select asset_id,asset_name,asset_type,asset_value,date from asset")
        a=my_cursor.fetchall()
        self.txtPrescription.insert(END,f"\nAsset Entry\n")
        self.txtPrescription.insert(END,"asset_id\t\t   asset_name\t\t  asset_type\t\t  asset_value\t\t date\n")
        for i in range(len(a)):
            for j in range(5):
                self.txtPrescription.insert(END,f"{a[i][j]}   "+"\t\t")
            self.txtPrescription.insert(END,f"  "+"\n")
        my_cursor.execute("select sum(asset_value) from asset")
        a=my_cursor.fetchall()
        my_cursor.execute("select count(*) from asset")
        b=my_cursor.fetchall()
       
        self.txtPrescription.insert(END,f"Total asset value is:\t{a[0][0]} of total entry {b[0][0]} "+"\n")
        self.txtPrescription.insert(END,f"+-----------------------------------------------------------+"+"\n")
        
        my_cursor.execute("select liab_id,liab_name,liab_type,liab_value,date from liability")
        c=my_cursor.fetchall()
       
        self.txtPrescription.insert(END,f"\nLiability Entry\n")
        self.txtPrescription.insert(END,"Liab_id\t\t   Liab_name\t\t  Liab_type\t\t  Liab_value\t\t  date\n")
        for i in range(len(c)):
            for j in range(5):
                self.txtPrescription.insert(END,f"{c[i][j]}   "+"\t\t")
            self.txtPrescription.insert(END,f"  "+"\n")
        my_cursor.execute("select sum(liab_value) from liability")
        c=my_cursor.fetchall()
        my_cursor.execute("select count(*) from liability")
        d=my_cursor.fetchall()
        self.txtPrescription.insert(END,f"Total laibility valueis:\t{c[0][0]} of total entry {d[0][0]} "+"\n")
        self.txtPrescription.insert(END,f"+-----------------------------------------------------------+"+"\n\n")
        
        self.ass=a[0][0]
        self.txtPrescription.insert(END,f"Total asset value is:\t{a[0][0]} of total entry {b[0][0]} "+"\n")
        
        self.lia=c[0][0]
        self.equ=self.ass-self.lia
        self.txtPrescription.insert(END,f"Total liability value is:\t{c[0][0]} of total entry {d[0][0]} "+"\n")
        self.txtPrescription.insert(END,f"Equity value is:\t{self.equ} "+"\n")
        self.total=self.equ+self.lia
        # if self.ass==self.total:
        #     self.txtPrescription.insert(END,f"Balance sheet is Balanced "+"\n")
        # else:
        #     self.txtPrescription.insert(END,f"Balance sheet is Unbalanced "+"\n")
        if self.ass>=self.lia:
            self.txtPrescription.insert(END,f"Balance sheet is Balanced "+"\n")
        else:
            self.txtPrescription.insert(END,f"Balance sheet is Unbalanced "+"\n")

        conn.commit()
        conn.close()
        self.fatch_data()
        messagebox.showinfo("calculate","Equity value has been calculated successfully")
    
    
        
       
    def liabilityinsert(self):
        if self.liab_name.get()=="":
            messagebox.showerror("Error","All fields are rquired")   
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Karan@123",database="karan")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into liability(date,liab_name,liab_type,liab_value) values(%s,%s,%s,%s)",(
                                                                                                
                                                                                                self.date.get(),
                                                                                                self.liab_name.get(),
                                                                                                self.liab_type.get(),
                                                                                                self.liab_value.get(),
                ))
            
            conn.commit()
            self.lfatch_data()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted")
                 
    
    def lfatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Karan@123",database="karan")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from liability")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.liability_table.delete(*self.liability_table.get_children())
            for i in rows:
                self.liability_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
        
    def lget_cursor(self,event=""):
        cursor_row=self.liability_table.focus()
        content=self.liability_table.item(cursor_row)
        row=content["values"]
        self.date.set(row[0])
        self.liab_id.set(row[1])
        self.liab_name.set(row[2])
        self.liab_type.set(row[3])
        self.liab_value.set(row[4])
        
        
    def lupdate_data(self):
        if self.liab_name.get()=="" or self.liab_type.get()=="" or self.date=="":
            messagebox.showerror("Error","All fields are rquired")   
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Karan@123",database="karan")
            my_cursor=conn.cursor()
            my_cursor.execute("update liability set liab_name=%s,liab_type=%s,liab_value=%s where liab_id=%s ",(
                                                                                                    self.liab_name.get(),
                                                                                                    self.liab_type.get(),
                                                                                                    self.liab_value.get(),
                                                                                                    self.liab_id.get(),
                                                                                                    
            ))
            self.lfatch_data()
            conn.commit()
            self.lfatch_data()
            conn.close()
        
            messagebox.showinfo("update","liability record has been update successfully")  
          
    def ldelete(self):
        if self.liab_name.get()=="" or self.liab_type.get()=="" or self.date=="":
            messagebox.showerror("Error","All fields are rquired")   
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Karan@123",database="karan")
            my_cursor=conn.cursor()
            query="delete from liability where liab_name=%s and liab_type=%s"
            value=(self.liab_name.get(),self.liab_type.get())
            my_cursor.execute(query,value)
            
            conn.commit()
            self.lfatch_data()
            conn.close()
            
            messagebox.showinfo("delete","liability Entry has been deleted successfully")
            
        
        
    def show(self):
        
        conn = mysql.connector.connect(host="localhost", username="root", password="Karan@123", database="karan")
        my_cursor = conn.cursor()

        try:
            # Execute the SQL query with FULL OUTER JOIN
            query = """
                SELECT asset_id, asset_name, asset_type, asset_value,
                   liab_id,liab_name, liab_type,liab_value
            FROM asset
            FULL JOIN liability
            ON asset_id = liab_id
            """
            value=(self.asset_id.get(),self.liab_id.get(),self.asset_id.get(),self.liab_id.get())
            my_cursor.execute(query)

            # Fetch the result
            result = my_cursor.fetchall()

            # Display the result in the Text widget
            self.txtPrescription.delete(1.0, END)
            self.txtPrescription.insert(END, "Asset and Liability Information\n")
            self.txtPrescription.insert(END, "asset_id  asset_name\t\tasset_type\t\tasset_value\t\tliab_id  liab_name\t\tliab_type\t\tliab_value\n")

            for row in result:
                self.txtPrescription.insert(END, f"{row[0]}  {row[1]}\t\t{row[2]}\t\t{row[3]}\t\t{row[4]}  {row[5]}\t\t{row[6]}\t\t{row[7]}\n")

        except Exception as e:
            messagebox.showerror("Error", f"Error fetching data: {e}")

        finally:
            # Close the database connection
            conn.close()

        # You may want to add further processing or error handling here

    
    def search(self):
        if self.liab_name.get() != "":
            conn = mysql.connector.connect(host="localhost", username="root", password="Karan@123", database="karan")
            my_cursor = conn.cursor()
            my_cursor.execute(
                "SELECT liab_id, liab_name, liab_type, liab_value, date FROM liability WHERE liab_name=%s",
                (self.liab_name.get(),)  # Use a tuple to pass the parameter
            )
            result = my_cursor.fetchall()

            if len(result) >= 0:
                self.txtPrescription.insert(END, "\nLiability Search Results\n")
                self.txtPrescription.insert(END, "liab_id\t\tliab_name\t\tliab_type\t\tliab_value\t\tdate\n")

                for row in result:
                    for value in row:
                        self.txtPrescription.insert(END, f"{value}\t\t")
                    self.txtPrescription.insert(END, "\n")

                messagebox.showinfo("Search", "Liability found successfully")
            else:
                messagebox.showinfo("Search", "Liability not found")

            conn.commit()
            conn.close()
            
        elif self.asset_name.get()!="":
            conn = mysql.connector.connect(host="localhost", username="root", password="Karan@123", database="karan")
            my_cursor = conn.cursor()
            my_cursor.execute(
                "SELECT asset_id, asset_name, asset_type, asset_value, date FROM asset WHERE asset_name=%s",
                (self.asset_name.get(),)  # Use a tuple to pass the parameter
            )
            result = my_cursor.fetchall()

            if len(result) > 0:
                self.txtPrescription.insert(END, "\nAsset Search Results\n")
                self.txtPrescription.insert(END, "Asset_id\t\tAsset_name\t\tAsset_type\t\tAsset_value\t\tdate\n")

                for row in result:
                    for value in row:
                        self.txtPrescription.insert(END, f"{value}\t\t")
                    self.txtPrescription.insert(END, "\n")

                messagebox.showinfo("Search", "Asset found successfully")
                
            
            else:
                messagebox.showinfo("Search", "Asset not found")
            conn.commit()
            conn.close()
        else:
            messagebox.showerror("Error","Name of liability or asset must be required")
            

            
        

    def logout(self):
        # Close the main program window
        self.root.destroy()

        # Open the login page again
        root = Tk()
        login_page = LoginPage(root)
        root.mainloop()


class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("User Authentication")
        self.root.geometry("1540x800+0+0")

        # User credentials dictionary
        self.user_credentials = {"karan":["karan123"]}

        self.create_widgets()
        self.image = PhotoImage(file="C:/Users/KARAN/OneDrive/Desktop/FMS_Project/pp.png")  # Replace with your image file path

        # Create a frame
        self.image_frame = Frame(root)
        self.image_frame.place(x=50,y=100,width=500,height=700)

        # Display the image using a Label inside the frame
        img_label = Label(self.image_frame, image=self.image)
        img_label.pack()

    def create_widgets(self):
        
        # Frame for Login
        
        """ self.image = PhotoImage(file="p.png")

            # Create a frame
            frame_p = Frame(self.root)
            frame_p.place(x=0,y=0,width=600,height=750)

            # Add image to the frame
            self.image_label = Label(self.frame_p, image=self.image)
            self.image_label.pack()"""
        frame_u = Frame(self.root,bg="#00A9FF")
        frame_u.place(x=700,y=0,width=1300,height=750)
        frame_login = Frame(self.root,bg="#00A9FF")
        frame_login.place(x=800,y=200,width=1300,height=750)

        lbl_title = Label(frame_login, text="Finance Management System", font=("Arial", 16, "bold"),bg="#00A9FF",fg="white")
        lbl_title.grid(row=0, column=0, columnspan=2, pady=10)
        lbl_title = Label(frame_login, text="Log In", font=("Arial", 16, "bold"),bg="#00A9FF")
        lbl_title.grid(row=1, column=0, columnspan=2, pady=10)

        lbl_username = Label(frame_login, text="Username :",bg="#00A9FF",fg="black",font=("arial",12,"bold"))
        lbl_username.grid(row=2, column=0, padx=1, pady=5, sticky="w")

        self.entry_username = Entry(frame_login, width=20)
        self.entry_username.grid(row=2, column=1, padx=1, pady=5)

        lbl_password = Label(frame_login, text="Password:",bg="#00A9FF",fg="black",font=("arial",12,"bold"))
        lbl_password.grid(row=3, column=0, padx=1, pady=5, sticky="w")

        self.entry_password = Entry(frame_login, width=20, show="*")
        self.entry_password.grid(row=3, column=1, padx=1, pady=5)

        btn_login = Button(frame_login, text="Login", command=self.check_credentials,bg="#001B79",fg="white",font=("arial",15,"bold"))
        btn_login.grid(row=4, column=0, columnspan=2, pady=10)
        
    
        

    def check_credentials(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        self.user_credentials = {"admin":"12345",
                                 "a":"a",
                                 "parth":"parth123",
                                 "keshav":"keshav123",
                                 "karan":"karan123"}
        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password")
            return
    
        

        if username in self.user_credentials and self.user_credentials[username] == password:
            messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
            # Close the login window
            self.root.destroy()
            # Open the main program window
            root = Tk()
            main_page = MainPage(root, username)
            root.mainloop()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
            
        


    
    
   
    
if __name__ == "__main__":
    root = Tk()
    login_page = LoginPage(root)
    root.mainloop()       
    

    
    

