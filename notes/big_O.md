---
author: Vasken Dermardiros
categories: note
tags:
- reference
title: Big O notation
links:
- https://stackabuse.com/big-o-notation-and-algorithm-analysis-with-python-examples/
- https://www.bigocheatsheet.com/
- https://en.wikipedia.org/wiki/Big_O_notation
---

# Algorithmic Complexity

Big O notation is about algorithmic complexity. It gives an indication on how the algorithm scales as the number of input grows.

+ Big $O$: worst-case complexity (O stands for Ordnung, it's German); upper bound
+ Big $\theta$: average case complexity; approximate trend; Big theta is either the exact performance value of the algorithm, or a useful range between narrow upper and lower bounds
+ Big $\Omaga$: best-case complexity; e.g. search for a number in list and it happens to be the first one

# Scaling

![Big O complexity chart](../attachments/2022-12-07-14-39-36.png)

![Common data structure operations](../attachments/2022-12-07-14-40-01.png)

![Array sorting algorithms](../attachments/2022-12-07-14-40-26.png)

# Common Cases

| Name | Big O |
| ---- | ----- |
| Constant | O(c) |
| Linear | O(n) |
| Quadratic | O(n²) |
| Cubic | O(n³) |
| Exponential | O(2ⁿ) |
| Logarithmic | O(log(n)) |
| Log Linear | O(nlog(n)) |

## Examples

<https://en.wikipedia.org/wiki/Big_O_notation#Orders_of_common_functions>

    T(n) = O(n100)
    T(n) = O(n3)
    T(n) = Θ(n3)

The equivalent English statements are respectively:

    T(n) grows asymptotically no faster than n100
    T(n) grows asymptotically no faster than n3
    T(n) grows asymptotically as fast as n3.

Typically we prefer having the closest upper bound (2nd statement)

    O(n): at n=1, 1 step is taken. At n=10, 10 steps are taken.
    O(n²): at n=1, 1 step is taken. At n=10, 100 steps are taken.

## Constant complexity

``` python
def constant_algo(items):
    result = items[0] * items[0]
    print(result)

constant_algo([4, 5, 6, 8])
```

## Linear complexity

``` python
def linear_algo(items):
    for item in items:
        print(item)

    # Even if you add another iterator, it becomes O(2n) which is equivalent to O(n)
    for item in items:
        print(item)

linear_algo([4, 5, 6, 8])
```

## Quadratic complexity

``` python
def quadratic_algo(items):
    for item in items:
        for item2 in items:
            print(item, ' ' ,item2)

quadratic_algo([4, 5, 6, 8])
```

## Space complexity

The following has a quadratic (square) space complexity.

``` python
def return_squares(n):
    square_list = []
    for num in n:
        square_list.append(num * num)

    return square_list

nums = [2, 4, 6, 8, 10]
print(return_squares(nums))
```
