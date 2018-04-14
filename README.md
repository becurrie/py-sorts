[![GitHub version](https://badge.fury.io/gh/becurrie%2Fpy-custom-sorters.svg)](https://badge.fury.io/gh/becurrie%2Fpy-custom-sorters)

# Py Custom Sorters

Sort Integers using different sorting algorithms!

## Getting Started

#### Sorts Available

- [Selection](https://www.geeksforgeeks.org/selection-sort/)
- [Merge](https://www.geeksforgeeks.org/merge-sort/)
- [Bogo](https://en.wikipedia.org/wiki/Bogosort)
- [Bubble](https://www.geeksforgeeks.org/bubble-sort/)

#### Arguments

- -s, --sort: provide a sort method to use.
    - selection, bogo, merge, bubble.
- -i, --integers: include your own list of integers. (ex: ```python -m sorter -i 9 3 2 8 4```
- -g, --generate: generate a random list of integers. (ex: ```python -m sorter -g 1000```

Simply use the console to begin sorting!

```
python -m sorter -g 100 -s bubble
```

### Caution
- Be careful when using the **Bogo** sorting algorithm, it shuffles
an array and checks it sorted iteratively, larger data sets will take a long time (forever).

```python -m sorter -h``` can be used to view the available arguments possible.

### Installing

- Clone repository locally.
- ```python setup.py install```.
- Access module from console with ```python -m sorter```.

## Authors

* **Brett Currie** - [becurrie](https://github.com/becurrie)

See also the list of [contributors](https://github.com/becurrie/py-custom-sorters/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
