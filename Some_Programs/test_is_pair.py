"""
Test
"""
import unittest
from is_pair import is_pair


class TestIsPair(unittest.TestCase):
    def test_is_pair(self):
        self.assertEqual(is_pair( 2 ), True)
        self.assertEqual(is_pair( 409 ), False)
        self.assertEqual(is_pair( 90 ), True)
        self.assertEqual(is_pair( 89 ), False)
        self.assertEqual(is_pair( 3 ), False)

        self.assertEqual(is_pair( 89.34 ), False)
        self.assertEqual(is_pair( 12.2 ), False)

        # Excepts
        self.assertRaises(ValueError, is_pair, 'hola')
        self.assertRaises(ValueError, is_pair, "jdksksj")
        self.assertRaises(ValueError, is_pair, False)
        self.assertRaises(ValueError, is_pair, True)
        self.assertRaises(ValueError, is_pair, ['2', True])
        self.assertRaises(ValueError, is_pair, ({'name': 'Daniel'}))


if __name__ == '__main__':
    unittest.main()
