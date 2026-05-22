# -*- coding: utf-8 -*-
"""示例标题、摘要和关键词。

此文件只演示 split pattern 的数据结构。生成真实论文时，必须替换为学生自己的
题目、摘要、关键词和真实研究内容。
"""

TITLE_CN = "示例研究题目：基于公开示例数据的多维分析流程演示"

TITLE_EN = "Example Thesis Title: Demonstration of a Multi-dimensional Analysis Workflow Using Public Example Data"

ABSTRACT_CN = (
    "本示例用于展示苏州大学本科毕业论文正文的分段代码组织方式。"
    "示例主题、数据名称、图题和参考文献均为占位内容，不能直接用于正式论文。"
    "在真实写作中，应根据学生实际完成的研究工作替换为可核验的数据来源、分析方法和研究结论。"
    "\n"
    "示例流程包括资料整理、数据预处理、指标构建、结果可视化和稳健性检查五个步骤。"
    "正文代码将内容拆分为多个 `content_part*.py` 文件，并由 `content_data.py` 汇总后供"
    "`create_thesis_docx.py` 调用。该结构可避免长篇中文内容集中在单个脚本中导致截断、"
    "字符串损坏或后续维护困难。"
    "\n"
    "示例结果部分展示了描述性统计、分组比较、趋势分析、模型输出和交叉验证等常见论文段落的写法。"
    "所有数字、结论和图名均为格式演示，不代表任何真实实验或真实数据。"
    "正式使用时，应在生成前确认数据来源、统计方法、图像内容和参考文献均与学生实际工作一致。"
    "\n"
    "综上，本示例仅作为文档生成 scaffold，用于检查标题、摘要、目录、章节、图题、参考文献和致谢等"
    "格式是否符合预期。实际论文生成必须完成内容替换、参考文献核验和图文对应检查。"
)

KEYWORDS_CN = "示例数据；分段代码；文档生成；格式校验；本科论文"

ABSTRACT_EN = (
    "This example demonstrates the segmented-code workflow for generating a Suzhou University "
    "undergraduate thesis document. The topic, dataset names, figure captions, and references "
    "are placeholders only and must not be used as final academic content."
    "\n"
    "The example workflow contains five illustrative steps: material organization, data "
    "preprocessing, indicator construction, result visualization, and robustness checking. "
    "Document content is split across `content_part*.py` files, aggregated by `content_data.py`, "
    "and rendered by `create_thesis_docx.py`. This pattern prevents very long Chinese prose from "
    "being placed in a single script, reducing truncation and maintenance risks."
    "\n"
    "The result section includes placeholder paragraphs for descriptive statistics, group "
    "comparison, trend analysis, model output, and cross-validation. All numbers, findings, "
    "and figure names are illustrative and do not describe real experiments or real datasets."
    "\n"
    "In summary, this file is a scaffold for checking document structure and formatting. A real "
    "thesis must replace every placeholder with verified data, real references, matched figures, "
    "and content that reflects the student's actual work."
)

KEYWORDS_EN = "Example data；Segmented code；Document generation；Format checking；Undergraduate thesis"
