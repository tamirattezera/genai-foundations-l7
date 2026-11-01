# Code Review Prompt

A reusable prompt specification for evidence-based review of supplied source code.

## Asset

- **Version:** [v1.0.0](v1.0.0.md)
- **Status:** **Draft — not evaluated**
- **Category:** Software Engineering

## Intended use

Use this prompt to identify and explain potential defects in a focused code snippet or change. It asks for evidence, impact, severity, uncertainty, and targeted recommendations. It is an assistant to human review, not a substitute for tests, security analysis, or domain knowledge.

## Example materials

- [Sample input](examples/sample_input.md)
- [Expected findings reference](examples/expected_findings.md)

The expected findings are a manually reasoned reference for the sample, not model-generated evaluation results.

## Inputs

Provide the code under review, language/framework, intended behavior, relevant surrounding context, and any review focus. Mark unavailable context explicitly.

## Output at a glance

The prompt requests a concise summary, prioritized findings, evidence, impact, confidence/status, targeted recommendation, verification steps, and questions for missing context. It also allows an explicit no-findings result bounded by the supplied material.

## Evaluation status

No model run or prompt evaluation is recorded for this asset. Do not interpret the sample and expected findings as proof that the prompt detects issues correctly. See the [evaluation framework](../../standards/evaluation_framework.md) and [evaluation records guide](../../evaluations/README.md) before evaluating it.
