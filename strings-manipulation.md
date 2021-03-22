
### Raw strings has r in front of the string
```python
print(r'That is Carol\'s cat.')
```

> That is Carol\'s cat.


### Multiline Strings with Triple Quotes
While you can use the \n escape character to put a newline into a string, it is often easier to use multiline strings. A multiline string in Python begins and ends with either three single quotes or three double quotes. Any quotes, tabs, or newlines in between the “triple quotes” are considered part of the string. Python’s indentation rules for blocks do not apply to lines inside a multiline string.
```python
print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')
```
Save this program as catnapping.py and run it. The output will look like this:

----------
Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob

---------
### Justifying Text with rjust(), ljust(), and center()
The rjust() and ljust() string methods return a padded version of the string they are called on, with spaces inserted to justify the text. The first argument to both methods is an integer length for the justified string. Enter the following into the interactive shell:

```python

'Hello'.rjust(20, '*')
```
> '***************Hello'

```python
'Hello'.ljust(20, '-')
```
> 'Hello---------------'

The center() string method works like ljust() and rjust() but centers the text rather than justifying it to the left or right. Enter the following into the interactive shell:

```python
'Hello'.center(20)
```
> '       Hello       '

```python
'Hello'.center(20, '=')
```
> '=======Hello========'

An example:
```python
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
```

Output:

---------

---PICNIC ITEMS--

sandwiches..    4

apples......   12

cups........    4

cookies..... 8000

-------PICNIC ITEMS-------

sandwiches..........     4

apples..............    12

cups................     4

cookies.............  8000

-----------
