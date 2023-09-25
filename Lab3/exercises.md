# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!


## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
	- MObject is a concrete class because it can be instantiated, and it is not defined as abstract, even though it doesn’t have any implemented methods or attributes.

1. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
	- ' __del__' method in the Image class would act as a destructor; it would define behavior for cleaning up resources or performing other necessary de-allocation actions when an object of the class is about to be destroyed by the garbage collector.

1. What class does Texture inherit from?
	- The `Texture` class inherits from the `Image` class.

1. What methods and attributes does the Texture class inherit from 'Image'? 
	- The `Texture` class inherits all methods (`__init__`, `getWidth`, `getHeight`, `getPixelColorR`, `getPixels`, `setPixelsToRandomValue`) and attributes (`m_width`, `m_height`, `m_colorChannels`, `m_Pixels`) from the `Image` class.

1. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
	- I think a texture should have a 'has-a' relationship with 'Image', especially if we consider scenarios where a texture might have additional attributes and methods that are not applicable to a regular image, such as mapping methods, tiling, or wrapping modes.

	- We can refractor the code like this:
	```python
	class Texture:
    def __init__(self, w, h):
        self.image = Image(w, h)  # Texture has-an Image
    
    # Additional Texture-specific methods and attributes can be added here
	```
1. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 
	- Yes, if we didn't declare a constructor for a class, Python will automatically use the constructor of its superclass. If none is found in any ancestor class, it defaults to the basic object constructor.

## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
  	-  `Logger created exactly once`
  - If the logger is already initialized, it will print:
  	-  `logger already created`
Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

```python
class Logger:
    _instance = None  # Private class variable to hold the single instance

    def __new__(cls):
        if cls._instance is None:
            print("Logger created exactly once")
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.messages = []  # Initialize messages attribute in the instance
        else:
            print("Logger already created")
        return cls._instance

    def add_message(self, message):
        self.messages.append(message)


def main():
    # Logger should only be initialized one time if it is properly
    # refactored as a singleton class
    for i in range(3):
        logger = Logger()
        logger.add_message(f"Adding message number: {i}")


if __name__ == "__main__":
    main()
```

1. Are singleton's in Python thread safe? Why or why not?

* Singletons in Python are not inherently thread-safe due to the possibility of multiple threads creating instances simultaneously. To make a Singleton thread-safe, we can use a locking mechanism like `threading.Lock` to synchronize instance creation, ensuring only one thread can create an instance at a time.  
