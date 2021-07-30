import tkinter.messagebox
from tkinter import *
from tkinter import font as tkFont
import mysql.connector
from mysql.connector import Error
import random
import time
from tkcalendar import*
from tkcalendar import Calendar, DateEntry
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
root=Tk()
w=root.winfo_screenwidth()
h=root.winfo_screenheight()
root.geometry(f"{w}x{h}+0+0")
root.title("Stock management system")
#mydatabase
mydb=mysql.connector.connect(host='localhost',user='root', passwd='123adega', database='Stockmanagement')
#Create Cursor Instance
my_cursor=mydb.cursor()


#LOG IN WINDOW
image_bg=Image.open(r"stock2.jpg")
image_bg = image_bg.resize((w, h), Image.ANTIALIAS)
bg=ImageTk.PhotoImage(image_bg)
my_canvas=Canvas(root, width=w, height=h)
my_canvas.pack(fill="both", expand=True)
my_canvas.create_image(0,0, image=bg, anchor="nw")
my_canvas.create_text(w/2, 78,text='STOCK MANAGEMENT SYSTEM', font=('Arial',40, 'bold'))

Rightframe=Frame(root, bg='#E9E7D0', bd=5, padx=10, pady=2, width=w/2, height=500, relief=RIDGE)
Rightframe_window=my_canvas.create_window((w/2-w/4), h/2, anchor="nw", window=Rightframe)

#super window
super=Toplevel(root)
super.title("Stock Information")
super.geometry(f"{w}x{h}+0+0") 
super.configure(background="#deddd1")
super.withdraw()


def xyz():
	root.withdraw()
	super.deiconify()
	reset()
	
def back_root_super():
	super.withdraw()
	root.deiconify()
	reset()
	entryUsername.delete(0, END)
	entryPassword.delete(0, END)

def back_root_super2():
	super2.withdraw()
	root.deiconify()
	reset()
	entryUsername.delete(0, END)
	entryPassword.delete(0, END)
	
def order_placed():
	super.withdraw()
	super2.deiconify()
	reset_n()
	
def logout_stock():
	super.quit()
	
def stock_information():
	super2.withdraw()
	super.deiconify()
	reset()
	
def logout_order():
	super2.quit()
	
Product_category=StringVar()
Product_id=StringVar()
Product_name=StringVar()
Price_item=IntVar()
Supp_date=StringVar()
Total_amt=IntVar()
Due_date=StringVar()
Supplier=StringVar()
Order_id=StringVar()
Quantity_avl=IntVar()
discount=IntVar()
Tax=IntVar()
Supp_contactNo=StringVar()
Supp_emailid=StringVar()
Pay_method=StringVar()
Amt_paid=IntVar()
Balance=IntVar()
Transaction_id=StringVar()
Quantity_supp=IntVar()
status=StringVar()
SupplierId_1=StringVar()

Product_category_n= StringVar()
Product_id_n= StringVar()
Product_name_n= StringVar()
Quantity_avl_n= IntVar()
Price_item_n= IntVar()
Quantity_ordered_n= IntVar()
Orderdel_date_n= StringVar()
discount_n= IntVar()
Tax_n= IntVar()
Total_amt_n= IntVar()
Amt_paid_n= IntVar()
Pay_method_n= StringVar()
Transaction_id_n= StringVar()
Balance_n= IntVar()
Due_date_n= StringVar()
Supplier_n= StringVar()
Order_id_n= StringVar()
Supp_contactNo_n= StringVar()
Supp_emailid_n= StringVar()
status_n=StringVar()
SupplierIddd_n=StringVar()

def insertdata():
	cursor=None
	my_cursor_insert=mydb.cursor()
	
	a=Product_category.get()
	b=Product_id.get()
	c=Product_name.get()
	d=Price_item.get()
	u=Supp_date.get()
	f=Total_amt.get()
	g=Due_date.get()
	t=Supplier.get()
	i11=Order_id.get()
	j=Quantity_avl.get()
	k=discount.get()
	l=Tax.get()
	m=Supp_contactNo.get()
	n=Supp_emailid.get()
	o=Pay_method.get()
	p=Amt_paid.get()
	q=Balance.get()
	r=Transaction_id.get()
	s=Quantity_supp.get()
	x=status.get()
	v=SupplierId_1.get()
	try:
		if Product_category.get()=="" or Product_id.get()=='' or Product_name.get()=='' or Price_item.get()=='' or Supp_date.get()=='' or Total_amt.get()=='' or Due_date.get()=='' or Supplier.get()=='' or Order_id.get()=='' or Quantity_supp.get()=='':
			messagebox.showerror("ERROR","Enter all the necessary details")
		else:
			for i in my_tree.get_children():
				my_tree.delete(i)
			mobile_no1=econtactno.get()
			if((mobile_no1.isnumeric()==True) & (len(mobile_no1)==10)):
				contact_no1=mobile_no1
			else:
				messagebox.showerror("ERROR","The mobile number should contain only numbers and only 10 numbers")
				econtactno.delete(0,END)
				econtactno.focus()
				return

			my_cursor_insert.execute(f"SELECT * FROM Products WHERE p_id='{Product_id.get()}';")
			data_p_id=my_cursor_insert.fetchall()
			rownumbers = my_cursor_insert.rowcount
			if rownumbers<= 0:
				my_cursor_insert.execute(f"INSERT INTO Products values('{Product_id.get()}','{Product_name.get()}','{Product_category.get()}',{d},{Quantity_avl.get()});")
				mydb.commit()
			else:
				my_cursor_insert.execute(f"UPDATE Products SET p_name='{Product_name.get()}', p_category='{Product_category.get()}',price={d}, qavl={Quantity_avl.get()} WHERE p_id='{Product_id.get()}';")
				mydb.commit()
			
			my_cursor_insert.execute(f"INSERT INTO Orders values('{Order_id.get()}','{v}','{u}',{f}, {p}, '{o}', {q}, '{g}', '{r}', {l},{k}, '{x}');")
			mydb.commit()
			my_cursor_insert.execute(f"SELECT * FROM Supplier WHERE s_id='{v}';")
			data_s_id=my_cursor_insert.fetchall()
			rownumbers5 = my_cursor_insert.rowcount
			if rownumbers5<= 0:
				my_cursor_insert.execute(f"INSERT INTO Supplier values('{v}','{t}','{contact_no1}', '{n}');")
				mydb.commit()
			my_cursor_insert.execute(f"INSERT INTO Order_products values('{b}', '{Order_id.get()}', {s});")
			mydb.commit()
			my_cursor_insert.execute(f"INSERT INTO Supplier_products values('{b}', '{v}');")
			mydb.commit()
			my_cursor_insert.execute(f"SELECT  p_category, Products.p_id, p_name, qavl, price, q_ordered, ddate, discount, tax, cost, amt_paid, pay_method, transaction_id, balance, duedate, s_name, Supplier.s_id, Orders.Order_id, s_contactno, s_emailid,status FROM Products, Orders, Supplier, Order_products, Supplier_products, SignUp_Data, User_access WHERE Products.p_id = Order_products.p_id AND Supplier_products.p_id = Products.p_id AND Orders.Order_id = Order_products.o_id AND Supplier.s_id=Orders.Supplier_id AND Supplier_products.s_id=Orders.Supplier_id AND Supplier_products.s_id=Supplier.s_id AND Supplier_products.p_id=Order_products.p_id AND Supplier_products.p_id=Order_products.p_id AND SignUp_Data.email=User_access.email_id AND  User_access.pcategory=Products.p_category AND User_access.email_id='{email_id_access}' AND status='delivered';")
			
			for row in my_cursor_insert:
				count=len(my_tree.get_children())	
			
				if count%2==0:
					my_tree.insert(parent='', index=count, iid=count, values=(row[0],row[1],row[2],row[3], row[4],row[5],row[6], row[7], row[8], row[9],row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18],row[19], row[20]), tags='evenrow')
				else:
					my_tree.insert(parent='', index=count, iid=count, values=(row[0],row[1],row[2],row[3], row[4],row[5],row[6], row[7], row[8], row[9],row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18],  row[19], row[20]), tags='oddrow')
				
			my_tree.pack()
			messagebox.showinfo("Success", "Data inserted successfully")
	except mysql.connector.Error as e:
		messagebox.showerror("Failure",e)
	finally:
		if my_cursor_insert is not None:
			my_cursor_insert.close()
			
def display():
	cursor=None
	my_cursor_display=mydb.cursor()
	try:
		if Product_id.get()=='' and Product_name.get()=='':
			messagebox.showerror("Error","Enter atleast the product id or product name")
		else:
			for i in my_tree.get_children():
				my_tree.delete(i)
			if Product_id.get()=='':
				a=Product_name.get()
				my_cursor_display.execute(f"SELECT  p_category, Products.p_id, p_name, qavl, price, q_ordered, ddate, discount, tax, cost, amt_paid, pay_method, transaction_id, balance, duedate, s_name, Supplier.s_id, Orders.Order_id, s_contactno, s_emailid,status FROM Products, Orders, Supplier, Order_products, Supplier_products, SignUp_Data, User_access WHERE Products.p_id = Order_products.p_id AND Supplier_products.p_id = Products.p_id AND Orders.Order_id = Order_products.o_id AND Supplier.s_id=Orders.Supplier_id AND Supplier_products.s_id=Orders.Supplier_id AND Supplier_products.s_id=Supplier.s_id AND Supplier_products.p_id=Order_products.p_id AND Supplier_products.p_id=Order_products.p_id AND SignUp_Data.email=User_access.email_id AND  User_access.pcategory=Products.p_category AND User_access.email_id='{email_id_access}'AND p_name='a' AND status='delivered';")
				#count=0
				data_fields=my_cursor_display.fetchall()
				numberrows=my_cursor_display.rowcount
				if numberrows<=0:
					messagebox.showerror("Error", "No match found")
				else:
					Product_category.set(data_fields[0][0])
					Product_id.set(data_fields[0][1])
					Product_name.set(data_fields[0][2])
					Quantity_avl.set(data_fields[0][3])
					Price_item.set(data_fields[0][4])
					Quantity_supp.set(data_fields[0][5])
					Supp_date.set(data_fields[0][6])
					discount.set(data_fields[0][7])
					Tax.set(data_fields[0][8])
					Total_amt.set(data_fields[0][9])
					Amt_paid.set(data_fields[0][10])
					Pay_method.set(data_fields[0][11])
					Transaction_id.set(data_fields[0][12])
					Balance.set(data_fields[0][13])
					Due_date.set(data_fields[0][14])
					Supplier.set(data_fields[0][15])
					Order_id.set(data_fields[0][16])
					Supp_contactNo.set(data_fields[0][17])
					Supp_emailid.set(data_fields[0][18])
					
					for row in data_fields:
						treeitems=len(my_tree.get_children())	
						print(treeitems)
						#treeitems=treeitems+1
						if treeitems%2==0:
							my_tree.insert(parent='', index=treeitems, iid=treeitems, values=(row[0],row[1],row[2],row[3], row[4],row[5],row[6], row[7], row[8], row[9],row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18],row[19], row[20]), tags='evenrow')
						else:
							my_tree.insert(parent='', index=treeitems, iid=treeitems, values=(row[0],row[1],row[2],row[3], row[4],row[5],row[6], row[7], row[8], row[9],row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20]), tags='oddrow')
						
					my_tree.pack()
				
			elif Product_name.get()=='':
				a1=Product_id.get()
				my_cursor_display.execute(f"SELECT  p_category, Products.p_id, p_name, qavl, price, q_ordered, ddate, discount, tax, cost, amt_paid, pay_method, transaction_id, balance, duedate, s_name, Supplier.s_id, Orders.Order_id, s_contactno, s_emailid,status FROM Products, Orders, Supplier, Order_products, Supplier_products, SignUp_Data, User_access WHERE Products.p_id = Order_products.p_id AND Supplier_products.p_id = Products.p_id AND Orders.Order_id = Order_products.o_id AND Supplier.s_id=Orders.Supplier_id AND Supplier_products.s_id=Orders.Supplier_id AND Supplier_products.s_id=Supplier.s_id AND Supplier_products.p_id=Order_products.p_id AND Supplier_products.p_id=Order_products.p_id AND SignUp_Data.email=User_access.email_id AND  User_access.pcategory=Products.p_category AND User_access.email_id='{email_id_access}'AND Products.p_id='{a1}' AND status='delivered';")
				
				data_fields=my_cursor_display.fetchall()
				numberrows=my_cursor_display.rowcount
				if numberrows<=0:
					messagebox.showerror("Error", "No match found")
				else:
					Product_category.set(data_fields[0][0])
					Product_id.set(data_fields[0][1])
					Product_name.set(data_fields[0][2])
					Quantity_avl.set(data_fields[0][3])
					Price_item.set(data_fields[0][4])
					Quantity_supp.set(data_fields[0][5])
					Supp_date.set(data_fields[0][6])
					discount.set(data_fields[0][7])
					Tax.set(data_fields[0][8])
					Total_amt.set(data_fields[0][9])
					Amt_paid.set(data_fields[0][10])
					Pay_method.set(data_fields[0][11])
					Transaction_id.set(data_fields[0][12])
					Balance.set(data_fields[0][13])
					Due_date.set(data_fields[0][14])
					Supplier.set(data_fields[0][15])
					SupplierId_1.set(data_fields[0][16])
					Order_id.set(data_fields[0][17])
					Supp_contactNo.set(data_fields[0][18])
					Supp_emailid.set(data_fields[0][19])
					status.set(data_fields[0][20])
					
					for row in data_fields:
						treeitems=len(my_tree.get_children())	
						
					
						if treeitems%2==0:
							my_tree.insert(parent='', index=treeitems, iid=treeitems, values=(row[0],row[1],row[2],row[3], row[4],row[5],row[6], row[7], row[8], row[9],row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20]), tags='evenrow')
						else:
							my_tree.insert(parent='', index=treeitems, iid=treeitems, values=(row[0],row[1],row[2],row[3], row[4],row[5],row[6], row[7], row[8], row[9],row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20]), tags='oddrow')
						
					my_tree.pack()
			elif (Product_id.get()!='' and Product_name.get()!=''):
				a=Product_name.get()
				a1=Product_id.get()
				my_cursor_display.execute(f"SELECT  p_category, Products.p_id, p_name, qavl, price, q_ordered, ddate, discount, tax, cost, amt_paid, pay_method, transaction_id, balance, duedate, s_name, Supplier.s_id, Orders.Order_id, s_contactno, s_emailid,status FROM Products, Orders, Supplier, Order_products, Supplier_products, SignUp_Data, User_access WHERE Products.p_id = Order_products.p_id AND Supplier_products.p_id = Products.p_id AND Orders.Order_id = Order_products.o_id AND Supplier.s_id=Orders.Supplier_id AND Supplier_products.s_id=Orders.Supplier_id AND Supplier_products.s_id=Supplier.s_id AND Supplier_products.p_id=Order_products.p_id AND Supplier_products.p_id=Order_products.p_id AND SignUp_Data.email=User_access.email_id AND  User_access.pcategory=Products.p_category AND User_access.email_id='{email_id_access}'AND p_name='{a}'and Products.p_id='{a1}' AND status='delivered';")
				#count=0
				data_fields=my_cursor_display.fetchall()
				numberrows=my_cursor_display.rowcount
				if numberrows<=0:
					messagebox.showerror("Error", "No match found")
				else:
					Product_category.set(data_fields[0][0])
					Product_id.set(data_fields[0][1])
					Product_name.set(data_fields[0][2])
					Quantity_avl.set(data_fields[0][3])
					Price_item.set(data_fields[0][4])
					Quantity_supp.set(data_fields[0][5])
					Supp_date.set(data_fields[0][6])
					discount.set(data_fields[0][7])
					Tax.set(data_fields[0][8])
					Total_amt.set(data_fields[0][9])
					Amt_paid.set(data_fields[0][10])
					Pay_method.set(data_fields[0][11])
					Transaction_id.set(data_fields[0][12])
					Balance.set(data_fields[0][13])
					Due_date.set(data_fields[0][14])
					Supplier.set(data_fields[0][15])
					SupplierId_1.set(data_fields[0][16])
					Order_id.set(data_fields[0][17])
					Supp_contactNo.set(data_fields[0][18])
					Supp_emailid.set(data_fields[0][19])
					status.set(data_fields[0][20])
					
					for row in data_fields:
						treeitems=len(my_tree.get_children())	
						print(treeitems)
						#treeitems=treeitems+1
						if treeitems%2==0:
							my_tree.insert(parent='', index=treeitems, iid=treeitems, values=(row[0],row[1],row[2],row[3], row[4],row[5],row[6], row[7], row[8], row[9],row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20]), tags='evenrow')
						else:
							my_tree.insert(parent='', index=treeitems, iid=treeitems, values=(row[0],row[1],row[2],row[3], row[4],row[5],row[6], row[7], row[8], row[9],row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20]), tags='oddrow')
						
					my_tree.pack()
	
	except mysql.connector.Error as e:
		messagebox.showerror("Failure",e)
	finally:
		if my_cursor_display is not None:
			my_cursor_display.close()
			
