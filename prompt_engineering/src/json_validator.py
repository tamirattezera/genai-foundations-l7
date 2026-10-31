import json

ALLOWED_LABELS = {
    "PRODUCT_QUESTION",
    "ORDER_ISSUE",
    "OTHER",
}


def validate_response(response):
    if not isinstance(response, str):
        return False, "Response must be a string"

    try:
        data = json.loads(response)
    except json.JSONDecodeError:
        return False, "Invalid JSON"

    if not isinstance(data, dict):
        return False, "Expected a JSON object"

    if set(data.keys()) != {"label"}:
        return False, "Expected exactly one key: label"

    label = data["label"]

    if not isinstance(label, str):
        return False, "Label must be a string"

    if label not in ALLOWED_LABELS:
        return False, "Invalid classification label"

    return True, data