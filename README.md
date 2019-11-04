[![GitHub version](https://badge.fury.io/gh/becurrie%2Fpy-custom-sorters.svg)](https://github.com/becurrie/sorters-py/releases)

# py-sorts

Sort Integers using different sorting algorithms!

## Getting Started

Check the [releases](https://github.com/becurrie/py-sorts/releases) section to find the latest working zip/tar.

### ```python -m py_sorter [args]```

#### Sorts Available
| Sorts Available                                           |                                                                     |                                                   |
|-----------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------|
| [Selection](https://en.wikipedia.org/wiki/Selection_sort) | [Merge](https://en.wikipedia.org/wiki/Merge_sort)                   | [Bogo](https://en.wikipedia.org/wiki/Bogosort)    |
| [Bubble](https://en.wikipedia.org/wiki/Bubble_sort)       | [Quick](https://en.wikipedia.org/wiki/Quicksort)                    | [Radix](https://en.wikipedia.org/wiki/Radix_sort) |
| [Insertion](https://en.wikipedia.org/wiki/Insertion_sort) | [Recursive Insertion](https://en.wikipedia.org/wiki/Insertion_sort) | [Heap](https://en.wikipedia.org/wiki/Heapsort)    |
| [Shell](https://en.wikipedia.org/wiki/Shellsort)

#### Arguments

| Argument        | Description                                                                          | Example                               |
|-----------------|--------------------------------------------------------------------------------------|---------------------------------------|
| -s / --sort     | type of sort being performed on list.                                                | ```python -m py_sorter -s radix```    |
| -i / --integers | provide a list of integers to be sorted.                                             | ```python -m py_sorter -i 9 34 5 4``` |
| -g / --generate | generate a random list of integers to be sorted.                                     | ```python -m py_sorter -g 1000```     |
| -l / --list     | displays the original/sorted lists.                                                  | ```python -m py_sorter -l```          |
| -a / --allsorts | perform sort on list with each algorithm, except bogo sort.                          | ```python -m py_sorter -a```          |
| -c / --compare  | display a time comparison between chosen sort and pythons default sorted() function. | ```python -m py_sorter -c```          |

## Examples

```bash
python -m py_sorter -g 8 -s bogo -l -c
```

Output:

```
Shuffles: 63,257
Algorithm: [bogo]
Original List:
468, 846, 801, 976, 261, 641, 72, 698
Sorted List:
72, 261, 468, 641, 698, 801, 846, 976
Time(seconds) bogo: 0.3453168464965863
Time(seconds) sorted(): 3.5189852184980275e-06
bogo was 0.3453133275113678 seconds slower.
```
***

```bash
python -m py_sorter --generate 10000 --sort quick
```

Output:

```
Algorithm: [quick]
Time(seconds): 0.02490532463518387
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