old_id=''	
o_id=''	
s_old_id=''	
def select():
	cursor=None
	my_cursor_select=mydb.cursor()
	try:
		row_id = my_tree.focus()
		values=my_tree.item(row_id, 'values')
		Product_category.set(values[0])
		Product_id.set(values[1])
		Product_name.set(values[2])
		Quantity_avl.set(values[3])
		Price_item.set(values[4])
		Quantity_supp.set(values[5])
		Supp_date.set(values[6])
		discount.set(values[7])
		Tax.set(values[8])
		Total_amt.set(values[9])
		Amt_paid.set(values[10])
		Pay_method.set(values[11])
		Transaction_id.set(values[12])
		Balance.set(values[13])
		Due_date.set(values[14])
		Supplier.set(values[15])
		SupplierId_1.set(values[16])
		Order_id.set(values[17])
		Supp_contactNo.set(values[18])
		Supp_emailid.set(values[19])
		status.set(values[20])
		global old_id
		old_id=values[1]
		global o_id
		o_id=values[17]
		global s_old_id
		s_old_id=values[16]
	except mysql.connector.Error as e:
		messagebox.showerror("Failure",e)
	finally:
		if my_cursor_select is not None:
			my_cursor_select.close()	
			
def update():
	cursor=None
	my_cursor_update=mydb.cursor()
	try:
		
		a2=Product_category.get()
		b2=Product_id.get()
		c2=Product_name.get()
		d2=Price_item.get()
		u2=Supp_date.get()
		f2=Total_amt.get()
		g2=Due_date.get()
		t2=Supplier.get()
		i2=Order_id.get()
		j2=Quantity_avl.get()
		k2=discount.get()
		l2=Tax.get()
		m2=Supp_contactNo.get()
		n2=Supp_emailid.get()
		o2=Pay_method.get()
		p2=Amt_paid.get()
		q2=Balance.get()
		r2=Transaction_id.get()
		s2=Quantity_supp.get()
		x2=status.get()
		v2=SupplierId_1.get()
		
		row_id = my_tree.focus()
		my_tree.item(row_id, text="", values=(Product_category.get(),Product_id.get(),Product_name.get(),
		Quantity_avl.get(),Price_item.get(), Quantity_supp.get(),Supp_date.get(), discount.get(), Tax.get(),
		Total_amt.get(), Amt_paid.get(), Pay_method.get(), Transaction_id.get(), Balance.get(), Due_date.get(),
		Supplier.get(), SupplierId_1.get(), Order_id.get(), Supp_contactNo.get(), Supp_emailid.get(), status.get()))
		
		my_cursor_update.execute(f"UPDATE Products SET p_id='{b2}', p_name='{c2}', p_category='{a2}',price={d2}, qavl={j2} WHERE p_id='{old_id}';");
		mydb.commit()
		
		my_cursor_update.execute(f"UPDATE Orders SET Order_id='{i2}', Supplier_id={v2}, ddate='{u2}', cost={f2}, amt_paid={p2}, pay_method='{o2}', balance={q2}, duedate={g2},  transaction_id='{r2}', tax='{l2}',discount={k2}, status='{x2}' WHERE Order_id='{o_id}';")
		mydb.commit()
		
		my_cursor_update.execute(f"UPDATE Supplier SET s_id='{v2}',s_name='{t2}', s_contactno='{m2}',s_emailid='{n2}' WHERE s_id='{s_old_id}';")
		mydb.commit()
		
		my_cursor_update.execute(f"UPDATE Order_products SET p_id='{b2}', o_id='{i2}', q_ordered='{s2}' WHERE p_id='{old_id}';")
		mydb.commit()
		
		my_cursor_update.execute(f"UPDATE Supplier_products SET p_id='{b2}', s_id='{v2}' WHERE p_id='{old_id}';")
		mydb.commit()
		
		Product_category.set('--Select--')
		ep_id.delete(0, END)
		epname.delete(0,END)
		equantity.delete(0,END)
		eprice.delete(0, END)
		ediscount.delete(0, END)
		etax.delete(0, END)
		esupplier.delete(0, END)
		esupp_id.delete(0, END)
		eorder_id.delete(0, END)
		econtactno.delete(0, END)
		eemailid.delete(0, END)
		cal.delete(0, END) #Supp_date
		Pay_method.set('--Select--')
		etotal_amount.delete(0, END)
		eAmtpaid.delete(0, END)
		ebalance.delete(0, END)
		cal1.delete(0, END) #Due_date
		etransactionid.delete(0, END)
		equantitysupplied.delete(0, END)
		estatus.delete(0, END)
		
		messagebox.showinfo("Success", "Record updated successfully")
	except mysql.connector.Error as e:
		messagebox.showerror("Failure",e)
	finally:
		if my_cursor_update is not None:
			my_cursor_update.close()
			
def delete():
	cursor=None
	my_cursor_delete=mydb.cursor()
	try:
		select()
		row_id = my_tree.focus()
		if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this record?"):
			my_cursor_delete.execute(f"DELETE FROM Products WHERE p_id='{old_id}';")
			mydb.commit()
			my_cursor_delete.execute(f"DELETE FROM Orders WHERE Order_id='{o_id}';")
			mydb.commit()
			my_cursor_delete.execute(f"DELETE FROM Supplier WHERE s_id='{s_old_id}';")
			mydb.commit()
			my_cursor_delete.execute(f"DELETE FROM Order_products WHERE p_id='{old_id}';")
			mydb.commit()
			my_cursor_delete.execute(f"DELETE FROM Supplier_products WHERE p_id='{old_id}';")
			mydb.commit()
			my_tree.delete(row_id)
			messagebox.showinfo("Success","Record is deleted")
	
		else:
			return True
	except mysql.connector.Error as e:
		messagebox.showerror("Failure",e)
	finally:
		if my_cursor_delete is not None:
			my_cursor_delete.close()
def reset():
	cursor=None
	my_cursor_reset=mydb.cursor()
	try:
		for i in my_tree.get_children():
			 my_tree.delete(i)
		
		my_cursor_reset.execute(f"SELECT  p_category, Products.p_id, p_name, qavl, price, q_ordered, ddate, discount, tax, cost, amt_paid, pay_method, transaction_id, balance, duedate, s_name, Supplier.s_id, Orders.Order_id, s_contactno, s_emailid,status FROM Products, Orders, Supplier, Order_products, Supplier_products, SignUp_Data, User_access WHERE Products.p_id = Order_products.p_id AND Supplier_products.p_id = Products.p_id AND Orders.Order_id = Order_products.o_id AND Supplier.s_id=Orders.Supplier_id AND Supplier_products.s_id=Orders.Supplier_id AND Supplier_products.s_id=Supplier.s_id AND Supplier_products.p_id=Order_products.p_id AND Supplier_products.p_id=Order_products.p_id AND SignUp_Data.email=User_access.email_id AND  User_access.pcategory=Products.p_category AND User_access.email_id='{email_id_access}' AND status='delivered';")
		for row in my_cursor_reset:
			count=len(my_tree.get_children())	
			if count%2==0:
				my_tree.insert(parent='', index=count, iid=count, values=(row[0],row[1],row[2],row[3], row[4],row[5],row[6], row[7], row[8], row[9],row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20]), tags='evenrow')
			else:
				my_tree.insert(parent='', index=count, iid=count, values=(row[0],row[1],row[2],row[3], row[4],row[5],row[6], row[7], row[8], row[9],row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20]), tags='oddrow')
				
		my_tree.pack()
		Product_category.set('--Select--')
		ep_id.delete(0, END)
		epname.delete(0,END)
		equantity.delete(0,END)
		eprice.delete(0, END)
		ediscount.delete(0, END)
		discount.set(0)
		etax.delete(0, END)
		Tax.set(0)
		esupplier.delete(0, END)
		esupp_id.delete(0, END)
		eorder_id.delete(0, END)
		econtactno.delete(0, END)
		eemailid.delete(0, END)
		cal.delete(0, END) #Supp_date
		Pay_method.set('--Select--')
		etotal_amount.delete(0, END)
		eAmtpaid.delete(0, END)
		ebalance.delete(0, END)
		cal1.delete(0, END) #Due_date
		estatus.delete(0, END)
		etransactionid.delete(0, END)
		equantitysupplied.delete(0, END)		
	except mysql.connector.Error as e:
		messagebox.showerror("Failure",e)
	finally:
		if my_cursor_reset is not None:
			my_cursor_reset.close()	

