import sys

class Sphere:
	Pi = 3.14

	def __init__(self, radius):
		self.radius = radius
		# self.PI = 3.14

	def get_surface_area(self):
		return 4*self.Pi*self.radius**2

	def get_volume(self):
		return 4/3*self.Pi*self.radius**3

	def set_radius(self, x):
		self.radius = x

n=Sphere(int(sys.argv[1]))
print(n.get_surface_area())
print(n.get_volume())
n.set_radius(int(sys.argv[1])*2)
print(n.get_surface_area())
print(n.get_volume())