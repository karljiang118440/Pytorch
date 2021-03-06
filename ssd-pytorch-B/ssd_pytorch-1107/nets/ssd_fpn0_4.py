import torch
import os
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
from utils.config import Config
from nets.ssd_layers import Detect
from nets.ssd_layers import L2Norm,PriorBox
from nets.vgg import vgg as add_vgg

from utils.config import USE_SE,USE_ECA
from utils.attention import Upsample,SEModule,ECAModule


class SSD(nn.Module):
    def __init__(self, phase, base, extras, head, num_classes):
        super(SSD, self).__init__()
        self.phase = phase
        self.num_classes = num_classes
        self.cfg = Config
        self.vgg = nn.ModuleList(base)
        self.L2Norm = L2Norm(512, 20)
        self.extras = nn.ModuleList(extras)
        self.priorbox = PriorBox(self.cfg)
        with torch.no_grad():
            self.priors = Variable(self.priorbox.forward())
        self.loc = nn.ModuleList(head[0])
        self.conf = nn.ModuleList(head[1])
        if phase == 'test':
            self.softmax = nn.Softmax(dim=-1)
            self.detect = Detect(num_classes, 0, 200, 0.01, 0.45)




        self.DilationConv_128_128 = nn.Conv2d(in_channels=128,out_channels=128,kernel_size=3,padding=2,
                                              dilation=2,stride=2)
        self.conv_512_256 = nn.Conv2d(in_channels=512,out_channels=256,kernel_size=1,stride=1)
        self.upsample_1024_1024 = Upsample(38)
        self.conv_1024_128 = nn.Conv2d(in_channels=1024,out_channels=128,kernel_size=1,stride=1)

        self.DilationConv_512_256 = nn.Conv2d(in_channels= 512,out_channels= 256,kernel_size=3,padding=2,dilation=2,
                                              stride=2)

        self.conv_1024_512 = nn.Conv2d(in_channels=1024,out_channels=512,kernel_size=1,stride=1)

        self.upsample_512_512 = Upsample(19)
        self.conv_512_256_fc7 = nn.Conv2d(in_channels=512,out_channels=256,kernel_size=1,stride=1)

        self.DilationConv_512_128_2 = nn.Conv2d(in_channels=512,out_channels=128,kernel_size=3,padding=2,
                                                dilation=2,stride=2)

        self.conv_512_256_2 = nn.Conv2d(in_channels=512,out_channels=256,kernel_size=1,stride=1)

        self.upsample_256_256_2 = Upsample(10)
        self.conv_256_128_2 = nn.Conv2d(in_channels=256,out_channels=128,kernel_size=1,stride=1)


        self.smooth = nn.Conv2d(512,512,kernel_size=3,padding=1,stride=1)
        self.smooth2 = nn.Conv2d(1024,1024,kernel_size=3,padding=1,stride=1)

        self.bn = nn.BatchNorm2d(128)
        self.bn1 = nn.BatchNorm2d(256)


        if USE_SE:
            self.SE1 = SEModule(512)
            self.SE2 = SEModule(512)
            self.SE3 = SEModule(512)
            self.SE4 = SEModule(256)
            self.SE5 = SEModule(256)
            self.SE6 = SEModule(256)

        if USE_ECA:
            self.ECA1 = ECAModule(512)
            self.ECA2 = ECAModule(1024)
            self.ECA3 = ECAModule(512)
            self.ECA4 = ECAModule(256)



            
    def forward(self, x):
        sources = list()
        loc = list()
        conf = list()



        for k in range(10):
            x = self.vgg[k](x)
        sources.append(x)

        # 获得conv4_3的内容
        for k in range(10,23):
            x = self.vgg[k](x)

        s = self.L2Norm(x)
        sources.append(s)

        # 获得fc7的内容
        # for k in range(23, len(self.vgg)):
        #     x = self.vgg[k](x)
        # sources.append(x)

        for k in range(23, 30):
            x = self.vgg[k](x)

        s = self.L2Norm(x)    
        sources.append(s)


        for k in range(30,len(self.vgg)):
            x = self.vgg[k](x)
        sources.append(x)


        # 获得后面的内容
        for k, v in enumerate(self.extras):
            x = F.relu(v(x), inplace=True)
            if k % 2 == 1:
                sources.append(x)

        sources_final = list()
        sources_final1 = list()

        if USE_ECA:
            sources_final.append(self.ECA4(sources[5]))
        else:
            sources_final.append(sources[5])


        conv8_fp1 = torch.cat((F.relu(self.bn(self.DilationConv_512_128_2(sources[2])),inplace=True),
                              F.relu(self.conv_512_256_2(sources[4]),inplace=True),
                              F.relu(self.conv_256_128_2(self.upsample_256_256_2(sources[5])),inplace = True)),1)

        conv8_fp = F.relu(self.smooth(conv8_fp1),inplace=True)

        if USE_ECA:
            sources_final.append(self.ECA3(conv8_fp))
        else:
            sources_final.append(conv8_fp)

        # fc7_fp = torch.cat((F.relu(self.bn(self.DilationConv_512_256(sources[1])),inplace=True),
        #                     F.relu(self.conv_1024_512(sources[3]),inplace=True),
        #                     F.relu(self.conv512_256_fc7(self.upsample_512_512(sources[4])),inplace=True)),1)




        # fc7_fp1 = torch.cat((F.relu(self.bn1(self.DilationConv_512_256(sources[1])),inplace=True),
        #                     F.relu(self.conv_1024_512(sources[3]),inplace=True),
        #                     F.relu(self.conv_512_256_fc7(self.upsample_512_512(sources[4])),inplace=True)),1)

        fc7_fp1 = torch.cat((F.relu(self.bn1(self.DilationConv_512_256(sources[1])), inplace=True),
                            F.relu(self.conv_1024_512(sources[3]), inplace=True),
                            F.relu(self.conv_512_256_fc7(self.upsample_512_512(sources[4])), inplace=True)), 1)


        fc7_fp = F.relu(self.smooth2(fc7_fp1),inplace=True)


        if USE_ECA:
            sources_final.append(self.ECA2(fc7_fp))
        else:
            sources_final.append(fc7_fp)



        conv4_fp = torch.cat((F.relu(self.bn(self.DilationConv_128_128(sources[0])),inplace=True),
                             F.relu(self.conv_512_256(sources[1]),inplace=True),
                             F.relu(self.conv_1024_128(self.upsample_1024_1024(sources[3])),inplace=True)),1)

        conv4_fp = F.relu(self.smooth(conv4_fp),inplace=True)
        if USE_ECA:
            sources_final.append(self.ECA1(conv4_fp))
        else:
            sources_final.append(conv4_fp)





        # 添加回归层和分类层
        # for (x, l, c) in zip(sources, self.loc, self.conf):
        #     loc.append(l(x).permute(0, 2, 3, 1).contiguous())
        #     conf.append(c(x).permute(0, 2, 3, 1).contiguous())

        for (x,l,c) in zip(sources_final[::-1],self.loc,self.conf):
            loc.append(l(x).permute(0,2,3,1).contiguous())
            conf.append(c(x).permute(0,2,3,1).contiguous())

        # 进行resize
        loc = torch.cat([o.view(o.size(0), -1) for o in loc], 1)
        conf = torch.cat([o.view(o.size(0), -1) for o in conf], 1)
        if self.phase == "test":
            # loc会resize到batch_size,num_anchors,4
            # conf会resize到batch_size,num_anchors,
            output = self.detect(
                loc.view(loc.size(0), -1, 4),                   # loc preds
                self.softmax(conf.view(conf.size(0), -1,
                             self.num_classes)),                # conf preds
                self.priors              
            )
        else:
            output = (
                loc.view(loc.size(0), -1, 4),
                conf.view(conf.size(0), -1, self.num_classes),
                self.priors
            )
        return output


