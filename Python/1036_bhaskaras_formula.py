"""
This module calculates the bhaskara.
"""

import math

def calculate_bhaskara() -> None:
    """
    Calculate the bhaskara.
    """
    a: float = float(input())
    b: float = float(input())
    c: float = float(input())

    delta: float = math.pow(b, 2) - 4 * (a * c)

    if ((a == 0) or (delta < 0)):
        print("Impossível calcular")
        return

    delta_positive: float = (-b + math.sqrt(delta)) / (2 * a)
    delta_negative = (-b - math.sqrt(delta)) / (2 * a)
    print(f"R1 = {delta_positive:.5f}")
    print(f"R2 = {delta_negative:.5f}")

calculate_bhaskara()
