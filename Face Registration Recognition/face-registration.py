import cv2
import face_recognition as fr
import pandas as pd

fd = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Reading data from csv file
try:
    face_db = pd.read_csv("./face_database.csv", index_col=0)
    final_data = {"NAMES": face_db["NAMES"].values.tolist(), "ENC": face_db["ENC"].values.tolist()}
except Exception as e:
    print(e)
    print("Creating new database")
    final_data = {"NAMES": [], "ENC": []}


# Video read using web cam
vid = cv2.VideoCapture(0)
counter = 0
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
                counter += 1
                if counter == 20:
                    # It will ask for name and save the face encodings in csv file
                    final_data["NAMES"].append(input("Enter your name: "))
                    face_enc = fr.face_encodings(cropped_face)
                    final_data["ENC"].append(face_enc[0].tolist())
                    db = pd.DataFrame(final_data)
                    db.to_csv("./face_database.csv")
                    captured = False
            else:
                counter = 0
            
        cv2.imshow("webcam_image",cropped_face)
        key = cv2.waitKey(1)
        if key == ord("q"):
            break
    else:
        break
vid.release()
cv2.destroyAllWindows()