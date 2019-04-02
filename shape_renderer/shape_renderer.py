from shape_renderer_base import ShapeRendererBase

# extending the base class
# very nice way to combat requirement changes
# and very nice way to split core logic from these extra features
# allows multiple collaborators to work in different files
class ShapeRenderer(ShapeRendererBase):

    def __init__(self, height, width, output):
        super().__init__(height, width, output)

    def scale_shapes(self, scalar):
        self._height *= scalar
        self._width *= scalar

        for (point, shape) in self.get_points_to_shapes():
            point.setx(point.getx() * scalar)
            point.sety(point.gety() * scalar)

            shape.scale(scalar)

    def translate_shapes(self, x, y):
        for (point, shape) in self.get_points_to_shapes():
            point.setx(point.getx() + x)
            point.sety(point.gety() + y)

        

