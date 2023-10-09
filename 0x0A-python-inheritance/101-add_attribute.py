#!/usr/bin/python3
"""a function that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj: The object to which the attribute will be added.
        attr_name: The name of the new attribute.
        attr_value: The value to assign to the new attribute.

    Raises:
        TypeError: If the object cannot have a new attribute.
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
