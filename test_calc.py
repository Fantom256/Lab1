from calc import add, factorial

def test_add():
    assert add(2, 3) == 2
    assert add(-1, 1) == 0

def test_factorial():
    assert factorial(5) == 120