def insertdata_n():
	cursor=None
	my_cursor_insertn=mydb.cursor()
	
	a=Product_category_n.get()
	b=Product_id_n.get()
	c=Product_name_n.get()
	d=Price_item_n.get()
	u=Orderdel_date_n.get()
	f=Total_amt_n.get()
	g=Due_date_n.get()
	t=Supplier_n.get()
	i1_2=Order_id_n.get()
	j=Quantity_avl_n.get()
	k=discount_n.get()
	l=Tax_n.get()
	m=Supp_contactNo_n.get()
	n=Supp_emailid_n.get()
	o=Pay_method_n.get()
	p=Amt_paid_n.get()
	q=Balance_n.get()
	r=Transaction_id_n.get()
	s=Quantity_ordered_n.get()
	x=status_n.get()
	v=SupplierIddd_n.get()
	
	try:
		if Product_category_n.get()=="" or Product_id_n.get()=='' or Product_name_n.get()=='' or Price_item_n.get()=='' or Orderdel_date_n.get()=='' or Total_amt_n.get()=='' or Due_date_n.get()=='' or Supplier_n.get()=='' or Order_id_n.get()=='' or Quantity_ordered_n.get()=='':
			messagebox.showerror("ERROR","Enter all the necessary details")
		else:
			for i in my_tree_n.get_children():
				my_tree_n.delete(i)
			mobile_no1_n=econtactno_n.get()
			if((mobile_no1_n.isnumeric()==True) & (len(mobile_no1_n)==10)):
				contact_no1_n=mobile_no1_n
			else:
				messagebox.showerror("ERROR","The mobile number should contain only numbers and only 10 numbers")
				econtactno_n.delete(0,END)
				econtactno_n.focus()
				return
			my_cursor_insertn.execute(f"SELECT * FROM Products WHERE p_id='{Product_id_n.get()}';")
			data_p_id_n=my_cursor_insertn.fetchall()
			rownumbers1 = my_cursor_insertn.rowcount
			if rownumbers1<= 0:
				my_cursor_insertn.execute(f"INSERT INTO Products values('{Product_id_n.get()}','{Product_name_n.get()}','{Product_category_n.get()}',{d},{Quantity_avl_n.get()});")
				mydb.commit()
			else:
				my_cursor_insertn.execute(f"UPDATE Products SET p_name='{Product_name_n.get()}', p_category='{Product_category_n.get()}',price={d}, qavl={Quantity_avl_n.get()} WHERE p_id='{Product_id_n.get()}';")
				mydb.commit()
			
			my_cursor_insertn.execute(f"INSERT INTO Orders values('{i1_2}','{v}','{u}',{f}, {p}, '{o}', {q}, '{g}', '{r}', {l},{k}, '{x}');")
			mydb.commit()
			my_cursor_insertn.execute(f"SELECT * FROM Supplier WHERE s_id='{v}';")
			data_s_id_n=my_cursor_insertn.fetchall()
			rownumbers2 = my_cursor_insertn.rowcount
			if rownumbers2<= 0:
				my_cursor_insertn.execute(f"INSERT INTO Supplier values('{v}','{t}','{m}', '{n}');")
				mydb.commit()
			my_cursor_insertn.execute(f"INSERT INTO Order_products values('{b}', '{i1_2}', {s});")
			mydb.commit()
			my_cursor_insertn.execute(f"INSERT INTO Supplier_products values('{b}', '{v}');")
			mydb.commit()
			
			my_cursor_insertn.execute(f"SELECT  p_category, Products.p_id, p_name, qavl, price, q_ordered, ddate, discount, tax, cost, amt_paid, pay_method, transaction_id, balance, duedate, s_name, Supplier.s_id, Orders.Order_id, s_contactno, s_emailid,status FROM Products, Orders, Supplier, Order_products, Supplier_products, SignUp_Data, User_access WHERE Products.p_id = Order_products.p_id AND Supplier_products.p_id = Products.p_id AND Orders.Order_id = Order_products.o_id AND Supplier.s_id=Orders.Supplier_id AND Supplier_products.s_id=Orders.Supplier_id AND Supplier_products.s_id=Supplier.s_id AND Supplier_products.p_id=Order_products.p_id AND Supplier_products.p_id=Order_products.p_id AND  SignUp_Data.email=User_access.email_id AND  User_access.pcategory=Products.p_category AND User_access.email_id='{email_id_access}' AND status<>'delivered';")
			
			for row in my_cursor_insertn:
				count_n=len(my_tree_n.get_children())	
			
				if count_n%2==0:
					my_tree_n.insert(parent='', index=count_n, iid=count_n, values=(row[0],row[1],row[2],row[3], row[4],row[5],row[6], row[7], row[8], row[9],row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20]), tags='evenrow')
				else:
					my_tree_n.insert(parent='', index=count_n, iid=count_n, values=(row[0],row[1],row[2],row[3], row[4],row[5],row[6], row[7], row[8], row[9],row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20]), tags='oddrow')
				
			my_tree_n.pack()
			messagebox.showinfo("Success", "Data inserted successfully")
	except mysql.connector.Error as e:
		messagebox.showerror("Failure",e)
	finally:
		if my_cursor_insertn is not None:
			my_cursor_insertn.close()
			
def display_n():
	cursor=None
	my_cursor_displayn=mydb.cursor()
	try:
		if Product_id_n.get()=='' and Product_name_n.get()=='':
			messagebox.showerror("Error","Enter atleast the product id or product name")
		else:
			for i in my_tree_n.get_children():
				my_tree_n.delete(i)
			if Product_id_n.get()=='':
				a=Product_name_n.get()
				my_cursor_displayn.execute(f"SELECT  p_category, Products.p_id, p_name, qavl, price, q_ordered, ddate, discount, tax, cost, amt_paid, pay_method, transaction_id, balance, duedate, s_name, Supplier.s_id, Orders.Order_id, s_contactno, s_emailid,status FROM Products, Orders, Supplier, Order_products, Supplier_products, SignUp_Data, User_access WHERE Products.p_id = Order_products.p_id AND Supplier_products.p_id = Products.p_id AND Orders.Order_id = Order_products.o_id AND Supplier.s_id=Orders.Supplier_id AND Supplier_products.s_id=Orders.Supplier_id AND Supplier_products.s_id=Supplier.s_id AND Supplier_products.p_id=Order_products.p_id AND Supplier_products.p_id=Order_products.p_id AND SignUp_Data.email=User_access.email_id AND  User_access.pcategory=Products.p_category AND User_access.email_id='{email_id_access}' AND p_name='a' AND status<>'delivered';")
				data_fields=my_cursor_displayn.fetchall()
				numberrows_n=my_cursor_displayn.rowcount
				if numberrows_n<=0:
					messagebox.showerror("Error", "No match found")
				else:
					Product_category_n.set(data_fields[0][0])
					Product_id_n.set(data_fields[0][1])
					Product_name_n.set(data_fields[0][2])
					Quantity_avl_n.set(data_fields[0][3])
					Price_item_n.set(data_fields[0][4])
					Quantity_ordered_n.set(data_fields[0][5])
					Orderdel_date_n.set(data_fields[0][6])
					discount_n.set(data_fields[0][7])
					Tax_n.set(data_fields[0][8])
					Total_amt_n.set(data_fields[0][9])
					Amt_paid_n.set(data_fields[0][10])
					Pay_method_n.set(data_fields[0][11])
					Transaction_id_n.set(data_fields[0][12])
					Balance_n.set(data_fields[0][13])
					Due_date_n.set(data_fields[0][14])
					Supplier_n.set(data_fields[0][15])
					SupplierIddd_n.set(data_fields[0][16])
					Order_id_n.set(data_fields[0][17])
					Supp_contactNo_n.set(data_fields[0][17])
					Supp_emailid_n.set(data_fields[0][19])
					status_n.set(data_fields[0][20])
					
					for row in data_fields:
						treeitems_n=len(my_tree_n.get_children())	
						#treeitems=treeitems+1
						if treeitems_n%2==0:
							my_tree_n.insert(parent='', index=treeitems_n, iid=treeitems_n, values=(row[0],row[1],row[2],row[3], row[4],row[5],row[6], row[7], row[8], row[9],row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20]), tags='evenrow')
						else:
							my_tree_n.insert(parent='', index=treeitems_n, iid=treeitems_n, values=(row[0],row[1],row[2],row[3], row[4],row[5],row[6], row[7], row[8], row[9],row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20]), tags='oddrow')
						
					my_tree_n.pack()
				
			elif Product_name_n.get()=='':
				a1=Product_id_n.get()
				my_cursor_displayn.execute(f"SELECT  p_category, Products.p_id, p_name, qavl, price, q_ordered, ddate, discount, tax, cost, amt_paid, pay_method, transaction_id, balance, duedate, s_name, Supplier.s_id, Orders.Order_id, s_contactno, s_emailid,status FROM Products, Orders, Supplier, Order_products, Supplier_products, SignUp_Data, User_access WHERE Products.p_id = Order_products.p_id AND Supplier_products.p_id = Products.p_id AND Orders.Order_id = Order_products.o_id AND Supplier.s_id=Orders.Supplier_id AND Supplier_products.s_id=Orders.Supplier_id AND Supplier_products.s_id=Supplier.s_id AND Supplier_products.p_id=Order_products.p_id AND Supplier_products.p_id=Order_products.p_id AND SignUp_Data.email=User_access.email_id AND  User_access.pcategory=Products.p_category AND User_access.email_id='{email_id_access}' AND Products.p_id='{a1}' AND status<>'delivered';")
				#count=0
				data_fields=my_cursor_displayn.fetchall()
				numberrows_n=my_cursor_displayn.rowcount
				if numberrows_n<=0:
					messagebox.showerror("Error", "No match found")
				else:
					Product_category_n.set(data_fields[0][0])
					Product_id_n.set(data_fields[0][1])
					Product_name_n.set(data_fields[0][2])
					Quantity_avl_n.set(data_fields[0][3])
					Price_item_n.set(data_fields[0][4])
					Quantity_ordered_n.set(data_fields[0][5])
					Orderdel_date_n.set(data_fields[0][6])
					discount_n.set(data_fields[0][7])
					Tax_n.set(data_fields[0][8])
					Total_amt_n.set(data_fields[0][9])
					Amt_paid_n.set(data_fields[0][10])
					Pay_method_n.set(data_fields[0][11])
					Transaction_id_n.set(data_fields[0][12])
					Balance_n.set(data_fields[0][13])
					Due_date_n.set(data_fields[0][14])
					Supplier_n.set(data_fields[0][15])
					SupplierIddd_n.set(data_fields[0][16])
					Order_id_n.set(data_fields[0][17])
					Supp_contactNo_n.set(data_fields[0][18])
					Supp_emailid_n.set(data_fields[0][19])
					status_n.set(data_fields[0][20])
					
					for row in data_fields:
						treeitems_n=len(my_tree_n.get_children())	
						#treeitems=treeitems+1
						if treeitems_n%2==0:
							my_tree_n.insert(parent='', index=treeitems_n, iid=treeitems_n, values=(row[0],row[1],row[2],row[3], row[4],row[5],row[6], row[7], row[8], row[9],row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20]), tags='evenrow')
						else:
							my_tree_n.insert(parent='', index=treeitems_n, iid=treeitems_n, values=(row[0],row[1],row[2],row[3], row[4],row[5],row[6], row[7], row[8], row[9],row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20]), tags='oddrow')
						
					my_tree_n.pack()
					
			elif (Product_id_n.get()!='' and Product_name_n.get()!=''):
				a=Product_name_n.get()
				a1=Product_id_n.get()
				my_cursor_displayn.execute(f"SELECT  p_category, Products.p_id, p_name, qavl, price, q_ordered, ddate, discount, tax, cost, amt_paid, pay_method, transaction_id, balance, duedate, s_name, Supplier.s_id, Orders.Order_id, s_contactno, s_emailid,status FROM Products, Orders, Supplier, Order_products, Supplier_products, SignUp_Data, User_access WHERE Products.p_id = Order_products.p_id AND Supplier_products.p_id = Products.p_id AND Orders.Order_id = Order_products.o_id AND Supplier.s_id=Orders.Supplier_id AND Supplier_products.s_id=Orders.Supplier_id AND Supplier_products.s_id=Supplier.s_id AND Supplier_products.p_id=Order_products.p_id AND Supplier_products.p_id=Order_products.p_id AND SignUp_Data.email=User_access.email_id AND  User_access.pcategory=Products.p_category AND User_access.email_id='{email_id_access}' AND p_name='{a}'and Products.p_id='{a1}' AND status<>'delivered';")
				#count=0
				data_fields=my_cursor_displayn.fetchall()
				numberrows_n=my_cursor_displayn.rowcount
				if numberrows_n<=0:
					messagebox.showerror("Error", "No match found")
				else:
					Product_category_n.set(data_fields[0][0])
					Product_id_n.set(data_fields[0][1])
					Product_name_n.set(data_fields[0][2])
					Quantity_avl_n.set(data_fields[0][3])
					Price_item_n.set(data_fields[0][4])
					Quantity_ordered_n.set(data_fields[0][5])
					Orderdel_date_n.set(data_fields[0][6])
					discount_n.set(data_fields[0][7])
					Tax_n.set(data_fields[0][8])
					Total_amt_n.set(data_fields[0][9])
					Amt_paid_n.set(data_fields[0][10])
					Pay_method_n.set(data_fields[0][11])
					Transaction_id_n.set(data_fields[0][12])
					Balance_n.set(data_fields[0][13])
					Due_date_n.set(data_fields[0][14])
					Supplier_n.set(data_fields[0][15])
					SupplierIddd_n.set(data_fields[0][16])
					Order_id_n.set(data_fields[0][17])
					Supp_contactNo_n.set(data_fields[0][18])
					Supp_emailid_n.set(data_fields[0][19])
					status_n.set(data_fields[0][20])
					
					for row in data_fields:
						treeitems_n=len(my_tree_n.get_children())	
						if treeitems_n%2==0:
							my_tree_n.insert(parent='', index=treeitems_n, iid=treeitems_n, values=(row[0],row[1],row[2],row[3], row[4],row[5],row[6], row[7], row[8], row[9],row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20]), tags='evenrow')
						else:
							my_tree_n.insert(parent='', index=treeitems_n, iid=treeitems_n, values=(row[0],row[1],row[2],row[3], row[4],row[5],row[6], row[7], row[8], row[9],row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20]), tags='oddrow')
						
					my_tree_n.pack()
	
	except mysql.connector.Error as e:
		messagebox.showerror("Failure",e)
	finally:
		if my_cursor_displayn is not None:
			my_cursor_displayn.close()


