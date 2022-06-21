# Python Variables

### Global Keyword

```python
x = "global "

def foo():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)

foo()
```

In the above code, we declare x as a global and y as a local variable in the `foo()`. Then, we use multiplication operator `*` to modify the global variable x and we print both x and y.

After calling the `foo()`, the value of x becomes `global global` because we used the `x * 2` to print two times `global`. After that, we print the value of local variable y i.e `local`.

```python
x = 0
def outer():
    x = 1
    def inner():
        global x
        x = 2
        print("inner:", x)
        
    inner()
    print("outer:", x)

outer()
print("global:", x)

# inner: 2
# outer: 1
# global: 2
```

### Nonlocal Variables

Nonlocal variables are used in nested functions whose local scope is  not defined. This means that the variable can be neither in the local nor the global scope. The `nonlocal` keyword is used to work with  variables inside nested functions, where the variable should not belong to the inner function.

Let's see an example of how a nonlocal variable is used in Python.

We use `nonlocal` keywords to create nonlocal variables.

```python
def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()
```

**Output**

```
inner: nonlocal
outer: nonlocal
```

In the above code, there is a nested `inner()` function. We use `nonlocal` keywords to create a nonlocal variable. The `inner()` function is defined in the scope of another function `outer()`.

**Note** : If we change the value of a nonlocal variable, the changes appear in the local variable.