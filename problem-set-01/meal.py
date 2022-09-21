import re


def main(meal_times: dict) -> None:
    """
    manage dataflow to check if given time is mealtime:

    Parameters:
        meal_times (dict): contains mealtimes with corresponding meals
                           e.g. {"700-800": "breakfast"}

    Returns:
        none: functions prints the results
    """

    user_input = input("Is it Mealtime? Enter like follows (6:30 p.m. or 18:30)\n")

    # remove the ":" so that time is not 7:30 but 730
    # so its easy to convert it to an int
    reduced_time = user_input.replace(":", "")

    # convert the string to an int
    converted = convert(reduced_time)

    is_mealtime = meal_time(converted, meal_times)

    # if user_time isnt found in mealtimes_dict meal_time() returns none
    return f"{is_mealtime} time" if is_mealtime else ""


def convert(time: str) -> int:
    """
    Convert the time to an integer, if time is p.m. add 12 hours -> + 1200

    Parameters:
        time (str): user input string, but already without ":"

    Returns:
        converted time (int)
    """

    # return 1 or 2 groups.
    # group1 "time" returns hours
    # group2 "twelve" if existent returns time format
    pattern = r"(?P<time>[0-9]{3,4}) ?(?P<twelve>[ap]\.m.)?"
    match_object = re.search(pattern, time)

    # transform hours into integer
    hours = int(match_object.group("time"))

    try:
        # if there is an english 12-hour format present
        is_twelve = match_object.group("twelve")
        if is_twelve == "p.m.":
            # and its p.m. add 12 hours
            hours = hours + 1200
    except AttributeError:
        pass
    finally:
        return hours


def meal_time(act_hour: int, mealtime_list: dict) -> str:
    """
    check if time, given by user, is found in the mealtime_list
    if so, return the corresponding meal

    Parameters:
        act_hour (int): converted time, given by user
        mealtime_list jdict): contains mealtimes with corresponding meals
                           e.g. {"700-800": "breakfast"}

    Returns:
        mealtime name (str)
    """

    for mealtime in mealtime_list.keys():
        mealtime_split = mealtime.split("-")
        # compare the act_hour to the dict keys
        if int(mealtime_split[0]) <= act_hour <= int(mealtime_split[1]):
            # if there is a match, return the value of the matching key
            return mealtime_list[mealtime]


if __name__ == "__main__":
    meal_times = {"700-800": "breakfast",
                  "1200-1300": "lunch",
                  "1800-1900": "dinner"
                  }

    print(main(meal_times))
