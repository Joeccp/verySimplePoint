from point import Point as P

# --------------------
# Basic usage you need to know (^*^)b
origin = P(0, 0)
a = P(2, 3)
a.x  # 2
a.y  # 3
len(a)  # 2, which is X-Coordinate
assert a == (2, 3)
assert a != origin
assert str(a) == "(2, 3)"
b = P(0, -3)  # +ve/0/-ve integer: OK
assert b.quadrant is None  # Any point that lies on X/Y-Axis does NOT belong to any quadrant, blame maths, not me
assert P(-8, -11).quadrant == 3  # Quadrant III
human = {"name": "Alex", "age": 15, "x": 6, "y": 9}
assert human == P(6, 9)
assert origin.isOrigin
assert origin.isOnXAxis
assert origin.isOnYAxis
c = P(123, 456)
c.x = -666
c.y = 888
assert c == (-666, 888)
(c.x, c.y) = (987, 654)
assert c == P(987, 654)
x = P(5, 6)
y = P(8, 10)
assert x.distance(y) == 5

quit()
# --------------------
# DON'T DO THIS!!!
e = P(3.5, 4.0)  # X-Coordinate and Y-Coordinate can only be int, sorry :(
e.X  # NO CAPITAL LETTER!!!!!!
e.Y  # I SAID DON'T YELL AT ME!!!!!!!!!

