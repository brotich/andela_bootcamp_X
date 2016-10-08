import unittest
from fibonacci import Fibonacci

class FibonacciTest(unittest.TestCase):
    
    def test_fib_raises_type_error_input_string(self):
        self.assertRaises(TypeError, Fibonacci().fib, "one")

    def test_fib_raises_type_error_input_list(self):
        self.assertRaises(TypeError, Fibonacci().fib, [1,2,3] )

    def test_fib_raise_value_error_int_equal_zero(self):
        self.assertRaises(ValueError, Fibonacci().fib, 0);

    def test_fib_raise_value_error_int_negative_one(self):
        self.assertRaises(ValueError, Fibonacci().fib, -1);

    def test_fib_three_numbers(self):
        self.assertEqual(Fibonacci().fib(3), [0, 1, 1], msg="Expected [0, 1, 1]")

    def test_fib_ten_numbers(self):
        self.assertEqual(Fibonacci().fib(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34], msg="Expected [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]")



if __name__ == '__main__':
    unittest.main()