# Python Arguments

### Overview

As guidance:

- Use positional-only if you want the name of the parameters to not be available to the user. This is useful when parameter names have no real meaning, if you want to enforce the order of the arguments when the function is called or if you need to take some positional parameters and arbitrary keywords.
- Use keyword-only when names have meaning and the function definition is more understandable by being explicit with names or you want to prevent users relying on the position of the argument being passed.
- For an API, use positional-only to prevent breaking API changes if the parameter’s name is modified in the future.

### List Arbitrary Arguments

An ***arbitrary argument list\*** is a Python feature to call a function with an arbitrary number of arguments.

 It’s based on the asterisk “unpacking” operator `*`. To catch an arbitrary number of function arguments in a tuple `args`, use the asterisk syntax `*args `within your function definition. For example, the function `def f(*args): ...` allows for an arbitrary number, and type, of arguments such as `f(1)`, `f(1, 2)`, or even `f('Alice', 1, 2, (3, 4))`. 

```py
def f(a, *arguments):
    print(a)
    for arg in arguments:
        print(arg)
f("A", "B", "C")
```

### Arbitrary Keyword Arguments

`**kwargs` works the same as `*args` but instead of accepting positional arguments, it accepts keyword arguments such as those from a dictionary (i.e. a dictionary of arguments). Use 2 asterisks `(**)` to unpack dictionaries.

```python
def full_name(**kwargs):
    for key, value in kwargs.items():
        print("%s is %s" % (key,value))
```

