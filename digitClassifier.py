# libraries and modules
from keras.models import Sequential, load_model
from keras.layers import Dense, Activation, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Embedding
from keras.layers import LSTM

from keras.optimizers import RMSprop
from keras.optimizers import SGD

from keras import utils as np_utils

import numpy as np
from PIL import Image
import glob
import os
import h5py


# Retrieves images from path

def get_images(path, IMAGE_WIDTH, IMAGE_HEIGHT):

    images = []
    filenames = glob.glob(path)

    i = 0
    for f in filenames:
        image = Image.open(f).convert("L")
        image = image.resize((IMAGE_WIDTH,IMAGE_HEIGHT))
        images.append(np.array(image))
        i += 1

    print(i)
    images = np.array(images)
    print(images.shape)
    images = images.reshape(i, IMAGE_WIDTH, IMAGE_HEIGHT, 1)

    images = images.astype('float32')
    images /= 255

    return images

# Retrieves images from path
# Inverts images in black and white

def get_images_inverted(path, IMAGE_WIDTH, IMAGE_HEIGHT):

    images = []
    filenames = glob.glob(path)

    i = 0
    for f in filenames:
        image = Image.open(f).convert("L")
        image = image.resize((IMAGE_WIDTH,IMAGE_HEIGHT))
        images.append(np.array(image))
        i += 1

    print(i)
    images = np.array(images)
    print(images.shape)
    images = images.reshape(i, IMAGE_WIDTH, IMAGE_HEIGHT, 1)

    images = images.astype('float32')
    images /= 255

    images = 1 - images

    return images


def predict(path, image):

    model = load_model(path)
    p = model.predict(image, batch_size=32, verbose=1)

    return p

def main():

    one = get_images_inverted('./digits/one/*.png', 18, 18)

    prediction = predict('digitClassifier.h5', one)

    print(np.argmax(prediction,1))

if __name__ == "__main__":

    main()
