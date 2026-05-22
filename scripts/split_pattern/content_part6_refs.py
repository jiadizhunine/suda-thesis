# -*- coding: utf-8 -*-
"""示例参考文献、致谢、图谱和目录。

参考文献为占位条目，正式论文必须替换为真实可核验文献。
"""

import os

REFERENCES = [
    "[1] 示例作者A, 示例作者B. 示例研究背景文献条目[J]. 示例期刊, 2024, 1(1): 1-10.（占位条目，请替换为真实文献）",
    "[2] 示例作者C. 示例方法学参考书[M]. 示例城市: 示例出版社, 2023: 11-20.（占位条目，请替换为真实文献）",
    "[3] 示例机构. 示例公开数据说明[EB/OL]. https://example.invalid/dataset, 2026-01-01.（占位条目，请替换为真实来源）",
    "[4] 示例作者D, 示例作者E. 示例验证方法文献条目[J]. 示例期刊, 2025, 2(2): 21-30.（占位条目，请替换为真实文献）",
]

ACKNOWLEDGEMENT = (
    "本示例致谢用于展示段落格式。正式论文应根据学生真实经历撰写，感谢指导者、合作者、同学、家人或其他"
    "实际提供帮助的人。"
    "\n"
    "致谢内容应真诚、简洁、具体，不应保留模板化占位句。若涉及合作数据、图像或代码，也应说明其来源和贡献边界。"
)

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FIG_DIR = os.path.join(_SCRIPT_DIR, 'figures')

FIGURE_MAP = {
    "fig3_1": os.path.join(FIG_DIR, 'example_figure_3_1.png'),
    "fig3_2": os.path.join(FIG_DIR, 'example_figure_3_2.png'),
    "fig3_3": os.path.join(FIG_DIR, 'example_figure_3_3.png'),
    "fig3_4": os.path.join(FIG_DIR, 'example_figure_3_4.png'),
    "fig3_5": os.path.join(FIG_DIR, 'example_figure_3_5.png'),
    "fig3_6": os.path.join(FIG_DIR, 'example_figure_3_6.png'),
    "fig3_7": os.path.join(FIG_DIR, 'example_figure_3_7.png'),
    "fig3_8": os.path.join(FIG_DIR, 'example_figure_3_8.png'),
    "fig3_9": os.path.join(FIG_DIR, 'example_figure_3_9.png'),
    "fig3_10": os.path.join(FIG_DIR, 'example_figure_3_10.png'),
    "fig3_11": os.path.join(FIG_DIR, 'example_figure_3_11.png'),
    "fig3_12": os.path.join(FIG_DIR, 'example_figure_3_12.png'),
    "fig3_13": os.path.join(FIG_DIR, 'example_figure_3_13.png'),
}

FIGURE_CAPTIONS = {
    "fig3_1": "图 3-1 示例资料来源概览图",
    "fig3_2": "图 3-2 示例质量控制摘要图",
    "fig3_3": "图 3-3 示例核心指标总体分布图",
    "fig3_4": "图 3-4 示例分组指标比较图",
    "fig3_5": "图 3-5 示例分层后样本分布图",
    "fig3_6": "图 3-6 示例分层后指标比较图",
    "fig3_7": "图 3-7 示例子指标聚类结果图",
    "fig3_8": "图 3-8 示例子指标分组差异图",
    "fig3_9": "图 3-9 示例综合指标效应方向图",
    "fig3_10": "图 3-10 示例样本级趋势热图",
    "fig3_11": "图 3-11 示例模型系数图",
    "fig3_12": "图 3-12 示例敏感性分析图",
    "fig3_13": "图 3-13 示例交叉验证摘要图",
}

TOC_ENTRIES = [
    ("第1章 绪论", 1, True),
    ("1.1 研究背景示例", 1, False),
    ("1.2 国内外研究现状示例", 2, False),
    ("1.3 研究问题示例", 3, False),
    ("1.4 研究内容与技术路线示例", 4, False),
    ("第2章 材料与方法", 5, True),
    ("2.1 示例资料来源", 5, False),
    ("2.2 数据预处理示例", 6, False),
    ("2.3 指标构建示例", 6, False),
    ("2.4 统计分析示例", 7, False),
    ("2.5 图表生成与格式检查示例", 7, False),
    ("第3章 结果", 8, True),
    ("3.1 示例资料整理结果", 8, False),
    ("3.2 示例描述性统计结果", 9, False),
    ("3.3 示例分组分析结果", 10, False),
    ("3.4 示例子指标分析结果", 11, False),
    ("3.5 示例综合指标分析结果", 12, False),
    ("3.6 示例模型验证结果", 13, False),
    ("3.7 示例交叉验证结果", 14, False),
    ("第4章 讨论", 15, True),
    ("4.1 主要发现示例", 15, False),
    ("4.2 与已有研究的关系示例", 16, False),
    ("4.3 方法学意义示例", 16, False),
    ("4.4 研究局限示例", 17, False),
    ("4.5 展望示例", 17, False),
    ("第5章 结论", 18, True),
    ("参考文献", 19, True),
    ("致 谢", 20, True),
]
