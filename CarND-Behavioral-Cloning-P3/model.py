import os
import csv
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Flatten, Dense, Lambda, Cropping2D, Dropout
from keras.layers.convolutional import Conv2D
from keras.layers.pooling import MaxPool2D
from keras import regularizers
import cv2
import numpy as np
import sklearn
import matplotlib.pyplot as plt

# Load simulation data
samples = []
with open('./driving-data/driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        samples.append(line)

# Split training from validation
train_samples, validation_samples = train_test_split(samples, test_size=0.2)

# Define generator for efficient generation of samples
def generator(samples, batch_size=32):
    num_samples = len(samples)
    while 1: # Loop forever so the generator never terminates
        for offset in range(0, num_samples, batch_size):
            batch_samples = samples[offset:offset+batch_size]

            images = []
            angles = []
            for batch_sample in batch_samples:
                name = './driving-data/IMG/'+batch_sample[0].split('/')[-1]
                center_image = cv2.imread(name)
                center_angle = float(batch_sample[3])
                images.append(center_image)
                angles.append(center_angle)

            # trim image to only see section with road
            X_train = np.array(images)
            y_train = np.array(angles)
            yield sklearn.utils.shuffle(X_train, y_train)

# compile and train the model using the generator function
batch_size = 256
train_generator = generator(train_samples, batch_size=batch_size)
validation_generator = generator(validation_samples, batch_size=batch_size)

ch, row, col = 3, 160, 320  # Image format

model = Sequential()

# Preprocess incoming data, normalizing it.
model.add(Lambda(lambda x: x/127.5 - 1.,
        input_shape=(row, col, ch)))

# LeNet architecture
model.add(Conv2D(24,(5,5),subsample=(2,2), activation='relu'))
model.add(Conv2D(36,(5,5),subsample=(2,2), activation='relu'))
model.add(Conv2D(48,(5,5),subsample=(2,2), activation='relu'))
model.add(Conv2D(64,(3,3), activation='relu'))
model.add(Dropout(0.5))
model.add(Conv2D(64,(3,3), activation='relu'))
model.add(Flatten())
model.add(Dense(100, kernel_regularizer=regularizers.l2(0.1)))
model.add(Dense(50))
model.add(Dense(10))

# Simple regression output
model.add(Dense(1))

model.compile(loss='mse', optimizer='adam')

train_steps = len(train_samples)/batch_size
print(train_steps)
validation_steps = len(validation_samples)/batch_size

history_object   = model.fit_generator(train_generator,
                    steps_per_epoch=train_steps,
                    validation_data=validation_generator,
                    validation_steps=validation_steps, nb_epoch=10, verbose=1)


### print the keys contained in the history object
print(history_object.history.keys())

### plot the training and validation loss for each epoch
plt.plot(history_object.history['loss'])
plt.plot(history_object.history['val_loss'])
plt.title('model mean squared error loss')
plt.ylabel('mean squared error loss')
plt.xlabel('epoch')
plt.legend(['training set', 'validation set'], loc='upper right')
plt.show()
