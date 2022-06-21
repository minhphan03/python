# Python Operators

### Shift Operators

* **x << y**

  Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the  same as multiplying x by $2^y$. 

  ```python
  Example 1:
  a = 5 = 0000 0101 (Binary)
  a << 1 = 0000 1010 = 10
  a << 2 = 0001 0100 = 20 
  
  Example 2:
  b = -10 = 1111 0110 (Binary)
  b << 1 = 1110 1100 = -20
  b << 2 = 1101 1000 = -40 
  ```

* **x >> y**

  Returns x with the bits shifted to the right by y places. This is the same as //'ing x by $2^y$  

  ```python
  Example 1:
  a = 10 = 0000 1010 (Binary)
  a >> 1 = 0000 0101 = 5
  
  Example 2:
  a = -10 = 1111 0110 (Binary)
  a >> 1 = 1111 1011 = -5 
  ```

### Bitwise Operators

* **x & y (AND)** 

  Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0. 

  ```python
  a = 10 = 1010 (Binary)
  b = 4 =  0100 (Binary)
  
  a & b = 1010
           &
          0100
        = 0000
        = 0 (Decimal)
  ```

* **x | y (OR)**

  Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.

  ```python
  a = 10 = 1010 (Binary)
  b = 4 =  0100 (Binary)
  
  a | b = 1010
           |
          0100
        = 1110
        = 14 (Decimal)
  ```

* **~ x (NOT)**

  Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1. 

  ```python
  a = 10 = 1010 (Binary)
  
  ~a = ~1010
     = -(1010 + 1)
     = -(1011)
     = -11 (Decimal)
  ```

  

* **x ^ y (XOR)** 

  Does a "bitwise exclusive or". Each bit of the output is the same as the  corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1. 

  Sets each bit to 1 if only one of two bits is 1

  ```python
  a = 10 = 1010 (Binary)
  b = 4 =  0100 (Binary)
  
  a ^ b = 1010
           ^
          0100
        = 1110
        = 14 (Decimal)
  ```

  