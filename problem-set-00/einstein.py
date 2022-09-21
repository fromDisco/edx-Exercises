def calc_energy(mass):
    return mass * pow(300000000, 2)


def main():
    user_input = input("How many kilos do you want to accelerate: ")

    try:
        # check if user input is a valid integer
        mass = int(user_input)
    except:
        # if not, sorry.
        print("Sorry, no integer Value given.")
    else:
        print(calc_energy(mass))


main()
