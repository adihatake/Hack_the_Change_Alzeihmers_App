import cv2
import numpy as np
import keras 


from PIL import Image


PERSON_LIST = ['Adi', 'Phu']
target_size = (300, 300)

def resize_img(image, target_size=(400, 400)):
    new_img = cv2.resize(face_image, target_size, interpolation=cv2.INTER_AREA)
    return new_img

face_model = keras.models.load_model("/Users/catherinebalajadia/Downloads/Random_Coding_Projects/Hack_the_Change_2024/Training/trained_models/face_model1.keras")
face_image = cv2.imread("/Users/catherinebalajadia/Downloads/Random_Coding_Projects/Hack_the_Change_2024/sample_test.jpg")

input_image = resize_img(face_image)
predicted_scores = face_model(np.array([input_image]))
max_label_index = np.argmax(predicted_scores)
identified_person = PERSON_LIST[max_label_index]

print(identified_person)
    
while True:
    cv2.imshow("input_image", input_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break