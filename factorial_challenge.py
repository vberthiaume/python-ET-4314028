def factorial(num):
    if not isinstance(num, int) or num < 0:
        return None
    elif num < 2:
        return 1
    else:
        return num * factorial(num-1)

def factorialNonRecursive(num):
    if not isinstance(num, int) or num < 0:
        return None

    fact = 1
    counter = 1
    while (counter <= num):
        fact *= counter
        counter += 1

    return fact