import torch
import torch.nn as nn
from einops import rearrange, repeat
from .contrast_and_atrous import AttnContrastLayer, AttnContrastLayer_n, AtrousAttnWeight, AttnContrastLayer_d, SELayer, NonLocalBlock,cbam
import math
import torch.nn.functional as F

import numpy as np

__all__ = [
           'RPCANet', 'RPCANet_wo','RPCANetMA','RPCANet9', 'RPCANet_Experi', 'RPCANet_wo_Merge',
           'RPCANetMA7','RPCANetMA8','RPCANetMA9','RPCANetMA10','RPCANetMA11','RPCANetMA12',
           'RPCANet_LSTM','RPCANet_LSTM1','RPCANet_LSTM2']


# A basic building block in many deep neural networks due to its ability to avoid vanishing gradient problems and enable training of deeper networks
class ResidualBlock(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size, bias=True, res_scale=1):

        super(ResidualBlock, self).__init__()
        self.res_scale = res_scale
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size, padding=(kernel_size//2), bias=bias)
        self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size, padding=(kernel_size//2), bias=bias)
        self.act1 = nn.ReLU(inplace=True)

    def forward(self, x):
        input = x
#         print("x[:(x.shape(0)//2), ...]", x[:(x.shape(0)//2), ...].shape)
        x = self.conv1(x)
        x = self.act1(x)
        x = self.conv2(x)
        res = x
        x = res + input
        return x




#====================================================================================================


class RPCANet_Experi(nn.Module):
    def __init__(self, stage_num=6, slayers=6, llayers=4, mlayers=3, channel=32):
        super(RPCANet_Experi, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        for _ in range(stage_num):
            self.decos.append(DecompositionModule_Experi(slayers=slayers, llayers=llayers,
                                                         mlayers=mlayers, channel=channel))

        # 迭代循环初始化参数
        for m in self.modules():
            # 也可以判断是否为conv2d，使用相应的初始化方式
            if isinstance(m, nn.Conv2d):
                nn.init.xavier_normal_(m.weight)
                # nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

    def forward(self, D):
        T = torch.zeros(D.shape).to(D.device)
        for i in range(self.stage_num):
            D, T = self.decos[i](D, T)
        return D, T


class DecompositionModule_Experi(nn.Module):
    def __init__(self, slayers=6, llayers=4, mlayers=3, channel=32):
        super(DecompositionModule_Experi, self).__init__()
        self.lowrank = LowrankModule_Experi(channel=channel, layers=llayers)
        self.sparse = SparseModule_Experi(channel=channel, layers=slayers)
        self.merge = MergeModule_Experi(channel=channel, layers=mlayers)

    def forward(self, D, T):
        B = self.lowrank(D, T)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T


class LowrankModule_Experi(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(LowrankModule_Experi, self).__init__()

        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)

    def forward(self, D, T):
        x = D - T
        B = x + self.convs(x)
        return B


class SparseModule_Experi(nn.Module):
    def __init__(self, channel=32, layers=6):
        super(SparseModule_Experi, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
               nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)
        self.epsilon = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)

    def forward(self, D, B, T):
        x = T + D - B
        T = x - self.epsilon * self.convs(x)
        return T


class MergeModule_Experi(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(MergeModule_Experi, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.mapping = nn.Sequential(*convs)

    def forward(self, B, T):
        return self.mapping(B+T)


#====================================================================================================


class RPCANet_wo_Merge(nn.Module):
    def __init__(self, stage_num=6, slayers=6, llayers=4, channel=32):
        super(RPCANet_wo_Merge, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        for _ in range(stage_num):
            self.decos.append(DecompositionModule_wo_Merge(slayers=slayers, llayers=llayers,
                                                           channel=channel))

        # 迭代循环初始化参数
        for m in self.modules():
            # 也可以判断是否为conv2d，使用相应的初始化方式
            if isinstance(m, nn.Conv2d):
                nn.init.xavier_normal_(m.weight)
                # nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

    def forward(self, D):
        T = torch.zeros(D.shape).to(D.device)
        for i in range(self.stage_num):
            B, T = self.decos[i](D, T)
        return B, T


class DecompositionModule_wo_Merge(nn.Module):
    def __init__(self, slayers=6, llayers=4, channel=32):
        super(DecompositionModule_wo_Merge, self).__init__()
        self.lowrank = LowrankModule_wo_Merge(channel=channel, layers=llayers)
        self.sparse = SparseModule_wo_Merge(channel=channel, layers=slayers)

    def forward(self, D, T):
        B = self.lowrank(D, T)
        T = self.sparse(D, B, T)
        return B, T


class LowrankModule_wo_Merge(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(LowrankModule_wo_Merge, self).__init__()

        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)

    def forward(self, D, T):
        x = D - T
        B = x + self.convs(x)
        return B


class SparseModule_wo_Merge(nn.Module):
    def __init__(self, channel=32, layers=6):
        super(SparseModule_wo_Merge, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
               nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)
        self.epsilon = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)

    def forward(self, D, B, T):
        x = T + D - B
        T = x - self.epsilon * self.convs(x)
        return T



#====================================================================================================


class RPCANet_wo(nn.Module):
    def __init__(self, stage_num=6, slayers=6, llayers=4, channel=32):
        super(RPCANet_wo, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        for _ in range(stage_num):
            self.decos.append(DecompositionModule_wo(slayers=slayers, llayers=llayers,
                                                           channel=channel))

        # 迭代循环初始化参数
        for m in self.modules():
            # 也可以判断是否为conv2d，使用相应的初始化方式
            if isinstance(m, nn.Conv2d):
                nn.init.xavier_normal_(m.weight)
                # nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

    def forward(self, D):
        T = torch.zeros(D.shape).to(D.device)
        for i in range(self.stage_num):
            D, T = self.decos[i](D, T)
        return D, T


class DecompositionModule_wo(nn.Module):
    def __init__(self, slayers=6, llayers=4, channel=32):
        super(DecompositionModule_wo, self).__init__()
        self.lowrank = LowrankModule_wo(channel=channel, layers=llayers)
        self.sparse = SparseModule_wo(channel=channel, layers=slayers)

    def forward(self, D, T):
        B = self.lowrank(D, T)
        T = self.sparse(D, B, T)
        D = B + T
        return D, T


class LowrankModule_wo(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(LowrankModule_wo, self).__init__()

        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)

    def forward(self, D, T):
        x = D - T
        B = x + self.convs(x)
        return B


class SparseModule_wo(nn.Module):
    def __init__(self, channel=32, layers=6):
        super(SparseModule_wo, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
               nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)
        self.epsilon = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)

    def forward(self, D, B, T):
        x = T + D - B
        T = x - self.epsilon * self.convs(x)
        return T


# #====================================================================================================


class RPCANet(nn.Module):
    def __init__(self, stage_num=6, slayers=6, llayers=3, mlayers=3, channel=32):
        super(RPCANet, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        for _ in range(stage_num):
            self.decos.append(DecompositionModule(slayers=slayers, llayers=llayers,
                                                  mlayers=mlayers, channel=channel))

        # 迭代循环初始化参数
        for m in self.modules():
            # 也可以判断是否为conv2d，使用相应的初始化方式
            if isinstance(m, nn.Conv2d):
                nn.init.xavier_normal_(m.weight)
                # nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

    def forward(self, D):
        T = torch.zeros(D.shape).to(D.device)
        for i in range(self.stage_num):
            D, T = self.decos[i](D, T)
        return D, T

class DecompositionModule(nn.Module):
    def __init__(self, slayers=6, llayers=4, mlayers=3, channel=32):
        super(DecompositionModule, self).__init__()
        self.lowrank = LowrankModule(channel=channel, layers=llayers)
        self.sparse = SparseModule(channel=channel, layers=slayers)
        self.merge = MergeModule(channel=channel, layers=mlayers)

    def forward(self, D, T):
        B = self.lowrank(D, T)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T



class LowrankModule(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(LowrankModule, self).__init__()

        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.BatchNorm2d(channel),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.BatchNorm2d(channel))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)

    def forward(self, D, T):
        x = D - T
        B = x + self.convs(x)
        return B


class SparseModule(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModule, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)
        self.epsilon = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)

    def forward(self, D, B, T):
        #print(D.shape)
        x = T + D - B
        T = x - self.epsilon * self.convs(x)
        return T


class MergeModule(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(MergeModule, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.BatchNorm2d(channel),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.BatchNorm2d(channel))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.mapping = nn.Sequential(*convs)

    def forward(self, B, T):
        return self.mapping(B+T)


# #====================================================================================================


class RPCANet9(nn.Module):
    def __init__(self, stage_num=6, slayers=6, llayers=3, mlayers=3, channel=32, mode='train'):
        super(RPCANet9, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for _ in range(stage_num):
            self.decos.append(DecompositionModule9(slayers=slayers, llayers=llayers,
                                                  mlayers=mlayers, channel=channel))
        # 迭代循环初始化参数
        for m in self.modules():
            # 也可以判断是否为conv2d，使用相应的初始化方式
            if isinstance(m, nn.Conv2d):
                nn.init.xavier_normal_(m.weight)
                #nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

    def forward(self, D):
        T = torch.zeros(D.shape).to(D.device)
        for i in range(self.stage_num):
            D, T = self.decos[i](D, T)
        if self.mode == 'train':
            return D,T
        else:
            return T

class DecompositionModule9(object):
    pass


class DecompositionModule9(nn.Module):
    def __init__(self, slayers=6, llayers=3, mlayers=3, channel=32):
        super(DecompositionModule9, self).__init__()
        self.lowrank = LowrankModule9(channel=channel, layers=llayers)
        self.sparse = SparseModule9(channel=channel, layers=slayers)
        self.merge = MergeModule9(channel=channel, layers=mlayers)

    def forward(self, D, T):
        B = self.lowrank(D, T)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T


class LowrankModule9(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(LowrankModule9, self).__init__()

        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.BatchNorm2d(channel),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.BatchNorm2d(channel))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)
        #self.relu = nn.ReLU()
        #self.gamma = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)

    def forward(self, D, T):
        x = D - T
        B = x + self.convs(x)
        return B


class SparseModule9(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModule9, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)
        self.epsilon = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)

    def forward(self, D, B, T):
        # print(D.shape)
        x = T + D - B
        T = x - self.epsilon * self.convs(x)
        return T


class MergeModule9(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(MergeModule9, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.BatchNorm2d(channel),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.BatchNorm2d(channel))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.mapping = nn.Sequential(*convs)

    def forward(self, B, T):
        x = B + T
        D = self.mapping(x)
        return D


# #====================================================================================================


class RPCANetMA(nn.Module):
    def __init__(self, stage_num=6, slayers=6, llayers=3, mlayers=3, channel=32, mode='train'):
        super(RPCANetMA, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for i in range(stage_num):
            self.decos.append(DecompositionModuleMA(stage_num=i+1, slayers=slayers, llayers=llayers,
                                                  mlayers=mlayers, channel=channel))
        # 迭代循环初始化参数
        for m in self.modules():
            # 也可以判断是否为conv2d，使用相应的初始化方式
            if isinstance(m, nn.Conv2d):
                nn.init.xavier_normal_(m.weight)
                #nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

    def forward(self, D):
        T = torch.zeros(D.shape).to(D.device)
        feats = T
        for i in range(self.stage_num):
            D, T = self.decos[i](D, T, feats)
            feats = torch.cat((feats, T), dim=1)
        if self.mode == 'train':
            return D,T
        else:
            return T

class DecompositionModuleMA(object):
    pass


class DecompositionModuleMA(nn.Module):
    def __init__(self, stage_num, slayers=6, llayers=3, mlayers=3, channel=32):
        super(DecompositionModuleMA, self).__init__()
        self.lowrank = LowrankModuleMA(channel=channel, layers=llayers)
        self.sparse = SparseModuleMA(stage_num=stage_num, channel=channel, layers=slayers)
        self.merge = MergeModuleMA(channel=channel, layers=mlayers)

    def forward(self, D, T, feats):
        B = self.lowrank(D, T)
        T = self.sparse(D, B, T, feats)
        D = self.merge(B, T)
        return D, T


class LowrankModuleMA(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(LowrankModuleMA, self).__init__()

        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.BatchNorm2d(channel),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.BatchNorm2d(channel))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)
        #self.relu = nn.ReLU()
        #self.gamma = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)

    def forward(self, D, T):
        x = D - T
        B = x + self.convs(x)
        return B


class SparseModuleMA(nn.Module):
    def __init__(self, stage_num, channel=32, layers=6) -> object:
        super(SparseModuleMA, self).__init__()
        convs = [nn.Conv2d(stage_num+1, channel, kernel_size=3, padding=1, stride=1),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)
        self.epsilon = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)

    def forward(self, D, B, T, feats):
        # print(D.shape)
        x = T + D - B
        T = x - self.epsilon * self.convs(torch.cat((x, feats), dim=1))
        return T


class MergeModuleMA(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(MergeModuleMA, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.BatchNorm2d(channel),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.BatchNorm2d(channel))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.mapping = nn.Sequential(*convs)

    def forward(self, B, T):
        x = B + T
        D = self.mapping(x)
        return D





# #====================================================================================================


class RPCANetMA7(nn.Module):
    def __init__(self, stage_num=6, slayers=6, llayers=3, mlayers=3, channel=32, mode='train'):
        super(RPCANetMA7, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for i in range(stage_num):
            self.decos.append(DecompositionModuleMA7(stage_num=i+1, slayers=slayers, llayers=llayers,
                                                  mlayers=mlayers, channel=channel))
        # 迭代循环初始化参数
        for m in self.modules():
            # 也可以判断是否为conv2d，使用相应的初始化方式
            if isinstance(m, nn.Conv2d):
                nn.init.xavier_normal_(m.weight)
                #nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

    def forward(self, D):
        T = torch.zeros(D.shape).to(D.device)
        feats = D - T
        for i in range(self.stage_num):
            D, T = self.decos[i](D, T, feats)
            B = D - T
            feats = torch.cat((feats, B), dim=1)
        if self.mode == 'train':
            return D,T
        else:
            return T


class DecompositionModuleMA7(nn.Module):
    def __init__(self, stage_num, slayers=6, llayers=3, mlayers=3, channel=32):
        super(DecompositionModuleMA7, self).__init__()
        self.lowrank = LowrankModuleMA7(stage_num=stage_num, channel=channel, layers=llayers)
        self.sparse = SparseModuleMA7(channel=channel, layers=slayers)
        self.merge = MergeModuleMA7(channel=channel, layers=mlayers)

    def forward(self, D, T, feats):
        B = self.lowrank(D, T, feats)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T


class LowrankModuleMA7(nn.Module):
    def __init__(self, stage_num, channel=32, layers=3):
        super(LowrankModuleMA7, self).__init__()
        convs = [nn.Conv2d(stage_num+1, channel, kernel_size=3, padding=1, stride=1),
                 nn.BatchNorm2d(channel),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.BatchNorm2d(channel))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)

    def forward(self,  D, T, feats):
        x = D - T
        acc = torch.cat((x,feats),dim=1)
        B = x + self.convs(acc)
        return B


class SparseModuleMA7(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModuleMA7, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)

        self.epsilon = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)
        self.beta = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)

        self.nlb = NonLocalBlock(planes=channel // 2)
        self.cbam = cbam(in_channel=channel)
        self.rc = nn.Conv2d(channel // 2, channel, kernel_size=3, padding=1, stride=1)

    def forward(self, D, B, T):
        # print(D.shape)
        x = T + D - B
        w = self.cbam(x)
        # w = self.rc(w)
        T = x - self.epsilon * self.convs(x + w)
        # T = T + w
        # T = self.conv2_1(torch.cat((w, T),dim = 1))
        return T


class MergeModuleMA7(nn.Module):
    def __init__(self,  channel=32, layers=3):
        super(MergeModuleMA7, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.BatchNorm2d(channel),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.BatchNorm2d(channel))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.mapping = nn.Sequential(*convs)

    def forward(self, B, T):
        x = B + T
        D = self.mapping(x)
        return D

# #====================================================================================================


class RPCANetMA8(nn.Module):
    def __init__(self, stage_num=6, slayers=6, mlayers=3, channel=32, mode='train'):
        super(RPCANetMA8, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for i in range(stage_num):
            self.decos.append(DecompositionModuleMA8(stage_num=i+1, slayers=slayers,
                                                  mlayers=mlayers, channel=channel))
        # 迭代循环初始化参数
        for m in self.modules():
            # 也可以判断是否为conv2d，使用相应的初始化方式
            if isinstance(m, nn.Conv2d):
                nn.init.xavier_normal_(m.weight)
                #nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

    def forward(self, D):
        T = torch.zeros(D.shape).to(D.device)
        feats = D - T
        for i in range(self.stage_num):
            D, T = self.decos[i](D, T, feats)
            B = D - T
            feats = torch.cat((feats, B), dim=1)
        if self.mode == 'train':
            return D,T
        else:
            return T



class DecompositionModuleMA8(nn.Module):
    def __init__(self, stage_num, slayers=6, mlayers=3, channel=32):
        super(DecompositionModuleMA8, self).__init__()
        self.lowrank = LowrankModuleMA8(stage_num=stage_num, channel=channel)
        self.sparse = SparseModuleMA8(channel=channel, layers=slayers)
        self.merge = MergeModuleMA8(channel=channel, layers=mlayers)

    def forward(self, D, T, feats):
        B = self.lowrank(D, T, feats)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T


class LowrankModuleMA8(nn.Module):
    def __init__(self, stage_num, channel=32):
        super(LowrankModuleMA8, self).__init__()
        self.channel = channel
        self.relu = nn.ReLU(True)
        self.ext = nn.Sequential(
            nn.Conv2d(stage_num+1, self.channel, kernel_size=3, padding=1, stride=1),
            nn.BatchNorm2d(self.channel),
        )
        self.res1 = nn.Sequential(
            nn.Conv2d(self.channel, self.channel, kernel_size=3, padding=1, stride=1),
            nn.BatchNorm2d(self.channel),
            nn.ReLU(True),
            nn.Conv2d(self.channel, self.channel, kernel_size=3, padding=1, stride=1),
            nn.BatchNorm2d(self.channel),
        )
        self.res2 = nn.Sequential(
            nn.Conv2d(self.channel, self.channel, kernel_size=3, padding=1, stride=1),
            nn.BatchNorm2d(self.channel),
            nn.ReLU(True),
            nn.Conv2d(self.channel, self.channel, kernel_size=3, padding=1, stride=1),
            nn.BatchNorm2d(self.channel),
        )
        self.rec = nn.Sequential(
            nn.Conv2d(self.channel, 1, kernel_size=3, padding=1, stride=1),
        )
        #self.relu = nn.ReLU()
        #self.gamma = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)

    def forward(self, D, T, feats):
        x = D - T
        acc = torch.cat((x, feats), dim=1)
        ext1 = self.ext(acc)
        rb1 = self.relu(ext1 + self.res1(ext1))
        rb2 = self.relu(rb1 + self.res1(rb1))
        rec = self.relu(self.rec(rb2))
        B = x  + rec
        return B



class SparseModuleMA8(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModuleMA8, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)

        self.epsilon = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)
        self.beta = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)

        self.nlb = NonLocalBlock(planes=channel // 2)
        self.cbam = cbam(in_channel=channel)
        self.rc = nn.Conv2d(channel // 2, channel, kernel_size=3, padding=1, stride=1)

    def forward(self, D, B, T):
        # print(D.shape)
        x = T + D - B
        w = self.cbam(x)
        # w = self.rc(w)
        T = x - self.epsilon * self.convs(x + w)
        # T = T + w
        # T = self.conv2_1(torch.cat((w, T),dim = 1))
        return T


class MergeModuleMA8(nn.Module):
    def __init__(self,  channel=32, layers=3):
        super(MergeModuleMA8, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.BatchNorm2d(channel),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.BatchNorm2d(channel))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.mapping = nn.Sequential(*convs)

    def forward(self, B, T):
        x = B + T
        D = self.mapping(x)
        return D


# #====================================================================================================


class RPCANetMA9(nn.Module):
    def __init__(self, stage_num=6, slayers=6, mlayers=3, channel=32, mode='train'):
        super(RPCANetMA9, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for i in range(stage_num):
            self.decos.append(DecompositionModuleMA9(stage_num=i+1, slayers=slayers,
                                                  mlayers=mlayers, channel=channel))
        # 迭代循环初始化参数
        for m in self.modules():
            # 也可以判断是否为conv2d，使用相应的初始化方式
            if isinstance(m, nn.Conv2d):
                nn.init.xavier_normal_(m.weight)
                #nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

    def forward(self, D):
        T = torch.zeros(D.shape).to(D.device)
        # B = torch.zeros(D.shape).to(D.device)
        feats = D - T
        for i in range(self.stage_num):
            D, T, B = self.decos[i](D, T, feats)
            feats = torch.cat((feats, B), dim=1)
        if self.mode == 'train':
            return D,T
        else:
            return T


class DecompositionModuleMA9(nn.Module):
    def __init__(self, stage_num, llayers=6,slayers=6, mlayers=3, channel=32):
        super(DecompositionModuleMA9, self).__init__()
        self.lowrank = LowrankModuleMA9(stage_num=stage_num, channel=channel,layers = llayers)
        self.sparse = SparseModuleMA9(channel=channel, layers=slayers)
        self.merge = MergeModuleMA9(channel=channel, layers=mlayers)

    def forward(self, D, T, feats):
        B = self.lowrank(D, T, feats)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T, B

class LowrankModuleMA9(nn.Module):
    def __init__(self, stage_num, channel=32, layers=3):
        super(LowrankModuleMA9, self).__init__()
        convs = [nn.Conv2d(stage_num + 1, channel, kernel_size=3, padding=1, stride=1),
                         nn.BatchNorm2d(channel),
                         nn.ReLU(True)]
        for i in range(layers):
                convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
                convs.append(nn.BatchNorm2d(channel))
                convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)

    def forward(self, D, T, feats):
        x = D - T
        acc = torch.cat((x, feats), dim=1)
        B = x + self.convs(acc)
        return B




class SparseModuleMA9(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModuleMA9, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)

        self.epsilon = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)
        self.beta = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)

        self.nlb = NonLocalBlock(planes=channel // 2)
        self.cbam = cbam(in_channel=channel)
        self.rc = nn.Conv2d(channel // 2, channel, kernel_size=3, padding=1, stride=1)

    def forward(self, D, B, T):
        # print(D.shape)
        x = T + D - B
        w = self.cbam(x)
        # w = self.rc(w)
        T = x - self.epsilon * self.convs(x + w)
        # T = T + w
        # T = self.conv2_1(torch.cat((w, T),dim = 1))
        return T


class MergeModuleMA9(nn.Module):
    def __init__(self,  channel=32, layers=3):
        super(MergeModuleMA9, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.BatchNorm2d(channel),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.BatchNorm2d(channel))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.mapping = nn.Sequential(*convs)

    def forward(self, B, T):
        x = B + T
        D = self.mapping(x)
        return D


# #====================================================================================================


class RPCANetMA10(nn.Module):
    def __init__(self, stage_num=6, slayers=6, llayers=4, mlayers=3, channel=32, mode='train'):
        super(RPCANetMA10, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for i in range(stage_num):
            self.decos.append(DecompositionModuleMA10(stage_num=i+1, slayers=slayers, llayers= llayers,
                                                  mlayers=mlayers, channel=channel))
        # 迭代循环初始化参数
        for m in self.modules():
            # 也可以判断是否为conv2d，使用相应的初始化方式
            if isinstance(m, nn.Conv2d):
                nn.init.xavier_normal_(m.weight)
                #nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

    def forward(self, D):
        T = torch.zeros(D.shape).to(D.device)
        # B = torch.zeros(D.shape).to(D.device)
        feats = D - T
        for i in range(self.stage_num):
            D, T, B = self.decos[i](D, T, feats)
            feats = torch.cat((feats, B), dim=1)
        if self.mode == 'train':
            return D,T
        else:
            return T


class DecompositionModuleMA10(nn.Module):
    def __init__(self, stage_num, slayers=6, llayers=6,  mlayers=3, channel=32):
        super(DecompositionModuleMA10, self).__init__()
        self.lowrank = LowrankModuleMA10(stage_num=stage_num, channel=channel,layers = llayers)
        self.sparse = SparseModuleMA10(channel=channel, layers=slayers)
        self.merge = MergeModuleMA10(channel=channel, layers=mlayers)

    def forward(self, D, T, feats):
        B = self.lowrank(D, T, feats)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T, B

class LowrankModuleMA10(nn.Module):
    def __init__(self, stage_num, channel=32, layers=3):
        super(LowrankModuleMA10, self).__init__()
        convs = [nn.Conv2d(stage_num + 1, channel, kernel_size=3, padding=1, stride=1),
                         nn.BatchNorm2d(channel),
                         nn.ReLU(True)]
        for i in range(layers):
                convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
                convs.append(nn.BatchNorm2d(channel))
                convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)

    def forward(self, D, T, feats):
        x = D - T
        acc = torch.cat((x, feats), dim=1)
        B = x + self.convs(acc)
        return B

class SparseModuleMA10(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModuleMA10, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)

        self.epsilon = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)
        self.beta = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)

        self.nlb = NonLocalBlock(planes=channel // 2)
        self.cbam = cbam(in_channel=channel)
        self.rc = nn.Conv2d(channel // 2, channel, kernel_size=3, padding=1, stride=1)

    def forward(self, D, B, T):
        # print(D.shape)
        x = T + D - B
        w = self.cbam(x)
        # w = self.rc(w)
        T = x - self.epsilon * self.convs(x + w)
        # T = T + w
        # T = self.conv2_1(torch.cat((w, T),dim = 1))
        return T


class MergeModuleMA10(nn.Module):
    def __init__(self,  channel=32, layers=3):
        super(MergeModuleMA10, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.BatchNorm2d(channel),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.BatchNorm2d(channel))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.mapping = nn.Sequential(*convs)

    def forward(self, B, T):
        x = B + T
        D = self.mapping(x)
        return D


# #====================================================================================================

'''
Are training
'''
class RPCANetMA11(nn.Module):
    def __init__(self, stage_num=6, slayers=6, llayers=4, mlayers=3, channel=32, mode='train'):
        super(RPCANetMA11, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for i in range(stage_num):
            self.decos.append(DecompositionModuleMA11(stage_num=i+1, slayers=slayers, llayers= llayers,
                                                  mlayers=mlayers, channel=channel))
        # 迭代循环初始化参数
        for m in self.modules():
            # 也可以判断是否为conv2d，使用相应的初始化方式
            if isinstance(m, nn.Conv2d):
                nn.init.xavier_normal_(m.weight)
                #nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

    def forward(self, D):
        T = torch.zeros(D.shape).to(D.device)
        # B = torch.zeros(D.shape).to(D.device)
        feats = D - T
        for i in range(self.stage_num):
            D, T, B = self.decos[i](D, T, feats)
            feats = torch.cat((feats, B), dim=1)
        if self.mode == 'train':
            return D,T
        else:
            return T


class DecompositionModuleMA11(nn.Module):
    def __init__(self, stage_num, slayers=6, llayers=6,  mlayers=3, channel=32):
        super(DecompositionModuleMA11, self).__init__()
        self.lowrank = LowrankModuleMA11(stage_num=stage_num, channel=channel,layers = llayers)
        self.sparse = SparseModuleMA11(channel=channel, layers=slayers)
        self.merge = MergeModuleMA11(channel=channel, layers=mlayers)

    def forward(self, D, T, feats):
        B = self.lowrank(D, T, feats)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T, B

class LowrankModuleMA11(nn.Module):
    def __init__(self, stage_num, channel=32, layers=3):
        super(LowrankModuleMA11, self).__init__()
        convs = [nn.Conv2d(stage_num + 1, channel, kernel_size=3, padding=1, stride=1),
                         nn.BatchNorm2d(channel),
                         nn.ReLU(True)]
        for i in range(layers):
                convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
                convs.append(nn.BatchNorm2d(channel))
                convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)

    def forward(self, D, T, feats):
        x = D - T
        acc = torch.cat((x, feats), dim=1)
        B = x + self.convs(acc)
        return B

class SparseModuleMA11(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModuleMA11, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)

        self.epsilon = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)
        # self.beta = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)
        self.contrast = nn.Sequential(
                nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                nn.ReLU(True),
                AttnContrastLayer(channel, kernel_size=17, padding=8),
                nn.ReLU(True),
                nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1)
            )

    def forward(self, D, B, T):
        # print(D.shape)
        x = T + D - B
        w = self.contrast(x)
        # w = self.rc(w)
        T = x - self.epsilon * self.convs(x + w)
        # T = T + w
        # T = self.conv2_1(torch.cat((w, T),dim = 1))
        return T


class MergeModuleMA11(nn.Module):
    def __init__(self,  channel=32, layers=3):
        super(MergeModuleMA11, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.BatchNorm2d(channel),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.BatchNorm2d(channel))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.mapping = nn.Sequential(*convs)

    def forward(self, B, T):
        x = B + T
        D = self.mapping(x)
        return D


# #====================================================================================================

'''
Have trained
'''
class RPCANetMA12(nn.Module):
    def __init__(self, stage_num=6, slayers=6, llayers=4, mlayers=3, channel=32, mode='train'):
        super(RPCANetMA12, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for i in range(stage_num):
            self.decos.append(DecompositionModuleMA12(stage_num=i+1, slayers=slayers, llayers= llayers,
                                                  mlayers=mlayers, channel=channel))
        # 迭代循环初始化参数
        for m in self.modules():
            # 也可以判断是否为conv2d，使用相应的初始化方式
            if isinstance(m, nn.Conv2d):
                nn.init.xavier_normal_(m.weight)
                #nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

    def forward(self, D):
        T = torch.zeros(D.shape).to(D.device)
        # B = torch.zeros(D.shape).to(D.device)
        feats = D - T
        for i in range(self.stage_num):
            D, T, B = self.decos[i](D, T, feats)
            feats = torch.cat((feats, B), dim=1)
        if self.mode == 'train':
            return D,T
        else:
            return T


class DecompositionModuleMA12(nn.Module):
    def __init__(self, stage_num, slayers=6, llayers=6,  mlayers=3, channel=32):
        super(DecompositionModuleMA12, self).__init__()
        self.lowrank = LowrankModuleMA12(stage_num=stage_num, channel=channel,layers = llayers)
        self.sparse = SparseModuleMA12(channel=channel, layers=slayers)
        self.merge = MergeModuleMA12(channel=channel, layers=mlayers)

    def forward(self, D, T, feats):
        B = self.lowrank(D, T, feats)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T, B

class LowrankModuleMA12(nn.Module):
    def __init__(self, stage_num, channel=32, layers=3):
        super(LowrankModuleMA12, self).__init__()
        convs = [nn.Conv2d(stage_num + 1, channel, kernel_size=3, padding=1, stride=1),
                         nn.BatchNorm2d(channel),
                         nn.ReLU(True)]
        for i in range(layers):
                convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
                convs.append(nn.BatchNorm2d(channel))
                convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)

    def forward(self, D, T, feats):
        x = D - T
        acc = torch.cat((x, feats), dim=1)
        B = x + self.convs(acc)
        return B

class SparseModuleMA12(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModuleMA12, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)

        self.epsilon = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)
        # self.beta = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)
        self.contrast = nn.Sequential(
                nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                nn.ReLU(True),
                AttnContrastLayer_n(channel, kernel_size=17, padding=8),
                nn.BatchNorm2d(channel),
                nn.LeakyReLU(0.1, inplace=True),
                nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1)
            )


    def forward(self, D, B, T):
        # print(D.shape)
        x = T + D - B
        w = self.contrast(x)
        # w = self.rc(w)
        T = x - self.epsilon * self.convs(x + w)
        # T = T + w
        # T = self.conv2_1(torch.cat((w, T),dim = 1))
        return T


class MergeModuleMA12(nn.Module):
    def __init__(self,  channel=32, layers=3):
        super(MergeModuleMA12, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.BatchNorm2d(channel),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.BatchNorm2d(channel))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.mapping = nn.Sequential(*convs)

    def forward(self, B, T):
        x = B + T
        D = self.mapping(x)
        return D


# #====================================================================================================


class RPCANet_LSTM(nn.Module):
    def __init__(self, stage_num=6, slayers=6, mlayers=3, channel=32, mode='train'):
        super(RPCANet_LSTM, self).__init__()。#继承
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for i in range(stage_num): #Stacking DecompositionModule_LSTM in a sequence so that each stage builds upon the previous one
            self.decos.append(DecompositionModule_LSTM(slayers=slayers, mlayers=mlayers, channel=channel))
        
        # 迭代循环初始化参数
        for m in self.modules():
            # 也可以判断是否为conv2d，使用相应的初始化方式
            if isinstance(m, nn.Conv2d):
                nn.init.xavier_normal_(m.weight)
                #nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

    def forward(self, D): #The forward pass processes an input tensor 'D'
        T = torch.zeros(D.shape).to(D.device)
        [h, c] = [None, None]
        # B = torch.zeros(D.shape).to(D.device)
        for i in range(self.stage_num):
            D, T, h, c = self.decos[i](D, T, h, c)
        if self.mode == 'train':
            return D,T
        else:
            return T


class ConvLSTM(nn.Module):
    def __init__(self, inp_dim, oup_dim, kernel):
        super().__init__()
        pad_x = 1
        self.conv_xf = nn.Conv2d(inp_dim, oup_dim, kernel, padding=pad_x)
        self.conv_xi = nn.Conv2d(inp_dim, oup_dim, kernel, padding=pad_x)
        self.conv_xo = nn.Conv2d(inp_dim, oup_dim, kernel, padding=pad_x)
        self.conv_xj = nn.Conv2d(inp_dim, oup_dim, kernel, padding=pad_x)

        pad_h = 1
        self.conv_hf = nn.Conv2d(oup_dim, oup_dim, kernel, padding=pad_h)
        self.conv_hi = nn.Conv2d(oup_dim, oup_dim, kernel, padding=pad_h)
        self.conv_ho = nn.Conv2d(oup_dim, oup_dim, kernel, padding=pad_h)
        self.conv_hj = nn.Conv2d(oup_dim, oup_dim, kernel, padding=pad_h)

    def forward(self, x, h, c):

        if h is None and c is None:
            #Do not exsit forget gate firstly
            i = F.sigmoid(self.conv_xi(x))
            o = F.sigmoid(self.conv_xo(x))
            j = F.tanh(self.conv_xj(x))
            c = i * j
            h = o * c
        else:
            f = F.sigmoid(self.conv_xf(x) + self.conv_hf(h))
            i = F.sigmoid(self.conv_xi(x) + self.conv_hi(h))
            o = F.sigmoid(self.conv_xo(x) + self.conv_ho(h))
            j = F.tanh(self.conv_xj(x) + self.conv_hj(h))
            c = f * c + i * j
            h = o * F.tanh(c)

        return h, h, c

class DecompositionModule_LSTM(nn.Module):  #Orchestrates the interaction between low-rank approximation, sparse representation, and merging of theses components
    def __init__(self, slayers=6, mlayers=3, channel=32):
        super(DecompositionModule_LSTM, self).__init__()
        self.lowrank = LowrankModule_LSTM(channel=channel)
        self.sparse = SparseModule_LSTM(channel=channel, layers=slayers)
        self.merge = MergeModule_LSTM(channel=channel, layers=mlayers)

    def forward(self, D, T, h, c):
        B, h, c = self.lowrank(D, T, h, c)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T, h, c


class LowrankModule_LSTM(nn.Module):
    def __init__(self, channel=32):
        super(LowrankModule_LSTM, self).__init__()
        self.conv1_C = nn.Sequential(nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                         nn.BatchNorm2d(channel),
                         nn.ReLU(True))
                         #a Sequential container that groups a 2D convolutional layer, a batch normalization layer, and a ReLU activation
        self.RB_1 = ResidualBlock(channel, channel, 3, bias=True, res_scale=1) #残差网络 有助于解决深层网络梯度消失和梯度爆炸的问题
        self.RB_2 = ResidualBlock(channel, channel, 3, bias=True, res_scale=1)
        self.convC_1 = nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1) #Receive input with 32 channel and produce output with 1 channel
        self.ConvLSTM = ConvLSTM(channel, channel, 3)

    def forward(self, D, T, h, c):
        x = D - T
        x_c = self.conv1_C(x)
        x_c1 = self.RB_1(x_c)
        x_ct, h, c = self.ConvLSTM(x_c1, h, c)
        x_c2 = self.RB_2(x_ct)
        x_1 = self.convC_1(x_c2)
        B = x + x_1
        return B, h, c

