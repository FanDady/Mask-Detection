# Encoding:UTF-8
# @Autor: Yuri Fan

'''
@说明：
此部分代码主要利用是移除掉空的标签txt文件以及对应的图片文件
@使用说明：
1、修改文件总数num
2、修改路径
'''

import os
from tqdm import tqdm


num = 1083
for i in range(num):
    filename = '{:0>4s}'.format(str(i))
    size = os.path.getsize('C:/Users/dell/Desktop/VOC2021/labels/' + filename +
                           '.txt')
    if size == 0:
        os.remove('C:/Users/dell/Desktop/VOC2021/labels/' + filename + '.txt')
        os.remove('C:/Users/dell/Desktop/VOC2021/JPEGImages/' + filename + '.jpg')
        os.remove('C:/Users/dell/Desktop/VOC2021/Annotations/' + filename + '.xml')
