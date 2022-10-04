from math_series.math_script import fibonacci, lucas, sum_series

###### Test Fibonacci Cases ######
def test_non_number():
    assert fibonacci("") == "You have to insert integer number"

def test_fibonacci_zero():
    assert fibonacci(0) == 0

def test_fibonacci_one():
    assert fibonacci(1) == 1

def test_fibonacci_two():
    assert fibonacci(2) ==1

def test_fibonacci_three():
    assert fibonacci(3) ==2

def test_fibonacci_four():
    assert fibonacci(4) ==3

def test_fibonacci_five():
    assert fibonacci(5) ==5

def test_fibonacci_six():
    assert fibonacci(6) ==8

def test_seven():
    assert fibonacci(7) ==13

###### Test Lucas Cases ######
def test_lucas_non_number():
    assert lucas("") == "You have to insert integer number"

def test_lucas_zero():
    assert lucas(0) == 2

def test_lucas_one():
    assert lucas(1) == 1

def test_lucas_two():
    assert lucas(2) == 3

def test_lucas_three():
    assert lucas(3) == 4

def test_lucas_four():
    assert lucas(4) == 7

def test_lucas_five():
    assert lucas(5) == 11

def test_lucas_six():
    assert lucas(6) == 18

def test_lucas_seven():
    assert lucas(7) == 29

###### Test sum_series Cases ######
def test_fibonacci():
    assert sum_series(7) == 13

def test_lucas():
    assert sum_series(7,2,1) == 29