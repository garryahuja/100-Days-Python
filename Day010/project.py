from art import logo
def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calc_dictionary = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}

# print(calc_dictionary["*"](4,8))
game_on = True
while game_on:
    print(logo)
    first_number = float(input("What's the first number?: "))
    for symbol in calc_dictionary:
        print(symbol)
    operator = input("Pick an operation: ")
    second_number = float(input("What's the next number?: "))

    result = float(calc_dictionary[operator](first_number, second_number))
    print (f"{first_number} {operator} {second_number} = {result}")
    continue_calc = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    new_result = 0
    while continue_calc == "y":
        for symbol in calc_dictionary:
            print(symbol)
        operator = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))
        new_result = float(calc_dictionary[operator](result, second_number))
        print(f"{result} {operator} {second_number} = {new_result}")
        result = new_result
        continue_calc = input(f"Type 'y' to continue calculating with {new_result}, or type 'n' to start a new calculation: ")






