from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import facerecog


class Face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1360x730+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=(
            "times new roman", 36, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1360, height=45)

        img_top = Image.open(
            r"clg_img\img\face_detector1.jpg")
        img_top = img_top.resize((650, 700), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=50, width=650, height=700)

        img_bottom = Image.open(
            r"clg_img\img\rr.jpg")
        img_bottom = img_bottom.resize((700, 700), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=50, width=700, height=700)

        face_btn = Button(f_lbl, text="Face Recognition", cursor="hand2", command=self.face_recog, font=(
            "times new roman", 15, "bold"), bg="green", fg="white")
        face_btn.place(x=270, y=590, width=150, height=40)

        # face recognition function

    def face_recog(self):
        facerecog.main()


if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()
