import re

def mime_check(file_name, mime_dict):
    try:
        extension = file_name.strip().split(".")[-1].lower()
        # if extension is not valid -> KeyError
        mime_type = mime_dict[extension]
    except KeyError:
        return "application/octet-stream"
    else:
        return mime_type


def main(mime_dict):
    user_input = input("Enter Filename: ")
    print(mime_check(user_input, mime_dict))


# dictionary is easily extensible, and keeps the function small
mime_dict = {
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "gif": "image/gif",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip",
    }

main(mime_dict)