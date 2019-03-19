from Rectangle import Rectangle
from Circle import Circle
from ShapeManager import ShapeManager

sm = ShapeManager(40)

r = Rectangle(4, 5)
c = Circle(3)

sm.add_shape(r) # can add this only area of 20
sm.add_shape(c) # can't add this, 20 + (3 * 3 * 3.1415) > 40
sm.add_shape(r) # can add this, 20 + 20 is not yet greater tha 40
sm.add_shape(r) # can't add this anymore

# as you can see, the ShapeManager doesnt care what shape it is given, it will still work