old_id_n=''	
o_id_n=''	
s_old_idn=''			
def select_n():
	cursor=None
	my_cursor_selectn=mydb.cursor()
	try:
		row_id_n = my_tree_n.focus()
		values=my_tree_n.item(row_id_n, 'values')
		Product_category_n.set(values[0])
		Product_id_n.set(values[1])
		Product_name_n.set(values[2])
		Quantity_avl_n.set(values[3])
		Price_item_n.set(values[4])
		Quantity_ordered_n.set(values[5])
		Orderdel_date_n.set(values[6])
		discount_n.set(values[7])
		Tax_n.set(values[8])
		Total_amt_n.set(values[9])
		Amt_paid_n.set(values[10])
		Pay_method_n.set(values[11])
		Transaction_id_n.set(values[12])
		Balance_n.set(values[13])
		Due_date_n.set(values[14])
		Supplier_n.set(values[15])
		SupplierIddd_n.set(values[16])
		Order_id_n.set(values[17])
		Supp_contactNo_n.set(values[18])
		Supp_emailid_n.set(values[19])
		status_n.set(values[20])
		global old_id_n
		old_id_n=values[1]
		global o_id_n
		o_id_n=values[17]
		global s_old_idn
		s_old_idn=values[16]
	except mysql.connector.Error as e:
		messagebox.showerror("Failure",e)
	finally:
		if my_cursor_selectn is not None:
			my_cursor_selectn.close()

def update_n():
	cursor=None
	my_cursor_updaten=mydb.cursor()
	try:
		a2=Product_category_n.get()
		b2=Product_id_n.get()
		c2=Product_name_n.get()
		d2=Price_item_n.get()
		u2=Orderdel_date_n.get()
		f2=Total_amt_n.get()
		g2=Due_date_n.get()
		t2=Supplier_n.get()
		i2=Order_id_n.get()
		j2=Quantity_avl_n.get()
		k2=discount_n.get()
		l2=Tax_n.get()
		m2=Supp_contactNo_n.get()
		n2=Supp_emailid_n.get()
		o2=Pay_method_n.get()
		p2=Amt_paid_n.get()
		q2=Balance_n.get()
		r2=Transaction_id_n.get()
		s2=Quantity_ordered_n.get()
		x2=status_n.get()
		v2=SupplierIddd_n.get()
		
		row_id = my_tree.focus()
		my_tree.item(row_id, text="", values=(Product_category.get(),Product_id.get(),Product_name.get(),
		Quantity_avl.get(),Price_item.get(), Quantity_supp.get(),Supp_date.get(), discount.get(), Tax.get(),
		Total_amt.get(), Amt_paid.get(), Pay_method.get(), Transaction_id.get(), Balance.get(), Due_date.get(),
		Supplier.get(), SupplierId_1.get(), Order_id.get(), Supp_contactNo.get(), Supp_emailid.get(), status.get()))
		
		my_cursor_updaten.execute(f"UPDATE Products SET p_id='{b2}', p_name='{c2}', p_category='{a2}',price={d2}, qavl={j2} WHERE p_id='{old_id_n}';");
		mydb.commit()
		
		my_cursor_updaten.execute(f"UPDATE Orders SET Order_id='{i2}', Supplier_id={v2}, ddate='{u2}', cost={f2}, amt_paid={p2}, pay_method='{o2}', balance={q2}, duedate={g2},  transaction_id='{r2}', tax='{l2}',discount={k2}, status='{x2}' WHERE Order_id='{o_id_n}';")
		mydb.commit()
		
		my_cursor_updaten.execute(f"UPDATE Supplier SET s_id='{v2}',s_name='{t2}', s_contactno='{m2}',s_emailid='{n2}' WHERE s_id='{s_old_idn}';")
		mydb.commit()
		
		my_cursor_updaten.execute(f"UPDATE Order_products SET p_id='{b2}', o_id='{i2}', q_ordered='{s2}' WHERE p_id='{old_id_n}';")
		mydb.commit()
		
		my_cursor_updaten.execute(f"UPDATE Supplier_products SET p_id='{b2}', s_id='{v2}' WHERE p_id='{old_id_n}';")
		mydb.commit()
		
		Product_category_n.set('--Select--')
		ep_id_n.delete(0, END)
		epname_n.delete(0,END)
		equantity_n.delete(0,END)
		eprice_n.delete(0, END)
		ediscount_n.delete(0, END)
		etax_n.delete(0, END)
		esupplier_n.delete(0, END)
		esupp_id_n.delete(0, END)
		eorder_id_n.delete(0, END)
		econtactno_n.delete(0, END)
		eemailid_n.delete(0, END)
		cal_n.delete(0, END) #Supp_date
		Pay_method_n.set('--Select--')
		etotal_amount_n.delete(0, END)
		eAmtpaid_n.delete(0, END)
		ebalance_n.delete(0, END)
		cal1_n.delete(0, END) #Due_date
		estatus_n.delete(0, END)
		etransactionid_n.delete(0, END)
		equantityordered_n.delete(0, END)
		
		messagebox.showinfo("Success", "Record updated successfully")
	except mysql.connector.Error as e:
		messagebox.showerror("Failure",e)
	finally:
		if my_cursor_updaten is not None:
			my_cursor_updaten.close()

def delete_n():
	cursor=None
	my_cursor_deleten=mydb.cursor()
	try:
		select()
		row_id = my_tree.focus()
		if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this record?"):
			my_cursor_deleten.execute(f"DELETE FROM Products WHERE p_id='{old_id}';")
			mydb.commit()
			my_cursor_deleten.execute(f"DELETE FROM Orders WHERE Order_id='{o_id}';")
			mydb.commit()
			my_cursor_deleten.execute(f"DELETE FROM Supplier WHERE s_id='{s_old_id}';")
			mydb.commit()
			my_cursor_deleten.execute(f"DELETE FROM Order_products WHERE p_id='{old_id}';")
			mydb.commit()
			my_cursor_deleten.execute(f"DELETE FROM Supplier_products WHERE p_id='{old_id}';")
			mydb.commit()
			my_tree.delete(row_id)
			messagebox.showinfo("Success","Record is deleted")
	
		else:
			return True
	except mysql.connector.Error as e:
		messagebox.showerror("Failure",e)
	finally:
		if my_cursor_deleten is not None:
			my_cursor_deleten.close()

def reset_n():
	cursor=None
	my_cursor_resetn=mydb.cursor()
	try:
		for i in my_tree_n.get_children():
			 my_tree_n.delete(i)
		#window.update()
		
		my_cursor_resetn.execute(f"SELECT  p_category, Products.p_id, p_name, qavl, price, q_ordered, ddate, discount, tax, cost, amt_paid, pay_method, transaction_id, balance, duedate, s_name, Supplier.s_id, Orders.Order_id, s_contactno, s_emailid,status FROM Products, Orders, Supplier, Order_products, Supplier_products, SignUp_Data, User_access WHERE Products.p_id = Order_products.p_id AND Supplier_products.p_id = Products.p_id AND Orders.Order_id = Order_products.o_id AND Supplier.s_id=Orders.Supplier_id AND Supplier_products.s_id=Orders.Supplier_id AND Supplier_products.s_id=Supplier.s_id AND Supplier_products.p_id=Order_products.p_id AND Supplier_products.p_id=Order_products.p_id AND SignUp_Data.email=User_access.email_id AND  User_access.pcategory=Products.p_category AND User_access.email_id='{email_id_access}'AND status<>'delivered';")
		for row in my_cursor_resetn:
			count_n=len(my_tree_n.get_children())	
			if count_n%2==0:
				my_tree_n.insert(parent='', index=count_n, iid=count_n, values=(row[0],row[1],row[2],row[3], row[4],row[5],row[6], row[7], row[8], row[9],row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20]), tags='evenrow')
			else:
				my_tree_n.insert(parent='', index=count_n, iid=count_n, values=(row[0],row[1],row[2],row[3], row[4],row[5],row[6], row[7], row[8], row[9],row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20]), tags='oddrow')
				
		my_tree_n.pack()
		Product_category_n.set('--Select--')
		ep_id_n.delete(0, END)
		epname_n.delete(0,END)
		equantity_n.delete(0,END)
		eprice_n.delete(0, END)
		ediscount_n.delete(0, END)
		discount_n.set(0)
		etax_n.delete(0, END)
		Tax_n.set(0)
		esupplier_n.delete(0, END)
		esupp_id_n.delete(0, END)
		eorder_id_n.delete(0, END)
		econtactno_n.delete(0, END)
		eemailid_n.delete(0, END)
		cal_n.delete(0, END) #Supp_date
		Pay_method_n.set('--Select--')
		etotal_amount_n.delete(0, END)
		eAmtpaid_n.delete(0, END)
		ebalance_n.delete(0, END)
		cal1_n.delete(0, END) #Due_date
		etransactionid_n.delete(0, END)
		equantityordered_n.delete(0, END)	
		estatus_n.delete(0, END)
	except mysql.connector.Error as e:
		messagebox.showerror("Failure",e)
	finally:
		if my_cursor_resetn is not None:
			my_cursor_resetn.close()	
			
email_id_access=''	
def LogIn():
	cursor=None
	my_cursor_login=mydb.cursor()
	try:
		username=entryUsername.get()
		p=entryPassword.get()
		sql = "SELECT email,password FROM SignUp_Data where email='"+str(username)+"' and password='"+str(p)+"';"
		my_cursor_login.execute(sql)
		data = my_cursor_login.fetchall()	
		numberofrows = my_cursor_login.rowcount
		if numberofrows==0:
			messagebox.showerror("ERROR","Username or Password did not match")
			entryUsername.delete(0, END)
			entryUsername.focus()
			entryPassword.delete(0, END)
		else:
			global email_id_access	
			email_id_access=username	
			xyz()
	except mysql.connector.Error as e:
		messagebox.showerror("Failure",e)
	finally:
		if my_cursor_login is not None:
			my_cursor_login.close()			

def SignUp():
	root.withdraw()
	SignUp.deiconify()

#Forgot Password-change password window 
def back_root():
	entUserid.delete(0, END)
	quest.set('--Your security question will be displayed here--')
	entSecuritya.delete(0, END)
	entNewPassword.delete(0, END)
	entconfirmnp.delete(0, END)
	ChangePassword.withdraw()
	root.deiconify()
	entryUsername.delete(0, END)
	entryPassword.delete(0, END)
	
def save_newpd():
	cursor=None
	my_cursor_savenpd=mydb.cursor()
	try:
		userid=entUserid.get()
		newp=entNewPassword.get()
		cpwd=entconfirmnp.get()
	
		if((newp.isalnum()==True) & (len(newp)>=6) & (len(newp)<=20)):
			n_pwd=newp
		else:
			messagebox.showerror("ERROR"," The password must contain minimum 6 and maximum 20 characters. It should be alphanumeric.") 
			entNewPassword.delete(0,END)
			entNewPassword.focus()
			return

		if(cpwd==n_pwd):
			n_cpwd=cpwd
			my_cursor_savenpd.execute("UPDATE SignUp_Data SET password='"+str(n_pwd)+"',cpassword='"+str(n_cpwd)+"' WHERE email='"+str(userid)+"';")
			mydb.commit()
			entUserid.delete(0, END)
			entUserid.focus()
			quest.set("--Your security question will be displayed here--")
			entSecuritya.delete(0, END)
			entNewPassword.delete(0,END)
			entconfirmnp.delete(0, END)
			messagebox.showinfo("Success","Password has been changed successfully")
		else:
			messagebox.showerror("Try Again","Your new password and confirm password did not match.\nPlease enter it again")
			entNewPassword.delete(0,END)
			entNewPassword.focus()
			entconfirmnp.delete(0, END)
			return	
			
	except mysql.connector.Error as e:
		messagebox.showerror("Failure",e)
	finally:
		if my_cursor_savenpd is not None:
			my_cursor_savenpd.close()
			
			
def window_ForgotPassword():
	root.withdraw()
	ChangePassword.deiconify()
	labelNewPassword.grid_forget()
	entNewPassword.grid_forget()
	labelconfirmnp.grid_forget()
	entconfirmnp.grid_forget()
	button_back.grid_forget()
	button_save.grid_forget()
	
