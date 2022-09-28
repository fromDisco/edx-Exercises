import re

def main() -> str:
    """
    Ask user for input and manage dataflow

    Returns: 
        return of camel_to_snake (str)
    """

    user_input = input("give me camelCase: ")

    return camel_to_snake(user_input)


def camel_to_snake(word: str) -> str:
    """
    Split camelCase into list and change it back to snake_case

    Parameters:
        word (str): given input of user

    Returns:
        snake_case (str): converted string
    """

    # search for word that optionally starts with Capital letter.
    pattern = r"([A-Z]?[a-z]+)"
    split_word = re.findall(pattern, word)

    # join list with "_" as seperator
    snake_case = "_".join(split_word).lower()

    return snake_case
    

if __name__ == "__main__":
    print(main())