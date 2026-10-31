# PE-001 — Final Experiment Report

## Zero-Shot vs Few-Shot Prompting

**Module:** Prompt Engineering & AI Productivity
**Experiment ID:** PE-001
**Status:** Completed
**Report type:** Reconstructed from available historical results

## 1. Executive Summary

This experiment investigated whether adding three labeled demonstrations to a classification prompt improves the accuracy of an AI model on unseen customer-support messages.

Two conditions were compared:

- Zero-shot prompting.
- Few-shot prompting with three labeled demonstrations.

Both approaches achieved 100% reported accuracy across six evaluation messages.

The observed accuracy improvement was zero percentage points. The hypothesis that few-shot prompting would improve accuracy was not supported by this experiment.

## 2. Research Question

Does few-shot prompting with three labeled demonstrations improve classification accuracy compared with zero-shot prompting?

## 3. Hypothesis

Few-shot prompting will perform better because demonstrations provide additional context about the expected classification behavior.

## 4. Methodology

### Task

Classify customer-support messages into predefined categories.

### Experimental Conditions

**Condition A — Zero-shot**

The model received classification instructions without labeled demonstrations.

**Condition B — Few-shot**

The model received classification instructions and three labeled demonstrations before classifying the evaluation messages.

### Evaluation Dataset

- Total messages: 6.
- Message type: Unseen customer-support messages.
- Evaluation metric: Accuracy.

The original message text and expected labels were not preserved in the current repository.

### Accuracy Formula

Accuracy = (Correct Predictions / Total Predictions) × 100

## 5. Results

| Metric                | Zero-shot | Few-shot |
| --------------------- | --------: | -------: |
| Total messages        |         6 |        6 |
| Correct predictions   |         6 |        6 |
| Incorrect predictions |         0 |        0 |
| Accuracy              |      100% |     100% |

### Observed Difference

Few-shot accuracy − Zero-shot accuracy

100% − 100% = 0 percentage points.

## 6. Hypothesis Evaluation

**Original hypothesis:** Few-shot prompting will improve classification accuracy.

**Observed result:** Both approaches achieved the same reported accuracy.

**Decision:** The hypothesis was not supported by the available experimental evidence.

This result does not prove that few-shot prompting is ineffective. It only shows that no accuracy improvement was observed in this small evaluation.

## 7. Limitations

### Small Sample Size

Six messages are insufficient to establish broad conclusions about prompting effectiveness.

### Ceiling Effect

Both approaches achieved 100% accuracy. This leaves no room for an accuracy improvement within this sample.

### Incomplete Experiment Records

The following historical evidence was not preserved:

- Exact original prompts.
- Original evaluation messages and expected labels.
- Individual model predictions.
- Complete model configuration.

The prompts in this repository are reconstructed templates, not verified copies of the originals.

### No Repeated Runs

The experiment did not include repeated runs to evaluate output consistency.

## 8. Key Findings

1. Zero-shot prompting achieved perfect reported accuracy in this test.
2. Few-shot prompting also achieved perfect reported accuracy.
3. Adding three demonstrations produced no observed accuracy improvement.
4. A small evaluation dataset limits the strength of the conclusion.
5. Complete experiment records are necessary for reproducibility.

## 9. Lessons Learned

### Prompt Engineering

More examples do not automatically produce better results. Prompt effectiveness depends on the task, examples, model, and evaluation dataset.

### Experimental Design

A good experiment needs a clear research question, controlled conditions, measurable outcomes, and an evaluation dataset.

### AI Evaluation

A high accuracy score is not enough to establish general reliability. Dataset size, class distribution, repeated runs, and error analysis matter.

### Reproducibility

Exact prompts, model settings, input datasets, and raw outputs should be preserved during experimentation rather than reconstructed afterward.

## 10. Future Improvements

A stronger follow-up experiment should:

- Use a larger and more diverse evaluation dataset.
- Preserve the exact prompts and all model settings.
- Save every model prediction.
- Repeat runs under controlled conditions.
- Compare accuracy and per-class performance.
- Include error analysis and consistency measurements.

## 11. Final Conclusion

In the completed PE-001 experiment, zero-shot and few-shot prompting both achieved 6/6 correct classifications, corresponding to 100% accuracy.

The observed improvement was zero percentage points.

The experiment did not support the hypothesis that few-shot prompting would improve accuracy in this particular test.

The most important outcome was learning how to compare prompting strategies using measurable results rather than assuming that a more elaborate prompt is automatically better.

---

**Final status:** Experiment completed. Aggregate results documented. Original raw evidence remains incomplete.
