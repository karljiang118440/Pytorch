  
#1. yolov3-tiny 


##1.1. 



export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-10.0/lib64
export PATH=$PATH:/usr/local/cuda-10.0/bin
export CUDA_HOME=$CUDA_HOME:/usr/local/cuda-10.0


./darknet partial /media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/build/darknet/x64/cfg/yolov3-tiny.cfg /media/jcq/Backup/DL_models/YOLO/yolov3-tiny.weights yolov3-tiny.conv.15 15



./darknet detector train data/voc.data /media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/build/darknet/x64/cfg/yolov3-tiny.cfg yolov3-tiny.conv.15



