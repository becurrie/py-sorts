"""py_sorter.sorter: provides argument parsing and entry point main()."""

__version__ = "0.2.0"


import argparse
import os
import sys
import timeit

from random import randint
from .sorts import *


def parse_args(args):
    """Create the parser and add all required arguments before parsing
    user input and returning the parser.parse_args() results.
    """
    parser = argparse.ArgumentParser(description='sort some integers.')

    # Parser group created to take in either one argument.
    # Integers manually specified or generated on the fly.
    integers_group = parser.add_mutually_exclusive_group(required=True)
    integers_group.add_argument('-i', '--integers', type=int, nargs='+',
                                help='integer(s) being sorted.')
    integers_group.add_argument('-g', '--generate', type=int,
                                help='generate a random list of integers to sort.')

    sorting_group = parser.add_mutually_exclusive_group(required=True)
    # Specify a specific sorting algorithm.
    sorting_group.add_argument('-s', '--sort', type=str,
                               choices=['bubble', 'bogo', 'merge', 'selection', 'quick', 'radix', 'insertion',
                                        'insertion_recursive', 'heap'],
                               help='type of sort being performed.')
    sorting_group.add_argument('-a', '--allsorts', action='store_true',
                               help='run all sort methods (excluding bogo sort).')

    # List argument used to display unsorted/sorted list in output.
    parser.add_argument('-l', '--list', action='store_true',
                        help='displays the original and unsorted lists if present.')

    return parser.parse_args(args)


def print_error(args, error):
    """Print an error to the screen when a sort fails."""
    print('\tAlgorithm: [%s]' % str.upper(args.sort))
    print("\terror occurred while sorting: %s" % error)
    print("\t")


def print_results(args, sorted_list, time):
    """Print an original list, sorted list and time required to sort the original list."""
    print('\tAlgorithm: [%s]' % str.upper(args.sort))

    # Determine whether or not the original and sorted lists will be printed
    # as part of the results output.
    if args.list:
        print('\tOriginal List:')
        for original_chunk in print_list_chunks(args.integers, 20):
            print('\t' + str(original_chunk)[1:-1])
        print('\tSorted List:')
        for sorted_chunk in print_list_chunks(sorted_list, 20):
            print('\t' + str(sorted_chunk)[1:-1])

    # Print time required to sort list.
    print('\tTime(seconds): %s' % time)
    print('\t')


def print_list_chunks(integer_list, n):
    """Simple helper method to print out a list in chunks."""
    for i in range(0, len(integer_list), n):
        yield integer_list[i:i + n]


def generate_integer_list(size):
    """Generate a list of Integers between specified size value."""
    integer_list = list()
    for i in range(0, size):
        integer_list.append(randint(0, 1000))

    return integer_list


def sort(args):
    """Sort a list of integers based on the type of sort specified. Any recursive
    algorithms use a try/except to print an error if recursive depth is reached.
    """
    # Create empty sorted_list variable.
    original_list = list(args.integers)
    sorted_list = list()

    # Initial default_timer() method call to grab current time of call.
    initial = timeit.default_timer()
    if args.sort == 'bubble':
        sorted_list = bubble_sort(original_list)

    elif args.sort == 'bogo':
        sorted_list = bogo_sort(original_list)

    elif args.sort == 'selection':
        sorted_list = selection_sort(original_list)

    elif args.sort == 'merge':
        sorted_list = merge_sort(original_list)

    elif args.sort == 'quick':
        try:
            sorted_list = quick_sort(original_list)
        except RecursionError as e:
            print_error(args, e.args[0])
            return

    elif args.sort == 'radix':
        try:
            sorted_list = radix_sort(original_list)
        except RecursionError as e:
            print_error(args, e.args[0])
            return

    elif args.sort == 'insertion':
        sorted_list = insertion_sort(original_list)

    elif args.sort == 'insertion_recursive':
        try:
            sorted_list = insertion_sort_recursive(original_list)
        except RecursionError as e:
            print_error(args, e.args[0])
            return

    elif args.sort == 'heap':
        sorted_list = heap_sort(original_list)

    # Final default_timer() method call to grab time after sort is completed.
    final = timeit.default_timer()
    print_results(args, sorted_list, final - initial)


def all_sorts(args):
    """Sort a list using each sorting algorithm excluding the bogo sort."""
    sorts = ['bubble', 'selection', 'merge', 'quick', 'radix', 'insertion', 'insertion_recursive', 'heap']
    for i in range(0, len(sorts)):
        args.sort = sorts[i]
        sort(args)


def main():
    """Main method. build arguments, clear console and parse arguments"""
    args = parse_args(sys.argv[1:])

    # Clear system terminal based on operating system name.
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

    # Check for generate argument specified and create random list.
    if args.generate:
        args.integers = generate_integer_list(args.generate)

    # Print each sort algorithm or just one that has been specified.
    if args.allsorts:
        all_sorts(args)
    else:
        sort(args)
