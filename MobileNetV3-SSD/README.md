# MobileNetV3-SSD
MobileNetV3-SSD implementation in PyTorch 

**目的**
Object Detection 
应用于目标检测

环境 

操作系统: Ubuntu18.04

Python: 3.6

PyTorch: 1.1.0


**使用MobileNetV3-SSD实现目标检测**

**Support Export ONNX**

代码参考（严重参考以下代码）


**一 SSD部分**


[A PyTorch Implementation of Single Shot MultiBox Detector ](https://github.com/amdegroot/ssd.pytorch)

**二 MobileNetV3 部分**



[1 mobilenetv3 with pytorch，provide pre-train model](https://github.com/xiaolai-sqlai/mobilenetv3) 


[2 MobileNetV3 in pytorch and ImageNet pretrained models ](https://github.com/kuan-wang/pytorch-mobilenet-v3)


[3Implementing Searching for MobileNetV3 paper using Pytorch ](https://github.com/leaderj1001/MobileNetV3-Pytorch)


[4 MobileNetV1, MobileNetV2, VGG based SSD/SSD-lite implementation in Pytorch 1.0 / Pytorch 0.4. Out-of-box support for retraining on Open Images dataset. ONNX and Caffe2 support. Experiment Ideas like CoordConv. 
no discernible latency cost](https://github.com/qfgaohao/pytorch-ssd).


针对4我这里没有做MobileNetV1, MobileNetV2等等代码兼容，只有MobileNetV3可用

**下载数据**
本例是以蛋糕和面包为例，原因是数据量小
所有类别总大小是561G，蛋糕和面包是3.2G

python3 open_images_downloader.py --root /media/santiago/a/data/open_images --class_names "Cake,Bread" --num_workers 20

修改为：

python open_images_downloader.py --root /media/jcq/Doc/DL_data/open_images --class_names "Cake,Bread" --num_workers 20


**训练过程**

**首次训练**

/home/jcq/.conda/envs/PyTorch/bin/python train_ssd.py --dataset_type open_images --datasets /media/jcq/Doc/DL_data/open_images --net mb3-ssd-lite  --scheduler cosine --lr 0.01 --t_max 100 --validation_epochs 5 --num_epochs 100 --base_net_lr 0.001  --batch_size 16


**预加载之前训练的模型**

/home/jcq/.conda/envs/PyTorch/bin/python train_ssd.py --dataset_type open_images --datasets /media/santiago/data/open_images --net mb3-ssd-lite --pretrained_ssd models/mb3-ssd-lite-Epoch-99-Loss-2.5194434596402613.pth  --scheduler cosine --lr 0.01 --t_max 100 --validation_epochs 5 --num_epochs 200 --base_net_lr 0.001  --batch_size 5




**测试一张图片**

/home/jcq/.conda/envs/PyTorch/bin/python run_ssd_example.py mb3-ssd-lite models/mb3-ssd-lite-Epoch-99-Loss-2.5194434596402613.pth models/open-images-model-labels.txt /test/test.jpg

/home/jcq/.conda/envs/PyTorch/bin/python run_ssd_example.py mb3-ssd-lite models/mb3-ssd-lite-Epoch-149-Loss-5.782852862012213.pth models/open-images-model-labels.txt /test/test.jpg

/home/jcq/.conda/envs/PyTorch/bin/python run_ssd_example.py mb3-ssd-lite models/mb3-ssd-lite-Epoch-100-Loss-2.546770755521852.pth models/open-images-model-labels.txt test.jpg

/home/jcq/.conda/envs/PyTorch/bin/python run_ssd_example.py mb3-ssd-lite models/mb3-ssd-lite-Epoch-100-Loss-2.546770755521852.pth models/open-images-model-labels.txt /test/test.jpg

**视频检测**

/home/jcq/.conda/envs/PyTorch/bin/python run_ssd_live_demo.py mb3-ssd-lite models/mb3-ssd-lite-Epoch-99-Loss-2.5194434596402613.pth models/open-images-model-labels.txt


**Cake and Bread Pretrained model**


链接: https://pan.baidu.com/s/1byY1eJk3Hm3CTp-29KirxA 

提取码: qxwv 

**VOC Dataset Pretrained model**

链接: https://pan.baidu.com/s/1yt_IRY0RcgSxB-YwywoHuA 

提取码: 2sta 




**prune_alexnet.py** added by self

如何对模型进行压缩：


/home/jcq/.conda/envs/PyTorch/bin/python train_ssd.py --dataset_type open_images --datasets /media/jcq/Doc/DL_data/open_images --net mb3-ssd-lite  --scheduler cosine --lr 0.01 --t_max 100 --validation_epochs 5 --num_epochs 100 --base_net_lr 0.001  --batch_size 16


/home/jcq/.conda/envs/PyTorch/bin/python prune_alexnet.py --trained_model ./models/mb3-ssd-lite-Epoch-50-Loss-2.854336971821992.pth --dataset /media/jcq/Doc/DL_data/open_images --validation_dataset /media/jcq/Doc/DL_data/open_images --prune_conv



# 对车辆或者行人进行检测

**下载数据**

python open_images_downloader.py --root ./open_images --class_names "Car,Person" --num_workers 20


**首次训练**

/home/jcq/.conda/envs/PyTorch/bin/python train_ssd.py --dataset_type open_images --datasets ./open_images --net mb3-ssd-lite  --scheduler cosine --lr 0.01 --t_max 100 --validation_epochs 3 --num_epochs 50 --base_net_lr 0.001  --batch_size 16


**测试一张图片**

/home/jcq/.conda/envs/PyTorch/bin/python run_ssd_example.py mb3-ssd-lite models/mb3-ssd-lite-Epoch-0-Loss-3.882783318864237.pth models/open-images-model-labels.txt test.jpg