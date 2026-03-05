# =============================================================
# Module 2: Polymorphism in Python
# =============================================================
# Topics Covered:
#   - Duck typing
#   - Method overriding (runtime polymorphism)
#   - Operator overloading (__add__, __len__, etc.)
#   - Function/method polymorphism
#   - Polymorphism with abstract classes
# =============================================================

from abc import ABC, abstractmethod
import math

# ---------------------------------------------------------
# 1. Duck Typing
# ---------------------------------------------------------
# "If it walks like a duck and quacks like a duck, it's a duck."
# Python doesn't care about the type of an object, only whether
# it has the required method or attribute.

print("=== Duck Typing ===")

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Robot:
    def speak(self):
        return "Beep boop."

def make_it_speak(entity):
    """Works on any object that has a speak() method."""
    print(f"  {entity.__class__.__name__}: {entity.speak()}")

for obj in [Dog(), Cat(), Robot()]:
    make_it_speak(obj)

# ---------------------------------------------------------
# 2. Method Overriding (Runtime Polymorphism)
# ---------------------------------------------------------
print("\n=== Method Overriding ===")

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        # Calls the overridden area/perimeter in the subclass
        return (f"{self.__class__.__name__}: "
                f"area={self.area():.2f}, perimeter={self.perimeter():.2f}")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def area(self):
        s = (self.a + self.b + self.c) / 2   # semi-perimeter
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5)]
for shape in shapes:
    print(f"  {shape.describe()}")

# Polymorphic function
def total_area(shapes):
    return sum(s.area() for s in shapes)

print(f"\nTotal area of all shapes: {total_area(shapes):.2f}")

# ---------------------------------------------------------
# 3. Operator Overloading
# ---------------------------------------------------------
print("\n=== Operator Overloading ===")

class Fraction:
    """Represents a mathematical fraction p/q."""

    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        gcd = math.gcd(abs(numerator), abs(denominator))
        sign = -1 if denominator < 0 else 1
        self.num = sign * numerator // gcd
        self.den = sign * denominator // gcd

    def __add__(self, other):
        return Fraction(
            self.num * other.den + other.num * self.den,
            self.den * other.den
        )

    def __sub__(self, other):
        return Fraction(
            self.num * other.den - other.num * self.den,
            self.den * other.den
        )

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other):
        return Fraction(self.num * other.den, self.den * other.num)

    def __eq__(self, other):
        return self.num == other.num and self.den == other.den

    def __lt__(self, other):
        return self.num * other.den < other.num * self.den

    def __str__(self):
        if self.den == 1:
            return str(self.num)
        return f"{self.num}/{self.den}"

    def __repr__(self):
        return f"Fraction({self.num}, {self.den})"


a = Fraction(1, 2)
b = Fraction(1, 3)

print(f"a = {a}, b = {b}")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a == b: {a == b}")
print(f"a < b:  {a < b}")
print(f"b < a:  {b < a}")

# Sorting using __lt__
fractions = [Fraction(3, 4), Fraction(1, 2), Fraction(2, 3)]
print(f"\nSorted fractions: {sorted(fractions)}")

# ---------------------------------------------------------
# 4. len() and iteration via __len__ / __iter__
# ---------------------------------------------------------
print("\n=== __len__ and __iter__ ===")

class Playlist:
    """A music playlist that behaves like a sequence."""

    def __init__(self, name):
        self.name = name
        self._songs = []

    def add(self, song):
        self._songs.append(song)

    def __len__(self):
        return len(self._songs)

    def __iter__(self):
        return iter(self._songs)

    def __getitem__(self, index):
        return self._songs[index]

    def __str__(self):
        return f"Playlist '{self.name}' ({len(self)} songs)"


pl = Playlist("Chill Vibes")
for song in ["Song A", "Song B", "Song C", "Song D"]:
    pl.add(song)

print(pl)
print(f"Number of songs: {len(pl)}")
print("Songs:")
for song in pl:
    print(f"  - {song}")
print(f"First song: {pl[0]}")
