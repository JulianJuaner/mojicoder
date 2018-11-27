#!/usr/bin/env python
from __future__ import print_function
from __future__ import absolute_import

import tensorflow as tf
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))

import sys

from utils import *
from emopred import *


def run(input_path, output_path, is_memory_intensive=False, pretrained_model=None):
    np.random.seed(7777)
    result = np.zeros((100, 3))
    datapath = '../dataset/fer2013/fer2013.csv'
    print('data loading...')
    FER2013 = input_data(datapath)
    FER2013.train.save_metadata(output_path)

    input_shape = (48, 48, 1)
    output_size = (7)
    steps_per_epoch = FER2013.train._num_examples / BATCH_SIZE
    model = EmoPred(input_shape, output_size, output_path)
    print('model complete!')
    if pretrained_model is not None:
        model.model.load_weights(pretrained_model)
    #result = np.empty((0))
    for m in range(0, 70):
        model.fit(FER2013.train._images, FER2013.train._labels)
        result[m] = (model.pred_accuracy(FER2013.test._images, FER2013.test._labels))
        if(result[m][2]>0.65):
            break;

    np.savetxt('test.txt', result, delimiter = ',')
        #model.test_batch(FER2013.test.images, FER2013.test._labels)
if __name__ == "__main__":
    argv = sys.argv[1:]

    if len(argv) < 2:
        print("Error: not enough argument supplied:")
        print("train.py <input path> <output path> <is memory intensive (default: 0)> <pretrained weights (optional)>")
        exit(0)
    else:
        input_path = argv[0]
        output_path = argv[1]
        use_generator = False if len(argv) < 3 else True if int(argv[2]) == 1 else False
        pretrained_weigths = None if len(argv) < 4 else argv[3]

    run(input_path, output_path, is_memory_intensive=use_generator, pretrained_model=pretrained_weigths)
