# Prompt Evaluations

This directory stores evidence from actual prompt evaluation runs. Keep evaluation artifacts separate from prompt specifications and illustrative examples.

## What belongs here

For each evaluated asset, create a directory named with its stable asset ID and version, for example:

```text
 evaluations/
 └── SE-CODE-REVIEW-001_v1.0.0/
     ├── README.md
     ├── dataset/       # approved, non-sensitive test cases
     ├── raw_outputs/   # model outputs, with secrets removed
     └── results/       # scoring and analysis
```

Use the [evaluation framework](../standards/evaluation_framework.md) and [evaluation template](../standards/evaluation_template.md).

## Evidence requirements

Record the exact prompt version, run date, model/provider and settings when known, dataset provenance, scoring criteria, raw outputs, results, failures, and limitations. Mark unavailable conditions as unknown. Protect credentials, personal data, and confidential source code; do not commit secrets or sensitive production data.

## Current evaluation status

No evaluation run is currently documented for the Code Review prompt `SE-CODE-REVIEW-001 v1.0.0`. The example's [expected findings](../software_engineering/code_review/examples/expected_findings.md) are a human-authored reference only, not evaluation evidence.
