import unittest

from sorter.sorts import *

from sorter.sorter import parse_args


class TestParsing(unittest.TestCase):

    def test_integers(self):
        """Test the optional one of: integers argument."""
        parser = parse_args(['-i', '1', '3', '6', '9', '-s', 'bubble'])
        self.assertTrue(parser.integers)

    def test_generate(self):
        """Test the optional one of: generate argument."""
        parser = parse_args(['-g', '100', '-s', 'bubble'])
        self.assertTrue(parser.generate)

    def test_sort(self):
        """Test the required sort argument."""
        parser = parse_args(['-g', '10', '-s', 'bubble'])
        self.assertTrue(parser.sort)


class TestSorts(unittest.TestCase):

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

    def test_quick(self):
        """Test the quick_sort function. This test is slightly different
        because the quick_sort method sorts in place and doesn't return
        a new sorted list.
        """
        clone = self.actual
        quick_sort(clone)
        self.assertEqual(self.expected, clone)
    
    def test_insertion(self):
        """Test the recursive insertion sort function.
        Uses a clone of self.actual
        """
        clone = self.actual[:]
        insertion_sort(clone)
        self.assertEqual(self.expected, clone)

    def test_insertion_recur(self):
        """Test the recursive insertion sort function.
        Uses a clone of self.actual
        """
        clone = self.actual[:]
        insertion_sort_recur(clone)
        self.assertEqual(self.expected, clone)

    def test_heap_sort(self):
        """Test the heap sort function.
        Uses a clone of self.actual
        """
        clone = self.actual[:]
        heap_sort(clone)
        self.assertEqual(self.expected, clone)
