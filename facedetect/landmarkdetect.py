# -*- coding: utf-8 -*-

import dlib

import numpy as np

from skimage import io

import sys
import cv2
import os

predictor_path = "../lmdat/shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)
#win = dlib.image_window()

def get_landmarks(im):
    dets = detector(im, 1)
    for k, d in enumerate(dets):
        shape = predictor(img, d)

    vec = np.empty([68, 2], dtype = int)
    for b in range(68):
        vec[b][0] = shape.part(b).x
        vec[b][1] = shape.part(b).y
    return vec

#coordinate = [0:top, 1:bottom, 2:right, 3:left, 4:width, 5:height]
def resize_and_recoordinate(img, points, coor):
    print("coor", coor)
    if coor[5] > coor[4]:
        diff = (int)((coor[5] - coor[4])/2)
        im = img[coor[0]:coor[1], max(0, coor[2]-diff):coor[3]+diff]
    else:
        diff = (int)((coor[4] - coor[5])/2)
        print(diff)
        im = img[max(0, coor[0]-diff):coor[1]+diff, coor[2]:coor[3]]
    im = cv2.resize(im, (256, 256))

    if coor[5]>coor[4]:
        coor[4] = coor[5]
    else:
        coor[5] = coor[4]

    for m in range(len(points)):
        points[m][0] = (int)((points[m][0]-left)*256/coor[4])
        points[m][1] = (int)((points[m][1]-top)*256/coor[5])
    return im, points;

if __name__ == '__main__':

    top = 30000
    bottom = 0
    left = 0
    right = 30000

    for arg in sys.argv[1:]:
        print('now is processing: {}'.format(arg))
        img = io.imread(arg)
        #win.clear_overlay()
        #win.set_image(img)

        #w = len(img[0]) # width of the original image.
        #h = len(img)    # height of the original image.

        dets = detector(img, 1)

        print("Number of faces detected: {}".format(len(dets)))
        for k, d in enumerate(dets):
            print("dets{}".format(d))

            print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
            k, d.left(), d.top(), d.right(), d.bottom()))

            shape = predictor(img, d)
            print("Part 0: {}, Part 1: {} ...".format(shape.part(0),  shape.part(1)))
            #win.add_overlay(shape)

            left = int(d.left())
            top = int(d.top())
            bottom = int(d.bottom())
            right = int(d.right())

        landmarks = get_landmarks(img)

        print((landmarks[3][0]))
        for m in landmarks:
            if m[1] < top:
                top = m[1] - 1
            if m[1] > bottom:
                bottom = m[1] + 1
            if m[0] > right:
                right = m[0] + 1
            if m[0] < left:
                left = m[0] - 1

        width = right - left
        height = bottom - top
        coordinate = [top, bottom, left, right, width, height]
        print(coordinate)
        image, points = resize_and_recoordinate(img, landmarks, coordinate)
        cv2.imwrite('lalala.jpg',image)
        _48_ = cv2.resize(image, (48, 48))

        cv2.imwrite('48x48.jpg',_48_)
        from PIL import Image
        img = Image.open('48x48.jpg').convert('LA')
        img.save('greyscale.png')
        print("face_landmark (re-coordinated):")
        print(landmarks)
        np.savetxt('landmarks.txt', landmarks)
        #dlib.hit_enter_to_continue()
