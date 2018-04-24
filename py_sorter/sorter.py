"""py_sorter.sorter: provides argument parsing and entry point main().
Any calls to the sorts methods are called from here based on the -s/--sort
argument specified by the user.
"""
__version__ = "0.3.0"

import argparse
import os
import timeit

from random import randint
from .sorts import *


def parse_args(args):
    """Create the parser and add all required arguments before parsing
    user input and returning the parser.parse_args() results.
    """
    parser = argparse.ArgumentParser(description='sort some integers.')

    # Parser group created to take in either argument. (-i or -g).
    # Integers manually specified or generated on the fly.
    integers_group = parser.add_mutually_exclusive_group(required=True)
    integers_group.add_argument('-i', '--integers', type=int, nargs='+',
                                help='integer(s) being sorted.')
    integers_group.add_argument('-g', '--generate', type=int,
                                help='generate a random list of integers to sort.')

    # Specific sort algorithm or use all sort algorithms.
    sorting_group = parser.add_mutually_exclusive_group(required=True)
    sorting_group.add_argument('-s', '--sort', type=str,
                               choices=['bubble', 'bogo', 'merge', 'selection', 'quick', 'radix', 'insertion',
                                        'insertion_recursive', 'heap'],
                               help='type of sort being performed.')
    sorting_group.add_argument('-a', '--allsorts', action='store_true',
                               help='run all sort methods (excluding bogo sort).')

    # List argument used to display unsorted/sorted list in output.
    parser.add_argument('-l', '--list', action='store_true',
                        help='displays the original and unsorted lists if present.')

    # Compare argument to display the time difference compared to the default python sorted() function.
    parser.add_argument('-c', '--compare', action='store_true',
                        help='display the difference in time compared to pythons default \'sorted()\' function.')

    return parser.parse_args(args)


def print_error(args, error):
    """Print an error to the screen when a sort fails."""
    print('\tAlgorithm: [%s]' % str(args.sort))
    print("\terror occurred while sorting: %s" % error)
    print("\t")


def print_results(args, sorted_list, time):
    """Print an original list, sorted list and time required to sort the original list."""
    print('\tAlgorithm: [%s]' % str(args.sort))

    # Determine whether or not the original and sorted lists will be printed
    # as part of the results output.
    if args.list:
        print('\tOriginal List:')
        for original_chunk in print_list_chunks(args.integers, 20):
            print('\t' + str(original_chunk)[1:-1])
        print('\tSorted List:')
        for sorted_chunk in print_list_chunks(sorted_list, 20):
            print('\t' + str(sorted_chunk)[1:-1])

    # Check for the --compare flag being present, and print out the difference
    # between this results time and the default sorted() function time.
    if args.compare:
        print('\tTime(seconds) %s: %s' % (args.sort, time))
        print('\tTime(seconds) sorted(): %s' % args.compare_time)
        print('\t%s' % calculate_compare_time_difference(time, args.compare_time, args.sort))
    else:
        print('\tTime(seconds): %s' % time)

    print('\t')


def calculate_compare_time_difference(algorithm_time, default_time, algorithm):
    """Calculate the difference between a custom algorithms time taken to sort, and
    pythons sorted() function time taken to sort the same list, returns a readable string
    detailing which was faster.
    """
    difference = algorithm_time - default_time

    if difference > 0:
        return '%s was %s seconds slower.' % (algorithm, difference)
    else:
        return '%s was %s seconds faster.' % (algorithm, -difference)


def print_list_chunks(integer_list, n):
    """Simple helper method to print out a list in chunks. This allows
    the console output to never surpass a specific width. Giving a cleaner
    output if the original/sorted lists are being printed.
    """
    for i in range(0, len(integer_list), n):
        yield integer_list[i:i + n]


def generate_integer_list(size):
    """Generate a list of integers between specified size value."""
    integer_list = list()
    for i in range(0, size):
        integer_list.append(randint(0, 1000))

    return integer_list


def sort(args):
    """Sort a list of integers based on the type of sort specified. Any recursive
    algorithms use a try/except to print an error if recursive depth is reached.
    """
    # Create a clone of the initial args.integers property.
    original_list = list(args.integers)

    # Empty sorted_list that will hold list after sort method returns.
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

    # Check for compare flag and get the time taken for the default sorted() call on list.
    if args.compare:
        default_initial = timeit.default_timer()
        default_list = sorted(original_list)
        default_final = timeit.default_timer()
        args.compare_time = default_final - default_initial

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
