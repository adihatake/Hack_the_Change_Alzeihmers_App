import cv2
import numpy as np
import time

def resize_img(image, target_size=(400, 400)):
    new_img = cv2.resize(face_image, target_size, interpolation=cv2.INTER_AREA)
    return new_img



# Load a pre-trained DNN face detection model (Caffe model)
net = cv2.dnn.readNetFromCaffe('deploy.prototxt.txt', 'res10_300x300_ssd_iter_140000.caffemodel')

# Initialize the webcam
cap = cv2.VideoCapture(0)

iterator = 1
name_dir = "Li"

while True:
    ret, frame = cap.read()
    height, width = frame.shape[:2]

    # Resize the frame to 300x300 for DNN input
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104.0, 177.0, 123.0))

    # Set the blob as input and get the face detections
    net.setInput(blob)
    detections = net.forward()

    # Draw bounding boxes around detected faces
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:  # You can adjust the threshold for confidence
            box = detections[0, 0, i, 3:7] * np.array([width, height, width, height])
            (x1, y1, x2, y2) = box.astype("int")
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            try:
                face_image = frame[y1:y2, x1:x2]
                cv2.imshow("detected face", face_image)
                waitr = input("press enter to capture")
                if waitr == "":
                    cv2.imwrite(f"/Users/catherinebalajadia/Downloads/Random_Coding_Projects/Hack_the_Change_2024/Training/face_data/{name_dir}/{name_dir}_{iterator}.jpg", 
                                resize_img(face_image))
                    iterator += 1
                else:
                    pass
                
                
            except:
                pass

            
            

    # Display the output frame
    cv2.imshow('DNN Face Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
