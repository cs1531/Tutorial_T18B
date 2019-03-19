from Shape import Shape


# class that 'realises' Shape
class Rectangle(Shape):

    def __init__(self, height, width):
        self._height = height
        self._width = width

    # implementing get_area as that is required
    def get_area(self):
        return self._height * self._width

# if defining get_area is forgotton, this wont run

# dont need to understand how this works, just the syntax


# new_rectangle = Rectangle(4, 5)
# print(new_rectangle.get_area())
