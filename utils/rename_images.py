# Encoding:UTF-8
# @Autor: Yuri Fan

'''
@说明：
此部分代码主要利用是规范化文件夹下图片和对应的xml标签的文件名
@使用说明：
1、修改train_list中存放xml标签文件的位置
2、修改文件命名的起始数，该变量j代表从数字j开始命名比如j=0即比如从0.jpg开始
3、修改重新命名的路径和规范化命名格式比如使用.format规范命名比如规范命名有几个字符
4、os.rename方法第一个参数是图片的原始路径，第二个参数是图片改变后的保存路径
'''


import os
from tqdm import tqdm

# 存放xml标签文件的位置
train_list = [
    file
    for file in os.listdir('C:/Users/dell/Desktop/mask/val/ann')
    if file.endswith('.xml')
]

train_list = tqdm(train_list)
# 文件命名的起始数
j = 0

for i in train_list:
    # 其中取i[:-4]是只取文件名，因为i是根据xml文件夹遍历的所以i是xxx.xml
    # print(i[:-4])
    # 修改xml文件的命名，以及根据需要修改保存的路径
    os.rename(
        'C:/Users/dell/Desktop/mask/val/ann/' + i,
        'C:/Users/dell/Desktop/mask/val/ann/' +
        '{:0>4s}'.format(str(j)) + '.xml')

    # 修改对应的图片文件的命名，以及根据需要修改图片保存路径
    os.rename(
        'C:/Users/dell/Desktop/mask/val/img/' + i[:-4] + '.jpg',
        'C:/Users/dell/Desktop/mask/val/img/' +
        '{:0>4s}'.format(str(j)) + '.jpg')
    j += 1

# for i in range(100):
#     s = str(i + 1)
#     s = s.zfill(6)
#     os.rename('C:/Users/dell/Desktop/HR/DIV2K_' + s + '.png', 'C:/Users/dell/Desktop/HR/' + str(i+1) + '.jpg')
