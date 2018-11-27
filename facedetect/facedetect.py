# -*- coding: utf-8 -*-

import sys
import dlib
import os
import cv2
from skimage import io
def facedetect(dirpath, size = 48, grayscale = True):
    detector = dlib.get_frontal_face_detector()
    #win = dlib.image_window()
    #dirpath = sys.argv[1]
    #outputpath = sys.argv[2]
    width = 0
    height = 0
    print("Processing file: {}".format(dirpath))
    if grayscale == True:
        img = cv2.imread(dirpath, 0)
    else:
        img = cv2.imread(dirpath)
    #print(len(img[0]), len(img[0][0]))
    dets = detector(img, 1)

    print("Number of faces detected: {}".format(len(dets)))
    for i, d in enumerate(dets):
        #print("dets{}".format(d))
        #print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}"
            #.format( i, d.left(), d.top(), d.right(), d.bottom()))
        width = int(d.right())-int(d.left())
        height = int(d.bottom())-int(d.top())
        print(d.right(), d.left(), width, height)
        if height > width:
            diff = (int)(height-width)/2
            im = img[(int)(d.top()):int(d.bottom()), max(0,int(d.left()-diff)):int(d.right()+diff)]
        else:
            diff = -(int)(height-width)/2
            im = img[int(d.top()-diff):int(d.bottom()+diff), max(0,int(d.left())):int(d.right())]
            im = cv2.resize(im, (size, size))
    #dets, scores, idx = detector.run(img, 1)
    #for i, d in enumerate(dets):
        #print("Detection {}, dets{},score: {}, face_type:{}".format( i, d, scores[i], idx[i]))
    #win.set_image(im)
    #win.add_overlay(dets)
    return im
    #dlib.hit_enter_to_continue()
