import threading
import cv2 
import os
from deepface import DeepFace

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0

face_matches = []
face_images = {}

images_path = "/Users/catherinebalajadia/Downloads/Random_Coding_Projects/Hack_the_Change_2024/Reference_Photos"

people_files = os.listdir(images_path)

if ".DS_Store" in os.listdir(images_path):
    os.remove(images_path+"/.DS_Store")
    people_files = os.listdir(images_path)

for person in people_files:
    input_img = cv2.imread(f"{images_path}/{person}")
    face_images[person] = input_img
    
    
def check_face(frame):
    global face_matches

    for person_present, reference_image in face_images.items():
        person_present = person_present.replace(".jpg", "")
        try:   
            if DeepFace.verify(frame, reference_image.copy())['verified']:
                if person_present not in face_matches:
                    face_matches.append(person_present)
            else:
                pass
        
        except ValueError:
            try:
                face_matches.clear()
            except:
                pass
    
 
while True:
    ret, frame = cap.read()
    
    if ret:
        if counter % 60 == 0:
            try:
                #check_face(frame)
                threading.Thread(target=check_face, args=(frame.copy(),)).start() 
            except ValueError:
                pass
        
        counter += 1

        if len(face_matches) > 0:
            people = ""
            person_num = 0
            for person in face_matches: 
                if person_num == 0:
                    people += person
                else:
                    people += f" and {person}"
                    
                person_num += 1
                
            if person_num == 1:
                cv2.putText(frame, f"{people} is here", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
            if person_num > 1:
                cv2.putText(frame, f"{people} are here", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                
        else:
            cv2.putText(frame, f"No one is here", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

        cv2.imshow("video", frame)
        
        key = cv2.waitKey(1)

        if key == ord("q"):
            break
            cv2.destroyAllWindows()
