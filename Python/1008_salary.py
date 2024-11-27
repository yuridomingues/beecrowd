"""Write a program that reads an employee's number, 
his/her worked hours number in a month and the amount he received per hour. 
Print the employee's number and salary that he/she will receive at end of the month, 
with two decimal places."""

def salary_calculator() -> None:

    """This function will calculate the employee salary"""
    employee_number: int = int(input())
    worked_hours: int = int(input())
    amount_per_hour: float = float(input())

    salary = worked_hours * amount_per_hour
    print(f"NUMBER = {employee_number}")
    print(f"SALARY = U$ {salary:.2f}")

salary_calculator()
