# Py Custom Sorters

Sort Integers using different sorting algorithms!

## Getting Started

Simply use the console to begin sorting!

```
python -m sorter -s bubble -i 9 3 2 8 4

Sort: Bubble
Original: [9, 3, 2, 8, 4]
Sorted: [2, 3, 4, 8, 9]
Time(s):  1.4662442710170721e-05
```

```python sorter.py -h``` can be used to view the available arguments possible.

```
optional arguments:
  -h, --help            show this help message and exit
  -i INTEGERS [INTEGERS ...], --integers INTEGERS [INTEGERS ...]
                        integer(s) being sorted.
  -g GENERATE, --generate GENERATE
                        generate a random list of integers to sort.
  -s {bubble,bogo,merge,selection}, --sort {bubble,bogo,merge,selection}
                        type of sort being performed.
```

### Installing

- Clone repository locally
- ```python setup.py install```
- Access library from console with ```python -m sorter```

## Authors

* **Brett Currie** - [becurrie](https://github.com/becurrie)

See also the list of [contributors](https://github.com/becurrie/py-custom-sorters/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
