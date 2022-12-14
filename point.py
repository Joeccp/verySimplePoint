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

__author__ = "Joe Chau"
__copyright__ = "(C) Copyright 2022 Joe Chau"
__email__ = "lmcs121005@gmail.com"

_NoneType = type(None)  # NoneType


class Point:
	"""
	A single point in a two-dimensional Cartesian coordinate system,
    aka rectangular coordinate system / orthogonal coordinate system.

    Both X-Coordinate and Y-Coordinate must be an integer ( `int` ).

    :param int x: X-Coordinate
    :param int y: Y-Coordinate


    Usage:
    `Point(x= X-Coordinate, y= Y-Coordinate)`
    """
	
	def __init__(self: 'Point', x: int, y: int) -> _NoneType:
		"""
        :param int x: X-Coordinate
        :param int y: Y-Coordinate
        """
		if type(x) is not int: raise TypeError("Coordinate must be an integer ( `int` )")
		if type(y) is not int: raise TypeError("Coordinate must be an integer ( `int` )")
		self._x = x
		self._y = y
	
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
		# https://stackoverflow.com/questions/74682389/find-angle-in-degrees-of-a-point-from-another-point
		# Credits to OM222O https://stackoverflow.com/users/7121783/om222o
		# Also thanks to Tim Roberts https://stackoverflow.com/users/1883316/tim-roberts
		from math import atan2, pi
		angle = atan2(self.y - other.y, self.x - other.x)
		if angle < 0:
			angle += 2 * pi
		result: float  # Angle in radian
		result: float = angle * 180 / pi  # Angle in degree
		if result.is_integer():
			result = int(result)
		else:
			result = round(result, 3)
		return result
	
	def __bool__(self) -> bool:
		"""True if not an origin"""
		return self != (0, 0)
	
	def __abs__(self) -> 'Point':
		return Point(abs(self.x), abs(self.y))
	
	def turnAbsolute(self) -> _NoneType:
		self.x = abs(self.x)
		self.y = abs(self.y)
	
	def __complex__(self) -> complex:
		return complex(self.x, self.y)
	
	def __len__(self) -> int:
		"""Return the value of X-Coordinate"""
		return self.x
	
	def __getitem__(self, item) -> int:
		if item in ('x', 'X'):
			return self.x
		elif item in ('y', 'Y'):
			return self.y
		else:
			raise KeyError(f"Point has no such key: {item}")
	
	def __setitem__(self, key, value) -> None:
		if value in ('x', 'X'):
			self.x = value
		elif value in ('y', 'Y'):
			self.y = value
		else:
			raise KeyError(f"Point has no such key: {key}")
	
	def __reversed__(self) -> 'Point':
		return Point(self.y, self.x)
	
	def reverse(self) -> None:
		(self.x, self.y) = (self.y, self.x)
	
	def __iter__(self):
		yield self.x
		yield self.y
	
	def __contains__(self, item) -> bool:
		return item in (self.x, self.y)


if __name__ == '__main__':
	pass
