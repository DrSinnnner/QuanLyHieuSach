from tkinter import *
from PIL import Image, ImageTk #pip install pillow
from tkinter import ttk, messagebox
import sqlite3

class employeeClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("792x435+206+130")
        self.root.title("- 📔 - HỆ THỐNG QUẢN LÝ HIỆU SÁCH - 📚 - NHÓM 9 - 📖 - K15DCPM06 - 📝 -")
        self.root.config(bg="#FFFFEC")
        self.root.focus_force()
        #===========================================================
        #----Tất cả biến--------
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_empid = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_utype = StringVar()
        self.var_address = StringVar()
        self.var_salary = StringVar()
        
        #===--image---===
        self.emp_img = Image.open("images/emp.png")
        self.emp_img = self.emp_img.resize((100, 100), Image.LANCZOS)
        self.emp_img = ImageTk.PhotoImage(self.emp_img)

        lbl_image = Label(self.root, image=self.emp_img)
        lbl_image.place(x=600, y=5)
        #=======------------Tìm kiếm----------- ==========
        SearchFrame = LabelFrame(self.root, text="Tìm Nhân Viên", bg='white', font=("time new roman",15,"bold"), bd=2, relief=RIDGE)
        SearchFrame.place(x=5, y=10, width=517, height=60)

        cmb_search=ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Chọn", "Tên", "Mã số"), state='readonly', justify=CENTER, font=("time new roman", 10))
        cmb_search.place(x=8, y=5, width=70)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("time new roman", 15), bg="#FFFFEC")
        txt_search.place(x=90, y=0, width=360)
        
        btn_search = Button(SearchFrame, text="Tìm", command=self.search, font=("time new roman", 10, "bold"), bg="#BFEA7C", cursor="hand2")
        btn_search.place(x=460, y=0, width=40)

        #===================content====================
        #================== hàng 1 ==========
        lbl_empid = Label(self.root, text="Mã số", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=5, y=80)
        lbl_gender = Label(self.root, text="Giới tính", font=("time new roman", 15), bg="#F1E4C3",fg="#000000").place(x=285, y=80)

        txt_empid = Entry(self.root, textvariable=self.var_empid, font=("time new roman", 15), bg="#F3EEEA", fg="#000000").place(x=70, y=80, width=200)
        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Select","Nam", "Nữ"), state='readonly', justify=CENTER, font=("time new roman", 15))
        cmb_gender.place(x=373, y=80, width=149)
        cmb_gender.current(0)

        #==================== hàng 2 ===========
        lbl_name = Label(self.root, text="Họ tên", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place( x=5, y=120)
        lbl_dob = Label(self.root, text="Ngày sinh", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=285, y=120)
        lbl_contact = Label(self.root, text="Liên hệ", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=535, y=120)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("time new roman", 15), bg="#F3EEEA", fg="#000000")
        txt_name.place(x=74, y=120, width=197)
        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("time new roman", 15), bg="#F3EEEA",fg="#000000")
        txt_dob.place(x=383, y=120, width=140)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("time new roman", 15), bg="#F3EEEA",fg="#000000")
        txt_contact.place(x=612, y=120, width=171)
        
        #==================== hàng 3 ===============
        lbl_utype = Label(self.root, text="phân quyền", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=535, y=160)
        lbl_email = Label(self.root, text="Email", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place( x=5, y=160)
        lbl_salary = Label(self.root, text="lương", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=285, y=160)

        txt_email = Entry(self.root, textvariable=self.var_email, font=("time new roman", 15), bg="#F3EEEA", fg="#000000")
        txt_email.place(x=63, y=160, width=208)

       
        txt_salary = Entry(self.root, textvariable=self.var_salary, font=("time new roman", 15), bg="#F3EEEA", fg="#000000")
        txt_salary.place(x=350, y=160, width=174)

        cmb_utype = ttk.Combobox(self.root, textvariable=self.var_utype, values=("Select", "Quản Lý", "Nhân viên"), state='readonly', justify=CENTER, font=("time new roman", 15))
        cmb_utype.place(x=648, y=160, width=135)
        cmb_utype.current(0)

        #============hàng 4=======================
        lbl_address = Label(self.root, text="Địa chỉ", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=5, y=200)

        self.txt_address = Text(self.root, font=("time new roman", 15), bg="#F3EEEA", fg="#000000")
        self.txt_address.place(x=77, y=200, width=705, height=30)

        #======= nút chức năng thêm xóa sửa ==========
        btn_add = Button(self.root, text="Lưu", command=self.add, font=("time new roman", 17), bg="#1A5D1A", fg="#FAF0D7").place(x=70, y=240, width=80, height=30)
        btn_upadte = Button(self.root, text="Sửa", command=self.update, font=("time new roman", 17), bg="#0C359E", fg="#FAF0D7").place(x=260, y=240, width=80, height=30)
        btn_delete = Button(self.root, text="xóa", command=self.delete, font=("time new roman", 17), bg="#B70404", fg="#FAF0D7").place(x=450, y=240, width=80, height=30)
        btn_clear = Button(self.root, text="làm mới", command=self.clear, font=("time new roman", 15), bg="#FFA447",fg="#FAF0D7").place(x=641, y=240, width=80, height=30)
       
        #====================title================
        title = Label(self.root, text="thông tin chi tiết của nhân viên", font=("time new roman", 15, "bold"), bg="#52D3D8", fg="#000000").place(x=10, y=280, width=770)
       
        #======= thông tin nhân viên ===========
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=315, relwidth=1, height=120)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.EmployeeTable = ttk.Treeview(emp_frame,columns=("empid", "name", "email", "gender", "contact", "dob","utype", "address", "salary"), yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.EmployeeTable.yview)

        self.EmployeeTable.heading("empid", text=u"Mã số")
        self.EmployeeTable.heading("name", text=u"Họ tên")
        self.EmployeeTable.heading("email", text=u"Email")
        self.EmployeeTable.heading("gender", text=u"Giới tính")
        self.EmployeeTable.heading("contact", text=u"Liên hệ")
        self.EmployeeTable.heading("dob", text=u"Ngày sinh")
        self.EmployeeTable.heading("utype", text=u"Quyền")
        self.EmployeeTable.heading("address", text=u"Địa chỉ")
        self.EmployeeTable.heading("salary", text=u"Lương")

        self.EmployeeTable["show"] = "headings"

        self.EmployeeTable.column("empid", width=5)
        self.EmployeeTable.column("name", width=90)
        self.EmployeeTable.column("email", width=70)
        self.EmployeeTable.column("gender", width=17)
        self.EmployeeTable.column("contact", width=40)
        self.EmployeeTable.column("dob", width=40)
        self.EmployeeTable.column("utype", width=30)
        self.EmployeeTable.column("address", width=50)
        self.EmployeeTable.column("salary", width=30)
        self.EmployeeTable.pack(fill=BOTH, expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
   
#=================================================================================================================
    
    #____add_____ 
    def add(self):
        con = sqlite3.connect(database="ims.db")
        cur = con.cursor()
        try:
            if self.var_empid.get() == "":
                messagebox.showerror("Lỗi", "Hãy nhập mã số nhân viên!", parent=self.root)
            else:
                cur.execute("Select * from employee where empid=?", (self.var_empid.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Lỗi", "Đã có mã số này rồi", parent=self.root)
                else:
                    cur.execute("Insert into employee(empid,name,email,gender,contact,dob,utype,address,salary) values (?,?,?,?,?,?,?,?,?)",(
                                        self.var_empid.get(),
                                        self.var_name.get(),
                                        self.var_email.get(),
                                        self.var_gender.get(),
                                        self.var_contact.get(),
                                        self.var_dob.get(),
                                        self.var_utype.get(),
                                        self.txt_address.get('1.0',END), 
                                        self.var_salary.get()
                        ))
                    con.commit()
                    messagebox.showinfo("Thêm", "Đã thêm nhân viên", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Lỗi", f"Lỗi đến từ : {str(ex)}",parent=self.root)


    #____show____
    def show(self):
        con=sqlite3.connect(database="ims.db")
        cur=con.cursor()
        try:
            cur.execute("Select * from employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Lỗi",f"Lỗi đến từ: {str(ex)}",parent=self.root)

   
    #____get-data____
    def get_data(self,ev):
        f = self.EmployeeTable.focus()
        content = self.EmployeeTable.item(f)
        row = content['values']
        if row:
            for value in row:
                print(str(value).encode('unicode_escape').decode('utf-8'))
            self.var_empid.set(row[0])
            self.var_name.set(row[1])
            self.var_email.set(row[2])
            self.var_gender.set(row[3])
            self.var_contact.set(row[4])
            self.var_dob.set(row[5])
            self.var_utype.set(row[6])
            self.txt_address.delete('1.0', END)
            self.txt_address.insert(END, row[7])
            self.var_salary.set(row[8])


    #____update____ 
    def update(self):
        con = sqlite3.connect(database="ims.db")
        cur = con.cursor()
        try:
            if self.var_empid.get() == "":
                messagebox.showerror("Lỗi", "Hãy nhập mã số nhân viên!", parent=self.root)
            else:
                cur.execute("Select * from employee where empid=?", (self.var_empid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Lỗi","Mã số không hợp lệ", parent=self.root)
                else:
                    cur.execute("Update employee set name=?,email=?,gender=?,contact=?,dob=?,utype=?,address=?,salary=? where empid=?",(
                                        
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_contact.get(),
                            self.var_dob.get(),
                            self.var_utype.get(),
                            self.txt_address.get('1.0',END), 
                            self.var_salary.get(),
                            self.var_empid.get()
                        ))
                    con.commit()
                    messagebox.showinfo("Sửa", "Đã cập nhật thành công", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Lỗi", f"Lỗi đến từ : {str(ex)}")


    #____Xóa____
    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_empid.get() == "":
                messagebox.showerror("Lỗi", "Hãy chọn nhân viên muốn xóa!", parent=self.root)
            else:
                cur.execute("Select * from employee where empid=?", (self.var_empid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Lỗi", "Đã có mã số này rồi", parent=self.root)
                else:
                    op=messagebox.askyesno("Xác nhận","Bạn muốn xóa thông tin?",parent=self.root)
                    if op==True:
                        cur.execute("delete from employee where empid=?",(self.var_empid.get(),))
                        con.commit()
                        messagebox.showinfo("Xóa","Đã xóa thành công",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Lỗi", f"Lỗi đến từ : {str(ex)}")


    #_____Làm mới____
    def clear(self):
        self.var_empid.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_utype.set("Select")
        self.txt_address.delete('1.0',END) 
        self.var_salary.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()
        

         #____Tìm Kiếm_____
    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get() == "Chọn":
                messagebox.showerror("Lỗi", "Hãy chọn trường tìm kiếm", parent=self.root)
            elif self.var_searchtxt.get() == "":
                messagebox.showerror("Lỗi", "Hãy nhập thông tin cần tìm", parent=self.root)
            else:
                if self.var_searchby.get() == "Tên":
                    cur.execute("SELECT * FROM employee WHERE name LIKE '%" + self.var_searchtxt.get() + "%'")
                elif self.var_searchby.get() == "Mã số":
                    cur.execute("SELECT * FROM employee WHERE empid LIKE '%" + self.var_searchtxt.get() + "%'")

                rows = cur.fetchall()
                if len(rows) != 0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Lỗi", "Không tồn tại", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Lỗi", f"Lỗi đến từ: {str(ex)}", parent=self.root)
   
if __name__ == "__main__":
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()
 