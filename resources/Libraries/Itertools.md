# Itertools

### `itertools.permutations(iterable)`:

- return all permutations of a list/string

### `itertools.groupby(iterable)`

* return an interablle group of groups by distinct keys, for example:

  ```python
  for key, group in groupby(s: str):
      y = len(list(group))
  # refer to the lineEncoding.py assignment in CodeSignal practice
  ```

  ```python
  >>> def print_groupby(iterable, keyfunc=None):
  ...    for k, g in it.groupby(iterable, keyfunc):
  ...        print("key: '{}'--> group: {}".format(k, list(g)))
  ```

  ```python
  >>> print_groupby("BCAACACAADBBB")
  key: 'B'--> group: ['B']
  key: 'C'--> group: ['C']
  key: 'A'--> group: ['A', 'A']
  key: 'C'--> group: ['C']
  key: 'A'--> group: ['A']
  key: 'C'--> group: ['C']
  key: 'A'--> group: ['A', 'A']
  key: 'D'--> group: ['D']
  key: 'B'--> group: ['B', 'B', 'B']
  ```

  

