# Python Control Flows

### Break

The [`break`](https://docs.python.org/3/reference/simple_stmts.html#break) statement, like in C, breaks out of the innermost enclosing [`for`](https://docs.python.org/3/reference/compound_stmts.html#for) or [`while`](https://docs.python.org/3/reference/compound_stmts.html#while) loop.

### Loop Else Statements

Loop statements may have an `else` clause; it is executed when the loop terminates through exhaustion of the iterable (with [`for`](https://docs.python.org/3/reference/compound_stmts.html#for)) or when the condition becomes false (with [`while`](https://docs.python.org/3/reference/compound_stmts.html#while)), but not when the loop is terminated by a [`break`](https://docs.python.org/3/reference/simple_stmts.html#break) statement.  

In other words, the `else` keyword in a `for` loop specifies a block of code to be  executed when the loop is finished. This is exemplified by the following loop, which searches for prime numbers:

```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
```

```py
2 is a prime number # executed after going through the for loop without touching the break statement
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```

### Continue

The [`continue`](https://docs.python.org/3/reference/simple_stmts.html#continue) statement, also borrowed from C, continues with the next iteration of the loop. In short, with the continue statement we can stop the  current iteration of the loop, and continue with the next.

```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
```

```python
apple
cherry
```

### [Try / Except](https://docs.python.org/3/tutorial/errors.html)

The [`try`](https://docs.python.org/3/reference/compound_stmts.html#try) … [`except`](https://docs.python.org/3/reference/compound_stmts.html#except) statement has an optional *else clause*, which, when present, must follow all *except clauses*.  It is useful for code that must be executed if the *try clause* does not raise an exception. For example:

```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```

### Else

The use of the `else` clause is better than adding additional code to the [`try`](https://docs.python.org/3/reference/compound_stmts.html#try) clause because it avoids accidentally catching an exception that wasn’t raised by the code being protected by the `try` … `except` statement.

```python
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
                         # but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)
```

```python
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
```

### Finally

If a [`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally) clause is present, the `finally` clause will execute as the last task before the [`try`](https://docs.python.org/3/reference/compound_stmts.html#try) statement completes. The `finally` clause runs whether or not the `try` statement produces an exception.

### Exception Chaining

```python
def func():
    raise ConnectionError

try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc # chaining exceptions
```

in which `exc` must be exception instance or `None`

```control
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Failed to open database
```