class SparseModule_LSTM(nn.Module): #理解不深
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModule_LSTM, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.ReLU(True)]
        for i in range(layers): #Constructs a sequence of convolutional layers and ReLU activations
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)

        self.epsilon = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)  #a trainable parameter, serving as a scaling factor in the module's operations
        # self.beta = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)
        self.contrast = nn.Sequential(
                nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                nn.ReLU(True),
                AttnContrastLayer_n(channel, kernel_size=17, padding=8),
                nn.BatchNorm2d(channel),
                nn.LeakyReLU(0.1, inplace=True),
                nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1)
            )


    def forward(self, D, B, T):
        # print(D.shape)
        x = T + D - B
        w = self.contrast(x)
        # w = self.rc(w)
        T = x - self.epsilon * self.convs(x + w) #To achieve sparse feature enhancement
        # T = T + w
        # T = self.conv2_1(torch.cat((w, T),dim = 1))
        return T


class MergeModule_LSTM(nn.Module):
    def __init__(self,  channel=32, layers=3):
        super(MergeModule_LSTM, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.BatchNorm2d(channel),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.BatchNorm2d(channel))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.mapping = nn.Sequential(*convs)

    def forward(self, B, T):
        x = B + T
        D = self.mapping(x)
        return D


# #====================================================================================================


