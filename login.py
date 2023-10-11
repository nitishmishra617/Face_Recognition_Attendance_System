from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_system
import os
from datetime import datetime
from time import strftime


def main():
    win = Tk()
    app = login_window(win)
    win.mainloop()


class login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1360x700+0+0")

        self.bg = ImageTk.PhotoImage(file=r"images/tech2.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        title_lbl = Label(self.root, text="TOCS FACE RECOGNITION ATTENDANCE SYSTEM", font=(
            "times new roman", 28, "bold"), bg="black", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font=("times new roman", 15, "bold"),
                    background="black", foreground="blue")
        lbl.place(x=0, y=0, width=110, height=50)
        time()

        # second Image
        img8 = Image.open(
            r"clg_img\img\3556_logo.jpg")
        img8 = img8.resize((320, 120), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        f_lbl = Label(self.root, image=self.photoimg8)
        f_lbl.place(x=630, y=50, width=300, height=110)

        img1 = Image.open(r"images/download.png")
        img1 = img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=(
            "times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        username = lblu = Label(frame, text="username", font=(
            "times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=70, y=155)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password = lblp = Label(frame, text="password", font=(
            "times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame, font=(
            "times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=250, width=270)

        ############Icon Image#######
        img2 = Image.open(r"images/user1.jpg")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg2.place(x=650, y=323, width=25, height=25)

        img3 = Image.open(r"images/User-Password-Icon.jpg")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg3.place(x=650, y=390, width=25, height=25)

        # loginbutton
        loginbtn = Button(frame, text="Login", font=(
            "times new roman", 15, "bold"), command=self.login, relief=RIDGE, fg="white", bg="red")
        loginbtn.place(x=110, y=300, width=120, height=35)

        registerbtn = Button(frame, text="Register New User", font=(
            "times new roman", 12, "bold"), command=self.register_window, borderwidth=0,  relief=RIDGE, fg="white", bg="black")
        registerbtn.place(x=20, y=360, width=190)

        forgtbtn = Button(frame, text="Forgot password?", font=(
            "times new roman", 12, "bold"), command=self.forgot_password_window, borderwidth=0,  relief=RIDGE, fg="white", bg="black")
        forgtbtn.place(x=25, y=390, width=160)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "all field required")
        # elif self.txtuser.get() == "nitish" and self.txtpass.get() == "mishra":
           # messagebox.showinfo("success", "Login Successful!")
        else:
            conn = mysql.connector.connect(
                host="localhost", user="root", password="", database="login_system")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s", (self.txtuser.get(), self.txtpass.get()
                                                                                        ))
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid username & password")
            else:
                open_main = messagebox.askyesno("Confirm", "Admin access only")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = Face_Recognition_system(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    # ========reset password================

    def reset_pass(self):
        if self.combo_security_q.get() == "select":
            messagebox.showerror(
                "Error", "select security question", parent=self.root2)
        elif self.txt_security_A.get() == "":
            messagebox.showerror(
                "Error", "Please enter the answer", parent=self.root2)
        elif self.txt_new_pswd.get() == "":
            messagebox.showerror(
                "Error", "please enter the new password", parent=self.root2)
        else:
            conn = mysql.connector.connect(
                host="localhost", user="root", password="", database="login_system")
            my_cursor = conn.cursor()
            query = (
                "select * from register where email=%s and securityQ=%s and securityA=%s")
            value = (self.txtuser.get(), self.combo_security_q.get(),
                     self.txt_security_A.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror(
                    "Error", "please enter correct answer", parent=self.root2)
            else:
                query = ("update register set password=%s where email=%s")
                value = (self.txt_new_pswd.get(), self.txtuser.get())
                my_cursor.execute(query, value)
                conn.commit()
                conn.close()
                messagebox.showinfo(
                    "Info", "your password has been reset, Please login with the new password", parent=self.root2)
                self.root2.destroy()

    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror(
                "Error", "Please enter the Email address to start password")
        else:
            conn = mysql.connector.connect(
                host="localhost", user="root", password="", database="login_system")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror(
                    "My Error", "Please enter the valid user name")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("forget password")
                self.root2.geometry("340x450+610+170")

                l = Label(self.root2, text="Forget Password", font=(
                    "times new roman", 20, "bold"), fg="red", bg="white")
                l.place(x=0, y=10, relwidth=1)

                security_Q = Label(self.root2, text="select security question", font=(
                    "times new roman", 15, "bold"), fg="black", bg="white")
                security_Q.place(x=50, y=80)

                self.combo_security_q = ttk.Combobox(self.root2, font=(
                    "times new roman", 15, "bold"), state="readonly")
                self.combo_security_q["values"] = (
                    "select", "your birth place", "your School name", "your pet name")
                self.combo_security_q.place(x=50, y=110, width=250)
                self.combo_security_q.current(0)

                security_A = Label(self.root2, text="Security Answer", font=(
                    "times new roman", 15, "bold"), bg="white", fg="black")
                security_A.place(x=50, y=150)

                self.txt_security_A = ttk.Entry(self.root2,  font=(
                    "times new roman", 15))
                self.txt_security_A.place(x=50, y=180, width=250)

                self.new_pswd = Label(self.root2, text="New password", font=(
                    "times new roman", 15, "bold"), bg="white", fg="black")
                self.new_pswd.place(x=50, y=220)
                self.txt_new_pswd = ttk.Entry(
                    self.root2, font=("times new roman", 15, "bold"))
                self.txt_new_pswd.place(x=50, y=250, width=250)

                btn = Button(self.root2, text="Reset",  font=(
                    "times new roman", 15, "bold"), command=self.reset_pass, fg="white", bg="green")
                btn.place(x=100, y=290)


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1360x700+0+0")

        # ======variables========

        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # =============bg image============

        self.bg = ImageTk.PhotoImage(file=r"images/345611.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # ==============left image===========
        self.bg1 = ImageTk.PhotoImage(file=r"images/quote3.jpg")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)

# ==================main Frame===============
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=700, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=(
            "times new roman", 20, "bold"), fg="darkgreen", bg="white")
        register_lbl.place(x=20, y=20)

        # ===========labels and entry===========
        fname = Label(frame, text="First Name", font=(
            "times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)
        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=(
            "times new roman", 15, "bold"))
        fname_entry.place(x=50, y=130, width=250)

        l_name = Label(frame, text="Last Name", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        l_name.place(x=370, y=100)

        self.txt_lname = ttk.Entry(
            frame, textvariable=self.var_lname, font=("times new roman", 15))
        self.txt_lname.place(x=370, y=130, width=250)

        # =======row2===============

        contact = Label(frame, text="Contact No", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=160)

        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=(
            "times new roman", 15))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=(
            "times new roman", 15))
        self.txt_email.place(x=370, y=200, width=250)

        security_q = Label(frame, text="Select Security Question", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        security_q.place(x=50, y=240)

        self.combo_security_q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=(
            "times new roman", 15, "bold"), state="readonly")
        self.combo_security_q["values"] = (
            "select", "your birth place", "your School name", "your pet name")
        self.combo_security_q.place(x=50, y=270, width=250)
        self.combo_security_q.current(0)

        security_A = Label(frame, text="Security Answer", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        security_A.place(x=370, y=240)

        self.txt_security_A = ttk.Entry(frame, textvariable=self.var_securityA, font=(
            "times new roman", 15))
        self.txt_security_A.place(x=370, y=270, width=250)

        pswd = Label(frame, text="password", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50, y=310)
        self.txt_pswd = ttk.Entry(
            frame, textvariable=self.var_pass, font=("times new roman", 15), show="*")
        self.txt_pswd.place(x=50, y=340, width=250)

        pswd_cnfrm = Label(frame, text="Confirm Password", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        pswd_cnfrm.place(x=370, y=310)
        self.txt_pswd_cnfrm = ttk.Entry(
            frame, textvariable=self.var_confpass, font=("times new roman", 15))
        self.txt_pswd_cnfrm.place(x=370, y=340, width=250)

        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, variable=self.var_check, text="I agree to the Terms & Conditions", font=(
            "times new roman", 12, "bold"), bg="white", onvalue=1)
        checkbtn.place(x=50, y=380)

        img = Image.open(
            r"images/register2.png")
        img = img.resize((170, 45), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        b1 = Button(frame, image=self.photoimg, borderwidth=0, cursor="hand2", command=self.register_data, font=(
            "times new roman", 15, "bold"), fg="white", bg="white")
        b1.place(x=10, y=420, width=200)

        img3 = Image.open(
            r"images/login3.png")
        img3 = img3.resize((150, 45), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b2 = Button(frame, image=self.photoimg3, command=self.return_login, borderwidth=0, cursor="hand2", font=(
            "times new roman", 15, "bold"), fg="white", bg="white")
        b2.place(x=330, y=400, width=200, height=100)

# ==========function declaration==========

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "select":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror(
                "Error", "password & confirm password must be same")
        elif self.var_check.get() == 0:
            messagebox.showerror(
                "Error", "Please agree our terms and condition")
        else:
            conn = mysql.connector.connect(
                host="localhost", user="root", password="", database="login_system")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror(
                    "Error", "User already exist, please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                ))

            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registered Successfully")

    def return_login(self):
        self.root.destroy()


if __name__ == "__main__":
    main()
