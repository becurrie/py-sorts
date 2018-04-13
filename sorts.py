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
