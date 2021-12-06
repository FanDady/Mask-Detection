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

# Structure

```
|-- utils
    |-- gen_yolo_format.py       # Python版的Yolo训练数据集生成，从VOC格式到YOLO格式
    |-- generate_txt.py          # 根据比例随机生成需要训练的图像名和验证图像名
    |-- get_images.py            # 网络爬虫爬取网络图像
    |-- remove_txt.py            # 去除掉一些可能是空的txt文件并把对应的图片删掉
    |-- remove_xml.py            # 删掉不符合xml要求的xml标签文件并把对应的图片删掉
    |-- rename_images.py         # 重新给图片数据集以及xml标签文件重命名有序命名
|-- darknet
    |-- cfg                      # 配置文件
    |-- data                     # 数据文件
    |-- maskdata                 # 存放训练需要的重要文件
    	|-- backup               # 存放训练后的模型
     		|-- yolov3-tiny.backup 
   			|-- yolov3-tiny_10000.weights  # 训练后的模型
		|-- images               # 训练图像
		|-- labels               # 训练标签
		|-- train.txt            # 需要训练的图像名
		|-- val.txt              # 需要验证的图像名
		|-- voc.data             # 数据格式
		|-- voc.names            # 数据标签名
		|-- yolov3-tiny.cfg      # yolov3-tiny配置文件
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
   |---Annotations 
   	   |--.xml                            # XML标签数据
   |---JPEGImages
       |--.jpg                            # JPG图片
   |---Main                               # 训练的图片的绝对路径的txt文件
       |--train.txt
       |--val.txt
       |--trainval.txt
       |--test.txt
   |---labels
       |--.txt                            # 所有图片的txt标签，内容是：标签ID、x、y、width、height
```

# How to Train

##  一、准备数据集

- 制作自己的数据集，收集好图像并命名好使用Labelbox 、CVAT 、精灵标注助手等标注工具标注生成xml文件并且文件格式放置参照VOC数据集格式如下其中Main文件的txt文件可通过`/utils/generate_txt.py`生成

```
   |---Annotations 
   	   |--.xml                            # XML标签数据
   |---JPEGImages
       |--.jpg                            # JPG图片
   |---Main                               # 训练的图片的绝对路径的txt文件
       |--train.txt
       |--val.txt
       |--trainval.txt
       |--test.txt
   |---labels
       |--.txt                            # 所有图片的txt标签，内容是：标签ID、x、y、width、height
```

- 其中对于train.txt和val.txt的图像文件名要按照绝对路径来写

## 二、训练模型

- 从头开始训练自己的数据集和模型
- 下载官方的源码文件

```
git clone https://github.com/pjreddie/darknet.git
cd darknet
```

- 修改Makefile的前几行

```
GPU=1
CUDNN=1    # 如果没有装cudnn就不要改了让CUDNN=0
OPENCV=1   # 如果没有装 OPENCV的C++版那就别改了让OPENCV=0
# 注意：每次修改完Makefile文件都需重新make编译
```

- 编译

```
make
# 注意：如果出现couldn’t open file: data/coco.names问题则很可能是因为安装包问题，Windows和Linux编码不同导致的错误，所以请直接下载源码安装包再放入# Linux服务器里面，不要在Windows下解压后再放进Linux服务器中
```

- 下载yolov3-tiny的预训练模型进行测试

```
wget https://pjreddie.com/media/files/yolov3-tiny.weights
./darknet detect cfg/yolov3-tiny.cfg yolov3-tiny.weights data/dog.jpg
```

- 在darknet目录下创建maskdata文件夹用来存放训练要用的所有文件和数据集

- 修改cfg/voc.data，修改后把voc.data放入maskdata文件夹下

```
classes= 2      #自己的类别数
train  = /home/darknet/maskdata/train.txt  # 存放训练图像路径
valid  = /home/darknet/maskdata/val.txt    # 存放验证图像路径
names = /home/darknet/maskdata/voc.names   # 存放检测的标签
backup = /home/darknet/maskdata/backup     # 存放训练后的模型
```

- 修改cfg/yolov3-tiny.cfg文件，修改后放入maskdata文件夹下

```
# 关闭Testing的参数打开training的参数
[net]
#Testing
#batch=1
#subdivisions=1
#Training
batch=64
subdivisions=16
····
····

# 以下的修改一共有两个地方即要修改两个filters和classes
[convolutional]
size=1
stride=1
pad=1
filters=21       # 改为3*(classes +5)
activation=linear

[yolo]
mask = 3,4,5
anchors = 10,14,  23,27,  37,58,  81,82,  135,169,  344,319
classes=2     # 改为自己的类别数目
num=6
jitter=.3
ignore_thresh = .7
truth_thresh = 1
random=1
```

- 修改data/voc.names，修改后放入voc.names

```
mask
nomask
```

- 回到darknet目录下产生yolov3-tiny的预训练模型

```
./darknet partial ./maskdata/yolov3-tiny.cfg ./maskdata/yolov3-tiny.weights ./yolov3-tiny.conv.15 15
```

- 开始训练模型，前1000周期每隔100就会保存一次模型，后面开始每隔10000个保存一次

```
sudo ./darknet detector train maskdata/voc.data maskdata/yolov3-tiny.cfg yolov3-tiny.conv.15
```

- 测试模型

```
./darknet detect test .maskdata/yolov3-tiny.cfg maskdata/backup/yolov3-tiny_10000.weights data/mask_test.jpg
```

# Reference

- [darknet](https://github.com/pjreddie/darknet)



