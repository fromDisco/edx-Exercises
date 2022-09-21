import re


def the_answer(wisdom):
    if check_for_wisdom(wisdom):
        return "Yes"
    else:
        return "No"


def check_for_wisdom(wisdom):
    # (?i) case insensitive match
    # \s matches whitespace character
    return re.fullmatch("(?i)\s*forty.two\s*|\s*42\s*", wisdom)


def main():
    user_input = input("Tell us: ")
    print(the_answer(user_input))


main()