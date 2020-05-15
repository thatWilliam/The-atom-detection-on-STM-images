import numpy as np
import cv2
import re
from os.path import splitext
import os
import matplotlib.pyplot as plt


# #debug for '11_test.png'
# path='/home/thatwilliam/Documents/Pytorch-UNet-master/test'
# img = cv2.imread(path+'/11_test.png', 0)
# ret,thresh = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
# cv2.imshow('a', thresh)
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (6, 6))
# opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
# cv2.imshow('opened', opening)
# cv2.waitKey(0)
# ###

path='/home/thatwilliam/Documents/Pytorch-UNet-master/test'
files=os.listdir(path)
for file in files:
    if re.search('_test', splitext(file)[0]):
        img = cv2.imread(os.path.join(path, file), 0)
        ret,thresh = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        contours,hierarchy = cv2.findContours(thresh,  cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        plt.figure(figsize=(6, 6))
        for cnt in contours:
            M = cv2.moments(cnt)
            if(M['m00']==0):
                continue
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            plt.scatter(cx, cy, s=5, c='k')
            plt.axis('off')
            plt.axis("equal")
        save_path=path[:-4]+ 'structure_plot/' + splitext(file)[0][:-4] + 'structure.png'
        plt.savefig(save_path)
        img = cv2.imread(save_path, 0)
        flip = cv2.flip(img, 0)
        cv2.imwrite(save_path, flip)
        # plt.show()
