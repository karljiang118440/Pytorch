  
# 1. yolov3-tiny PRN module 

> 添加 prn 模块


## 1.1. envroment



export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-10.0/lib64
export PATH=$PATH:/usr/local/cuda-10.0/bin
export CUDA_HOME=$CUDA_HOME:/usr/local/cuda-10.0

export WEIGHTS_DIR=/media/jcq/Soft/Pytorch/YOLO/PyTorch_YOLOv3/weights

export CFG_DIR=/media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/YOLOv3-mirc-target/cfg/voc/PRN



## 1.2. train


### 1.2.1 、生成文件

./darknet partial  \
${CFG_DIR}/yolov3-tiny-prn.cfg \
/media/jcq/Backup/DL_models/YOLO/yolov3-tiny.weights \
${CFG_DIR}/yolov3-tiny.conv.15 15



./darknet detector train \
 /media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/YOLOv3-mirc-target/data/voc.data  \
${CFG_DIR}/yolov3-tiny-prn.cfg  \
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
${CFG_DIR}/yolov3-tiny-prn.cfg  \
${CFG_DIR}/yolov3-tiny.conv.15   \
/media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/YOLOv3-mirc-target/backup/PRN/yolov3-tiny-prn.backup

