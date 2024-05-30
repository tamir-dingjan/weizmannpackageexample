# An Example Package

This repository is an example layout for a data analysis project in Python. The arrangement of modules, data, notebooks, and graphs is one suggestion for how to arrange these elements together into a single, easily-transferred package.

## Installation

The recommended way to install this example is to first generate a new Python environment using ```conda``` (see [Anaconda Documentation](https://docs.anaconda.com/index.html) for how to get and use this tool). You can generate new Python environment by running:
```
conda create -n YOUR_ENVIRONMENT_NAME python=3.11
```

Clone this repository into your working directory, and then in the same folder where the ```pyproject.toml``` file is located, run:
 ```
 python -m pip install .
 ```

to download and install this example package's dependencies. This will also install the ```weizmannpackageexample``` package.