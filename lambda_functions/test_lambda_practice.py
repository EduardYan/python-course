"""
Test
"""
import unittest
from lambda_practice import add_2


class TestLambda(unittest.TestCase):
    def setUp(self):
        print('Setup')

    def setDown(self):
        print('SetDown')

    def test_add_2(self):
        # Testing with the values
        self.assertEqual(add_2(12, 45.6), 57.6)
        self.assertEqual(add_2(23, 10), 33)
        self.assertEqual(add_2(12, 12), 24)

        self.assertNotEqual(add_2(23, 23), 89)

        # Excepts
        self.assertRaises(TypeError, add_2, 'jsksksks')
        self.assertRaises(TypeError, add_2, 77.0)
        self.assertRaises(TypeError, add_2, 12)
        self.assertRaises(TypeError, add_2, ['jsksl', True, False])
        self.assertRaises(TypeError, add_2, False)


if __name__ == '__main__':
    unittest.main()
