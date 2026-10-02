
from colorama import init, Fore
import magic_square as ms
from unittest.mock import patch
from io import StringIO

#Different scenarios to test whether the is_magic_sum functions properly compares the value of each sum to the magic number
data_sum_magic = (
    ([2, 7, 6], 15),
    ([1, 5, 9], 15),
    ([1, 2, 3], 15),
    ([4, 4, 4], 15)
)

data_sum_magic_response = (
    True,
    True,
    False,
    False
)
#Different scenarios to test whether the is_valid_rows correctly determines whether the sum of
#each row in a square matches the value of the magic number
data_rows = (
    (
        [[2, 7, 6],
         [9, 5, 1],
         [4, 3, 8]],
        15
    ),
    (
        [[2, 7, 6],
         [9, 5, 2],
         [4, 3, 8]],
        15
    )
)

data_rows_response = (
    True,
    False
)

#Diffrent scenarios to test whether the is_valid_columns correctly determines whether the sum of
#each column in a square matches the value of the magic number

data_columns = (
    (
        [[2, 9, 4],
         [7, 5, 3],
         [6, 1, 8]],
        15
    ),
    (
        [[2, 9, 4],
         [7, 5, 4],
         [6, 1, 8]],
        15
    )
)

data_columns_response = (
    True,
    False
)
#Diffrent scenarios to test whether the is_valid_diagonals correctly determines whether the sum of
#each diagonal in a square matches the value of the magic number
data_diagonals = (
    (
        [[2, 5, 8],
         [6, 5, 4]],
        15
    ),
    (
        [[2, 5, 8],
         [6, 5, 7]],
        15
    )
)

data_diagonals_response = (
    True,
    False
)

#These tests cover various input scenarios (valid input, missing number, out of range value, and duplicate number)
data_valid_input = (
    (
        [[2, 7, 6],
         [9, 5, 1],
         [4, 3, 8]],
        3
    ),
    (
        [[2, 7, 6],
         [9, 5],
         [4, 3, 8]],
        3
    ),
    (
        [[2, 7, 6],
         [9, 5, 1],
         [4, 3, 10]],
        3
    ),
    (
        [[2, 7, 6],
         [9, 5, 1],
         [4, 3, 3]],
        3
    )
)

data_valid_input_response = (
    True,
    False,
    False,
    False,
)

#Test to ensure get_columns() returns the correct columns based on the inputted rows
data_get_columns = (
    (
        [[2, 7, 6],
         [9, 5, 1],
         [4, 3, 8]]
    ),
    (
        [[1, 2],
         [3, 4]]
    )
)

data_get_columns_response = (
    [
        [2, 9, 4],
        [7, 5, 3],
        [6, 1, 8]
    ],
    [
        [1, 3],
        [2, 4]
    ]
)

#Test to ensure get_diagonals() returns the correct diagonals based on the inputted rows
data_get_diagonals = (
    (
        [[2, 7, 6],
         [9, 5, 1],
         [4, 3, 8]],
        3
    ),
    (
        [[1, 2],
         [3, 4]],
        2
    )
)

data_get_diagonals_response = (
    [
        [2, 5, 8],
        [6, 5, 4]
    ],
    [
        [1, 4],
        [2, 3]
    ]
)

#Test to ensure get_magic_number() returns the correct magic number based on the number of rows
data_magic_number = (
    3,
    4,
    5
)

data_magic_number_response = (
    15,
    34,
    65
)

#Test to ensure get_rows() correctly returns a list of lists where each list represents a row in the square
data_get_rows = (
    (
        "2 7 6",
        "9 5 1",
        "4 3 8"
    ),
    (
        "1 2",
        "3 4"
    )
)

data_get_rows_response = (
    [
        [2, 7, 6],
        [9, 5, 1],
        [4, 3, 8]
    ],
    [
        [1, 2],
        [3, 4]
    ]
)

data_main = (
    (
        "2 7 6",
        "9 5 1",
        "4 3 8"
    ),
    (
        "2 7 6",
        "9 5 2",
        "4 3 8"
    ),
    (
        "4 9 6",
        "3 4",
        "1 2 8"
    ),
    (
        "4 5 4",
        "3 6 2",
        "9 8 7"
    )
)

data_main_response = (
    "This is a magic square! The sum of each row, column and diagonal is 15.",
    "This is not a magic square. The sum of each row, column and diagonal is not 15.",
    "Each row must have 3 numbers.",
    "The square does not respect the range constraint."
     
)


def print_pass(the_data, i):
    print(f'{Fore.GREEN}Test {i} with {the_data} passed')


def print_fail(the_data, i):
    print(f'{Fore.RED}*** Test {i} with {the_data} failed.')


def run_sum_magic_test(test_data, expected):
    value, magic_number = test_data
    actual = ms.is_sum_magic(value, magic_number)
    assert actual == expected, actual


def run_rows_test(test_data, expected):
    rows, magic_number = test_data
    actual = ms.is_valid_rows(rows, magic_number)
    assert actual == expected, actual