def add_extras(i, batch_norm=False):
    # Extra layers added to VGG for feature scaling
    layers = []
    in_channels = i

    # Block 6
    # 19,19,1024 -> 10,10,512
    layers += [nn.Conv2d(in_channels, 256, kernel_size=1, stride=1)]
    layers += [nn.Conv2d(256, 512, kernel_size=3, stride=2, padding=1)]

    # Block 7
    # 10,10,512 -> 5,5,256
    layers += [nn.Conv2d(512, 128, kernel_size=1, stride=1)]
    layers += [nn.Conv2d(128, 256, kernel_size=3, stride=2, padding=1)]

    # Block 8
    # 5,5,256 -> 3,3,256
    layers += [nn.Conv2d(256, 128, kernel_size=1, stride=1)]
    layers += [nn.Conv2d(128, 256, kernel_size=3, stride=1)]
    
    # Block 9
    # 3,3,256 -> 1,1,256
    layers += [nn.Conv2d(256, 128, kernel_size=1, stride=1)]
    layers += [nn.Conv2d(128, 256, kernel_size=3, stride=1)]

    return layers

mbox = [4, 6, 6, 6, 4, 4]

def get_ssd(phase,num_classes):

    vgg, extra_layers = add_vgg(3), add_extras(1024)

    loc_layers = []
    conf_layers = []
    vgg_source = [21, -2]
    for k, v in enumerate(vgg_source):
        loc_layers += [nn.Conv2d(vgg[v].out_channels,
                                 mbox[k] * 4, kernel_size=3, padding=1)]
        conf_layers += [nn.Conv2d(vgg[v].out_channels,
                        mbox[k] * num_classes, kernel_size=3, padding=1)]
                        
    for k, v in enumerate(extra_layers[1::2], 2):
        loc_layers += [nn.Conv2d(v.out_channels, mbox[k]
                                 * 4, kernel_size=3, padding=1)]
        conf_layers += [nn.Conv2d(v.out_channels, mbox[k]
                                  * num_classes, kernel_size=3, padding=1)]

    SSD_MODEL = SSD(phase, vgg, extra_layers, (loc_layers, conf_layers), num_classes)
    return SSD_MODEL
