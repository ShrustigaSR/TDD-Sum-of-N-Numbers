import unittest
import timeit
import sys
sys.path.append('C:/users/shrustiga.sr/Desktop/Intern_Exercise-1-18')

from Sample.sum_of_n import *

class SumofNNumbersTest(unittest.TestCase):
    def test_zero_input_sum(self):
        """Test Calculation with zero input"""
        total = SumOfNNumbers(0)
        expected_sum = 0

        self.assertEqual(total.calculate_sum(),expected_sum)
    
    def test_negative_input_sum(self):
        """Handling negative inputs"""
        total = SumOfNNumbers(-2)

        with self.assertRaises(ValueError) as message:
            total.calculate_sum()
        self.assertEqual(str(message.exception),"Enter Positive Integer")


    def test_decimal_input_sum(self):
        """Handling decimal inputs"""
        total = SumOfNNumbers(1.2)
        with self.assertRaises(ValueError) as message:
            total.calculate_sum()
        self.assertEqual(str(message.exception),"Enter Positive Integer")

    def test_alpha_input_sum(self):
        """Handling Non-numeric inputs"""
        total = SumOfNNumbers("r")

        with self.assertRaises(ValueError) as message:
            total.calculate_sum()
        self.assertEqual(str(message.exception),"Enter Positive Integer")

        total = SumOfNNumbers("#")
        
        with self.assertRaises(ValueError) as message:
            total.calculate_sum()
        self.assertEqual(str(message.exception),"Enter Positive Integer")


    def test_small_input_sum(self):
        """Checking program's functionality"""
        total = SumOfNNumbers(10)
        expected_sum = sum(list(range(1,11)))

        self.assertEqual(total.calculate_sum(),expected_sum)

    def test_large_input_sum(self):
        """Test calculation with large positive input"""
        total = SumOfNNumbers(100000)
        expected_sum = sum(list(range(1,100001)))

        execution_time = timeit.timeit(total.calculate_sum,number = 1000)
        max_allowed_time = 0.1
        self.assertLessEqual(execution_time,max_allowed_time)
        self.assertEqual(total.calculate_sum(),expected_sum)


if __name__ == '__main__':
    unittest.main()