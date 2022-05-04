import keras
import PIL

from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPool2D
from keras.layers import Flatten
from keras.layers import Dense, Dropout

# initialising CNN
model = Sequential()

# Adding 1st layer
model.add(Convolution2D(32, (3, 3), input_shape=(64, 64, 3), activation='relu'))
model.add(MaxPool2D(pool_size=(2, 2)))

# Adding 2nd layer
model.add(Convolution2D(32, (3, 3), activation='relu'))
model.add(MaxPool2D(pool_size=(2, 2)))


# Flattening
model.add(Flatten())

# Making Connections
model.add(Dense(units=128, activation='relu'))
model.add(Dropout(0.4))
model.add(Dense(units=64, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(units=64, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(units=1, activation='sigmoid'))

# Compiling
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

import zipfile
from zipfile import ZipFile

file = "archive.zip"
with ZipFile(file, 'r') as z:
    z.extractall()
    print('finish')


from keras.preprocessing.image import ImageDataGenerator

data = ImageDataGenerator(rescale=1. / 255,
                          shear_range=0.2,
                          zoom_range=0.2,
                          horizontal_flip=True)

# Splitting into training and test sets
train_datagen = ImageDataGenerator(rescale=1. / 255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True,
                                   validation_split=0.2)  # set validation split

train_generator = train_datagen.flow_from_directory(
    'dataset',
    target_size=(64, 64),
    batch_size=32,
    class_mode='binary')  # set as training data

validation_generator = train_datagen.flow_from_directory(
    'dataset',
    target_size=(64, 64),
    batch_size=32,
    class_mode='binary',
    subset='validation')  # set as validation data

model.fit_generator(
    train_generator,
    steps_per_epoch=150,
    epochs=5,
    validation_data=validation_generator,
    validation_steps=800)

model.save('model.h5')

model = keras.models.load_model("model.h5")

import numpy as np
from keras.preprocessing import image

tested_image = image.load_img('x.jpg', target_size=(64, 64))
tested_image = image.img_to_array(tested_image)
tested_image = np.expand_dims(tested_image, axis=0)
output = model.predict(tested_image)
#train_generator.class_indices
if output[0][0] == 1:
    prediction = 'Without Mask'
    print(prediction)
else:
    prediction = 'Mask'
    print(prediction)

tested_image = image.load_img('lol2.jpg', target_size=(64, 64))
tested_image = image.img_to_array(tested_image)
tested_image = np.expand_dims(tested_image, axis=0)
output = model.predict(tested_image)
#train_generator.class_indices
if output[0][0] == 1:
    prediction = 'Without Mask'
    print(prediction)
else:
    prediction = 'Mask'
    print(prediction)

