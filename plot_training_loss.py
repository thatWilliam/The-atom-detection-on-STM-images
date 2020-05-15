import matplotlib.pyplot as plt
import numpy as np
#定义两个数组
Loss_list = []
Accuracy_list = []

Loss_list=np.load('loss.npy')
# Accuracy_list=np.load('acc.npy')
Learning_rate_list=np.load('learning_rate.npy')
#我这里迭代了200次，所以x的取值范围为(0，200)，然后再将每次相对应的准确率以及损失率附在x上
x1 = range(0, 45*25*5, 25*5)
x2 = range(0, 45*25*5, 25*5)
x3 = range(0, 45*25*5, 25*5)
y1 = Accuracy_list
y2 = Loss_list
y3 = Learning_rate_list

plt.figure()
plt.plot(x2, y2, '.-', color='g')
plt.title('Training loss vs. Iters')
plt.xlabel('Iters')
plt.ylabel('Training loss')
plt.savefig("Training_loss.jpg")
plt.figure()
plt.plot(x3, y3, '.-')
plt.title('Learning rate vs. Iters')
plt.xlabel('Iters')
plt.ylabel('Learning rate')
plt.savefig("Learning_rate.jpg")
plt.show()

