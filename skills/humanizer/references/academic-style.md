# Academic Humanizing

Use this reference when rewriting Chinese or English academic prose across disciplines:
thesis chapters, abstracts, introductions, methods, results, discussions, literature
reviews, reports, and journal-style manuscripts.

## Core Aim

Make the text read like a careful researcher wrote it. Preserve evidence and structure.
Remove AI polish by making claims specific, cautious, and logically connected, not by
making the text casual or decorative.

## Evidence-First Rules

- Preserve all numerical values, sample sizes, thresholds, confidence intervals, p values,
  q values, effect sizes, labels, software versions, citation markers, figure numbers, and
  table numbers.
- Keep observational language observational. Use "associated with", "correlated with",
  "was higher/lower in", "suggests", "supports", "may indicate", or equivalent cautious
  Chinese wording when evidence is not causal.
- Do not turn limitations into confident conclusions.
- Keep methods concrete: data source, sample, instrument or material, database, version,
  normalization, statistical test, correction method, grouping standard, and evaluation
  metric when provided.
- Maintain user-provided technical terminology exactly unless correcting obvious
  formatting: model names, grouping labels, thresholds, species or material names,
  software tools, database names, theory names, pathway names, policy names, and
  statistical tests.

## Chinese Academic Style

Prefer concise Chinese scholarly prose:

- Use "本研究", "结果显示", "进一步分析表明", "提示", "可能", "有待进一步验证", "为后续研究提供参考".
- Use "然而/不过/此外/同时/因此/总体而言" only when the logical relationship is real.
- Avoid inflated phrases: "具有里程碑意义", "极大推动", "深刻揭示", "重要突破", "广阔前景", "不可忽视的重要作用".
- Avoid empty summaries: "综上所述，本研究具有重要意义" unless followed by a specific contribution.
- Prefer specific contribution statements: "为该变量与研究对象之间的关系提供了补充证据".
- Use Chinese punctuation and full-width parentheses in Chinese paragraphs, but keep
  symbols and abbreviations readable: score<1, score≥50, p<0.05, n=17.

## English Academic Style

Prefer restrained journal-like prose:

- Use "This study...", "We analyzed...", "These findings suggest...", "Together, these
  results support..." when appropriate for the genre.
- Avoid "groundbreaking", "landmark", "pivotal", "robustly proves", "sheds light on"
  unless the phrase is clearly justified.
- Vary sentence structure, but keep the chain: context -> gap -> method -> result ->
  interpretation.
- In abstracts, one sentence should usually carry one main claim. Do not stack many vague
  clauses.
- Prefer exact subjects over empty abstractions: "the baseline feature distribution"
  instead of "this complex landscape"; "predefined strata" instead of "these groups" when
  clarity matters.

## Cross-Disciplinary Style Notes

- Start from a concrete unresolved problem, not a broad slogan.
- State the data, material, corpus, sample, method, or case source early.
- Separate association from mechanism or causality. Observational, archival, textual,
  computational, or survey results usually support association or interpretation, not
  causal claims by themselves.
- Give the main result before interpretation. Do not bury the result under significance
  language.
- Close with a bounded implication: what the result supports, what it cannot prove, and
  what future work would need to verify.

These notes are style guidance only. They are not sources for thesis claims.

## Rewrite Procedure

1. Identify the section type: abstract, introduction, methods, results, discussion,
   conclusion, literature review, report, response letter, or popular summary.
2. Preserve technical content exactly before improving rhythm.
3. Remove AI tells: generic importance claims, synonym cycling, exaggerated transitions,
   empty "future prospects", and overuse of "significant/important/complex".
4. Rebuild the paragraph around a claim chain:
   - Background/gap
   - What was done
   - What was found
   - What it means and what remains uncertain
5. For bilingual text, align terminology across languages. If the Chinese and English
   versions differ in claim strength, harmonize them toward the more evidence-faithful
   version.

## Terminology Rules

- First Chinese mention: 中文术语（English term，ABBR） when useful. Later mentions can use
  the abbreviation.
- First English mention: English term (ABBR); avoid translating every repeated term.
- Preserve capitalization, spelling, mathematical notation, and discipline-specific
  symbols unless the user asks to standardize them.
- Do not translate database, tool, organization, theory, law, policy, or model names
  unless a standard Chinese name exists.

## Output Options

Unless the user asks otherwise, return:

1. The rewritten text.
2. A short "主要修改" list only when helpful, focusing on claim strength, logic,
   terminology, and tone. Do not over-explain obvious wording changes.
