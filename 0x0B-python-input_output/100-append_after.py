#!/usr/bin/python3
""" a function that inserts a line of text to a file,
after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """def append_after(filename="", search_string="", new_string="")"""

    try:
        with open(filename, "r+", encoding='UTF-8') as f:
            lines = f.readlines()
            f.seek(0)
            for line in lines:
                f.write(line)
                if search_string in line:
                    f.write(new_string)
            f.truncate()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
