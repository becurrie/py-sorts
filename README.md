[![GitHub version](https://badge.fury.io/gh/becurrie%2Fpy-custom-sorters.svg)](https://github.com/becurrie/sorters-py/releases)

# py-sorts

Sort Integers using different sorting algorithms!

## Getting Started

Check the [releases](https://github.com/becurrie/sorters-py/releases) section to find the latest working zip/tar.

### ```python -m py_sorter [args]```

#### Sorts Available
| Sorts Available                                           |                                                                     |                                                   |
|-----------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------|
| [Selection](https://en.wikipedia.org/wiki/Selection_sort) | [Merge](https://en.wikipedia.org/wiki/Merge_sort)                   | [Bogo](https://en.wikipedia.org/wiki/Bogosort)    |
| [Bubble](https://en.wikipedia.org/wiki/Bubble_sort)       | [Quick](https://en.wikipedia.org/wiki/Quicksort)                    | [Radix](https://en.wikipedia.org/wiki/Radix_sort) |
| [Insertion](https://en.wikipedia.org/wiki/Insertion_sort) | [Recursive Insertion](https://en.wikipedia.org/wiki/Insertion_sort) | [Heap](https://en.wikipedia.org/wiki/Heapsort)    |

#### Arguments

| Argument        | Description                                                | Example                               |
|-----------------|------------------------------------------------------------|---------------------------------------|
| -s / --sort     | type of sort being performed on list                       | ```python -m py_sorter -s radix```    |
| -i / --integers | provide a list of integers to be sorted                    | ```python -m py_sorter -i 9 34 5 4``` |
| -g / --generate | generate a random list of integers to be sorted            | ```python -m py_sorter -g 1000```     |
| -l / --list     | displays the original/sorted lists                         | ```python -m py_sorter -l```          |
| -a / --allsorts | perform sort on list with each algorithm, except bogo sort | ```python -m py_sorter -a```          |

## Examples

```bash
python -m py_sorter --generate 8 --sort bogo --list
```

Output:

```
Shuffles: 20,222
Algorithm: [BOGO]
Original List:
126, 61, 946, 874, 990, 488, 601, 787
Sorted List:
61, 126, 488, 601, 787, 874, 946, 990
Time(seconds): 0.10767681062733224
```
***

```bash
python -m py_sorter --generate 10000 --sort quick
```

Output:

```
Algorithm: [QUICK]
Time(seconds): 0.026681231351216618
```

### Caution

- Be careful when using the **Bogo** sorting algorithm, it shuffles
an array and checks it's been sorted, shuffling infinitely until list is sorted. larger data sets will take a long time (forever).

- Some algorithms use recursive sub routines to sort, this can lead to RecursionErrors if the data set is very large.

## Installing

- Clone repository locally.
- ```python setup.py install```.
- Access module from console with ```python -m py_sorter [args]```.

## Development

### Launching

- While developing, inside root (/py_sorter) you can test new code changes with:
    - ```python sorter-runner.py [args]```

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

### Resources

#### Sorting Algorithms

- [Interactive Python](http://interactivepython.org)
- [GeeksforGeeks](https://www.geeksforgeeks.org/)

#### Argument Parsing

- [argparse](https://docs.python.org/3.6/library/argparse.html)