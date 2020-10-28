import fractions


def addition(numbers):
    return sum(numbers)

def multiplication(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def decimal_to_fraction(decimal):
    return fractions.Fraction(decimal).limit_denominator()
