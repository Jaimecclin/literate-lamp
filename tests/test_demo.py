import unittest
from unittest.mock import Mock, MagicMock, patch
from src.demo import Demo, ValueError, SpecialError
import datetime

class MockInteger:

    @staticmethod
    def get_int(num):
        return num + 1

class TestDemo(unittest.TestCase):

    def test_basic(self):
        demo = Demo(1, 2)
        self.assertEqual(1, demo.num1)
        self.assertEqual(2, demo.num2)
        self.assertEqual(1, demo._special_number())
        self.assertEqual(4, demo.sum())
        self.assertEqual(8, demo.sum_bias())
    
    def test_raise_error(self):
        demo = Demo(1, 2)
        demo._special_number = MagicMock(return_value=-1)
        with self.assertRaises(ValueError):
            demo.sum()
        demo._special_number.assert_called_with()

    def test_raise_error_side_effect(self):
        demo = Demo(1, 2)
        demo._special_number = MagicMock(side_effect=SpecialError)
        with self.assertRaises(SpecialError):
            demo.sum()
        demo._special_number.assert_called_with()
    
    def test_raise_error_patch(self):    
        with patch.object(Demo, '_special_number', return_value=-1) as mocked_mathod:
            demo = Demo(1, 2)
            with self.assertRaises(ValueError):
                demo.sum()
        mocked_mathod.assert_called_once_with()

    def test_mock_sum_bias(self):
        demo = Demo(1, 2)
        self.assertEqual(8, demo.sum_bias())

    @patch('src.demo.Bias')
    def test_sum_bias(self, mocked_bias):
        mocked_bias.get_bias.return_value = 7
        demo = Demo(1, 2)
        self.assertEqual(10, demo.sum_bias())

    def test_datetime(self):
        demo = Demo(1, 2)
        self.assertTrue('abc' in demo.append_datetime('abc'))
    
    @patch('src.demo.datetime')
    def test_mock_datetime(self, mocked_datetime):
        mocked_datetime.datetime.today.return_value = 'This is a mocked method'
        demo = Demo(1, 2)
        self.assertTrue('mocked' in demo.append_datetime('abc'))
        mocked_datetime.datetime.today.assert_called_once()

if __name__ == '__main__':
    unittest.main()