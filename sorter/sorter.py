import argparse
import os
import sys
import timeit

from sorter.sorts import *


def parse_args(args):
    """Create the parser and add all required arguments before parsing
    user input and returning the parser.parse_args() results.
    """
    parser = argparse.ArgumentParser(description='sort some integers.')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-i', '--integers', type=int, nargs='+',
                       help='integer(s) being sorted.')
    group.add_argument('-g', '--generate', type=int,
                       help='generate a random list of integers to sort.')
    parser.add_argument('-s', '--sort', type=str, required=True,
                        choices=['bubble', 'bogo', 'merge', 'selection', 'quick'],
                        help='type of sort being performed.')

    return parser.parse_args(args)


def print_results(sort_type, original_list, sorted_list, time):
    """Print an original list, sorted list and time required to sort the original list."""
    print('\tSort Type: [%s]' % str.upper(sort_type))
    print('\tOriginal List:')
    for original_chunk in print_list_chunks(original_list, 20):
        print('\t' + str(original_chunk)[1:-1])

    print('\n\tSorted List:')
    for sorted_chunk in print_list_chunks(sorted_list, 20):
        print('\t' + str(sorted_chunk)[1:-1])

    # Print time required to sort list.
    print('\tTime(seconds): %s' % time)


def print_list_chunks(integer_list, n):
    """Simple helper method to print out a list in chunks."""
    for i in range(0, len(integer_list), n):
        yield integer_list[i:i + n]


def generate_integer_list(size):
    """Generate a list of Integers between specified size value."""
    integer_list = list()
    for i in range(0, size):
        integer_list.append(random.randint(0, 1000))

    return integer_list


def sort(sort_type, integers):
    """Sort a list of integers based on the type of sort specified."""
    if sort_type == 'bubble':
        initial = timeit.default_timer()
        sorted_list = bubble_sort(integers)
        final = timeit.default_timer()
        print_results(sort_type, integers, sorted_list, final - initial)

    elif sort_type == 'bogo':
        initial = timeit.default_timer()
        sorted_list = bogo_sort(integers)
        final = timeit.default_timer()
        print_results(sort_type, integers, sorted_list, final - initial)

    elif sort_type == 'selection':
        initial = timeit.default_timer()
        sorted_list = selection_sort(integers)
        final = timeit.default_timer()
        print_results(sort_type, integers, sorted_list, final - initial)

    elif sort_type == 'merge':
        initial = timeit.default_timer()
        original = list(integers)
        sorted_list = merge_sort(integers)
        final = timeit.default_timer()
        print_results(sort_type, original, sorted_list, final - initial)

    elif sort_type == 'quick':
        initial = timeit.default_timer()
        original = list(integers)
        quick_sort(integers)
        final = timeit.default_timer()

        # Slightly different print call, quick_sort sorts in place.
        # A new list isn't made, args.integers becomes sorted.
        print_results(sort_type, original, integers, final - initial)


def main(args):
    """Main method. build arguments, clear console and parse arguments"""
    args = parse_args(args[1:])

    # Clear system terminal based on operating system name.
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

    # Check for generate argument specified and create random list.
    if args.generate:
        args.integers = generate_integer_list(args.generate)

    # Main sort() method call from main.
    sort(args.sort, args.integers)


if __name__ == "__main__":
    # Allow import run through __name__ = __main__ idiom.
    main(sys.argv)