class RPCANet_LSTM1(nn.Module):
    def __init__(self, stage_num=6, slayers=6, mlayers=3, channel=32, mode='train'):
        super(RPCANet_LSTM1, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for i in range(stage_num):
            self.decos.append(DecompositionModule_LSTM1(slayers=slayers, mlayers=mlayers, channel=channel))
        # 迭代循环初始化参数
        for m in self.modules():
            # 也可以判断是否为conv2d，使用相应的初始化方式
            if isinstance(m, nn.Conv2d):
                nn.init.xavier_normal_(m.weight)
                #nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

    def forward(self, D):
        T = torch.zeros(D.shape).to(D.device)
        [h, c] = [None, None]
        # B = torch.zeros(D.shape).to(D.device)
        for i in range(self.stage_num):
            D, T, h, c = self.decos[i](D, T, h, c)
        if self.mode == 'train':
            return D,T
        else:
            return T


class DecompositionModule_LSTM1(nn.Module):
    def __init__(self, slayers=6, mlayers=3, channel=32):
        super(DecompositionModule_LSTM1, self).__init__()
        self.lowrank = LowrankModule_LSTM1(channel=channel)
        self.sparse = SparseModule_LSTM1(channel=channel, layers=slayers)
        self.merge = MergeModule_LSTM1(channel=channel, layers=mlayers)

    def forward(self, D, T, h, c):
        B, h, c = self.lowrank(D, T, h, c)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T, h, c


class LowrankModule_LSTM1(nn.Module):
    def __init__(self, channel=32):
        super(LowrankModule_LSTM1, self).__init__()
        self.conv1_C = nn.Sequential(nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                         nn.BatchNorm2d(channel),
                         nn.ReLU(True))
        self.RB_1 = ResidualBlock(channel, channel, 3, bias=True, res_scale=1)
        self.RB_2 = ResidualBlock(channel, channel, 3, bias=True, res_scale=1)
        self.convC_1 = nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1)
        self.ConvLSTM = ConvLSTM(channel, channel, 3)

    def forward(self, D, T, h, c):
        x = D - T
        x_c = self.conv1_C(x)
        x_c1 = self.RB_1(x_c)
        x_ct, h, c = self.ConvLSTM(x_c1, h, c)
        x_c2 = self.RB_2(x_ct)
        x_1 = self.convC_1(x_c2)
        B = x + x_1
        return B, h, c

