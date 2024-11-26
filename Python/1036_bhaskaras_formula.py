"""
This module calculates the bhaskara.
"""

import math as math

def calculate_average() -> None:
    """
    Calculate the bhaskara.
    """
    a: float = float(input())
    b: float = float(input())
    c: float = float(input())

    delta: float = math.pow(b, 2) - 4 * (a * c)
    
    R1: float = -b + math.sqrt(delta) / 2 * a
    R2: float = -b - math.sqrt(delta) / 2 * a
    print()

calculate_average()
