
import numpy as np
import cv2
import os

t=0.6
path='/home/thatwilliam/Documents/Pytorch-UNet-master'
a=cv2.imread(os.path.join(path, 'test/18.png'))
b=cv2.imread(os.path.join(path, '晶格.png'))
c=a+b
cv2.imshow('combo', c)
cv2.imwrite('combo.png', c)
cv2.waitKey(0)