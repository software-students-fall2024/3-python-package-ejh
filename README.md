![Build Status](https://github.com/software-students-fall2024/3-python-package-ejh/actions/workflows/event-logger.yml/badge.svg)

# pyAnimals-ejh

## Table of Contents
1. [Description](#description)
2. [PyPI Page](#pypi-page)
3. [Installation](#installation)
4. [Virtual Environment](#virtual-environment)
5. [Functions](#functions)
6. [Example](#example)
7. [Contributing](#contributing)
8. [Team Members](#team-members)

## Description
A fun package that displays animals on the terminal with movement and messages.

## PyPI Page
You can find pyAnimals_ejh on PyPI [HERE](https://pypi.org/project/pyAnimals-ejh/0.2.0/)

## Installation
Install `pyAnimals_ejh` with pip:
```
pip install pyAnimals_ejh
```
Check that the package is installed with pip:
```
pip list
```

## Virtual Environment
Set up the virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```

## Functions
Parameter for all functions are: animal (str): name of animal.\
***Note: Valid animal names include "cat", "bunny", "elephant", "rabbit". Only these can be used with our package.

1. move(animal)
Moves specified animal across the terminal screen
```
move("cat")
```

2. race(animal)
Displays race between player and specified animal
```
race("rabbit")
```

3. randMessage(animal)
Prints a random message for the specified animal
```
randMessage("bunny")
```

4. print_fact(animal)
Prints a random fact for the specified animal.
Raises: ValueError if no facts are available for the specified animal.
```
print_fact("elephant")
```
## Example
To run an example implementation of `pyAnimals_ejh`, use the following command:
```
python3 example.py
```
See this example program [HERE](/example.py)

## Contributing
We welcome contributions to enhance and grow pyAnimals_ejh! Follow these steps to set up the development environment:
1. Clone the Repository:
```
git clone https://github.com/software-students-fall2024/3-python-package-ejh.git
cd 3-python-package-ejh
```
2. Set Up the Virtual Environment
```python -m venv venv
source venv/bin/activate
```
3. Build and Test the Package
```
python -m build
```
4. Run Tests
```
```
5. Add New Tests\
If you add new functionality, include tests in the tests directory.

## Team members

[Haley Hobbs](https://github.com/haleyhobbs) \
[Emma Zhu](https://github.com/ez106) \
[Jason Tran](https://github.com/huyy422) \
[Jenna Han](https://github.com/jnahan)