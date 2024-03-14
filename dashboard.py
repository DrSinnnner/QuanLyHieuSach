from tkinter import *
from PIL import Image, ImageTk #pip install pillow
from employee import employeeClass
class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("- - - HỆ THỐNG QUẢN LÝ HIỆU SÁCH - - - NHÓM 9 - - - K15DCPM06 - - -")
        self.create_title_label()
        self.create_clock_label()# Gọi hàm tạo label clock
        self.create_footer_label()# Gọi hàm tạo footer
        self.create_left_menu()# Gọi hàm tạo left menu
        self.create_content_label()  # Gọi hàm tạo nội dung
        self.root.config(bg="#FFFFEC")
    
    #====title====
    def create_title_label(self):
        self.icon_title = PhotoImage(file="images/book.png")
        title = Label(self.root, text="HỆ THỐNG QUẢN LÝ HIỆU SÁCH", image=self.icon_title, compound=LEFT , font=("Arial Rounded MT Bold", 30, "bold"), bg="#B19470", fg="#F8FAE5", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)

        #====btn_logout====
        btn_logout = Button(self.root, text="Thoát", font=("time new roman", 15, "bold"), bg="#BECA5C")
        btn_logout.place(x=1230, y=10, width=100)

    #====clock====
    def create_clock_label(self):
        self.lbl_clock = Label(self.root, text="Chào mừng đã đến với hệ thống\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS", font=("Arial Rounded MT Bold", 15), bg="#E1C78F", fg="#F8FAE5")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)  

    #====Left menu====
    def create_left_menu(self):
        self.MenuLogo = Image.open("images/menu.png")
        self.MenuLogo = self.MenuLogo.resize((200, 200), Image.LANCZOS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)

        self.leftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="#F3EEEA")
        self.leftMenu.place(x=0, y=102, width=200, height=533)
        
        lbl_menuLogo = Label(self.leftMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP, fill=X)

        lbl_menu = Label(self.leftMenu, text="Menu", font=("time new roman", 25, "bold"), bg="#76453B",fg="#F8FAE5")
        lbl_menu.pack(side=TOP, fill=X)
        
        self.icon_side=PhotoImage(file="images/side.png")
        btn_employee = Button(self.leftMenu, text="Nhân viên",command=self.employee,image=self.icon_side,compound=LEFT,padx=10,anchor="w", font=("time new roman", 20, "bold"), bg="#CC9B6D", bd=3, cursor="hand2")
        btn_employee.pack(side=TOP, fill=X)

        btn_supplier = Button(self.leftMenu, text="Vật tư",image=self.icon_side,compound=LEFT,padx=10,anchor="w", font=("time new roman", 20, "bold"), bg="#CC9B6D", bd=3, cursor="hand2")
        btn_supplier.pack(side=TOP, fill=X)

        btn_category = Button(self.leftMenu, text="Danh mục",image=self.icon_side,compound=LEFT,padx=10,anchor="w", font=("time new roman", 20, "bold"), bg="#CC9B6D", bd=3, cursor="hand2")
        btn_category.pack(side=TOP, fill=X)
        
        btn_product = Button(self.leftMenu, text="Sách",image=self.icon_side,compound=LEFT,padx=10,anchor="w", font=("time new roman", 20, "bold"), bg="#CC9B6D", bd=3, cursor="hand2")
        btn_product.pack(side=TOP, fill=X)
        
        btn_sales = Button(self.leftMenu, text="Lợi tức",image=self.icon_side,compound=LEFT,padx=10,anchor="w", font=("time new roman", 20, "bold"), bg="#CC9B6D", bd=3, cursor="hand2")
        btn_sales.pack(side=TOP, fill=X)

    #========content=========
    def create_content_label(self):
        self.lbl_employee = Label(self.root, text="Tổng số nhân viên\n[ 0 ]",bd=5,relief=RIDGE, bg="#5F6F52", fg="#FFF4F4", font=("Arial Rounded MT Bold", 20, "bold"))
        self.lbl_employee.place(x=300, y=120, height=150, width=300)

        self.lbl_supplier = Label(self.root, text="Tổng số vật tư\n[ 0 ]",bd=5,relief=RIDGE, bg="#898121", fg="#FFF4F4", font=("Arial Rounded MT Bold", 20, "bold"))
        self.lbl_supplier.place(x=650, y=120, height=150, width=300)

        self.lbl_category = Label(self.root, text="Tổng số danh mục\n[ 0 ]",bd=5,relief=RIDGE, bg="#ABC270", fg="#FFF4F4", font=("Arial Rounded MT Bold", 20, "bold"))
        self.lbl_category.place(x=1000, y=120, height=150, width=300)

        self.lbl_product = Label(self.root, text="Tổng số sách\n[ 0 ]",bd=5,relief=RIDGE, bg="#94B49F", fg="#FFF4F4", font=("Arial Rounded MT Bold", 20, "bold"))
        self.lbl_product.place(x=300, y=300, height=150, width=300)

        self.lbl_sales = Label(self.root, text="Tổng doanh thu\n[ 0 ]",bd=5,relief=RIDGE, bg="#95CD41", fg="#FFF4F4", font=("Arial Rounded MT Bold", 20, "bold"))
        self.lbl_sales.place(x=650, y=300, height=150, width=300)

    #====footer====
    def create_footer_label(self):
        self.lbl_footer = Label(self.root, text="Hệ thống quản lý hiệu sách  |  phát triển bởi nhóm 9 -lớp K15DCPM06\nNguyễn Anh Dũng  -  Nguyễn Trọng Nghĩa  -  Nguyễn Hoàng Giang", font=("Arial Rounded MT Bold", 12, "bold"), bg="#76453B", fg="#F8FAE5").pack(side=BOTTOM,fill=X) 

#===============================================================================================================================================================================================

    def employee(self):
        self.new_win=Toplevel(self.root)
        self.obj=employeeClass(self.new_win)

if __name__=="__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
