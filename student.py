from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import data

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Information System")

        # variable
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        # First Image
        img = Image.open(
            r"C:\Users\Amresh Mishra\Desktop\face_recognition system\clg_img\img\stface1.jpg")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # second Image
        img1 = Image.open(
            r"C:\Users\Amresh Mishra\Desktop\face_recognition system\clg_img\img\stface2.jpg")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # third image
        img2 = Image.open(
            r"C:\Users\Amresh Mishra\Desktop\face_recognition system\clg_img\img\stface3.png")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=550, height=130)

        # Background Image
        img3 = Image.open(
            r"C:\Users\Amresh Mishra\Desktop\face_recognition system\clg_img\img\bgimg.jpeg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=(
            "times new roman", 24, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1550, height=25)

        # main frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=30, width=1320, height=800)

        # left frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=660, height=580)

        img_left = Image.open(
            r"C:\Users\Amresh Mishra\Desktop\face_recognition system\clg_img\img\smart-attendance.jpg")
        img_left = img_left.resize((630, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=0, y=0, width=650, height=120)

        # current course
        current_course_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                          text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=15, y=135, width=650, height=110)

        dep_label = Label(current_course_frame, text="Department", font=(
            "times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=(
            "times new roman", 12, "bold"), state="readonly")
        dep_combo["values"] = ("Select Department",
                               "Computer", "IT", "civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # current course information
        course_label = Label(current_course_frame, text="Course", font=(
            "times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=(
            "times new roman", 12, "bold"), state="readonly")
        course_combo["values"] = ("Select Course",
                                  "BCA", "BSc", "BCom", "BA")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Year", font=(
            "times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=(
            "times new roman", 12, "bold"), state="readonly")
        year_combo["values"] = ("Select Year",
                                "2018", "2019", "2020", "2021")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # semester
        sem_label = Label(current_course_frame, text="Semester", font=(
            "times new roman", 12, "bold"), bg="white")
        sem_label.grid(row=1, column=2, padx=10)

        sem_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=(
            "times new roman", 12, "bold"), state="readonly")
        sem_combo["values"] = ("Select Semester",
                               "1", "2", "3", "4", "5", "6")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # class student Information
        class_student_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                         text="Class Student Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=15, y=250, width=650, height=300)

        # student ID
        studentID_label = Label(class_student_frame, text="Student ID", font=(
            "times new roman", 12, "bold"), bg="white")
        studentID_label.grid(row=0, column=0, padx=7, pady=5)

        studentID_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id, width=20, font=(
            "times new roman", 12, "bold"))
        studentID_entry.grid(row=0, column=1, padx=7, pady=5, sticky=W)

        # student Name
        studentName_label = Label(class_student_frame, text="Student Name", font=(
            "times new roman", 12, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=7, pady=5)

        studentName_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_name, width=20, font=(
            "times new roman", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class Division
        classDiv_label = Label(class_student_frame, text="Division", font=(
            "times new roman", 12, "bold"), bg="white")
        classDiv_label.grid(row=1, column=0, padx=7, pady=5)

        div_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div, font=(
            "times new roman", 12, "bold"), state="readonly")
        div_combo["values"] = ("Select", "A",
                               "B", "C", "D")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Class Rollno
        classRollno_label = Label(class_student_frame, text="Roll No", font=(
            "times new roman", 12, "bold"), bg="white")
        classRollno_label.grid(row=1, column=2, padx=7, pady=5)

        classRollno_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, width=20, font=(
            "times new roman", 12, "bold"))
        classRollno_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Class Gender
        classGender_label = Label(class_student_frame, text="Gender", font=(
            "times new roman", 12, "bold"), bg="white")
        classGender_label.grid(row=2, column=0, padx=7, pady=5)

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=(
            "times new roman", 12, "bold"), state="readonly")
        gender_combo["values"] = ("Select", "Male",
                                  "Female", "Others")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Class DOB
        classDob_label = Label(class_student_frame, text="DOB", font=(
            "times new roman", 12, "bold"), bg="white")
        classDob_label.grid(row=2, column=2, padx=7, pady=5)

        classDob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20, font=(
            "times new roman", 12, "bold"))
        classDob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Class Email
        classEmail_label = Label(class_student_frame, text="Email", font=(
            "times new roman", 12, "bold"), bg="white")
        classEmail_label.grid(row=3, column=0, padx=7, pady=5)

        classEmail_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=(
            "times new roman", 12, "bold"))
        classEmail_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Class Phone No
        classPhoneNo_label = Label(class_student_frame, text="Phone No", font=(
            "times new roman", 12, "bold"), bg="white")
        classPhoneNo_label.grid(row=3, column=2, padx=7, pady=5)

        classPhoneNo_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20, font=(
            "times new roman", 12, "bold"))
        classPhoneNo_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Class Address
        classAdress_label = Label(class_student_frame, text="Address", font=(
            "times new roman", 12, "bold"), bg="white")
        classAdress_label.grid(row=4, column=0, padx=7, pady=5)

        classAdress_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20, font=(
            "times new roman", 12, "bold"))
        classAdress_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Class Teacher
        classTeacher_label = Label(class_student_frame, text="Teacher Name", font=(
            "times new roman", 12, "bold"), bg="white")
        classTeacher_label.grid(row=4, column=2, padx=7, pady=5)

        classTeacher_entry = ttk.Entry(class_student_frame, textvariable=self.var_teacher, width=20, font=(
            "times new roman", 12, "bold"))
        classTeacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # Radio Button
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(
            class_student_frame, variable=self.var_radio1, text="TakePhoto Sample", value="yes")
        radiobtn1.grid(row=6, column=0)

        self.var_radio2 = StringVar()
        radiobtn2 = ttk.Radiobutton(
            class_student_frame, variable=self.var_radio1, text="No photo Sample", value="no")
        radiobtn2.grid(row=6, column=1)

        # Button frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=200, width=715, height=35)

        save_btn = Button(btn_frame, command=self.add_data, text="save", width=14, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0, padx=3)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=14, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1, padx=5)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=14, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2, padx=5)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=14, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=5)

        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=235, width=715, height=35)

        takephoto_btn = Button(btn_frame1, text="Take Photo Sample", command=self.generate_dataset, width=30, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        takephoto_btn.grid(row=0, column=0, padx=3)

        updatephoto_btn = Button(btn_frame1, text="Update Photo Sample", command=self.generate_dataset, width=30, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        updatephoto_btn.grid(row=0, column=1)

        # Right frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                 text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=680, y=10, width=620, height=580)

        img_right = Image.open(
            r"C:\Users\Amresh Mishra\Desktop\face_recognition system\clg_img\img\student.jpg")
        img_right = img_right.resize((600, 130), Image.ANTIALIAS)
        self.photoimageright = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimageright)
        f_lbl.place(x=10, y=0, width=600, height=130)

        # search system
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE,
                                  text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=130, width=610, height=60)
        search_label = Label(search_frame, text="Search By", font=(
            "times new roman", 12, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=5)

        search_combo = ttk.Combobox(search_frame, font=(
            "times new roman", 12, "bold"), state="readonly")
        search_combo["values"] = ("Select",
                                  "Roll No", "Phone No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", width=15, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=2, padx=3)

        searchall_btn = Button(search_frame, text="Show All", width=15, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        searchall_btn.grid(row=0, column=3, padx=3)

        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=600, height=300)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=(
            "dep", "course", "year", "sem", "id", "name", "div", "roll", "gender",  "dob", "email", "phone", "address", "teacher", "photo"))

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

        # function declaration

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(), self.var_std_id.get(), self.var_std_name.get(), self.var_div.get(), self.var_roll.get(), self.var_gender.get(), self.var_dob.get(), self.var_email.get(), self.var_phone.get(), self.var_address.get(), self.var_teacher.get(), self.var_radio1.get()))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Student details has been saved successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To :{str(es)}", parent=self.root)

    # fetch data

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from Student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # get cusor...............

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

        # update variable

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "All Fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno(
                    "update", "Do you want to update this student details", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photosample=%s where Student_id=%s", (self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(
                        ), self.var_std_name.get(), self.var_div.get(), self.var_roll.get(), self.var_gender.get(), self.var_dob.get(), self.var_email.get(), self.var_phone.get(), self.var_address.get(), self.var_teacher.get(), self.var_radio1.get(), self.var_std_id.get()))
                else:
                    if not update:
                        return
                messagebox.showinfo(
                    "success", "Student details successfully update completed", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to:{str(es)}", parent=self.root)


# delete Function

    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "Student Delete Page", "Do you want to delete this student", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to:{str(es)}", parent=self.root)
    # Reset Button

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select")
        self.var_roll.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

        # generate data set or take photo sample

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute(
                    "update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photosample=%s where Student_id=%s", (self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(), self.var_std_name.get(), self.var_div.get(), self.var_roll.get(), self.var_gender.get(), self.var_dob.get(), self.var_email.get(), self.var_phone.get(), self.var_address.get(), self.var_teacher.get(), self.var_radio1.get(), self.var_std_id.get() == id+1))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

        # ========= Load predefined data on face frontals from opencv ======
                data.main(id)

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to:{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
