import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体和负号显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 任务数据
tasks = [
    {"name": "项目启动与需求分析", "start_week": 1, "duration_weeks": 1, "color": "#4CAF50"},  # 绿色
    {"name": "微生物菌株筛选与鉴定", "start_week": 2, "duration_weeks": 3, "color": "#2196F3"},  # 蓝色
    {"name": "发酵工艺初步设计", "start_week": 3, "duration_weeks": 4, "color": "#FFC107"},  # 黄色
    {"name": "菌株基因工程改造", "start_week": 5, "duration_weeks": 6, "color": "#FF5722"},  # 红色
    {"name": "小试发酵实验", "start_week": 11, "duration_weeks": 3, "color": "#9C27B0"},  # 紫色
    {"name": "发酵条件优化", "start_week": 14, "duration_weeks": 4, "color": "#00796B"},  # 深绿色
    {"name": "发酵产物提取与纯化工艺开发", "start_week": 16, "duration_weeks": 7, "color": "#607D8B"},  # 灰色
    {"name": "中试放大实验", "start_week": 23, "duration_weeks": 6, "color": "#FF9800"},  # 橙色
    {"name": "产品质量检测与分析", "start_week": 29, "duration_weeks": 3, "color": "#9E9E9E"},  # 浅灰色
    {"name": "项目总结与报告撰写", "start_week": 32, "duration_weeks": 2, "color": "#3F51B5"}   # 深蓝色
]

# 绘制甘特图
fig, ax = plt.subplots(figsize=(12, 8))

# 反转任务顺序
tasks.reverse()

# 绘制任务条形图
for i, task in enumerate(tasks):
    start = task["start_week"]
    duration = task["duration_weeks"]
    ax.barh(i, duration, left=start, height=0.4, align='center', color=task["color"], edgecolor='white',
            linewidth=1, alpha=0.8, zorder=2)  # 添加白色边框，透明度调整
    ax.text(start + duration + 0.5, i, f"{task['name']}", va='center', ha='left', fontsize=10, color='gray', zorder=3)

# 设置时间轴
max_week = max(task["start_week"] + task["duration_weeks"] for task in tasks)
weeks = np.arange(1, max_week + 1, 2)  # 每隔2周显示一个刻度
ax.set_xticks(weeks)
ax.set_xticklabels([f"第{w}周" for w in weeks])  # 显示“第几周”

# 添加任务进度条（假设所有任务已完成）
for i, task in enumerate(tasks):
    start = task["start_week"]
    duration = task["duration_weeks"]
    progress = 100  # 假设所有任务已完成
    ax.text(start + duration - 0.5, i, f"{progress}%", va='center', ha='right', fontsize=8, color='white', zorder=3)

# 添加项目里程碑（去掉第一个里程碑）
milestones = [11, 29]  # 假设第6周和第10周是里程碑
for milestone in milestones:
    ax.axvline(x=milestone, color='red', linestyle='--', linewidth=1, alpha=0.7, zorder=1)
    ax.text(milestone, len(tasks) + 0.5, f"里程碑", va='center', ha='center', fontsize=10, color='red', zorder=3)

# 添加标签和标题
plt.xlabel('项目进度（周）', fontsize=12)
plt.ylabel('任务', fontsize=12)
plt.title('发酵工程项目管理甘特图', fontsize=16, fontweight='bold', pad=20)
plt.grid(True, linestyle='--', alpha=0.5, color='lightgray', zorder=1)

# 设置任务名称的显示顺序
plt.yticks(range(len(tasks)), [task["name"] for task in tasks])

# 设置图表样式
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# 显示图表
plt.tight_layout()
plt.show()