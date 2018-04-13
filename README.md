[![GitHub version](https://badge.fury.io/gh/becurrie%2Fpy-custom-sorters.svg)](https://badge.fury.io/gh/becurrie%2Fpy-custom-sorters)

# Py Custom Sorters

Sort Integers using different sorting algorithms!

## Getting Started

### Sorts Available

- Selection
- Merge
- Bogo
- Bubble

Simply use the console to begin sorting!

```python
python -m sorter -s bubble -i 9 3 2 8 4
python -m sorter -g 100 -s selection
python -m sorter -g 5 -s bogo
python -m sorter -i  1 5 4 38 5 4 56 8 2 -s selection
```

### Caution
- Be careful when using the **Bogo** sorting algorithm, it shuffles
an array and checks it sorted iteratively, larger data sets will take a long time (forever).

```python sorter.py -h``` can be used to view the available arguments possible.

### Installing

- Clone repository locally
- ```python setup.py build```
- ```python setup.py install```
- Access module from console with ```python -m sorter```

## Authors

* **Brett Currie** - [becurrie](https://github.com/becurrie)

See also the list of [contributors](https://github.com/becurrie/py-custom-sorters/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
