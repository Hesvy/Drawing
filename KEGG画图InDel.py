import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

# 读取Excel数据
file_path = r"C:\Users\Administrator\Nutstore\2\我的坚果云\博士研究工作\刘天罡组合作项目\比较基因组学信息分析\GO KEGG注释\KEGG注释\InDel KEGG注释\InDel KEGG.xlsx"
try:
    df = pd.read_excel(file_path, sheet_name=2)
except Exception as e:
    print(f"Error reading file: {e}")
    exit()

# 数据预处理：删除NaN行，筛选数量大于0的行，并按大类和小类分组
df = df.dropna()
df_grouped = df.groupby(['大类', '小类'])['数量'].sum().reset_index()
df_grouped = df_grouped[df_grouped['数量'] > 0]

# 自定义颜色调色板（更柔和的色系）
colors = ['#A0D5F5', '#90EE90', '#FFB6C1', '#87CEFA', '#DDA0DD', '#F0E68C']

# 颜色映射：每个大类分配不同颜色
大类列表 = df_grouped['大类'].unique()
大类颜色 = dict(zip(大类列表, colors[:len(大类列表)]))

# 绘图设置
plt.rcParams['font.sans-serif'] = ['Arial', 'SimHei']  # 优先使用Arial
plt.rcParams['axes.unicode_minus'] = False
fig, ax = plt.subplots(figsize=(15, 10), dpi=300)

# Y轴位置初始化
y_positions = []
current_y = 0
大类_start_positions = {}

# 绘制柱状图和置顶大类标签
for 大类 in 大类列表:
    大类_df = df_grouped[df_grouped['大类'] == 大类]
    大类_start_positions[大类] = current_y

    # 绘制小类柱状图
    for _, row in 大类_df.iterrows():
        ax.barh(current_y, row['数量'], color=大类颜色[大类], edgecolor='none')
        y_positions.append((current_y, row['小类']))
        current_y += 1

    # 分组间隔（在每个大类末尾增加间距）
    current_y += 0.8

# 添加大类标签
for 大类, start_pos in 大类_start_positions.items():
    大类_df = df_grouped[df_grouped['大类'] == 大类]
    end_pos = start_pos + len(大类_df) - 1

    ax.text(-3, end_pos + 0.8, 大类,
            fontsize=9,
            fontweight='bold',
            color='red',
            ha='left',  # 左对齐
            va='center',
            fontfamily='Arial')

# 添加小类标签
for i, (pos, label) in enumerate(y_positions):
    ax.text(-2, pos, label,
            va='center',
            ha='left',  # 左对齐
            fontsize=7,
            fontfamily='Arial')

# 设置Y轴标签
ax.set_yticks([])
ax.set_yticklabels([])

# 设置X轴刻度
plt.xticks(np.linspace(0, max(df_grouped['数量']), 5).astype(int), fontsize=7)

# 设置标题和X轴标签
ax.set_title("KEGG pathway annotation", fontsize=10, fontweight='bold', fontfamily='Arial')
ax.set_xlabel("Number of Gene", fontsize=8, fontfamily='Arial')

# 调整布局并显示图形
plt.tight_layout()
plt.show()