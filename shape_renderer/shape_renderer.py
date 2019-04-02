from shape_renderer_base import ShapeRendererBase

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

        

