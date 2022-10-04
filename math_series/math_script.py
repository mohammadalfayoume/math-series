def fibonacci(n):
    if type(n) != int:
        return "You have to insert integer number"
    if n == 0 or n == 1:
        return n
    num1 = 0
    num2 = 1
    sum = 0
    for x in range(2, n+1):
        sum = num1 + num2
        num1 = num2
        num2 = sum
    return sum

def lucas(n):
    if type(n) != int:
        return "You have to insert integer number"
    if n == 0:
        return 2
    if n == 1:
        return n
    num1 = 2
    num2 = 1
    sum = 0
    for x in range(2, n+1):
        sum = num1 + num2
        num1 = num2
        num2 = sum
    return sum