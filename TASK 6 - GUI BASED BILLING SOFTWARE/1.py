from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import time
import os
import tempfile

class billclass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1024x768+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="#ccffff")
        self.cart_list = []
        self.chk_print = 0

        # Product Data (replaces database)
        self.product_data = [
            {"pdt_id": 1, "name": "Product 1", "price": 100, "qty": 10, "status": "ACTIVE"},
            {"pdt_id": 2, "name": "Product 2", "price": 200, "qty": 5, "status": "ACTIVE"},
            {"pdt_id": 3, "name": "Product 3", "price": 150, "qty": 8, "status": "ACTIVE"},
        ]

        # Customer and Product variables
        self.var_search = StringVar()
        self.var_cname = StringVar()
        self.var_contact = StringVar()
        self.var_pid = StringVar()
        self.var_pname = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_stock = StringVar()

        # Title
        title = Label(self.root, text="Inventory Management System", font=("Arial", 27, "bold"), bg="#00EEEE", fg="#FFFFF0", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=80)

        # Clock
        self.lbl_clock = Label(self.root, text="Inventory Management System \t\t Date: DD-MM-YYYY \t\t Time: HH:MM:SS", font=("Arial", 15), bg="#B25068", fg="#FFFAFA")
        self.lbl_clock.place(x=0, y=80, relwidth=1, height=30)

        # Product Frame
        pd_frame1 = Frame(self.root, bd=4, relief=RIDGE, bg="#ccffff")
        pd_frame1.place(x=6, y=110, width=250, height=600)

        ptitle = Label(pd_frame1, text="All Products", font=("Arial", 20), bg="#8B9A46", fg="#FFFFF0").pack(side=TOP, fill=X)

        # Search Frame
        pd_frame2 = Frame(pd_frame1, bd=2, relief=RIDGE, bg="#ccffff")
        pd_frame2.place(x=1, y=42, width=240, height=130)

        lbl_search = Label(pd_frame2, text="Search Product/By Name", font=("Arial", 10), bg="#ccffff", fg="green").place(x=2, y=5)
        lbl_name = Label(pd_frame2, text="Product Name", font=("Arial", 13, "bold"), bg="#ccffff").place(x=2, y=45)
        txt_name = Entry(pd_frame2, textvariable=self.var_search, font=("Arial", 13, "bold"), bg="#ccffcc").place(x=5, y=70, width=200, height=25)
        btn_search = Button(pd_frame2, text="Search", font=("Arial", 13), command=self.search, bg="#cc6600", fg="white", cursor="hand1").place(x=5, y=100, width=100, height=25)
        btn_showall = Button(pd_frame2, text="Show All", font=("Arial", 13), command=self.show, bg="#cc99ff", fg="white", cursor="hand1").place(x=125, y=100, width=100, height=25)

        # Product Details Frame
        pd_frame3 = Frame(pd_frame1, bd=3, relief=RIDGE)
        pd_frame3.place(x=0, y=180, width=245, height=420)

        scrolly = Scrollbar(pd_frame3, orient=VERTICAL)
        scrollx = Scrollbar(pd_frame3, orient=HORIZONTAL)

        self.pdt_table = ttk.Treeview(pd_frame3, columns=("pid", "name", "price", "qty", "status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.pdt_table.xview)
        scrolly.config(command=self.pdt_table.yview)
        self.pdt_table.heading("pid", text="PID")
        self.pdt_table.heading("name", text="NAME")
        self.pdt_table.heading("price", text="PRICE")
        self.pdt_table.heading("qty", text="QUANTITY")
        self.pdt_table.heading("status", text="STATUS")
        self.pdt_table["show"] = "headings"
        self.pdt_table.column("pid", width=40)
        self.pdt_table.column("name", width=100)
        self.pdt_table.column("price", width=100)
        self.pdt_table.column("qty", width=40)
        self.pdt_table.column("status", width=90)
        self.pdt_table.pack(fill=BOTH, expand=2)
        self.pdt_table.bind("<ButtonRelease-1>", self.get_data)

        # Customer Frame
        cust_frame = Frame(self.root, bd=4, relief=RIDGE, bg="#ccffff")
        cust_frame.place(x=260, y=110, width=465, height=100)
        custtitle = Label(cust_frame, text="Customer Details", font=("Arial", 15), bg="#816797", fg="#FFFFF0").pack(side=TOP, fill=X)
        lbl_name = Label(cust_frame, text="Name", font=("Arial", 13), bg="#ccffff").place(x=5, y=40)
        txt_name = Entry(cust_frame, textvariable=self.var_cname, font=("Arial", 15), bg="#ccffcc").place(x=5, y=65, width=200, height=25)
        lbl_contact = Label(cust_frame, text="Contact No", font=("Arial", 13), bg="#ccffff").place(x=243, y=40)
        txt_contact = Entry(cust_frame, textvariable=self.var_contact, font=("Arial", 15), bg="#ccffcc").place(x=245, y=65, width=200, height=25)

        # Additional frames and code remain the same (calculator, cart, billing, etc.)
                      #__cal_cart frame__
        cal_cart_frame=Frame(self.root,bd=2,relief=RIDGE,bg="#ccffff")
        cal_cart_frame.place(x=260,y=215,width=465,height=330)

                      #__cal frame__
        self.var_cal_input=StringVar()
        cal_frame=Frame(cal_cart_frame,bd=10,relief=RIDGE,bg="#ccffff")
        cal_frame.place(x=5,y=17,width=240,height=290)

        txt_cal_input=Entry(cal_frame,textvariable=self.var_cal_input,font=('arial',14,'bold'),width=18,bd=9,relief=GROOVE,justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=5)

        btn_7=Button(cal_frame,text='7',font=('arial',12,'bold'),command=lambda:self.get_input(7),bd=5,width=4,pady=10,cursor="hand1").grid(row=1,column=0)
        btn_8=Button(cal_frame,text='8',font=('arial',12,'bold'),command=lambda:self.get_input(8),bd=5,width=4,pady=10,cursor="hand1").grid(row=1,column=1)
        btn_9=Button(cal_frame,text='9',font=('arial',12,'bold'),command=lambda:self.get_input(9),bd=5,width=4,pady=10,cursor="hand1").grid(row=1,column=2)
        btn_sum=Button(cal_frame,text='+',font=('arial',12,'bold'),command=lambda:self.get_input('+'),bd=5,width=4,pady=10,cursor="hand1").grid(row=1,column=3)

        btn_4=Button(cal_frame,text='4',font=('arial',12,'bold'),command=lambda:self.get_input(4),bd=5,width=4,pady=10,cursor="hand1").grid(row=2,column=0)
        btn_5=Button(cal_frame,text='5',font=('arial',12,'bold'),command=lambda:self.get_input(5),bd=5,width=4,pady=10,cursor="hand1").grid(row=2,column=1)
        btn_6=Button(cal_frame,text='6',font=('arial',12,'bold'),command=lambda:self.get_input(6),bd=5,width=4,pady=10,cursor="hand1").grid(row=2,column=2)
        btn_sub=Button(cal_frame,text='-',font=('arial',12,'bold'),command=lambda:self.get_input('-'),bd=5,width=4,pady=10,cursor="hand1").grid(row=2,column=3)

        btn_1=Button(cal_frame,text='1',font=('arial',12,'bold'),command=lambda:self.get_input(1),bd=5,width=4,pady=10,cursor="hand1").grid(row=3,column=0)
        btn_2=Button(cal_frame,text='2',font=('arial',12,'bold'),command=lambda:self.get_input(2),bd=5,width=4,pady=10,cursor="hand1").grid(row=3,column=1)
        btn_3=Button(cal_frame,text='3',font=('arial',12,'bold'),command=lambda:self.get_input(3),bd=5,width=4,pady=10,cursor="hand1").grid(row=3,column=2)
        btn_mul=Button(cal_frame,text='*',font=('arial',12,'bold'),command=lambda:self.get_input('*'),bd=5,width=4,pady=10,cursor="hand1").grid(row=3,column=3)

        btn_0=Button(cal_frame,text='0',font=('arial',12,'bold'),command=lambda:self.get_input(0),bd=5,width=4,pady=10,cursor="hand1").grid(row=4,column=0)
        btn_C=Button(cal_frame,text='C',font=('arial',12,'bold'),command=self.clear_calc,bd=5,width=4,pady=10,cursor="hand1").grid(row=4,column=1)
        btn_eq=Button(cal_frame,text='=',font=('arial',12,'bold'),command=self.perform_calc,bd=5,width=4,pady=10,cursor="hand1").grid(row=4,column=2)
        btn_div=Button(cal_frame,text='/',font=('arial',12,'bold'),command=lambda:self.get_input('/'),bd=5,width=4,pady=10,cursor="hand1").grid(row=4,column=3)


        #__billing area__
        bill_frame=Frame(self.root,bd=2,relief=RIDGE,bg="#DCD7C9")
        bill_frame.place(x=725,y=110,width=300,height=410)
        billtitle=Label(bill_frame,text="Customer Bill Area",font=("KG HAPPY",18),bg="#A5C9CA",fg="#FFFFF0").pack(side=TOP,fill=X)
        scrolly=Scrollbar(bill_frame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        self.txt_bill_area=Text(bill_frame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)

        #__billing btn__
        bill_menu_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        bill_menu_frame.place(x=725,y=520,width=300,height=190)

        self.lbl_amt=Label(bill_menu_frame,text="Bill Amount \n[0]",font=("Tempus Sans ITC",10,"bold"),bg="#3f51b5",fg="white")
        self.lbl_amt.place(x=2,y=5,width=90,height=90)

        self.lbl_discount=Label(bill_menu_frame,text="Discount \n[5%]",font=("Tempus Sans ITC",10,"bold"),bg="#3f51b5",fg="white")
        self.lbl_discount.place(x=95,y=5,width=90,height=90)

        self.lbl_netpay=Label(bill_menu_frame,text="Net Pay \n[0]",font=("Tempus Sans ITC",10,"bold"),bg="#3f51b5",fg="white")
        self.lbl_netpay.place(x=188,y=5,width=125,height=90)

        btn_print=Button(bill_menu_frame,text="Print",command=self.print_bill,font=("Tempus Sans ITC",10,"bold"),bg="#3f51b5",fg="white",cursor="hand1")
        btn_print.place(x=2,y=97,width=90,height=50)

        btn_clear=Button(bill_menu_frame,text="Clear All",command=self.clear_all,font=("Tempus Sans ITC",10,"bold"),bg="#3f51b5",fg="white",cursor="hand1")
        btn_clear.place(x=95,y=97,width=90,height=50)

        btn_generate_bill=Button(bill_menu_frame,text="Generate Bill/Save Bill",command=self.generate_bill,font=("Tempus Sans ITC",9,"bold"),bg="#3f51b5",fg="white",cursor="hand1")
        btn_generate_bill.place(x=188,y=97,width=125,height=50)
        lbl_note=Label(bill_menu_frame,text="NOTE:\n'Enter'0'qty to remove product form list'",font=("JMH Typewriter",10,'bold'),bg="#950101",anchor="w",fg="white").pack(side=BOTTOM,fill=X)

        #__cart frame__
        cart_frame=Frame(cal_cart_frame,bd=3,relief=RIDGE)
        cart_frame.place(x=250,y=0,width=210,height=325)
        self.cart_title=Label(cart_frame,text="CART     Total Products : [0]",font=("Times new roman",13),bg="#00EEEE")
        self.cart_title.pack(side=TOP,fill=X)

        scrolly=Scrollbar(cart_frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_frame,orient=HORIZONTAL)

        self.cart_table=ttk.Treeview(cart_frame,columns=("pid","name","price","qty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.cart_table.xview)
        scrolly.config(command=self.cart_table.yview)
        self.cart_table.heading("pid",text="PID")
        self.cart_table.heading("name",text="NAME")
        self.cart_table.heading("price",text="PRICE")
        self.cart_table.heading("qty",text="QUANTITY")
        self.cart_table["show"]="headings"
        self.cart_table.column("pid",width=40)
        self.cart_table.column("name",width=90)
        self.cart_table.column("price",width=90)
        self.cart_table.column("qty",width=80)
        self.cart_table.pack(fill=BOTH,expand=2)
        self.cart_table.bind("<ButtonRelease-1>",self.get_data_cart)



        # Only database related code has been removed or replaced with in-memory data

        self.show()
        self.update_date_time()

        #__cart btn frame__
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()

        cart_btn_frame=Frame(self.root,bd=2,relief=RIDGE,bg="#ccffff")
        cart_btn_frame.place(x=260,y=550,width=465,height=160)

        lbl_pdt_name=Label(cart_btn_frame,text="Product Name",font=("JMH Typewriter",13),bg="#ccffff").place(x=5,y=15)
        txt_pdt_name=Entry(cart_btn_frame,textvariable=self.var_pname,font=("JMH Typewriter",13),bg="#ccffcc",state='readonly').place(x=5,y=50,width=150,height=25)
        lbl_p_price=Label(cart_btn_frame,text="Price Per QTY",font=("JMH Typewriter",13),bg="#ccffff").place(x=160,y=15)
        txt_p_price=Entry(cart_btn_frame,textvariable=self.var_price,font=("JMH Typewriter",13),bg="#ccffcc",state='readonly').place(x=160,y=50,width=150,height=25)
        lbl_p_qty=Label(cart_btn_frame,text="Quantity",font=("JMH Typewriter",13),bg="#ccffff").place(x=350,y=15)
        txt_p_qty=Entry(cart_btn_frame,textvariable=self.var_qty,font=("JMH Typewriter",13),bg="#ccffcc").place(x=350,y=50,width=90,height=25)

        self.lbl_instock=Label(cart_btn_frame,text="IN STOCK",font=("JMH Typewriter",13),bg="#ccffff")
        self.lbl_instock.place(x=5,y=90)

        btn_clear_cart=Button(cart_btn_frame,text="Clear",command=self.clear_cart,font=("JMH Typewriter",15,"bold"),bg="#666699",fg="white",cursor="hand1").place(x=100,y=120,width=150,height=30)
        btn_add_cart=Button(cart_btn_frame,text="Add | Update Cart",command=self.add_update_cart,font=("JMH Typewriter",15,"bold"),bg="#66ccff",fg="white",cursor="hand1").place(x=260,y=120,width=200,height=30)

    def clear_cart(self):
            self.var_pid.set('')
            self.var_pname.set('')
            self.var_price.set('')
            self.lbl_instock.config(text=f"IN STOCK")
            self.var_stock.set('')
            self.var_qty.set('')

    def get_data_cart(self,ev):
            f=self.cart_table.focus()
            content=(self.cart_table.item(f))
            row=content['values']
            self.var_pid.set(row[0])
            self.var_pname.set(row[1])
            self.var_price.set(row[2])
            self.var_qty.set(row[3])
            self.lbl_instock.config(text=f"IN STOCK [{str(row[4])}]")
            self.var_stock.set(row[4])

    def show_cart(self):
            try:
                    self.cart_table.delete(*self.cart_table.get_children())
                    for row in self.cart_list:
                        self.cart_table.insert('',END,values=row)
            except Exception as ex:
                    messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def add_update_cart(self):
            if self.var_pid.get()=='':
                    messagebox.showerror('Error',"Please Select Product From The List",parent=self.root)
            elif self.var_qty.get()=='':
                    messagebox.showerror('Error',"Quantity is Required",parent=self.root)
            elif int(self.var_qty.get())>int(self.var_stock.get()):
                    messagebox.showerror('Error',"Invalid Quantity",parent=self.root)
            else:
                    price_calc=self.var_price.get()
                    cart_data=[self.var_pid.get(),self.var_pname.get(),price_calc,self.var_qty.get(),self.var_stock.get()]
                    #__Update cart__
                    present='no'
                    index_=0
                    for row in self.cart_list:
                        if self.var_pid.get()==row[0]:
                                present='yes'
                                break
                        index_+=1
                    if present=='yes':
                        op=messagebox.askyesno('Confirm',"Product Already Present \n Do You Want To Update | Remove From The Cart List",parent=self.root)
                        if op==True:
                                if self.var_qty.get()=='0':
                                        self.cart_list.pop(index_)
                                else:
                                        self.cart_list[index_][3]=self.var_qty.get()#quantity
                    else:
                        self.cart_list.append(cart_data)

                    self.show_cart()
                    self.bill_update()


    def clear_all(self):
            del self.cart_list[:]
            self.var_cname.set('')
            self.var_contact.set('')
            self.txt_bill_area.delete('1.0',END)
            self.cart_title.config(text=f"CART \t Total Products : [0]")
            self.var_search.set('')
            self.clear_cart()
            self.show()
            self.show_cart()
            self.chk_print=0


    def show(self):
        """Display all active products in the product table"""
        self.pdt_table.delete(*self.pdt_table.get_children())  # Clear the table
        for product in self.product_data:
            if product["status"] == "ACTIVE":
                self.pdt_table.insert('', END, values=(product["pdt_id"], product["name"], product["price"], product["qty"], product["status"]))

    def search(self):
        """Search products by name"""
        search_term = self.var_search.get().lower()
        self.pdt_table.delete(*self.pdt_table.get_children())  # Clear the table
        for product in self.product_data:
            if search_term in product["name"].lower() and product["status"] == "ACTIVE":
                self.pdt_table.insert('', END, values=(product["pdt_id"], product["name"], product["price"], product["qty"], product["status"]))

    def get_data(self, ev):
        """Fetch product data from the selected row in the product table"""
        f = self.pdt_table.focus()
        content = self.pdt_table.item(f)
        row = content['values']
        if row:
            self.var_pid.set(row[0])
            self.var_pname.set(row[1])
            self.var_price.set(row[2])
            self.lbl_instock.config(text=f"IN STOCK [{str(row[3])}]")
            self.var_stock.set(row[3])
            self.var_qty.set('1')

    # Remaining methods (cart handling, billing, etc.) are the same
    def clear_calc(self):
            self.var_cal_input.set("")

    def perform_calc(self):
            result=self.var_cal_input.get()
            self.var_cal_input.set(eval(result))


    def update_date_time(self):
        time_ = time.strftime("%I:%M:%S")  # use 'H' instead of 'I' for 24-hour format
        date_ = time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Inventory Management System \t\t Date: {str(date_)} \t\t Time: {str(time_)}")
        self.lbl_clock.after(200, self.update_date_time)

    def generate_bill(self):
            if self.var_cname.get()=='' or self.var_contact.get()=='':
                    messagebox.showerror("Error",f"Customer Details Are Required",parent=self.root)
            elif len(self.cart_list)==0:
                    messagebox.showerror("Error",f"Please Add product To The Cart",parent=self.root)

            else:
                    #=====BILL TOP=====
                    self.bill_top()
                    #=====BILL MIDDLE=====
                    self.bill_middle()
                    #=====BILL BOTTOM=====
                    self.bill_bottom()
                    
                    fp=open(f'bills/{str(self.invoice)}.txt','w')
                    fp.write(self.txt_bill_area.get('1.0',END))
                    fp.close()
                    messagebox.showinfo('SAVED',"Bill has been Generated and Saved",parent=self.root)
                    self.chk_print=1
    
    def bill_top(self):
            self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%y"))
            bill_top_temp=f"""
\t\tKSSS INTERNATIONAL
Phone No. 04639 280 227, Sahupuram-628 229
{str("="*47)}
Customer Name : {self.var_cname.get()}
Ph No : {self.var_contact.get()}
Bill No : {str(self.invoice)}\t\tDate : {str(time.strftime("%d/%m/%y"))}\t\tTime : {str(time.strftime("%I:%M:%S"))}
{str("="*47)}
Product Name\t\t\tQTY\tPrice
{str("="*47)}
            """
            self.txt_bill_area.delete('1.0',END)
            self.txt_bill_area.insert('1.0',bill_top_temp)

    def bill_bottom(self):
            bill_bottom_temp=f"""
{str("="*47)}
Bill Amount\t\t\t\t Rs.{self.bill_amt}
Discount\t\t\t\t Rs.{self.discount}
Net Pay\t\t\t\t Rs.{self.net_pay}
{str("="*47)}\n
            """
            self.txt_bill_area.insert(END,bill_bottom_temp)

    def bill_middle(self):
        try:
            for row in self.cart_list:
                pdt_id = row[0]
                name = row[1]
                qty_purchased = int(row[3])
                price = float(row[2]) * qty_purchased
                price = str(price)

                # Find the corresponding product in self.product_data
                for product in self.product_data:
                    if product["pdt_id"] == int(pdt_id):
                        product["qty"] -= qty_purchased  # Reduce the stock
                        # Update the product status based on the remaining quantity
                        if product["qty"] == 0:
                            product["status"] = "INACTIVE"
                        else:
                            product["status"] = "ACTIVE"
                        break

                # Insert product details into the bill area
                self.txt_bill_area.insert(END, f"\n{name}\t\t\t{row[3]}\tRS.{price}")
            
            # Update the product table to reflect changes in stock and status
            self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def bill_update(self):
            self.bill_amt=0
            self.net_pay=0
            self.discount=0
            for row in self.cart_list:
                    self.bill_amt=self.bill_amt+(float(row[2])*int(row[3]))

            self.discount=(self.bill_amt*5)/100
            self.net_pay=self.bill_amt-self.discount
            self.lbl_amt.config(text=f'Bill Amount\n{str(self.bill_amt)}')
            self.lbl_netpay.config(text=f'Net Pay\n{str(self.net_pay)}')
            self.cart_title.config(text=f"CART \t Total Products : [{str(len(self.cart_list))}]")
              
    def print_bill(self):
            if self.chk_print==1:
                    messagebox.showinfo('PRINT',"Please wait whil printing.....",parent=self.root)
                    new_file=tempfile.mktemp('.txt')
                    open(new_file,'w').write(self.txt_bill_area.get('1.0',END))
                    os.startfile(new_file,'print')
            else:
                    messagebox.showerror('PRINT',"Please generate bill to print receipt",parent=self.root)



if __name__ == "__main__":
    root = Tk()
    obj = billclass(root)
    root.mainloop()
