import torch
import torch.nn as nn
import numpy as np
import scipy.io as scio
import cv2
import matplotlib.pyplot as plt
from torch.autograd import Variable
from export import get_model  # 确保 models.py 存在
import os.path as osp
import os

class LayerActivations:
    """ 用于提取特定层的特征图 """
    def __init__(self, model, layer_num=None):
        if layer_num is not None:
            self.hook = model[layer_num].register_forward_hook(self.hook_fn)
        else:
            self.hook = model.register_forward_hook(self.hook_fn)
        self.features = None

    def hook_fn(self, module, input, output):
        self.features = output[0].cpu()

    def remove(self):
        self.hook.remove()


class HeatmapGenerator:
    def __init__(self, model_name,model_path, use_cuda=True):
        """
        初始化热力图生成器

        :param model_path: 预训练模型路径 (.pth)
        :param use_cuda: 是否使用 GPU 计算
        """
        self.device = torch.device("cuda" if use_cuda and torch.cuda.is_available() else "cpu")
        self.model = self.load_model(model_name,model_path)

    def load_model(self, model_name ,model_path):
        """
        加载模型

        :param model_path: 预训练模型路径
        :return: 加载的 PyTorch 模型
        """
        print(f"Loading model from {model_path}...")
        net = get_model(model_name)  # 你可以更改模型架构
        checkpoint = torch.load(model_path, map_location=self.device)
        net.load_state_dict(checkpoint)
        net.to(self.device)
        net.eval()
        print("Model loaded successfully!")
        return net

    def preprocess_image(self, img_path):
        """
        预处理输入图像

        :param img_path: 输入图像路径
        :return: 预处理后的 PyTorch Tensor
        """
        img = cv2.resize(cv2.imread(osp.join(img_path), 0), (256, 256)).astype(int)
   

        img = np.float32(cv2.resize(img, (256, 256))) / 255.
        tmp = img.reshape((1, 1, 256, 256))
        input = torch.from_numpy(tmp)
        return input

    def extract_layer_features(self, input_tensor, layer):
        """
        通过 LayerActivations 提取指定层的特征图

        :param input_tensor: 预处理后的图像 Tensor
        :param layer: 需要提取的模型层
        :return: 该层的输出特征图
        """
        activation_extractor = LayerActivations(layer)
        with torch.no_grad():
            _ = self.model(input_tensor)  # 进行前向传播
        activation_extractor.remove()
        return activation_extractor.features.numpy().squeeze()  # 转换为 numpy 格式

    def generate_heatmap(self, img_path, data_name ,output_mat=None, output_png=None):
        """
        生成热力图并保存

        :param img_path: 输入图像路径
        :param data_name: 测试数据名
        :param output_mat: 输出 .mat 文件路径（可选）
        :param output_png: 输出 .png 文件路径（可选）
        """
        input_tensor = self.preprocess_image(img_path)

        # 提取不同层的特征图
        heatmaps_back = []
        heatmaps_sparse = []
        heatmaps_merge = []
        for i in range(6):  # 提取 6 层的特征
            feature_map_back = self.extract_layer_features(input_tensor, self.model.decos[i].lowrank)
            feature_map_sparse = self.extract_layer_features(input_tensor, self.model.decos[i].sparse)
            feature_map_merge = self.extract_layer_features(input_tensor, self.model.decos[i].merge)
            heatmaps_back.append(feature_map_back)
            heatmaps_sparse.append(feature_map_sparse)
            heatmaps_merge.append(feature_map_merge)
        
        for i in range(6):
            # 取第一层特征作为热力图
            heatmap_back = heatmaps_back[i]
            heatmap_back = np.maximum(heatmap_back, 0)  # ReLU 处理，防止负值
            heatmap_back = np.flipud(heatmap_back)  # 翻转，使方向一致
            heatmap_sparse = heatmaps_sparse[i]
            heatmap_sparse = np.maximum(heatmap_sparse, 0)  # ReLU 处理，防止负值
            heatmap_sparse = np.flipud(heatmap_sparse)  # 翻转，使方向一致
            heatmap_merge = heatmaps_merge[i]
            heatmap_merge = np.maximum(heatmap_merge, 0)  # ReLU 处理，防止负值
            heatmap_merge = np.flipud(heatmap_merge)  # 翻转，使方向一致

            # 保存为 .mat 文件
            if output_mat:
                os.makedirs(osp.join(output_mat,f"{data_name}"), exist_ok= True)
                path_back = osp.join(output_mat,f"{data_name}/back-{i}.mat")
                scio.savemat(path_back, {'back': heatmap_back})

                path_sparse = osp.join(output_mat,f"{data_name}/sparse-{i}.mat")
                scio.savemat(path_sparse, {'sparse': heatmap_sparse})

                path_merge = osp.join(output_mat,f"{data_name}/merge-{i}.mat")
                scio.savemat(path_merge, {'merge': heatmap_merge})
                print(f"Saved heatmap as .mat: {output_mat}")

            # 可视化并保存 .png
            
            if output_png:
                os.makedirs(osp.join(output_png,f"{data_name}"), exist_ok= True)
                plt.figure(figsize=(6, 6))
                plt.pcolor(heatmap_back, cmap='jet', shading='auto')
                plt.axis('off')
                plt.colorbar()
                path_back = osp.join(output_png,f"{data_name}/back-{i}.png")
                plt.savefig(path_back, bbox_inches='tight', pad_inches=0)
                plt.close()
                print(f"Saved heatmap as .png: {path_back}")

                plt.figure(figsize=(6, 6))
                plt.pcolor(heatmap_sparse, cmap='jet', shading='auto')
                plt.axis('off')
                plt.colorbar()
                path_sparse = osp.join(output_png,f"{data_name}/sparse-{i}.png")
                plt.savefig(path_sparse, bbox_inches='tight', pad_inches=0)
                plt.close()
                print(f"Saved heatmap as .png: {path_sparse}")

                plt.figure(figsize=(6, 6))
                plt.pcolor(heatmap_merge, cmap='jet', shading='auto')
                plt.axis('off')
                plt.colorbar()
                path_merge = osp.join(output_png,f"{data_name}/merge-{i}.png")
                plt.savefig(path_merge, bbox_inches='tight', pad_inches=0)
                plt.close()
                print(f"Saved heatmap as .png: {path_merge}")

        
