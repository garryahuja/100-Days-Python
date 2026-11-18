def odd_or_even(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

print(odd_or_even(10))

def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(leap_year(2027))


def fizz_buzz(num):
    for number in range(1, num + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


fizz_buzz(15)