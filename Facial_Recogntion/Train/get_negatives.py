import cv2

iterator = 1
name_dir = "Empty"

cap = cv2.VideoCapture(0)

def resize_img(image, target_size=(400, 400)):
    new_img = cv2.resize(image, target_size, interpolation=cv2.INTER_AREA)
    return new_img

while True:
    ret, frame = cap.read()
    cv2.imwrite(f"/Users/catherinebalajadia/Downloads/Random_Coding_Projects/Hack_the_Change_2024/Training/face_data/{name_dir}/{name_dir}_{iterator}.jpg", 
                                resize_img(frame))
    x = input('press enter to caputre')
    
    iterator += 1