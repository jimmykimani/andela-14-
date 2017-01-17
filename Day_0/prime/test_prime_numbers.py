import prime_numbers
import unittest


class PrimeNumbersTest(unittest.TestCase):
    """prime number test for Integer,  """

    def test_if_value_is_integer(self):
        self.assertEqual(prime_numbers.prime_numbers("three"), "only Integers alowed")
    def test_zero_is_not_prime(self):
        self.assertEqual(prime_numbers.prime_numbers(0), "Prime numbers start from 2")

    def test_prime_numbers_are_returned_in_a_list(self):
        self.assertEqual(type(prime_numbers.prime_numbers(3)), list)

    def test_input_value_is_included_in_range_if_input_value_is_prime_number(self):
        self.assertEqual(prime_numbers.prime_numbers(101)[-1], 101)

    def test_one_is_not_prime(self):
        self.assertEqual(prime_numbers.prime_numbers(1), "Prime numbers start from 2")

    def test_two_is_prime(self):
        self.assertEqual(prime_numbers.prime_numbers(2), [2])

    def test_negative_value_inputs(self):
        self.assertEqual(prime_numbers.prime_numbers(-2), "negative numbers are not allowed")

    def test_two_is_the_first_value_returned_by_inputs_equal_to_and_greater_than_two(self):
        self.assertEqual(prime_numbers.prime_numbers(500)[0], 2)

    def test_even_numbers_are_absent_in_the_returned_result(self):
        self.assertNotEqual((i for i in prime_numbers.prime_numbers(10) if i % 2 == 0), [2, 3, 4, 5, 6, 7, 8])
    def test_if_function_validity(self):
        self.assertEqual(prime_numbers.prime_numbers(100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])



if __name__ == '__main__':
    unittest.main()
