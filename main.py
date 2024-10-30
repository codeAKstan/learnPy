import unittest


def divide_numbers(numerator, denominator):
    if denominator == 0:
        raise ValueError("Cannot divide by zero")
    return numerator / denominator


class TestDivideNumbers(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(divide_numbers(10, 2), 5)
        self.assertEqual(divide_numbers(15, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(divide_numbers(-10, 2), -5)
        self.assertEqual(divide_numbers(10, -2), -5)
        self.assertEqual(divide_numbers(-10, -2), 5)

    def test_zero_numerator(self):
        self.assertEqual(divide_numbers(0, 5), 0)
        self.assertEqual(divide_numbers(0, -5), 0)

    def test_one_as_numerator_or_denominator(self):
        self.assertEqual(divide_numbers(1, 5), 0.2)
        self.assertEqual(divide_numbers(5, 1), 5)
        self.assertEqual(divide_numbers(-1, 5), -0.2)
        self.assertEqual(divide_numbers(5, -1), -5)

    def test_floating_point_numbers(self):
        self.assertAlmostEqual(divide_numbers(10.5, 2), 5.25)
        self.assertAlmostEqual(divide_numbers(-10.5, 2), -5.25)
        self.assertAlmostEqual(divide_numbers(10.5, -2), -5.25)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError) as context:
            divide_numbers(10, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")

        with self.assertRaises(ValueError) as context:
            divide_numbers(0, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")


if __name__ == '__main__':
    unittest.main()
