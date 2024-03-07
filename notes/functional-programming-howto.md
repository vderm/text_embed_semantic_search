---
author:
- A. M. Kuchling
categories: website
draft: false
lastmod: 2021-01-03 22:49:09-05:00
tags:
- programming
- reference
title: Functional Programming How-To
links:
- https://docs.python.org/3/howto/functional.html
---

<https://docs.python.org/3/howto/functional.html>

## General {#general}

Most programming languages are **procedural**: programs are a lit of instructions
that tell the computer what to do with the program's input.

- **Declarative**: you write a specification that describes the
    problem to be solved (SQL)
- **Object-oriented**: manipulate collections of objects, objects have internal
    states and support methods to query or modify this state
- **Functional**: decomposes a problem into a set of functions where inputs are
    transformed to outputs without having an internal state

Functional programs offer _modularity_ and easier debugging and testing.
_Composability_ is also available since functions are cascaded together.

## Iterators {#iterators}

An iterator is an object representing a stream of data; this object returns the
data one element at a time. A Python iterator must support a method called
\_\_next\_\_() that takes no arguments and always returns the next element of the
stream. If there are no more elements in the stream, \_\_next\_\_() must raise the
StopIteration exception.

The built-in iter() function takes an arbitrary object and tries to return an
iterator that will return the object’s contents or elements, raising TypeError
if the object doesn’t support iteration.

```python
L = [1, 2, 3]

it = iter(L)

it
<...iterator object at ...>

it.__next__()  # same as next(it)
1

next(it)
2

next(it)
3

next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
```

Note that you can only go forward in an iterator; there’s no way to get the
previous element, reset the iterator, or make a copy of it. Iterator objects can
optionally provide these additional capabilities, but the iterator protocol only
specifies the \_\_next\_\_() method.

## Generator expressions and list comprehensions {#generator-expressions-and-list-comprehensions}

Two common operations on an iterator’s output are 1) performing some operation
for every element, 2) selecting a subset of elements that meet some condition.

```python
line_list = ['  line 1\n', 'line 2  \n', ...]

# Generator expression -- returns iterator
stripped_iter = (line.strip() for line in line_list)

# List comprehension -- returns list
stripped_list = [line.strip() for line in line_list]
```

## Generators {#generators}

Generators are a special class of functions that simplify the task of writing
iterators. Regular functions compute a value and return it, but generators
return an iterator that returns a stream of values.

You’re doubtless familiar with how regular function calls work in Python or C.
When you call a function, it gets a private namespace where its local variables
are created. When the function reaches a return statement, the local variables
are destroyed and the value is returned to the caller. A later call to the same
function creates a new private namespace and a fresh set of local variables.
But, **what if the local variables weren’t thrown away on exiting a function?**
What if you could later resume the function where it left off? **This is what
generators provide**; they can be thought of as resumable functions.

```python
    def generate_ints(N):
       for i in range(N):
           yield i

  gen = generate_ints(3)

  gen
  <generator object generate_ints at ...>

  next(gen)
  0

  next(gen)
  1

  next(gen)
  2

  next(gen)
  Traceback (most recent call last):
    File "stdin", line 1, in <module>
    File "stdin", line 2, in generate_ints
  StopIteration


# A recursive generator that generates Tree leaves in in-order.
def inorder(t):
    if t:
        for x in inorder(t.left):
            yield x

        yield t.label

        for x in inorder(t.right):
            yield x
```

`yield` keyword makes it a generator function. This returns a generator object
that supports the iterator protocol. Both `yield` and `return` outputs a value
`i` except that the generator suspends the execution and preserves the local
variables. On the next call to the generator's `__next__()` method, the function
is resumed.


## Passing values into a generator {#passing-values-into-a-generator}

<https://docs.python.org/3/howto/functional.html#passing-values-into-a-generator>
val = (yield i)

- Use `send(value)` method to send the values into the generator.
- There is also `throw(type, value=None, taceback=None)` to raise an exception
    inside the generator.
- `close()` raises GeneratorExit exception to terminate the iteration.


## Built-in functions {#built-in-functions}


### map() {#map}

`map(f, iterA, iterB, ...)`: returns an iterator over the sequence

