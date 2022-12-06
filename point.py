# point.py

"""
Simple class for points.
(C) Copyright 2023, Joe Chau.
All rights reserved.
"""


#  ██████╗  ██████╗ ██╗███╗   ██╗████████╗
#  ██╔══██╗██╔═══██╗██║████╗  ██║╚══██╔══╝
#  ██████╔╝██║   ██║██║██╔██╗ ██║   ██║
#  ██╔═══╝ ██║   ██║██║██║╚██╗██║   ██║
#  ██║     ╚██████╔╝██║██║ ╚████║   ██║
#  ╚═╝      ╚═════╝ ╚═╝╚═╝  ╚═══╝   ╚═╝


#  (C) Copyright 2022 Joe Chau.
#  All rights reserved.
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
#  associated documentation files (the "Software"), to deal in the Software without restriction,
#  including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do
#  so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all copies or substantial
#  portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
#  INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
#  PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
#  COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN
#  AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
#  WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
#  Except as contained in this notice, the name of Joe Chau shall not be used in advertising or
#  otherwise to promote the sale, use or other dealings in this Software without prior written
#  authorization from the Joe Chau.


from typing import *

__all__ = ["Point"]
__doc__ = "Simple class for points."

_NoneType = type(None)  # NoneType


class Point:
	"""
	A single point in a two-dimensional Cartesian coordinate system,
    aka rectangular coordinate system / orthogonal coordinate system.

    Both X-Coordinate and Y-Coordinate must be an integer ( `int` ).

    Support description text.

    :param int x: X-Coordinate
    :param int y: Y-Coordinate
    :param str description: Description text of the point, keyword-only argument.


    Usage:
    `Point(x= X-Coordinate, y= Y-Coordinate, description= Description-text)`
    """
	
	def __init__(self: 'Point', x: int, y: int, *, description: _NoneType | str = None) -> _NoneType:
		"""
        :param int x: X-Coordinate
        :param int y: Y-Coordinate
        :param str description: Description text of the point, keyword-only argument.
        """
		if type(x) is not int: raise TypeError("Coordinate must be an integer ( `int` )")
		if type(y) is not int: raise TypeError("Coordinate must be an integer ( `int` )")
		self._x = x
		self._y = y
		if description is None:
			self._description: _NoneType = None
		else:
			if type(description) is not str: raise TypeError("Description text must be a string ( `str` )")
			self._description: str = description
	
	@property
	def x(self):
		return self._x
	
	@property
	def y(self):
		return self._y
	
	@x.setter
	def x(self, x_coordinate):
		if type(x_coordinate) is not int: raise TypeError("Coordinate must be an integer ( `int` )")
		self._x = x_coordinate
	
	@y.setter
	def y(self, y_coordinate):
		if type(y_coordinate) is not int: raise TypeError("Coordinate must be an integer ( `int` )")
		self._y = y_coordinate
	
	@property
	def description(self) -> str:
		if self._description is None:
			return "No description."
		else:
			return self._description
	
	@description.setter
	def description(self, description_text: _NoneType | str):
		if description_text is None:
			self._description = None
		elif type(description_text) is str:
			self._description = description_text
		else:
			raise TypeError("Description text must be a string ( `str` )")
	
	def setToOrigin(self) -> 'Point':
		"""
        Set the coordinates to origin (0,0),
        where X-Axis and Y-Axis intersect.

        :return: Return itself
        """
		(self.x, self.y) = (0, 0)
		return self
	
	def __str__(self) -> str:
		return f"{self.x, self.y}"
	
	def __repr__(self) -> str:
		return f"{self.x, self.y}"
	
	def __eq__(self, other: 'Point') -> bool:
		if type(other) == Point:
			other: Point
			return self.x == other.x and self.y == other.y
		elif type(other) in (list, tuple):
			other: list | tuple
			if len(other) == 2:
				return self.x == other[0] and self.y == other[1]
			else:
				raise TypeError(f"Cannot compare with {type(other).__name__} that doesn't have a length of 2")
		elif type(other) is dict:
			other: dict
			if "x" in other.keys():
				if other["x"] != self.x:
					return False
			elif "X" in other.keys():
				if other["X"] != self.x:
					return False
			else:
				raise KeyError('Cannot find key `"x"` or `"X"` in the dictionary ( `dict` ) , '
				               'hence don\'t know X-Coordinate')
			if "y" in other.keys():
				return not other["y"] != self.y
			elif "Y" in other.keys():
				return not other["Y"] != self.y
			else:
				raise KeyError('Cannot find key `"y"` or `"Y"` in the dictionary ( `dict` ) , '
				               'hence don\'t know Y-Coordinate')
		else:
			raise TypeError(f"Cannot compare Point with {other.__class__.__name__}")
	
	def createOriginPoint() -> 'Point':
		# `self` argument OMITTED ON PURPOSE
		"""Create an origin point. Call this method from the class directly."""
		return Point(0, 0)
	
	def __ne__(self, other) -> bool:
		return not self == other
	
	def setCoordinate(self, x: int, y: int) -> _NoneType:
		"""
        :param int x: X-Coordinate
        :param int y: Y-Coordinate
        """
		self.x = x
		self.y = y
	
	setCoor: Callable[[int, int], None] = setCoordinate
	
	def printDescription(self):
		print(f"Point{self.x, self.y}: {self.description}")
	
	@property
	def isOnXAxis(self) -> bool:
		return not self.y != 0
	
	@property
	def isOnYAxis(self) -> bool:
		return not self.x != 0
	
	@property
	def isOrigin(self) -> bool:
		return self == (0, 0)
	
	@property
	def quadrant(self) -> _NoneType | int:
		if self.isOnXAxis or self.isOnYAxis or self.isOrigin:
			return None
		elif self.x > 0 and self.y > 0:
			return 1
		elif self.x > 0 > self.y:
			return 2
		elif self.x < 0 and self.y < 0:
			return 3
		else:
			return 4
	
	def distance(self, other: 'Point') -> int | float:
		answer: float = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
		if answer.is_integer():
			return int(answer)
		return answer

	@property
	def areaWithOrigin(self) -> int | float:
		return self.x * self.y
	
	@property
	def absoluteAreaWithOrigin(self) -> int | float:
		return abs(self.x * self.y)
	
	def angleFromSelf(self, other) -> int | float:
		from math import atan2, pi
		angle = atan2(self.y - other.y, self.x - other.x)
		if angle < 0:
			angle += 2 * pi
		result: float  # Angle in radian
		result: float = angle * 180 / pi  # Angle in degree
		if angle.is_integer(): angle = int(angle)
		return result


if __name__ == '__main__':
	print(Point(3,0).distance(Point(0,4)))
