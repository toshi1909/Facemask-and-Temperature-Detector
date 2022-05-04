import cv2
import serial
# import CNN_code
import keras
import numpy as np
from keras.preprocessing import image
import time

#serial communication
serialport = serial.Serial(port='COM3', baudrate=9600, timeout=.1)


class Serial:
    def __init__(self, arduino):
        self.arduino = arduino

    def write(self, x):
        print(x)
        self.arduino.write(bytes(x, 'utf-8'))
        # time.sleep(0.05)

    def read(self):
        serialString = self.arduino.readline().rstrip()
        print(serialString)
        return serialString


# prediction
model = keras.models.load_model("model.h5")


def predict():
    tested_image = image.load_img('x.jpg', target_size=(64, 64))
    tested_image = image.img_to_array(tested_image)
    tested_image = np.expand_dims(tested_image, axis=0)
    output = model.predict(tested_image)
    # train_generator.class_indices
    if output[0][0] == 1:
        prediction = 'w' # without mask
    else:
        prediction = 'm' # mask

    return prediction


s = Serial(serialport)
cap = cv2.VideoCapture(1)
success, img = cap.read()

while True:
    r = s.read()
    while True:
        r = s.read()
        if r== b'1':
            break
    success, img = cap.read()
    cv2.imwrite('x.jpg', img)
    p = predict()
    print(p)
    s.write(p)
    #time.sleep(10)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