```python
def upper(s):
    return s.upper()

list(map(upper, ['sentence', 'fragment']))
['SENTENCE', 'FRAGMENT']

[upper(s) for s in ['sentence', 'fragment']]
['SENTENCE', 'FRAGMENT']
```


### filter() {#filter}

`filter(predicate, iter)`: returns an iterator over all the sequence elements
that meet a certain condition, and is similarly duplicated by list
comprehensions. A predicate is a function that returns the truth value of some
condition; for use with filter(), the predicate must take a single value.

```python
def is_even(x):
    return (x % 2) == 0

list(filter(is_even, range(10)))
[0, 2, 4, 6, 8]

# This can also be written as a list comprehension:
list(x for x in range(10) if is_even(x))
[0, 2, 4, 6, 8]
```


### enumerate() {#enumerate}


### sorted() {#sorted}

`sorted(iterable, key=None, reverse=False)` collects all the elements of the
iterable into a list, sorts the list, and returns the sorted result. The key and
reverse arguments are passed through to the constructed list’s sort() method.


### any() & all() {#any-and-all}

```python
any([0, 1, 0])
True

any([0, 0, 0])
False

any([1, 1, 1])
True

all([0, 1, 0])
False

all([0, 0, 0])
False

all([1, 1, 1])
True
```


### zip() {#zip}

```python
zip(['a', 'b', 'c'], (1, 2, 3)) =>
  ('a', 1), ('b', 2), ('c', 3)

# dictionary building
dictionary = dict(zip(keys, values))
```

It doesn’t construct an in-memory list and exhaust all the input iterators
before returning; instead tuples are constructed and returned only if they’re
requested. (The technical term for this behaviour is lazy evaluation.)


## itertools module {#itertools-module}

itertools.count(start, step) returns an infinite stream of evenly spaced values. You can optionally supply the starting number, which defaults to 0, and the interval between numbers, which defaults to 1:

```python
itertools.count() =>
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...
itertools.count(10) =>
  10, 11, 12, 13, 14, 15, 16, 17, 18, 19, ...
itertools.count(10, 5) =>
  10, 15, 20, 25, 30, 35, 40, 45, 50, 55, ...
```

itertools.cycle(iter) saves a copy of the contents of a provided iterable and returns a new iterator that returns its elements from first to last. The new iterator will repeat these elements infinitely.

```python
itertools.cycle([1, 2, 3, 4, 5]) =>
  1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
```

itertools.repeat(elem, [n]) returns the provided element n times, or returns the element endlessly if n is not provided.

```python
itertools.repeat('abc') =>
  abc, abc, abc, abc, abc, abc, abc, abc, abc, abc, ...
itertools.repeat('abc', 5) =>
  abc, abc, abc, abc, abc
```

itertools.chain(iterA, iterB, ...) takes an arbitrary number of iterables as input, and returns all the elements of the first iterator, then all the elements of the second, and so on, until all of the iterables have been exhausted.

```python
itertools.chain(['a', 'b', 'c'], (1, 2, 3)) =>
  a, b, c, 1, 2, 3
```

itertools.islice(iter, [start], stop, [step]) returns a stream that’s a slice of the iterator. With a single stop argument, it will return the first stop elements. If you supply a starting index, you’ll get stop-start elements, and if you supply a value for step, elements will be skipped accordingly. Unlike Python’s string and list slicing, you can’t use negative values for start, stop, or step.

```python
itertools.islice(range(10), 8) =>
  0, 1, 2, 3, 4, 5, 6, 7
itertools.islice(range(10), 2, 8) =>
  2, 3, 4, 5, 6, 7
itertools.islice(range(10), 2, 8, 2) =>
  2, 4, 6
```

itertools.tee(iter, [n]) replicates an iterator; it returns n independent iterators that will all return the contents of the source iterator. If you don’t supply a value for n, the default is 2. Replicating iterators requires saving some of the contents of the source iterator, so this can consume significant memory if the iterator is large and one of the new iterators is consumed more than the others.

```python
itertools.tee( itertools.count() ) =>
   iterA, iterB

where iterA ->
   0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...
and   iterB ->
   0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...
```

itertools.filterfalse(predicate, iter) is the opposite of filter(), returning all elements for which the predicate returns false:

