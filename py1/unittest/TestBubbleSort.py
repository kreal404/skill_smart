import unittest
import random
from sort import bubble_sort


class TestBubbleSort(unittest.TestCase):

    def test_regression(self):
        arr = [4, 2, 7, 1, 9, 3]
        bubble_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 7, 9])

    def test_random(self):
        arr = random.sample(range(1, 1000), 100)
        original_arr = arr.copy()
        bubble_sort(arr)
        self.assertEqual(arr, sorted(original_arr))

    def test_null(self):
        arr = [0, 0, 0, 0, 0]
        bubble_sort(arr)
        self.assertEqual(arr, [0, 0, 0, 0, 0])

    def test_boundary_values(self):
        arr = [float('-inf'), 5, 3, 8, 2, float('inf')]
        bubble_sort(arr)
        self.assertEqual(arr, [float('-inf'), 2, 3, 5, 8, float('inf')])

if __name__ == '__main__':
    unittest.main()