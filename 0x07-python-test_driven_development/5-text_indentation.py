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
    new_text = text.strip()
    new_text = "\n\n".join([i.strip() for i in new_text.split(".")])
    new_text = "\n\n".join([i.strip() for i in new_text.split(":")])
    new_text = "\n\n".join([i.strip() for i in new_text.split("?")])
    print(new_text, end="")
