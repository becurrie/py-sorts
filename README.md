[![GitHub version](https://badge.fury.io/gh/becurrie%2Fpy-custom-sorters.svg)](https://github.com/becurrie/sorters-py/releases)

# py-sorts

Sort Integers using different sorting algorithms!

## Getting Started

Check the [releases](https://github.com/becurrie/sorters-py/releases) section to find the latest working zip/tar.

#### Sorts Available

1. [Selection](https://en.wikipedia.org/wiki/Selection_sort)
2. [Merge](https://en.wikipedia.org/wiki/Merge_sort)
3. [Bogo](https://en.wikipedia.org/wiki/Bogosort)
4. [Bubble](https://en.wikipedia.org/wiki/Bubble_sort)
5. [Quick](https://en.wikipedia.org/wiki/Quicksort)
6. [Radix](https://en.wikipedia.org/wiki/Radix_sort)
7. [Insertion](https://en.wikipedia.org/wiki/Insertion_sort)
8. [Recursive Insertion](https://en.wikipedia.org/wiki/Insertion_sort)
9. [Heap](https://en.wikipedia.org/wiki/Heapsort)

#### Arguments

| Argument        | Description                                         | Example                            |
|-----------------|-----------------------------------------------------|------------------------------------|
| -s / --sort     | type of sort being performed                        | ```python -m sorter -s radix```    |
| -i / --integers | integer(s) being sorted                             | ```python -m sorter -i 9 34 5 4``` |
| -g / --generate | generate a random list of integers to sort          | ```python -m sorter -g 1000```     |
| -l / --list     | displays the original and unsorted lists if present | ```python -m sorter -l```          |
| -a / --allsorts | perform sort on each algorithm, except bogo sort    | ```python -m sorter -a```          |

## Examples

```bash
python -m py_sorter -i 1 9 8 3 4 5 -s bogo -l
```

Output:
```
Algorithm: [BOGO]
Original List:
1, 9, 8, 3, 4, 5
Sorted List:
1, 3, 4, 5, 8, 9
Time(seconds): 0.0038447857274609663
```

***


```bash
python -m py_sorter -g 10000 -s quick
```

Output:
```
Sort Type: [QUICK]
Time(seconds): 0.02460269912110386
```

### Caution

- Be careful when using the **Bogo** sorting algorithm, it shuffles
an array and checks it's been sorted, shuffling infinitely until list is sorted. larger data sets will take a long time (forever).

- Some algorithms use recursive sub routines to sort, this can lead to RecursionErrors if the data set is very large.

## Installing

- Clone repository locally.
- ```python setup.py install```.
- Access module from console with ```python -m py_sorter```.

## Development

### Launching

- While developing, inside root (/py_sorter) you can use two options to invoke:
    - ```python sorter-runner.py [args]```
    - ```python -m py_sorter [args]```

### Testing

- New tests can be added to the `run_all.py` file located at (/tests).

- To run automated tests:
    - ```python -m run_all```



## Authors

* [**becurrie**](https://github.com/becurrie)
* [**garroadran**](https://github.com/garroadran) - Heap, Insertion, Recursive Insertion algorithms.

See also the list of [contributors](https://github.com/becurrie/py-custom-sorters/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Resources

### Sorting Algorithms

- [Interactive Python](http://interactivepython.org)
- [GeeksforGeeks](https://www.geeksforgeeks.org/)

### Argument Parsing

- [argparse](https://docs.python.org/3.6/library/argparse.html)