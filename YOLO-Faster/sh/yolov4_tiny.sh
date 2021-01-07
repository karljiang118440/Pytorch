  
#1. yolov3-tiny 


##1.1. 



export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-10.0/lib64
export PATH=$PATH:/usr/local/cuda-10.0/bin
export CUDA_HOME=$CUDA_HOME:/usr/local/cuda-10.0


export DIR=/media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/backup/yolov4-tiny/coco/20210106


./darknet partial ${DIR}/yolov4-tiny.cfg ${DIR}/yolov4-tiny.weights ${DIR}/yolov4-tiny.conv.15 15



./darknet detector train data/coco.data ${DIR}/yolov4-tiny.cfg ${DIR}/yolov4-tiny.conv.29



export DIR=/media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/backup/yolov4-tiny/voc/20210106

./darknet detector train data/voc.data ${DIR}/yolov4-tiny.cfg ${DIR}/yolov4-tiny.conv.29



./darknet detector  test ./data/voc.data  ${DIR}/yolov4-tiny.cfg  ${DIR}/yolov4-tiny_60000.weights  data/dog.jpg  -thresh 0.55



./darknet detector test \
/media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/data/voc.data  \
/media/jcq/Soft/Pytorch/YOLO/pytorch-YOLOv4/cfg/yolov4.cfg \
/media/jcq/Soft/Pytorch/YOLO/pytorch-YOLOv4/download/yolov4.weights data/dog.jpg -i 0 -thresh 0.25