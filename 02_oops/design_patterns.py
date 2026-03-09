# =============================================================
# Module 2: Design Patterns in Python
# =============================================================
# Topics Covered:
#   - Singleton Pattern
#   - Factory Pattern
#   - Observer Pattern
#   - Strategy Pattern
#   - Decorator Pattern
# =============================================================

# ---------------------------------------------------------
# 1. Singleton Pattern
# ---------------------------------------------------------
# Ensures a class has only one instance.

print("=== Singleton Pattern ===")

class DatabaseConnection:
    """Singleton: only one database connection exists at a time."""

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._connected = False
        return cls._instance

    def connect(self, host):
        self._host = host
        self._connected = True
        print(f"  Connected to {host}")

    def __str__(self):
        status = f"connected to {self._host}" if self._connected else "disconnected"
        return f"DatabaseConnection ({status})"


db1 = DatabaseConnection()
db2 = DatabaseConnection()

db1.connect("localhost:5432")
print(f"db1: {db1}")
print(f"db2: {db2}")
print(f"db1 is db2: {db1 is db2}")   # True — same instance

# ---------------------------------------------------------
# 2. Factory Pattern
# ---------------------------------------------------------
# Creates objects without specifying the exact class.

print("\n=== Factory Pattern ===")

class Notification:
    def send(self, message):
        raise NotImplementedError


class EmailNotification(Notification):
    def __init__(self, email):
        self.email = email

    def send(self, message):
        return f"[Email → {self.email}] {message}"


class SMSNotification(Notification):
    def __init__(self, phone):
        self.phone = phone

    def send(self, message):
        return f"[SMS → {self.phone}] {message}"


class PushNotification(Notification):
    def __init__(self, device_id):
        self.device_id = device_id

    def send(self, message):
        return f"[Push → {self.device_id}] {message}"


class NotificationFactory:
    """Factory that creates the correct Notification subclass."""

    _registry = {
        "email": EmailNotification,
        "sms": SMSNotification,
        "push": PushNotification,
    }

    @classmethod
    def create(cls, channel, target):
        klass = cls._registry.get(channel.lower())
        if not klass:
            raise ValueError(f"Unknown channel: {channel!r}")
        return klass(target)


n1 = NotificationFactory.create("email", "alice@example.com")
n2 = NotificationFactory.create("sms", "+1-555-1234")
n3 = NotificationFactory.create("push", "device-abc123")

for n in [n1, n2, n3]:
    print(f"  {n.send('Hello!')}")

# ---------------------------------------------------------
# 3. Observer Pattern
# ---------------------------------------------------------
# Allows objects (observers) to subscribe to events.

print("\n=== Observer Pattern ===")

class EventEmitter:
    """Subject that notifies registered observers on events."""

    def __init__(self):
        self._listeners = {}

    def on(self, event, callback):
        """Register a callback for an event."""
        self._listeners.setdefault(event, []).append(callback)

    def emit(self, event, *args, **kwargs):
        """Trigger all callbacks registered for an event."""
        for callback in self._listeners.get(event, []):
            callback(*args, **kwargs)


class StockMarket(EventEmitter):
    def __init__(self):
        super().__init__()
        self._prices = {}

    def update_price(self, symbol, price):
        old = self._prices.get(symbol, 0)
        self._prices[symbol] = price
        change = price - old
        self.emit("price_change", symbol=symbol, price=price, change=change)


market = StockMarket()

# Subscribe observers
market.on("price_change",
          lambda **kw: print(f"  [Trader]  {kw['symbol']}: ${kw['price']:.2f} "
                             f"({'▲' if kw['change'] >= 0 else '▼'}{abs(kw['change']):.2f})"))
market.on("price_change",
          lambda **kw: print(f"  [Logger]  Recorded: {kw['symbol']} = {kw['price']}"))

market.update_price("AAPL", 150.00)
market.update_price("AAPL", 153.50)
market.update_price("GOOG", 2800.00)

# ---------------------------------------------------------
# 4. Strategy Pattern
# ---------------------------------------------------------
# Define a family of algorithms, encapsulate each, and make
# them interchangeable.

print("\n=== Strategy Pattern ===")

class SortStrategy:
    def sort(self, data):
        raise NotImplementedError


class BubbleSortStrategy(SortStrategy):
    def sort(self, data):
        arr = data[:]
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


class MergeSortStrategy(SortStrategy):
    def sort(self, data):
        if len(data) <= 1:
            return data[:]
        mid = len(data) // 2
        left = self.sort(data[:mid])
        right = self.sort(data[mid:])
        return self._merge(left, right)

    def _merge(self, left, right):
        result, i, j = [], 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i]); i += 1
            else:
                result.append(right[j]); j += 1
        return result + left[i:] + right[j:]


class Sorter:
    """Context: uses a pluggable sort strategy."""

    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy

    def sort(self, data):
        return self._strategy.sort(data)


data = [64, 25, 12, 22, 11]
sorter = Sorter(BubbleSortStrategy())
print(f"  Bubble sort: {sorter.sort(data)}")

sorter.set_strategy(MergeSortStrategy())
print(f"  Merge sort:  {sorter.sort(data)}")

# ---------------------------------------------------------
# 5. Decorator Pattern (using functools.wraps)
# ---------------------------------------------------------
print("\n=== Decorator Pattern ===")

import time
import functools

def timer(func):
    """Decorator: measure and print execution time."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  {func.__name__} took {elapsed:.6f}s")
        return result
    return wrapper

def retry(times=3):
    """Decorator factory: retry on exception up to 'times' attempts."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"  Attempt {attempt} failed: {e}")
            print(f"  All {times} attempts failed.")
            return None
        return wrapper
    return decorator


@timer
def compute_sum(n):
    return sum(range(n))

result = compute_sum(1_000_000)
print(f"  Sum: {result}")

attempt_count = 0

@retry(times=3)
def flaky_operation():
    """Simulates an operation that fails twice then succeeds."""
    global attempt_count
    attempt_count += 1
    if attempt_count < 3:
        raise ConnectionError("Network timeout")
    return "Success!"

attempt_count = 0
result = flaky_operation()
print(f"  flaky_operation result: {result}")
