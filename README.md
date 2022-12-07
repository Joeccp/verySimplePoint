# verySimplePoint
 A single point in a two-dimensional Cartesian coordinate system.



## Contributions are welcomed! (^_-)-☆
**Just do what you should do!** Make an issue, pull request......<br/>
~~Blah Blah Blah~~  :|


## Why this module?

Because this module is very ***Simple*** and ***Easy to use***!

This module is just for <u>reducing the time used to create a new class</u> when you only need points for some simple use.
Not to replace the existence of other large modules/packages. 
This module is **not** perfect, but it will be there when you need it.



## Why NOT this module?

Because the X and Y Coordinate can only be integers (+ve/0/-ve).
No float, then no floating point trouble(ﾟ∀ﾟ).



## What can I do with this module?

I just leave it here, you **will** understand ^^
```python
from point import Point

a = Point(3, 4)
b = Point(0, 0)

a.x  # 3
a.y  # 4
```
[BUT WHAT IF I DON't UNDERSTAND? 👆🏻](https://youtu.be/VYMdlCEDYvo)

<br/>

```python
a.x = 3
a.x = 4
a.x, a.y = 3, 4  # OK
a.setCoordinate(3, 4)  # Why not?
```

```python
a == b  # False
b == (0, 0)  # True, and yes, you can do that  :)

b.isOrigin  # True
b.isOnXAxis  # True
b.isOnYAxis  # True

anotherOrigin = Point.createOriginPoint()  # If you don't like Point(0, 0)
b == anotherOrigin  # True
```

```python
str(a) == "(3, 4)"  # True
len(a)  # 3, which is the X-Coordinate
c = Point(-6, -9)
abs(c)  # (6, 9)
```

```python
target: dict = {
    "name": "Olivia",
    "gender": "female",
    "age": 13,
    "x": 38_53_43,
    "y": 77_01_30,
    "FBI": True
}

human == Point(385343, 770130)  # True
```

<!--Ha ha ha I can now see your SOURCECODE I am a HACKER now!!!-->
<p title="Pls look at the source code yourself (￣ー￣)">And many other features!</p>