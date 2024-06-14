import matplotlib.pyplot as plt
import numpy as np
from adjustText import adjust_text

# 数据
labels = ['GCL-YOLO-S', 'YOLOv7-Tiny', 'YOLOv8-S', 'PicoDet-L', 'YOLOX-Tiny',
          'YOLOv5-S', 'Nanodet-Plus-M-1.5x', 'YOLOv5-N', 'YOLOv4-Tiny',
          'YOLOv3-Tiny', 'YOLOv5-Lite-G', 'DS3FN']

params = [1.64, 6.03, 11.10, 3.30, 5.04, 7.04, 2.44, 1.77, 5.89, 8.68, 5.39, 2.77]
# map_50 = [39.6, 36.8, 39.2, 34.2, 31.3, 32.7, 30.4, 26.4, 19.5, 15.9, 27.3, 45.5]
map_50 = [31.6, 31.2, 31.9, 31.1, 29.1, 29.8, 27.9, 29.5, 27.7, 26.9, 27.6, 36.2]

colors = ['red', 'gray', 'yellow', 'purple', 'green', 'blue',
          'orange', 'pink', 'brown', 'gold', 'cyan', 'magenta']
marker = '*'

fig, ax = plt.subplots()

# 绘制散点图
stars = [plt.scatter(p, m, s=100, c=c, marker=marker) for p, m, c in zip(params, map_50, colors)]

# 创建文本注释对象
texts = []
for i in range(len(labels)):
    txt = ax.annotate(labels[i], (params[i], map_50[i]), fontsize=10)
    texts.append(txt)

# 调整文本位置以避免重叠
adjust_text(texts, only_move={'points': 'y', 'text': 'y'}, expand_points=(1.1, 1.1))

# 设置坐标轴标签和标题
plt.xlabel('Params (M)')
plt.ylabel('mAP50 (%)')
# plt.title('Scatter Plot with Star Markers')

# 保存图形到本地
plt.savefig("uavdt-param.png", dpi=300, bbox_inches='tight')

# 显示图表
plt.show()