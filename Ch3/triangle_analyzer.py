"""
Program: triangle_analyzer.py
Author: Kirill Redin
Description: 
	This program identifies triangle type
Inputs:
	sides (integer numbers)
Calculations: 
	Check if all summs of two sides are greater than a third side. If not, than it's not a triangle.
	If three of triangle sides are equal, it's and equilateral triangle. If two sides of triangle are equal,
	it's an esosceles triangle. If all sides are different, it's a scalene triangle. If sqaure of greater 
	side equals the summ of squares of two other sides, it's a right triangle.
Output:
	triangleType (string).
"""


class Triangle:
	"""docstring for Triangle"""
	def __init__(self, sides):
		self.sides = sides

	def get_triangle_type(self):
		triangleType = ''

		if self.sides[0] == self.sides[1] == self.sides[2]:
			return "It's an equilateral triangle."

		if self.sides[0] ** 2 + self.sides[1] ** 2 == self.sides[2] ** 2:
			triangleType += "It's a right triangle. "

		for i in range(2, -1, -1):
			if (self.sides[i] == self.sides[i-1]):
				return triangleType + "It's and isosceles triangle."

		return triangleType + "It's a scalene triangle."

		


def is_triangle(sides):
	return sides[0] + sides[1] > sides[2]

while True:
	sides = []

	try:
		for _ in range(3):
			sides.append(int(input("Enter triangle side length: ")))
	except ValueError:
		break

	sides.sort()
	if not is_triangle(sides):
		print("It's not a triangle", end='\n\n')
	else:
		triangle = Triangle(sides)
		triangleType = triangle.get_triangle_type()
		print(triangleType, end='\n\n')


