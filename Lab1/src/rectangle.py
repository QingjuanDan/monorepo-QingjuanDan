"""
 Sample modified from CS5500, Mike Shah

 A rectangle class
 Note that there is no constructor or destructor,
 so a default one will be created for us.
"""
class Shape(ABC):
	def __init__(self, width, height):
		self._width = width
		self._height = height

	@abstractmethod
	def set_values(self, width, height):
		pass

	@abstractmethod
	def area(self):
		pass
class Rectangle:
    def set_values(self, x, y):
        super().__init__(width, height)

    def area(self):
        return self.width * self.height


if __name__ == "__main__":
    # Create a rectangle object
    rect = Rectangle()

    # Call a member function
    rect.set_values(3, 4)

    # Print out the area function
    print("area:", rect.area())
