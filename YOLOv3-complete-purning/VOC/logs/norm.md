(pytorch) 
# jcq @ jcq-linux in /media/jcq/Soft/Pytorch/Model_optimazition/YOLOv3-complete-pruning-voc on git:master x [17:40:10] 
$ python3 train.py --data cfg/voc.data --batch-size 8 --accumulate 1 --weights /media/jcq/DATA/DL_models/YOLO/yolov3.weights --cfg cfg/yolov3-voc.cfg

Namespace(accumulate=1, adam=False, arc='default', batch_size=8, bucket='', cache_images=False, cfg='cfg/yolov3-voc.cfg', data='cfg/voc.data', device='', epochs=91, evolve=False, img_size=416, img_weights=False, multi_scale=False, name='', nosave=False, notest=False, prebias=False, prune=0, rect=False, resume=False, s=0.001, sr=False, transfer=False, var=None, weights='/media/jcq/DATA/DL_models/YOLO/yolov3.weights')
Using CUDA device0 _CudaDeviceProperties(name='GeForce RTX 2070', total_memory=7949MB)

single-gpu sparse
normal sparse training
Reading labels (2501 found, 0 missing, 0 empty for 2501 images): 100%|████████████████████████████████████████████████████████████████████████████████████████████████| 2501/2501 [00:00<00:00, 5793.07it/s]
Model Summary: 222 layers, 6.1626e+07 parameters, 6.1626e+07 gradients
Starting training for 91 epochs...

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
  0%|                                                                                                                                                                               | 0/313 [00:00<?, ?it/s]/media/jcq/Soft/Pytorch/Model_optimazition/YOLOv3-complete-pruning-voc/utils/utils.py:813: MatplotlibDeprecationWarning: Passing non-integers as three-element position specification is deprecated since 3.3 and will be removed two minor releases later.
  plt.subplot(ns, ns, i + 1).imshow(imgs[i].transpose(1, 2, 0))
/media/jcq/Soft/Pytorch/Model_optimazition/YOLOv3-complete-pruning-voc/utils/utils.py:813: MatplotlibDeprecationWarning: Passing non-integers as three-element position specification is deprecated since 3.3 and will be removed two minor releases later.
  plt.subplot(ns, ns, i + 1).imshow(imgs[i].transpose(1, 2, 0))
/media/jcq/Soft/Pytorch/Model_optimazition/YOLOv3-complete-pruning-voc/utils/utils.py:813: MatplotlibDeprecationWarning: Passing non-integers as three-element position specification is deprecated since 3.3 and will be removed two minor releases later.
  plt.subplot(ns, ns, i + 1).imshow(imgs[i].transpose(1, 2, 0))
/media/jcq/Soft/Pytorch/Model_optimazition/YOLOv3-complete-pruning-voc/utils/utils.py:813: MatplotlibDeprecationWarning: Passing non-integers as three-element position specification is deprecated since 3.3 and will be removed two minor releases later.
  plt.subplot(ns, ns, i + 1).imshow(imgs[i].transpose(1, 2, 0))
/media/jcq/Soft/Pytorch/Model_optimazition/YOLOv3-complete-pruning-voc/utils/utils.py:813: MatplotlibDeprecationWarning: Passing non-integers as three-element position specification is deprecated since 3.3 and will be removed two minor releases later.
  plt.subplot(ns, ns, i + 1).imshow(imgs[i].transpose(1, 2, 0))
/media/jcq/Soft/Pytorch/Model_optimazition/YOLOv3-complete-pruning-voc/utils/utils.py:813: MatplotlibDeprecationWarning: Passing non-integers as three-element position specification is deprecated since 3.3 and will be removed two minor releases later.
  plt.subplot(ns, ns, i + 1).imshow(imgs[i].transpose(1, 2, 0))
/media/jcq/Soft/Pytorch/Model_optimazition/YOLOv3-complete-pruning-voc/utils/utils.py:813: MatplotlibDeprecationWarning: Passing non-integers as three-element position specification is deprecated since 3.3 and will be removed two minor releases later.
  plt.subplot(ns, ns, i + 1).imshow(imgs[i].transpose(1, 2, 0))
