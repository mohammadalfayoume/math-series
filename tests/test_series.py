from math_series.math_script import fibonacci

def test_non_number():
    assert fibonacci("") == "You have to insert integer number"

def test_zero():
    assert fibonacci(0) == 0

def test_one():
    assert fibonacci(1) == 1

def test_two():
    assert fibonacci(2) ==1

def test_three():
    assert fibonacci(3) ==2

def test_four():
    assert fibonacci(4) ==3

def test_five():
    assert fibonacci(5) ==5

def test_six():
    assert fibonacci(6) ==8

def test_seven():
    assert fibonacci(7) ==13