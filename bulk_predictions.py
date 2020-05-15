# 利用命令行脚本批量地产生预测
from os.path import split, splitext
import os
import glob

filenames = glob.glob('test' + '/*.png')

for filename in filenames:
    output_filename=splitext(split(filename)[1])[0] + '_test.png'
    os.system('python predict.py -i ' + f'{filename}' + ' -o ' + f'{output_filename}')