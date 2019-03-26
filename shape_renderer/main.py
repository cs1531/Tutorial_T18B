from shape_renderer_base import ShapeRendererBase, Rectangle, Point

rec1 = Rectangle(100, 200)
rec2 = Rectangle(300, 300) # square

sr = ShapeRendererBase(500, 700, 'output.html')

sr.add_shape(Point(400, 100), rec1)
sr.add_shape(Point(200, 300), rec2)

sr.render_shapes()