def run_columns_test(test_data, expected):
    columns, magic_number = test_data
    actual = ms.is_valid_columns(columns, magic_number)
    assert actual == expected, actual


def run_diagonals_test(test_data, expected):
    diagonals, magic_number = test_data
    actual = ms.is_valid_diagonals(diagonals, magic_number)
    assert actual == expected, actual


def run_valid_input_test(test_data, expected):
    rows, number_of_rows = test_data
#Rather than waiting for a real person to enter input, the 
 #the program is automatically fed the test_data. 
    with patch("sys.stdout", new=StringIO()):
        actual = ms.is_valid_input(rows, number_of_rows)
    assert actual == expected, actual


def run_get_columns_test(test_data, expected):
    actual = ms.get_columns(test_data)
    assert actual == expected, actual


def run_get_diagonals_test(test_data, expected):
    rows, number_of_rows = test_data
    actual = ms.get_diagonals(rows, number_of_rows)
    assert actual == expected, actual


def run_magic_number_test(test_data, expected):
    actual = ms.get_magic_number(test_data)
    assert actual == expected, actual


def run_get_rows_test(test_data, expected):
    #Rather than waiting for a real person to enter input, the 
    #the program is automatically fed the test_data. 
    with patch("builtins.input", side_effect=test_data):
        actual = ms.get_rows()
    assert actual == expected, actual


def run_main_test(test_data, expected):
     #Rather than waiting for a real person to enter input, the 
        #the program is automatically fed the test_data. The result of the print
        #statement is saved in a variable called output
        with patch("builtins.input", side_effect=test_data):
            with patch("sys.stdout", new=StringIO()) as output:
                ms.main()
    
        actual = output.getvalue().strip()
        assert actual == expected, actual


def test_sum_magic():
    print("Test is_sum_magic")

    for i, test_val in enumerate(data_sum_magic):
        try:
            run_sum_magic_test(test_val, data_sum_magic_response[i])
            print_pass(test_val, i + 1)

        except AssertionError as test_data:
            print_fail(test_data, i + 1)
            continue


def test_valid_rows():
    print("Test is_valid_rows")
    for i, test_val in enumerate(data_rows):
        try:
            run_rows_test(test_val, data_rows_response[i])
            print_pass(test_val, i + 1)
        except AssertionError as test_data:
            print_fail(test_data, i + 1)
            continue


def test_valid_columns():
    print("Test is_valid_columns")
    for i, test_val in enumerate(data_columns):
        try:
            run_columns_test(test_val, data_columns_response[i])
            print_pass(test_val, i + 1)
        except AssertionError as test_data:
            print_fail(test_data, i + 1)
            continue


def test_valid_diagonals():
    print("Test is_valid_diagonals")
    for i, test_val in enumerate(data_diagonals):
        try:
            run_diagonals_test(test_val, data_diagonals_response[i])
            print_pass(test_val, i + 1)
        except AssertionError as test_data:
            print_fail(test_data, i + 1)
            continue


def test_valid_input():
    print("Test is_valid_input")
    for i, test_val in enumerate(data_valid_input):
        try:
            run_valid_input_test(test_val, data_valid_input_response[i])
            print_pass(test_val, i + 1)
        except AssertionError as test_data:
            print_fail(test_data, i + 1)
            continue


def test_get_columns():
    print("Test get_columns")
    for i, test_val in enumerate(data_get_columns):
        try:
            run_get_columns_test(test_val, data_get_columns_response[i])
            print_pass(test_val, i + 1)
        except AssertionError as test_data:
            print_fail(test_data, i + 1)
            continue


def test_get_diagonals():
    print("Test get_diagonals")
    for i, test_val in enumerate(data_get_diagonals):
        try:
            run_get_diagonals_test(test_val, data_get_diagonals_response[i])
            print_pass(test_val, i + 1)
        except AssertionError as test_data:
            print_fail(test_data, i + 1)
            continue


def test_magic_number():
    print("Test get_magic_number")
    for i, test_val in enumerate(data_magic_number):
        try:
            run_magic_number_test(test_val, data_magic_number_response[i])
            print_pass(test_val, i + 1)
        except AssertionError as test_data:
            print_fail(test_data, i + 1)
            continue


def test_get_rows():
    print("Test get_rows")
    for i, test_val in enumerate(data_get_rows):
        try:
            run_get_rows_test(test_val, data_get_rows_response[i])
            print_pass(test_val, i + 1)
        except AssertionError as test_data:
            print_fail(test_data, i + 1)
            continue


def test_main():
    print("Test main")
    for i, test_val in enumerate(data_main):
        try:
            run_main_test(test_val, data_main_response[i])
            print_pass(test_val, i + 1)
        except AssertionError as test_data:
            print_fail(test_data, i + 1)
            continue


def do_tests():
    test_sum_magic()
    test_valid_rows()
    test_valid_columns()
    test_valid_diagonals()
    test_valid_input()
    test_get_columns()
    test_get_diagonals()
    test_magic_number()
    test_get_rows()
    test_main()


if __name__ == "__main__":
    init(autoreset=True)
    do_tests()

