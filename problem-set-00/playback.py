# Convert the string/sentence and substitute spaces with ...
def substitute_chars(string, please_replace, replace_with):
    print(string.replace(please_replace, replace_with))


user_input = input("Please type something long and boring: ")
substitute_chars(user_input, " ", "...")
