# Installation

## Stable release

To install thinkgreen, run this command in your terminal:

```
pip install thinkgreen
```

This is the preferred method to install thinkgreen, as it will always install the most recent stable release.

If you don't have [pip](https://pip.pypa.io) installed, this [Python installation guide](http://docs.python-guide.org/en/latest/starting/installation/) can guide you through the process.

## Install from GitHub 

To install thinkgreen from GitHub using Git, run the following command in your terminal:

```bash
pip install git+https://github.com/olilamm/thinkgreen
```

## From sources

The sources for thinkgreen can be downloaded from the Github repo.

You can clone the public repository:

```
git clone git://github.com/olilamm/thinkgreen
```

## Upgrade thinkgreen

to upgrade to the latest version of thinkgreen, you can run the following command in your terminal:
```bash
pip install -U thinkgreen
```

If you use conda, you can update thinkgreen to the latest version by running the following command in your terminal:

```bash
conda update -c conda-forge thinkgreen
```

To install the development version from GitHub directly within Jupyter notebook without using Git, run the following code:

```python
import thinkgreen
thinkgreen.update_package()
```
