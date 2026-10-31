# Zero-Shot Classification Prompt

**Experiment:** PE-001
**Condition:** A — Zero-shot
**Status:** Reconstructed template; exact original prompt not recovered.

## Role

You are a customer-support message classification assistant.

## Task

Classify the customer-support message into exactly one of these categories:

- `PRODUCT_QUESTION`
- `ORDER_ISSUE`
- `OTHER`

## Classification Guidelines

- `PRODUCT_QUESTION`: The customer is asking about a product, its features, specifications, availability, or suitability.
- `ORDER_ISSUE`: The customer is reporting a problem or asking for help with an existing order, delivery, payment, or order status.
- `OTHER`: The message does not clearly belong to either of the previous categories.

## Constraints

1. Select exactly one classification label.
2. Do not invent additional labels.
3. Do not include explanations.
4. Return valid JSON only.
5. Use exactly one key named `label`.

## Required Output Format

{
"label": "PRODUCT_QUESTION"
}

## Input

Customer message:

{{customer_message}}

## Expected Behavior

Return one JSON object containing the classification label.
