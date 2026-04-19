# PYTHON
```

***Python*** is a versatile, high-level, and human-friendly programming language favored for its readability, simplicity, and widespread use in data science, AI, web development, and automation

```
***Pros**: Easy to learn, versatile, large community support, high productivity.
***Cons**: Slower speed compared to compiled languages like C++
```

Key **Data Types**: Includes integers (int), decimal numbers (float), text (str), and boolean (bool).
**Data Structures**: Lists (ordered, mutable), sets (unordered, unique), and dictionaries (key-value pairs).
**Installation & Tools**: Installed from ***python.org***. Popular IDEs include PyCharm, VS Code, and Jupyter.

** Interactive shell** : REPL (read-evaluate-print-loop)
**Python program**: .py

```
## Learning resources
```
- https://python.land/python-tutorial
-
```
##  Why learn python
- Web development
- Data science
- Data analysis
- Machine Learning
- Artificial intelligence(AI)
- scripting and tooling

(comprehensive base libraries and frameworks)

## Python 2 vs Python 3

Python 2 and 3 have been developed and maintained side by side for an extended period. The primary reason is that Python 3 code is not entirely backward compatible with Python 2 code. This incompatibility caused a prolonged adoption rate. Many people were happy with version 2 and had no reason to upgrade.

On top of that, Python 3 was initially slower than Python 2. As Python 3 kept improving and receiving new features, it eventually took off. With the latest efforts led by Guido, Python 3 is now faster than ever. In addition, Python 3 adds many useful features to the language, making it easier and more fun. Unless you need to maintain a legacy code base, avoid Python 2.
```
###Python Basics
solid base-level knowledge of the important topics
```
- Python Perl
    - arithmetic operators
        - + ,-,*,/,%,//,**
        - operator precedence
            - mathematics and left to right for tie breakers

- variables
    - Case Types:
        Camel-case
            - e.g. Pythonistas use shopping_cart_total
    - Data Types
        - int e.g. 2
            - random.randint()
            - str()
            - isinstance(value, int)
        - float e.g. 2.0
            - round()
            - [math module]
                - floor()
                - Ceil()



- strings (' ')
    - escaping \
    - mulitline ("""  "")
    - escape sequence (\n,\r,\t)

    string operations ( built-in)
    - built in functions
    - slicing ( mystring[start:stop:stepsize])
    - chaining calls
    - Formatting( f-strings)
        - f' This is a string {mystring}''

- the print() function
- Booleans
    A boolean is the simplest data type; it’s either True or False
    - if [condition]: Code-block  // executes if the condition is found true
    - else: code-block // exception condition

    comparison operators (>,<,<=,>=, == , !=)
    logic operators ( and , or, not)

- Loops
    An iterable is an object in Python that can return its members one at a time

    - for [variable] in  [iterable]: code-block
        On each iteration, an element from iterable is assigned to variable ( indexed )
    
    - While [condition]: code-block
        while this expression evaluates to True, keep doing the stuff below

- Functions
    A Python function is a named section of a program that performs a specific task and, optionally, returns a value

    - def [functionName]():
         code-block // to call function call the code name initialised after the def keyword
        return [output] // you can also use the  **'pass'** keyword to break free from the function code block

        //functions can take arguments in the () of the function, more than one argument not a problem , separate by commas
    - Variable scope
        The visibility of a variable is called scope. The scope defines which parts of your program can see and use a variable.

- Try...except
- Dictionaries {:}
    - get()
    - dictionary comprehensions
        {X: X**2 for x in (values of x)}
    - dict.fromkeys()
    - items()
    - **dict
- Tuple ()
    - tuples are immutable 
    - tuples can be hashed
- lists []
    - create/delete
        del keyword
    - modify
        - append()
        - *list
        - pop()
        - remove()
        - clear()
    - sort
        - remove duplicates
            -set()
        - count()
        - index()
        - sort()
        -reverse()
    - loop
    - slice
- set {}
    sets can only hold unique values, allow mixed types and are unordered
    - modify
        - add()
        - update()

- Numbers
- Iterators

#\ is a comment

```
###Python objects 

```
***Python functions***
__add__  are called magic/dunder methods.

**Methods**
When a function is part of an object or Python class, we call it a method.

**Object**
An object is a collection of data (variables) and methods that operate on that data. Objects are defined by a Python class.

**class**
A class is the blueprint for one or more objects

Python constructor 
    - car = Car() // default constructor
        // can take parameters


```
### Structure your project: Modules and Packages

```
Modules are the ideal way to group and organize code, while packages are collections of Python modules.
In python a single python fileused to preform some tasks, is called a script.
Python code ends with a .py extension

Python imports
- import [modulename]

calling on an import
- modulename.my_function()

importing certain parts of a module
- from [myModule] import [My_function]
 
import aliases
- import [myModule] as [alias]

// if __name__ == '__main__'
When we import a module, its name (stored in the variable __name__) is equal to the module name. When a script is executed, its name is always set to the string __main__. Hence, if we check for this name, we find out if we are running as a script or if we’re included somewhere as a module.

// you may be interested in finding out what the __init__.py is in a python package

``` 
Python Extensions
- Python
    - intelliSense
    - linting
    - debugging
    - code navigation
    - code formatting
    - refactioring
    - variable explorer
    - test explorer
    - snippets
    (pylance)

- SonarQube for IDE
    - plugin that detects bugs and mistakes ( security and code-quality issues)
- magicPython
- Python Indent
-AutoDocstring
    - helps quickly generate docstrings snippets
- Visual Studio Intellicode

// visual studio code GUI tour
- https://python.land/creating-python-programs/vscode-gui-tour

(run configurations)
