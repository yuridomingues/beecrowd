"""
This module calculates the average of three numbers.
"""

def calculate_average() -> None:
    """
    Calculate the average of three numbers and print the result.
    """
    a: float = float(input())
    b: float = float(input())
    c: float = float(input())

    averaged_number: float = (a * 2 + b * 3 + c * 5) / (2 + 3 + 5)

    formatted_average = f"{averaged_number:.1f}"
    print("MEDIA =", formatted_average)


calculate_average()
