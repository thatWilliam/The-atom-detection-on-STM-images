# import networkx as nx
# from pylab import show
import numpy as np
import os
# coding:utf-8
import matplotlib as mpl
from matplotlib import pyplot as plt
mpl.rcParams['font.sans-serif'] = ['simhei']
mpl.rcParams['axes.unicode_minus'] = False
# G=nx.Graph()
# G.add_edge(1, 2)
# G.add_edge(1, 2)
# G.add_edge(1, 2)
# nx.draw(G)
# show()
#

# kdtree查找实例
# from scipy import spatial
# x, y = np.mgrid[0:5, 2:8]
# print(x.ravel())
# tree = spatial.KDTree(np.stack((x.ravel(), y.ravel()), axis=-1))
# tree.data
# pts = np.array([[0, 0], [2.1, 2.9]])
# print(tree.query(pts, 1))
# print(tree.query(pts, 3))


import cv2
path='/home/thatwilliam/Documents/Pytorch-UNet-master'
img = cv2.imread(os.path.join(path, 'test/18_test.png'), 0)
ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
plt.figure(figsize=(6, 6))
cx=[]
cy=[]
for cnt in contours:
    M = cv2.moments(cnt)
    if (M['m00'] == 0):
        continue
    x=int(M['m10'] / M['m00'])
    y=int(M['m01'] / M['m00'])
    cx.append(x)
    cy.append(y)
    plt.scatter(x, y, s=5, c='k')
    plt.axis('off')
    plt.axis("equal")
# plt.show()

from scipy import spatial
def bond_length_cal():
    lattices = np.stack((cx, cy), axis=-1)
    tree = spatial.KDTree(lattices)
    a = []
    count = 0
    bond_length = []
    for lattice in lattices:
        query_result = tree.query(lattice, 8)
        a.append(query_result[0])
        if np.all(query_result[0][1:7] > 30) and np.all(query_result[0][1:7] < 36):
            bond_length.append(query_result[0][1:7])
            count += 1
    a = np.array(a)
    bond_length = np.array(bond_length)*0.143/33.16283
    bond_length_average=np.mean(bond_length)#1.43/33.16283
    print(bond_length_average)


    """
    绘制直方图
    data:必选参数，绘图数据
    bins:直方图的长条形数目，可选项，默认为10
    normed:是否将得到的直方图向量归一化，可选项，默认为0，代表不归一化，显示频数。normed=1，表示归一化，显示频率。
    facecolor:长条形的颜色
    edgecolor:长条形边框的颜色
    alpha:透明度
    """
    plt.figure()
    plt.hist(bond_length.ravel(), bins=12, range=(0.130, 0.154), rwidth=1, normed=1, facecolor="blue", edgecolor="black", alpha=0.7)
    # 显示横轴标签
    plt.xlabel(u'C-C bond length (nm)')
    # 显示纵轴标签
    plt.ylabel(u'Count')
    # 显示图标题
    plt.title(u'The bond lengths of graphene')
    plt.savefig('石墨烯键长分布图.png')
    plt.show()

bond_length_cal()

from scipy import spatial
lattices=np.stack((cx, cy), axis=-1)
tree = spatial.KDTree(lattices)
a=[]
count=0
real_lattice = []
for lattice in lattices:
    query_result=tree.query(lattice, 13)
    a.append(query_result[0])
    if np.all(query_result[0][7:]<60) and np.all(query_result[0][7:]>55) and np.all(query_result[0][1:7]>30) and np.all(query_result[0][1:7]<35):
        real_lattice.append((lattices[query_result[1][7:]]-np.tile(lattice, (6, 1)))*1/3+np.tile(lattice, (6, 1)))
        real_lattice.append((lattices[query_result[1][7:]]-np.tile(lattice, (6, 1)))*2/3+np.tile(lattice, (6, 1)))
        count+=1
a=np.array(a)
real_lattice=np.array(real_lattice)
plt.figure(figsize=(6, 6))

plt.scatter(real_lattice[:,:,0], real_lattice[:,:,1], s=5, c='k')
plt.axis('off')
plt.axis("equal")
plt.savefig('process.png')
plt.show()
print(real_lattice.shape)

import networkx as nx
print(os.path.join(path, 'process.png'))
img=cv2.imread(os.path.join(path, 'process.png'), 0)

ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
plt.figure(figsize=(6, 6))
cx=[]
cy=[]
for cnt in contours:
    M = cv2.moments(cnt)
    if (M['m00'] == 0):
        continue
    x = int(M['m10'] / M['m00'])
    y = int(M['m01'] / M['m00'])
    cx.append(x)
    cy.append(y)
    plt.scatter(x, y, s=10, c='k')
    plt.axis('off')
    plt.axis("equal")
save_path = os.path.join(path, 'process2.png')
plt.savefig(save_path)
img = cv2.imread(save_path, 0)
flip = cv2.flip(img, 0)
cv2.imwrite(save_path, flip)
plt.show()


G=nx.Graph()
nodes=np.stack((cx, cy), axis=-1)
# kdtree查找实例
tree = spatial.KDTree(nodes)
to_plot=[]
b=[]
for node in nodes:
    query_result=tree.query(node, 4)
    b.append(query_result[0])
    if np.all(query_result[0][1:]>15) and np.all(query_result[0][1:]<20):
        to_plot.append(node)
        for i in range(1, 4):
            to_plot.append(nodes[query_result[1][i]])

b=np.array(b)
print(b.shape)
to_plot=np.array(to_plot)
for i in range(to_plot.shape[0]):
    if i%4==0:
        for j in range(1, 4):
            G.add_edge(i, i+j)

nx.draw(G, to_plot, node_color='b', node_size=3)
plt.axis("equal")
plt.savefig('networkX.png')
plt.show()

# def opecv_muti_pic():
#     # 图1
#     img = cv2.imread(os.path.join(path, 'test/22_test.png'))
#     # 图2
#     img2 = cv2.imread(os.path.join(path, 'networkX.png'))
#     # 图集
#     imgs = img+img2
#     # 展示多个
#     cv2.imshow("mutil_pic", imgs)
#     #等待关闭
#     cv2.waitKey(0)
# opecv_muti_pic()