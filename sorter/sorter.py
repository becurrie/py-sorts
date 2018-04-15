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

    # Parser group created to take in either one argument.
    # Integers manually specified or generated on the fly.
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-i', '--integers', type=int, nargs='+',
                       help='integer(s) being sorted.')
    group.add_argument('-g', '--generate', type=int,
                       help='generate a random list of integers to sort.')

    # Specify a specific sorting algorithm.
    parser.add_argument('-s', '--sort', type=str, required=True,
                        choices=['bubble', 'bogo', 'merge', 'selection', 'quick', 'radix'],
                        help='type of sort being performed.')

    # List argument used to display unsorted/sorted list in output.
    parser.add_argument('-l', '--list', action='store_true',
                        help='displays the original and unsorted lists if present.')

    return parser.parse_args(args)


def print_results(args, sorted_list, time):
    """Print an original list, sorted list and time required to sort the original list."""
    print("\t========================")
    print('\tSort Type: [%s]' % str.upper(args.sort))

    # Determine whether or not the original and sorted lists will be printed
    # as part of the results output.
    if args.list:
        print('\tOriginal List:')
        for original_chunk in print_list_chunks(args.integers, 20):
            print('\t' + str(original_chunk)[1:-1])
        print("\t========================")
        print('\tSorted List:')
        for sorted_chunk in print_list_chunks(sorted_list, 20):
            print('\t' + str(sorted_chunk)[1:-1])

    # Print time required to sort list.
    print('\tTime(seconds): %s' % time)
    print("\t========================")


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


def sort(args):
    """Sort a list of integers based on the type of sort specified."""
    # Create empty sorted_list variable.
    sorted_list = list()

    # Initial default_timer() method call to grab current time of call.
    initial = timeit.default_timer()
    if args.sort == 'bubble':
        sorted_list = bubble_sort(args.integers)
    elif args.sort == 'bogo':
        sorted_list = bogo_sort(args.integers)
    elif args.sort == 'selection':
        sorted_list = selection_sort(args.integers)
    elif args.sort == 'merge':
        sorted_list = merge_sort(args.integers)
    elif args.sort == 'quick':
        sorted_list = quick_sort(args.integers)
    elif args.sort == 'radix':
        sorted_list = radix_sort(args.integers)

    # Final default_timer() method call to grab time after sort is completed.
    final = timeit.default_timer()
    print_results(args, sorted_list, final - initial)


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
    sort(args)


if __name__ == "__main__":
    # Allow import run through __name__ = __main__ idiom.
    main(sys.argv)
