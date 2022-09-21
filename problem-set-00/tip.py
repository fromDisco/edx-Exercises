import re

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollar_string):
    # match only digits.
    # group() returns the match, because otherwise match object is result
    cleaned_dollar = re.search("\d+", dollar_string).group()
    return float(cleaned_dollar)



def percent_to_float(percent_string):
    # match only digits.
    # group() returns the match, because otherwise match object is result
    cleaned_percent = re.search("\d+", percent_string).group()
    # devide by 100 to get the percentage,
    return float(cleaned_percent) / 100


main()