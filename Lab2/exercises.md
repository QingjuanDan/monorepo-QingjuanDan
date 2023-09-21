# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

Yes, Python's Standard Library functions like `.pop()`, `.clear()`, `.copy()`, and `.get()` are well-named, reflecting their actions effectively.

2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

A dictionary is a mutable, unordered collection of key-value pairs where each key must be unique, and it is optimized for retrieving values when the key is known. It is defined using curly braces {}. In contrast, a list is a mutable, ordered collection of elements that allows duplicates and is optimized for retrieving elements by their position in the list. It is defined using square brackets [].

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

Yes, lists in Python do allow for random access, meaning you can access any element directly using an index, like `myList[7]`.

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?

Pros:
1. Flexibility: Can be used in various scenarios and domains.
2. Usability: Accommodates different needs without requiring multiple libraries.
3. Extensibility: Easy to extend and integrate with other types and libraries.

Cons:
1. Complexity: Handling various types can increase code complexity and maintenance.
2. Performance: Type-agnostic structures might not be optimized for specific data types, potentially impacting performance.
3. Error Proneness: More prone to runtime errors due to type mismatches or incorrect usage.

## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

Yes it's well named.
2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

Yes, the constructor of the `requests.Request` class has numerous arguments, potentially making it confusing, but they are optional and well-documented, aiding in usability and flexibility.

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  

`**kwargs` allows passing variable keyword arguments to a function, providing flexibility and extensibility but can potentially cause unclear API, complicate debugging, and hinder clarity in documentation.

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?

Default values in method parameters (like `None`) are optional; they're used if no value is provided when the method is called, allowing for more flexible method calls.
