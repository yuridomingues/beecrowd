"""
This module calculates the bhaskara.
"""

import math

def calculate_bhaskara() -> None:
    """
    Calculate the bhaskara.
    """
    float_numbers: str = str(input())
    numbers = float_numbers.split(" ")

    a = float(numbers[0])
    b = float(numbers[1])
    c = float(numbers[2])

    delta: float = math.pow(b, 2) - 4 * (a * c)

    if ((a == 0) or (delta < 0)):
        print("Impossível calcular")
        return

    raiz_one: float = (-b + math.sqrt(delta)) / (2 * a)
    raiz_two = (-b - math.sqrt(delta)) / (2 * a)
    print(f"R1 = {raiz_one:.5f}")
    print(f"R2 = {raiz_two:.5f}")

calculate_bhaskara()
