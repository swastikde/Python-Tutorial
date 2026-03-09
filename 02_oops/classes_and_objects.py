# =============================================================
# Module 2: Classes and Objects in Python (OOP Basics)
# =============================================================
# Topics Covered:
#   - Defining a class
#   - __init__ constructor
#   - Instance attributes and methods
#   - Class attributes and class methods
#   - Static methods
#   - __str__ and __repr__ dunder methods
#   - Property decorator
# =============================================================

# ---------------------------------------------------------
# 1. Basic Class Definition
# ---------------------------------------------------------
print("=== Basic Class Definition ===")

class Dog:
    """Represents a dog with a name and breed."""

    # Class attribute — shared by all instances
    species = "Canis lupus familiaris"

    def __init__(self, name, breed, age):
        """Initialize a Dog instance."""
        # Instance attributes — unique to each instance
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        """Make the dog bark."""
        return f"{self.name} says: Woof!"

    def describe(self):
        """Return a description of the dog."""
        return f"{self.name} is a {self.age}-year-old {self.breed}."

    def __str__(self):
        """Readable string representation (for print())."""
        return f"Dog({self.name}, {self.breed}, age={self.age})"

    def __repr__(self):
        """Unambiguous string representation (for debugging)."""
        return f"Dog(name={self.name!r}, breed={self.breed!r}, age={self.age!r})"


# Creating instances
dog1 = Dog("Buddy", "Golden Retriever", 3)
dog2 = Dog("Max", "Bulldog", 5)

print(dog1)                   # calls __str__
print(repr(dog1))             # calls __repr__
print(dog1.bark())
print(dog2.describe())

# Accessing class attribute
print(f"\nSpecies: {Dog.species}")
print(f"Via instance: {dog1.species}")

# ---------------------------------------------------------
# 2. Class Methods and Static Methods
# ---------------------------------------------------------
print("\n=== Class Methods and Static Methods ===")

class Circle:
    """Represents a circle."""

    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Instance method — accesses self."""
        return Circle.pi * self.radius ** 2

    def circumference(self):
        return 2 * Circle.pi * self.radius

    @classmethod
    def from_diameter(cls, diameter):
        """Class method — alternative constructor using diameter."""
        return cls(diameter / 2)

    @staticmethod
    def is_valid_radius(r):
        """Static method — doesn't need self or cls."""
        return r > 0

    def __str__(self):
        return f"Circle(radius={self.radius})"


c1 = Circle(5)
print(f"{c1}: area={c1.area():.2f}, circumference={c1.circumference():.2f}")

c2 = Circle.from_diameter(10)   # class method constructor
print(f"Created from diameter 10: {c2}")

print(f"Is radius 5 valid? {Circle.is_valid_radius(5)}")
print(f"Is radius -3 valid? {Circle.is_valid_radius(-3)}")

# ---------------------------------------------------------
# 3. Property Decorator
# ---------------------------------------------------------
print("\n=== Property Decorator ===")

class Temperature:
    """Stores temperature in Celsius, exposes Fahrenheit as a property."""

    def __init__(self, celsius):
        self._celsius = celsius   # underscore = conventionally private

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible.")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Read-only computed property."""
        return self._celsius * 9 / 5 + 32

    def __str__(self):
        return f"{self._celsius}°C / {self.fahrenheit:.1f}°F"


t = Temperature(100)
print(f"Boiling point: {t}")

t.celsius = 0
print(f"Freezing point: {t}")

t.celsius = 37
print(f"Body temperature: {t}")

# ---------------------------------------------------------
# 4. Dunder Methods (Operator Overloading)
# ---------------------------------------------------------
print("\n=== Dunder Methods ===")

class Vector:
    """2D vector with operator overloading."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 3  = {v1 * 3}")
print(f"|v1|    = {v1.magnitude():.2f}")
print(f"v1 == v1: {v1 == v1}")
print(f"v1 == v2: {v1 == v2}")
