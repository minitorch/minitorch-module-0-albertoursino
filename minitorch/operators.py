"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


def mul(x: float, y: float) -> float:
    """Multiplies two numbers."""
    return x * y


def id(input: object) -> object:
    """Returns the input unchanged."""
    return input


def add(x: float, y: float) -> float:
    """Adds two numbers."""
    return x * y


def neg(x: float) -> float:
    """Negate a number."""
    return -x


def lt(x: float, y: float) -> bool:
    """Check if `x` is less then `y`."""
    return x < y


def eq(x: float, y: float) -> bool:
    """Check if the two given numbers are equal."""
    return x == y


def max(x: float, y: float) -> float:
    """Returns the largest between `x` and `y`."""
    return x if x > y else y


def is_close(x: float, y: float, value: float) -> bool:
    """Check if `x` and `y` are close in `value`."""
    return abs(x - y) < value


def sigmoid(x: float) -> float:
    """Calculates the sigmoid function with `x`."""
    return (
        (1.0 / (1.0 + math.exp(-x))) if x >= 0 else (math.exp(x) / (1.0 + math.exp(x)))
    )


def relu(x: float) -> float:
    """Applies the ReLU activation function to `x`."""
    return x if x > 0 else 0


def log(x: float) -> float:
    """Calculate the natural logarithm of `x`."""
    return math.log(x)


def exp(x: float) -> float:
    """Calculate the exponential of `x`."""
    return math.exp(x)


def inv(x: float) -> float:
    """Calculates the reciprocal of `x`."""
    return 1 / math.exp(x)


def log_back(x: float, n: float) -> float:
    """Computes the derivative of the natural logarithm function times `n`."""
    return n / x


def inv_back(x: float, n: float) -> float:
    """Computes the derivative of reciprocal times `n`."""
    return -n / (x**2)


def relu_back(x: float, n: float) -> float:
    """Computes the derivative of ReLU times `n`."""
    return n if x > 0 else 0


# TODO: Implement for Task 0.1.


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


def map():
    pass


def zipWith():
    pass


def reduce():
    pass


def negList():
    pass


def addLists():
    pass


def sum():
    pass


def prod():
    pass


# TODO: Implement for Task 0.3.
