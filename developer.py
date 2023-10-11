from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import data


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x740+0+0")
        self.root.title("Developer")

        title_lbl = Label(self.root, text="Developer", font=(
            "times new roman", 36, "bold"), bg="black", fg="blue")
        title_lbl.place(x=0, y=0, width=1350, height=45)

        img_top = Image.open(
            r"images/1385386.jpg")
        img_top = img_top.resize((1350, 740), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=50, width=1360, height=740)

        # frame
        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=900, y=0, width=500, height=600)

        img_top1 = Image.open(
            r"images/nitz.jpg")
        img_top1 = img_top1.resize((200, 200), Image.ANTIALIAS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl = Label(main_frame, image=self.photoimg_top1)
        f_lbl.place(x=300, y=0, width=200, height=200)

        dev_label = Label(main_frame, text="Hello I am Nitish,", font=(
            "times new roman", 20, "bold"), bg="white", fg="blue")
        dev_label.place(x=0, y=5)
        dev_label1 = Label(main_frame, text="from BCA 6th sem", font=(
            "times new roman", 20, "bold"), bg="white", fg="blue")
        dev_label1.place(x=0, y=40)
        dev_label2 = Label(main_frame, text="This project is made for", font=(
            "times new roman", 20, "bold"), bg="white", fg="blue")
        dev_label2.place(x=0, y=80)
        dev_label3 = Label(main_frame, text="Final year submission.", font=(
            "times new roman", 20, "bold"), bg="white", fg="blue")
        dev_label3.place(x=0, y=120)

        img_top5 = Image.open(
            r"images/devl.jfif")
        img_top5 = img_top5.resize((500, 390), Image.ANTIALIAS)
        self.photoimg_top5 = ImageTk.PhotoImage(img_top5)

        f_lbl = Label(main_frame, image=self.photoimg_top5)
        f_lbl.place(x=0, y=210, width=500, height=390)


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
