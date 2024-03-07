---
author: Federico Vallucci
categories: note
date: Feb 7, 2022
links:
- https://docs.pytest.org/en/6.2.x/contents.html
tags:
- programming
- improve
title: PyTest
---

# pytest.ini
![pytest.ini](../attachments/2022-02-07-12-06-15.png)

High-level configuration file. Can group tests together as [test scenarios](https://docs.pytest.org/en/6.2.x/example/parametrize.html#a-quick-port-of-testscenarios) and point to where the test files are.

# conftest.py
Loaded by default in pytest, override based on how close to code it is

# Decorators
## Reused variables / cache
``` python
@pytest.fixture(scope="session")  # <-- reused variable / cache
def test():
    ...
```

## Marking tests
``` python
@pytest.mark.preprocess
def test():
    ...
```

## Different Arguments, Same Test
![Permutations of test](../attachments/2022-02-07-12-16-10.png)

Can pass different arguments to a same test **but** the test should return the same error (for the sake of maintainability), instead of writting a test per different argument.

Eg. test can be an `isinstace()` where non-complying inputs result in the same error.

# VSCode
![Test panel](../attachments/2022-02-07-12-38-06.png)


# Fede's notes
official documentation :
- [set_up_folder_structure](https://docs.pytest.org/en/6.2.x/goodpractices.html#test-discovery)
- [advanced parametrize](https://docs.pytest.org/en/6.2.x/example/parametrize.html#deferring-the-setup-of-parametrized-resources)
- [advanced test scenario](https://docs.pytest.org/en/6.2.x/example/parametrize.html#a-quick-port-of-testscenarios)
- [special assertion](https://docs.pytest.org/en/6.2.x/assert.html#assert)
Basic reading
- [Basic stuff](https://realpython.com/pytest-python-testing/#test-filtering)
- [video_2 -- VSCode integration](https://www.youtube.com/watch?v=UMgxJvozR5A&t=730s)
- [video 1 -- nice package & test](https://www.youtube.com/watch?v=DhUpxWjOhME&t=324s&ab_channel=mCoding)
- [advance things](https://www.nerdwallet.com/blog/engineering/5-pytest-best-practices/)
**Some tips from advanced tutorial** [advance things](https://www.nerdwallet.com/blog/engineering/5-pytest-best-practices/) :
1. Prefer mocker over mock
2. *Parametrize the same behavior, have different tests for different behaviors*
3. Don’t modify fixture values in other fixtures
4. Prefer responses over mocking outbound HTTP requests
5. Prefer tmpdir over global test artifacts
### **CMD**
`pytest -q test_sysexit.py`  == `-q` is quiet, it will print only the summary result
`pytest -v` == `-v`  stands for verbose, print all
`pytest --fixtures` == show all the fixtures available to pytest
`pytest -m "model"` == will run only the test marked as `"model"`
`pytest -m "not model"` == will run only the test that do not have the  `"model"` mark
`pytest --durations=3` == report the 3 longest test
`pytest --collect-only` == collects only the tests (do not execute the tests)
`pytest --cov`== runs all the test and percentage of line that have been executed
set up a number of coverage (for instance 80%) so that you are ready to put a condition in CICD everytime
**plug-in**
https://github.com/pytest-dev/pytest-randomly
https://coverage.readthedocs.io/en/6.3/cmd.html

