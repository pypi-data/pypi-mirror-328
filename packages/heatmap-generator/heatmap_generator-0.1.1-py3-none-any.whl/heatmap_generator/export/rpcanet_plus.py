import torch
import torch.nn as nn
from einops import rearrange, repeat
from .contrast_and_atrous import AttnContrastLayer, AttnContrastLayer_n, \
    AtrousAttnWeight, AttnContrastLayer_d, SELayer, NonLocalBlock,cbam,SELayer #这里我把CDCLayer改成SE了
import math
import torch.nn.functional as F

import numpy as np

__all__ = ['RPCANet0', 'RPCANet1', 'RPCANet2', 'RPCANet3', 'RPCANet4', 'RPCANet5', 'RPCANet6','RPCANet7','RPCANet8',
           'RPCANet9', 'RPCANet10','RPCANet11', 'RPCANet_Experi', 'RPCANet_wo_Merge', 'RPCANet', 'RNet',
           'RPCANet12', 'RPCANet13','RPCANet14','RPCANet_wo','RPCANetMA','TRPCANet','RPCANetW','RPCANetW1','RPCANetW2',
           'RPCANetW3', 'RPCANetW4', 'RPCANetW5', 'RPCANetMA1',
           'RPCANetMA2','RPCANetMA3','RPCANetMA4','RPCANetMA5','RPCANetMA6','RPCANetMA7','RPCANetMA8','RPCANetMA9','RPCANetMA10',
           'RPCANetMA11','RPCANetMA12',
           'RPCANet_LSTM','RPCANet_LSTM1','RPCANet_LSTM_wop','RPCANet_LSTM_wom',
           'RPCANet_LSTM_TT','RPCANet_LSTM_CT', 'RPCANet_LSTM2',
           'RPCANet_LSTM_2RB','RPCANet_LSTM_2CNN','RPCANet_LSTM_1CNN','RPCANet_LSTM_3CNN',
           'RPCANet_LSTM_9P','RPCANet_LSTM_5P','RPCANet_LSTM_3P','RPCANet_LSTM_CDC','RPCANet_LSTM_CBAM','RPCANet_LSTM_SE']


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


class RPCANet0(nn.Module):
    def __init__(self, stage_num=6):
        super(RPCANet0, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        for _ in range(stage_num):
            self.decos.append(DecompositionModule0())

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


class DecompositionModule0(nn.Module):
    def __init__(self):
        super(DecompositionModule0, self).__init__()
        self.lowrank = LowrankModule0()
        self.sparse = SparseModule0()
        self.merge = MergeModule0()

    def forward(self, D, T):
        B = self.lowrank(D, T)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T



class LowrankModule0(nn.Module):
    def __init__(self, nnseg=True, channel=32, layers=4):
        super(LowrankModule0, self).__init__()
        self.nnseg = nnseg
        if self.nnseg:
            # self.convs = nn.Sequential(
            #     nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
            #     nn.ReLU(True),
            #     nn.MaxPool2d(kernel_size=4, stride=4, padding=0),
            #     nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1),
            #     nn.ReLU(True),
            #     nn.MaxPool2d(kernel_size=4, stride=4, padding=0),
            #     nn.Conv2d(channel, 256, kernel_size=16, padding=0, stride=16),
            # )
            # self.fc = nn.Linear(256, 256)

            convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                     nn.ReLU(True)]
            for i in range(layers):
                convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
                convs.append(nn.ReLU(True))
            convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
            self.convs = nn.Sequential(*convs)

        else:
            self.svt_thre = nn.Parameter(torch.Tensor([0.01]))
        # self.mapping = nn.Conv2d(1, 1, kernel_size=3, padding=1, stride=1)

    def forward(self, D, T):
        B = D - T
        # U, S, Vh = torch.linalg.svd(B, full_matrices=False)
        if self.nnseg:
            # feat = self.convs(B)
            # thre = feat.view(feat.size(0), 1, -1)
            # S = F.relu(S-thre)
            B = B + self.convs(B)
        else:
            # S = F.relu(S-self.svt_thre)
            pass

        # us = torch.matmul(U, torch.diag_embed(S))
        # Bk = torch.matmul(us, Vh)
        return B


class SparseModule0(nn.Module):
    def __init__(self, channel=32, layers=6):
        super(SparseModule0, self).__init__()
        self.rho = nn.Parameter(torch.Tensor([0.01]))
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
               nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)

    def forward(self, D, B, T):
        pre = T + D - B
        out = pre - self.rho * self.convs(pre)
        return out