```python
itertools.filterfalse(is_even, itertools.count()) =>
  1, 3, 5, 7, 9, 11, 13, 15, ...
```

itertools.takewhile(predicate, iter) returns elements for as long as the predicate returns true. Once the predicate returns false, the iterator will signal the end of its results.

```python
def less_than_10(x):
    return x < 10
itertools.takewhile(less_than_10, itertools.count()) =>
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9

itertools.takewhile(is_even, itertools.count()) =>
  0
```

itertools.dropwhile(predicate, iter) discards elements while the predicate returns true, and then returns the rest of the iterable’s results.

```python
itertools.dropwhile(less_than_10, itertools.count()) =>
  10, 11, 12, 13, 14, 15, 16, 17, 18, 19, ...

itertools.dropwhile(is_even, itertools.count()) =>
  1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...
```

itertools.compress(data, selectors) takes two iterators and returns only those elements of data for which the corresponding element of selectors is true, stopping whenever either one is exhausted:

```python
itertools.compress([1, 2, 3, 4, 5], [True, True, False, False, True]) =>
   1, 2, 5
```

The itertools.combinations(iterable, r) returns an iterator giving all possible r-tuple combinations of the elements contained in iterable.

```python
itertools.combinations([1, 2, 3, 4, 5], 2) =>
  (1, 2), (1, 3), (1, 4), (1, 5),
  (2, 3), (2, 4), (2, 5),
  (3, 4), (3, 5),
  (4, 5)

itertools.combinations([1, 2, 3, 4, 5], 3) =>
  (1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5),
  (2, 3, 4), (2, 3, 5), (2, 4, 5),
  (3, 4, 5)
```

The elements within each tuple remain in the same order as iterable returned them. For example, the number 1 is always before 2, 3, 4, or 5 in the examples above. A similar function, itertools.permutations(iterable, r=None), removes this constraint on the order, returning all possible arrangements of length r:

```python
itertools.permutations([1, 2, 3, 4, 5], 2) =>
  (1, 2), (1, 3), (1, 4), (1, 5),
  (2, 1), (2, 3), (2, 4), (2, 5),
  (3, 1), (3, 2), (3, 4), (3, 5),
  (4, 1), (4, 2), (4, 3), (4, 5),
  (5, 1), (5, 2), (5, 3), (5, 4)

itertools.permutations([1, 2, 3, 4, 5]) =>
  (1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5),
  ...
  (5, 4, 3, 2, 1)
```

itertools.groupby(iter, key\_func=None) collects all the consecutive elements
from the underlying iterable that have the same key value, and returns a stream
of 2-tuples containing a key value and an iterator for the elements with that
key.


## functools module {#functools-module}


### partial() {#partial}

The most useful tool in this module is the functools.partial() function.

For programs written in a functional style, you’ll sometimes want to construct
variants of existing functions that have some of the parameters filled in.
Consider a Python function f(a, b, c); you may wish to create a new function
g(b, c) that’s equivalent to f(1, b, c); you’re filling in a value for one of
f()’s parameters. This is called “partial function application”.

The constructor for partial() takes the arguments (function, arg1, arg2, ...,
kwarg1=value1, kwarg2=value2). The resulting object is callable, so you can just
call it to invoke function with the filled-in arguments.

```python
import functools

def log(message, subsystem):
    """Write the contents of 'message' to the specified subsystem."""
    print('%s: %s' % (subsystem, message))
    ...

server_log = functools.partial(log, subsystem='server')
server_log('Unable to open socket')
```


### reduce() {#reduce}

```python
import functools
# Instead of:
product = functools.reduce(operator.mul, [1, 2, 3], 1)

# You can write:
product = 1
for i in [1, 2, 3]:
    product *= i
```


## operator module {#operator-module}

- Math operations: add(), sub(), mul(), floordiv(), abs(), …
- Logical operations: not\_(), truth().
- Bitwise operations: and\_(), or\_(), invert().
- Comparisons: eq(), ne(), lt(), le(), gt(), and ge().
- Object identity: is\_(), is\_not().


## Small functions and the lambda expression {#small-functions-and-the-lambda-expression}

```python
adder = lambda x, y: x+y
print_assign = lambda name, value: name + '=' + str(value)
```