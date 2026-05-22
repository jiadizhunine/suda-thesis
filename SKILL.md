---
name: suda-thesis
description: Use when generating or editing Suzhou University undergraduate thesis DOCX files, including 苏州大学论文, 苏大毕设, 毕业论文, 论文正文, 文献综述, 文献翻译, 任务书, 中期检查, literature review, literature translation, task book, midterm-check forms, or Chinese academic DOCX formatting that must follow Suzhou University thesis style.
license: MIT
---

# Suda Thesis

Generate Suzhou University undergraduate academic documents as `.docx` files with
`python-docx`. For long documents (thesis body, literature review, and literature
translation), always generate segmented Python code: content lives in `content_part*.py`
modules, one aggregator imports those modules, and one `create_*_docx.py` script handles
formatting and assembly. For short form documents (task book and midterm-check), use a
focused table/form script unless the user's supplied content is long enough to require
content parts.

## Bundled Resources

- `scripts/split_pattern/`: the only retained code scaffold. Copy or adapt this folder
  into the user's output directory when building a new document. Do not edit the bundled
  scaffold in place for a user paper.
- `skills/humanizer/`: bundled academic prose humanizer. Use it after thesis body and
  literature review drafts are generated.
- `references/format-standards.md`: formatting details for page setup, styles, TOC,
  bookmarks, figure captions, references, and metadata cleanup.
- `references/forms.md`: task-book and midterm-check field structure, writing rules, and
  table/form review checklist.
- `references/pitfalls.md`: known failure modes and exact code patterns to avoid.

## Supported Documents

| Document | Output Script | Required Split Use | Humanizer |
| --- | --- | --- | --- |
| Thesis body | `create_thesis_docx.py` | Always split | Required after draft |
| Literature review | `create_review_docx.py` | Always split | Required after draft |
| Literature translation | `create_translation_docx.py` | Always split for long papers | Preserve source meaning; use only for faithful academic fluency checks |
| Task book | `create_task_book_docx.py` | Not required; use table/form script | Formal concision check only |
| Midterm-check form | `create_midterm_check_docx.py` | Not required; use table/form script | Formal concision check only |

Currently supported Suzhou University document types are thesis body, literature review,
literature translation, task book, and midterm-check form.

## Non-Negotiable Rules

1. Use the split pattern for thesis body, literature review, and long translation tasks.
   Never put long prose into one giant `create_*_docx.py`.
2. Keep long-document `create_*_docx.py` files focused on formatting and assembly. Store
   prose, references, figure maps, and captions in `content_part*.py` files imported
   through `content_data.py`.
3. Never fabricate references. Verify title, authors, and journal/source before using a
   reference. A real DOI or article number is not enough if the title/authors/source do
   not match.
4. Never fabricate experimental details. Ask what the student actually measured or
   observed before writing Methods, Results, or Discussion text.
5. Introduce each specialized term or abbreviation exactly once across the whole
   document, including abstracts and body text.
6. Visually inspect every figure before insertion and confirm that the image, caption,
   surrounding text, and citation match.
7. For thesis body and literature review, run the bundled humanizer after drafting prose
   and before final DOCX delivery. Use `skills/humanizer/SKILL.md` in academic mode,
   preserving all evidence, citations, data, terminology, and claim strength.
8. Erase DOCX privacy metadata for every generated file type. Clear creator/editor
   fields, comments, title/subject/keywords/category, company/manager fields, and
   `python-docx` application fingerprints as described in `references/format-standards.md`.
9. Never deliver after the first successful generation alone. Every generated DOCX must
   pass the review step for its document type; thesis body and literature review must
   repeat the review-regenerate loop until figure-content correspondence, reference
   authenticity, humanizer quality, and formatting checks pass.
10. For task book and midterm-check forms, do not fabricate student identity, advisor
    identity, project membership, dates, progress, results, or review opinions. Use
    placeholders when the user has not provided required form fields.

## Standard Workflow

1. Gather the topic, document type, output directory, source materials, reference list
   expectations, and figure availability. For translation, also gather the exact source
   paper/PDF. For thesis body, gather the actual experimental protocol and observations.
   For task book and midterm-check forms, gather the form fields: college, topic, student,
   major, grade, advisor, dates, project type, completed work, remaining work, problems,
   solutions, schedule, and any required placeholder signatures.
2. Read only the resources needed for the current task:
   - For thesis body, literature review, and long translation tasks, inspect
     `scripts/split_pattern/create_thesis_docx.py` and
     `scripts/split_pattern/content_data.py` to understand the scaffold.
   - For task book and midterm-check forms, read `references/forms.md`.
   - Read `references/format-standards.md` before writing or modifying formatting code.
   - Read `references/pitfalls.md` before finalizing any generated script.
