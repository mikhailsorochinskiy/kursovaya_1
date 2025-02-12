from src.decorators import decorator


def test_decorator():
    @decorator
    def add_num(a, b):
        return a + b

    result = add_num(1, 3)
    assert result == "4"


def test_divide():
    @decorator
    def divide(a, b):
        return a / b

    result = divide(3, 0)
    assert result == "divide error: ZeroDivisionError. Inputs: (3, 0), {}"
