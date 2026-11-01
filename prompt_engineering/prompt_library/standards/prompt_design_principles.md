# Prompt Design Principles

These principles apply to every reusable prompt in this library.

## 1. Define the task precisely

State the task, intended user, relevant role or perspective, and what a successful response should accomplish. Avoid vague requests such as “make this better” without defining the target.

## 2. Make inputs explicit

List required inputs, optional context, and placeholders. Tell the model what to do when information is missing. Do not silently invent requirements or facts.

## 3. Establish boundaries

Specify what the model must and must not do. Distinguish analysis from modification; for example, a code-review prompt should recommend targeted fixes rather than rewrite an entire application unless asked.

## 4. Require evidence

Tie findings to supplied material using file names, symbols, line references when available, or short quoted excerpts. Explain the reasoning and impact. Do not fabricate locations or facts.

## 5. Represent uncertainty honestly

Separate confirmed findings from potential concerns and items requiring verification. State what context is missing and how to verify the concern. Do not convert absence of evidence into proof of safety.

## 6. Define a useful output contract

Specify headings, fields, ordering, and any machine-readable format. Keep the format proportional to the task and make “no findings” a valid outcome.

## 7. Prioritize by impact

When multiple findings exist, order them by severity and practical impact. Severity labels must have documented definitions.

## 8. Avoid unnecessary changes

Prefer minimal, actionable recommendations. Explain trade-offs where relevant. Do not change unrelated code or domain behavior.

## 9. Make prompts reusable

Use clear placeholders, avoid user-specific assumptions, and include a short usage guide. Keep examples separate from the reusable core where practical.

## 10. Evaluate important behavior changes

For consequential prompts, maintain representative test cases and compare versions under recorded conditions. Report limitations and avoid claiming reliability from a small or unrepresentative sample.
