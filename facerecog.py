import cv2
import numpy as np
import os
import mysql.connector
import attendence
from datetime import datetime


def main():
    n, d, r = "", "", ""
    cnt = 0
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)

    font = cv2.FONT_HERSHEY_SIMPLEX

    # iniciate id counter
    id = 0

    # names related to ids: example ==> Marcelo: id=1,  etc
    names = ['None', 'nitesh', 'kannaiah']

    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # set video widht
    cam.set(4, 480)  # set video height

    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    present = [("ID", "NAME", "DEPARTMENT", "DATE AND TIME")]
    roll = []
    while True:

        ret, img = cam.read()
        # img = cv2.flip(img, -1)  # Flip vertically
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )

        for(x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            id, confidence = recognizer.predict(gray[y:y+h, x:x+w])

            # Check if confidence is less them 100 ==> "0" is perfect match
            if (confidence < 100):
                #id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute(
                    "select Name from student where Student_id="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute(
                    "select Roll from student where Student_id="+str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute(
                    "select Dep from student where Student_id="+str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                if id not in roll:
                    cnt = cnt+1
                    k = datetime.now()
                    k = str(k)
                    k = k[:-10]
                    present.append((id, n, d, k))
                    print("present value is", present)
                    roll.append(id)
                    print("roll value is")
                    print("person cnt", cnt)
                    cv2.putText(img, str(present), (30, 80),
                                font, 1, (255, 255, 255), 2)

            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))

            cv2.putText(img, str(n), (10, 50), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(d), (10, 70), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(r), (10, 100), font, 1, (255, 255, 255), 2)

        cv2.imshow('camera', img)

        k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
        if k == 27:
            present = tuple(present)
            print("final present list is", present)
            attendence.main(present)
            break

    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()
    # return id,confidence

# main()