3. Choose the generation pattern:
   - For thesis body, literature review, and long translation tasks, copy/adapt
     `scripts/split_pattern/` into the output directory. Rename the assembly script to
     match the document type: `create_thesis_docx.py`, `create_review_docx.py`, or
     `create_translation_docx.py`.
   - For task book and midterm-check forms, create a focused table/form script named
     `create_task_book_docx.py` or `create_midterm_check_docx.py`. Reuse formatting
     helpers from `references/format-standards.md`; keep form data in constants near the
     top of the script, or in `content_data.py` if the form text is long.
4. For long documents, generate content modules by section. Use parallel workers when
   available; otherwise write them sequentially. Keep each module small enough to avoid
   truncation or broken string literals.
5. For thesis body and literature review, run the bundled humanizer:
   - Read `skills/humanizer/SKILL.md`.
   - Use Academic mode.
   - Also read `skills/humanizer/references/academic-style.md`.
   - If matching the user's thesis voice is needed, also read
     `skills/humanizer/references/thesis-style.md`.
   - Humanize the prose in `content_part*.py` section by section while preserving
     references, figure mentions, numeric values, methods, and cautious academic claims.
6. For long documents, build `content_data.py` as the only aggregation layer. The assembly
   script should import from `content_data.py`, not from each content part directly.
7. Run syntax checks and generate the document.

   For long split documents:

   ```bash
   python3 -m py_compile content_part*.py content_data.py create_*_docx.py
   python3 create_*_docx.py
   ```

   For form documents:

   ```bash
   python3 -m py_compile create_task_book_docx.py
   python3 create_task_book_docx.py
   # or
   python3 -m py_compile create_midterm_check_docx.py
   python3 create_midterm_check_docx.py
   ```

8. Run the review-regenerate loop below. If any issue is found, fix the relevant content
   part, form data constants, figure map, reference list, or assembly script; regenerate
   the DOCX; then review again.

## Split Pattern Contract

A typical output directory should look like this:

```text
content_part1_abstract.py
content_part2_ch1.py
content_part3_ch2.py
content_part4_ch3.py
content_part5_ch4_ch5.py
content_part6_refs.py
content_data.py
create_<document_type>_docx.py
figures/
```

This layout is a starting point, not a hard chapter count. Add more
`content_partN_*.py` files when a document has more sections, or rename the suffixes to
match a translation's original paper structure. Preserve the core contract:

- `content_part*.py` contains prose/data constants only.
- `content_data.py` imports and re-exports the constants used by the assembly script.
- `create_*_docx.py` imports from `content_data.py`, defines formatting helpers, inserts
  content, cleans metadata, saves the DOCX, and prints the output path.

## Document Rules

### Thesis Body

- Include Chinese abstract, English abstract, TOC, chapters, references, and
  acknowledgement.
- Use Suzhou University page setup, heading styles, TOC field codes, and `-N-` page
  numbers.
- References and acknowledgement are not numbered chapters. Style them visually as
  first-level headings and add them to the TOC without putting them in Word's heading
  outline.
- Use the student's actual data and observations only.
- After the first complete draft, run the bundled humanizer before regenerating the final
  DOCX.

### Literature Review

- Include abstract, TOC, foreword/introduction, thematic chapters, conclusion, and
  references.
- Let chapter count follow the topic. Do not force a fixed number of chapters.
- Use real, verified references only. Put citation numbers at the end of clauses or
  sentences rather than directly after author names.
- Use figures only from cited sources, and include the source in each caption.
- After the first complete draft, run the bundled humanizer before regenerating the final
  DOCX.
- Verify every reference used in the review before delivery. Literature review citations
  are high-risk because plausible but fake bibliographic entries are easy to generate.

### Literature Translation

- Mirror the source paper's structure exactly. Do not add sections that are absent from
  the original paper.
- Translate every paragraph without summarizing or condensing.
- Preserve original figure and panel references such as `Figure 1B-C`.
- Include the source paper as the only reference unless the user explicitly asks for
  additional context.
- Split by original paper section when the translation is long.
- Keep or download the source PDF/source URL alongside the generated DOCX when available,
  so translation structure and figure references can be checked.

### Task Book

- Generate the Suzhou University undergraduate thesis/design task book as a structured
  table/form DOCX.
- Include the document title, college/department line, topic line, student/advisor/basic
  information table, major task and goal, main content, basic requirements, main
  references, and schedule.
- Use concise formal prose. The task book should describe what the project will do, what
  the student must complete, and the expected schedule; it should not read like a full
  thesis chapter.
- Use real, verified references for the reference section. If the user has not provided
  references, search or ask before filling them; do not invent plausible entries.
- Use placeholders such as `XXX` or `待填写` for missing student/advisor/date fields
  rather than inventing personal information.
- Follow `references/forms.md` for field order and table/form review.
- The split pattern is not required unless the user provides unusually long content.

