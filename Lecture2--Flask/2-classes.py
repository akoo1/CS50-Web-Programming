
# Classes are used to define entirely new data types.  User-defined data type.
class Point:
    def __init__(self, x, y):      # In Python, self refers to the object that was just created
        self.x = x                 # This means initializes the object p1's data attribute x to x, which is the argument 3
        self.y = y                 # This means initializes the object p1's data attribute y to y, which is the argument 4
                                   # The dot notation gives you access to an object's data attribute

p1 = Point(3, 4)
print("The x value is", p1.x)
print("The y value is", p1.y)
