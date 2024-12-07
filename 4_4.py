###
# Calculates the sum of the digits in a number
#


def sum_digits(number):
    total = 0
    abs_number = abs(number)
    string_num = str(abs_number)
    for i in string_num:
        total += int(i)
    return total


any_number = int(input('Enter a number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')
