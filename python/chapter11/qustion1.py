# create a class (2-d vector) and use it to create another class representing a 3-D
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        return f"Vector2D({self.x}, {self.y})"

class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def display(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

# Creating 2D vector object
v2d = Vector2D(1, 2)
print(v2d.display())

# Creating 3D vector object
v3d = Vector3D(1, 2, 3)
print(v3d.display())
