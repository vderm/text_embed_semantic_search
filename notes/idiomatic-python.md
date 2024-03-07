---
author: Raymond Hettinger
categories: website
tags:
- programming
- reference
title: Transforming Code into Beautiful, Idiomatic Python
links:
- https://www.youtube.com/watch?v=OSGv2VnC0go
- https://speakerdeck.com/pyconslides/transforming-code-into-beautiful-idiomatic-python-by-raymond-hettinger-1
---

Program the Python way, beautiful is better than ugly!


## Looping in sorted order (reversed)
```
for color in sorted(colors, reverse=True):
    print(color)
```

## A for-loop has a built-in conditional
So you can use "else" for the last iteration:

```
def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
        else:
            return -1
        return i
```

## Construct a dictionary from pairs
```
names = [...]
colors = [...]

d = dict(izip(names, colors))
```

## Counting with dictionaries
```
colors = ['red', 'green', 'red', 'blue']
d = defaultdict(int)  # if not there, creates a int
for color in colors:
    d[color] += 1
```

## Grouping with dictionaries
```
d = defaultdict(list)  # if not there, creates a list
for name in names:
    key = len(name)
    d[key].append(name)
```

## Linking dictionaries together
```
defaults = {'color': 'red', 'user', 'guest'}
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args([])
command_line_args = {k:v for k, v in vars(namespace).items() if v}
```

BAD:
```
d = defaults.copy()
d.update(os.environ)
d.update(command_line_args)
```

GOOD:
```
d = ChainMap(command_line_args, os.environ, defaults)
```

## Clarify multiple return values with named tuples
```
TestResults = namedtuple('TestResults', ['failed', 'attempted'])
```

## Updating multiple state variables
```
def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        print x
        x, y = y, x+y

x, y, dx, dy = (x + dx * t,
                y + dy * t,
                influence(m, x, y, dx, dy, partial='x'),
                influence(m, x, y, dx, dy, partial='y'))
```

## Concatenating strings
Two combine strings, use "join" not "+"
```
names = [...]
print(', '.join(names))
```

## Updating sequences
use deque not a list/dictionary

## Decorators and context managers
use them @
with xyx:
    print...


Factor-out temporary contexts
BAD:
```
try:
    os.remove('somefile.tmp')
except: OSError:
    pass
```

GOOD:
```
with ignored(OSError):
    os.remove('somefile.tmp')
```

## Generator expressions
BAD:
`print sum([i**2 for i in range(10)])`
GOOD:
`print sum(i**2 for i in range(10))`

# Beyond PEP 8 -- Best practices for beautiful intelligible code - PyCon 2015
#+Author: Raymond Hettinger
Video: https://www.youtube.com/watch?v=wf-BqAjZb8MI

## 80-100 line limit
90ish instead; enough to finish up, but not too much

## Enter/exit/repr/len/getitem in Class
in the class

```
def __enter__(self):
    return self

def __exit__(self, ...):

def __repr__(self):  # for subclassing
    return '%s(%r)' % (self.__class__.__name__, self....)

def __len__(self):  # how big is something (better than get size)

def __getitem__(self, index):
    if index >= len(self):
        raise IndexError
    return ...
```

with __len__ and __getitem__ the class becomes a sequence -> iterable

so that it can be used like:
with class as ...:
    ...

## Named tuples
BAD:
`p = (170, 0.1, 0.6)`

GOOD:
```
from collections import namedtuple
Color = namedtuple('Color', ['hue', 'saturation', 'luminosity'])
p = Color(170, 0.1, 0.6)
if p.saturation >= 0.5: ...
```