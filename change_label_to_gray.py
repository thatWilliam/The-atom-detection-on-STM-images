import numpy
import cv2
import os
import glob

filenames = glob.glob('data/masks' + '/*.png')
for idx, filename in enumerate(filenames):
    mask=cv2.imread(filename, 0)
    RGB_mask=mask
    cv2.imwrite(filename, RGB_mask)