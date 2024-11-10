import keras
from keras import *
from keras.applications.mobilenet import MobileNet
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

num_classes = 3

base_model = MobileNet(include_top=False, weights=None, input_shape=(400, 400, 3), alpha=1.0, depth_multiplier=1)
base_model.load_weights('mobilenet_1_0_224_tf_no_top.h5')

base_model.trainable = False

# Create a model by adding a Dense layer on top of MobileNetV2
model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),  # Pooling to reduce dimensions
    layers.Dense(num_classes, activation='softmax')  # Output layer with 2 classes
])

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Summary of the model
model.summary()

data_location = "/Users/catherinebalajadia/Downloads/Random_Coding_Projects/Hack_the_Change_2024/Training/numpy_data"
face_train = np.load(f'{data_location}/face_train.npy')
face_targets = np.load(f'{data_location}/face_targets.npy')

batch_size = 16

history = model.fit(
                    x=face_train,
                    y=face_targets,
                    epochs=10,
                    batch_size=batch_size,
                    validation_split=0.2,
                               )

Model_num = 1
model.save(f"/Users/catherinebalajadia/Downloads/Random_Coding_Projects/Hack_the_Change_2024/Training/trained_models/face_model{Model_num}.keras")


#burrowed from https://machinelearningmastery.com/display-deep-learning-model-training-history-in-keras/
# summarize history for accuracy
plt.plot(history.history['val_accuracy'])
plt.title('Model 1 Validation Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epochs')
plt.ylim(0, 1.2)  # Set the y-axis limit from 0 to 1.2
plt.show()

# summarize history for loss
plt.plot(history.history['val_loss'])
plt.title('Model 1 Validation Loss')
plt.ylabel('Loss')
plt.xlabel('Epochs')
#plt.legend(['train', 'validation'], loc='upper left')
plt.show()