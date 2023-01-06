#!/usr/bin/env python3
""" A type-annotated function concat."""


def concat(str1: str, str2: str) -> str:
    """ Returns the concatenation of two strings."""
    return "{} {}".format(str1, str2)


# if __name__ == "__main__":
#     print(concat("Hello", "World"))
#     print(concat.__annotations__)
