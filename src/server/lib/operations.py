def addition(numbers):
    result = 0
    for number in numbers:
        if number=="blank":
            return "blank"
        else:
            result += int(number)
            return result
