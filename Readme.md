# Config modifier

Achieves changes to a given config file. :rocket:

[Detailed specifications (technical-test.md)](technical-test.md).

Requires Python 3.6 or more.

## How to install


You must have [Python package manager (pip)](https://pypi.org/project/pip/) installed. It is recommanded to use virtual environnement (as [venv](https://docs.python.org/3/library/venv.html)).

To set the virtual environnement and install requirements:

```
python -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

## How to run

```
python main.py
```

There are default config and changes files. You can specify them too.

```
python main.py --config ./inputs/config2.json --changes ./inputs/changes4.txt
```



## How to test (unit)

```
pytest
```

The 9 tests should pass.




