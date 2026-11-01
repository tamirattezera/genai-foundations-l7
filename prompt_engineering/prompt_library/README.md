# Prompt Library

A collection of reusable, versioned prompt templates developed as part of **Module 02 — Prompt Engineering & AI Productivity**.

## Purpose

This library treats prompts as maintainable engineering assets rather than one-time conversations. Each asset documents its purpose, inputs, constraints, expected output, limitations, and version history.

## Repository map

```text
prompt_library/
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── standards/
│   ├── prompt_design_principles.md
│   ├── versioning_policy.md
│   ├── evaluation_framework.md
│   ├── prompt_template.md
│   └── evaluation_template.md
├── software_engineering/
│   └── code_review/
│       ├── README.md
│       ├── v1.0.0.md
│       └── examples/
│           ├── sample_input.md
│           └── expected_findings.md
└── evaluations/
    └── README.md
```

## Prompt categories

### Software engineering

- [Code Review](software_engineering/code_review/README.md) — structured review with evidence-based findings, uncertainty labels, severity, impact, and targeted recommendations.

## Standards and contribution

- [Prompt design principles](standards/prompt_design_principles.md)
- [Versioning policy](standards/versioning_policy.md)
- [Evaluation framework](standards/evaluation_framework.md)
- [Reusable prompt specification template](standards/prompt_template.md)
- [Evaluation report template](standards/evaluation_template.md)
- [Contribution guide](CONTRIBUTING.md)

## Versioning

Prompt assets use semantic-style version identifiers (`MAJOR.MINOR.PATCH`). A filename such as `v1.0.0.md` identifies the documented candidate version; it does not by itself mean the prompt is stable, validated, or production-ready. Development and evaluation status must be stated inside each prompt specification.

See [Versioning Policy](standards/versioning_policy.md) for increment rules.

## Evaluation policy

A prompt must not be described as evaluated, validated, reliable, or production-ready without recorded evidence. Evaluation records should identify the prompt version, model and settings when known, test cases, criteria, results, limitations, and date. The [evaluation directory guide](evaluations/README.md) defines how evidence is stored.

## Current status

The initial Code Review asset is documented as **Draft — not evaluated**. Its example and expected findings provide a review exercise and an evaluation starting point; they are not evidence that a model followed the prompt successfully.

No automated prompt-evaluation or regression run is claimed by this documentation package.
