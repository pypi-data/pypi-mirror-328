import torch
import torch.nn as nn
import torch.nn.functional as F

class SELayer(nn.Module):
    def __init__(self, channels, r=4):
        super(SELayer, self).__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.conv1_c = nn.Conv2d(1, channels, kernel_size=3, padding=1, stride=1)
        self.convc_1 = nn.Conv2d(channels, 1, kernel_size=3, padding=1, stride=1)
        self.fc = nn.Sequential(
            nn.Linear(channels, channels//r, bias=False),  # 全局平均池化 bz,C_out,h,w -> bz,C_out,1,1
            nn.ReLU(),
            nn.Linear(channels // r, channels, bias=False),  # bz,C_out/r,1,1 -> bz,C_out,1,1
            nn.Sigmoid()
        )

    def forward(self, x):
        x = self.conv1_c(x)
        b, c, h, w = x.shape
        y = self.avg_pool(x)
        y = y.view([b, c])
        # print(x.shape)
        # print(y.shape)
        y = self.fc(y)
        y = y.view([b, c, 1, 1])
        out = self.convc_1(x * y.expand_as(x))
        return out


# （1）通道注意力机制
class channel_attention(nn.Module):
    # 初始化, in_channel代表输入特征图的通道数, ratio代表第一个全连接的通道下降倍数
    def __init__(self, in_channel, ratio=4):
        # 继承父类初始化方法
        super(channel_attention, self).__init__()

        # 全局最大池化 [b,c,h,w]==>[b,c,1,1]
        self.max_pool = nn.AdaptiveMaxPool2d(output_size=1)
        # 全局平均池化 [b,c,h,w]==>[b,c,1,1]
        self.avg_pool = nn.AdaptiveAvgPool2d(output_size=1)

        # 第一个全连接层, 通道数下降4倍
        self.fc1 = nn.Linear(in_features=in_channel, out_features=in_channel // ratio, bias=False)
        # 第二个全连接层, 恢复通道数
        self.fc2 = nn.Linear(in_features=in_channel // ratio, out_features=in_channel, bias=False)

        # relu激活函数
        self.relu = nn.ReLU()
        # sigmoid激活函数
        self.sigmoid = nn.Sigmoid()

    # 前向传播
    def forward(self, inputs):
        # 获取输入特征图的shape
        b, c, h, w = inputs.shape

        # 输入图像做全局最大池化 [b,c,h,w]==>[b,c,1,1]
        max_pool = self.max_pool(inputs)
        # 输入图像的全局平均池化 [b,c,h,w]==>[b,c,1,1]
        avg_pool = self.avg_pool(inputs)

        # 调整池化结果的维度 [b,c,1,1]==>[b,c]
        max_pool = max_pool.view([b, c])
        avg_pool = avg_pool.view([b, c])

        # 第一个全连接层下降通道数 [b,c]==>[b,c//4]
        x_maxpool = self.fc1(max_pool)
        x_avgpool = self.fc1(avg_pool)

        # 激活函数
        x_maxpool = self.relu(x_maxpool)
        x_avgpool = self.relu(x_avgpool)

        # 第二个全连接层恢复通道数 [b,c//4]==>[b,c]
        x_maxpool = self.fc2(x_maxpool)
        x_avgpool = self.fc2(x_avgpool)

        # 将这两种池化结果相加 [b,c]==>[b,c]
        x = x_maxpool + x_avgpool
        # sigmoid函数权值归一化
        x = self.sigmoid(x)
        # 调整维度 [b,c]==>[b,c,1,1]
        x = x.view([b, c, 1, 1])
        # 输入特征图和通道权重相乘 [b,c,h,w]
        outputs = inputs * x

        return outputs


# （2）空间注意力机制
class spatial_attention(nn.Module):
    # 初始化，卷积核大小为7*7
    def __init__(self, kernel_size=7):
        # 继承父类初始化方法
        super(spatial_attention, self).__init__()

        # 为了保持卷积前后的特征图shape相同，卷积时需要padding
        padding = kernel_size // 2
        # 7*7卷积融合通道信息 [b,2,h,w]==>[b,1,h,w]
        self.conv = nn.Conv2d(in_channels=2, out_channels=1, kernel_size=kernel_size,
                              padding=padding, bias=False)
        # sigmoid函数
        self.sigmoid = nn.Sigmoid()

    # 前向传播
    def forward(self, inputs):
        # 在通道维度上最大池化 [b,1,h,w]  keepdim保留原有深度
        # 返回值是在某维度的最大值和对应的索引
        x_maxpool, _ = torch.max(inputs, dim=1, keepdim=True)

        # 在通道维度上平均池化 [b,1,h,w]
        x_avgpool = torch.mean(inputs, dim=1, keepdim=True)
        # 池化后的结果在通道维度上堆叠 [b,2,h,w]
        x = torch.cat([x_maxpool, x_avgpool], dim=1)

        # 卷积融合通道信息 [b,2,h,w]==>[b,1,h,w]
        x = self.conv(x)
        # 空间权重归一化
        x = self.sigmoid(x)
        # 输入特征图和空间权重相乘
        outputs = inputs * x
        return outputs


class cbam(nn.Module):
    # 初始化，in_channel和ratio=4代表通道注意力机制的输入通道数和第一个全连接下降的通道数
    # kernel_size代表空间注意力机制的卷积核大小
    def __init__(self, in_channel, ratio=4, kernel_size=7):
        # 继承父类初始化方法
        super(cbam, self).__init__()

        self.conv1_c = nn.Conv2d(1, in_channel, kernel_size=3, padding=1, stride=1)
        self.convc_1 = nn.Conv2d(in_channel, 1, kernel_size=3, padding=1, stride=1)
        # 实例化通道注意力机制
        self.channel_attention = channel_attention(in_channel=in_channel, ratio=ratio)
        # 实例化空间注意力机制
        self.spatial_attention = spatial_attention(kernel_size=kernel_size)

    # 前向传播
    def forward(self, inputs):
        # 先将输入图像经过通道注意力机制
        inputs = self.conv1_c(inputs)

        x = self.channel_attention(inputs)
        # 然后经过空间注意力机制
        x = self.spatial_attention(x)
        x = self.convc_1(x)

        return x


class NonLocalBlock(nn.Module):
    def __init__(self, planes, reduce_ratio=8):
        super(NonLocalBlock, self).__init__()

        self.conv1_c = nn.Conv2d(1, planes, kernel_size=3, padding=1, stride=1)
        self.convc_1 = nn.Conv2d(planes, 1, kernel_size=3, padding=1, stride=1)
        inter_planes = planes // reduce_ratio
        self.query_conv = nn.Conv2d(planes, inter_planes, kernel_size=1)
        self.key_conv = nn.Conv2d(planes, inter_planes, kernel_size=1)
        self.value_conv = nn.Conv2d(planes, planes, kernel_size=1)
        self.gamma = nn.Parameter(torch.zeros(1))

        self.softmax = nn.Softmax(dim=-1)

    def forward(self, x):
        x = self.conv1_c(x)
        m_batchsize, C, height, width = x.size()

        proj_query = self.query_conv(x)
        proj_key = self.key_conv(x)
        proj_value = self.value_conv(x)

        proj_query = proj_query.contiguous().view(m_batchsize, -1, width * height).permute(0, 2, 1)
        proj_key = proj_key.contiguous().view(m_batchsize, -1, width * height)
        energy = torch.bmm(proj_query, proj_key)
        attention = self.softmax(energy)
        proj_value = proj_value.contiguous().view(m_batchsize, -1, width * height)

        out = torch.bmm(proj_value, attention.permute(0, 2, 1))
        out = out.view(m_batchsize, -1, height, width)

        out = self.gamma * out + x
        out = self.convc_1(out)
        return out



class Avg_ChannelAttention_n(nn.Module):
    def __init__(self, channels, r=4):
        super(Avg_ChannelAttention_n, self).__init__()
        self.avg_channel = nn.Sequential(
            nn.AdaptiveAvgPool2d((1, 1)),  # 全局平均池化 bz,C_out,h,w -> bz,C_out,1,1
            nn.Conv2d(channels, channels // r, 1, 1, 0),  # bz,C_out,1,1 -> bz,C_out/r,1,1
            nn.BatchNorm2d(channels // r),
            nn.ReLU(True),
            nn.Conv2d(channels // r, channels, 1, 1, 0),  # bz,C_out/r,1,1 -> bz,C_out,1,1
            nn.BatchNorm2d(channels),
            nn.Sigmoid(),
        )

    def forward(self, x):
        return self.avg_channel(x)



class Avg_ChannelAttention(nn.Module):
    def __init__(self, channels, r=4):
        super(Avg_ChannelAttention, self).__init__()
        self.avg_channel = nn.Sequential(
            nn.AdaptiveAvgPool2d((1, 1)),  # 全局平均池化 bz,C_out,h,w -> bz,C_out,1,1
            nn.Conv2d(channels, channels // r, 1, 1, 0),  # bz,C_out,1,1 -> bz,C_out/r,1,1
            nn.ReLU(True),
            nn.Conv2d(channels // r, channels, 1, 1, 0),  # bz,C_out/r,1,1 -> bz,C_out,1,1
            nn.Sigmoid(),
        )

    def forward(self, x):
        return self.avg_channel(x)


class AttnContrastLayer(nn.Module):
    def __init__(self, channels, kernel_size=3, stride=1, padding=1, dilation=1, groups=1, bias=False):
        super(AttnContrastLayer, self).__init__()
        # 原始普通卷积
        self.conv = nn.Conv2d(channels, channels, kernel_size=kernel_size, stride=stride,
                              padding=padding, dilation=dilation, groups=groups, bias=bias)
        # 用于计算差分系数的全局注意力机制
        self.attn = Avg_ChannelAttention(channels)

    def forward(self, x):
        # 原始k*k滤波（卷积）
        out_normal = self.conv(x)
        # 系数
        theta = self.attn(x)

        # 对k*k滤波器的权重求和，形成1*1滤波器进行滤波
        kernel_w1 = self.conv.weight.sum(2).sum(2)  # 对每一个k*k滤波器的权重求和 C_out,C_in
        # print(kernel_w1.shape)
        kernel_w2 = kernel_w1[:, :, None, None]  # 扩充两个维度 C_out,C_in,1,1
        # print(kernel_w2.shape)
        out_center = F.conv2d(input=x, weight=kernel_w2, bias=self.conv.bias, stride=self.conv.stride,
                              padding=0, groups=self.conv.groups)

        # 将k*k的滤波结果与1*1的滤波结果相减
        return theta * out_center - out_normal


class AttnContrastLayer_n(nn.Module):
    def __init__(self, channels, kernel_size=3, stride=1, padding=1, dilation=1, groups=1, bias=False):
        super(AttnContrastLayer_n, self).__init__()
        # 原始普通卷积
        self.conv = nn.Conv2d(channels, channels, kernel_size=kernel_size, stride=stride,
                              padding=padding, dilation=dilation, groups=groups, bias=bias)
        # 用于计算差分系数的全局注意力机制
        self.attn = Avg_ChannelAttention_n(channels)

    def forward(self, x):
        # 原始k*k滤波（卷积）
        out_normal = self.conv(x)
        # 系数
        theta = self.attn(x)

        # 对k*k滤波器的权重求和，形成1*1滤波器进行滤波
        kernel_w1 = self.conv.weight.sum(2).sum(2)  # 对每一个k*k滤波器的权重求和 C_out,C_in
        # print(kernel_w1.shape)
        kernel_w2 = kernel_w1[:, :, None, None]  # 扩充两个维度 C_out,C_in,1,1
        # print(kernel_w2.shape)
        out_center = F.conv2d(input=x, weight=kernel_w2, bias=self.conv.bias, stride=self.conv.stride,
                              padding=0, groups=self.conv.groups)

        # 将k*k的滤波结果与1*1的滤波结果相减
        return theta * out_center - out_normal

class AttnContrastLayer_d(nn.Module):
    def __init__(self, channels, kernel_size=3, stride=1, padding=1, dilation=2, groups=1, bias=False):
        super(AttnContrastLayer_d, self).__init__()
        # 原始普通卷积
        self.conv = nn.Conv2d(channels, channels, kernel_size=kernel_size, stride=stride,
                              padding=padding, dilation=dilation, groups=groups, bias=bias)
        # 用于计算差分系数的全局注意力机制
        self.attn = Avg_ChannelAttention(channels)

    def forward(self, x):
        # 原始k*k滤波（卷积）
        out_normal = self.conv(x)
        # 系数
        theta = self.attn(x)

        # 对k*k滤波器的权重求和，形成1*1滤波器进行滤波
        kernel_w1 = self.conv.weight.sum(2).sum(2)  # 对每一个k*k滤波器的权重求和 C_out,C_in
        kernel_w2 = kernel_w1[:, :, None, None]  # 扩充两个维度 C_out,C_in,1,1
        out_center = F.conv2d(input=x, weight=kernel_w2, bias=self.conv.bias, stride=self.conv.stride,
                              padding=0, groups=self.conv.groups)

        # 将k*k的滤波结果与1*1的滤波结果相减
        # return theta * out_center - out_normal
        return out_center - theta * out_normal

class AtrousAttnWeight(nn.Module):
    def __init__(self, channels):
        super(AtrousAttnWeight, self).__init__()
        self.attn = Avg_ChannelAttention(channels)

    def forward(self, x):
        return self.attn(x)


