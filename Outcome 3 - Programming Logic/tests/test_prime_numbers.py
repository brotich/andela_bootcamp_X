import unittest
from prime_numbers import PrimeNumbers

class PrimeNumberTest(unittest.TestCase):

    def test_prime_raises_type_error_input_string(self):
        self.assertRaises(TypeError, PrimeNumbers().prime, "one")

    def test_prime_raises_type_error_input_list(self):
        self.assertRaises(TypeError, PrimeNumbers().prime, [1,2,3] )

    def test_prime_raise_value_error_int_equal_zero(self):
        self.assertRaises(ValueError, PrimeNumbers().prime, 0);

    def test_prime_raise_value_error_int_negative_one(self):
        self.assertRaises(ValueError, PrimeNumbers().prime, -1);

    def test_prime_upto_two(self):
        self.assertEqual(PrimeNumbers().prime(2), [2], msg="Expected [2]")

    def test_prime_upto_ten(self):
        self.assertEqual(PrimeNumbers().prime(12), [2, 3, 5, 7, 11], msg="Expected [[2, 3, 5, 7, 11]")

    def test_prime_upto_twenty(self):
        self.assertEqual(PrimeNumbers().prime(20), [2, 3, 5, 7, 11, 13, 17, 19], msg="Expected [2, 3, 5, 7, 11, 13, 17, 19]")    


if __name__ == '__main__':
    unittest.main()