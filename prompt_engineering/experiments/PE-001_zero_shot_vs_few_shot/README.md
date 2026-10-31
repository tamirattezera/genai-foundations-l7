# PE-001 — Zero-Shot vs Few-Shot Prompting

## 1. Experiment Overview

**Module:** Module 02 — Prompt Engineering & AI Productivity
**Experiment ID:** PE-001
**Topic:** Zero-Shot vs Few-Shot Prompting
**Status:** Experiment completed; original raw artifacts not fully preserved.

### Objective

Investigate whether adding three labeled demonstrations to a classification prompt improves the accuracy of an AI model when classifying unseen customer-support messages.

## 2. Research Question

Does few-shot prompting with three labeled examples improve classification accuracy compared with zero-shot prompting?

## 3. Hypothesis

Few-shot prompting will achieve higher classification accuracy than zero-shot prompting because demonstrations provide examples of the expected input-to-label relationship.

## 4. Experimental Design

Two prompting conditions were compared.

| Condition     | Description                                                    |
| ------------- | -------------------------------------------------------------- |
| A — Zero-shot | Classification instructions without labeled demonstrations     |
| B — Few-shot  | The same classification task with three labeled demonstrations |

Both conditions were evaluated using six unseen customer-support messages.

The intended comparison was based on classification accuracy.

## 5. Results

| Metric                | Zero-shot | Few-shot |
| --------------------- | --------: | -------: |
| Evaluation messages   |         6 |        6 |
| Correct predictions   |         6 |        6 |
| Incorrect predictions |         0 |        0 |
| Accuracy              |      100% |     100% |

**Observed accuracy difference:** 0 percentage points.

## 6. Interpretation

The hypothesis that few-shot prompting would improve classification accuracy was not supported by this experiment.

Both approaches achieved 100% accuracy on the six evaluated messages.

This does not establish that zero-shot and few-shot prompting are equally effective in general. The small dataset and ceiling effect limit the strength of the conclusion.

## 7. Limitations

- Only six evaluation messages were used.
- Both conditions achieved perfect accuracy, creating a ceiling effect.
- Complete model settings were not preserved.
- Repeated experimental runs were not performed.
- Original message-level predictions and exact prompt wording were not preserved in the repository.

## 8. Reproducibility and Evidence

This repository contains a reconstructed description of the experiment.

The reported aggregate results are preserved from the completed experiment. The prompt files are reconstructed templates, not verified copies of the original prompts.

The original evaluation messages and raw predictions have not been recovered. The dataset file therefore documents this evidence gap instead of inventing historical observations.

## 9. Key Lessons

1. Zero-shot prompting can perform well when task instructions are sufficiently clear.
2. Few-shot prompting does not guarantee better performance.
3. Accuracy alone is insufficient when the evaluation dataset is very small.
4. A ceiling effect can hide differences between prompting strategies.
5. Prompt experiments should preserve exact prompts, model settings, datasets, and raw outputs.
6. Reproducibility is part of responsible AI experimentation.

## 10. Conclusion

In this experiment, zero-shot and few-shot prompting both achieved 100% accuracy across six customer-support messages.

The observed improvement was zero percentage points. The initial hypothesis was therefore not supported by the available evidence.

A larger dataset, repeated runs, and complete experiment records would be required to draw stronger conclusions.

---

**Final status:** Completed experiment; documentation reconstructed from the available historical results.
