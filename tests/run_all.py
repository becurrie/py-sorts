"""tests.run_all: Runs all tests for py_sorter console application."""
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath('..'))

from py_sorter.sorts import *
from py_sorter.sorter import parse_args, calculate_compare_time_difference


class TestParsing(unittest.TestCase):
    """Test each argument available in the parser located in the sorter.py file."""
    def test_integers(self):
        """Test the optional one of: integers argument."""
        parser = parse_args(['-i', '1', '3', '6', '9', '-s', 'bubble'])
        self.assertTrue(parser.integers)

    def test_generate(self):
        """Test the optional one of: generate argument."""
        parser = parse_args(['-g', '100', '-s', 'bubble'])
        self.assertTrue(parser.generate)

    def test_sort(self):
        """Test the optional one of: sort argument."""
        parser = parse_args(['-g', '10', '-s', 'bubble'])
        self.assertTrue(parser.sort)

    def test_allsorts(self):
        """Test the optional one of: allsorts argument."""
        parser = parse_args(['-g', '10', '-a'])
        self.assertTrue(parser.allsorts)
        self.assertEqual(True, parser.allsorts)

        parser = parse_args(['-g', '10', '-s', 'bubble'])
        self.assertEqual(False, parser.allsorts)

    def test_list(self):
        """Test the optional list argument."""
        parser = parse_args(['-g', '10', '-s', 'bubble', '-l'])
        self.assertTrue(parser.list)
        self.assertEqual(True, parser.list)

        parser = parse_args(['-g', '10', '-s', 'bubble'])
        self.assertEqual(False, parser.list)

    def test_compare(self):
        """Test the optional compare argument."""
        parser = parse_args(['-g', '10', '-s', 'bubble', '-c'])
        self.assertTrue(parser.compare)
        self.assertEqual(True, parser.compare)

        parser = parse_args(['-g', '10', '-s', 'bubble'])
        self.assertEqual(False, parser.compare)


class TestHelpers(unittest.TestCase):
    """Test any helper methods present in the sorter.py file."""
    def test_compare_difference_string_slower(self):
        """Test that the calculate_compare_time_difference function will always
        return the proper string when the custom algorithm takes longer then the
        default python sorted() function.
        """
        test_algorithm = 'bubble'
        test_algorithm_time = 5
        test_sorted_time = 1
        result = calculate_compare_time_difference(test_algorithm_time, test_sorted_time, test_algorithm)
        self.assertEqual('bubble was 4 seconds slower.', result)

    def test_compare_difference_string_faster(self):
        """Test that the calculate_compare_time_difference function will always
        return the proper string when the custom algorithm is faster then the
        default python sorted() function.
        """
        test_algorithm = 'bubble'
        test_algorithm_time = 2
        test_sorted_time = 4
        result = calculate_compare_time_difference(test_algorithm_time, test_sorted_time, test_algorithm)
        self.assertEqual('bubble was 2 seconds faster.', result)


class TestSorts(unittest.TestCase):
    """Test each sorting method located in the sorts.py file."""
    def setUp(self):
        """Simple setup function to create the actual/expected
        lists that each sort method should produce if working as
        intended.
        """
        self.actual = [5, 7, 4, 9, 1, 2]
        self.expected = [1, 2, 4, 5, 7, 9]

    def test_bubble(self):
        """Test the bubble_sort function."""
        integers = bubble_sort(self.actual)
        self.assertEqual(self.expected, integers)

    def test_selection(self):
        """Test the selection_sort function."""
        integers = bubble_sort(self.actual)
        self.assertEqual(self.expected, integers)

    def test_bogo(self):
        """Test the bogo_sort function."""
        integers = bogo_sort(self.actual)
        self.assertEqual(self.expected, integers)

    def test_merge(self):
        """Test the merge_sort function."""
        integers = merge_sort(self.actual)
        self.assertEqual(self.expected, integers)

    def test_shell(self):
        """Test the shell_sort function."""
        integers = shell_sort(self.actual)
        self.assertEqual(self.expected, integers)

    def test_quick(self):
        """Test the quick_sort function."""
        integers = quick_sort(self.actual)
        self.assertEqual(self.expected, integers)

    def test_radix(self):
        """Test the radix_sort function."""
        integers = radix_sort(self.actual)
        self.assertEqual(self.expected, integers)

    def test_insertion(self):
        """Test the recursive insertion sort function."""
        integers = insertion_sort(self.actual)
        self.assertEqual(self.expected, integers)

    def test_insertion_recursive(self):
        """Test the recursive insertion sort function."""
        integers = insertion_sort_recursive(self.actual)
        self.assertEqual(self.expected, integers)

    def test_heap_sort(self):
        """Test the heap sort function."""
        integers = heap_sort(self.actual)
        self.assertEqual(self.expected, integers)


if __name__ == '__main__':
    unittest.main()
