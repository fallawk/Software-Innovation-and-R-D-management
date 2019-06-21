import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow, imread
import numpy as np
import keras
import os
import time
import sys
sys.path.append('/root/webapp/detector')

# import cPickle
from keras.layers import Input
from keras.models import Model

from keras_csp import config, bbox_process
from keras_csp.utilsfunc import *
from keras_csp import resnet50 as nn


class csp_det(object):
    def __init__(self, input_size=(640, 480)):
        self.C = config.Config()
        self.C.offset = True
        self.C.size_test = input_size
        input_shape_img = (self.C.size_test[0], self.C.size_test[1], 3)
        img_input = Input(shape=input_shape_img)
        # define the network prediction
        preds = nn.nn_p3p4p5(img_input, offset=self.C.offset, num_scale=self.C.num_scale, trainable=True)
        self.model = Model(img_input, preds)
        self.model_path = '/root/webapp/detector/models_weight'
        self.detec_hum(np.random.rand(200, 300, 3))

    def detec_hum(self, image): # arg: numpy array with shape of (, , 3)
        # resize the image manually to the fixed model input size
        # shape_orig = image.shape
        image = cv2.resize(image, (self.C.size_test[1], self.C.size_test[0]))
        x_rcnn = format_img(image, self.C)
        Y = self.model.predict(x_rcnn)
        boxes = bbox_process.parse_det_offset(Y, self.C, score=0.1,down=4)
        return boxes[boxes[:, 4]>0.3] if len(boxes)>0 else []

                    
