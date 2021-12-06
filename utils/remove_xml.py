# Encoding:UTF-8
# @Autor: Yuri Fan

'''
@说明：
此部分代码主要利用是移除不符合要求的xml文件以及对应的图片文件
主要是由于某些xml文件中保存的不规范导致缺失图片的分辨率大小或者分辨率大小为0
@使用说明：
1、修改xml存放路径
2、修改移除xml和图片的路径
'''

import os
from tqdm import tqdm
from xml.dom.minidom import parse
xml_list = [
    file for file in os.listdir('C:/Users/dell/Desktop/MaskVOC/Annotations')
    if file.endswith('.xml')
]
xml_list = tqdm(xml_list)

for i in xml_list:
    filepath = 'C:/Users/dell/Desktop/MaskVOC/Annotations/' + i
    dom = parse(str(filepath))
    xml_root = dom.documentElement
    if not xml_root.getElementsByTagName("size") or xml_root.getElementsByTagName("size")[0] == 0:
        os.remove('C:/Users/dell/Desktop/MaskVOC/Annotations/' + i)
        os.remove('C:/Users/dell/Desktop/MaskVOC/JPEGImages/' + i[:-4] + '.jpg')
        continue
    img_size = xml_root.getElementsByTagName("size")[0]