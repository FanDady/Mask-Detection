# Encoding:UTF-8
# @Autor: Yuri Fan

'''
@说明：
此部分代码主要是修改txt文件里面的内容
@使用说明：
1、修改txt文件的存放路径
2、根据需要修改txt文件中每一行需要修改的内容
'''

import os
import glob

readfile = open('C:/Users/dell/Desktop/MaskVOC/ImageSets/Main/train.txt', 'r')
fline = readfile.readlines()
savetxt = open('C:/Users/dell/Desktop/MaskVOC/ImageSets/Main/train.txt', 'w')

for i in fline:
    print(i)
    s = '/home/darknet/maskdata/images/' + str(i) + '.jpg'
    print(s)

