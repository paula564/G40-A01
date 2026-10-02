#put everything under main 
#need to do testing for this

import sys

def is_sum_magic(value, magic_number):
    return sum(value) == magic_number

def is_valid_rows(rows, magic_number):
    for row in rows:
        if not is_sum_magic(row, magic_number):
            return False
    return True

def is_valid_columns(columns, magic_number):
    for column in columns:
        if not is_sum_magic(column, magic_number):
            return False
    return True

def is_valid_diagonals(diagonals, magic_number):
    for diagonal in diagonals:
        if not is_sum_magic(diagonal, magic_number):
            return False
    return True

def get_rows():
    rows = []
    first_row = input("Enter row 1 of the magic square: ")
    rows.append([int(x) for x in first_row.split()])
    number_of_rows = len(rows[0]) 
    for x in range(2, number_of_rows + 1):
        row = input(f"Enter row {x} of the magic square: ")
        rows.append([int(x) for x in row.split()])
    return rows

def is_valid_input(rows, number_of_rows):
    for row in rows:
        if len(row) != number_of_rows:
            print(f"Each row must have {number_of_rows} numbers.")
            return False

    range_list = sorted([int(number) for sublist in rows for number in sublist])

    if len(range_list) > number_of_rows ** 2  or len(range_list) < number_of_rows ** 2:
        print(f"The square must have {number_of_rows ** 2} numbers.")
        return False

    if any(number not in range(1, (number_of_rows ** 2) + 1 ) for number in range_list):
        print("The square does not respect the range constraint.")
        return False

    if len(range_list) != len(set(range_list)):
        print("The square cannot have duplicates.")
        return False
    
    return True

def get_columns(rows):
    #passes three separate lists into zip instead of one big list. matches the items based on index (index 0s with index 0s, etc.)
    return [list(column) for column in zip(*rows)]

def get_diagonals(rows, number_of_rows):
    main_diagonal = [rows[i][i] for i in range(number_of_rows)]
    anti_diagonal = [rows[i][number_of_rows - 1 - i] for i in range(number_of_rows)]
    return [main_diagonal, anti_diagonal]

def get_magic_number(number_of_rows):
    return (number_of_rows * (number_of_rows ** 2 + 1)) // 2

no_invalid_input = True


def main():
    rows = get_rows()
    number_of_rows = len(rows[0]) 
    if not is_valid_input(rows, number_of_rows):
            sys.exit(0)

    columns = get_columns(rows)
    diagonals = get_diagonals(rows, number_of_rows)

    MAGIC_NUMBER = get_magic_number(number_of_rows)
    if not is_valid_rows(rows, MAGIC_NUMBER) or not is_valid_columns(columns, MAGIC_NUMBER) or not is_valid_diagonals(diagonals, MAGIC_NUMBER):
        print(f"This is not a magic square. The sum of each row, column and diagonal is not {MAGIC_NUMBER}.")
    
    else:
        print(f"This is a magic square! The sum of each row, column and diagonal is {MAGIC_NUMBER}.")


if __name__ == "__main__":
    main()








   





