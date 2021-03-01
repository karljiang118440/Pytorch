  
# 1. yolov3-tiny Anchors module 


## 1.1. envroment



export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-10.0/lib64
export PATH=$PATH:/usr/local/cuda-10.0/bin
export CUDA_HOME=$CUDA_HOME:/usr/local/cuda-10.0

export WEIGHTS_DIR=/media/jcq/Backup/DL_models/YOLO

export CFG_DIR=/media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/YOLOv3-mirc-target/cfg/voc/Anchor



## 1.2. train


### 1.2.1 、生成文件

./darknet partial  \
${CFG_DIR}/yolov3-tiny-6a.cfg \
${WEIGHTS_DIR}/yolov3-tiny.weights \
${CFG_DIR}/yolov3-tiny.conv.15 15



./darknet detector train \
 /media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/YOLOv3-mirc-target/data/voc.data  \
${CFG_DIR}/yolov3-tiny-6a.cfg  \
${CFG_DIR}/yolov3-tiny.conv.15




# 1.3、测试图像

./darknet detector  test \
/media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/YOLOv3-mirc-target/data/voc.data  \
${CFG_DIR}/yolov3-tiny-6a.cfg  \
/media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/YOLOv3-mirc-target/backup/Anchors/Anchors-6/yolov3-tiny-6a_50000.weights \
/media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/data/dog.jpg  -thresh 0.55



### 1.3.1 ：anchors = 37,35,  181,175,  48,90,  94,128,  13,25,  21,63

Loading weights from /media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/YOLOv3-mirc-target/backup/Anchors/Anchors-6/yolov3-tiny-6a_60000.weights...Done!
/media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/data/dog.jpg: Predicted in 0.003171 seconds.
dog: 76%
car: 64%




### 1.3.2 ：anchors = 93,132,  216,176,  321,335,  27,45,  45,103,  124,272

Loading weights from /media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/YOLOv3-mirc-target/backup/Anchors/Anchors-6/yolov3-tiny-6a_60000.weights...Done!
/media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/data/dog.jpg: Predicted in 0.003163 seconds.

并没有任何检测结果出来，除非是降低阈值才有检测结果





# 1.4、断点续训

./darknet detector train \
 /media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/YOLOv3-mirc-target/data/voc.data  \
${CFG_DIR}/yolov3-tiny-6a.cfg  \
/media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/YOLOv3-mirc-target/backup/Anchors/Anchors-6/yolov3-tiny-6a.backup



# 2 . Anchors = 3


### 2.2.1 、生成文件

./darknet partial  \
${CFG_DIR}/yolov3-tiny-3a.cfg \
${WEIGHTS_DIR}/yolov3-tiny.weights \
${CFG_DIR}/yolov3-tiny.conv.15 15



./darknet detector train \
 /media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/YOLOv3-mirc-target/data/voc.data  \
${CFG_DIR}/yolov3-tiny-3a.cfg  \
${CFG_DIR}/yolov3-tiny.conv.15
