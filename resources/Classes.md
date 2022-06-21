#  [Python Classes](https://docs.python.org/3/tutorial/classes.html)

### Class Objects Operations

*Attribute references* use the standard syntax used for all attribute references in Python: `obj.name`.  Valid attribute names are all the names that were in the class’s namespace when the class object was created.  So, if the class definition looked like this:

```python
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
```

then `MyClass.i` and `MyClass.f` are valid attribute references, returning an integer and a function object, respectively.

`__doc__` is also a valid attribute, returning the docstring belonging to the class: `"A simple example class"`.

### Class Instantiation

When a class defines an `__init__()` method, class instantiation automatically invokes `__init__()` for the newly-created class instance.

```python
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
x.r, x.i
```

```pyt
(3.0, -4.5)
```

### Class Inheritance

The syntax for a derived class definition looks like this:

```python
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```

Derived classes kay override methods of their base classes. Because methods have no special privileges when calling other methods of the same object, a method of a base class that calls another method defined in the same base class may end up calling a method of the same name.

Python has two built-in functions that work with inheritance:

* `isinstance()` to check an instance's type: `isinstance(obj, int)` will be True only if `obj.__class__` is `int` or some class derived from `int`

### Multiple Class Inheritance

For most purposes, in the simplest cases, you can think of the search for attributes inherited from a parent class as depth-first, left-to-right, not searching twice in the same class where there is an overlap in the hierarchy. Thus, if an attribute is not found in `DerivedClassName`, it is searched for in `Base1`, then (recursively) in the base classes of `Base1`, and if it was not found there, it was searched for in `Base2`, and so on.
