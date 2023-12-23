"""
Test is_empty
"""
import unittest
from is_empty import join_word


class TestIsEmpty(unittest.TestCase):
    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

    def test_join_word(self):
        print('test join_word')
        list_empty = []
        self.assertEqual(join_word('hola', list_empty), ['hola'])


if __name__ == '__main__':
    unittest.main()
