

def fizz_buzz(num):

    """
        return 'Fizz', 'Buzz', 'FizzBuzz', or the argument it receives,
         all depending on the argument of the function,
         a number that is divisible by, 3, 5, or both 3 and 5, respectively.
    """

    if not isinstance(num, int):
        raise TypeError("Expected integer as input")

    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"

    return num

#  http://stackoverflow.com/a/14300802/3750565
