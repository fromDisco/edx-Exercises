def calculator(num1, operator, num2):
    num1 = int(num1)
    num2 = int(num2)

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "/":
        result = num1 / num2
    elif operator == "*":
        result = num1 * num2
    else:
        result = "unknown operator"

    result = float(result)
    return round(result, 2)



def parser(input):
    return input.split(" ")


def main():
    user_input = input("Please enter the expression: ")
    num1, operator, num2 = parser(user_input)
    print(calculator(num1, operator, num2))


main()