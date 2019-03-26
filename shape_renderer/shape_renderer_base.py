# Shape Renderer that currently supports Rectangles

class ShapeRendererBase():

    def __init__(self, height, width, output):
        self._point_shapes = [] # list of (point, shape) tuples
        self._height = height
        self._width = width
        self._output = output

    def get_points_to_shapes(self): # returns list of (point, shape) tuples
        return self._point_shapes

    def add_shape(self, point, shape):
        if point.getx() > self.get_width() or point.gety() > self.get_height():
            return # raise exception instead

        self.get_points_to_shapes().append((point, shape))

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def render_shapes(self): # calls shape.render() on all shapes
        with open(self._output, 'w') as fp:
            fp.write('<canvas id="myCanvas" \
                              width="%d" height="%d" \
                              style="border:1px \
                              solid #000000;"></canvas>' % (self._width, self._height))
            fp.write('<script> \
                    var c = document.getElementById("myCanvas"); \
                    var ctx = c.getContext("2d");')
            for (point, shape) in self.get_points_to_shapes():
                instructions = list(map(lambda a : 'ctx.' + a + ';', shape.render(point)))
                fp.write('\n'.join(instructions))

            fp.write('</script>')

class Rectangle():

    def __init__(self, height, width):
        self._height = height
        self._width = width

    def get_height(self):
        return self._height

    def get_width(self):
        return self._width

    def render(self, point):
        return [ \
                'fillRect(%d, %d, %d, %d)' % (point.getx(), point.gety(), self._width, self._height) \
                ]


class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y
        

if __name__ == '__main__':

    rec1 = Rectangle(100, 200)
    rec2 = Rectangle(300, 300)

    sr = ShapeRendererBase(500, 700, 'output.html')

    sr.add_shape(Point(400, 100), rec1)
    sr.add_shape(Point(200, 300), rec2)

    sr.render_shapes()

