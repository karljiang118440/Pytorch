  
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
${CFG_DIR}/yolov3-tiny-prn.cfg  \
/media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/YOLOv3-mirc-target/backup/PRN/yolov3-tiny-prn_130000.weights \
/media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/data/dog.jpg  -thresh 0.55

> :明显效果并不理想，虽然速度快一点
Loading weights from /media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/YOLOv3-mirc-target/backup/PRN/yolov3-tiny-prn_130000.weights...Done!
/media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/data/dog.jpg: Predicted in 0.002687 seconds.
car: 98%









# 1.4、断点续训

./darknet detector train \
 /media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/YOLOv3-mirc-target/data/voc.data  \
${CFG_DIR}/yolov3-tiny-6a.cfg  \
/media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/YOLOv3-mirc-target/backup/Anchors/Anchors-6/yolov3-tiny-6a.backup

