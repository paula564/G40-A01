
def is_sum_magic(value, magic_number):
    return sum(value) == magic_number

def is_valid_rows(rows, magic_number):
    for row in rows:
        if not is_sum_magic(row, MAGIC_NUMBER):
            return False
    return True

def is_valid_columns(columns, magic_number):
    for column in columns:
        if not is_sum_magic(column, MAGIC_NUMBER):
            return False
    return True


rows = []


first_row = input("Enter row 1 of the magic square: ")

rows.append([int(x) for x in first_row.split()])

number_of_rows = len(rows[0]) 


MAGIC_NUMBER = (number_of_rows * (number_of_rows ** 2 + 1)) / 2

for x in range(2, number_of_rows + 1):
    row = input(f"Enter row {x} of the magic square: ")
    rows.append([int(x) for x in row.split()])

range_list = sorted([number for sublist in rows for number in sublist])
#passes three separate lists into zip instead of one big list. matches the items based on index (index 0s with index 0s, etc.)
columns = [list(column) for column in zip(*rows)]

if len(range_list) > number_of_rows ** 2  or len(range_list) < number_of_rows ** 2:
     print(f"The square must have {number_of_rows ** 2} numbers.")

if any(number not in range(1, (number_of_rows ** 2) + 1 ) for number in range_list):
    print("The square does not respect the range constraint.")

if len(range_list) != len(set(range_list)):
    print("The square cannot have duplicates.")

if not is_valid_rows(rows, MAGIC_NUMBER) and not is_valid_columns(columns, MAGIC_NUMBER):
    print(f"The magic square is invalid because the sum of each row does not equate to {MAGIC_NUMBER}.")
else:
    print("It's a magic square!")

print(rows)
print(columns)






