[![GitHub version](https://badge.fury.io/gh/becurrie%2Fpy-custom-sorters.svg)](https://badge.fury.io/gh/becurrie%2Fpy-custom-sorters)

# Py Custom Sorters

Sort Integers using different sorting algorithms!

## Getting Started

#### Sorts Available

1. [Selection](https://en.wikipedia.org/wiki/Selection_sort)
2. [Merge](https://en.wikipedia.org/wiki/Merge_sort)
3. [Bogo](https://en.wikipedia.org/wiki/Bogosort)
4. [Bubble](https://en.wikipedia.org/wiki/Bubble_sort)
5. [Quick](https://en.wikipedia.org/wiki/Quicksort)
6. [Radix](https://en.wikipedia.org/wiki/Radix_sort)
7. [Insertion](https://en.wikipedia.org/wiki/Insertion_sort)
8. [Heap](https://en.wikipedia.org/wiki/Heapsort)

#### Arguments

| Argument        | Description                                         | Example                            |
|-----------------|-----------------------------------------------------|------------------------------------|
| -s / --sort     | type of sort being performed                        | ```python -m sorter -s radix```    |
| -i / --integers | integer(s) being sorted                             | ```python -m sorter -i 9 34 5 4``` |
| -g / --generate | generate a random list of integers to sort          | ```python -m sorter -g 1000```     |
| -l / --list     | displays the original and unsorted lists if present | ```python -m sorter -l```          |

## Examples

```bash
python -m sorter -i 1 9 8 3 4 5 -s bogo -l
```

Output:
```
========================
Sort Type: [BOGO]
Original List:
1, 3, 4, 5, 8, 9
========================
Sorted List:
1, 3, 4, 5, 8, 9
Time(seconds): 0.0038447857274609663
========================
```

***


```bash
python -m sorter -g 10000 -s quick
```

Output:
```
========================
Sort Type: [QUICK]
Time(seconds): 0.02460269912110386
========================
```


### Caution
- Be careful when using the **Bogo** sorting algorithm, it shuffles
an array and checks it sorted iteratively, larger data sets will take a long time (forever).

- Specifying an array of size > **650,000** can result in errors due to recursion depth with some sorting algorithms.

## Installing

- Clone repository locally.
- ```python setup.py install```.
- Access module from console with ```python -m sorter```.

## Authors

* **Brett Currie** - [becurrie](https://github.com/becurrie)

See also the list of [contributors](https://github.com/becurrie/py-custom-sorters/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Resources

### Sorting Algorithms

- [Interactive Python](http://interactivepython.org)
- [GeeksforGeeks](https://www.geeksforgeeks.org/)

### Argument Parsing

- [argparse](https://docs.python.org/3.6/library/argparse.html)