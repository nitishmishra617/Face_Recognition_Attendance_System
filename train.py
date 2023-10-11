from PIL import Image
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import train2


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("TRAIN DATA SET")

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=(
            "times new roman", 36, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1360, height=45)

        img_top = Image.open(
            r"clg_img\img\facialrecognition.png")
        img_top = img_top.resize((1360, 350), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=50, width=1360, height=290)

        train_btn = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2", font=(
            "times new roman", 32, "bold"), bg="red", fg="white")
        train_btn.place(x=0, y=335, width=1360, height=50)

        img_bottom = Image.open(
            r"clg_img\img\trainingimg.jpg")
        img_bottom = img_bottom.resize((1360, 350), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=400, width=1360, height=280)

        # data training function

    def train_classifier(self):
        mssg = train2.main()
        messagebox.showinfo("Result", mssg, parent=self.root)
        root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
