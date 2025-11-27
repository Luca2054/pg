class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def __add__(self, other): #other je ta druhá veličina co se přičítá 
    x = self.x + other.x
    y = self.y + other.y
    return Vector(x, y)
def __mul__(self, scalar): #scalar je ta číslice co se násobí
    x = self.x * scalar
    y = self.y * scalar
    return Vector(x, y)

def __str__(self):
        return f"Vector({self.x}, {self.y})"

if __name__ == "__main__":
    v1 = Vector(2, 3)
    print(v1)
    v2 = Vector(3, 4)
    print(v1)

    v3 = v1 + v2
    print(v3)

    v4 = v1 * 3
    print(v4)