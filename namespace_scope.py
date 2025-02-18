"""
From RealPython's YT Video: Namespaces in Python: Built-in, Global, Enclosing and Local
Link: https://youtu.be/dBg8ueJaq-w?si=8x_pGkYh5r1cPcl_
"""

# print(__doc__)


# class SomeClass:
#     """
#     this is a simple docstring inside the SomeClass class. pffffft
#     """

#     def __init__(self):
#         print(self.__doc__)


# hugeObj = SomeClass()


# def someFunc():
#     """
#     Docstring inside a weird function.
#     """
#     print(someFunc.__doc__)


# print(f'Name of the function is {someFunc.__name__}')

"""
Types of namespaces:
1. Built-in (always available when python is running)
2. Global
3. Enclosing & Local
"""
# 2. Global
# There is a globals() namespace, which we see using globals()
# This is a dictionary of all the global variables and functions in the module

# When we define a variable we can find it in globals() namespace dictionary
import datetime
x = 'foo'
# print(globals())

# We can also define a new variable using the globals() namespace dictionary
globals()['y'] = 'bar'
# print(globals())

# We can finally use those 2 variabels to do a simple concatenation as shown below
z = x + y
# print(globals())
# print(z)

# When we import a module --- only the module is added into the current globals() namespace dict.
# Not the names which are inside the module
# e.g. the datetime module from import

# because python interpreter creates a brand new namespace for every module that we import using the 'import' statement
# print(globals())

# 3. Enclosing and Local
# locals() - accesses only the local variables when it is called.
# Once a function is terminated, only the function and other local variables outside this function
# exist within the locals() namespace dictionary
# each function has a different locals namespace dictionary


def f(x, y):
    print('Start f()')
    s = 3000
    print(locals())

    def g():
        print('Start g()')
        t = 2000
        print(locals())
        print('End g()')
    g()
    print(locals())
    print('End f()')


f(10, 12)
