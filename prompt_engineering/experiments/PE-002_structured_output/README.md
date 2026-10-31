# PE-002 — Structured Output Validation

## 1. Experiment Overview

**Module:** Prompt Engineering & AI Productivity
**Experiment ID:** PE-002
**Topic:** Structured Output Validation
**Status:** Implementation and unit testing completed

### Objective

Build and test a Python validator that checks whether a JSON response follows a predefined structure and contains an allowed classification label.

The goal is to understand how to make structured data more reliable when working with AI-generated outputs.

## 2. Research Question

Can a Python validation function reliably reject malformed JSON, incorrect data structures, missing or extra fields, and unsupported classification labels?

## 3. Expected JSON Contract

The validator expects a JSON object containing exactly one key: `label`.

The accepted labels are:

- `PRODUCT_QUESTION`
- `ORDER_ISSUE`
- `OTHER`

Example of a valid response:

```json
{
  "label": "PRODUCT_QUESTION"
}
```

Examples of invalid responses:

```json
{ "category": "OTHER" }
```

```json
{ "label": "UNKNOWN" }
```

```json
{ "label": "OTHER", "confidence": 0.95 }
```

## 4. Implementation

**Source file:** `prompt_engineering/src/json_validator.py`

The implementation uses Python's built-in `json` module.

Validation checks:

1. Confirm the input is a string.
2. Parse the input using `json.loads()`.
3. Confirm the parsed value is a dictionary (JSON object).
4. Require exactly one key: `label`.
5. Confirm the label is a string.
6. Check that the label belongs to the allowed set.
7. Return a success result or a descriptive error.

## 5. Testing Methodology

**Test file:** `prompt_engineering/tests/test_json_validator.py`

The test suite uses Python's built-in `unittest` framework.

It covers 12 cases:

| Test case                     | Expected behavior |
| ----------------------------- | ----------------- |
| Valid PRODUCT_QUESTION        | Accept            |
| Valid ORDER_ISSUE             | Accept            |
| Valid OTHER                   | Accept            |
| Malformed JSON                | Reject            |
| JSON number instead of object | Reject            |
| Missing label key             | Reject            |
| Extra JSON key                | Reject            |
| Unknown classification label  | Reject            |
| Integer label                 | Reject            |
| Null label                    | Reject            |
| Python None input             | Reject            |
| Empty string                  | Reject            |

## 6. Results

**Test command:**

```bash
python -m unittest discover -s prompt_engineering/tests -v
```

**Observed result:**

- Tests run: 12
- Passed: 12
- Failed: 0
- Errors: 0

**Result:** All 12 tests passed.

The formatting and whitespace verification command also completed successfully:

```bash
git diff --check
```

No output was produced, indicating no whitespace errors were detected.

## 7. Limitations

This experiment validates JSON responses supplied to the Python function. It does not measure how frequently an LLM generates valid JSON.

The experiment also does not yet cover:

- JSON Schema validation.
- Nested objects and arrays.
- Additional field types and constraints.
- Real LLM-generated response samples.
- Repeated model runs and structured-output reliability metrics.

These are possible future improvements.

## 8. Key Engineering Lessons

1. Valid JSON syntax does not guarantee valid application data.
2. Parsing and validation are separate responsibilities.
3. Structural validation should check both required fields and unexpected fields.
4. Type checking prevents invalid values from entering application logic.
5. Automated tests make validation behavior reproducible.
6. Clear error messages make debugging easier.

## 9. Conclusion

The PE-002 implementation successfully validates a small, explicitly defined JSON classification contract.

All 12 unit tests passed, providing evidence that the implemented validation rules behave as expected for the tested inputs.

This establishes a foundation for more advanced structured-output validation and future experiments involving actual LLM-generated responses.

---

**Experiment status:** Validator implementation and unit tests completed. Documentation recorded. Further LLM reliability evaluation remains future work.
