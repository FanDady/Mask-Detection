# Mask-Detection

基于YoloV3-tiny实现口罩检测，使用的YoloV3-tiny版本是C语言编译实现的非Python实现；YoloV3的基础框架主要基于Darknet实现，更多详细相关的工作或者文档可以参考[Darknet官方Github]([pjreddie/darknet: Convolutional Neural Networks (github.com)](https://github.com/pjreddie/darknet))或者[Darknet官网]([Darknet: Open Source Neural Networks in C (pjreddie.com)](https://pjreddie.com/darknet/))；该项目包含训练编译过的YoloV3-tiny源码和权重文件同时也包含1600张的口罩数据集.

![](https://s4.ax1x.com/2021/12/06/osPev6.jpg)



# Requirement

```
Python3
cmake
gcc
opencv3.5
tqdm
CUDA 10.2
Cudnn
Linux
```



# Quick Start

- 下载源码

```
git clone https://github.com/FanDady/Mask-Detection
```

- 进入darknet文件夹下并进行编译

```
cd Mask-Detection/darknet
make
```

- 测试口罩检测

```
./darknet detect test .maskdata/yolov3-tiny.cfg maskdata/backup/yolov3-tiny_10000.weights data/mask_test.jpg
```

- 在darknet目录下生成prediction.jpg预测图像



# Mask Dataset

- 口罩检测VOC格式数据集

```
# 百度网盘链接：https://pan.baidu.com/s/1ti0-C1p3i9md_tuI_8lryA
# 提取码：hfb6
```

- 口罩检测数据集文件结构

```
   |---Annotations----.xml                # XML标签数据
   |
   |---JPEGImages-----.jpg                # JPG图片
   |
   |---Main-----------|                   # 训练的图片的绝对路径的txt文件
                      |--train.txt
                      |--val.txt
                      |--trainval.txt
                      |--test.txt
   |---labels---------.txt                # 所有图片的txt标签，内容是：标签ID、x、y、width、height
```



# How to Train

