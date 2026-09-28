def add(a, b):
    """Повертає суму двох чисел."""
    return a + b


def multiply(a, b):
    """Повертає добуток двох чисел."""
    return a * b


def greet(name):
    """Повертає привітання для користувача."""
    return f"Привіт, {name}!"


if __name__ == "__main__":
    print(greet("DevOps"))
    print("2 + 3 =", add(2, 3))