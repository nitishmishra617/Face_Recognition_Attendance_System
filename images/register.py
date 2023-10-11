from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


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
            frame, textvariable=self.var_pass, font=("times new roman", 15))
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

        b2 = Button(frame, image=self.photoimg3, borderwidth=0, cursor="hand2", font=(
            "times new roman", 15, "bold"), fg="white", bg="white")
        b2.place(x=330, y=400, width=200, height=100)

# ==========function declaration==========

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "select":
            messagebox.showerror("Error", "All fields are required")
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
            messagebox.showinfo("Success", "Register Successfully")


if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
