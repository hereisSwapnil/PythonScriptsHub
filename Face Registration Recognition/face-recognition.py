import cv2
import numpy as np
import face_recognition as fr
import pandas as pd

fd = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Reading data from csv file
try:
    face_db = pd.read_csv("./face_database.csv", index_col=0)
    final_data = {"NAMES": face_db["NAMES"].values.tolist(), "ENC": face_db["ENC"].values.tolist()}
except Exception as e:
    print(e)
    final_data = {"NAMES": [], "ENC": []}

# Video read using web cam
vid = cv2.VideoCapture(0)
captured = True
cropped_face = None

# main loop to read and show image until we break the loop
while captured :
    flag, img = vid.read()
    cropped_face = img

    # if flag is true then only show image
    if flag:
        faces = fd.detectMultiScale(img, 1.3, 5)
        for x,y,w,h in faces:
            cropped_face = img[y:y+h, x:x+w].copy()
            
            # It will check if face is present in front of cam for 20 frames
            if len(faces) == 1:
                try:
                    face_enc = fr.face_encodings(cropped_face)
                    for fe in final_data["ENC"]:
                        if fr.compare_faces(np.array(eval(fe)), face_enc)[0]:
                            cv2.putText(img, final_data["NAMES"][final_data["ENC"].index(fe)], (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)
                            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
                        else:
                            cv2.putText(img, "Unknown", (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,255), 2)
                            cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)
                except Exception as e:
                    print(e)
            else:
                print("Multiple faces detected")

        cv2.imshow("webcam_image", img)
        key = cv2.waitKey(1)
        if key == ord("q"):
            break
    else:
        break
vid.release()
cv2.destroyAllWindows()