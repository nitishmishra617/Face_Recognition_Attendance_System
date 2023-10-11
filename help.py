from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import data


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x740+0+0")
        self.root.title("Help Desk")

        title_lbl = Label(self.root, text="HELP DESK", font=(
            "times new roman", 36, "bold"), bg="black", fg="violet")
        title_lbl.place(x=0, y=0, width=1350, height=45)

        img_top = Image.open(
            r"images/dev.jpg")
        img_top = img_top.resize((1350, 740), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=50, width=1360, height=740)

        title_lbl2 = Label(self.root, text="Mail us: nitishofficial91@gmail.com", font=(
            "times new roman", 26, "bold"), bg="black", fg="green")
        title_lbl2.place(x=350, y=350, width=600, height=100)


if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