def verify_ans():
	cursor=None
	my_cursor_verifyans=mydb.cursor()
	try:
		userid=entUserid.get()
		securityanswer=entSecuritya.get()
		my_cursor_verifyans.execute("SELECT sans FROM SignUp_Data WHERE email='"+str(userid)+"';")
		data_sans=my_cursor_verifyans.fetchall()
		if data_sans[0][0]==securityanswer:
			labelNewPassword.grid(row=3, column=0, pady=20)
			entNewPassword.grid(row=3, column=1, pady=20)
			labelconfirmnp.grid(row=4, column=0, pady=20)
			entconfirmnp.grid(row=4, column=1, pady=20)
			button_back.grid(row=5, column=0, pady=20)
			button_save.grid(row=5, column=1, pady=20)
		else:
			messagebox.showerror("Error","The security answer did not match.\nPlease try again")
			entSecuritya.delete(0,END)
			entSecuritya.focus()
	except mysql.connector.Error as e:
		messagebox.showerror("Failure",e)
	finally:
		if my_cursor_verifyans is not None:
			my_cursor_verifyans.close()		
			
def ForgotPassword():
	cursor=None
	my_cursor_forgotpd=mydb.cursor()
	try:
		userid=entUserid.get()
		userid=userid.strip()
		my_cursor_forgotpd.execute("SELECT email FROM SignUp_Data where email='"+str(userid)+"';")
		data=my_cursor_forgotpd.fetchall()
		numofrows = my_cursor_forgotpd.rowcount
		if numofrows<= 0:
			messagebox.showerror("ERROR","Username did not match")
			entryUsername.delete(0, END)
			entryUsername.focus()
		else:
			my_cursor_forgotpd.execute("SELECT sq FROM SignUp_Data WHERE email='"+str(userid)+"';")
			data_sq=my_cursor_forgotpd.fetchone()
			quest.set(data_sq[0])
	except mysql.connector.Error as e:
		messagebox.showerror("Failure",e)
	finally:
		if my_cursor_forgotpd is not None:
			my_cursor_forgotpd.close()
			
			
#ChangePassword window
ChangePassword=Toplevel(root)
ChangePassword.title("new password Page")
ChangePassword.geometry(f"{w}x{h}+0+0")	
ChangePassword.configure(background="#deddd1")
labelUserid=Label(ChangePassword, text='Username', width=15, font=('Arial', 12, 'bold'), bg="#deddd1")
labelUserid.grid(row=0, column=0, pady=20)
entUserid=Entry(ChangePassword, width=50, font=('Arial', 12, 'bold'))
entUserid.grid(row=0, column=1, pady=20)

quest=StringVar()
quest.set('--Your security question will be displayed here--')

labelSecurityq=Label(ChangePassword, text='Security Question', width=15, font=('Arial', 12, 'bold') , bg="#deddd1")
labelSecurityq.grid(row=1, column=0, pady=20)
entSecurityq=Entry(ChangePassword, textvariable=quest, width=50, font=('Arial', 12, 'bold'))
entSecurityq.grid(row=1, column=1, pady=20)

labelSecuritya=Label(ChangePassword, text='Security Answer', width=15, font=('Arial', 12, 'bold'), bg="#deddd1" )
labelSecuritya.grid(row=2, column=0, pady=20)
entSecuritya=Entry(ChangePassword, width=50, font=('Arial', 12, 'bold') )
entSecuritya.grid(row=2, column=1, pady=20)
labelNewPassword=Label(ChangePassword,text='New Password', width=15, font=('Arial', 12, 'bold'), bg="#deddd1")
labelNewPassword.grid(row=3, column=0, pady=20)
entNewPassword=Entry(ChangePassword, width=50, font=('Arial', 12, 'bold'), show="*")
entNewPassword.grid(row=3, column=1, pady=20)
labelconfirmnp=Label(ChangePassword, text='Confirm Password', width=15, font=('Arial', 12, 'bold'), bg="#deddd1")
labelconfirmnp.grid(row=4, column=0, pady=20)
entconfirmnp=Entry(ChangePassword, width=50, font=('Arial', 12, 'bold'),show="*")
entconfirmnp.grid(row=4, column=1, pady=20)
				
button_back=Button(ChangePassword, width=14, text='BACK', font=('Arial', 12, 'bold'), bg="#A0F8E7", command=back_root)
button_back.grid(row=5, column=0, pady=20)
button_save=Button(ChangePassword, width=14, text='SAVE', font=('Arial', 12, 'bold'),bg="#A0F8E7", command=save_newpd)
button_save.grid(row=5, column=1, pady=20)
			
buttonproceed=Button(ChangePassword, width=10, text='Proceed',font=('Arial', 12), bg="#A0F8E7", command=ForgotPassword)
buttonproceed.grid(row=0, column=2, pady=20, padx=10)

buttoncheck=Button(ChangePassword, width=10, text='Check',font=('Arial', 12), bg="#A0F8E7",  command=verify_ans)
buttoncheck.grid(row=2, column=2, pady=20, padx=10)		
ChangePassword.withdraw()

#Log in window widgets			
labelUsername=Label(Rightframe, width=20, font=('Arial', 12, 'bold'),bg='#E9E7D0', fg="blue",text='Username:')
labelUsername.grid(row=0, column=0, pady=4)
entryUsername=Entry(Rightframe, bd=2, width=30, font=('Arial', 12), relief=SUNKEN)
entryUsername.grid(row=0, column=1, padx=2)
labelPassword=Label(Rightframe, width=20, font=('Arial', 12, 'bold'), bg='#E9E7D0', fg="blue",text='Password:')
labelPassword.grid(row=1, column=0,pady=20)
entryPassword=Entry(Rightframe, bd=2, width=30, font=('Arial', 12), show="*", relief=SUNKEN)
entryPassword.grid(row=1, column=1, pady=20, padx=2 )

button1=Button(Rightframe, bd=4, width=15, text='Sign Up',font=('Arial', 12, 'bold'), bg="#AFE0CE", fg="blue", relief=RAISED, command=SignUp)
button1.grid(row=3, column=0)
button2=Button(Rightframe, bd=4, width=13, text='Login',font=('Arial', 12, 'bold'), bg="#AFE0CE", fg="blue", relief=RAISED, command=LogIn)
button2.grid(row=3, column=2)
button3=Button(Rightframe, bd=4, width=15, text='Forgot Password',font=('Arial', 12), bg="#AFE0CE",fg="blue", relief=RAISED, command=window_ForgotPassword)
button3.grid(row=4, column=1, pady=4)


#SIGN UP WINDOW
	
SignUp=Toplevel(root)
SignUp.title("SignUp Page")
SignUp.geometry(f"{w}x{h}+0+0")
SignUp.configure(background="#deddd1")

emailRegex=re.compile(r'[\w\.-]+@[\w\.-]+')
def checkEmail(email):  
	if(re.search(emailRegex,email)):  
		return True  
	else:  
		return False
		
def Back_from_SignUp():
	entFirstName.delete(0,END)
	entLastName.delete(0,END)
	entEmail.delete(0,END)
	entContactNo.delete(0,END)
	#omenu.set('--Select--')
	qchoosen.set('--Select--')
	entSecurityA.delete(0,END)
	entPassword.delete(0,END)
	entConfirmPassword.delete(0,END)
	SignUp.withdraw()
	root.deiconify()
	entryUsername.delete(0, END)
	entryPassword.delete(0, END)
	
def save_signup_data():
	cursor=None
	my_cursor_save=mydb.cursor()
	try:
		sql="INSERT INTO SignUp_Data VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
		fname=entFirstName.get()
		if((fname.isalpha()==True) & (len(fname)>1)):
			firstname=fname
		else:
			messagebox.showerror("ERROR","Name length cannot be less than 2 characters and name should contain only alphabets")
			entFirstName.delete(0,END)
			entFirstName.focus()
			return
			
		lname=entLastName.get()
		if((lname.isalpha()==True) & (len(lname)>1)):
			lastname=lname
		else:
			messagebox.showerror("ERROR","Name length cannot be less than 2 characters and name should contain only alphabets")
			entLastName.delete(0,END)
			entLastName.focus()
			return

		email=entEmail.get()
		
		if(checkEmail(email)):
			emailid=email
		else:
			messagebox.showerror('ERROR','Please enter a valid email address' )
			entEmail.delete(0, END)
			entEmail.focus()

		mobile_no=entContactNo.get()
		if((mobile_no.isnumeric()==True) & (len(mobile_no)==10)):
			contact_no=mobile_no
		else:
			messagebox.showerror("ERROR","The mobile number should contain only numbers and only 10 numbers")
			entContactNo.delete(0,END)
			entContactNo.focus()
			return
		
		sq=qchoosen.get()
		if((sq=='--Select--') | (sq=='')):
			messagebox.showerror("ERROR","Choose a security question")
			return
		else:
			securityq=sq
		
		sans=entSecurityA.get()
		if((sans=='') | (len(sans)<=1)):
			messagebox.showerror("ERROR"," Write a security ans") 
			entSecurityA.delete(0,END)
			entSecurityA.focus()
			return
		else:
			securitya=sans
			
		password=entPassword.get()
		if((password.isalnum()==True) & (len(password)>=6) & (len(password)<=20)):
			pwd=password
		else:
			messagebox.showerror("ERROR"," The password must contain minimum 6 and maximum 20 characters. It should be alphanumeric.") 
			entPassword.delete(0,END)
			entPassword.focus()
			return
		
		confirmpassword=entConfirmPassword.get()
		if(confirmpassword==password):
			c_pwd=confirmpassword
		else:
			messagebox.showerror("ERROR","Password did not match")
			entConfirmPassword.delete(0, END)
			entConfirmPassword.focus()
			return
		

		args=(firstname, lastname, emailid, contact_no,securityq,securitya,pwd, c_pwd)
		my_cursor_save.execute(sql, args)
		mydb.commit()
		for i in Pcategory.curselection():
			print(Pcategory.get(i))
			p1=Pcategory.get(i)
			my_cursor_save.execute(f"INSERT INTO User_access (email_id, pcategory) VALUES('{emailid}', '{p1}');")
			mydb.commit()
		msg=str(my_cursor_save.rowcount)+"record(s) inserted"
		messagebox.showinfo("Success", msg)
		entFirstName.delete(0,END)
		entLastName.delete(0,END)
		entEmail.delete(0,END)
		entContactNo.delete(0,END)
		qchoosen.set('--Select--')
		entSecurityA.delete(0,END)
		entPassword.delete(0,END)
		entConfirmPassword.delete(0,END)
		Pcategory.delete(0, END)
	except mysql.connector.Error as e:
		messagebox.showerror("Failure",e)


	finally:
		if my_cursor_save is not None:
			my_cursor_save.close()
		
arial14 = tkFont.Font(family='arial', size=14)
labelFirstName=Label(SignUp, text='First Name:', width=15, font=('Arial', 12, 'bold'), bg="#deddd1")
labelFirstName.grid(row=0, column=0, pady=10)
labelLastName=Label(SignUp, text='Last Name:', width=15, font=('Arial', 12, 'bold'), bg="#deddd1")
labelLastName.grid(row=1, column=0, pady=10)
labelEmail=Label(SignUp, text='Email id:', width=15, font=('Arial', 12, 'bold'), bg="#deddd1")
labelEmail.grid(row=2, column=0, pady=10)
labelContactNo=Label(SignUp, text='ContactNo:', width=15, font=('Arial', 12, 'bold'), bg="#deddd1")
labelContactNo.grid(row=3, column=0, pady=10)
labelSecurityQ=Label(SignUp, text='Security Question:', width=15, font=('Arial', 12, 'bold'), bg="#deddd1")
labelSecurityQ.grid(row=4, column=0, pady=10)
labelSecurityA=Label(SignUp, text='Security Answer:', width=15, font=('Arial', 12, 'bold'), bg="#deddd1")
labelSecurityA.grid(row=5, column=0, pady=10)
labelPassword=Label(SignUp, text='Password:', width=15, font=('Arial', 12, 'bold'), bg="#deddd1")
labelPassword.grid(row=6, column=0, pady=10)
labelConfirmPassword=Label(SignUp, text='Confirm Password:', width=15, font=('Arial', 12, 'bold'), bg="#deddd1")
labelConfirmPassword.grid(row=7, column=0, pady=10)
labelPcategory=Label(SignUp, text='Product Category:', width=15, font=('Arial', 12, 'bold'), bg="#deddd1")
labelPcategory.grid(row=8, column=0, pady=10)

entFirstName=Entry(SignUp, width=50, font=('Arial', 12, 'bold'))
entFirstName.grid(row=0, column=1, pady=10, padx=3)
entLastName=Entry(SignUp, width=50, font=('Arial', 12, 'bold'))
entLastName.grid(row=1, column=1, pady=10, padx=3)
entEmail=Entry(SignUp, width=50, font=('Arial', 12, 'bold'))
entEmail.grid(row=2, column=1, pady=10, padx=3)
entContactNo=Entry(SignUp, width=50, font=('Arial', 12, 'bold'))
entContactNo.grid(row=3, column=1, pady=10, padx=3)

