# override the __len__() method on vector of problem 5 to display the dimension of the vector
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        return 2

    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"

# Example usage
v2d = Vector2D(3, 4)
print(v2d)
print("Dimension of 2D vector:", len(v2d))
class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __len__(self):
        return 3

    def __str__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

# Example usage
v3d = Vector3D(1, 2, 3)
print(v3d)
print("Dimension of 3D vector:", len(v3d))
