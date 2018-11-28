import numpy as np
import math
'''0: horizontal, 1: vertical'''

def choose_eyebrow(points, case):
    width = math.sqrt((points[15][1] - points[0][1])*(points[15][1] - points[0][1])+\
    (points[15][0] - points[0][0])*(points[15][0] - points[0][0]))/175
    if points[17][1] - points[21][1]>=10*width:
        if points[26][1] - points[22][1]>=10*width:
            return 'smallLeftBrow\nsmallRightBrow'
        if case == 'sad' or case == 'angry':
            return 'very_pieLeftBrow\nvery_naRightBrow'
    if points[8][1] - points[19][1]>=150*width:
        return 'very_pieLeftBrow\nvery_naRightBrow'
    return "LeftBrow\nRightBrow"

def choose_eyes(points, case):
    width = math.sqrt((points[15][1] - points[0][1])*(points[15][1] - points[0][1])+\
        (points[15][0] - points[0][0])*(points[15][0] - points[0][0]))/175
    if case == 'angry':
        return 'angryLeftEye\nangryRightEye'
    if case == 'fear':
        if points[41][1] - points[38][1]>=7*width and points[46][1] - points[44][1]>=7*width:
            return 'pandaLeftEye\npandaRightEye'
        return 'vshapeLeftEye\nvshapeRightEye'
    if case == 'happy':
        if (points[39][0] - points[36][0]) -(points[40][1] - points[38][1])<=15*width:
            if points[40][1] - points[38][1]>=30*width:
                return 'bulingLeftEye\nbulingRightEye'
            return 'defaultLeftEye\ndefaultRightEye'
        print(points[11][1] - points[45][1])
        if points[5][1] - points[36][1]>=90*width and points[11][1] - points[45][1]>=90*width:
            return 'uppercLeftEye\nuppercRightEye'
        if points[39][1] - points[37][1]>=10*width and points[36][1] - points[38][1]>=10*width:
            return 'half_circleLeftEye\nhalf_circleRightEye'
        return 'cLeftEye\ncRightEye'
    if case == 'neural':
        if points[39][1] - points[37][1]<=5*width and points[36][1] - points[38][1]<=5*width:
            return 'lineLeftEye\nlineRightEye'
        return 'ringLeftEye\nringRightEye'
    if case =='suprise':
        return 'surpriseLeftEye\n surpriseRightEye'
    if case =='sad':
        if points[39][1] - points[36][1]>=7*width and points[42][1] - points[45][1]>=7*width:
            return 'vshapeLeftEye\nvshapeRightEye'
        if points[29][1] - points[40][1]<=30*width and points[29][1] - points[46][1]<=30*width:
            return 'very_low_upLeftEye\nvery_low_upLeftEye'
        if points[29][1] - points[40][1]>=60*width and points[29][1] - points[46][1]>=60*width:
            return 'up_cLeftEye\nup_cRightEye'
    if case =='digust':
        return 'chaLeftEye\nchaRightEye'
        return 'cryEyes\ncryEyes'
    return 'defaultLeftEye\ndefaultRightEye'

def choose_mouth(points, case):
    width = math.sqrt((points[15][1] - points[0][1])*(points[15][1] - points[0][1])+\
        (points[15][0] - points[0][0])*(points[15][0] - points[0][0]))/175
    if case == 'neural':
        if points[54][0] - points[48][0]>=80*width:
            if points[57][1] - points[51][1]<=20*width:
                return 'lineMouth'
            return 'waveMouth'
    if case == 'happy':
        if points[54][0] - points[48][0]<=30*width:
            return 'catMouth'
        if points[8][1] - points[57][1]<=20*width:
            return 'small_cMouth'
        if points[54][0] - points[48][0]>=60*width:
            if points[66][1] - points[62][1]>=25*width and points[63][0] - points[61][0]>=30*width:
                if points[8][1] - points[57][1]<=15*width:
                    return 'shipMouth\ntongueMouth'
                return 'shipMouth'
        print(width)
        if points[54][1] - points[48][1]>=20*width or points[48][1] - points[54][1]>=20*width:
            return 'hookMouth'
        if points[54][0] - points[48][0]>=50*width and points[57][1] - points[51][1]<=10*width and points[8][1] - points[57][1]<=20*width:
            return 'sweetMouth'
        if points[67][1] - points[61][1]>=10*width and points[65][1] - points[63][1]>=10*width and points[66][1] - points[62][1]>=10*width:
            return 'toothMouth'
        return 'cMouth'
    if case == 'sad' or case == 'angry':
        if points[54][0] - points[48][0]>=40*width:
            if points[59][1] - points[49][1]>=15 and points[55][1] - points[53][1]>=15*width:
                if points[54][0] - points[48][0]>=60*width:
                    return 'ovalMouth'
                return 'waaMouth'
            return 'lueMouth'
        if points[48][1] - points[51][1]>=20*width and points[57][1] - points[51][1]<=10*width:
            if points[8][1] - points[51][1]>=40*width:
                return 'down_cMonth'
            return 'very_lowMouth'
        return 'small_downMouth'
    if case == 'suprise':
        return 'surpriseMouth'
    if case == 'digust':
        return 'spannerMouth'
    if case == 'fear':
        if points[54][1] - points[48][1]>=50*width:
            return 'ovalMouth'
        return 'waaMouth'
    return "cMouth"

    return False
