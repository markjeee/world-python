## World Python

A demo package in Python, used to explore in creating packages in
Python.

## How to use

Add in your Pipfile as:

```
[packages]
world-python = "*"
```

Then install,

```
pipenv install
```

You may now use it as:

```
import world-python
print world-python.world()
```
