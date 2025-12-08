import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.processor import DataProcessor


class TestDataProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = DataProcessor()

    def test_clean_whitespace_removes_empty_lines(self):
        items = ['hello', '  ', 'world', '\n', 'test']
        result = self.processor.clean_whitespace(items)
        self.assertEqual(result, ['hello', 'world', 'test'])

    def test_clean_whitespace_strips_leading_trailing_spaces(self):
        items = ['  hello  ', '  world  ', '  test  ']
        result = self.processor.clean_whitespace(items)
        self.assertEqual(result, ['hello', 'world', 'test'])

    def test_remove_duplicates_keeps_first_occurrence(self):
        items = ['apple', 'banana', 'apple', 'cherry', 'banana']
        result = self.processor.remove_duplicates(items)
        self.assertEqual(result, ['apple', 'banana', 'cherry'])

    def test_remove_duplicates_preserves_order(self):
        items = ['z', 'a', 'z', 'b', 'a']
        result = self.processor.remove_duplicates(items)
        self.assertEqual(result, ['z', 'a', 'b'])

    def test_normalize_case_to_lower(self):
        items = ['HELLO', 'World', 'TeSt']
        result = self.processor.normalize_case(items, 'lower')
        self.assertEqual(result, ['hello', 'world', 'test'])

    def test_normalize_case_to_upper(self):
        items = ['hello', 'World', 'test']
        result = self.processor.normalize_case(items, 'upper')
        self.assertEqual(result, ['HELLO', 'WORLD', 'TEST'])

    def test_normalize_case_to_title(self):
        items = ['hello world', 'test case', 'python programming']
        result = self.processor.normalize_case(items, 'title')
        self.assertEqual(result, ['Hello World', 'Test Case', 'Python Programming'])

    def test_normalize_case_to_sentence(self):
        items = ['hello world', 'test case', 'python']
        result = self.processor.normalize_case(items, 'sentence')
        self.assertEqual(result, ['Hello world', 'Test case', 'Python'])

    def test_parse_key_value_with_colons(self):
        items = ['name:john', 'age:30', 'city:new york']
        result = self.processor.parse_key_value(items)
        self.assertEqual(result[0], {'key': 'name', 'value': 'john'})
        self.assertEqual(result[1], {'key': 'age', 'value': '30'})
        self.assertEqual(result[2], {'key': 'city', 'value': 'new york'})

    def test_parse_key_value_without_colons(self):
        items = ['hello', 'world']
        result = self.processor.parse_key_value(items)
        self.assertEqual(result[0], {'raw': 'hello'})
        self.assertEqual(result[1], {'raw': 'world'})

    def test_parse_key_value_mixed(self):
        items = ['name:john', 'hello', 'age:30']
        result = self.processor.parse_key_value(items)
        self.assertEqual(result[0], {'key': 'name', 'value': 'john'})
        self.assertEqual(result[1], {'raw': 'hello'})
        self.assertEqual(result[2], {'key': 'age', 'value': '30'})

    def test_combined_operations(self):
        items = ['  HELLO  ', '  WORLD  ', '  HELLO  ', '  TEST  ']
        items = self.processor.clean_whitespace(items)
        self.assertEqual(items, ['HELLO', 'WORLD', 'HELLO', 'TEST'])
        items = self.processor.remove_duplicates(items)
        self.assertEqual(items, ['HELLO', 'WORLD', 'TEST'])
        items = self.processor.normalize_case(items, 'lower')
        self.assertEqual(items, ['hello', 'world', 'test'])


if __name__ == '__main__':
    unittest.main()
