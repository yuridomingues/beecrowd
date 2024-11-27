#Read two integer values, in this case, the variables A and B. After this, calculate the sum between them and assign it to the variable SOMA. Write the value of this variable.
def main () -> None: 
    a = int(input())
    b = int(input())

    SOMA = a + b

    print(f'SOMA = {SOMA}')


if __name__ == '__main__':
    main()