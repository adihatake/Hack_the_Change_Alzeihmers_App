import cv2
import numpy as np
import keras 


def reformat_img(image, target_size=(400, 400)):
    new_img = cv2.resize(image, target_size, interpolation=cv2.INTER_AREA)
    return new_img

PERSON_LIST = ["Adi", "Phu", "Li"]

# Load a pre-trained DNN face detection model (Caffe model)
net = cv2.dnn.readNetFromCaffe('deploy.prototxt.txt', 'res10_300x300_ssd_iter_140000.caffemodel')
face_model = keras.models.load_model("/Users/catherinebalajadia/Downloads/Random_Coding_Projects/Hack_the_Change_2024/Training/trained_models/face_model1.keras")

# Initialize the webcam
cap = cv2.VideoCapture(0)

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
            
            face_image = frame[y1:y2, x1:x2]
            
            try:
                cv2.imshow("detected face", face_image)
                face_image = reformat_img(face_image)
                predicted_scores = face_model(np.array([face_image]))
                max_label_index = np.argmax(predicted_scores)
                identified_person = PERSON_LIST[max_label_index]
                print(identified_person)
                
            except:
                pass

           
    # Display the output frame
    cv2.imshow('DNN Face Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
