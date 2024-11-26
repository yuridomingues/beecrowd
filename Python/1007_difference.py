"""
This module calculates the difference of four numbers.
"""

def calculate_average() -> None:
    """
    Calculate the difference of four numbers and print the result.
    """
    a: int = int(input())
    b: int = int(input())
    c: int = int(input())
    d: int = int(input())

    difference = (a * b - c * d)
    print("DIFERENCA =", difference)

calculate_average()