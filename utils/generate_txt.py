# Encoding:UTF-8
# @Autor: Yuri Fan

'''
@说明：
此部分代码主要是按照比例随机生成训练图像的文件名和验证图像的文件名分别是train.txt和val.txt
@使用说明：
1、修改xml文件的存放路径以及输出txt文件的保存路径
2、根据需要修改训练验证集的比例
3、修改txt的保存路径
4、根据需要修改写入txt的内容
'''

import os
import random

# 将所有图片都分为训练集和验证集，所以trainval_percent设为1.0，否则设为<1.0
# 即把图片分为训练集和验证集以及测试集，但个人觉得没必要分测试集了
trainval_percent = 1.0
# 训练集占比80%，验证集占比20%
train_percent = 0.8
xmlfilepath = 'C:\\Users\\dell\\Desktop\\MaskVOC\\Annotations'
txtsavepath = 'C:\\Users\\dell\\Desktop\\MaskVOC\\ImageSets\\Main'
total_xml = os.listdir(xmlfilepath)
 
num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

# 修改txt的保存路径，会生成四个txt但有用的就是train.txt和val.txt，test.txt没有用到
# trainval.txt是指代train.txt和val.txt的总和
ftrainval = open('C:\\Users\\dell\\Desktop\\MaskVOC\\ImageSets\\Main\\trainval.txt', 'w')
ftest = open('C:\\Users\\dell\\Desktop\\MaskVOC\\ImageSets\\Main\\test.txt', 'w')
ftrain = open('C:\\Users\\dell\\Desktop\\MaskVOC\\ImageSets\\Main\\train.txt', 'w')
fval = open('C:\\Users\\dell\\Desktop\\MaskVOC\\ImageSets\\Main\\val.txt', 'w')

# 根据需要修改写入txt的内容，这里写入的是绝对路径下的图像文件格式
for i in list:
    name = total_xml[i][:-4]
    if i in trainval:
        ftrainval.write('/home/darknet/maskdata/images/' + name + '.jpg' + '\n')
        if i in train:
            ftrain.write('/home/darknet/maskdata/images/' + name + '.jpg' + '\n')
        else:
            fval.write('/home/darknet/maskdata/images/' + name + '.jpg' + '\n')
    else:
        ftest.write(name)
 
ftrainval.close()
ftrain.close()
fval.close()
ftest.close()