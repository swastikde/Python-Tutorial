# =============================================================
# Module 2: Inheritance in Python
# =============================================================
# Topics Covered:
#   - Single inheritance
#   - Method overriding
#   - super()
#   - Multi-level inheritance
#   - Multiple inheritance and MRO (Method Resolution Order)
#   - Abstract base classes (ABC)
# =============================================================

from abc import ABC, abstractmethod

# ---------------------------------------------------------
# 1. Single Inheritance
# ---------------------------------------------------------
print("=== Single Inheritance ===")

class Animal:
    """Base class for all animals."""

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}!"

    def breathe(self):
        return f"{self.name} is breathing."

    def __str__(self):
        return f"Animal({self.name})"


class Dog(Animal):
    """Dog extends Animal with dog-specific behaviour."""

    def __init__(self, name, breed):
        super().__init__(name, "Woof")   # call parent __init__
        self.breed = breed

    def fetch(self, item="ball"):
        return f"{self.name} fetches the {item}!"

    def __str__(self):
        return f"Dog({self.name}, {self.breed})"


class Cat(Animal):
    """Cat extends Animal with cat-specific behaviour."""

    def __init__(self, name, indoor=True):
        super().__init__(name, "Meow")
        self.indoor = indoor

    def purr(self):
        return f"{self.name} purrs contentedly."

    def __str__(self):
        loc = "indoor" if self.indoor else "outdoor"
        return f"Cat({self.name}, {loc})"


d = Dog("Rex", "Labrador")
c = Cat("Whiskers")

print(d)
print(d.speak())        # inherited from Animal
print(d.fetch())        # Dog-specific
print(d.breathe())      # inherited

print()
print(c)
print(c.speak())        # inherited
print(c.purr())         # Cat-specific

# isinstance / issubclass checks
print(f"\nisinstance Dog is Animal: {isinstance(d, Animal)}")
print(f"issubclass Dog of Animal: {issubclass(Dog, Animal)}")

# ---------------------------------------------------------
# 2. Method Overriding
# ---------------------------------------------------------
print("\n=== Method Overriding ===")

class Shape:
    def area(self):
        return 0

    def describe(self):
        return f"I am a {self.__class__.__name__} with area {self.area():.2f}"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):         # override
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):         # override
        return 0.5 * self.base * self.height


shapes = [Shape(), Rectangle(4, 5), Triangle(6, 3)]
for s in shapes:
    print(f"  {s.describe()}")

# ---------------------------------------------------------
# 3. Multi-level Inheritance
# ---------------------------------------------------------
print("\n=== Multi-level Inheritance ===")

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        return f"{self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, doors=4):
        super().__init__(make, model)
        self.doors = doors

    def info(self):
        return f"{super().info()} ({self.doors}-door car)"


class ElectricCar(Car):
    def __init__(self, make, model, battery_kwh):
        super().__init__(make, model)
        self.battery_kwh = battery_kwh

    def info(self):
        return f"{super().info()} [Electric, {self.battery_kwh} kWh]"


ec = ElectricCar("Tesla", "Model 3", 75)
print(ec.info())

# ---------------------------------------------------------
# 4. Multiple Inheritance and MRO
# ---------------------------------------------------------
print("\n=== Multiple Inheritance and MRO ===")

class Flyable:
    def move(self):
        return "flying"

    def describe(self):
        return "I can fly"


class Swimmable:
    def move(self):
        return "swimming"

    def describe(self):
        return "I can swim"


class Duck(Flyable, Swimmable):
    """Duck can both fly and swim."""

    def describe(self):
        # super() follows MRO: Duck → Flyable → Swimmable
        return f"I am a duck. {super().describe()} and {Swimmable.describe(self)}"


duck = Duck()
print(f"Duck moves by: {duck.move()}")   # Flyable wins (listed first)
print(duck.describe())

# Inspect MRO
print(f"\nMRO for Duck: {[cls.__name__ for cls in Duck.__mro__]}")

# ---------------------------------------------------------
# 5. Abstract Base Classes
# ---------------------------------------------------------
print("\n=== Abstract Base Classes ===")

class PaymentProcessor(ABC):
    """Abstract base class — defines interface for payment processors."""

    @abstractmethod
    def process_payment(self, amount):
        """Process a payment of the given amount."""
        pass

    @abstractmethod
    def refund(self, amount):
        """Refund a payment."""
        pass

    def log(self, message):
        """Concrete method shared by all subclasses."""
        print(f"  [LOG] {message}")


class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        self.log(f"Credit card charged: ${amount:.2f}")
        return True

    def refund(self, amount):
        self.log(f"Credit card refunded: ${amount:.2f}")
        return True


class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        self.log(f"PayPal payment sent: ${amount:.2f}")
        return True

    def refund(self, amount):
        self.log(f"PayPal refund issued: ${amount:.2f}")
        return True


processors = [CreditCardProcessor(), PayPalProcessor()]
for processor in processors:
    print(f"\n{processor.__class__.__name__}:")
    processor.process_payment(99.99)
    processor.refund(99.99)

# Cannot instantiate abstract class
try:
    p = PaymentProcessor()
except TypeError as e:
    print(f"\nCannot instantiate abstract class: {e}")
