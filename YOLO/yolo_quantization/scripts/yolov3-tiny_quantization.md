  
#1. yolov3-tiny 


##1.1. 



export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-10.0/lib64
export PATH=$PATH:/usr/local/cuda-10.0/bin
export CUDA_HOME=$CUDA_HOME:/usr/local/cuda-10.0




./darknet partial /media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/build/darknet/x64/cfg/yolov3-tiny.cfg /media/jcq/Backup/DL_models/YOLO/yolov3-tiny.weights yolov3-tiny.conv.15 15


./darknet partial \
/media/jcq/Soft/Pytorch/YOLO/YOLO_quantiztion/yolo_quantization/cfg/yolov3_tiny_quant_channelwise-train.cfg \
/media/jcq/Soft/Pytorch/YOLO/YOLO_quantiztion/yolo_quantization/cfg/yolov3_tiny_quant_channelwise.weights \
/media/jcq/Soft/Pytorch/YOLO/YOLO_quantiztion/yolo_quantization/cfg/yolov3-tiny.conv.15 15


./darknet detector train /media/jcq/Soft/Pytorch/YOLO/YOLO_quantiztion/yolo_quantization/cfg/voc.data \
/media/jcq/Soft/Pytorch/YOLO/YOLO_quantiztion/yolo_quantization/cfg/yolov3_tiny_quant_channelwise-train.cfg \
/media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/backup/yolov3-tiny/voc-20210105/cfg/yolov3-tiny.conv.15





./darknet detector train cfg/voc.data cfg/yolov3-tiny.cfg backup/yolov3-tiny.backup




##1.2、、测试图像


./darknet detector  test  data/voc.data \
/media/jcq/Soft/Pytorch/YOLO/YOLO_quantiztion/yolo_quantization/cfg/yolov3_tiny_quant_channelwise-test.cfg \
/media/jcq/Soft/Pytorch/YOLO/YOLO_quantiztion/yolo_quantization/backup/yolov3_tiny_quant_channelwise-train_190000.weights \
 data/dog.jpg  -thresh 0.55



Loading weights from /media/jcq/Soft/Pytorch/YOLO/YOLO_quantiztion/yolo_quantization/backup/yolov3_tiny_quant_channelwise-train_190000.weights...Done!
data/dog.jpg: Predicted in 0.009963 seconds.
dog: 92%
bicycle: 85%

> : 怎么时间相比 yolov3-tiny 相比还变长了呢，是由于没有其他配件吗？




##1.3、断点续训

 ./darknet detector train /media/jcq/Soft/Pytorch/YOLO/YOLO_quantiztion/yolo_quantization/cfg/voc.data \
/media/jcq/Soft/Pytorch/YOLO/YOLO_quantiztion/yolo_quantization/cfg/yolov3_tiny_quant_channelwise-train.cfg \
/media/jcq/Soft/Pytorch/YOLO/Yolo-Fastest/backup/yolov3-tiny/voc-20210105/cfg/yolov3-tiny.conv.15





./darknet detector train cfg/voc.data cfg/yolov3-tiny.cfg backup/yolov3-tiny.backup


