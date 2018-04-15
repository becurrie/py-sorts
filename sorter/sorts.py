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

def insertion_sort(integers):
    """Iterate over the list of integers. With each iteration,
    place the new element into its sorted position by shifting
    over elements to the left of the pointer until the correct
    location is found for the new element.
    Sorts the list in place. O(n^2) running time, O(1) space. 
    """
    for i in range(1, len(integers)):
        j = i
        while integers[j] < integers[j - 1] and j > 0:
            integers[j], integers[j-1] = integers[j-1], integers[j]
            j -= 1

def insertion_sort_recur(integers):
    """Performs insertion sort recursively.
    """
    def helper(arr, n):
        if n > 0:
            helper(arr, n-1)
            while arr[n] < arr[n-1] and n > 0:
                arr[n], arr[n-1] = arr[n-1], arr[n]
                n -= 1

    helper(integers, len(integers) - 1)

def heap_sort(integers):
    """Sorts elements by first building an array that fulfills the
    maxheap property. Once the original array has been modified
    to be a maxheap, move the 0th element to the end of the array,
    and fix the maxheap property for the array[0:-1]. Continue
    moving elements to the end of the heap and reducing the size of
    the heap until there is only one element left, at which point
    the array is sorted.
    """
    # Reorganize the array so that it has the maxheap property
    n = len(integers)
    for i in range(n, -1, -1):
        max_heapify(integers, i, n)

    # Swap the biggest element with the last element in the array
    # Then fix the maxheap property on everything except the
    # last element, which is now in its sorted position.
    n -= 1
    while n > 0:
        integers[0], integers[n] = integers[n], integers[0]
        max_heapify(integers, 0, n)
        n -= 1

def max_heapify(arr, i, n):
    """Corrects a violation of the maxheap property, provided the
    subtrees on the left and right of arr[i] are max heaps.
    arr: The heap
    i: Index of the node to fix
    n: Size of the heap
    """
    largest = i
    left_child = (i*2) + 1
    right_child = (i*2) + 2

    # Check whether the node at i fulfills the maxheap property
    # Requires short-circuit evaluation to make sure the
    # children don't throw index exceptions
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # If violated, repair maxheap property recursively
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, n)