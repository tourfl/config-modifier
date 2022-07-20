# Config modifier

Achieves changes to a given config file. :rocket:

Coded in Python 3.6.

## How to run

```
python main.py
```

You can specify config file and changes file pathes.

```
python main.py --config ./inputs/config2.json --changes ./inputs/changes4.txt
```



## How to run tests (unit)

You must have [Python package manager](https://pypi.org/project/pip/) installed. It is recommanded to use virtual environnement (as [venv](https://docs.python.org/3/library/venv.html)).

After you've set the virtual environnement, please type:

```
pip install -r requirements.txt

pytest
```

The 9 tests should pass.




