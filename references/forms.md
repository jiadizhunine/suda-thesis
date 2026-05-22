# Form Documents Reference

Use this reference for Suzhou University task-book and midterm-check form generation.
These are short table/form documents, not long thesis chapters.

## Task Book

Generate `create_task_book_docx.py` unless the user requests another filename.

Required content:

- Title: `苏州大学本科生毕业设计（论文）任务书`
- College/department line and topic line
- Basic information table: college, topic, advisor, title/role, student, grade,
  major, project type, and project membership when provided
- Main task and goal
- Main content
- Basic requirements
- Main references
- Schedule

Writing rules:

- Use concise formal prose. Describe what the project will do and what the student must
  complete; do not write full thesis paragraphs.
- Use placeholders such as `XXX`, `待填写`, or `待确认` for missing personal fields.
- References must be real and verified. Do not invent bibliographic entries.
- Schedule dates must come from the user or remain placeholders.

Default layout when no official sample is provided:

- A centered title.
- A compact basic-information table.
- Four bordered sections for major task and goal, main content, basic requirements, and
  references.
- One schedule table with `序号 / 任务 / 起止日期`.
- Use 10-20 verified key references unless the user specifies another count.

## Midterm-Check Form

Generate `create_midterm_check_docx.py` unless the user requests another filename.

Required content:

- Title: `苏州大学本科生毕业设计（论文）中期进展情况检查表`
- College/department line
- Student, grade, major, date, and topic fields
- Completed tasks
- Whether progress matches the task book
- Remaining tasks
- Whether the project can finish on time
- Problems and proposed solutions
- Advisor, expert group, and college opinion/signature placeholders

Writing rules:

- Completed tasks should describe work progress, not detailed findings.
- Do not add numeric results, named variables, private data, or conclusions unless the
  user explicitly provides them and asks to keep them.
- Problems and solutions should be practical: workload, data organization, figure
  preparation, writing schedule, format checking, and revision plan.
- Do not fabricate approval opinions. Use neutral placeholders unless exact wording is
  provided.

Default layout when no official sample is provided:

- A centered title and college/department line.
- One bordered table containing basic information, topic, completed tasks, remaining
  tasks, problems, proposed solutions, and opinion/signature rows.
- Use concise numbered items for completed and remaining tasks.
- Use `是 / 待确认` style placeholders for yes/no progress fields when the user has not
  provided the exact answer.

## Formatting And Review

- Use A4 page setup and table borders that match the user's sample when provided.
- If no sample is provided, use A4, 2.54 cm margins, 宋体 body text, and stable bordered
  tables with merged label cells where needed.
- Keep fonts, line spacing, merged cells, labels, and signature areas stable.
- Apply the metadata-erasure routine from `format-standards.md` before saving.
- Before delivery, confirm every required field is either filled from user input or marked
  with an explicit placeholder.
