
import time
from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_recognition
from tkinter import messagebox
from developer import Developer
from help import Help
from datetime import datetime
from time import strftime


class Face_Recognition_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1360x700+0+0")
        self.root.title("face Recognition system")

    # First Image
        img = Image.open(
            r"clg_img\img\university.jpg")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

    # second Image
        img1 = Image.open(
            r"clg_img\img\facialrecognition.png")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

    # third image
        img2 = Image.open(
            r"clg_img\img\clg.jpg")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=550, height=130)

        # background image
        img3 = Image.open(
            r"C:\Users\Amresh Mishra\Desktop\face_recognition system\clg_img\img\bgimg.jpeg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=(
            "times new roman", 28, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # ==========time=========
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font=("times new roman", 15, "bold"),
                    background="white", foreground="blue")
        lbl.place(x=0, y=0, width=110, height=50)
        time()

        # student button
        img4 = Image.open(
            r"C:\Users\Amresh Mishra\Desktop\face_recognition system\clg_img\img\student.jpg")
        img4 = img4.resize((200, 200), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4,
                    command=self.student_details, cursor="hand2")
        b1.place(x=200, y=70, width=200, height=200)

        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=270, width=200, height=40)

        # Face Detector
        img5 = Image.open(
            r"C:\Users\Amresh Mishra\Desktop\face_recognition system\clg_img\img\face_detector1.jpg")
        img5 = img5.resize((200, 200), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5,
                    cursor="hand2", command=self.face_data)
        b1.place(x=500, y=70, width=200, height=200)

        b1_1 = Button(bg_img, text="Face Detector", cursor="hand2", command=self.face_data, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=270, width=200, height=40)

        # Attendance
        img6 = Image.open(
            r"C:\Users\Amresh Mishra\Desktop\face_recognition system\clg_img\img\developer.jpg")
        img6 = img6.resize((200, 200), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6,
                    command=self.open_dev, cursor="hand2")

        b1.place(x=800, y=335, width=200, height=200)

        b1_1 = Button(bg_img, text="Developer", command=self.open_dev, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=535, width=200, height=40)

        # Help Desk
        img7 = Image.open(
            r"C:\Users\Amresh Mishra\Desktop\face_recognition system\clg_img\img\help.jpg")
        img7 = img7.resize((200, 200), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7,
                    cursor="hand2", command=self.open_help)
        b1.place(x=1100, y=70, width=200, height=200)

        b1_1 = Button(bg_img, text="Help Desk", cursor="hand2", command=self.open_help, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100, y=270, width=200, height=40)

        # Train Data
        img8 = Image.open(
            r"C:\Users\Amresh Mishra\Desktop\face_recognition system\clg_img\img\traindata.jpg")
        img8 = img8.resize((200, 200), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8,
                    cursor="hand2", command=self.train_data)
        b1.place(x=200, y=335, width=200, height=200)

        b1_1 = Button(bg_img, text="Train Data", cursor="hand2", command=self.train_data, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=535, width=200, height=40)

        # Photos
        img9 = Image.open(
            r"C:\Users\Amresh Mishra\Desktop\face_recognition system\clg_img\img\photos.jpg")
        img9 = img9.resize((200, 200), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9,
                    cursor="hand2", command=self.open_img)
        b1.place(x=500, y=335, width=200, height=200)

        b1_1 = Button(bg_img, text="Photos", cursor="hand2", command=self.open_img, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=535, width=200, height=40)

        # Attendance repot
        img10 = Image.open(
            r"C:\Users\Amresh Mishra\Desktop\face_recognition system\clg_img\img\face2.jpg")
        img10 = img10.resize((200, 200), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10,
                    cursor="hand2", command=self.attend_record)
        b1.place(x=800, y=70, width=200, height=200)

        b1_1 = Button(bg_img, text="Attendance Report", cursor="hand2", command=self.attend_record, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")

        b1_1.place(x=800, y=270, width=200, height=40)

        # Exit
        img11 = Image.open(
            r"C:\Users\Amresh Mishra\Desktop\face_recognition system\clg_img\img\exit.jpg")
        img11 = img11.resize((200, 200), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11,
                    cursor="hand2", command=self.exit_button,)
        b1.place(x=1100, y=335, width=200, height=200)

        b1_1 = Button(bg_img, text="Logout", cursor="hand2", command=self.exit_button, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100, y=535, width=200, height=40)

        # functions buttons........

    def open_img(self):
        os.startfile("dataset")

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognition(self.new_window)

    def open_dev(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def open_help(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)

    def exit_button(self):
        self.exit_button = messagebox.askyesno(
            "Face Recognition", "Are you sure you want to exit?", parent=self.root)
        if self.exit_button > 0:
            self.root.destroy()
        else:
            return

    def attend_record(self):
        os.startfile("records")


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_system(root)
    root.mainloop()