### Midterm-Check Form

- Generate the Suzhou University undergraduate thesis/design midterm progress check form
  as a table/form DOCX.
- Include the title, college line, student/year/major/date fields, topic, completed tasks,
  whether progress matches the task book, remaining tasks, whether the project can finish
  on time, problems, proposed solutions, and opinion/signature placeholders.
- Describe completed work at the work-progress level. Do not insert specific numerical
  results, named variables, private data, or detailed conclusions unless the user explicitly
  provides them and asks to keep them.
- Problems and solutions should be practical and concise: workload, data organization,
  figure preparation, writing schedule, format checking, and revision plan. Avoid turning
  the form into a literature discussion.
- Do not fabricate progress or approval opinions. Use neutral placeholders for signatures
  and review comments unless the user provides exact wording.
- Follow `references/forms.md` for field order and table/form review.
- The split pattern is not required unless the user provides unusually long content.

## Review-Regenerate Loop

Run this loop after every generated DOCX for thesis body and literature review. Do not
stop at "the script ran" or "the file exists". For literature translation, task book, and
midterm-check forms, run the shorter document-specific reviews at the end of this section.

1. **Figure-content correspondence (highest priority)**:
   - Inspect every figure file visually.
   - Locate the exact section where the figure is inserted.
   - Confirm the surrounding paragraph discusses the same object, method, result, or
     mechanism shown in the image.
   - Confirm the caption describes the actual image and, for literature review figures,
     cites the same verified source as the image.
   - If any figure is missing, mislabeled, from the wrong paper, or placed in the wrong
     section, fix `FIGURE_MAP`, `FIGURE_CAPTIONS`, or the relevant prose and regenerate.

2. **Reference authenticity (highest priority)**:
   - For thesis body and literature review, verify each reference title, authors, journal
     or source, year, volume/issue, pages/article number, and DOI/URL when present.
   - A real DOI or article number alone is not enough; title, authors, and source must
     match.
   - Check every in-text citation is within range and every cited source appears in the
     reference list.
   - If any reference cannot be verified, replace it with a real source or remove the
     unsupported claim, then regenerate.

3. **Humanizer quality for thesis/review**:
   - Confirm the bundled humanizer has been applied to all prose content parts.
   - Re-scan for AI-style artifacts such as empty significance claims, overlong
     English-syntax Chinese, vague author-name narrative citations, filler `等`, metaphors,
     colloquialisms, first-person thesis prose, and exaggerated causal claims.
   - If the humanizer introduced new issues, fix them and regenerate.

4. **Format and document integrity**:
   - Check page setup, header/footer, heading styles, TOC, bookmarks, figure captions,
     references, acknowledgement, page numbers, and metadata erasure.
   - Re-run syntax checks before each regeneration.

Repeat the loop until all four categories pass. Keep the fixes in the segmented content
files so the final DOCX can be regenerated reproducibly.

For task book and midterm-check forms, run this shorter review before delivery:

1. Confirm every required form field is filled from user-provided information or marked
   with an explicit placeholder.
2. Confirm references in a task book are real and formatted consistently.
3. Confirm midterm progress statements do not fabricate results, measurements, or approval
   opinions.
4. Confirm table borders, merged cells, fonts, spacing, margins, and metadata cleanup.
5. If any issue is found, revise the form script and regenerate the DOCX.

For literature translation, run this review before delivery:

1. Confirm the generated document mirrors the source paper's section order and headings.
2. Confirm every source paragraph is translated without summarizing, omission, or added
   sections.
3. Confirm original figure, table, supplement, and panel references are preserved.
4. Confirm the source paper is the only reference unless the user requested added context.
5. Confirm formatting and metadata cleanup. If any issue is found, revise the relevant
   content part or assembly script and regenerate the DOCX.

## Post-Generation Review

Before delivering the document, confirm the final loop pass:

- Long-document formatting: CJK fonts set through XML, first-line indent uses
  `firstLineChars='200'`, heading spacing uses `beforeLines='100'` and
  `afterLines='100'`, TOC field code is correct, captions are 12 pt, and metadata is
  erased.
- Content: abstract matches the chapters, transitions are natural, conclusion answers
  the document's opening questions, and thesis/review prose has passed the bundled
  humanizer.
- References: every entry is real, citation numbers are in range, GB/T 7714 formatting
  is consistent, and title/authors/source match verification results.
- Figures: every image has been inspected, is placed in the correct section, and has a
  matching caption and source.
- Translation: source structure, paragraph coverage, figure/table references, and source
  reference policy have been checked against the original paper.
- Forms: task book and midterm-check fields are complete, table layout is intact, missing
  personal information remains explicit placeholders, and no progress or review opinion
  has been invented.

If any check fails, fix the relevant content part or assembly script, regenerate the
DOCX, and repeat verification.
