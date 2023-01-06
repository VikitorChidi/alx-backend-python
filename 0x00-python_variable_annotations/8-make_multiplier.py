#!/usr/bin/env python3
"""A type-annotation of make_multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Return multiplies a float by multiplier."""
    return lambda x: x * multiplier


if __name__ == "__main__":
    print(make_multiplier.__annotations__)
    fun = make_multiplier(2.22)
    print("{}".format(fun(2.22)))
