import matplotlib.pyplot as plt
import numpy as np
import keras
import os
import cv2
from pandas import DataFrame


mnist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()


model = keras.models.load_model('handwritten.model')

loss,accuracy = model.evaluate(x_test, y_test)
print(loss)
print(accuracy)

image_number = 1

while os.path.isfile(f'Practice_imgs/{image_number}.png'):
    try:
        img = cv2.imread(f'Practice_imgs/{image_number}.png')[:,:,0]
        img = np.invert(np.array([img]))
        prediction = model.predict(img)
        print(DataFrame({'image': prediction[0]}))
        print('most probable: ', np.argmax(prediction))
        
        plt.imshow(img[0], cmap=plt.cm.binary)
        plt.show()
    except:
        print('Error!')
    finally:
        image_number+=1