# Python Files & Structures

### Packages

As our application program grows larger in size with a lot of  modules, we place similar modules in one package and different modules in different packages. This makes a project (program) easy to manage and conceptually clear.

Similarly, as a directory can contain subdirectories and files, a Python package can have sub-packages and modules.

A directory must contain a file named `__init__.py` in  order for Python to consider it as a package. This file can be left empty but we generally place the initialization code for that package in this file.

Here is an example. Suppose we are developing a game. One possible organization of packages and modules could be as shown in the figure below.

![image-20220621153920148](C:\Users\User\AppData\Roaming\Typora\typora-user-images\image-20220621153920148.png)