from Shape import Shape

class ShapeManager():

    def __init__(self, area_limit): # passing area_limit to constructor
                                    # could define area_limit in other ways (maybe a setter)

        self._area_limit = area_limit
        self._curr_area = 0 # the current total area in the manager
        self._all_shapes = []

    def get_curr_area(self):
        return self._curr_area

    def add_shape(self, shape):
        shape_area = shape.get_area()

        # if this shape's area goes over the area limit
        if(self._curr_area + shape_area > self._area_limit): 
            print("Cannot add this Shape")
            return

        print("Adding this Shape")

        self._curr_area += shape_area # add the Shapes's area to the current area held
        self._all_shapes.append(shape) # 'manage' this Shape by adding it to the private list

