import networkx as nx
from pylab import show
import numpy as np
import cv2
import re
from os.path import splitext
import os
import matplotlib.pyplot as plt

path='/home/thatwilliam/Documents/Pytorch-UNet-master/test'
files=os.listdir(path)
x=[]
y=[]
for file in files:
    if re.search('^3_test', splitext(file)[0]):
        img = cv2.imread(os.path.join(path, file), 0)
        ret,thresh = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        contours,hierarchy = cv2.findContours(thresh,  cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            M = cv2.moments(cnt)
            if(M['m00']==0):
                continue
            x.append(int(M['m10']/M['m00']))
            y.append(int(M['m01']/M['m00']))
x=np.array(x)
y=np.array(y)


from scipy import spatial
coords=np.stack((x.ravel(), y.ravel()), axis=-1)
tree = spatial.KDTree(coords)
def bond_length_calculator():
    bond_lengths=[]
    for coord in coords:
        bond_lengths.append(tree.query(coord, 8)[0])
    bond_lengths=np.array(bond_lengths)
    bond_lengths=bond_lengths[bond_lengths>30]
    bond_lengths=bond_lengths[bond_lengths<35]
    bond_length=np.mean(bond_lengths)
    print(f'The bond length is {bond_length}')


bond_length_calculator()

