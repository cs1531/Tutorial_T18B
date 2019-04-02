from shape_renderer_base import Point
from shape_renderer import ShapeRenderer
from Shape import Rectangle, Circle

rec1 = Rectangle(100, 200)
rec2 = Rectangle(300, 300) # square
circle = Circle(50) # square

sr = ShapeRenderer(500, 700, 'output.html')

sr.add_shape(Point(400, 100), rec1)
sr.add_shape(Point(200, 200), rec2)
sr.add_shape(Point(50, 50), circle)

sr.scale_shapes(0.5)
sr.translate_shapes(50, 0)
sr.render_shapes()