class SparseModule_LSTM1(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModule_LSTM1, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)

        self.epsilon = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)
        # self.beta = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)
        self.contrast = nn.Sequential(
                nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                nn.ReLU(True),
                AttnContrastLayer(channel, kernel_size=17, padding=8),
                nn.ReLU(True),
                nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1)
            )


    def forward(self, D, B, T):
        # print(D.shape)
        x = T + D - B
        w = self.contrast(x)
        # w = self.rc(w)
        T = x - self.epsilon * self.convs(x + w)
        # T = T + w
        # T = self.conv2_1(torch.cat((w, T),dim = 1))
        return T


class MergeModule_LSTM1(nn.Module):
    def __init__(self,  channel=32, layers=3):
        super(MergeModule_LSTM1, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.BatchNorm2d(channel),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.BatchNorm2d(channel))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.mapping = nn.Sequential(*convs)

    def forward(self, B, T):
        x = B + T
        D = self.mapping(x)
        return D


# #====================================================================================================


class RPCANet_LSTM2(nn.Module):
    def __init__(self, stage_num=6, slayers=6, mlayers=3, channel=32, mode='train'):
        super(RPCANet_LSTM2, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        self.fe = nn.Conv2d(1, channel, 3, padding=1, bias=True)
        for i in range(stage_num):
            self.decos.append(DecompositionModule_LSTM2(slayers=slayers, mlayers=mlayers, channel=channel))
        # 迭代循环初始化参数
        for m in self.modules():
            # 也可以判断是否为conv2d，使用相应的初始化方式
            if isinstance(m, nn.Conv2d):
                nn.init.xavier_normal_(m.weight)
                #nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

    def forward(self, D):
        T = torch.zeros(D.shape).to(D.device)
        [h, c] = [None, None]
        z = self.fe(D - T)
        # B = torch.zeros(D.shape).to(D.device)
        for i in range(self.stage_num):
            D, T, z, h, c = self.decos[i](D, T, z, h, c)
        if self.mode == 'train':
            return D,T
        else:
            return T


class DecompositionModule_LSTM2(nn.Module):
    def __init__(self, slayers=6, mlayers=3, channel=32):
        super(DecompositionModule_LSTM2, self).__init__()
        self.lowrank = LowrankModule_LSTM2(channel=channel)
        self.sparse = SparseModule_LSTM2(channel=channel, layers=slayers)
        self.merge = MergeModule_LSTM2(channel=channel, layers=mlayers)

    def forward(self, D, T, z, h, c):
        B, z, h, c = self.lowrank(D, T, z, h, c)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T, z, h, c


class LowrankModule_LSTM2(nn.Module):
    def __init__(self, channel=32):
        super(LowrankModule_LSTM2, self).__init__()
        self.conv1_C = nn.Sequential(nn.Conv2d(channel + 1, channel, kernel_size=3, padding=1, stride=1),
                         nn.BatchNorm2d(channel),
                         nn.ReLU(True))
        self.RB_1 = ResidualBlock(channel, channel, 3, bias=True, res_scale=1)
        self.RB_2 = ResidualBlock(channel, channel, 3, bias=True, res_scale=1)
        self.convC_1 = nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1)
        self.ConvLSTM = ConvLSTM(channel, channel, 3)

    def forward(self, D, T, z, h, c):
        x = D - T
        x_in = torch.cat([x, z], 1)
        # x_in = x + x_c2
        x_c = self.conv1_C(x_in)
        x_c1 = self.RB_1(x_c)
        x_ct, h, c = self.ConvLSTM(x_c1, h, c)
        x_c2 = self.RB_2(x_ct)
        x_1 = self.convC_1(x_c2)
        B = x + x_1
        return B, x_c2, h, c

