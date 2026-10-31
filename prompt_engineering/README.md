# Module 02 — Prompt Engineering & AI Productivity

A practical learning and experimentation workspace focused on designing effective prompts, evaluating AI outputs, validating structured data, and building reliable AI-assisted workflows.

## 1. Overview

**Learning path:** Generative AI Foundations → Prompt Engineering & AI Productivity

**Module:** 02
**Status:** In progress
**Primary language:** Python
**Testing framework:** Python `unittest`

This module moves beyond understanding how generative AI works toward using it systematically and evaluating its outputs.

The focus is not simply writing better prompts. It is learning to design controlled experiments, validate outputs, measure results, and build reusable workflows.

## 2. Learning Objectives

By completing this module, I aim to develop practical skills in:

- Designing reusable prompt templates.
- Applying zero-shot and few-shot prompting.
- Evaluating prompt effectiveness through controlled experiments.
- Generating and validating structured JSON outputs.
- Using AI tools for coding, debugging, research, and productivity.
- Building repeatable evaluation workflows.
- Documenting results and limitations with evidence.
- Organizing experiments and tools into a maintainable repository.

## 3. Engineering Workflow

Each practical task follows this process:

1. **Understand** — Define the problem and learning objective.
2. **Design** — Establish the approach, inputs, constraints, and expected behavior.
3. **Implement** — Build the prompt, experiment, or tool.
4. **Test** — Evaluate behavior using controlled examples and automated tests.
5. **Document** — Record methodology, results, limitations, and lessons.
6. **Commit** — Preserve verified progress with meaningful Git commits.

## 4. Experiments and Implementations

### PE-001 — Zero-Shot vs Few-Shot Prompting

**Status:** Completed

**Research question:** Does adding three labeled demonstrations improve classification accuracy on six unseen customer-support messages?

**Results:**
- Zero-shot: 6/6 (100%).
- Few-shot: 6/6 (100%).
- Accuracy difference: 0 percentage points.

**Conclusion:** The hypothesis that few-shot prompting would improve accuracy was not supported by this small experiment.

**Limitations:** Small dataset, ceiling effect, incomplete model settings, and missing original message-level evidence.

Experiment documentation:
- [PE-001 Overview](experiments/PE-001_zero_shot_vs_few_shot/README.md)
- [Zero-Shot Prompt](experiments/PE-001_zero_shot_vs_few_shot/prompts/zero_shot.md)
- [Few-Shot Prompt](experiments/PE-001_zero_shot_vs_few_shot/prompts/few_shot.md)
- [Evaluation Dataset](experiments/PE-001_zero_shot_vs_few_shot/data/evaluation_dataset.json)
- [Evaluation Summary](experiments/PE-001_zero_shot_vs_few_shot/results/evaluation_summary.json)
- [Final Report](experiments/PE-001_zero_shot_vs_few_shot/results/final_report.md)

### PE-002 — Structured Output Validation

**Status:** Implementation and unit testing completed.

**Objective:** Build a Python validator for a predefined JSON classification contract.

**Implementation:**
- JSON parsing using `json.loads()`.
- Input type checking.
- JSON object validation.
- Exact key validation.
- Classification label validation.
- Descriptive error handling.

**Automated testing:**
- 12 test cases.
- 12 passed.
- 0 failed.

[Read PE-002 Experiment Report](experiments/PE-002_structured_output/README.md)
### PE-002 — Structured Output Validation

**Objective:** Build a Python validator for a predefined JSON classification contract.

Implementation:

- JSON parsing using `json.loads()`.
- Input type checking.
- JSON object validation.
- Exact key validation.
- Classification label validation.
- Descriptive error handling.

**Automated testing:**

- 12 test cases.
- 12 passed.
- 0 failed.

Experiment report: `experiments/PE-002_structured_output/README.md`

**Key lesson:** Valid JSON syntax alone does not guarantee that data meets an application's requirements.

## 5. Current Repository Structure

```text
prompt_engineering/
├── README.md
├── data/
├── experiments/
│   └── PE-002_structured_output/
│       └── README.md
├── notebooks/
├── results/
├── src/
│   └── json_validator.py
└── tests/
    └── test_json_validator.py
```

Additional directories and artifacts will be introduced as the module progresses.

## 6. Running the Tests

Run the test suite from the repository root:

```bash
python -m unittest discover -s prompt_engineering/tests -v
```

Check the current Git diff for whitespace errors:

```bash
git diff --check
```

## 7. Module Deliverables

| Deliverable | Current status |
|---|---|
| Reusable Prompt Library | Planned |
| Prompt Experimentation and Evaluation | PE-001 completed |
| Structured Output Validation | Implemented and tested |
| AI-Assisted Coding and Debugging Experiment | Planned |
| AI Productivity Toolkit | Planned |
| Testing and Reproducibility | In progress |
| GitHub Documentation and Portfolio | In progress |
| Professional Communication | Planned |

A deliverable is considered complete only when its implementation or practical evidence, evaluation, and documentation are available.

## 8. Engineering Principles

- Evidence over assumptions.
- Controlled experiments over intuition.
- Validation over blind trust in AI outputs.
- Reproducibility over one-time success.
- Honest reporting of limitations.
- Small, testable implementations.
- Meaningful version-control history.

## 9. Expected Outcome

By the end of Module 02, this repository should contain a practical collection of prompt templates, evaluation experiments, validation tools, automated tests, productivity workflows, and documented engineering lessons.

The goal is to develop the judgment required to use AI effectively—not just to produce outputs, but to evaluate whether those outputs are useful, valid, and reliable.
