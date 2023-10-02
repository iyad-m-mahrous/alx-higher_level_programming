#!/usr/bin/python3
""" a function that prints a text with 2 new lines
after each of these characters: ., ? and :"""


def text_indentation(text):
    """text_indentation(text)

    Raises:
        TypeError: if text not string
    """

    if (not isinstance(text, str)):
        raise TypeError("text must be a string")
    new_text = "\n".join([y.strip() for y in text.splitlines()])
    new_text = ".".join([y.strip(" \t") for y in new_text.split(".")])
    new_text = ":".join([y.strip(" \t") for y in new_text.split(":")])
    new_text = "?".join([y.strip(" \t") for y in new_text.split("?")])
    new_text = new_text.replace(".", ".\n\n")
    new_text = new_text.replace(":", ":\n\n")
    new_text = new_text.replace("?", "?\n\n")
    print(new_text, end="")