class SparseModule_LSTM2(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModule_LSTM2, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)

        self.epsilon = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)
        # self.beta = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)
        self.contrast = nn.Sequential(
                nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                nn.ReLU(True),
                AttnContrastLayer(channel, kernel_size=17, padding=8),
                nn.ReLU(True),
                nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1)
            )


    def forward(self, D, B, T):
        # print(D.shape)
        x = T + D - B
        w = self.contrast(x)
        # w = self.rc(w)
        T = x - self.epsilon * self.convs(x + w)
        # T = T + w
        # T = self.conv2_1(torch.cat((w, T),dim = 1))
        return T


class MergeModule_LSTM2(nn.Module):
    def __init__(self,  channel=32, layers=3):
        super(MergeModule_LSTM2, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.BatchNorm2d(channel),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.BatchNorm2d(channel))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.mapping = nn.Sequential(*convs)

    def forward(self, B, T):
        x = B + T
        D = self.mapping(x)
        return D


# #====================================================================================================

def count_params(model):
    model_parameters = filter(lambda p: p.requires_grad, model.parameters())
    params = sum([np.prod(p.size()) for p in model_parameters])
    return params
# net = LowrankModule(nnseg=True)
# net = SparseModule()
# net = RPCANet()
# net.eval()
# img = torch.zeros((3, 1, 256, 256))
# out = net(img)
# # out = list(out)
#
# print(net)
# # print(out.shape)
#
# params = count_params(net)
# print('Params: {:d}'.format(int(params)))

# for name, para in net.named_parameters():
#     print(name, para.shape)
