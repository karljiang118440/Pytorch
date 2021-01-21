import torch
import os
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
from utils.config import Config
from nets.ssd_layers import Detect
from nets.ssd_layers import L2Norm,PriorBox
from nets.vgg import vgg as add_vgg


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


        self.upsample_256_256 = Upsample(10)
        self.conv_256_512 = nn.Conv2d(in_channels = 256,out_channels= 512,kernel_size=1,stride=1)

        #conv8_2 -> conv8_2
        self.conv_512_512_1 = nn.Conv2d(in_channels=512,out_channels= 512,kernel_size=1,stride=1)

        self.upsample_512_512 = Upsample(19)
        self.conv_512_1024 = nn.Conv2d(in_channels=512,out_channels =1024,kernel_size=1,stride =1)
        self.conv_1024_1024 = nn.Conv2d(in_channels=1024,out_channels=1024,kernel_size=1,stride=1)

        self.upsample_1024_1024 = Upsample(38)
        self.conv_1024_512 = nn.Conv2d(in_channels=1024,out_channels=512,kernel_size=1,stride=1)
        self.conv_512_512_2 = nn.Conv2d(in_channels=512,out_channels=512,kernel_size=1,stride=1)

        self.smooth = nn.Conv2d(512,512,kernel_size=3,padding=1,stride=1)
        self.smooth1 = nn.Conv2d(1024,1024,kernel_size=3,padding=1,stride=1)




        if USE_CBAM:

            self.CBAM1 = Bottleneck(512)
            self.CBAM2 = Bottleneck(1024)
            self.CBAM3 = Bottleneck(512)
            self.CBAM4 = Bottleneck(256)
            self.CBAM5 = Bottleneck(256)
            self.CBAM6 = Bottleneck(256)


        if USE_SE:
            self.SE1 = SEModule(512)
            self.SE2 = SEModule(1024)
            self.SE3 = SEModule(512)
            self.SE4 = SEModule(256)
            self.SE5 = SEModule(256)
            self.SE6 = SEModule(256)



    def forward(self, x):
        sources = list()
        attention = list()
        loc = list()
        conf = list()

        # 获得conv4_3的内容
        for k in range(10):
            x = self.vgg[k](x)

        sources.append(x)

        for k in range(23,30):
            x = self.vgg[k](x)

        s = self.L2Norm(x)
        sources.append(s)



        # 获得fc7的内容
        for k in range(30, len(self.vgg)):
            x = self.vgg[k](x)
        sources.append(x)

        # 获得后面的内容
        for k, v in enumerate(self.extras):
            x = F.relu(v(x), inplace=True)
            if k % 2 == 1:
                sources.append(x)

        if USE_SE:
            attention.append(sources[0])
            attention.append(self.SE1(sources[1]))
            attention.append(sources[2])
            attention.append(self.SE2(sources[3]))
            attention.append(self.SE3(sources[4]))
            attention.append(self.SE4(sources[5]))
            attention.append(self.SE5(sources[6]))
            attention.append(self.SE6(sources[7]))

        sources_final = list()

        conv8_fp1 = self.conv_256_512(self.upsample_256_256(attention[5])) + self.conv_512_512_1(attention[4])
        conv8_fp = self.smooth(conv8_fp1)

        fc7_fp1 = self.conv_512_1024(self.upsample_512_512(conv8_fp1)) + self.conv_1024_1024(attention[3])
        fc7_fp = self.smooth(fc7_fp1)

        conv4_fp = self.conv_1024_512(self.upsample_1024_1024(fc7_fp1)) + self.conv_512_512_2(attention[1])
        conv4_fp = self.smooth(conv4_fp)

        if USE_CBAM:
            sources_final.append(self.CBAM1(conv4_fp))
            sources_final.append(self.CBAM2(fc7_fp))
            sources_final.append(self.CBAM3(conv8_fp))
            sources_final.append(self.CBAM4(sources[5]))
            sources_final.append(self.CBAM5(sources[6]))
            sources_final.append(self.CBAM6(sources[7]))


        else:
            sources_final.append(conv4_fp)
            sources_final.append(fc7_fp)
            sources_final.append(conv8_fp)
            sources_final.append(attention[5])
            sources_final.append(attention[6])
            sources_final.append(attention[7])



        # 添加回归层和分类层
        # for (x, l, c) in zip(sources, self.loc, self.conf):
        #     loc.append(l(x).permute(0, 2, 3, 1).contiguous())
        #     conf.append(c(x).permute(0, 2, 3, 1).contiguous())


        for(x,l,c) in zip(sources_final,self.loc,self.conf):
            loc.append(l(x).permute(0,2,3,1).contiguous())
            conf.append(c(x).permute(0,2,3,1).contiguous())

        # 进行resize
        loc = torch.cat([o.view(o.size(0), -1) for o in loc], 1)
        conf = torch.cat([o.view(o.size(0), -1) for o in conf], 1)
        if self.phase == "test":
            # loc会resize到batch_size,num_anchors,4
            # conf会resize到batch_size,num_anchors,

            # 这部分暂时没有进行改动
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
