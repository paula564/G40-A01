rows = []

first_row = input("Enter row 1 of the magic square: ")

rows.append([int(x) for x in first_row.split()])

number_of_rows = len(rows[0]) 

for x in range(2, number_of_rows + 1):
    row = input(f"Enter row {x} of the magic square: ")
    rows.append([int(x) for x in row.split()])

for i in rows:
    print(i)