/media/jcq/Soft/Pytorch/Model_optimazition/YOLOv3-complete-pruning-voc/utils/utils.py:813: MatplotlibDeprecationWarning: Passing non-integers as three-element position specification is deprecated since 3.3 and will be removed two minor releases later.
  plt.subplot(ns, ns, i + 1).imshow(imgs[i].transpose(1, 2, 0))
      0/90     4.23G      2.24      1.14       6.7      10.1        31       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:03<00:00,  2.53it/s]
Reading image shapes: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2510/2510 [00:02<00:00, 1162.52it/s]
               Class    Images   Targets         P         R       mAP        F1:   0%|                                                                                             | 0/314 [00:00<?, ?it/s]/media/jcq/Soft/Pytorch/Model_optimazition/YOLOv3-complete-pruning-voc/utils/utils.py:813: MatplotlibDeprecationWarning: Passing non-integers as three-element position specification is deprecated since 3.3 and will be removed two minor releases later.
  plt.subplot(ns, ns, i + 1).imshow(imgs[i].transpose(1, 2, 0))
/media/jcq/Soft/Pytorch/Model_optimazition/YOLOv3-complete-pruning-voc/utils/utils.py:813: MatplotlibDeprecationWarning: Passing non-integers as three-element position specification is deprecated since 3.3 and will be removed two minor releases later.
  plt.subplot(ns, ns, i + 1).imshow(imgs[i].transpose(1, 2, 0))
/media/jcq/Soft/Pytorch/Model_optimazition/YOLOv3-complete-pruning-voc/utils/utils.py:813: MatplotlibDeprecationWarning: Passing non-integers as three-element position specification is deprecated since 3.3 and will be removed two minor releases later.
  plt.subplot(ns, ns, i + 1).imshow(imgs[i].transpose(1, 2, 0))
/media/jcq/Soft/Pytorch/Model_optimazition/YOLOv3-complete-pruning-voc/utils/utils.py:813: MatplotlibDeprecationWarning: Passing non-integers as three-element position specification is deprecated since 3.3 and will be removed two minor releases later.
  plt.subplot(ns, ns, i + 1).imshow(imgs[i].transpose(1, 2, 0))
/media/jcq/Soft/Pytorch/Model_optimazition/YOLOv3-complete-pruning-voc/utils/utils.py:813: MatplotlibDeprecationWarning: Passing non-integers as three-element position specification is deprecated since 3.3 and will be removed two minor releases later.
  plt.subplot(ns, ns, i + 1).imshow(imgs[i].transpose(1, 2, 0))
/media/jcq/Soft/Pytorch/Model_optimazition/YOLOv3-complete-pruning-voc/utils/utils.py:813: MatplotlibDeprecationWarning: Passing non-integers as three-element position specification is deprecated since 3.3 and will be removed two minor releases later.
  plt.subplot(ns, ns, i + 1).imshow(imgs[i].transpose(1, 2, 0))
/media/jcq/Soft/Pytorch/Model_optimazition/YOLOv3-complete-pruning-voc/utils/utils.py:813: MatplotlibDeprecationWarning: Passing non-integers as three-element position specification is deprecated since 3.3 and will be removed two minor releases later.
  plt.subplot(ns, ns, i + 1).imshow(imgs[i].transpose(1, 2, 0))
