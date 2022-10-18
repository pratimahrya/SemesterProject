from tkinter import*
from PIL import Image, ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
from billing import BillClass
import sqlite3
from tkinter import messagebox
import os
import time
from tkmacosx import Button


class IMS:

    def __init__(self, root: object) -> object:
        self.root = root
        # getting screen width and height of display
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()

        # self.root.attributes("-fullscreen", True)
        # setting tkinter window size
        self.root.geometry("%dx%d+0+0" % (width, height))

        #self.root.geometry("1350x700+0+0")
        self.root.title("GrabMart Inventory")
        self.root.config(bg="white")


        #==title==
        self.icon_title = PhotoImage(file="images/logo1.png")
        title=Label(self.root, text="GrabMart Inventory", image=self.icon_title, compound=LEFT,font=("times new roman", 40, "bold"), bg="#76b5c5", fg="white", anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=70)

        #==logout button==
        btn_logout=Button(self.root, text="Logout",command=self.logout ,font=("times new roman", 15, "bold"), bg="#eee", cursor="hand2").place(x=1285, y=10, height=50, width=150)

        #==clock==
        self.lbl_clock = Label(self.root, text="Welcome to GrabMart\t\t Date:DD-MM-YYYY\t\t Time:HH:MM:SS", font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        #==left menu==
        self.MenuLogo=Image.open("images/menu_im.png")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu=Frame(self.root,bd=2, relief=GROOVE, )
        LeftMenu.place(x=0, y=200, width=200, height=500)

        lbl_menuLogo=Label(LeftMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP, fill=X)

        lbl_menu=Label(LeftMenu, text="Menu", font=("times new roman", 20), bg="#eab676",).pack(side=TOP, fill=X)

        btn_employee = Button(LeftMenu, text="Employee", command=self.employee, font=("times new roman", 20,"bold" ), bg="white",bd=3, cursor="hand2" ).pack(side=TOP, fill=X)
        btn_supplier = Button(LeftMenu, text="Supplier",command=self.supplier, font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_category = Button(LeftMenu, text="Category",command=self.category,font=("times new roman", 20, "bold"), bg="white", bd=3,cursor="hand2").pack(side=TOP, fill=X)
        btn_product = Button(LeftMenu, text="Products",command=self.product,font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_sales = Button(LeftMenu, text="Sales",command=self.sales, font=("times new roman", 20, "bold"), bg="white", bd=3,cursor="hand2").pack(side=TOP, fill=X)
        btn_billing = Button(LeftMenu, text="Billing", command=self.billing, font=("times new roman", 20, "bold"), bg="white",bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_exit = Button(LeftMenu, text="Exit", font=("times new roman", 20,"bold" ), bg="white",bd=3, cursor="hand2" ).pack(side=TOP, fill=X)

        #===content===

        self.lbl_employee=Label(self.root, text="Total Employee\n[0]",bd=5,relief=RIDGE, bg="#e0c075",fg="white", font=("goudy old style",20,"bold" ))
        self.lbl_employee.place(x=300,y=250,height=150, width=300)

        self.lbl_supplier = Label(self.root, text="Total Supplier\n[0]", bd=5, relief=RIDGE, bg="#e0c075", fg="white",
                                  font=("goudy old style", 20, "bold"))
        self.lbl_supplier.place(x=650, y=250, height=150, width=300)

        self.lbl_category = Label(self.root, text="Total Category\n[0]", bd=5, relief=RIDGE, bg="#e0c075", fg="white",
                                  font=("goudy old style", 20, "bold"))
        self.lbl_category.place(x=1000, y=250, height=150, width=300)

        self.lbl_product = Label(self.root, text="Total Product\n[0]", bd=5, relief=RIDGE, bg="#e0c075", fg="white",
                                  font=("goudy old style", 20, "bold"))
        self.lbl_product.place(x=400, y=450, height=150, width=300)

        self.lbl_sales = Label(self.root, text="Total Sales\n[0]", bd=5, relief=RIDGE, bg="#e0c075", fg="white",
                                  font=("goudy old style", 20, "bold"))
        self.lbl_sales.place(x=750, y=450, height=150, width=300)






        # ==footer==
        lbl_footer = Label(self.root, text="GrabMart",font=("times new roman", 12), bg="#4d636d", fg="white").pack(side=BOTTOM, fill=X)
        self.update_content()
#=======================================================================================
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)

    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = categoryClass(self.new_win)

    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = productClass(self.new_win)

    def billing(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = BillClass(self.new_win)

    def sales(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = salesClass(self.new_win)

    def update_content(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_product.config(text=f'Total Products\n[{str(len(product))}]')

            cur.execute("select * from supplier")
            supplier = cur.fetchall()
            self.lbl_supplier.config(text=f'Total Suppliers\n[{str(len(supplier))}]')

            cur.execute("select * from category")
            category = cur.fetchall()
            self.lbl_category.config(text=f'Total Category\n[{str(len(category))}]')

            cur.execute("select * from employee")
            employee = cur.fetchall()
            self.lbl_employee.config(text=f'Total Employees\n[{str(len(employee))}]')
            bill=len(os.listdir('bill'))
            self.lbl_sales.config(text=f'Total Sales\n[{str(bill)}]')

            time_ = time.strftime("%I:%M:%S")
            date_ = time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome to GrabMart Inventory\t\t Date:{str(date_)}\t\t Time:{str(time_)}")
            self.lbl_clock.after(200, self.update_content)

        except Exception as ex:
            messagebox.showerror("ERROR", f"Error due to : {str(ex)}", parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system("python3 login.py")

if __name__=="__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
