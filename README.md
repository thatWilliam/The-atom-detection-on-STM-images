# The-atom-detection-on-STM-images

针对单层完美石墨烯的图像，进行全卷积型神经网络的训练，对实验图像进行测试并获取C-C键的键长分布。

其中：

    train.py为网络训练的主程序， dice_loss.py为代价函数计算， eval.py为训练过程中的验证
    
    change_label_to_gray.py将标签图灰度化，以适应网络结构
    
    lattice+source.py, plot_hex.py, plot_training_loss.py, plot_with_networkX.py, structure_plot.py用于论文作图
    
  


