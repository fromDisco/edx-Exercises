import re


def hello_or_not(greeting):
    # sorry but these tasks screem for regEx
    # (?<![a-z0-9]\s) no preceding word
    # (?P<groupname>) named group, can be called with match.group("groupname")
    # (?:) non capturing group
    # (?:ello)? ? matches (?:ello) between 0 and 1 times -> optional
    pattern = r"(?<![a-z0-9]\s)(?P<word>\bh(?:ello)?)"
    # re.IGNORECASE pattern is case insensitive
    is_greeting = re.search(pattern, greeting, re.IGNORECASE)

    # is_greeting is a "match object" or "None"
    if is_greeting:
        # return "$20" if len(is_greeting.group("word")) == 1 else "S0"
        if len(is_greeting.group("word")) == 5:
            return "$0"
        else:
            return "$20"
    else:
        return "$100"


def main():
    user_input = input("Do you want to be friendly? ")
    print(hello_or_not(user_input))


main()
