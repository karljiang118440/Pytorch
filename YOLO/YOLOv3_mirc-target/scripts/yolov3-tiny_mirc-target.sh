  
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


2021.02.22 > : it seems no any results,but why?


>: 2021.02.22:修改 cfg ，保证效果

./darknet partial ${CFG_DIR}/yolov3-voc-train.cfg ${WEIGHTS_DIR}/yolov3.weights ${CFG_DIR}/darknet53.conv.74 74


./darknet detector train \
/media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/YOLOv3-mirc-target/data/voc.data  \
${CFG_DIR}/yolov3-voc-train.cfg  \
${CFG_DIR}/darknet53.conv.74













./darknet detector train \
 /media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/YOLOv3-mirc-target/data/voc.data  \
/${CFG_DIR}/yolov3-spp-voc-train.cfg  \
 ${WEIGHTS_DIR}/darknet53.conv.74





##1.2、


./darknet partial /media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/backup/yolov3-tiny/voc-20210105/cfg/yolov3-tiny.cfg \
 /media/jcq/Backup/DL_models/YOLO/yolov3-tiny.weights \
 /media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/backup/yolov3-tiny/voc-20210105/cfg/yolov3-tiny.conv.15 15



./darknet detector train data/voc.data /media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/backup/yolov3-tiny/voc-20210105/cfg/yolov3-tiny.cfg /media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/backup/yolov3-tiny/voc-20210105/cfg/yolov3-tiny.conv.15


重新进行训练，加大次数



./darknet partial /media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/backup/yolov3-tiny/voc-20210105/cfg/yolov3-tiny.cfg \
 /media/jcq/Backup/DL_models/YOLO/yolov3-tiny.weights \
 /media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/backup/yolov3-tiny/voc-20210105/cfg/yolov3-tiny.conv.15 15



./darknet detector train data/voc.data \
/media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/backup/yolov3-tiny/voc-20210105/cfg/yolov3-tiny.cfg \
/media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/backup/yolov3-tiny/voc-20210105/cfg/yolov3-tiny.conv.15



#1.3、测试图像


export DIR=/media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/backup/yolov3-tiny/voc-20210105

./darknet detector  test ./data/voc.data  ${DIR}/yolov4-tiny.cfg  ${DIR}/yolov4-tiny_60000.weights  data/dog.jpg  -thresh 0.55



./darknet detector  test data/voc.data \
/media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/backup/yolov3-tiny/voc-20210105/cfg/yolov3-tiny-test.cfg \
/media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/backup/yolov3-tiny/voc-20210105/yolov3-tiny_100000.weights\
 data/dog.jpg  -thresh 0.55


替换 weights :

./darknet detector  test data/voc.data \
 /media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/backup/yolov3-tiny/voc-20210105/cfg/yolov3-tiny.cfg \
 /media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/backup/yolov3-tiny/voc-20210105/yolov3-tiny_100000.weights\
 data/dog.jpg  -thresh 0.55

 /media/jcq/Backup/DL_models/YOLO/yolov3-tiny.weights  \
 data/dog.jpg  -thresh 0.55

 结论：（还是没有任何检测结果）


 替换 cfg :


./darknet detector  test data/voc.data \
 /media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/build/darknet/x64/cfg/yolov3-tiny.cfg \
 /media/jcq/Backup/DL_models/YOLO/yolov3-tiny.weights  data/dog.jpg  -thresh 0.55

 结论：（还是没有任何检测结果）


 方法2：

