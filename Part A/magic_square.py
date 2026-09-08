rows = []

first_row = input("Enter row 1 of the magic square: ")

rows.append([int(x) for x in first_row.split()])

number_of_rows = len(rows[0]) 

for x in range(2, number_of_rows + 1):
    row = input(f"Enter row {x} of the magic square: ")
    rows.append([int(x) for x in row.split()])

range_list = sorted([number for sublist in rows for number in sublist])

if len(range_list) > number_of_rows ** 2  or len(range_list) < number_of_rows ** 2:
     print(f"The square must have {number_of_rows ** 2} numbers.")

if range_list[-1] > number_of_rows ** 2 or range_list[0] < 1:
    print("The square does not respect the range constraint.")


if len(range_list) != len(set(range_list)):
    print("The square cannot have duplicates.")
