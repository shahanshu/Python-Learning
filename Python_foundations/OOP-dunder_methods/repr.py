class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"Vector({self.x}, {self.y}) - magnitude: {self.magnitude():.2f}"
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def magnitude(self):
        return (self.x**2 + self.y**2)**0.5

v = Vector(3, 4)
print(v)        # User-friendly with calculated magnitude
print(repr(v))  # Precise constructor representation