n = tk.StringVar()
qchoosen = ttk.Combobox(SignUp, width = 73, textvariable = n)  
# Adding combobox drop down list
qchoosen['values'] = ('--Select--',"What is the name of your first School?", "What is your favourite food?", "what was the name of your 1st teacher", "What is the name of your pet?")
qchoosen.grid(row=4, column=1, pady=10, padx=3)
qchoosen.current(0)

entSecurityA=Entry(SignUp, width=50, font=('Arial', 12, 'bold'))
entSecurityA.grid(row=5, column=1, pady=10, padx=3)
entPassword=Entry(SignUp, width=50, font=('Arial', 12, 'bold'), show="*")
entPassword.grid(row=6, column=1, pady=10, padx=3)
entConfirmPassword=Entry(SignUp, width=50, font=('Arial', 12, 'bold'), show="*")
entConfirmPassword.grid(row=7, column=1, pady=10, padx=3)
access=StringVar()
Pcategory=Listbox(SignUp, selectmode="extended", width=73)
Pcategory.insert(1,"Decor")
Pcategory.insert(2,"Food")
Pcategory.insert(3,"Soaps")
Pcategory.insert(4,"Stationary")
Pcategory.grid(row=8, column=1, pady=10, padx=3)

buttonback=Button(SignUp, width=20, text='BACK', font=('Arial', 12, 'bold'), bg="#A0F8E7",  command=Back_from_SignUp)
buttonback.grid(row=9, column=0, pady=10, padx=3)

buttonsave=Button(SignUp, width=20, text='SAVE', font=('Arial', 12, 'bold'), bg="#A0F8E7",  command=save_signup_data)
buttonsave.grid(row=9, column=1, pady=10, padx=3)
SignUp.withdraw()

#Frames on super window
Mainframe=Frame(super, width=w, height=h, bg="#deddd1", relief=RIDGE)
Mainframe.grid()
Topframe1= Frame(Mainframe, bd=3, width=w, height=320, bg="#deddd1", relief=RIDGE)
Topframe1.grid(row=0, column=0, sticky=N+S+W)
Topframe2= Frame(Mainframe, bd=3, width=w, height=60, bg="#deddd1", relief=RIDGE)
Topframe2.grid(row=1, column=0, pady=3)
Topframe3= Frame(Mainframe, bd=3, width=w, bg="#deddd1", relief=RIDGE)
Topframe3.grid(row=2, column=0)

#widgets of super window
lpcategory=Label(Topframe1, font=('arial',10,'bold'), text="Product Category", width=20, bg="#deddd1")
lpcategory.grid(row=0,column=0,pady=3,sticky=W)

category_choosen = ttk.Combobox(Topframe1, width =39 ,textvariable = Product_category)  
# Adding combobox drop down list
category_choosen['values'] = ('--Select--',"Decor", "Food", "Soaps", "Stationary")
category_choosen.grid(row=0, column=1, pady=3, padx=2, sticky=W)
category_choosen.current(0)

lp_id=Label(Topframe1, font=('arial',10,'bold'), text="Product Id", width=20, bg="#deddd1")
lp_id.grid(row=0,column=2,pady=3,sticky=W)
ep_id=Entry(Topframe1, width= 25,font=('Arial', 12), bd=3, textvariable=Product_id, relief=SUNKEN)
ep_id.grid(row=0, column=3, pady=3, padx=2, sticky=W)

lpname=Label(Topframe1, font=('arial',10,'bold'), text="Product Name", width=20, bg="#deddd1")
lpname.grid(row=0,column=4,pady=3, sticky=W)
epname=Entry(Topframe1, width=30,font=('arial',12), bd=3, textvariable=Product_name, relief=SUNKEN)
epname.grid(row=0,column=5,pady=3, padx=2, sticky=W)

lquantity=Label(Topframe1, font=('arial',10,'bold'), text="Quantity available", width=20, bg="#deddd1")
lquantity.grid(row=1,column=0,pady=3, sticky=W)
equantity=Entry(Topframe1, width=25, font=('arial',12), bd=3, textvariable=Quantity_avl, relief=SUNKEN)
equantity.grid(row=1,column=1,pady=3, padx=2, sticky=W)

lprice=Label(Topframe1, font=('arial',10,'bold'), text="Price/item(₹)",width=20, bg="#deddd1")
lprice.grid(row=1,column=2,pady=3, sticky=W)
eprice=Entry(Topframe1, width=25, font=('arial',12), bd=3, textvariable=Price_item, relief=SUNKEN)
eprice.grid(row=1,column=3,pady=3,padx=2,sticky=W)

ldiscount=Label(Topframe1, font=('arial',10,'bold'), text="Discount(%)", width=20, bg="#deddd1")
ldiscount.grid(row=1,column=4,pady=3, sticky=W)
ediscount=Entry(Topframe1, width=30,font=('arial',12), bd=3, textvariable=discount, relief=SUNKEN)
ediscount.grid(row=1,column=5,pady=3, padx=2, sticky=W)

ltax=Label(Topframe1, font=('arial',10,'bold'), text="Tax(₹)", width=20, bg="#deddd1")
ltax.grid(row=2,column=0,pady=3, sticky=W)
etax=Entry(Topframe1, width=25, font=('arial',12), bd=3, textvariable=Tax, relief=SUNKEN)
etax.grid(row=2,column=1,pady=3, padx=2, sticky=W)

lsupplier=Label(Topframe1, font=('arial',10,'bold'), text="Supplier",width=20, bg="#deddd1")
lsupplier.grid(row=2,column=2,pady=3, sticky=W)
esupplier=Entry(Topframe1, width=25, font=('arial',12), bd=3,textvariable=Supplier, relief=SUNKEN)
esupplier.grid(row=2,column=3,pady=3,padx=2,sticky=W)

lorder_id=Label(Topframe1, font=('arial',10,'bold'), text="Order Id",width=20, bg="#deddd1")
lorder_id.grid(row=2,column=4,pady=3, sticky=W)
eorder_id=Entry(Topframe1, width=30, font=('arial',12), bd=3, textvariable=Order_id, relief=SUNKEN)
eorder_id.grid(row=2,column=5,pady=3,padx=2,sticky=W)

lcontactno=Label(Topframe1, font=('arial',10,'bold'), text="Supplier Contact No.", width=20, bg="#deddd1")
lcontactno.grid(row=3,column=0,pady=3, sticky=W)
econtactno=Entry(Topframe1, width=25,font=('arial',12), bd=3,textvariable=Supp_contactNo, relief=SUNKEN)
econtactno.grid(row=3,column=1,pady=3, padx=2, sticky=W)

lemailid=Label(Topframe1, font=('arial',10,'bold'), text="Supplier email id", width=20, bg="#deddd1")
lemailid.grid(row=3,column=2,pady=3, sticky=W)
eemailid=Entry(Topframe1, width=25, font=('arial',12), bd=3, textvariable=Supp_emailid, relief=SUNKEN)
eemailid.grid(row=3,column=3,pady=3, padx=2, sticky=W)

lsupplied_date=Label(Topframe1, font=('arial',10,'bold'), text="Supplied Date",width=20, bg="#deddd1")
lsupplied_date.grid(row=3,column=4,pady=3, sticky=W)
cal=DateEntry(Topframe1,font=('arial',10), selectmode='day', year=2021, month=1, date_pattern='yyyy/mm/dd', width=33, selectbackground='#A0F8E7', background="#A0F8E7", foreground='black', selectforeground="black", bd=3, textvariable=Supp_date, relief=SUNKEN)
cal.grid(row=3, column=5, pady=3, padx=2, sticky=W)
cal.delete(0, END)

lpaymethod=Label(Topframe1, font=('arial',10,'bold'), text="Payment Method", width=20, bg="#deddd1")
lpaymethod.grid(row=4,column=0,pady=3, sticky=W)

paymethod_choosen = ttk.Combobox(Topframe1, width =39 ,textvariable =Pay_method)  
# Adding combobox drop down list
paymethod_choosen['values'] = ('--Select--',"Cash", "Cheque", "NEFT", "Pay Order", "UPI")
paymethod_choosen.grid(row=4, column=1, pady=3, padx=2, sticky=W)
paymethod_choosen.current(0)

ltotal_amount=Label(Topframe1, font=('arial',10,'bold'), text="Total Amount(₹)", width=20, bg="#deddd1")
ltotal_amount.grid(row=4,column=2,pady=3, sticky=W)
etotal_amount=Entry(Topframe1, width=25, font=('arial',12), bd=3, textvariable=Total_amt, relief=SUNKEN)
etotal_amount.grid(row=4,column=3,pady=3, padx=2, sticky=W)

lAmtpaid=Label(Topframe1, font=('arial',10,'bold'), text="Amount paid(₹)",width=20, bg="#deddd1")
lAmtpaid.grid(row=4,column=4,pady=3, sticky=W)
eAmtpaid=Entry(Topframe1, width=30, font=('arial',12), bd=3, textvariable=Amt_paid, relief=SUNKEN)
eAmtpaid.grid(row=4,column=5,pady=3,padx=2,sticky=W)

lbalance=Label(Topframe1, font=('arial',10,'bold'), text="Balance(₹)", width=20, bg="#deddd1")
lbalance.grid(row=5,column=0,pady=3, sticky=W)
ebalance=Entry(Topframe1, width=25,font=('arial',12), bd=3, textvariable=Balance, relief=SUNKEN)
ebalance.grid(row=5,column=1,pady=3, padx=2, sticky=W)

lduedate=Label(Topframe1, font=('arial',10,'bold'), text="Due Date", width=20, bg="#deddd1")
lduedate.grid(row=5,column=2,pady=3, sticky=W)
cal1=DateEntry(Topframe1,font=('arial',10), selectmode='day', year=2021, month=1, date_pattern='yyyy/mm/dd', width=29, selectbackground='#A0F8E7', background="#A0F8E7", foreground='black', selectforeground="black", bd=3, textvariable=Due_date, relief=SUNKEN)
cal1.grid(row=5, column=3, pady=3, padx=2, sticky=W)
cal1.delete(0, END)

ltransactionid=Label(Topframe1, font=('arial',10,'bold'), text="Transaction Id",width=20, bg="#deddd1")
ltransactionid.grid(row=5,column=4,pady=3, sticky=W)
etransactionid=Entry(Topframe1, width=30, font=('arial',12), bd=3, textvariable=Transaction_id, relief=SUNKEN)
etransactionid.grid(row=5,column=5,pady=3,padx=2,sticky=W)

lquantitysupplied=Label(Topframe1, font=('arial',10,'bold'), text="Quantity Supplied",width=20, bg="#deddd1")
lquantitysupplied.grid(row=6,column=0,pady=3, sticky=W)
equantitysupplied=Entry(Topframe1, width=25, font=('arial',12), bd=3, textvariable=Quantity_supp, relief=SUNKEN)
equantitysupplied.grid(row=6,column=1,pady=3,padx=2,sticky=W)

lstatus=Label(Topframe1, font=('arial',10,'bold'), text="Status", width=20, bg="#deddd1")
lstatus.grid(row=6,column=2,pady=3, sticky=W)
estatus=Entry(Topframe1, width=25, font=('arial',12), bd=3, textvariable=status, relief=SUNKEN)
estatus.grid(row=6,column=3,pady=3,padx=2,sticky=W)

lsupp_id=Label(Topframe1, font=('arial',10,'bold'), text="Supplier id", width=20, bg="#deddd1")
lsupp_id.grid(row=6,column=4,pady=3, sticky=W)
esupp_id=Entry(Topframe1, width=30, font=('arial',12), bd=3, textvariable=SupplierId_1, relief=SUNKEN)
esupp_id.grid(row=6,column=5,pady=3,padx=2,sticky=W)

binsert=Button(Topframe2, font=('arial',10,'bold'), bg="#A0F8E7", text='INSERT',width=20, bd=2, relief=RAISED, command=insertdata)
binsert.grid(row=0, column=0, pady=5, padx=3)

bsearch=Button(Topframe2, font=('arial',10,'bold'), bg="#A0F8E7", text='SEARCH', width=21, bd=2, relief=RAISED, command=display)
bsearch.grid(row=0, column=1, pady=5, padx=3)

bupdate=Button(Topframe2, font=('arial',10,'bold'), bg="#A0F8E7", text='UPDATE', width=21, bd=2, relief=RAISED, command=update)
bupdate.grid(row=0, column=2, pady=5, padx=3)

bdelete=Button(Topframe2, font=('arial',10,'bold'), bg="#A0F8E7", text='DELETE', width=21, bd=2, relief=RAISED, command=delete)
bdelete.grid(row=0, column=3, pady=5, padx=3)

bselect=Button(Topframe2, font=('arial',10,'bold'), bg="#A0F8E7", text='SELECT', width=21, bd=2, relief=RAISED, command=select)
bselect.grid(row=0, column=4, pady=5, padx=3)

