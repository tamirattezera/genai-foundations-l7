import unittest

from prompt_engineering.src.json_validator import validate_response


class TestValidateResponse(unittest.TestCase):

    def test_accepts_product_question(self):
        response = '{"label": "PRODUCT_QUESTION"}'

        is_valid, data = validate_response(response)

        self.assertTrue(is_valid)
        self.assertEqual(data, {"label": "PRODUCT_QUESTION"})

    def test_accepts_order_issue(self):
        response = '{"label": "ORDER_ISSUE"}'

        is_valid, data = validate_response(response)

        self.assertTrue(is_valid)
        self.assertEqual(data, {"label": "ORDER_ISSUE"})

    def test_accepts_other(self):
        response = '{"label": "OTHER"}'

        is_valid, data = validate_response(response)

        self.assertTrue(is_valid)
        self.assertEqual(data, {"label": "OTHER"})
    def test_rejects_invalid_json(self):
        response = "not JSON"

        is_valid, error = validate_response(response)

        self.assertFalse(is_valid)
        self.assertEqual(error, "Invalid JSON")
    def test_rejects_json_number(self):
        response = "42"

        is_valid, error = validate_response(response)

        self.assertFalse(is_valid)
        self.assertEqual(error, "Expected a JSON object")
    def test_rejects_missing_label_key(self):
        response = '{"category": "OTHER"}'

        is_valid, error = validate_response(response)

        self.assertFalse(is_valid)
        self.assertEqual(error, "Expected exactly one key: label")
    def test_rejects_extra_keys(self):
        response = '{"label": "OTHER", "confidence": 0.95}'

        is_valid, error = validate_response(response)

        self.assertFalse(is_valid)
        self.assertEqual(error, "Expected exactly one key: label")
    def test_rejects_unknown_label(self):
        response = '{"label": "UNKNOWN"}'

        is_valid, error = validate_response(response)

        self.assertFalse(is_valid)
        self.assertEqual(error, "Invalid classification label")
    def test_rejects_integer_label(self):
        response = '{"label": 42}'

        is_valid, error = validate_response(response)

        self.assertFalse(is_valid)
        self.assertEqual(error, "Label must be a string")
    def test_rejects_null_label(self):
        response = '{"label": null}'

        is_valid, error = validate_response(response)

        self.assertFalse(is_valid)
        self.assertEqual(error, "Label must be a string")
    def test_rejects_none_input(self):
        response = None

        is_valid, error = validate_response(response)

        self.assertFalse(is_valid)
        self.assertEqual(error, "Response must be a string")
    def test_rejects_empty_string(self):
        response = ""

        is_valid, error = validate_response(response)

        self.assertFalse(is_valid)
        self.assertEqual(error, "Invalid JSON")

if __name__ == "__main__":
    unittest.main()