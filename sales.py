from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox, StringVar
import sqlite3
import os
from tkmacosx import Button


class salesClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+260+210")
        self.root.title("GrabMart Inventory")
        self.root.config(bg="white")
        self.root.focus_force()

        self.bill_list=[]
#---------Variables-----
        self.var_invoice=StringVar()

#------------title-------------
        lbl_title = Label(self.root, text="View Customer Bills", font=("goudy old style", 30), bg="#184a45", fg="white", bd=3, relief=RIDGE).pack(side=TOP, fill=X, padx=10, pady=20)

        lbl_invoice=Label(self.root, text="Invoice No.", font=("times new roman", 15), bg="white").place(x=50, y=100)
        txt_invoice = Entry(self.root, textvariable=self.var_invoice, font=("times new roman", 15), bg="lightyellow").place(x=160, y=100, width=180, height=28)

        btn_search= Button(self.root, bd=0, text="Search",command=self.search ,font=("times new roman",15, "bold" ),bg="#2196f3",fg="#0f4d7d").place(x=360, y=100, width=120, height=28)
        btn_clear = Button(self.root, bd=0, text="Clear", command=self.clear,font=("times new roman", 15, "bold"),bg="#eee",fg="black").place(x=490, y=100, width=120, height=28)

#----------Bill List---------------------
        sales_Frame= Frame(self.root, bd=3, relief=RIDGE)
        sales_Frame.place(x=50, y=140, width=200, height=330 )

        lbl_title1 = Label(sales_Frame, text="List of Bills", font=("goudy old style", 20), bg="#1e81b0", ).pack(side=TOP, fill=X)

        scrolly= Scrollbar(sales_Frame, orient=VERTICAL)
        self.Sales_List=Listbox(sales_Frame, font=("goudy old style", 15), bg="#eeeee4", yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.Sales_List.yview)
        self.Sales_List.pack(fill=BOTH, expand=1)
        self.Sales_List.bind("<ButtonRelease-1>", self.get_data)


#---------Bill Area-------------------------
        bill_Frame = Frame(self.root, bd=3, relief=RIDGE)
        bill_Frame.place(x=280, y=140, width=410, height=330)

        lbl_title2 = Label(bill_Frame, text="Customer Bill Area", font=("goudy old style", 20), bg="#1e81b0",).pack(side=TOP, fill=X)

        scrolly2 = Scrollbar(bill_Frame, orient=VERTICAL)
        self.bill_area = Text(bill_Frame, bg="#eeeee4", yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT, fill=Y)
        scrolly2.config(command=self.Sales_List.yview)
        self.bill_area.pack(fill=BOTH, expand=1)

#----------Images----------
        self.bill_photo=Image.open("images/cat2.jpg")
        self.bill_photo=self.bill_photo.resize((450,300),Image.ANTIALIAS)
        self.bill_photo=ImageTk.PhotoImage(self.bill_photo)

        lbl_image=Label(self.root, image=self.bill_photo, bd=0)
        lbl_image.place(x=700, y=110)

        self.show()

#---------------------------------------
    def show(self):
        del self.bill_list[:]
        self.Sales_List.delete(0, END)
        #print(os.listdir('Bill'))
        for i in os.listdir('Bill'):
            if i.split('.')[-1]=='txt':
                self.Sales_List.insert(END, i)
                self.bill_list.append(i.split('.')[0])


    def get_data(self, ev):
        index_=self.Sales_List.curselection()
        file_name=self.Sales_List.get(index_)
        #print(file_name)
        self.bill_area.delete('1.0',END)
        fp=open(f'Bill/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END, i)
        fp.close()

    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("ERROR", "Invoice Num required!", parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                fp = open(f'Bill/{self.var_invoice.get()}.txt', 'r')
                self.bill_area.delete('1.0',END)
                for i in fp:
                    self.bill_area.insert(END, i)
                fp.close()
            else:
                messagebox.showerror("ERROR", "Invoice Not Found!", parent=self.root)

    def clear(self):
        self.show()
        self.bill_area.delete('1.0', END)


if __name__ == "__main__":
    root = Tk()
    obj = salesClass(root)
    root.mainloop()