class MergeModule0(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(MergeModule0, self).__init__()
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


class RPCANet1(nn.Module):
    def __init__(self, stage_num=6):
        super(RPCANet1, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        for _ in range(stage_num):
            self.decos.append(DecompositionModule1())

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


class DecompositionModule1(nn.Module):
    def __init__(self):
        super(DecompositionModule1, self).__init__()
        self.lowrank = LowrankModule1(channel=32, layers=4)
        self.sparse = SparseModule1(channel=32, layers=6)
        self.epsilon = nn.Parameter(torch.Tensor([0.5]), requires_grad=True)

    def forward(self, D, T):
        B = self.lowrank(D, T)
        T = self.sparse(D, B, T)
        D = self.epsilon * D + (1-self.epsilon) * (B + T)
        return D, T


class LowrankModule1(nn.Module):
    def __init__(self, channel=32, layers=4):
        super(LowrankModule1, self).__init__()

        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)
        self.gamma = nn.Parameter(torch.Tensor([0.1]), requires_grad=True)

    def forward(self, D, T):
        B = D - T + self.gamma * self.convs(D - T)
        return B


class SparseModule1(nn.Module):
    def __init__(self, channel=32, layers=6):
        super(SparseModule1, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
               nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)
        self.epsilon = nn.Parameter(torch.Tensor([0.1]), requires_grad=True)

    def forward(self, D, B, T):
        T = 0.5 * (T + D - B) - self.epsilon * self.convs(T + D - B)
        return T


#====================================================================================================


class RPCANet2(nn.Module):
    def __init__(self, stage_num=6):
        super(RPCANet2, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        for _ in range(stage_num):
            self.decos.append(DecompositionModule2())

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


class DecompositionModule2(nn.Module):
    def __init__(self):
        super(DecompositionModule2, self).__init__()
        self.lowrank = LowrankModule2(channel=32, layers=4)
        self.sparse = SparseModule2(channel=32, layers=6)
        self.merge = MergeModule2()

    def forward(self, D, T):
        B = self.lowrank(D, T)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T


class LowrankModule2(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(LowrankModule2, self).__init__()

        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)
        self.gamma = nn.Parameter(torch.Tensor([0.1]), requires_grad=True)

    def forward(self, D, T):
        B = D - T + self.gamma * self.convs(D - T)
        return B


class SparseModule2(nn.Module):
    def __init__(self, channel=32, layers=6):
        super(SparseModule2, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
               nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)
        self.epsilon = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)

    def forward(self, D, B, T):
        T = 0.5 * (T + D - B) - self.epsilon * self.convs(T + D - B)
        return T


class MergeModule2(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(MergeModule2, self).__init__()
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


class RPCANet3(nn.Module):
    def __init__(self, stage_num=6):
        super(RPCANet3, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        for _ in range(stage_num):
            self.decos.append(DecompositionModule3())

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


class DecompositionModule3(nn.Module):
    def __init__(self):
        super(DecompositionModule3, self).__init__()
        self.lowrank = LowrankModule3(channel=32, layers=4)
        self.sparse = SparseModule3(channel=32, layers=6)
        self.merge = MergeModule3()

    def forward(self, D, T):
        B = self.lowrank(D, T)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T


class LowrankModule3(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(LowrankModule3, self).__init__()

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


class SparseModule3(nn.Module):
    def __init__(self, channel=32, layers=6):
        super(SparseModule3, self).__init__()
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


class MergeModule3(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(MergeModule3, self).__init__()
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


class RPCANet4(nn.Module):
    def __init__(self, stage_num=6):
        super(RPCANet4, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        for _ in range(stage_num):
            self.decos.append(DecompositionModule4())

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


class DecompositionModule4(nn.Module):
    def __init__(self):
        super(DecompositionModule4, self).__init__()
        self.lowrank = LowrankModule4(channel=32, layers=4)
        self.sparse = SparseModule4(channel=32, layers=6)
        self.merge = MergeModule4()

    def forward(self, D, T):
        B = self.lowrank(D, T)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T


class LowrankModule4(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(LowrankModule4, self).__init__()

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


class SparseModule4(nn.Module):
    def __init__(self, channel=32, layers=6):
        super(SparseModule4, self).__init__()

        self.up_conv = nn.Sequential(
            nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
            nn.ReLU(True))
        mid_conv = []
        for i in range(layers):
            mid_conv.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            mid_conv.append(nn.ReLU(True))
        self.mid_conv = nn.Sequential(*mid_conv)
        self.down_conv = nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1)

        self.epsilon = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)

    def forward(self, D, B, T):
        # x = T + D - B
        # T = x - self.epsilon * self.convs(x)

        x = T + D - B
        up_in = self.up_conv(x)
        up_out = self.mid_conv(up_in) + up_in
        out = self.down_conv(up_out)
        T = x - self.epsilon * out
        return T


class MergeModule4(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(MergeModule4, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.ReLU(True))
        convs.append(nn.Dropout(0.5))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.mapping = nn.Sequential(*convs)

    def forward(self, B, T):
        return self.mapping(B+T)


#====================================================================================================


class RPCANet5(nn.Module):
    def __init__(self, stage_num=6):
        super(RPCANet5, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        for _ in range(stage_num):
            self.decos.append(DecompositionModule5())

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


class DecompositionModule5(nn.Module):
    def __init__(self):
        super(DecompositionModule5, self).__init__()
        self.lowrank = LowrankModule5(channel=32, layers=4)
        self.sparse = SparseModule5(channel=32, layers=6)
        self.merge = MergeModule5()

    def forward(self, D, T):
        B = self.lowrank(D, T)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T


class LowrankModule5(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(LowrankModule5, self).__init__()

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


class SparseModule5(nn.Module):
    def __init__(self, channel=32, layers=6):
        super(SparseModule5, self).__init__()

        self.up_conv = nn.Sequential(
            nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
            nn.ReLU(True))
        mid_conv = []
        for i in range(layers):
            mid_conv.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            mid_conv.append(nn.ReLU(True))
        self.mid_conv = nn.Sequential(*mid_conv)
        self.down_conv = nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1)

        self.epsilon = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)

    def forward(self, D, B, T):
        # x = T + D - B
        # T = x - self.epsilon * self.convs(x)

        x = T + D - B
        up_in = self.up_conv(x)
        up_out = self.mid_conv(up_in) + up_in
        out = self.down_conv(up_out)
        T = x - self.epsilon * out
        return T


class MergeModule5(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(MergeModule5, self).__init__()
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


class RPCANet6(nn.Module):
    def __init__(self, stage_num=6):
        super(RPCANet6, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        for _ in range(stage_num):
            self.decos.append(DecompositionModule6())

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


class DecompositionModule6(nn.Module):
    def __init__(self):
        super(DecompositionModule6, self).__init__()
        self.lowrank = LowrankModule6(channel=32, layers=3)
        self.sparse = SparseModule6(channel=32, layers=6)
        self.merge = MergeModule6()

    def forward(self, D, T):
        B = self.lowrank(D, T)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T


class LowrankModule6(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(LowrankModule6, self).__init__()

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


class SparseModule6(nn.Module):
    def __init__(self, channel=32, layers=6):
        super(SparseModule6, self).__init__()
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


class MergeModule6(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(MergeModule6, self).__init__()
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







class DecompositionModule(object):
    pass

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
# #====================================================================================================


class RPCANet7(nn.Module):
    def __init__(self, stage_num=6, slayers=6, llayers=3, mlayers=3, channel=32):
        super(RPCANet7, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        for _ in range(stage_num):
            self.decos.append(DecompositionModule7(slayers=slayers, llayers=llayers,
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
        return D, T

class DecompositionModule7(object):
    pass


class DecompositionModule7(nn.Module):
    def __init__(self, slayers=6, llayers=3, mlayers=3, channel=32):
        super(DecompositionModule7, self).__init__()
        self.lowrank = LowrankModule7(channel=channel, layers=llayers)
        self.sparse = SparseModule7(channel=channel, layers=slayers)
        self.merge = MergeModule7(channel=channel, layers=mlayers)

    def forward(self, D, T):
        B = self.lowrank(D, T)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T


class LowrankModule7(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(LowrankModule7, self).__init__()

        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.BatchNorm2d(channel),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.BatchNorm2d(channel))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)
        self.gamma = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)

    def forward(self, D, T):
        x = D - T
        B = x + self.gamma * self.convs(x)
        return B


class SparseModule7(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModule7, self).__init__()
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


class MergeModule7(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(MergeModule7, self).__init__()
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
        return self.mapping(B + T)
# #====================================================================================================
# #====================================================================================================


class RPCANet8(nn.Module):
    def __init__(self, stage_num=9, slayers=6, llayers=3, mlayers=3, channel=32):
        super(RPCANet8, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        for _ in range(stage_num):
            self.decos.append(DecompositionModule8(slayers=slayers, llayers=llayers,
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
        return D, T

class DecompositionModule8(object):
    pass


class DecompositionModule8(nn.Module):
    def __init__(self, slayers=6, llayers=3, mlayers=3, channel=32):
        super(DecompositionModule8, self).__init__()
        self.lowrank = LowrankModule8(channel=channel, layers=llayers)
        self.sparse = SparseModule8(channel=channel, layers=slayers)
        self.merge = MergeModule8(channel=channel, layers=mlayers)

    def forward(self, D, T):
        B = self.lowrank(D, T)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T


class LowrankModule8(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(LowrankModule8, self).__init__()

        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.BatchNorm2d(channel),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.BatchNorm2d(channel))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)
        #self.gamma = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)

    def forward(self, D, T):
        x = D - T
        B = x + self.convs(x)
        return B


class SparseModule8(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModule8, self).__init__()
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


class MergeModule8(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(MergeModule8, self).__init__()
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
        D = x + self.mapping(x)
        #D = self.mapping(x)
        return D
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


class RPCANet10(nn.Module):
    def __init__(self, stage_num=6, slayers=6, mlayers=3, channel=32, mode='train'):
        super(RPCANet10, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for _ in range(stage_num):
            self.decos.append(DecompositionModule10(slayers=slayers,
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

class DecompositionModule10(object):
    pass


class DecompositionModule10(nn.Module):
    def __init__(self, slayers=6, mlayers=3, channel=32):
        super(DecompositionModule10, self).__init__()
        self.lowrank = LowrankModule10(channel=channel)
        self.sparse = SparseModule10(channel=channel, layers=slayers)
        self.merge = MergeModule10(channel=channel, layers=mlayers)

    def forward(self, D, T):
        B = self.lowrank(D, T)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T


class LowrankModule10(nn.Module):
    def __init__(self, channel=32):
        super(LowrankModule10, self).__init__()
        self.channel = channel
        self.relu = nn.ReLU(True)
        self.ext = nn.Sequential(
            nn.Conv2d(1, self.channel, kernel_size=3, padding=1, stride=1),
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

    def forward(self, D, T):
        x = D - T
        ext1 = self.ext(x)
        rb1 = self.relu(ext1+self.res1(ext1))
        rb2 = self.relu(rb1+ self.res1(rb1))
        rec = self.relu(self.rec(rb2))
        B = rec
        return B

class SparseModule10(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModule10, self).__init__()
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


class MergeModule10(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(MergeModule10, self).__init__()
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


class RPCANet11(nn.Module):
    def __init__(self, stage_num=6, slayers=6, mlayers=3, channel=32, mode='train'):
        super(RPCANet11, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for _ in range(stage_num):
            self.decos.append(DecompositionModule11(slayers=slayers,
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

class DecompositionModule11(object):
    pass


class DecompositionModule11(nn.Module):
    def __init__(self, slayers=6, mlayers=3, channel=32):
        super(DecompositionModule11, self).__init__()
        self.lowrank = LowrankModule11(channel=channel)
        self.sparse = SparseModule11(channel=channel, layers=slayers)
        self.merge = MergeModule11(channel=channel, layers=mlayers)

    def forward(self, D, T):
        B = self.lowrank(D, T)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T


class LowrankModule11(nn.Module):
    def __init__(self, channel=32):
        super(LowrankModule11, self).__init__()
        self.channel = channel
        self.relu = nn.ReLU(True)
        self.ext = nn.Sequential(
            nn.Conv2d(1, self.channel, kernel_size=3, padding=1, stride=1),
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

    def forward(self, D, T):
        x = D - T
        ext1 = self.ext(x)
        rb1 = self.relu(ext1+self.res1(ext1))
        rb2 = self.relu(rb1+ self.res1(rb1))
        rec = self.relu(self.rec(rb2))
        B = rec
        return B

class SparseModule11(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModule11, self).__init__()
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


class MergeModule11(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(MergeModule11, self).__init__()
        self.channel = channel
        self.relu = nn.ReLU(True)
        self.ext = nn.Sequential(
            nn.Conv2d(1, self.channel, kernel_size=3, padding=1, stride=1),
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

    def forward(self, B, T):
        x = B + T
        ext1 = self.relu(self.ext(x))
        rb1 = self.relu(ext1 + self.res1(ext1))
        rb2 = self.relu(rb1 + self.res1(rb1))
        D = self.rec(rb2)
        # D = x + rec
        return D

# #====================================================================================================


class RPCANet12(nn.Module):
    def __init__(self, stage_num=6, slayers=6, llayers=3, mlayers=3, channel=32, mode='train'):
        super(RPCANet12, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for _ in range(stage_num):
            self.decos.append(DecompositionModule12(slayers=slayers, llayers=llayers,
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

class DecompositionModule12(object):
    pass


class DecompositionModule12(nn.Module):
    def __init__(self, slayers=6, llayers=3, mlayers=3, channel=32):
        super(DecompositionModule12, self).__init__()
        self.lowrank = LowrankModule12(channel=channel, layers=llayers)
        self.sparse = SparseModule12(channel=channel, layers=slayers)
        self.merge = MergeModule12(channel=channel, layers=mlayers)

    def forward(self, D, T):
        B = self.lowrank(D, T)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T


class LowrankModule12(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(LowrankModule12, self).__init__()

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
        B = self.convs(x)
        return B


class SparseModule12(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModule12, self).__init__()
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
        T = x - self.epsilon * self.convs(T)
        return T


class MergeModule12(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(MergeModule12, self).__init__()
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


class RPCANet13(nn.Module):
    def __init__(self, stage_num=6, llayers=3, slayers=6, channel=32, mode='train'):
        super(RPCANet13, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for _ in range(stage_num):
            self.decos.append(DecompositionModule13(slayers=slayers, llayers = llayers,
                                                channel=channel))
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

class DecompositionModule13(object):
    pass


class DecompositionModule13(nn.Module):
    def __init__(self, slayers=6, llayers=3, channel=32):
        super(DecompositionModule13, self).__init__()
        self.lowrank = LowrankModule13(channel=channel,layers=llayers)
        self.sparse = SparseModule13(channel=channel, layers=slayers)
        self.merge = MergeModule13(channel=channel)

    def forward(self, D, T):
        B = self.lowrank(D, T)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T


class LowrankModule13(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(LowrankModule13, self).__init__()
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


class SparseModule13(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModule13, self).__init__()
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


class MergeModule13(nn.Module):
    def __init__(self, channel=32):
        super(MergeModule13, self).__init__()
        self.channel = channel
        self.relu = nn.ReLU(True)
        self.ext = nn.Sequential(
            nn.Conv2d(1, self.channel, kernel_size=3, padding=1, stride=1),
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

    def forward(self, B, T):
        x = B + T
        ext1 = self.relu(self.ext(x))
        rb1 = self.relu(ext1 + self.res1(ext1))
        rb2 = self.relu(rb1 + self.res1(rb1))
        D = self.rec(rb2)
        # D = x + rec
        return D


class RPCANet14(nn.Module):
    def __init__(self, stage_num=6, slayers=6, llayers=3, mlayers=3, channel=32, mode='train'):
        super(RPCANet14, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for _ in range(stage_num):
            self.decos.append(DecompositionModule14(slayers=slayers, llayers=llayers,
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

class DecompositionModule14(object):
    pass


class DecompositionModule14(nn.Module):
    def __init__(self, slayers=6, llayers=3, mlayers=3, channel=32):
        super(DecompositionModule14, self).__init__()
        self.lowrank = LowrankModule14(channel=channel, layers=llayers)
        self.sparse = SparseModule14(channel=channel, layers=slayers)
        self.merge = MergeModule14(channel=channel, layers=mlayers)

    def forward(self, D, T):
        B = self.lowrank(D, T)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T


class LowrankModule14(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(LowrankModule14, self).__init__()

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


class SparseModule14(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModule14, self).__init__()
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
        T = x - self.epsilon * self.convs(T)
        return T


class MergeModule14(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(MergeModule14, self).__init__()
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
# #====================================================================================================


class RPCANetMA1(nn.Module):
    def __init__(self, stage_num=6, slayers=6, llayers=3, mlayers=3, channel=32, mode='train'):
        super(RPCANetMA1, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for i in range(stage_num):
            self.decos.append(DecompositionModuleMA1(slayers=slayers, llayers=llayers,
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


class DecompositionModuleMA1(nn.Module):
    def __init__(self, slayers=6, llayers=3, mlayers=3, channel=32):
        super(DecompositionModuleMA1, self).__init__()
        self.lowrank = LowrankModuleMA1(channel=channel, layers=llayers)
        self.sparse = SparseModuleMA1( channel=channel, layers=slayers)
        self.merge = MergeModuleMA1(channel=channel, layers=mlayers)

    def forward(self, D, T):
        B = self.lowrank(D, T)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T


class LowrankModuleMA1(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(LowrankModuleMA1, self).__init__()

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


class SparseModuleMA1(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModuleMA1, self).__init__()
        convs = [nn.Conv2d(2, channel, kernel_size=3, padding=1, stride=1),
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
        T = x - self.epsilon * self.convs(torch.cat((x, T), dim=1))
        return T


class MergeModuleMA1(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(MergeModuleMA1, self).__init__()
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


# #====================================================================================================


class RPCANetMA2(nn.Module):
    def __init__(self, stage_num=6, slayers=6, llayers=3, mlayers=3, channel=32, mode='train'):
        super(RPCANetMA2, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for i in range(stage_num):
            self.decos.append(DecompositionModuleMA2(stage_num=i+1, slayers=slayers, llayers=llayers,
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

class DecompositionModuleMA2(object):
    pass


class DecompositionModuleMA2(nn.Module):
    def __init__(self, stage_num, slayers=6, llayers=3, mlayers=3, channel=32):
        super(DecompositionModuleMA2, self).__init__()
        self.lowrank = LowrankModuleMA2(channel=channel, layers=llayers)
        self.sparse = SparseModuleMA2(stage_num=stage_num, channel=channel, layers=slayers)
        self.merge = MergeModuleMA2(channel=channel, layers=mlayers)

    def forward(self, D, T, feats):
        B = self.lowrank(D, T)
        T = self.sparse(D, B, T, feats)
        D = self.merge(B, T)
        return D, T


class LowrankModuleMA2(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(LowrankModuleMA2, self).__init__()

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


class SparseModuleMA2(nn.Module):
    def __init__(self, stage_num, channel=32, layers=6) -> object:
        super(SparseModuleMA2, self).__init__()
        convs = [nn.Conv2d(stage_num+1, channel, kernel_size=3, padding=1, stride=1),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)
        self.contrast = nn.Sequential(
            nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
            nn.ReLU(True),
            AttnContrastLayer(channel, kernel_size=17, padding=8),
            nn.BatchNorm2d(channel),
            nn.LeakyReLU(0.1, inplace=True),
            nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1)
        )
        self.epsilon = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)

    def forward(self, D, B, T, feats):
        # print(D.shape)
        x = T + D - B
        w = self.contrast(x)
        T = x - self.epsilon * self.convs(torch.cat((x + w, feats), dim=1))
        return T


class MergeModuleMA2(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(MergeModuleMA2, self).__init__()
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


# #====================================================================================================


class RPCANetMA3(nn.Module):
    def __init__(self, stage_num=6, slayers=6, llayers=3, mlayers=3, channel=32, mode='train'):
        super(RPCANetMA3, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for i in range(stage_num):
            self.decos.append(DecompositionModuleMA3(stage_num=i+1, slayers=slayers, llayers=llayers,
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
        feats = D
        for i in range(self.stage_num):
            D, T = self.decos[i](D, T, feats)
            feats = torch.cat((feats, D), dim=1)
        if self.mode == 'train':
            return D,T
        else:
            return T


class DecompositionModuleMA3(nn.Module):
    def __init__(self, stage_num, slayers=6, llayers=3, mlayers=3, channel=32):
        super(DecompositionModuleMA3, self).__init__()
        self.lowrank = LowrankModuleMA3(channel=channel, layers=llayers)
        self.sparse = SparseModuleMA3(channel=channel, layers=slayers)
        self.merge = MergeModuleMA3(stage_num=stage_num, channel=channel, layers=mlayers)

    def forward(self, D, T, feats):
        B = self.lowrank(D, T)
        T = self.sparse(D, B, T)
        D = self.merge(B, T, feats)
        return D, T


class LowrankModuleMA3(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(LowrankModuleMA3, self).__init__()

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


class SparseModuleMA3(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModuleMA3, self).__init__()
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


class MergeModuleMA3(nn.Module):
    def __init__(self, stage_num, channel=32, layers=3):
        super(MergeModuleMA3, self).__init__()
        convs = [nn.Conv2d(stage_num+1, channel, kernel_size=3, padding=1, stride=1),
                 nn.BatchNorm2d(channel),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.BatchNorm2d(channel))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.mapping = nn.Sequential(*convs)

    def forward(self, B, T,feats):
        x = B + T
        acc = torch.cat((x,feats),dim=1)
        D = self.mapping(acc)
        return D

# #====================================================================================================





class RPCANetMA4(nn.Module):
    def __init__(self, stage_num=6, slayers=6, llayers=3, mlayers=3, channel=32, mode='train'):
        super(RPCANetMA4, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for i in range(stage_num):
            self.decos.append(DecompositionModuleMA4(slayers=slayers, llayers=llayers,
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
        feats = D
        for i in range(self.stage_num):
            D, T = self.decos[i](D, T, feats)
            feats = D
        if self.mode == 'train':
            return D,T
        else:
            return T


class DecompositionModuleMA4(nn.Module):
    def __init__(self, slayers=6, llayers=3, mlayers=3, channel=32):
        super(DecompositionModuleMA4, self).__init__()
        self.lowrank = LowrankModuleMA4(channel=channel, layers=llayers)
        self.sparse = SparseModuleMA4(channel=channel, layers=slayers)
        self.merge = MergeModuleMA4(channel=channel, layers=mlayers)

    def forward(self, D, T, feats):
        B = self.lowrank(D, T)
        T = self.sparse(D, B, T)
        D = self.merge(B, T, feats)
        return D, T


class LowrankModuleMA4(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(LowrankModuleMA4, self).__init__()

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


class SparseModuleMA4(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModuleMA4, self).__init__()
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


class MergeModuleMA4(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(MergeModuleMA4, self).__init__()
        convs = [nn.Conv2d(2, channel, kernel_size=3, padding=1, stride=1),
                 nn.BatchNorm2d(channel),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.BatchNorm2d(channel))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.mapping = nn.Sequential(*convs)

    def forward(self, B, T,feats):
        x = B + T
        acc = torch.cat((x,feats),dim=1)
        D = self.mapping(acc)
        return D


# #====================================================================================================


class RPCANetMA5(nn.Module):
    def __init__(self, stage_num=6, slayers=6, llayers=3, mlayers=3, channel=32, mode='train'):
        super(RPCANetMA5, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for i in range(stage_num):
            self.decos.append(DecompositionModuleMA5(stage_num=i+1, slayers=slayers, llayers=llayers,
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
        feats = D
        for i in range(self.stage_num):
            D, T = self.decos[i](D, T, feats)
            feats = torch.cat((feats, D), dim=1)
        if self.mode == 'train':
            return D,T
        else:
            return T


class DecompositionModuleMA5(nn.Module):
    def __init__(self, stage_num, slayers=6, llayers=3, mlayers=3, channel=32):
        super(DecompositionModuleMA5, self).__init__()
        self.lowrank = LowrankModuleMA5(channel=channel, layers=llayers)
        self.sparse = SparseModuleMA5(channel=channel, layers=slayers)
        self.merge = MergeModuleMA5(stage_num=stage_num, channel=channel, layers=mlayers)

    def forward(self, D, T, feats):
        B = self.lowrank(D, T)
        T = self.sparse(D, B, T)
        D = self.merge(B, T, feats)
        return D, T


class LowrankModuleMA5(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(LowrankModuleMA5, self).__init__()

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


class SparseModuleMA5(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModuleMA5, self).__init__()
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


class MergeModuleMA5(nn.Module):
    def __init__(self, stage_num, channel=32, layers=3):
        super(MergeModuleMA5, self).__init__()
        convs = [nn.Conv2d(stage_num+1, channel, kernel_size=3, padding=1, stride=1),
                 nn.BatchNorm2d(channel),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.BatchNorm2d(channel))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.mapping = nn.Sequential(*convs)

    def forward(self, B, T,feats):
        x = B + T
        acc = torch.cat((x,feats),dim=1)
        D = self.mapping(acc)
        return D


# #====================================================================================================


class RPCANetMA6(nn.Module):
    def __init__(self, stage_num=6, slayers=6, llayers=3, mlayers=3, channel=32, mode='train'):
        super(RPCANetMA6, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for i in range(stage_num):
            self.decos.append(DecompositionModuleMA6(stage_num=i+1, slayers=slayers, llayers=llayers,
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
        feats = D
        for i in range(self.stage_num):
            D, T = self.decos[i](D, T, feats)
            feats = torch.cat((feats, D), dim=1)
        if self.mode == 'train':
            return D,T
        else:
            return T


class DecompositionModuleMA6(nn.Module):
    def __init__(self, stage_num, slayers=6, llayers=3, mlayers=3, channel=32):
        super(DecompositionModuleMA6, self).__init__()
        self.lowrank = LowrankModuleMA6(channel=channel, layers=llayers)
        self.sparse = SparseModuleMA6(channel=channel, layers=slayers)
        self.merge = MergeModuleMA6(stage_num=stage_num, channel=channel, layers=mlayers)

    def forward(self, D, T, feats):
        B = self.lowrank(D, T)
        T = self.sparse(D, B, T)
        D = self.merge(B, T, feats)
        return D, T


class LowrankModuleMA6(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(LowrankModuleMA6, self).__init__()

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


class SparseModuleMA6(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModuleMA6, self).__init__()
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


class MergeModuleMA6(nn.Module):
    def __init__(self, stage_num, channel=32, layers=3):
        super(MergeModuleMA6, self).__init__()
        convs = [nn.Conv2d(stage_num+1, channel, kernel_size=3, padding=1, stride=1),
                 nn.BatchNorm2d(channel),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.BatchNorm2d(channel))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.mapping = nn.Sequential(*convs)

    def forward(self, B, T,feats):
        x = B + T
        acc = torch.cat((x,feats),dim=1)
        D = self.mapping(acc)
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

        # class LowrankModuleMA9(nn.Module):
#     def __init__(self, stage_num, channel=32):
#         super(LowrankModuleMA9, self).__init__()
    #     self.channel = channel
    #     self.relu = nn.ReLU(True)
    #     self.ext = nn.Sequential(
    #         nn.Conv2d(stage_num+1, self.channel, kernel_size=3, padding=1, stride=1),
    #         nn.BatchNorm2d(self.channel),
    #         nn.ReLU(True)
    #     )
    #     self.res1 = nn.Sequential(
    #         nn.Conv2d(self.channel, self.channel, kernel_size=3, padding=1, stride=1),
    #         nn.BatchNorm2d(self.channel),
    #         nn.ReLU(True),
    #         nn.Conv2d(self.channel, self.channel, kernel_size=3, padding=1, stride=1),
    #         nn.BatchNorm2d(self.channel),
    #     )
    #     self.res2 = nn.Sequential(
    #         nn.Conv2d(self.channel, self.channel, kernel_size=3, padding=1, stride=1),
    #         nn.BatchNorm2d(self.channel),
    #         nn.ReLU(True),
    #         nn.Conv2d(self.channel, self.channel, kernel_size=3, padding=1, stride=1),
    #         nn.BatchNorm2d(self.channel),
    #     )
    #     self.rec = nn.Sequential(
    #         nn.Conv2d(self.channel, 1, kernel_size=3, padding=1, stride=1),
    #     )
    #     #self.relu = nn.ReLU()
    #     #self.gamma = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)
    #
    # def forward(self, D, T, feats):
    #     x = D - T
    #     acc = torch.cat((x, feats), dim=1)
    #     ext1 = self.ext(acc)
    #     rb1 = self.relu(ext1 + self.res1(ext1))
    #     rb2 = self.relu(rb1 + self.res1(rb1))
    #     rec = self.relu(self.rec(rb2))
    #     B = x  + rec
    #     return B



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


class RPCANet_LSTM(nn.Module):
    def __init__(self, stage_num=6, slayers=6, mlayers=3, channel=32, mode='train'):
        super(RPCANet_LSTM, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for i in range(stage_num):
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

class DecompositionModule_LSTM(nn.Module):
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

class SparseModule_LSTM(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModule_LSTM, self).__init__()
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




class RPCANet_LSTM_wop(nn.Module):
    def __init__(self, stage_num=6, slayers=6, mlayers=3, channel=32, mode='train'):
        super(RPCANet_LSTM_wop, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for i in range(stage_num):
            self.decos.append(DecompositionModule_LSTM_wop(slayers=slayers, mlayers=mlayers, channel=channel))
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


class DecompositionModule_LSTM_wop(nn.Module):
    def __init__(self, slayers=6, mlayers=3, channel=32):
        super(DecompositionModule_LSTM_wop, self).__init__()
        self.lowrank = LowrankModule_LSTM_wop(channel=channel)
        self.sparse = SparseModule_LSTM_wop(channel=channel, layers=slayers)
        self.merge = MergeModule_LSTM_wop(channel=channel, layers=mlayers)

    def forward(self, D, T, h, c):
        B, h, c = self.lowrank(D, T, h, c)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T, h, c


class LowrankModule_LSTM_wop(nn.Module):
    def __init__(self, channel=32):
        super(LowrankModule_LSTM_wop, self).__init__()
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

class SparseModule_LSTM_wop(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModule_LSTM_wop, self).__init__()
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
        # w = self.rc(w)
        T = x - self.epsilon * self.convs(x)
        # T = T + w
        # T = self.conv2_1(torch.cat((w, T),dim = 1))
        return T


class MergeModule_LSTM_wop(nn.Module):
    def __init__(self,  channel=32, layers=3):
        super(MergeModule_LSTM_wop, self).__init__()
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





class RPCANet_LSTM_wom(nn.Module):
    def __init__(self, stage_num=6, slayers=6, llayers=3, mlayers=3, channel=32, mode='train'):
        super(RPCANet_LSTM_wom, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for _ in range(stage_num):
            self.decos.append(DecompositionModule_LSTM_wom(slayers=slayers, llayers=llayers,
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


class DecompositionModule_LSTM_wom(nn.Module):
    def __init__(self, slayers=6, llayers=3, mlayers=3, channel=32):
        super(DecompositionModule_LSTM_wom, self).__init__()
        self.lowrank = LowrankModule_LSTM_wom(channel=channel, layers=llayers)
        self.sparse = SparseModule_LSTM_wom(channel=channel, layers=slayers)
        self.merge = MergeModule_LSTM_wom(channel=channel, layers=mlayers)

    def forward(self, D, T):
        B = self.lowrank(D, T)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T


class LowrankModule_LSTM_wom(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(LowrankModule_LSTM_wom, self).__init__()

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


class SparseModule_LSTM_wom(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModule_LSTM_wom, self).__init__()
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


class MergeModule_LSTM_wom(nn.Module):
    def __init__(self,  channel=32, layers=3):
        super(MergeModule_LSTM_wom, self).__init__()
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



class RPCANet_LSTM_TT(nn.Module):
    def __init__(self, stage_num=6, slayers=6, llayers=4, mlayers=3, channel=32, mode='train'):
        super(RPCANet_LSTM_TT, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for i in range(stage_num):
            self.decos.append(DecompositionModule_LSTM_TT(slayers=slayers, mlayers=mlayers,
                                                          llayers=llayers, channel=channel))
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
        B = D
        # B = torch.zeros(D.shape).to(D.device)
        for i in range(self.stage_num):
            D, T, B = self.decos[i](D, T, B)
        if self.mode == 'train':
            return D,T
        else:
            return T


class DecompositionModule_LSTM_TT(nn.Module):
    def __init__(self, slayers=6, llayers=4, mlayers=3, channel=32):
        super(DecompositionModule_LSTM_TT, self).__init__()
        self.lowrank = LowrankModule_LSTM_TT(channel=channel, layers = llayers)
        self.sparse = SparseModule_LSTM_TT(channel=channel, layers=slayers)
        self.merge = MergeModule_LSTM_TT(channel=channel, layers=mlayers)

    def forward(self, D, T, B):
        B = self.lowrank(D, T, B)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T, B


class LowrankModule_LSTM_TT(nn.Module):
    def __init__(self, channel = 32,layers = 6):
        super(LowrankModule_LSTM_TT, self).__init__()
        convs = [nn.Conv2d(2, channel, kernel_size=3, padding=1, stride=1),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)

    def forward(self, D, B, T):
        # print(D.shape)
        x = D - T
        x_B = self.convs(torch.cat((x, B), dim=1))
        B = x + x_B
        return B

class SparseModule_LSTM_TT(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModule_LSTM_TT, self).__init__()
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


class MergeModule_LSTM_TT(nn.Module):
    def __init__(self,  channel=32, layers=3):
        super(MergeModule_LSTM_TT, self).__init__()
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




class RPCANet_LSTM_CT(nn.Module):
    def __init__(self, stage_num=6, slayers=6, llayers=4, mlayers=3, channel=32, mode='train'):
        super(RPCANet_LSTM_CT, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for i in range(stage_num):
            self.decos.append(DecompositionModule_LSTM_CT(stage_num=i+1, slayers=slayers, llayers= llayers,
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


class DecompositionModule_LSTM_CT(nn.Module):
    def __init__(self, stage_num, slayers=6, llayers=6,  mlayers=3, channel=32):
        super(DecompositionModule_LSTM_CT, self).__init__()
        self.lowrank = LowrankModule_LSTM_CT(stage_num=stage_num, channel=channel,layers = llayers)
        self.sparse = SparseModule_LSTM_CT(channel=channel, layers=slayers)
        self.merge = MergeModule_LSTM_CT(channel=channel, layers=mlayers)

    def forward(self, D, T, feats):
        B = self.lowrank(D, T, feats)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T, B

class LowrankModule_LSTM_CT(nn.Module):
    def __init__(self, stage_num, channel=32, layers=3):
        super(LowrankModule_LSTM_CT, self).__init__()
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

class SparseModule_LSTM_CT(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModule_LSTM_CT, self).__init__()
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


class MergeModule_LSTM_CT(nn.Module):
    def __init__(self,  channel=32, layers=3):
        super(MergeModule_LSTM_CT, self).__init__()
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




class RPCANet_LSTM_2RB(nn.Module):
    def __init__(self, stage_num=6, slayers=6, mlayers=3, channel=32, mode='train'):
        super(RPCANet_LSTM_2RB, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for i in range(stage_num):
            self.decos.append(DecompositionModule_LSTM_2RB(slayers=slayers, mlayers=mlayers, channel=channel))
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




class DecompositionModule_LSTM_2RB(nn.Module):
    def __init__(self, slayers=6, mlayers=3, channel=32):
        super(DecompositionModule_LSTM_2RB, self).__init__()
        self.lowrank = LowrankModule_LSTM_2RB(channel=channel)
        self.sparse = SparseModule_LSTM_2RB(channel=channel, layers=slayers)
        self.merge = MergeModule_LSTM_2RB(channel=channel, layers=mlayers)

    def forward(self, D, T, h, c):
        B, h, c = self.lowrank(D, T, h, c)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T, h, c


class LowrankModule_LSTM_2RB(nn.Module):
    def __init__(self, channel=32):
        super(LowrankModule_LSTM_2RB, self).__init__()
        self.conv1_C = nn.Sequential(nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                         nn.BatchNorm2d(channel),
                         nn.ReLU(True))
        self.RB_1 = ResidualBlock(channel, channel, 3, bias=True, res_scale=1)
        self.RB_2 = ResidualBlock(channel, channel, 3, bias=True, res_scale=1)
        self.RB_3 = ResidualBlock(channel, channel, 3, bias=True, res_scale=1)
        self.RB_4 = ResidualBlock(channel, channel, 3, bias=True, res_scale=1)
        self.convC_1 = nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1)
        self.ConvLSTM = ConvLSTM(channel, channel, 3)

    def forward(self, D, T, h, c):
        x = D - T
        x_c = self.conv1_C(x)
        x_c1 = self.RB_1(x_c)
        x_c2 = self.RB_2(x_c1)
        x_ct, h, c = self.ConvLSTM(x_c1, h, c)
        x_c3 = self.RB_3(x_ct)
        x_c4 = self.RB_4(x_c3)
        x_1 = self.convC_1(x_c4)
        B = x + x_1
        return B, h, c

class SparseModule_LSTM_2RB(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModule_LSTM_2RB, self).__init__()
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


class MergeModule_LSTM_2RB(nn.Module):
    def __init__(self,  channel=32, layers=3):
        super(MergeModule_LSTM_2RB, self).__init__()
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


class RPCANet_LSTM_1CNN(nn.Module):
    def __init__(self, stage_num=6, slayers=6, mlayers=3, channel=32, mode='train'):
        super(RPCANet_LSTM_1CNN, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for i in range(stage_num):
            self.decos.append(DecompositionModule_LSTM_1CNN(slayers=slayers, mlayers=mlayers, channel=channel))
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




class DecompositionModule_LSTM_1CNN(nn.Module):
    def __init__(self, slayers=6, mlayers=3, channel=32):
        super(DecompositionModule_LSTM_1CNN, self).__init__()
        self.lowrank = LowrankModule_LSTM_1CNN(channel=channel)
        self.sparse = SparseModule_LSTM_1CNN(channel=channel, layers=slayers)
        self.merge = MergeModule_LSTM_1CNN(channel=channel, layers=mlayers)

    def forward(self, D, T, h, c):
        B, h, c = self.lowrank(D, T, h, c)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T, h, c


class LowrankModule_LSTM_1CNN(nn.Module):
    def __init__(self, channel=32):
        super(LowrankModule_LSTM_1CNN, self).__init__()
        self.conv1_C = nn.Sequential(nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                         nn.BatchNorm2d(channel),
                         nn.ReLU(True))

        self.convC_C_1 = nn.Sequential(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1),
                         nn.BatchNorm2d(channel),
                         nn.ReLU(True))

        self.convC_C_2 = nn.Sequential(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1),
                                       nn.BatchNorm2d(channel),
                                       nn.ReLU(True))

        self.convC_1 = nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1)
        self.ConvLSTM = ConvLSTM(channel, channel, 3)

    def forward(self, D, T, h, c):
        x = D - T
        x_c = self.conv1_C(x)
        x_c1 = self.convC_C_1(x_c)
        x_ct, h, c = self.ConvLSTM(x_c1, h, c)
        x_c2 = self.convC_C_2(x_ct)
        x_1 = self.convC_1(x_c2)
        B = x + x_1
        return B, h, c

class SparseModule_LSTM_1CNN(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModule_LSTM_1CNN, self).__init__()
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


class MergeModule_LSTM_1CNN(nn.Module):
    def __init__(self,  channel=32, layers=3):
        super(MergeModule_LSTM_1CNN, self).__init__()
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


class RPCANet_LSTM_2CNN(nn.Module):
    def __init__(self, stage_num=6, slayers=6, mlayers=3, channel=32, mode='train'):
        super(RPCANet_LSTM_2CNN, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for i in range(stage_num):
            self.decos.append(DecompositionModule_LSTM_2CNN(slayers=slayers, mlayers=mlayers, channel=channel))
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
        [h, c] = [None, None]
        # B = torch.zeros(D.shape).to(D.device)
        for i in range(self.stage_num):
            D, T, h, c = self.decos[i](D, T, h, c)
        if self.mode == 'train':
            return D, T
        else:
            return T


class DecompositionModule_LSTM_2CNN(nn.Module):
    def __init__(self, slayers=6, mlayers=3, channel=32):
        super(DecompositionModule_LSTM_2CNN, self).__init__()
        self.lowrank = LowrankModule_LSTM_2CNN(channel=channel)
        self.sparse = SparseModule_LSTM_2CNN(channel=channel, layers=slayers)
        self.merge = MergeModule_LSTM_2CNN(channel=channel, layers=mlayers)

    def forward(self, D, T, h, c):
        B, h, c = self.lowrank(D, T, h, c)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T, h, c


class LowrankModule_LSTM_2CNN(nn.Module):
    def __init__(self, channel=32):
        super(LowrankModule_LSTM_2CNN, self).__init__()
        self.conv1_C = nn.Sequential(nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                                     nn.BatchNorm2d(channel),
                                     nn.ReLU(True)
                                     )

        self.convC_C_1 = nn.Sequential(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1),
                                       nn.BatchNorm2d(channel),
                                       nn.ReLU(True),
                                       nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1),
                                       nn.BatchNorm2d(channel),
                                       nn.ReLU(True)
                                       )

        self.convC_C_2 = nn.Sequential(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1),
                                       nn.BatchNorm2d(channel),
                                       nn.ReLU(True),
                                       nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1),
                                       nn.BatchNorm2d(channel),
                                       nn.ReLU(True)
                                       )

        self.convC_1 = nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1)
        self.ConvLSTM = ConvLSTM(channel, channel, 3)

    def forward(self, D, T, h, c):
        x = D - T
        x_c = self.conv1_C(x)
        x_c1 = self.convC_C_1(x_c)
        x_ct, h, c = self.ConvLSTM(x_c1, h, c)
        x_c2 = self.convC_C_2(x_ct)
        x_1 = self.convC_1(x_c2)
        B = x + x_1
        return B, h, c


class SparseModule_LSTM_2CNN(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModule_LSTM_2CNN, self).__init__()
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


class MergeModule_LSTM_2CNN(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(MergeModule_LSTM_2CNN, self).__init__()
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



class RPCANet_LSTM_3CNN(nn.Module):
    def __init__(self, stage_num=6, slayers=6, mlayers=3, channel=32, mode='train'):
        super(RPCANet_LSTM_3CNN, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for i in range(stage_num):
            self.decos.append(DecompositionModule_LSTM_3CNN(slayers=slayers, mlayers=mlayers, channel=channel))
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
        [h, c] = [None, None]
        # B = torch.zeros(D.shape).to(D.device)
        for i in range(self.stage_num):
            D, T, h, c = self.decos[i](D, T, h, c)
        if self.mode == 'train':
            return D, T
        else:
            return T


class DecompositionModule_LSTM_3CNN(nn.Module):
    def __init__(self, slayers=6, mlayers=3, channel=32):
        super(DecompositionModule_LSTM_3CNN, self).__init__()
        self.lowrank = LowrankModule_LSTM_3CNN(channel=channel)
        self.sparse = SparseModule_LSTM_3CNN(channel=channel, layers=slayers)
        self.merge = MergeModule_LSTM_3CNN(channel=channel, layers=mlayers)

    def forward(self, D, T, h, c):
        B, h, c = self.lowrank(D, T, h, c)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T, h, c


class LowrankModule_LSTM_3CNN(nn.Module):
    def __init__(self, channel=32):
        super(LowrankModule_LSTM_3CNN, self).__init__()
        self.conv1_C = nn.Sequential(nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                                     nn.BatchNorm2d(channel),
                                     nn.ReLU(True)
                                     )

        self.convC_C_1 = nn.Sequential(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1),
                                       nn.BatchNorm2d(channel),
                                       nn.ReLU(True),
                                       nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1),
                                       nn.BatchNorm2d(channel),
                                       nn.ReLU(True),
                                       nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1),
                                       nn.BatchNorm2d(channel),
                                       nn.ReLU(True)
                                       )

        self.convC_C_2 = nn.Sequential(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1),
                                       nn.BatchNorm2d(channel),
                                       nn.ReLU(True),
                                       nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1),
                                       nn.BatchNorm2d(channel),
                                       nn.ReLU(True),
                                       nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1),
                                       nn.BatchNorm2d(channel),
                                       nn.ReLU(True)
                                       )

        self.convC_1 = nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1)
        self.ConvLSTM = ConvLSTM(channel, channel, 3)

    def forward(self, D, T, h, c):
        x = D - T
        x_c = self.conv1_C(x)
        x_c1 = self.convC_C_1(x_c)
        x_ct, h, c = self.ConvLSTM(x_c1, h, c)
        x_c2 = self.convC_C_2(x_ct)
        x_1 = self.convC_1(x_c2)
        B = x + x_1
        return B, h, c


class SparseModule_LSTM_3CNN(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModule_LSTM_3CNN, self).__init__()
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


class MergeModule_LSTM_3CNN(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(MergeModule_LSTM_3CNN, self).__init__()
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






class RPCANet_LSTM_9P(nn.Module):
    def __init__(self, stage_num=6, slayers=6, mlayers=3, channel=32, mode='train'):
        super(RPCANet_LSTM_9P, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for i in range(stage_num):
            self.decos.append(DecompositionModule_LSTM_9P(slayers=slayers, mlayers=mlayers, channel=channel))
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




class DecompositionModule_LSTM_9P(nn.Module):
    def __init__(self, slayers=6, mlayers=3, channel=32):
        super(DecompositionModule_LSTM_9P, self).__init__()
        self.lowrank = LowrankModule_LSTM_9P(channel=channel)
        self.sparse = SparseModule_LSTM_9P(channel=channel, layers=slayers)
        self.merge = MergeModule_LSTM_9P(channel=channel, layers=mlayers)

    def forward(self, D, T, h, c):
        B, h, c = self.lowrank(D, T, h, c)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T, h, c


class LowrankModule_LSTM_9P(nn.Module):
    def __init__(self, channel=32):
        super(LowrankModule_LSTM_9P, self).__init__()
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

class SparseModule_LSTM_9P(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModule_LSTM_9P, self).__init__()
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
                AttnContrastLayer_n(channel, kernel_size=9, padding=4),
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


class MergeModule_LSTM_9P(nn.Module):
    def __init__(self,  channel=32, layers=3):
        super(MergeModule_LSTM_9P, self).__init__()
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


class RPCANet_LSTM_5P(nn.Module):
    def __init__(self, stage_num=6, slayers=6, mlayers=3, channel=32, mode='train'):
        super(RPCANet_LSTM_5P, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for i in range(stage_num):
            self.decos.append(DecompositionModule_LSTM_5P(slayers=slayers, mlayers=mlayers, channel=channel))
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




class DecompositionModule_LSTM_5P(nn.Module):
    def __init__(self, slayers=6, mlayers=3, channel=32):
        super(DecompositionModule_LSTM_5P, self).__init__()
        self.lowrank = LowrankModule_LSTM_5P(channel=channel)
        self.sparse = SparseModule_LSTM_5P(channel=channel, layers=slayers)
        self.merge = MergeModule_LSTM_5P(channel=channel, layers=mlayers)

    def forward(self, D, T, h, c):
        B, h, c = self.lowrank(D, T, h, c)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T, h, c


class LowrankModule_LSTM_5P(nn.Module):
    def __init__(self, channel=32):
        super(LowrankModule_LSTM_5P, self).__init__()
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

class SparseModule_LSTM_5P(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModule_LSTM_5P, self).__init__()
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
                AttnContrastLayer_n(channel, kernel_size=5, padding=2),
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


class MergeModule_LSTM_5P(nn.Module):
    def __init__(self,  channel=32, layers=3):
        super(MergeModule_LSTM_5P, self).__init__()
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


class RPCANet_LSTM_3P(nn.Module):
    def __init__(self, stage_num=6, slayers=6, mlayers=3, channel=32, mode='train'):
        super(RPCANet_LSTM_3P, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for i in range(stage_num):
            self.decos.append(DecompositionModule_LSTM_3P(slayers=slayers, mlayers=mlayers, channel=channel))
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




class DecompositionModule_LSTM_3P(nn.Module):
    def __init__(self, slayers=6, mlayers=3, channel=32):
        super(DecompositionModule_LSTM_3P, self).__init__()
        self.lowrank = LowrankModule_LSTM_3P(channel=channel)
        self.sparse = SparseModule_LSTM_3P(channel=channel, layers=slayers)
        self.merge = MergeModule_LSTM_3P(channel=channel, layers=mlayers)

    def forward(self, D, T, h, c):
        B, h, c = self.lowrank(D, T, h, c)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T, h, c


class LowrankModule_LSTM_3P(nn.Module):
    def __init__(self, channel=32):
        super(LowrankModule_LSTM_3P, self).__init__()
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

class SparseModule_LSTM_3P(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModule_LSTM_3P, self).__init__()
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
                AttnContrastLayer_n(channel, kernel_size=3, padding=1),
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


class MergeModule_LSTM_3P(nn.Module):
    def __init__(self,  channel=32, layers=3):
        super(MergeModule_LSTM_3P, self).__init__()
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


class RPCANet_LSTM_CDC(nn.Module):
    def __init__(self, stage_num=6, slayers=6, mlayers=3, channel=32, mode='train'):
        super(RPCANet_LSTM_CDC, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for i in range(stage_num):
            self.decos.append(DecompositionModule_LSTM_CDC(slayers=slayers, mlayers=mlayers, channel=channel))
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


class DecompositionModule_LSTM_CDC(nn.Module):
    def __init__(self, slayers=6, mlayers=3, channel=32):
        super(DecompositionModule_LSTM_CDC, self).__init__()
        self.lowrank = LowrankModule_LSTM_CDC(channel=channel)
        self.sparse = SparseModule_LSTM_CDC(channel=channel, layers=slayers)
        self.merge = MergeModule_LSTM_CDC(channel=channel, layers=mlayers)

    def forward(self, D, T, h, c):
        B, h, c = self.lowrank(D, T, h, c)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T, h, c


class LowrankModule_LSTM_CDC(nn.Module):
    def __init__(self, channel=32):
        super(LowrankModule_LSTM_CDC, self).__init__()
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

class SparseModule_LSTM_CDC(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModule_LSTM_CDC, self).__init__()
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
                CDCLayer(channel, kernel_size=17, padding=8),
                nn.ReLU(True),
                nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1)
            )


    def forward(self, D, B, T):
        # print(D.shape)
        x = T + D - B
        w = self.contrast(x)
        T = x - self.epsilon * self.convs(x+w)
        # T = T + w
        # T = self.conv2_1(torch.cat((w, T),dim = 1))
        return T


class MergeModule_LSTM_CDC(nn.Module):
    def __init__(self,  channel=32, layers=3):
        super(MergeModule_LSTM_CDC, self).__init__()
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


class RPCANet_LSTM_CBAM(nn.Module):
    def __init__(self, stage_num=6, slayers=6, mlayers=3, channel=32, mode='train'):
        super(RPCANet_LSTM_CBAM, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for i in range(stage_num):
            self.decos.append(DecompositionModule_LSTM_CBAM(slayers=slayers, mlayers=mlayers, channel=channel))
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


class DecompositionModule_LSTM_CBAM(nn.Module):
    def __init__(self, slayers=6, mlayers=3, channel=32):
        super(DecompositionModule_LSTM_CBAM, self).__init__()
        self.lowrank = LowrankModule_LSTM_CBAM(channel=channel)
        self.sparse = SparseModule_LSTM_CBAM(channel=channel, layers=slayers)
        self.merge = MergeModule_LSTM_CBAM(channel=channel, layers=mlayers)

    def forward(self, D, T, h, c):
        B, h, c = self.lowrank(D, T, h, c)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T, h, c


class LowrankModule_LSTM_CBAM(nn.Module):
    def __init__(self, channel=32):
        super(LowrankModule_LSTM_CBAM, self).__init__()
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

class SparseModule_LSTM_CBAM(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModule_LSTM_CBAM, self).__init__()
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


class MergeModule_LSTM_CBAM(nn.Module):
    def __init__(self,  channel=32, layers=3):
        super(MergeModule_LSTM_CBAM, self).__init__()
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


class RPCANet_LSTM_SE(nn.Module):
    def __init__(self, stage_num=6, slayers=6, mlayers=3, channel=32, mode='train'):
        super(RPCANet_LSTM_SE, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for i in range(stage_num):
            self.decos.append(DecompositionModule_LSTM_SE(slayers=slayers, mlayers=mlayers, channel=channel))
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


class DecompositionModule_LSTM_SE(nn.Module):
    def __init__(self, slayers=6, mlayers=3, channel=32):
        super(DecompositionModule_LSTM_SE, self).__init__()
        self.lowrank = LowrankModule_LSTM_SE(channel=channel)
        self.sparse = SparseModule_LSTM_SE(channel=channel, layers=slayers)
        self.merge = MergeModule_LSTM_SE(channel=channel, layers=mlayers)

    def forward(self, D, T, h, c):
        B, h, c = self.lowrank(D, T, h, c)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T, h, c


class LowrankModule_LSTM_SE(nn.Module):
    def __init__(self, channel=32):
        super(LowrankModule_LSTM_SE, self).__init__()
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

class SparseModule_LSTM_SE(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModule_LSTM_SE, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)

        self.epsilon = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)
        self.beta = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)

        self.se = SELayer(channels=channel)

    def forward(self, D, B, T):
        # print(D.shape)
        x = T + D - B
        w = self.se(x)
        T = x - self.epsilon * self.convs(x + w)
        # T = T + w
        # T = self.conv2_1(torch.cat((w, T),dim = 1))
        return T

class MergeModule_LSTM_SE(nn.Module):
    def __init__(self,  channel=32, layers=3):
        super(MergeModule_LSTM_SE, self).__init__()
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




class RPCANetW(nn.Module):
    def __init__(self, stage_num=6, slayers=6, llayers=3, mlayers=3, channel=32, mode='train'):
        super(RPCANetW, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for _ in range(stage_num):
            self.decos.append(DecompositionModuleW(slayers=slayers, llayers=llayers,
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

class DecompositionModuleW(object):
    pass


class DecompositionModuleW(nn.Module):
    def __init__(self, slayers=6, llayers=3, mlayers=3, channel=32):
        super(DecompositionModuleW, self).__init__()
        self.lowrank = LowrankModuleW(channel=channel, layers=llayers)
        self.sparse = SparseModuleW(channel=channel, layers=slayers)
        self.merge = MergeModuleW(channel=channel, layers=mlayers)

    def forward(self, D, T):
        B = self.lowrank(D, T)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T


class LowrankModuleW(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(LowrankModuleW, self).__init__()

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


class SparseModuleW(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModuleW, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)

        self.epsilon = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)
        self.beta = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)

        self.contrast = nn.Sequential(
                nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                nn.ReLU(True),
                AttnContrastLayer(channel, kernel_size=17, padding=8),
                nn.BatchNorm2d(channel),
                nn.LeakyReLU(0.1, inplace=True),
                nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1)
            )
        self.conv2_1 = nn.Sequential(nn.Conv2d(2, 1, kernel_size=3, padding=1, stride=1),
                 nn.ReLU(True))

    def forward(self, D, B, T):
        # print(D.shape)
        x = T + D - B
        w = self.beta * self.contrast(x)
        T = x - self.epsilon * self.convs(x + w)
        # T = T + w
        # T = self.conv2_1(torch.cat((w, T),dim = 1))
        return T


class MergeModuleW(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(MergeModuleW, self).__init__()
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
# #====================================================================================================


class RPCANetW1(nn.Module):
    def __init__(self, stage_num=6, slayers=6, llayers=3, mlayers=3, channel=32, mode='train'):
        super(RPCANetW1, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for _ in range(stage_num):
            self.decos.append(DecompositionModuleW1(slayers=slayers, llayers=llayers,
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

class DecompositionModuleW1(object):
    pass

class DecompositionModuleW1(nn.Module):
    def __init__(self, slayers=6, llayers=3, mlayers=3, channel=32):
        super(DecompositionModuleW1, self).__init__()
        self.lowrank = LowrankModuleW1(channel=channel, layers=llayers)
        self.sparse = SparseModuleW1(channel=channel, layers=slayers)
        self.merge = MergeModuleW1(channel=channel, layers=mlayers)

    def forward(self, D, T):
        B = self.lowrank(D, T)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T

class LowrankModuleW1(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(LowrankModuleW1, self).__init__()

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

class SparseModuleW1(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModuleW1, self).__init__()
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
                nn.BatchNorm2d(channel),
                nn.LeakyReLU(0.1, inplace=True),
                nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1)
            )

        self.conv2_1 = nn.Sequential(nn.Conv2d(2, 1, kernel_size=3, padding=1, stride=1),
                 nn.ReLU(True))

    def forward(self, D, B, T):
        # print(D.shape)
        x = T + D - B
        w = self.contrast(x)
        T = x - self.epsilon * self.convs(x + w)
        # T = T + w
        # T = self.conv2_1(torch.cat((w, T),dim = 1))
        return T

class MergeModuleW1(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(MergeModuleW1, self).__init__()
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

# #====================================================================================================


class RPCANetW2(nn.Module):
    def __init__(self, stage_num=6, slayers=6, llayers=3, mlayers=3, channel=32, mode='train'):
        super(RPCANetW2, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for _ in range(stage_num):
            self.decos.append(DecompositionModuleW2(slayers=slayers, llayers=llayers,
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

class DecompositionModuleW2(object):
    pass

class DecompositionModuleW2(nn.Module):
    def __init__(self, slayers=6, llayers=3, mlayers=3, channel=32):
        super(DecompositionModuleW2, self).__init__()
        self.lowrank = LowrankModuleW2(channel=channel, layers=llayers)
        self.sparse = SparseModuleW2(channel=channel, layers=slayers)
        self.merge = MergeModuleW2(channel=channel, layers=mlayers)

    def forward(self, D, T):
        B = self.lowrank(D, T)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T

class LowrankModuleW2(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(LowrankModuleW2, self).__init__()

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

class SparseModuleW2(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModuleW2, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)

        self.epsilon = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)
        self.beta = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)

        self.contrast = nn.Sequential(
                nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                nn.ReLU(True),
                AttnContrastLayer(channel, kernel_size=17, padding=8),
                nn.BatchNorm2d(channel),
                nn.LeakyReLU(0.1, inplace=True),
                nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1)
            )
        self.conv2_1 = nn.Sequential(nn.Conv2d(2, 1, kernel_size=3, padding=1, stride=1),
                 nn.ReLU(True))

    def forward(self, D, B, T):
        # print(D.shape)
        x = T + D - B
        w = self.beta * torch.linalg.pinv(x)
        T = x - self.epsilon * self.convs(x + self.conv2_1(torch.cat((w, T),dim = 1)))
        # T = T + w
        # T = self.conv2_1(torch.cat((w, T),dim = 1))
        return T

class MergeModuleW2(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(MergeModuleW2, self).__init__()
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

# #====================================================================================================


class RPCANetW3(nn.Module):
    def __init__(self, stage_num=6, slayers=6, llayers=3, mlayers=3, channel=32, mode='train'):
        super(RPCANetW3, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for _ in range(stage_num):
            self.decos.append(DecompositionModuleW3(slayers=slayers, llayers=llayers,
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

class DecompositionModuleW3(object):
    pass

class DecompositionModuleW3(nn.Module):
    def __init__(self, slayers=6, llayers=3, mlayers=3, channel=32):
        super(DecompositionModuleW3, self).__init__()
        self.lowrank = LowrankModuleW3(channel=channel, layers=llayers)
        self.sparse = SparseModuleW3(channel=channel, layers=slayers)
        self.merge = MergeModuleW3(channel=channel, layers=mlayers)

    def forward(self, D, T):
        B = self.lowrank(D, T)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T

class LowrankModuleW3(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(LowrankModuleW3, self).__init__()

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

class SparseModuleW3(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModuleW3, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)

        self.epsilon = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)
        self.beta = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)

        self.contrast = nn.Sequential(
                nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                nn.ReLU(True),
                AttnContrastLayer(channel, kernel_size=17, padding=8),
                nn.BatchNorm2d(channel),
                nn.LeakyReLU(0.1, inplace=True),
                nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1)
            )
        self.conv2_1 = nn.Sequential(nn.Conv2d(2, 1, kernel_size=3, padding=1, stride=1),
                 nn.ReLU(True))

    def forward(self, D, B, T):
        # print(D.shape)
        x = T + D - B
        w = self.beta * torch.linalg.pinv(x)
        T = x - self.epsilon * self.convs(self.conv2_1(torch.cat((w, T),dim = 1)))
        # T = T + w
        # T = self.conv2_1(torch.cat((w, T),dim = 1))
        return T

class MergeModuleW3(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(MergeModuleW3, self).__init__()
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
# #====================================================================================================


class RPCANetW4(nn.Module):
    def __init__(self, stage_num=6, slayers=6, llayers=3, mlayers=3, channel=32, mode='train'):
        super(RPCANetW4, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for _ in range(stage_num):
            self.decos.append(DecompositionModuleW4(slayers=slayers, llayers=llayers,
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

class DecompositionModuleW4(object):
    pass

class DecompositionModuleW4(nn.Module):
    def __init__(self, slayers=6, llayers=3, mlayers=3, channel=32):
        super(DecompositionModuleW4, self).__init__()
        self.lowrank = LowrankModuleW4(channel=channel, layers=llayers)
        self.sparse = SparseModuleW4(channel=channel, layers=slayers)
        self.merge = MergeModuleW4(channel=channel, layers=mlayers)

    def forward(self, D, T):
        B = self.lowrank(D, T)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T

class LowrankModuleW4(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(LowrankModuleW4, self).__init__()

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

class SparseModuleW4(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModuleW4, self).__init__()
        convs = [nn.Conv2d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv2d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv2d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)

        self.epsilon = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)
        self.beta = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)

        self.se = SELayer(channels=channel)

    def forward(self, D, B, T):
        # print(D.shape)
        x = T + D - B
        w = self.se(x)
        T = x - self.epsilon * self.convs(x + w)
        # T = T + w
        # T = self.conv2_1(torch.cat((w, T),dim = 1))
        return T

class MergeModuleW4(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(MergeModuleW4, self).__init__()
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

# #====================================================================================================


class RPCANetW5(nn.Module):
    def __init__(self, stage_num=6, slayers=6, llayers=3, mlayers=3, channel=32, mode='train'):
        super(RPCANetW5, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        self.mode = mode
        for _ in range(stage_num):
            self.decos.append(DecompositionModuleW5(slayers=slayers, llayers=llayers,
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

class DecompositionModuleW5(object):
    pass

class DecompositionModuleW5(nn.Module):
    def __init__(self, slayers=6, llayers=3, mlayers=3, channel=32):
        super(DecompositionModuleW5, self).__init__()
        self.lowrank = LowrankModuleW5(channel=channel, layers=llayers)
        self.sparse = SparseModuleW5(channel=channel, layers=slayers)
        self.merge = MergeModuleW5(channel=channel, layers=mlayers)

    def forward(self, D, T):
        B = self.lowrank(D, T)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T

class LowrankModuleW5(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(LowrankModuleW5, self).__init__()

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

class SparseModuleW5(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModuleW5, self).__init__()
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

class MergeModuleW5(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(MergeModuleW5, self).__init__()
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


# #====================================================================================================
class TRPCANet(nn.Module):
    def __init__(self, stage_num=6, slayers=6, llayers=3, mlayers=3, channel=32):
        super(TRPCANet, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        for _ in range(stage_num):
            self.decos.append(DecompositionModuleT(slayers=slayers, llayers=llayers,
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


class DecompositionModuleT(object):
    pass


class DecompositionModuleT(nn.Module):
    def __init__(self, slayers=6, llayers=4, mlayers=3, channel=32):
        super(DecompositionModuleT, self).__init__()
        self.lowrank = LowrankModuleT(channel=channel, layers=llayers)
        self.sparse = SparseModuleT(channel=channel, layers=slayers)
        self.merge = MergeModuleT(channel=channel, layers=mlayers)

    def forward(self, D, T):
        # print(D.shape)
        # print(T.shape)
        tenD = D.reshape(D.shape[0], 16, 64, 64)
        tenT = T.reshape(T.shape[0], 16, 64, 64)
        tenD = torch.unsqueeze(tenD, 1)
        tenT = torch.unsqueeze(tenT, 1)
        # print(tenD.shape)
        # print(tenT.shape)
        tenB = self.lowrank(tenD, tenT)
        tenT = self.sparse(tenD, tenB, tenT)
        tenD = self.merge(tenB, tenT)
        tenD = torch.squeeze(tenD, 1)
        tenT = torch.squeeze(tenT, 1)
        D = tenD.reshape(D.shape[0], 1, 256, 256)
        T = tenT.reshape(T.shape[0], 1, 256, 256)
        return D, T



class LowrankModuleT(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(LowrankModuleT, self).__init__()

        convs = [nn.Conv3d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.BatchNorm3d(channel),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv3d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.BatchNorm3d(channel))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv3d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)

    def forward(self, tenD, tenT):
        tenx = tenD - tenT
        tenB = tenx + self.convs(tenx)
        return tenB


class SparseModuleT(nn.Module):
    def __init__(self, channel=32, layers=6) -> object:
        super(SparseModuleT, self).__init__()
        convs = [nn.Conv3d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv3d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv3d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.convs = nn.Sequential(*convs)
        self.epsilon = nn.Parameter(torch.Tensor([0.01]), requires_grad=True)

    def forward(self, tenD, tenB, tenT):
        tenx = tenT + tenD - tenB
        tenT = tenx - self.epsilon * self.convs(tenx)
        return tenT


class MergeModuleT(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(MergeModuleT, self).__init__()
        convs = [nn.Conv3d(1, channel, kernel_size=3, padding=1, stride=1),
                 nn.BatchNorm3d(channel),
                 nn.ReLU(True)]
        for i in range(layers):
            convs.append(nn.Conv3d(channel, channel, kernel_size=3, padding=1, stride=1))
            convs.append(nn.BatchNorm3d(channel))
            convs.append(nn.ReLU(True))
        convs.append(nn.Conv3d(channel, 1, kernel_size=3, padding=1, stride=1))
        self.mapping = nn.Sequential(*convs)

    def forward(self, tenB, tenT):
        return self.mapping(tenB+tenT)





class RNet(nn.Module):
    def __init__(self, stage_num=15, slayers=6, rank=8, mlayers=3, channel=32):
        super(RNet, self).__init__()
        self.stage_num = stage_num
        self.decos = nn.ModuleList()
        for _ in range(stage_num):
            self.decos.append(DModule(slayers=slayers, rank=rank, mlayers=mlayers, channel=channel))

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
        return D, T


class DModule(object):
    pass


class DModule(nn.Module):
    def __init__(self, slayers=6, rank=8, mlayers=3, channel=32):
        super(DModule, self).__init__()
        self.lrank = LRModule(channel=channel, rank=rank)
        self.sparse = SparseModule(channel=channel, layers=slayers)
        self.merge = MergeModule(channel=channel, layers=mlayers)

    def forward(self, D, T):
        B = self.lrank(D, T)
        T = self.sparse(D, B, T)
        D = self.merge(B, T)
        return D, T


class LRModule(nn.Module):
    def __init__(self, rank, channel=32):
        super(LRModule, self).__init__()
        self.rank = rank
        self.channel = channel
        # self.first_stage = first_stage
        self.lr_base = nn.Sequential(
            nn.Conv2d(1, channel, kernel_size=3, stride=1, padding=1),
            nn.ReLU(True),
        )
        # if not first_stage:
        #     self.lr_combine = nn.Sequential(
        #         nn.Conv2d(channels, channels, kernel_size=1, stride=1, padding=0),
        #         nn.ReLU(True),
        #     )
        self.lr_pool1 = nn.Sequential(
            nn.AdaptiveAvgPool2d((256, rank)),
            nn.Conv2d(channel, channel, kernel_size=1, stride=1, padding=0),
            nn.ReLU(True),
            nn.Conv2d(channel, 1, kernel_size=1, stride=1, padding=0),
            nn.ReLU(True),
        )
        self.lr_pool2 = nn.Sequential(
            nn.AdaptiveAvgPool2d((rank, 256)),
            nn.Conv2d(channel, channel, kernel_size=1, stride=1, padding=0),
            nn.ReLU(True),
            nn.Conv2d(channel, 1, kernel_size=1, stride=1, padding=0),
            nn.ReLU(True),
        )

    def forward(self, D, T):
        x = D - T
        b, c, hei, wid = D.shape
        hc, wc = hei // 256, wid // 256

        # update L
        B = self.lr_base(x)

        tmp = rearrange(B, 'b c (h hc) (w wc) -> (b hc wc) c h w', h=256, w=256)
        B = torch.matmul(self.lr_pool1(tmp), self.lr_pool2(tmp))
        B = rearrange(B, '(b hc wc) c h w -> b c (h hc) (w wc)', h=256, w=256, hc=hc, wc=wc)


        return B


class SModule(nn.Module):
    def __init__(self, channel=32, layers=6):
        super(SModule, self).__init__()
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


class MModule(nn.Module):
    def __init__(self, channel=32, layers=3):
        super(MModule, self).__init__()
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
#         self.sparse = SparseModule(channel=channel, layers=slayers)
#         self.merge = MergeModule(channel=channel, layers=mlayers)
#
#     def forward(self, D, T):
#         print(D.shape)
#         d_t = gen_patch_ten(D, 30, 30)
#         print(d_t.shape)
#         n1 = d_t.shape[0]
#         n2 = d_t.shape[1]
#         n3 = d_t.shape[2]
#         B_T = self.lowrank1()
#         B = res_patch_ten(B_T, 30, 30)
#
#         #B = self.lowrank(D, T)
#         T = self.sparse(D, B, T)
#         D = self.merge(B, T)
#         return D, T
# class LowRankt(nn.Module):
#
#     def __init__(self, n_1=30, n_2=30, n_3=81):
#         super(LowRankt, self).__init__()
#         self.A_hat = nn.Parameter(torch.Tensor(n_3, n_1, n_2))
#         self.B_hat = nn.Parameter(torch.Tensor(n_3, n_2, n_2))
#
#         self.net = nn.Sequential(permute_change(1, 2, 0),
#                                  nn.Linear(int(n_3), int(n_3), bias=False),
#                                  nn.LeakyReLU(),
#                                  nn.Linear(int(n_3), n_3, bias=False))
#
#         self.reset_parameters()
#
#     def reset_parameters(self):
#         stdv = 1. / math.sqrt(self.A_hat.size(0))
#         self.A_hat.data.uniform_(-stdv, stdv)
#         self.B_hat.data.uniform_(-stdv, stdv)
#
#     def forward(self):
#         x = torch.matmul(self.A_hat, self.B_hat)
#         return self.net(x)
#
#
# def gen_patch_ten(im, patchSize, slideStep):
#     #from skimage import color
#     #from skimage import io
#     #from array import array
#
#     img = np.squeeze(im[0])
#
#     imgHei = 256;
#     imgWid = 256;
#     #if im.shape[2] == 3:
#     #    img = color.rgb2gray(im)
#     #else:
#     #img = im;
#     rowPatchNum = math.ceil((imgHei - patchSize) / slideStep) + 1;
#     colPatchNum = math.ceil((imgWid - patchSize) / slideStep) + 1;
#     print(rowPatchNum);
#     print(colPatchNum);
#
#     rowPosArr = []
#     colPosArr = []
#     for i in range(1, rowPatchNum):
#         tmprow = 1 + (i - 1) * slideStep;
#         rowPosArr.append(tmprow);
#     rowPosArr.append(imgHei - patchSize + 1);
#     print(rowPosArr)
#
#     for i in range(1, colPatchNum):
#         tmpcol = 1 + (i - 1) * slideStep;
#         colPosArr.append(tmpcol);
#
#     colPosArr.append(imgWid - patchSize + 1);
#     print(colPosArr)
#
#     x = np.zeros((patchSize, patchSize, rowPatchNum * colPatchNum));
#     print(x.shape);
#     k = 0;
#     for col in colPosArr:
#         for row in rowPosArr:
#             tmp_patch = img[row - 1: row + patchSize - 1, col - 1: col + patchSize - 1];
#             x[:, :, k] = tmp_patch.cuda().data.cpu();
#             k = k + 1;
#     return x;
#
#
# def res_patch_ten(patchTen, patchSize, slideStep):
#     #from skimage import color
#     #from skimage import io
#     #from array import array
#     imgHei = 256;
#     imgWid = 256;
#     #print(im.shape[2]);
#     #if im.shape[2] == 3:
#     #    img = color.rgb2gray(im);
#     #else:
#      # img = im;
#     rowPatchNum = math.ceil((imgHei - patchSize) / slideStep) + 1;
#     colPatchNum = math.ceil((imgWid - patchSize) / slideStep) + 1;
#     print(rowPatchNum);
#     print(colPatchNum);
#
#     rowPosArr = []
#     colPosArr = []
#     for i in range(1, rowPatchNum):
#         tmprow = 1 + (i - 1) * slideStep;
#         rowPosArr.append(tmprow);
#     rowPosArr.append(imgHei - patchSize + 1);
#     print(rowPosArr)
#
#     for i in range(1, colPatchNum):
#         tmpcol = 1 + (i - 1) * slideStep;
#         colPosArr.append(tmpcol);
#
#     colPosArr.append(imgWid - patchSize + 1);
#     accImg = np.zeros((imgHei, imgWid));
#     weiImg = np.zeros((imgHei, imgWid));
#     onesMat = np.ones((patchSize, patchSize));
#     k = 0;
#     for col in colPosArr:
#         for row in rowPosArr:
#             tmp_patch = np.squeeze(patchTen[:, :, k]);
#             accImg[row - 1: row + patchSize - 1, col - 1: col + patchSize - 1] = tmp_patch.cuda().data.cpu();
#             weiImg[row - 1: row + patchSize - 1, col - 1: col + patchSize - 1] = onesMat;
#             k = k + 1;
#     recImg = accImg / weiImg;
#     print(recImg.shape)
#     rest = torch.from_numpy(recImg)
#     res = torch.unsqueeze(torch.unsqueeze(rest, 1),1)
#
#     device = torch.device('cuda:0')
#     res = res.type(torch.FloatTensor).to(device)
#
#     return res;
#
#
# class permute_change(nn.Module):
#     def __init__(self, n1, n2, n3):
#         super(permute_change, self).__init__()
#         self.n1 = n1
#         self.n2 = n2
#         self.n3 = n3
#
#     def forward(self, x):
#         x = x.permute(self.n1, self.n2, self.n3)
#         return x
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
