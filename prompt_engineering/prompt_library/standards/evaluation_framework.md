# Prompt Evaluation Framework

This framework provides a repeatable approach to assessing prompt behavior. It does not imply that any prompt in this library has already been evaluated.

## 1. Define the evaluation question

State the behavior being assessed and why it matters. Keep the question narrow enough to answer with observable evidence.

## 2. Specify the test set

Record:

- Dataset source and selection method.
- Number and type of cases.
- Input text and relevant context, subject to privacy constraints.
- Expected behavior or reference answers and how they were established.
- Edge cases and out-of-scope cases.

Avoid evaluating only on examples used to design the prompt.

## 3. Record conditions

Capture prompt version, model/provider, date, relevant model settings, tools, context supplied, and any unavailable settings. If a condition is unknown, mark it unknown rather than guessing.

## 4. Define criteria before running

Choose criteria appropriate to the task. For code review, possible criteria include:

- Finding correctness and evidence support.
- Severity calibration.
- Detection of important issues.
- False-positive rate.
- Uncertainty handling.
- Actionability and scope discipline.
- Output-format compliance.

Define scoring rules before inspecting results where practical.

## 5. Run and preserve evidence

Keep raw outputs, case identifiers, scoring decisions, and failures. Record retries and nondeterministic behavior. Do not silently discard unfavorable outputs.

## 6. Analyze and report

Summarize counts and rates with denominators. Include representative successes and failures, limitations, and possible confounders. Small samples do not establish general reliability. Human reference labels may themselves be uncertain and should be documented.

## 7. Compare versions fairly

Use the same test set and comparable conditions when comparing versions. Explain any differences in model, settings, data, or evaluator. Do not attribute changes to the prompt alone when conditions also changed.

## 8. State status honestly

- **Not evaluated:** no documented evaluation run exists.
- **Under evaluation:** a run is in progress or evidence is incomplete.
- **Evaluated:** results and limitations are recorded.

Evaluation is not the same as formal validation or production readiness.
