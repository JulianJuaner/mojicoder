from __future__ import print_function
from __future__ import absolute_import

import tensorflow as tf
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))

import sys
import cv2
from decision_tree import*
from utils import *
from emopred import *

        #model.fit(FER2013.train._images, FER2013.train._labels)

        #model.test_batch(FER2013.test.images, FER2013.test._labels)
if __name__ == "__main__":
    argv = sys.argv[1:]
    if len(argv) < 1:
        print("Error: not enough argument supplied:")
        print("sample.py <trained weights path> <trained model name> <input image> <output path> <search method (default: greedy)>")
        exit(0)
    elif len(argv) == 2: #for confusing graph。。。
        trained_weights_path = argv[0]
        datapath = '../dataset/fer2013/fer2013.csv'
        FER2013 = input_data(datapath)
        trained_model_name = 'emotion_prediction_contract'
        meta_dataset = np.load("{}/meta_dataset.npy".format(trained_weights_path))
        input_shape = (48, 48, 1)
        output_size = meta_dataset[1]
        model = EmoPred(input_shape, output_size, trained_weights_path)
        model.load(trained_model_name)
        listlabels = FER2013.test._labels.values.tolist()
        result = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],\
        [0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],]
        for img in range(0, 2000):
            m = np.argmax(model.predict((np.array([FER2013.test._images[img]]))))
            label = np.argmax(listlabels[img])
            print(m, label, listlabels[img])
            result[m][label] = result[m][label] + 1
            print(img)
        print(result)
    else:
        trained_weights_path = argv[0]
        input_path = argv[1]
        array_path = argv[2]
        img = cv2.imread(input_path, 0)
        trained_model_name = 'emotion_prediction_contract'
        meta_dataset = np.load("{}/meta_dataset.npy".format(trained_weights_path))
        input_shape = (48, 48, 1)
        output_size = meta_dataset[1]

        img = np.expand_dims(np.array([img]), -1)
        model = EmoPred(input_shape, output_size, trained_weights_path)
        model.load(trained_model_name)
        print('load over.')
        m = np.argmax(model.predict(img))
        cases = ['angry', 'digust', 'fear', 'happy', 'sad', 'suprise', 'neural']
        case = cases[m]
        print(case)
        points = np.reshape(np.loadtxt(array_path), (68, 2)).astype(int)
        eyebrow = choose_eyebrow(points, case)
        mouth = choose_mouth(points, case)
        eye = choose_eyes(points, case)
        print(eyebrow,mouth,eye)
        content = 'circleFace' + '\n' + eyebrow + '\n'+mouth+'\n'+eye
        file = open('DSL.emj', 'w+')
        file.write(content)
        file.close()
