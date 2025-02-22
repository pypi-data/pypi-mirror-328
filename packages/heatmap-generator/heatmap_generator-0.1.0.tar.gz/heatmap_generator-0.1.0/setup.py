from setuptools import setup, find_packages

setup(
    name="heatmap_generator",  # 包名称
    version="0.1.0",  # 版本号
    author="Fengyi_Wu",
    author_email="your_email@example.com",
    description="A Python package to generate heatmaps from deep learning models.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your_github/heatmap_generator",  # 你的 GitHub 主页
    packages=find_packages(),
    install_requires=[
        "torch",
        "torchvision",
        "numpy",
        "scipy",
        "opencv-python",
        "matplotlib",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
