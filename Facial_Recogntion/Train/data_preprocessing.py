import keras
import numpy as np
import os
import PIL

def get_images(input_images_dir):
  num_images = len(os.listdir(input_images_dir))  # find number of images in dataset
  data_loader_size = (400, 400)   #specify input image size for keras data loader
  final_image_size = (400, 400)  # specify final image size for the dataset
  dataset = np.zeros(shape=(num_images, final_image_size[0], final_image_size[1], 3))  # creates empty array of batches size (1000, 218, 336, 3)
                                                                           # indicates (num_imgs, image_dim1, image_dim2, #of channels like rgb)

  for image_index, file_name in enumerate(os.listdir(input_images_dir)):  # enumerate listing of image_dir
    image_path = f"{input_images_dir}/{file_name}"
    print(image_path)

    # load img from directory as a PIL instance
    img = keras.utils.load_img(
        path=image_path,
        color_mode='rgb',
        target_size=data_loader_size,
        interpolation='bilinear') # what is interpolation? --> helps rescale image if it doesn't fit with the target size

    img = keras.utils.img_to_array(img) # converts PIL instance from utils.load_img() to numpy array
    img = img.astype("float32") / 255 # scale pixel values to range of 0-1 to make model training easier
    dataset[image_index] = img # replace specific index of dataset to numpy image array

  return np.array(dataset) # return array of the dataset


def get_dataset(dataset_dir):
  input_data = [] # create some empty variables
  target_labels = []
  person_index = 0

  for person in names_list:
    face_img_data = get_images(f"{dataset_dir}/{person}") # get images from each directory

    num_images = len(face_img_data)
    num_classes = len(names_list)
    ground_truths = np.zeros(shape=(num_images, num_classes)) # create empty array of 1000 images and 10 classes --> np.shape() = (1000, 10)
    input_data.append(face_img_data) # add to overall list to convert to giant np array later

    for index in range(ground_truths.shape[0]): # for each image, change the value of the 10 array and put in a 1 for its class position (genre_index)
     ground_truths[index, person_index] = 1

    target_labels.append(ground_truths) # add to overall list to convert to giant np array later again
    person_index += 1 # iterate to next person genre

  #print(input_data[9].shape)
  input_data = np.vstack(input_data) # concatenate all classes
  target_labels = np.vstack(target_labels)
  
  return input_data, target_labels



dataset_path = "/Users/catherinebalajadia/Downloads/Random_Coding_Projects/Hack_the_Change_2024/Training/face_data"
names_list = ["Adi", "Phu", "Li"]

for name in names_list:
    dir_name = f"{dataset_path}/{name}"
    workdir = os.listdir(dir_name)
    if ".DS_Store" in workdir:
        os.remove(dir_name+"/.DS_Store")
        x = os.listdir(dir_name)
        
        
face_train, face_targets = get_dataset(dataset_path)

print(face_train.shape)
print(face_targets.shape)


save_location = "/Users/catherinebalajadia/Downloads/Random_Coding_Projects/Hack_the_Change_2024/Training/numpy_data"
np.save(f'{save_location}/face_train.npy', face_train)
np.save(f'{save_location}/face_targets.npy', face_targets)