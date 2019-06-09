import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow, imread
import keras
import os
import time
# import cPickle
from keras.layers import Input
from keras.models import Model
from keras_csp import config, bbox_process
from keras_csp.utilsfunc import *
from keras_csp import resnet50 as nn


# define the network prediction
preds = nn.nn_p3p4p5(img_input, offset=C.offset, num_scale=C.num_scale, trainable=True)
model = Model(img_input, preds)

class detector(object):
    def __init__(self, input_size=(480, 640)):
        self.C = config.Config()
        self.C.offset = True
        self.C.size_test = input_size
        input_shape_img = (self.C.size_test[0], self.C.size_test[1], 3)
        img_input = Input(shape=input_shape_img)
        # define the network prediction
        preds = nn.nn_p3p4p5(img_input, offset=C.offset, num_scale=C.num_scale, trainable=True)
        self.model = Model(img_input, preds)

    def detec_hum(self, image): # arg: numpy array with shape of (, , 3)
        # resize the image manually to the fixed model input size
        shape_orig = image.shape
        image = cv2.resize(image, (self.C.size_test[1], self.C.size_test[0]))
	return []

                    
