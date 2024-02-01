"""
Contains a Python program that:
-accepts a list of integers
-emits an error message if the list is not a multiple of 10 in length
-returns or prints a list of integers based on the input list, but with items
at positions which are a multiple of 2 or 3 removed
"""


import unittest


def process_list(lst):
    """Accept a list of integers and returns a list of integers based on the
    input list with items at positions which are a multiple of 2 or 3 removed

    Args: lst (list): list of integers
    Returns: result (list): list of integers with items at positions which are
    a multiple of 2 or 3 removed
    """

    result = []
    n = len(lst)

    if n % 10 != 0:
        raise ValueError("list is not a multiple of 10 in length")
    else:
        for i in range(n):
            if (i + 1) % 2 != 0 and (i + 1) % 3 != 0:
                result.append(lst[i])
    return result


class TestProcessList(unittest.TestCase):
    """Test process_list function."""

    def test_valid_input(self):
        """Test valid output."""
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                      11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.assertEqual(process_list(input_list), [
                         1, 5, 7, 11, 13, 17, 19])

    def test_invalid_length(self):
        """Test invalid length."""
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                      10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        with self.assertRaises(ValueError):
            process_list(input_list)

    def test_empty_input(self):
        """Test empty input."""
        input_list = []
        self.assertEqual(process_list(input_list), [])


if __name__ == '__main__':
    unittest.main()
