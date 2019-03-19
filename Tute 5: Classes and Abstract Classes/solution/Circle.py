from Shape import Shape

class Circle(Shape):

    def __init__(self, radius):
        self._radius = radius

    def get_area(self):
        return self._radius * self._radius * 3.1415 # cheating here
