自动提取神经网络的中间层特征 并生成热力图
支持 GPU 加速（可选）
支持 .mat 格式（用于进一步分析）
支持 .png 输出（用于可视化）
可直接 import 在 Python 代码或 Jupyter Notebook 里使用

pip install heatmap_generator


快速开始
from heatmap_generator import HeatmapGenerator

# 初始化热力图生成器（加载模型）
heatmap_gen = HeatmapGenerator(model_name="rpcanetma9",model_path="/Users/yourname/My_mission/API/RPCANet_Code/heatmap_package/heatmap_generator/result/20240519T07-24-39_rpcanetma9_nudt/best.pkl", use_cuda=True)

# 生成热力图，保存为 .mat 和 .png
heatmap = heatmap_gen.generate_heatmap(
    img_path="/Users/yourname/My_mission/API/RPCANet_Code/datasets/NUDT-SIRST/test/images/001101.png",
    data_name="NUDT-SIRST_test_images_001101",
    output_mat="/Users/yourname/My_mission/API/RPCANet_Code/heatmap_test_2.20/mat",
    output_png="/Users/yourname/My_mission/API/RPCANet_Code/heatmap_test_2.20/png"
)
