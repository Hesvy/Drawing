import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.use('Qt5Agg')   # 设置backend

df = pd.read_excel(r"C:\Users\Administrator\Nutstore\2\我的坚果云\博士研究工作\刘天罡组合作项目\比较基因组学信息分析\GO KEGG注释\GO注释\InDel GO注释\InDel GO anno_total.xlsx",0)

# 重组数据
# 首先，将数据中的分号分隔内容拆分成独立的行
categories = ['biological process', 'cellular component', 'molecular function']
df_long = pd.DataFrame(columns=['GO_category', 'GO_term'])

for category in categories:
    # 对每一列进行处理，将分号分隔的内容拆分成多行
    terms = df[category].dropna().str.split(';').explode().str.strip()
    temp_df = pd.DataFrame({
        'GO_category': [category] * len(terms),
        'GO_term': terms
    })
    df_long = pd.concat([df_long, temp_df], ignore_index=True)

# 计算每个 GO term 的数量
df_count = df_long.groupby(['GO_category', 'GO_term']).size().reset_index(name='Number of Gene')

# 按 GO 大类和数量排序
df_count = df_count.sort_values(['GO_category', 'Number of Gene'], ascending=[True, False])

# 设置颜色映射
colors = {
    'biological process': sns.color_palette("Blues_r", n_colors=len(df_count[df_count['GO_category'] == 'biological process'])),
    'cellular component': sns.color_palette("Greens_r", n_colors=len(df_count[df_count['GO_category'] == 'cellular component'])),
    'molecular function': sns.color_palette("Reds_r", n_colors=len(df_count[df_count['GO_category'] == 'molecular function']))
}

# 创建图形
plt.figure(figsize=(12, len(df_count) * 0.3))  # 根据条目数量调整图形高度

# 绘制横向柱状图
bars = plt.barh(range(len(df_count)), df_count['Number of Gene'], color='gray')  # 初始颜色设置为灰色

# 设置颜色
for i, bar in enumerate(bars):
    category = df_count.iloc[i]['GO_category']
    category_items = df_count[df_count['GO_category'] == category]
    color_idx = category_items.index.get_loc(df_count.index[i])
    bar.set_color(colors[category][color_idx])

# 设置 y 轴标签
plt.yticks(range(len(df_count)), df_count['GO_term'], fontsize=8)

# 添加图例
legend_elements = [plt.Rectangle((0, 0), 1, 1, fc=colors[cat][0], label=cat) for cat in colors.keys()]
plt.legend(handles=legend_elements, bbox_to_anchor=(1.05, 1), loc='upper left')

# 设置标题和轴标签
plt.title('GO Terms Distribution')
plt.xlabel('Number of Gene')

# 调整布局
plt.tight_layout()

# 显示图形
plt.show()
