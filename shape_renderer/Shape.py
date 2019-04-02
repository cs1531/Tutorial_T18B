from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def render(self, point):
        pass

    @abstractmethod
    def scale(self, scalar):
        pass

class Rectangle(Shape):

    def __init__(self, height, width):
        self._height = height
        self._width = width

    def get_height(self):
        return self._height

    def get_width(self):
        return self._width

    def scale(self, scalar):
        self._height *= scalar
        self._width *= scalar

    def render(self, point):
        return [ \
                'fillRect(%d, %d, %d, %d)' % (point.getx(), point.gety(), self._width, self._height) \
                ]

class Circle(Shape):

    def __init__(self, radius):
        self._radius = radius

    def scale(self, scalar):
        self._radius *= scalar

    def get_radius(self):
        return self._radius

    def render(self, point):
        return ['beginPath()', \
                'arc(%d, %d, %d, 0, 2 * Math.PI)' % (point.getx(), point.gety(), self.get_radius()), \
                'stroke()']

