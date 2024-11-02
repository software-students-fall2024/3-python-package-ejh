<!-- Need to finish badge -->
![Build Status](https://github.com/software-students-fall2024/3-python-package-ejh/actions/workflows/event-logger.yml/badge.svg)

# Python Package Exercise

An exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.

## Table of Contents

1. [PyPI Page](#pypi-page)
2. [Installation](#installation)
3. [Running pyAnimals_ejh](#running-pyanimals_ejh)
5. [Contributing](#contributing)
6. [Team Members](#team-members)
7. [Configuration and Environment Setup](#configuration-and-environment-setup)

## PyPI Page
You can find pyAnimals_ejh on [PyPI here](https://pypi.org/project/pyAnimals-ejh/0.1.0/)

## Installation

Install `pyAnimals_ejh` with pip:
```
pip install pyAnimals_ejh
```

## Running pyAnimals_ejh

To run `pyAnimals_ejh`, use the following command:
```
python -m pyAnimals_ejh
```

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
pip install -r requirements.txt
```
3. Build and Test the Package
```
python -m build
```
4. Run Tests
```
pytest
```
5. Add New Tests
If you add new functionality, include tests in the tests/ directory.

## Team members

[Haley Hobbs](https://github.com/haleyhobbs) \
[Emma Zhu](https://github.com/ez106) \
[Jason Tran](https://github.com/huyy422) \
[Jenna Han](https://github.com/jnahan)