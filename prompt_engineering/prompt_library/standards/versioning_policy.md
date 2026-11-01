# Prompt Versioning Policy

Prompt assets use semantic-style version identifiers: `MAJOR.MINOR.PATCH`.

## Version increments

- **MAJOR** (`2.0.0`): incompatible change to the prompt's purpose, required inputs, output contract, or core behavior.
- **MINOR** (`1.1.0`): backward-compatible capability, instruction, or output improvement.
- **PATCH** (`1.0.1`): wording clarification, typo correction, or narrow fix that should not change intended behavior.

## Drafts and releases

A version number is an identifier, not evidence of maturity. Each prompt file must state one of:

- **Draft — not evaluated**
- **Under evaluation**
- **Evaluated — limitations documented**
- **Deprecated**

Use “validated,” “reliable,” or “production-ready” only when the project defines the supporting criteria and records sufficient evidence. A file named `v1.0.0.md` may still be a draft candidate.

## Immutable history

When a meaningful revision is made, add a new version file rather than silently replacing the old version. Keep prior versions available unless there is a documented reason to remove sensitive or harmful content.

## Changelog

Update `CHANGELOG.md` with the actual change, the affected prompt/version, and evaluation status where relevant. Do not record planned work as completed work. Do not describe an unrun evaluation as a test result.
