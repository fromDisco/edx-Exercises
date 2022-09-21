def convert(string):
    faces = {":)": "🙂", ":(": "🙁"}
    # keep orignal Argument
    new_string = string
    # loop through dictionary with possible substitutions
    for face in faces:
        new_string = new_string.replace(face, faces[face])

    return new_string


def main():
    user_input = input("Wanna see me make a happy or a sad face?: ")
    print(convert(user_input))


main()
