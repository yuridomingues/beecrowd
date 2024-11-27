def averageNumber() -> None:
    A: float = float(input("Enter grade A: "))
    B: float = float(input("Enter grade B: "))

    A = A * 3.5
    B = B * 7.5

    average = (A + B) / (3.5 + 7.5)

    formatted_average = "{:.5f}".format(average)
    print("MEDIA =", formatted_average)

averageNumber()