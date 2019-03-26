
class Rectangle():

    def __init__(self, length, height):
        self._length = length
        self._height = height

    def get_length(self):
        return self._length

    def set_length(self, length):
        if length <= 0 :
            return # raise an exception
        self._length = length

    def get_height(self):
        return self._height

    def set_height(self, height):
        if height <= 0:
            return # raise an exception
        self._height = height




r = Rectangle(5, 4)
print(r.get_height())
