(pytorch) 
# jcq @ jcq-linux in /media/jcq/Soft/Pytorch/Model_optimazition/YOLOv3-complete-pruning-voc on git:master x [10:40:19] 
$ python3 train.py --data data/voc.data --batch-size 8 --accumulate 1 --weights /media/jcq/DATA/DL_models/YOLO/yolov3.weights --cfg cfg/yolov3-voc.cfg -sr --s 0.001 --prune 0 
Namespace(accumulate=1, adam=False, arc='default', batch_size=8, bucket='', cache_images=False, cfg='cfg/yolov3-voc.cfg', data='data/voc.data', device='', epochs=91, evolve=False, img_size=416, img_weights=False, multi_scale=False, name='', nosave=False, notest=False, prebias=False, prune=0, rect=False, resume=False, s=0.001, sr=True, transfer=False, var=None, weights='/media/jcq/DATA/DL_models/YOLO/yolov3.weights')
Using CUDA device0 _CudaDeviceProperties(name='GeForce RTX 2070', total_memory=7949MB)

single-gpu sparse
normal sparse training
Reading labels (2501 found, 0 missing, 0 empty for 2501 images): 100%|████████████████████████████████████████████████████████████████████████████████████████████████| 2501/2501 [00:00<00:00, 5831.46it/s]
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
      0/90     4.23G      2.24      1.14      6.65        10        31       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:03<00:00,  2.53it/s]
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
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:37<00:00,  8.48it/s]
                 all  2.51e+03  6.31e+03      0.43     0.682     0.506     0.509

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
      1/90     4.23G      1.85     0.912      3.95      6.72        25       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.52it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.83it/s]
                 all  2.51e+03  6.31e+03     0.491     0.693     0.549     0.566

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
      2/90     4.23G      1.75     0.915      4.11      6.78        25       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.73it/s]
                 all  2.51e+03  6.31e+03     0.481     0.699     0.537     0.562

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
      3/90     4.23G      1.66     0.871      3.37       5.9        28       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.74it/s]
                 all  2.51e+03  6.31e+03     0.529     0.704     0.572     0.592

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
      4/90     4.23G       1.6     0.865      3.57      6.03        17       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.81it/s]
                 all  2.51e+03  6.31e+03      0.51     0.672     0.527     0.569

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
      5/90     4.23G      1.63     0.844      3.02      5.49        22       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.78it/s]
                 all  2.51e+03  6.31e+03     0.505     0.717     0.572     0.586

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
      6/90     4.23G      1.56     0.824      2.99      5.37        24       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.79it/s]
                 all  2.51e+03  6.31e+03     0.498     0.701      0.56     0.572

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
      7/90     4.23G       1.5     0.816      2.67      4.99        20       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.86it/s]
                 all  2.51e+03  6.31e+03     0.541     0.704     0.587     0.604

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
      8/90     4.23G      1.52     0.799      2.83      5.15        25       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.80it/s]
                 all  2.51e+03  6.31e+03     0.509     0.693     0.567     0.574

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
      9/90     4.23G      1.49     0.827       2.8      5.12        30       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.95it/s]
                 all  2.51e+03  6.31e+03     0.556     0.686     0.582     0.604

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     10/90     4.23G      1.47     0.816      2.52       4.8        25       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.84it/s]
                 all  2.51e+03  6.31e+03     0.512     0.706     0.578     0.583

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     11/90     4.23G       1.5     0.854      3.56      5.91        26       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.83it/s]
                 all  2.51e+03  6.31e+03      0.52     0.657     0.539     0.566

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     12/90     4.23G       1.5     0.846       2.9      5.24        19       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.79it/s]
                 all  2.51e+03  6.31e+03     0.501      0.67     0.546     0.567

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     13/90     4.23G      1.49     0.832      2.62      4.94        23       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.88it/s]
                 all  2.51e+03  6.31e+03     0.534     0.683     0.567     0.592

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     14/90     4.23G      1.41     0.843      2.81      5.06        28       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.94it/s]
                 all  2.51e+03  6.31e+03     0.547     0.652     0.539      0.58

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     15/90     4.23G      1.41      0.81      2.61      4.83        30       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.88it/s]
                 all  2.51e+03  6.31e+03      0.54     0.662     0.546     0.588

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     16/90     4.23G      1.43     0.837      2.96      5.22        18       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.82it/s]
                 all  2.51e+03  6.31e+03       0.5      0.65     0.514     0.554

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     17/90     4.23G      1.42      0.85      2.93       5.2        21       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.89it/s]
                 all  2.51e+03  6.31e+03     0.527      0.66      0.55     0.578

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     18/90     4.23G      1.44     0.849      3.33      5.62        25       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.95it/s]
                 all  2.51e+03  6.31e+03     0.544     0.635     0.532     0.573

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     19/90     4.23G      1.42     0.867      3.02      5.31        22       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.86it/s]
                 all  2.51e+03  6.31e+03     0.538     0.634     0.515     0.572

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     20/90     4.23G      1.43     0.835      2.83      5.09        23       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.83it/s]
                 all  2.51e+03  6.31e+03     0.525     0.638     0.529     0.569

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     21/90     4.23G      1.41     0.838      2.81      5.05        27       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.86it/s]
                 all  2.51e+03  6.31e+03     0.522     0.639     0.528     0.569

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     22/90     4.23G      1.45     0.864      3.22      5.53        22       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.88it/s]
                 all  2.51e+03  6.31e+03     0.484     0.633     0.508      0.54

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     23/90     4.23G      1.41     0.896      3.26      5.56        15       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:34<00:00,  9.11it/s]
                 all  2.51e+03  6.31e+03     0.505     0.609     0.483     0.545

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     24/90     4.23G       1.4     0.901      3.13      5.44        27       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:34<00:00,  9.04it/s]
                 all  2.51e+03  6.31e+03     0.492     0.606     0.483     0.536

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     25/90     4.23G      1.44     0.878      3.03      5.35        19       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:34<00:00,  9.00it/s]
                 all  2.51e+03  6.31e+03     0.477     0.561     0.442     0.503

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     26/90     4.23G      1.42     0.898      3.33      5.65        19       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.89it/s]
                 all  2.51e+03  6.31e+03     0.488     0.589     0.476     0.525

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     27/90     4.23G      1.43     0.913      3.49      5.84        26       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.96it/s]
                 all  2.51e+03  6.31e+03     0.442     0.561     0.426     0.482

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     28/90     4.23G      1.43     0.906      3.74      6.07        29       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.92it/s]
                 all  2.51e+03  6.31e+03     0.486     0.588     0.459     0.515

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     29/90     4.23G      1.44     0.938      3.46      5.84        13       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:34<00:00,  8.98it/s]
                 all  2.51e+03  6.31e+03     0.445     0.543     0.415     0.478

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     30/90     4.23G      1.49     0.929       3.5      5.91        24       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:34<00:00,  8.99it/s]
                 all  2.51e+03  6.31e+03      0.46     0.546     0.426     0.489

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     31/90     4.23G      1.47     0.941      3.61      6.02        19       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:34<00:00,  9.06it/s]
                 all  2.51e+03  6.31e+03     0.492     0.577     0.448      0.51

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     32/90     4.23G      1.49     0.957      3.96       6.4        24       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:34<00:00,  9.16it/s]
                 all  2.51e+03  6.31e+03     0.463     0.461     0.335     0.446

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     33/90     4.23G      1.47     0.957      3.94      6.37        24       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.94it/s]
                 all  2.51e+03  6.31e+03     0.463     0.519     0.391     0.474

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     34/90     4.23G      1.51     0.973      3.93       6.4        28       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:35<00:00,  8.74it/s]
                 all  2.51e+03  6.31e+03     0.402     0.517     0.366     0.431

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     35/90     4.23G       1.5     0.999       4.3       6.8        13       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:34<00:00,  9.02it/s]
                 all  2.51e+03  6.31e+03     0.418     0.494     0.358     0.442

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     36/90     4.23G      1.54      1.03      4.71      7.28        20       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:04<00:00,  2.51it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:36<00:00,  8.67it/s]
                 all  2.51e+03  6.31e+03      0.39     0.462     0.315     0.383

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     37/90     4.23G      1.55      1.04      4.67      7.26        19       416: 100%|███████████████████████████████████████████████████████████████████████████████████| 313/313 [02:05<00:00,  2.50it/s]
               Class    Images   Targets         P         R       mAP        F1: 100%|███████████████████████████████████████████████████████████████████████████████████| 314/314 [00:34<00:00,  9.09it/s]
                 all  2.51e+03  6.31e+03      0.45     0.424     0.311     0.405

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     38/90     4.23G      1.56     0.989      4.22      6.77        41       416:   1%|▌                                                                                    | 2/313 [00:00<02:27,  2.11it/s]     38/90     4.23G      1.56     0.989      4.22      6.77        41       416:   1%|▌                                                                                    | 2/313 [00:01<03:18,  1.56it/s]
Traceback (most recent call last):
  File "train.py", line 479, in <module>
    train()  # train normally
  File "train.py", line 331, in train
    optimizer.step()
  File "/home/jcq/anaconda3/envs/pytorch/lib/python3.6/site-packages/torch/optim/lr_scheduler.py", line 51, in wrapper
    return wrapped(*args, **kwargs)
  File "/home/jcq/anaconda3/envs/pytorch/lib/python3.6/site-packages/torch/optim/sgd.py", line 100, in step
    buf.mul_(momentum).add_(1 - dampening, d_p)
KeyboardInterrupt
(pytorch) 
# jcq @ jcq-linux in /media/jcq/Soft/Pytorch/Model_optimazition/YOLOv3-complete-pruning-voc on git:master x [12:23:50] C:1
$ 

