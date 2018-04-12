import argparse
import os
import random
import timeit

from sorts import bubble_sort, bogo_sort, selection_sort


class Parser:
    """Parser class for building and retrieving arguments from console."""
    parser = argparse.ArgumentParser(description='sort some integers.')

    def build_arguments(self):
        """Build argument parser."""
        group = self.parser.add_mutually_exclusive_group(required=True)
        group.add_argument('-i', '--integers', type=int, nargs='+',
                                 help='integer(s) being sorted.')
        group.add_argument('-g', '--generate', type=int,
                                 help='generate a random list of integers to sort.')
        self.parser.add_argument('-s', '--sort', type=str, required=True,
                                 choices=['bubble', 'bogo', 'merge', 'selection'],
                                 help='type of sort being performed.')
        return self

    def get_args(self):
        """Get args through argparser default sys.argv"""
        self.parser.parse_args()


def print_results(sort_type, original_list, sorted_list, time):
    """Print an original list, sorted list and time required to sort the original list."""
    print('\tSort:     %s' % str.capitalize(sort_type))
    print('\tOriginal:   ')
    for original_chunk in print_list_chunks(original_list, 20):
        print('\t' + str(original_chunk))

    print('\tSorted:     ')
    for sorted_chunk in print_list_chunks(sorted_list, 20):
        print('\t' + str(sorted_chunk))

    # Calculate time required to sort using sequential sort.
    print('\tTime(s):  %s' % time)
    print('\t-------------------------------')


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


def main():
    """Main method. build arguments and sort based on --sort arg."""
    parser = Parser().build_arguments()
    args = parser.parser.parse_args()

    # Clear system terminal based on operating system name.
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

    # Check for generate argument specified and create random list.
    if args.generate:
        args.integers = generate_integer_list(args.generate)

    # Sort the list of Integers based on sort type.
    if args.sort == 'bubble':
        initial = timeit.default_timer()
        sorted_list = bubble_sort(args.integers)
        final = timeit.default_timer()
        print_results(args.sort, args.integers, sorted_list, final - initial)

    elif args.sort == 'bogo':
        initial = timeit.default_timer()
        sorted_list = bogo_sort(args.integers)
        final = timeit.default_timer()
        print_results(args.sort, args.integers, sorted_list, final - initial)

    elif args.sort == 'selection':
        initial = timeit.default_timer()
        sorted_list = selection_sort(args.integers)
        final = timeit.default_timer()
        print_results(args.sort, args.integers, sorted_list, final - initial)


if __name__ == "__main__":
    # Allow import run through __name__ = __main__ idiom.
    main()
