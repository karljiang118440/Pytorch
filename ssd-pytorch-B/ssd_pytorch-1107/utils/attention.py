import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim.lr_scheduler import _LRScheduler

class ChannelAttention(nn.Module):
    def __init__(self,inpanes,ration = 16):
        super(ChannelAttention,self).__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.max_pool = nn.AdaptiveAvgPool2d(1)

        self.fc1 = nn.Conv2d(inplanes,inpanes // 16,1,bias=False)
        self.relu = nn.ReLU()
        self.fc2  = nn.Conv2d(inpanes // 16,inpanes,1 , bias=False)

        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        """
        docstring
        """
        avg_out = self.fc2(self.relu1(self.fc1(self,avg_pool(x))))
        max_out = self.fc2(self.relu1(self.fc1(self.max_pool(x))))

        out = avg_out + max_out
        return self.sigmoid(out)

#print(ChannelAttention())


class SEModule(nn.Module):
    def __init__(self,channel,reduction=16):
        super(SEModule,self).__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.fc = nn.Sequential(
            nn.Linear(channel,channel // reduction ,bias = False),
            nn.ReLU(inplace= True),
            nn.Linear(channel // reduction, channel,bias= False),
            nn.Sigmoid()

        )

    def forward(self,x):
        b , c, _, _ = x.size()
        y = self.avg_pool(x).view(b,c)
        y = self.fc(y).view(b,c,1,1)
        return x*y.expand_as(x)

        

class Upsample(nn.Module):
    def __init__(self,size,scale_factor=None,mode = "nearest"):
        super(Upsample,self).__init__()
        self.size = size 
        self.scale_factor =  scale_factor
        self.mode = mode 

    def forward(self,x):
        x = F.interpolate(x,size= self.sieze,scale_factor= self.scale_factor,mode = self.mode )
        return x