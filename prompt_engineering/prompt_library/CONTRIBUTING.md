# Contributing to the Prompt Library

This guide defines how to add or revise prompt assets while keeping them understandable, reusable, and evidence-based.

## Before making a change

1. Read the [design principles](standards/prompt_design_principles.md) and [versioning policy](standards/versioning_policy.md).
2. Search the existing library before creating a new category or duplicating an asset.
3. Identify the user, task, inputs, boundaries, and expected output.
4. Preserve existing work; make focused changes and explain any replacement.

## Adding a prompt

1. Choose the narrowest appropriate category.
2. Create a prompt specification using [the prompt template](standards/prompt_template.md).
3. Include a version identifier and an explicit development status.
4. Add representative input examples when they materially clarify use.
5. Add expected findings or expected outputs only when they can be justified independently of a model run.
6. Link the asset from the relevant category README and the library README when appropriate.
7. Add a changelog entry describing the actual repository change.

## Revising a prompt

- Keep the existing version file unchanged when preserving a historical version.
- Create a new version file according to the [versioning policy](standards/versioning_policy.md).
- Document the reason for the change and the behavior expected to change.
- Do not claim an improvement until a comparable evaluation supports it.

## Evaluating a prompt

Use the [evaluation framework](standards/evaluation_framework.md) and [evaluation template](standards/evaluation_template.md). Record the exact prompt version and test conditions. Separate observed results from interpretation and limitations. If no evaluation was run, say so plainly.

## Documentation quality checklist

- [ ] Purpose, inputs, constraints, and output contract are clear.
- [ ] Placeholders are named and explained.
- [ ] Uncertainty and unsupported assumptions are handled explicitly.
- [ ] Examples match the prompt's intended behavior.
- [ ] Severity labels and terminology are consistent.
- [ ] Relative links resolve.
- [ ] Version and development status are accurate.
- [ ] Changelog describes changes actually made.
- [ ] No unsupported performance, testing, or validation claims are present.
