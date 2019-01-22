import math
class QuadraticEquation:
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c
	def discriminant(self):
		return ((self.b)**2) - (4 * self.a * self.c)
		
	def x1(self):
		if self.discriminant() < 0:
			istr = "imaginary"
			return istr
		else:
			return (-self.b + math.sqrt(self.discriminant()))
