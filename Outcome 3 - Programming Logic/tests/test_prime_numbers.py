import unittest
from prime_numbers import PrimeNumbers

class PrimeNumberTest(unittest.TestCase):

  def test_prime_upto_ten(self):
    self.assertEqual(PrimeNumbers().prime(12), [2, 3, 5, 7, 11], msg="Expected [[2, 3, 5, 7, 11]")

  def test_prime_upto_two(self):
    self.assertEqual(PrimeNumbers().prime(2), [2], msg="Expected [2]")



if __name__ == '__main__':
    unittest.main()