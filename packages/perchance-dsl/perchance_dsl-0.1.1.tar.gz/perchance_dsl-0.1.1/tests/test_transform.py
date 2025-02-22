import unittest
from perchance.transform import transform_code

class TestTransform(unittest.TestCase):
    def test_if_replacement(self):
        source = "perchance a == b:\n    print('hello')"
        result = transform_code(source)
        # Verify that 'perchance' is replaced with 'if'
        self.assertNotIn("perchance", result)
        self.assertIn("if a == b:", result)

    def test_elif_replacement(self):
        source = "or perchance a == c:\n    print('elif')"
        result = transform_code(source)
        # Verify that 'or perchance' is replaced with 'elif'
        self.assertNotIn("or perchance", result)
        self.assertIn("elif a == c:", result)

    def test_else_replacement(self):
        source = "certainly:\n    print('else')"
        result = transform_code(source)
        # Verify that 'certainly' is replaced with 'else'
        self.assertNotIn("certainly", result)
        self.assertIn("else:", result)

    def test_combined_replacement(self):
        source = (
            "perchance a == b:\n"
            "    print('if')\n"
            "or perchance a == c:\n"
            "    print('elif')\n"
            "certainly:\n"
            "    print('else')\n"
        )
        result = transform_code(source)
        # Check that all DSL keywords have been replaced
        self.assertNotIn("perchance", result)
        self.assertNotIn("or perchance", result)
        self.assertNotIn("certainly", result)
        self.assertIn("if a == b:", result)
        self.assertIn("elif a == c:", result)
        self.assertIn("else:", result)

    def test_keywords_in_strings(self):
        # Ensure that keywords inside string literals remain unchanged
        source = (
            "def greet():\n"
            "    print(\"This is a chance: perchance, or certainly not!\")\n"
        )
        result = transform_code(source)
        self.assertIn("perchance, or certainly not!", result)
        self.assertIn("def greet():", result)

if __name__ == '__main__':
    unittest.main()