/media/jcq/Soft/Pytorch/Model_optimazition/YOLOv3-complete-pruning-voc/utils/utils.py:813: MatplotlibDeprecationWarning: Passing non-integers as three-element position specification is deprecated since 3.3 and will be removed two minor releases later.
  plt.subplot(ns, ns, i + 1).imshow(imgs[i].transpose(1, 2, 0))
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:37<00:00,  8.30it/s]
                 all  2.51e+03  6.31e+03     0.425     0.643     0.455     0.493

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
      1/90     4.23G      1.87     0.921      4.16      6.95        25       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:36<00:00,  8.69it/s]
                 all  2.51e+03  6.31e+03     0.462     0.693     0.539     0.542

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
      2/90     4.23G      1.73     0.917      4.17      6.81        25       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.83it/s]
                 all  2.51e+03  6.31e+03     0.488     0.668     0.532     0.554

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
      3/90     4.23G      1.64     0.883      3.47      5.99        28       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:36<00:00,  8.71it/s]
                 all  2.51e+03  6.31e+03     0.488     0.703     0.554     0.563

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
      4/90     4.23G      1.65     0.874      3.52      6.04        17       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.80it/s]
                 all  2.51e+03  6.31e+03     0.508     0.695     0.553     0.577

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
      5/90     4.23G      1.61     0.841      2.93      5.39        22       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.79it/s]
                 all  2.51e+03  6.31e+03     0.484     0.729     0.584     0.576

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
      6/90     4.23G       1.6     0.816      2.82      5.24        24       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.83it/s]
                 all  2.51e+03  6.31e+03     0.525     0.684     0.549     0.586

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
      7/90     4.23G      1.53     0.827      2.72      5.08        20       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.84it/s]
                 all  2.51e+03  6.31e+03      0.53     0.725     0.593     0.608

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
      8/90     4.23G      1.56     0.817      2.95      5.33        25       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:36<00:00,  8.72it/s]
                 all  2.51e+03  6.31e+03     0.469     0.666     0.521     0.539

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
      9/90     4.23G      1.56     0.831      2.83      5.22        30       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.80it/s]
                 all  2.51e+03  6.31e+03     0.533     0.678     0.563     0.575

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     10/90     4.23G      1.51     0.819      2.76      5.09        25       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.78it/s]
                 all  2.51e+03  6.31e+03     0.519     0.713      0.59     0.594

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     11/90     4.23G      1.49     0.811      3.05      5.36        26       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:36<00:00,  8.72it/s]
                 all  2.51e+03  6.31e+03     0.477     0.675     0.529     0.547

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     12/90     4.23G       1.5     0.828      2.97       5.3        19       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.74it/s]
                 all  2.51e+03  6.31e+03     0.479     0.665     0.536      0.54

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     13/90     4.23G      1.52     0.821      2.67      5.01        23       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.81it/s]
                 all  2.51e+03  6.31e+03     0.497     0.672     0.551     0.565

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     14/90     4.23G      1.47     0.835      2.91      5.22        28       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.87it/s]
                 all  2.51e+03  6.31e+03     0.516     0.669     0.545     0.574

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     15/90     4.23G      1.45     0.793      2.43      4.68        30       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.74it/s]
                 all  2.51e+03  6.31e+03     0.505     0.692     0.561     0.576

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     16/90     4.23G      1.47     0.807      2.69      4.96        18       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.86it/s]
                 all  2.51e+03  6.31e+03     0.513     0.655     0.528     0.562

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     17/90     4.23G      1.45     0.802      2.51      4.77        21       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.85it/s]
                 all  2.51e+03  6.31e+03     0.538     0.673     0.571     0.593

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     18/90     4.23G      1.49     0.791      2.89      5.17        25       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.82it/s]
                 all  2.51e+03  6.31e+03     0.532      0.69     0.568     0.593

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     19/90     4.23G      1.43     0.805      2.52      4.76        22       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.86it/s]
                 all  2.51e+03  6.31e+03     0.536     0.678     0.562     0.591

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     20/90     4.23G      1.46     0.777      2.32      4.55        23       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.80it/s]
                 all  2.51e+03  6.31e+03     0.527     0.674     0.563     0.588

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     21/90     4.23G      1.44     0.783      2.52      4.74        27       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.76it/s]
                 all  2.51e+03  6.31e+03     0.498     0.683      0.56     0.572

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     22/90     4.23G       1.5     0.793      2.52      4.81        22       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.81it/s]
                 all  2.51e+03  6.31e+03     0.496     0.666     0.534     0.559

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     23/90     4.23G      1.41     0.818      2.64      4.87        15       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.75it/s]
                 all  2.51e+03  6.31e+03     0.501     0.678     0.558     0.565

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     24/90     4.23G       1.4     0.807      2.39       4.6        27       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.76it/s]
                 all  2.51e+03  6.31e+03     0.526     0.678     0.556     0.588

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     25/90     4.23G      1.42     0.773      2.24      4.43        19       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.76it/s]
                 all  2.51e+03  6.31e+03     0.527     0.674      0.55     0.582

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     26/90     4.23G      1.41     0.771      2.29      4.48        19       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.78it/s]
                 all  2.51e+03  6.31e+03     0.535     0.672     0.567     0.589

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     27/90     4.23G      1.39     0.763      2.14      4.29        26       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:36<00:00,  8.67it/s]
                 all  2.51e+03  6.31e+03     0.491     0.682     0.557     0.559

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     28/90     4.23G      1.38     0.749      2.22      4.35        29       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.82it/s]
                 all  2.51e+03  6.31e+03     0.518     0.681     0.561     0.583

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     29/90     4.23G      1.41     0.806      2.48       4.7        13       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.82it/s]
                 all  2.51e+03  6.31e+03     0.495     0.662     0.547     0.557

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     30/90     4.23G      1.43     0.774      2.31      4.51        24       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.80it/s]
                 all  2.51e+03  6.31e+03     0.451     0.638     0.507     0.522

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     31/90     4.23G      1.41     0.797       2.6      4.81        19       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.83it/s]
                 all  2.51e+03  6.31e+03     0.494     0.669     0.555     0.563

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     32/90     4.23G       1.4     0.776      2.27      4.45        24       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.79it/s]
                 all  2.51e+03  6.31e+03     0.515     0.662     0.539      0.57

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     33/90     4.23G      1.38     0.755      2.28      4.41        24       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.81it/s]
                 all  2.51e+03  6.31e+03     0.533     0.668     0.553     0.584

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     34/90     4.23G      1.41      0.76      2.14       4.3        28       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.86it/s]
                 all  2.51e+03  6.31e+03     0.515     0.679     0.564     0.579

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     35/90     4.23G      1.37     0.767      2.26       4.4        13       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.81it/s]
                 all  2.51e+03  6.31e+03     0.485     0.636     0.498     0.534

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     36/90     4.23G      1.38     0.777      2.58      4.74        20       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.84it/s]
                 all  2.51e+03  6.31e+03     0.504     0.648     0.528     0.562

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     37/90     4.23G      1.35     0.771      2.13      4.26        19       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.84it/s]
                 all  2.51e+03  6.31e+03     0.518     0.651     0.547      0.57

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     38/90     4.23G      1.41     0.757      2.19      4.35        21       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.85it/s]
                 all  2.51e+03  6.31e+03     0.513     0.645     0.524     0.561

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     39/90     4.23G       1.4     0.799      2.51      4.71        34       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.86it/s]
                 all  2.51e+03  6.31e+03     0.494     0.634     0.516      0.55

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     40/90     4.23G      1.43     0.822         3      5.25        26       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.81it/s]
                 all  2.51e+03  6.31e+03     0.445     0.606     0.488     0.504

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     41/90     4.23G      1.46      0.82      2.66      4.94        26       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.74it/s]
                 all  2.51e+03  6.31e+03     0.468     0.642     0.506     0.535

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     42/90     4.23G      1.41     0.793      2.48      4.69        19       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.75it/s]
                 all  2.51e+03  6.31e+03     0.481     0.653     0.525     0.547

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     43/90     4.23G       1.4     0.809      2.44      4.65        24       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.85it/s]
                 all  2.51e+03  6.31e+03     0.465      0.63     0.506      0.53

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     44/90     4.23G       1.4       0.8      2.56      4.75        22       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.85it/s]
                 all  2.51e+03  6.31e+03     0.478     0.639     0.516     0.539

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     45/90     4.23G      1.44     0.844      3.15      5.43        22       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.90it/s]
                 all  2.51e+03  6.31e+03     0.466     0.615     0.497     0.519

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     46/90     4.23G      1.43     0.824      2.87      5.13        16       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.82it/s]
                 all  2.51e+03  6.31e+03     0.477     0.639     0.508     0.534

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     47/90     4.23G      1.41     0.803      2.44      4.65        21       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.87it/s]
                 all  2.51e+03  6.31e+03      0.48     0.651     0.521     0.547

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     48/90     4.23G       1.4     0.783      2.43      4.62        24       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.79it/s]
                 all  2.51e+03  6.31e+03     0.501     0.635     0.524      0.55

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     49/90     4.23G       1.4     0.806       2.5      4.71        30       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.82it/s]
                 all  2.51e+03  6.31e+03     0.481     0.644     0.522     0.545

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     50/90     4.23G      1.41      0.78      2.31       4.5        21       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.89it/s]
                 all  2.51e+03  6.31e+03     0.484     0.613     0.483     0.535

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     51/90     4.23G      1.42     0.829      2.69      4.94        22       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.91it/s]
                 all  2.51e+03  6.31e+03     0.476     0.599     0.472      0.52

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     52/90     4.23G      1.39     0.814      2.57      4.78        32       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.88it/s]
                 all  2.51e+03  6.31e+03       0.5     0.609       0.5     0.537

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     53/90     4.23G      1.41     0.789      2.53      4.73        22       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.90it/s]
                 all  2.51e+03  6.31e+03     0.483     0.613     0.496     0.533

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     54/90     4.23G      1.39     0.804      2.32      4.52        27       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.84it/s]
                 all  2.51e+03  6.31e+03     0.472     0.629     0.519     0.534

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     55/90     4.23G      1.37     0.789      2.26      4.42        27       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.93it/s]
                 all  2.51e+03  6.31e+03     0.518     0.612     0.501     0.549

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     56/90     4.23G      1.38     0.797      2.38      4.56        21       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.91it/s]
                 all  2.51e+03  6.31e+03     0.485     0.613     0.503      0.53

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     57/90     4.23G      1.39     0.817      2.44      4.64        18       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.78it/s]
                 all  2.51e+03  6.31e+03     0.449     0.635     0.506     0.513

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     58/90     4.23G      1.42     0.812      2.51      4.75        27       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.84it/s]
                 all  2.51e+03  6.31e+03     0.458     0.587      0.46     0.504

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     59/90     4.23G      1.45     0.838      2.69      4.98        21       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.84it/s]
                 all  2.51e+03  6.31e+03     0.463     0.613     0.491     0.519

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     60/90     4.23G       1.4     0.798       2.4       4.6        30       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.85it/s]
                 all  2.51e+03  6.31e+03     0.481     0.591     0.471     0.513

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     61/90     4.23G      1.44     0.821      2.78      5.04        23       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.87it/s]
                 all  2.51e+03  6.31e+03     0.453     0.623     0.498     0.518

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     62/90     4.23G      1.44     0.816      2.68      4.93        33       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.86it/s]
                 all  2.51e+03  6.31e+03      0.43     0.581     0.434     0.483

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     63/90     4.23G      1.43     0.842      2.85      5.12        21       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.76it/s]
                 all  2.51e+03  6.31e+03     0.464     0.605     0.478     0.511

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     64/90     4.23G      1.42     0.817      2.47       4.7        25       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.84it/s]
                 all  2.51e+03  6.31e+03     0.488     0.625     0.502      0.54

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     65/90     4.23G      1.42     0.796      2.34      4.56        40       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.87it/s]
                 all  2.51e+03  6.31e+03     0.429     0.558     0.414     0.467

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     66/90     4.23G      1.38     0.805      2.27      4.46        26       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.86it/s]
                 all  2.51e+03  6.31e+03     0.465     0.621     0.488     0.521

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     67/90     4.23G      1.41     0.799      2.41      4.62        28       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.82it/s]
                 all  2.51e+03  6.31e+03     0.448     0.573      0.45     0.492

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     68/90     4.23G      1.42     0.849      2.92      5.19        19       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.79it/s]
                 all  2.51e+03  6.31e+03     0.447     0.616     0.484      0.51

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     69/90     4.23G      1.42     0.806      2.63      4.85        29       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.85it/s]
                 all  2.51e+03  6.31e+03     0.485     0.619     0.502      0.54

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     70/90     4.23G      1.41     0.818      2.53      4.76        19       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.85it/s]
                 all  2.51e+03  6.31e+03      0.45     0.595      0.47     0.503

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     71/90     4.23G      1.39     0.786      2.26      4.44        18       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.76it/s]
                 all  2.51e+03  6.31e+03     0.451     0.592     0.475     0.506

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     72/90     4.23G      1.42     0.862      3.02       5.3        31       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.81it/s]
                 all  2.51e+03  6.31e+03     0.434     0.593     0.461     0.496

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     73/90     4.23G      1.44     0.841      2.65      4.93        31       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.84it/s]
                 all  2.51e+03  6.31e+03     0.465     0.571     0.454       0.5

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     74/90     4.23G      1.25     0.813      2.36      4.41        13       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.88it/s]
                 all  2.51e+03  6.31e+03     0.505     0.634     0.521     0.557

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     75/90     4.23G      1.16     0.762      1.89      3.82        21       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.83it/s]
                 all  2.51e+03  6.31e+03     0.509     0.644     0.531     0.564

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     76/90     4.23G      1.14     0.739       1.8      3.68        32       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.86it/s]
                 all  2.51e+03  6.31e+03     0.532     0.646     0.543     0.581

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     77/90     4.23G      1.11     0.717      1.69      3.52        14       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.89it/s]
                 all  2.51e+03  6.31e+03     0.524     0.649     0.541     0.576

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     78/90     4.23G       1.1     0.714      1.53      3.35        33       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.94it/s]
                 all  2.51e+03  6.31e+03     0.553     0.653     0.551     0.595

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     79/90     4.23G      1.11     0.712      1.53      3.35        22       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.83it/s]
                 all  2.51e+03  6.31e+03     0.528     0.666     0.558     0.586

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     80/90     4.23G       1.1     0.705      1.44      3.25        21       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.87it/s]
                 all  2.51e+03  6.31e+03     0.551     0.664     0.563       0.6

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     81/90     4.23G      1.08     0.713      1.39      3.19        37       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.96it/s]
                 all  2.51e+03  6.31e+03     0.548     0.665     0.562     0.598

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     82/90     4.23G      1.08     0.694       1.4      3.17        22       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.92it/s]
                 all  2.51e+03  6.31e+03     0.555      0.66     0.561       0.6

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     83/90     4.23G      1.04     0.696      1.43      3.17        17       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.90it/s]
                 all  2.51e+03  6.31e+03      0.56     0.661     0.561     0.603

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     84/90     4.23G      1.03      0.68      1.32      3.03        19       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.87it/s]
                 all  2.51e+03  6.31e+03     0.556     0.668     0.567     0.604

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     85/90     4.23G      1.04     0.679       1.3      3.01        21       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.95it/s]
                 all  2.51e+03  6.31e+03     0.564     0.665     0.565     0.608

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     86/90     4.23G      1.04     0.694      1.29      3.02        28       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.89it/s]
                 all  2.51e+03  6.31e+03     0.566     0.667     0.566     0.609

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     87/90     4.23G      1.03     0.701      1.27      3.01        26       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.87it/s]
                 all  2.51e+03  6.31e+03     0.559      0.67     0.569     0.607

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     88/90     4.23G      1.04     0.687      1.36      3.09        20       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.89it/s]
                 all  2.51e+03  6.31e+03     0.566     0.667     0.566      0.61

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     89/90     4.23G      1.03     0.696      1.29      3.02        23       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.90it/s]
                 all  2.51e+03  6.31e+03     0.567     0.671     0.571     0.612

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     90/90     4.23G      1.04     0.688      1.34      3.07        22       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [01:21<00:00,  3.87it/s]
                 all  2.51e+03  6.31e+03    0.0553     0.817      0.61     0.102
91 epochs completed in 4.133 hours.

(pytorch) 
# jcq @ jcq-linux in /media/jcq/Soft/Pytorch/Model_optimazition/YOLOv3-complete-pruning-voc on git:master x [8:43:47] 
$ 


