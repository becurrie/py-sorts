import random


def bubble_sort(integers):
    """Sort a list of integers using a simple bubble sorting method.
    Compare each element with its neighbor (except the last index)
    with its neighbor to the right, perform same check iteratively
    with the last n elements not being checked because they are sorted.
    """
    integers_clone = list(integers)

    for number in range(len(integers_clone) - 1, 0, -1):
        for i in range(number):
            if integers_clone[i] > integers_clone[i + 1]:
                temp = integers_clone[i]
                integers_clone[i] = integers_clone[i + 1]
                integers_clone[i + 1] = temp

    return integers_clone


def selection_sort(integers):
    """Search through a list of Integers using the selection sorting method.
    Search elements 0 through n - 1 and select smallest, swap with element at
    index 0, iteratively search through elements n - 1 and swap with smallest.
    """
    integers_clone = list(integers)

    for index in range(len(integers_clone) - 1, 0, -1):
        max_position = 0
        for location in range(1, index + 1):
            if integers_clone[location] > integers_clone[max_position]:
                max_position = location

        temp = integers_clone[index]
        integers_clone[index] = integers_clone[max_position]
        integers_clone[max_position] = temp

    return integers_clone


def merge_sort(integers):
    """Divide and conquer approach to sorting a list. Check left index
    id > right index and return, otherwise, grab new middle variable and call
    method recursively until sorted, then merge the half together
    """
    if len(integers) > 1:
        mid = len(integers) // 2
        left = integers[:mid]
        right = integers[mid:]

        merge_sort(left)
        merge_sort(right)

        # Splitting here.
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                integers[k] = left[i]
                i += 1
            else:
                integers[k] = right[j]
                j += 1

            k += 1

        # Merging here.
        while i < len(left):
            integers[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            integers[k] = right[j]
            j += 1
            k += 1

    return integers


def bogo_sort(integers):
    """Sort a list of integers using a bogo sort, randomly replacing
    integers in the list until a sorted list is created.
    """
    integers_clone = list(integers)

    is_sorted = False

    while not is_sorted:
        random.shuffle(integers_clone)
        for i in range(len(integers_clone) - 1):
            if integers_clone[i] > integers_clone[i + 1]:
                is_sorted = False
                break
            else:
                is_sorted = True

    return integers_clone


def quick_sort(integers):
    """Perform a quick sort on a list of integers, selecting a pivot
    point, partition all elements into a first and second part while
    looping so all elements < pivot are in first part, any elements
    > then pivot are in seconds part, recursively sort both half's
    and combine.
    """
    quick_sort_helper(integers, 0, len(integers) - 1)
    return integers


def quick_sort_helper(integers, first, last):
    """Small helper method for calling and recursively finding
    pivot/split points.
    """
    if first < last:
        split = quick_sort_partition(integers, first, last)

        quick_sort_helper(integers, first, split - 1)
        quick_sort_helper(integers, split + 1, last)


def quick_sort_partition(integers, first, last):
    """Generate a correct partition point for the given list of integers."""
    pivot_value = integers[first]

    left = first + 1
    right = last

    done = False
    while not done:
        while left <= right and integers[left] <= pivot_value:
            left += 1

        while integers[right] >= pivot_value and right >= left:
            right -= 1

        if right < left:
            done = True
        else:
            temp = integers[left]
            integers[left] = integers[right]
            integers[right] = temp

    temp = integers[first]
    integers[first] = integers[right]
    integers[right] = temp

    return right


def counting_sort(integers, exp):
    """Counting sort helper method used with the radix_sort()"""
    n = len(integers)

    output = [0] * n
    count = [0] * 10

    for i in range(0, n):
        index = (integers[i] // exp)
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = integers[i] // exp
        output[count[index % 10] - 1] = integers[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, len(integers)):
        integers[i] = output[i]


def radix_sort(integers):
    """Radix sorting method that utilizes the counting_sort, sorting
    ach digit starting from the least significant digit to most significant.
    Uses the counting_sort() method as it's subroutine for sorting.
    """
    integers_clone = list(integers)
    max_integer = max(integers)

    # Do counting sort on each digit in list.
    exp = 1
    while max_integer / exp > 0:
        counting_sort(integers_clone, exp)
        exp *= 10

    return integers_clone
