# recall the general structure of a class and understand that
# the Constructor and attribute definition are combined

# class definition, 
# the brackets would contain the class it inherits from (if it inherits from anything)
class Rectangle():

    # Constructor for this class, so that we can create objects of this type
    # e.g.  new_rectangle = Rectangle(5, 4)
    def __init__(self, height, width):

        # define attributes, they can be public or private
        # most commonly private to follow encapsulation (denoted by _ in front)
        self._height = height
        self._width = width

    # define any methods for your class
    # this is a getter, used to get private data
    def get_height(self):
        return self._height

    # this is a setter, used to change private data
    def set_height(self, new_height):
        if(new_height > 0):
            self._height = new_height

    def get_width(self):
        return self._width

    def get_area(self):
        return self._height * self._width

    
# example without comments many comments

class ShapeManager():

    def __init__(self, area_limit): # passing area_limit to constructor
                                    # could define area_limit in other ways (maybe a setter)

        self._area_limit = area_limit
        self._curr_area = 0 # the current total area in the manager
        self._all_shapes = []

    def get_curr_area(self):
        return self._curr_area

    def add_rectangle(self, rect):
        rect_area = rect.get_area()

        # if this rectangle goes over the area limit
        if(self._curr_area + rect_area > self._area_limit): 
            print("Cannot add this Rectangle")
            return

        self._curr_area += rect_area # add the rectangle's area to the current area held
        self._all_shapes.append(rect) # 'manage' this rectangle by adding it to the private list


new_rectangle = Rectangle(4, 5) # creating a Rectangle object
print(new_rectangle.get_area()) # calling one of its methods