bback=Button(Topframe2, font=('arial',10,'bold'), bg="#A0F8E7", text='BACK', width=21, bd=2, relief=RAISED,  command=back_root_super)
bback.grid(row=0, column=5, pady=5, padx=3)

breset=Button(Topframe2, font=('arial',10,'bold'), bg="#A0F8E7", text='RESET', width=20, bd=2, relief=RAISED, command=reset)
breset.grid(row=0, column=6, pady=5, padx=3)

Topframe3.columnconfigure(0, weight=1)

my_menu=Menu(super)
super.config(menu=my_menu)
file_menu=Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Order placed information", command=order_placed)
file_menu.add_command(label="Log out", command=logout_stock)

style=ttk.Style()
style.theme_use('default')
style.configure("Treeview",background="#d3d3d3", foreground="black", rowheight=25, fieldbackground="#D3D3D3", font=('Helvetica',9))
style.map('Treeview',background=[('selected','#347083')])  

style.configure("Treeview.Heading",  background="#D7FFF2", font=('Arial',10, 'bold')) # Modify the font, colour of the headings

tree_frame=Frame(Topframe3, width=w-800,bg="#deddd1")
tree_frame.pack(pady=10)

tree_scroll_y=Scrollbar(tree_frame, orient=VERTICAL)
tree_scroll_y.pack(side=RIGHT, fill=Y)
tree_scroll_x=Scrollbar(tree_frame, orient=HORIZONTAL)
tree_scroll_x.pack(side=BOTTOM, fill=X)

my_tree=ttk.Treeview(tree_frame, height=12, yscrollcommand=tree_scroll_y.set, xscrollcommand=tree_scroll_x.set, selectmode="extended")

my_tree['columns']=("Product Category", "Product ID", "Product Name", "Quantity available", "Price/item","Quantity supplied", "Supplied Date", "Discount","Tax", "Total Amount", "Amount Paid", "Payment method", "Transaction id","Balance", "Due Date",  "Supplier", "Supp Id", "Order id", "Supplier Contact No.", "Supplier email id", "Status")
tree_scroll_y.configure(command=my_tree.yview)
tree_scroll_x.configure(command=my_tree.xview)
my_tree.pack()

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Product Category", anchor=W, width=80)
my_tree.column("Product ID", anchor=W, width=60 )
my_tree.column("Product Name", anchor=W, width=84)
my_tree.column("Quantity available", anchor=W, width=39)
my_tree.column("Price/item", anchor=W, width=65)
my_tree.column("Quantity supplied", anchor=W, width=60)
my_tree.column("Supplied Date", anchor=W, width=65)
my_tree.column("Discount", anchor=W, width=46)
my_tree.column("Tax", anchor=W, width=40)
my_tree.column("Total Amount", anchor=W, width=80)
my_tree.column("Amount Paid", anchor=W, width=65)
my_tree.column("Payment method", anchor=W, width=60)
my_tree.column("Transaction id", anchor=W, width=90)
my_tree.column("Balance", anchor=W, width=46)
my_tree.column("Due Date", anchor=W, width=65)
my_tree.column("Supplier", anchor=W, width=50)
my_tree.column("Supp Id", anchor=W, width=30)
my_tree.column("Order id", anchor=W, width=44)
my_tree.column("Supplier Contact No.", anchor=W, width=80)
my_tree.column("Supplier email id", anchor=W, width=75)
my_tree.column("Status", anchor=W, width=25)

my_tree.heading("#0",text="", anchor=W)
my_tree.heading("Product Category",text="Category", anchor=W)
my_tree.heading("Product ID",text="ID",anchor=W)
my_tree.heading("Product Name",text="Name", anchor=W)
my_tree.heading("Quantity available", text="Qty avl",anchor=W)
my_tree.heading("Price/item", text="Price/item",anchor=W)
my_tree.heading("Quantity supplied", text="Qty supp", anchor=W)
my_tree.heading("Supplied Date", text="S Date", anchor=W)
my_tree.heading("Discount", text="Discount",anchor=W)
my_tree.heading("Tax", text="Tax", anchor=W)
my_tree.heading("Total Amount", text="Total Amt", anchor=W)
my_tree.heading("Amount Paid", text="Amt Paid", anchor=W)
my_tree.heading("Payment method", text="Pay method", anchor=W)
my_tree.heading("Transaction id", text="Transaction id", anchor=W)
my_tree.heading("Balance", text="Bal", anchor=W)
my_tree.heading("Due Date", text="Due Date", anchor=W)
my_tree.heading("Supplier", text="Supplier",anchor=W)
my_tree.heading("Supp Id", text="Supp Id", anchor=W)
my_tree.heading("Order id", text="Order id",anchor=W)
my_tree.heading("Supplier Contact No.", text="S Contact No.", anchor=W)
my_tree.heading("Supplier email id", text="S email id", anchor=W)
my_tree.heading("Status", text="Status", anchor=W)
my_tree['show']='headings'

my_tree.tag_configure('oddrow',background="#A0F8E7")
my_tree.tag_configure('evenrow',background="white")

my_cursor.execute(f"SELECT  p_category, Products.p_id, p_name, qavl, price, q_ordered, ddate, discount, tax, cost, amt_paid, pay_method, transaction_id, balance, duedate, s_name, Supplier.s_id, Orders.Order_id, s_contactno, s_emailid,status FROM Products, Orders, Supplier, Order_products, Supplier_products, SignUp_Data, User_access WHERE Products.p_id = Order_products.p_id AND Supplier_products.p_id = Products.p_id AND Orders.Order_id = Order_products.o_id AND Supplier.s_id=Orders.Supplier_id AND Supplier_products.s_id=Orders.Supplier_id AND Supplier_products.s_id=Supplier.s_id AND Supplier_products.p_id=Order_products.p_id AND Supplier_products.p_id=Order_products.p_id AND  SignUp_Data.email=User_access.email_id AND  User_access.pcategory=Products.p_category AND User_access.email_id='{email_id_access}' AND status='delivered';")
for row in my_cursor:
	count=len(my_tree.get_children())	
			
	if count%2==0:
		my_tree.insert(parent='', index=count, iid=count, values=(row[0],row[1],row[2],row[3], row[4],row[5],row[6], row[7], row[8], row[9],row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20]), tags='evenrow')
	else:
		my_tree.insert(parent='', index=count, iid=count, values=(row[0],row[1],row[2],row[3], row[4],row[5],row[6], row[7], row[8], row[9],row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20]), tags='oddrow')
				
	my_tree.pack()

#super 2 window widgets
super2=Toplevel(super)
super2.title("Order Placed Information ")
super2.geometry(f"{w}x{h}+0+0")	
super2.configure(background="#deddd1")
super2.withdraw()

Mainframe_neworder=Frame(super2, width=w, height=h, bg="#E9E7D0", relief=RIDGE)
Mainframe_neworder.grid()
Topframe1_neworder= Frame(Mainframe_neworder, bd=3, width=w, height=320, bg="#deddd1", relief=RIDGE)
Topframe1_neworder.grid(row=0, column=0, sticky=N+S+W, padx=2)
Topframe2_neworder= Frame(Mainframe_neworder, bd=3, width=w, height=60, bg="#deddd1", relief=RIDGE)
Topframe2_neworder.grid(row=1, column=0, pady=3, padx=2)
Topframe3_neworder= Frame(Mainframe_neworder, bd=3, width=w, bg="#deddd1", relief=RIDGE)
Topframe3_neworder.grid(row=2, column=0, padx=2)

#widgets
lpcategory_n=Label(Topframe1_neworder, font=('arial',10,'bold'), text="Product Category", width=20, bg="#deddd1")
lpcategory_n.grid(row=0,column=0,pady=3,sticky=W)

category_choosen_n = ttk.Combobox(Topframe1_neworder, width =39 ,textvariable = Product_category_n)  
# Adding combobox drop down list
category_choosen_n['values'] = ('--Select--',"Decor", "Food", "Soaps", "Stationary")
category_choosen_n.grid(row=0, column=1, pady=3, padx=2, sticky=W)
category_choosen_n.current(0)

lp_id_n=Label(Topframe1_neworder, font=('arial',10,'bold'), text="Product Id", width=20, bg="#deddd1")
lp_id_n.grid(row=0,column=2,pady=3,sticky=W)
ep_id_n=Entry(Topframe1_neworder, width= 25,font=('Arial', 12), bd=3, textvariable=Product_id_n, relief=SUNKEN)
ep_id_n.grid(row=0, column=3, pady=3, padx=2, sticky=W)

lpname_n=Label(Topframe1_neworder, font=('arial',10,'bold'), text="Product Name", width=20, bg="#deddd1")
lpname_n.grid(row=0,column=4,pady=3, sticky=W)
epname_n=Entry(Topframe1_neworder, width=30,font=('arial',12), bd=3, textvariable=Product_name_n, relief=SUNKEN)
epname_n.grid(row=0,column=5,pady=3, padx=2, sticky=W)

lquantity_n=Label(Topframe1_neworder, font=('arial',10,'bold'), text="Quantity available", width=20, bg="#deddd1")
lquantity_n.grid(row=1,column=0,pady=3, sticky=W)
equantity_n=Entry(Topframe1_neworder, width=25, font=('arial',12), bd=3, textvariable=Quantity_avl_n, relief=SUNKEN)
equantity_n.grid(row=1,column=1,pady=3, padx=2, sticky=W)

lprice_n=Label(Topframe1_neworder, font=('arial',10,'bold'), text="Price/item(₹)",width=20, bg="#deddd1")
lprice_n.grid(row=1,column=2,pady=3, sticky=W)
eprice_n=Entry(Topframe1_neworder, width=25, font=('arial',12), bd=3, textvariable=Price_item_n, relief=SUNKEN)
eprice_n.grid(row=1,column=3,pady=3,padx=2,sticky=W)

ldiscount_n=Label(Topframe1_neworder, font=('arial',10,'bold'), text="Discount(%)", width=20, bg="#deddd1")
ldiscount_n.grid(row=1,column=4,pady=3, sticky=W)
ediscount_n=Entry(Topframe1_neworder, width=30,font=('arial',12), bd=3, textvariable=discount_n, relief=SUNKEN)
ediscount_n.grid(row=1,column=5,pady=3, padx=2, sticky=W)

ltax_n=Label(Topframe1_neworder, font=('arial',10,'bold'), text="Tax(₹)", width=20, bg="#deddd1")
ltax_n.grid(row=2,column=0,pady=3, sticky=W)
etax_n=Entry(Topframe1_neworder, width=25, font=('arial',12), bd=3, textvariable=Tax_n, relief=SUNKEN)
etax_n.grid(row=2,column=1,pady=3, padx=2, sticky=W)

lsupplier_n=Label(Topframe1_neworder, font=('arial',10,'bold'), text="Supplier",width=20, bg="#deddd1")
lsupplier_n.grid(row=2,column=2,pady=3, sticky=W)
esupplier_n=Entry(Topframe1_neworder, width=25, font=('arial',12), bd=3,textvariable=Supplier_n, relief=SUNKEN)
esupplier_n.grid(row=2,column=3,pady=3,padx=2,sticky=W)

lorder_id_n=Label(Topframe1_neworder, font=('arial',10,'bold'), text="Order Id",width=20, bg="#deddd1")
lorder_id_n.grid(row=2,column=4,pady=3, sticky=W)
eorder_id_n=Entry(Topframe1_neworder, width=30, font=('arial',12), bd=3, textvariable=Order_id_n, relief=SUNKEN)
eorder_id_n.grid(row=2,column=5,pady=3,padx=2,sticky=W)

lcontactno_n=Label(Topframe1_neworder, font=('arial',10,'bold'), text="Supplier Contact No.", width=20, bg="#deddd1")
lcontactno_n.grid(row=3,column=0,pady=3, sticky=W)
econtactno_n=Entry(Topframe1_neworder, width=25,font=('arial',12), bd=3,textvariable=Supp_contactNo_n, relief=SUNKEN)
econtactno_n.grid(row=3,column=1,pady=3, padx=2, sticky=W)

lemailid_n=Label(Topframe1_neworder, font=('arial',10,'bold'), text="Supplier email id", width=20, bg="#deddd1")
lemailid_n.grid(row=3,column=2,pady=3, sticky=W)
eemailid_n=Entry(Topframe1_neworder, width=25, font=('arial',12), bd=3, textvariable=Supp_emailid_n, relief=SUNKEN)
eemailid_n.grid(row=3,column=3,pady=3, padx=2, sticky=W)

lorderdel_date_n=Label(Topframe1_neworder, font=('arial',10,'bold'), text="Delivery Date",width=20, bg="#deddd1")
lorderdel_date_n.grid(row=3,column=4,pady=3, sticky=W)
cal_n=DateEntry(Topframe1_neworder,font=('arial',10), selectmode='day', year=2021, month=1, date_pattern='yyyy/mm/dd', width=33, selectbackground='#A0F8E7', background="#A0F8E7", foreground='black', selectforeground="black", bd=3, textvariable=Orderdel_date_n, relief=SUNKEN)
cal_n.grid(row=3, column=5, pady=3, padx=2, sticky=W)
cal_n.delete(0, END)

