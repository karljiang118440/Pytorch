3. Darknet2ONNX
This script is to convert the official pretrained darknet model into ONNX

Pytorch version Recommended:

Pytorch 1.4.0 for TensorRT 7.0 and higher
Pytorch 1.5.0 and 1.6.0 for TensorRT 7.1.2 and higher
Install onnxruntime

pip install onnxruntime
Run python script to generate ONNX model and run the demo

python demo_darknet2onnx.py <cfgFile> <weightFile> <imageFile> <batchSize>

python demo_darknet2onnx.py cfg/yolo-fastest.cfg data/yolo-fastest_160000.weights data/dog.jpg 1


