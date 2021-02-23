  
#1. yolov3 


##1.1. envroment



export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-10.0/lib64
export PATH=$PATH:/usr/local/cuda-10.0/bin
export CUDA_HOME=$CUDA_HOME:/usr/local/cuda-10.0

export WEIGHTS_DIR=/media/jcq/Soft/Pytorch/YOLO/PyTorch_YOLOv3/weights

export CFG_DIR=/media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/YOLOv3-mirc-target/cfg/voc



##1.2. train


./darknet partial ${CFG_DIR}/yolov3-voc-train.cfg ${WEIGHTS_DIR}/yolov3.weights darknet53.conv.74 74




./darknet detector train \
 /media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/YOLOv3-mirc-target/data/voc.data  \
/${CFG_DIR}/yolov3-voc-train.cfg  \
 ${WEIGHTS_DIR}/darknet53.conv.74



>: 2021.02.22:修改 cfg ，保证效果

./darknet partial ${CFG_DIR}/yolov3-voc-train.cfg ${WEIGHTS_DIR}/yolov3.weights ${CFG_DIR}/darknet53.conv.74 74


./darknet detector train \
/media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/YOLOv3-mirc-target/data/voc.data  \
${CFG_DIR}/yolov3-voc-train.cfg  \
${CFG_DIR}/darknet53.conv.74



#1.3、测试图像

./darknet detector  test \
/media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/YOLOv3-mirc-target/data/voc.data  \
${CFG_DIR}/yolov3-voc-train.cfg  \
/media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/YOLOv3-mirc-target/backup/yolov3/yolov3-voc-train_40000.weights \
/media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/data/dog.jpg  -thresh 0.55

>20210222:效果一般













#2. yolov3-spp 


##2.1. envroment



export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-10.0/lib64
export PATH=$PATH:/usr/local/cuda-10.0/bin
export CUDA_HOME=$CUDA_HOME:/usr/local/cuda-10.0

export WEIGHTS_DIR=/media/jcq/Soft/Pytorch/YOLO/PyTorch_YOLOv3/weights

export CFG_DIR=/media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/YOLOv3-mirc-target/cfg/voc



##2.2. train


./darknet partial ${CFG_DIR}/yolov3-spp-voc.cfg ${WEIGHTS_DIR}/yolov3.weights \
${CFG_DIR}/darknet53.conv.74 74




./darknet detector train \
 /media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/YOLOv3-mirc-target/data/voc.data  \
${CFG_DIR}/yolov3-spp-voc.cfg  \
${CFG_DIR}/darknet53.conv.74




>: 2021.02.23

目前看来这个更惨，直接全部nan ,不知道到底为何






#2.3、测试图像

./darknet detector  test \
/media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/YOLOv3-mirc-target/data/voc.data  \
${CFG_DIR}/yolov3-voc-train.cfg  \
/media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/YOLOv3-mirc-target/backup/yolov3/yolov3-voc-train_40000.weights \
/media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/data/dog.jpg  -thresh 0.55