lpaymethod_n=Label(Topframe1_neworder, font=('arial',10,'bold'), text="Payment Method", width=20, bg="#deddd1")
lpaymethod_n.grid(row=4,column=0,pady=3, sticky=W)

paymethod_choosen_n = ttk.Combobox(Topframe1_neworder, width =39 ,textvariable =Pay_method_n)  
# Adding combobox drop down list
paymethod_choosen_n['values'] = ('--Select--',"Cash", "Cheque", "NEFT", "Pay Order", "UPI")
paymethod_choosen_n.grid(row=4, column=1, pady=3, padx=2, sticky=W)
paymethod_choosen_n.current(0)

ltotal_amount_n=Label(Topframe1_neworder, font=('arial',10,'bold'), text="Total Amount(₹)", width=20, bg="#deddd1")
ltotal_amount_n.grid(row=4,column=2,pady=3, sticky=W)
etotal_amount_n=Entry(Topframe1_neworder, width=25, font=('arial',12), bd=3, textvariable=Total_amt_n, relief=SUNKEN)
etotal_amount_n.grid(row=4,column=3,pady=3, padx=2, sticky=W)

lAmtpaid_n=Label(Topframe1_neworder, font=('arial',10,'bold'), text="Amount paid(₹)",width=20, bg="#deddd1")
lAmtpaid_n.grid(row=4,column=4,pady=3, sticky=W)
eAmtpaid_n=Entry(Topframe1_neworder, width=30, font=('arial',12), bd=3, textvariable=Amt_paid_n, relief=SUNKEN)
eAmtpaid_n.grid(row=4,column=5,pady=3,padx=2,sticky=W)

lbalance_n=Label(Topframe1_neworder, font=('arial',10,'bold'), text="Balance(₹)", width=20, bg="#deddd1")
lbalance_n.grid(row=5,column=0,pady=3, sticky=W)
ebalance_n=Entry(Topframe1_neworder, width=25,font=('arial',12), bd=3, textvariable=Balance_n, relief=SUNKEN)
ebalance_n.grid(row=5,column=1,pady=3, padx=2, sticky=W)

lduedate_n=Label(Topframe1_neworder, font=('arial',10,'bold'), text="Due Date", width=20, bg="#deddd1")
lduedate_n.grid(row=5,column=2,pady=3, sticky=W)
cal1_n=DateEntry(Topframe1_neworder,font=('arial',10), selectmode='day', year=2021, month=1, date_pattern='yyyy/mm/dd', width=29, selectbackground='#A0F8E7', background="#A0F8E7", foreground='black', selectforeground="black", bd=3, textvariable=Due_date_n, relief=SUNKEN)
cal1_n.grid(row=5, column=3, pady=3, padx=2, sticky=W)
cal1_n.delete(0, END)

ltransactionid_n=Label(Topframe1_neworder, font=('arial',10,'bold'), text="Transaction Id",width=20, bg="#deddd1")
ltransactionid_n.grid(row=5,column=4,pady=3, sticky=W)
etransactionid_n=Entry(Topframe1_neworder, width=30, font=('arial',12), bd=3, textvariable=Transaction_id_n, relief=SUNKEN)
etransactionid_n.grid(row=5,column=5,pady=3,padx=2,sticky=W)

lquantityordered_n=Label(Topframe1_neworder, font=('arial',10,'bold'), text="Quantity Ordered",width=20, bg="#deddd1")
lquantityordered_n.grid(row=6,column=0,pady=3, sticky=W)
equantityordered_n=Entry(Topframe1_neworder, width=25, font=('arial',12), bd=3, textvariable=Quantity_ordered_n, relief=SUNKEN)
equantityordered_n.grid(row=6,column=1,pady=3,padx=2,sticky=W)

lstatus_n=Label(Topframe1_neworder, font=('arial',10,'bold'), text="Status", width=20, bg="#deddd1")
lstatus_n.grid(row=6,column=2,pady=3, sticky=W)
estatus_n=Entry(Topframe1_neworder, width=25, font=('arial',12), bd=3, textvariable=status_n, relief=SUNKEN)
estatus_n.grid(row=6,column=3,pady=3,padx=2,sticky=W)

lsupp_id_n=Label(Topframe1_neworder, font=('arial',10,'bold'), text="Supplier id", width=20, bg="#deddd1")
lsupp_id_n.grid(row=6,column=4,pady=3, sticky=W)
esupp_id_n=Entry(Topframe1_neworder, width=30, font=('arial',12), bd=3, textvariable=SupplierIddd_n, relief=SUNKEN)
esupp_id_n.grid(row=6,column=5,pady=3,padx=2,sticky=W)

binsert_n=Button(Topframe2_neworder, font=('arial',10,'bold'), bg="#A0F8E7", text='INSERT',width=20, bd=2, relief=RAISED, command=insertdata_n)
binsert_n.grid(row=0, column=0, pady=5, padx=3)

bsearch_n=Button(Topframe2_neworder, font=('arial',10,'bold'), bg="#A0F8E7", text='SEARCH', width=21, bd=2, relief=RAISED, command=display_n)
bsearch_n.grid(row=0, column=1, pady=5, padx=3)

bupdate_n=Button(Topframe2_neworder, font=('arial',10,'bold'), bg="#A0F8E7", text='UPDATE', width=21, bd=2, relief=RAISED, command=update_n)
bupdate_n.grid(row=0, column=2, pady=5, padx=3)

bdelete_n=Button(Topframe2_neworder, font=('arial',10,'bold'), bg="#A0F8E7", text='DELETE', width=21, bd=2, relief=RAISED, command=delete_n)
bdelete_n.grid(row=0, column=3, pady=5, padx=3)

bselect_n=Button(Topframe2_neworder, font=('arial',10,'bold'), bg="#A0F8E7", text='SELECT', width=21, bd=2, relief=RAISED, command=select_n)
bselect_n.grid(row=0, column=4, pady=5, padx=3)

bback_n=Button(Topframe2_neworder, font=('arial',10,'bold'), bg="#A0F8E7", text='BACK', width=21, bd=2, relief=RAISED,  command=back_root_super2)
bback_n.grid(row=0, column=5, pady=5, padx=3)

breset_n=Button(Topframe2_neworder, font=('arial',10,'bold'), bg="#A0F8E7", text='RESET', width=20, bd=2, relief=RAISED, command=reset_n)
breset_n.grid(row=0, column=6, pady=5, padx=3)

Topframe3_neworder.columnconfigure(0, weight=1)

my_menu=Menu(super)
super.config(menu=my_menu)
file_menu=Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Order placed information", command=order_placed)
file_menu.add_command(label="Log out", command=logout_stock)

style=ttk.Style()
style.theme_use('default')
style.configure("Treeview",background="#deddd1", foreground="black", rowheight=25, fieldbackground="#D3D3D3", font=("Helvetica", 9))
style.map('Treeview',background=[('selected','#347083')])

style.configure("Treeview.Heading",  background="#D7FFF2", font=('Arial', 10, 'bold'))

tree_frame_n=Frame(Topframe3_neworder, width=w-800, bg="#deddd1")
tree_frame_n.pack(pady=10)

tree_scroll_y_n=Scrollbar(tree_frame_n, orient=VERTICAL)
tree_scroll_y_n.pack(side=RIGHT, fill=Y)
tree_scroll_x_n=Scrollbar(tree_frame_n, orient=HORIZONTAL)
tree_scroll_x_n.pack(side=BOTTOM, fill=X)

my_tree_n=ttk.Treeview(tree_frame_n, height=12, yscrollcommand=tree_scroll_y_n.set, xscrollcommand=tree_scroll_x_n.set, selectmode="extended")

my_tree_n['columns']=("Product Category", "Product ID", "Product Name", "Quantity available", "Price/item","Quantity ordered", "Delivery Date", "Discount","Tax", "Total Amount", "Amount Paid", "Payment method", "Transaction id","Balance", "Due Date",  "Supplier", "Supp Id", "Order id", "Supplier Contact No.", "Supplier email id", "Status")
tree_scroll_y_n.configure(command=my_tree_n.yview)
tree_scroll_x_n.configure(command=my_tree_n.xview)
my_tree_n.pack()

my_tree_n.column("#0", width=0, stretch=NO)
my_tree_n.column("Product Category", anchor=W, width=80)
my_tree_n.column("Product ID", anchor=W, width=60 )
my_tree_n.column("Product Name", anchor=W, width=84)
my_tree_n.column("Quantity available", anchor=W, width=39)
my_tree_n.column("Price/item", anchor=W, width=65)
my_tree_n.column("Quantity ordered", anchor=W, width=60)
my_tree_n.column("Delivery Date", anchor=W, width=65)
my_tree_n.column("Discount", anchor=W, width=46)
my_tree_n.column("Tax", anchor=W, width=40)
my_tree_n.column("Total Amount", anchor=W, width=80)
my_tree_n.column("Amount Paid", anchor=W, width=65)
my_tree_n.column("Payment method", anchor=W, width=60)
my_tree_n.column("Transaction id", anchor=W, width=90)
my_tree_n.column("Balance", anchor=W, width=46)
my_tree_n.column("Due Date", anchor=W, width=65)
my_tree_n.column("Supplier", anchor=W, width=50)
my_tree_n.column("Supp Id", anchor=W, width=30)
my_tree_n.column("Order id", anchor=W, width=44)
my_tree_n.column("Supplier Contact No.", anchor=W, width=80)
my_tree_n.column("Supplier email id", anchor=W, width=75)
my_tree_n.column("Status", anchor=W, width=25)

my_tree_n.heading("#0",text="", anchor=W)
my_tree_n.heading("Product Category",text="Category", anchor=W)
my_tree_n.heading("Product ID",text="ID",anchor=W)
my_tree_n.heading("Product Name",text="Name", anchor=W)
my_tree_n.heading("Quantity available", text="Qty avl",anchor=W)
my_tree_n.heading("Price/item", text="Price/item",anchor=W)
my_tree_n.heading("Quantity ordered", text="Qty ordered", anchor=W)
my_tree_n.heading("Delivery Date", text="Del Date", anchor=W)
my_tree_n.heading("Discount", text="Discount",anchor=W)
my_tree_n.heading("Tax", text="Tax", anchor=W)
my_tree_n.heading("Total Amount", text="Total Amt", anchor=W)
my_tree_n.heading("Amount Paid", text="Amt Paid", anchor=W)
my_tree_n.heading("Payment method", text="Pay method", anchor=W)
my_tree_n.heading("Transaction id", text="Transaction id", anchor=W)
my_tree_n.heading("Balance", text="Bal", anchor=W)
my_tree_n.heading("Due Date", text="Due Date", anchor=W)
my_tree_n.heading("Supplier", text="Supplier",anchor=W)
my_tree_n.heading("Supp Id", text="Supp Id",anchor=W)
my_tree_n.heading("Order id", text="Order id",anchor=W)
my_tree_n.heading("Supplier Contact No.", text="S Contact No.", anchor=W)
my_tree_n.heading("Supplier email id", text="S email id", anchor=W)
my_tree_n.heading("Status", text="Status", anchor=W)
my_tree_n['show']='headings'

my_tree_n.tag_configure('oddrow',background="#A0F8E7")
my_tree_n.tag_configure('evenrow',background="white")

my_cursor.execute(f"SELECT  p_category, Products.p_id, p_name, qavl, price, q_ordered, ddate, discount, tax, cost, amt_paid, pay_method, transaction_id, balance, duedate, s_name, Supplier.s_id, Orders.Order_id, s_contactno, s_emailid,status FROM Products, Orders, Supplier, Order_products, Supplier_products, SignUp_Data, User_access WHERE Products.p_id = Order_products.p_id AND Supplier_products.p_id = Products.p_id AND Orders.Order_id = Order_products.o_id AND Supplier.s_id=Orders.Supplier_id AND Supplier_products.s_id=Orders.Supplier_id AND Supplier_products.s_id=Supplier.s_id AND Supplier_products.p_id=Order_products.p_id AND Supplier_products.p_id=Order_products.p_id AND  SignUp_Data.email=User_access.email_id AND  User_access.pcategory=Products.p_category AND User_access.email_id='{email_id_access}' AND status<>'delivered';")
for row in my_cursor:
	count=len(my_tree_n.get_children())
	
	if count%2==0:
		my_tree_n.insert(parent='', index=count, iid=count, values=(row[0],row[1],row[2],row[3], row[4],row[5],row[6], row[7], row[8], row[9],row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20]), tags='evenrow')
	else:
		my_tree_n.insert(parent='', index=count, iid=count, values=(row[0],row[1],row[2],row[3], row[4],row[5],row[6], row[7], row[8], row[9],row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18],  row[19], row[20]), tags='oddrow')
				
	my_tree_n.pack()


my_menu1=Menu(super2)
super2.config(menu=my_menu1)
file_menu1=Menu(my_menu1, tearoff=False)
my_menu1.add_cascade(label="File", menu=file_menu1)
file_menu1.add_command(label="Stock information", command=stock_information)
file_menu1.add_command(label="Log out", command=logout_order)

root.mainloop()
