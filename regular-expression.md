Import the regular expression module, a standard module in the python standard library

```python
import re

message = 'Call me 415-678-9045 tomorrow, or at 415-654-9353 which is my office line.'

phoneNumRegEx = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

```

We pass a pattern into the arguments, in which \d stands for digits

r is a raw string, and we are looking for a raw string that has the form of a number in the message

The function will then return a regular expression object, and we will use this object to find the phone number in this text

```python
mo = phoneNumRegEx.search(message)
```
Sfter we perform the search the regular expression in the object, it will return a match object. We have to convert this object to a string to display the first result.

```python
print(mo.group())
```
In case there are more than one results, find all function can display results in a list and we can print that list.
```python
mo2 = phoneNumRegEx.findall(message)
print(mo2)
```
