from colorama import init, Fore
import todo_list as tl
import tempfile
import os


#Three different scenarios: add a task to an empty list, 
# add a task with a project to an empty list, and add a task to a non-empty list, and add invalid task to empty list
data_add_task = (
    ("add Study for Programming test", {}),
    ("add Study for Programming test #school", {}),
    ("add Complete English assignment", {
        "1": {
            "desc": "Existing task",
            "completed": False,
            "project": None
        }
    }),
    ("add", {})
)

#First three scenarios should add while the last one should return an error message and not add. 
data_add_task_response = (
    {
        "1": {
            "desc": "Study for Programming test",
            "completed": False,
            "project": None
        }
    },
    {
        "1": {
            "desc": "Study for Programming test",
            "completed": False,
            "project": "school"
        }
    },
    {
        "1": {
            "desc": "Existing task",
            "completed": False,
            "project": None
        },
        "2": {
            "desc": "Complete English assignment",
            "completed": False,
            "project": None
        }
    }, 
    
        {}
)

#Want the last one to test whether or not the system prompts the user to re-enter the description
data_update_task = (
    ("upd 1 Write English essay", {
        "1": {
            "desc": "Complete Web IV assignment",
            "completed": False,
            "project": "school"
        }
    }),
    ("upd 2 Study for test", {
        "1": {
            "desc": "Complete Web IV assignment",
            "completed": False,
            "project": None
        },
        "2": {
            "desc": "Study for test",
            "completed": True,
            "project": "school"
        }
    })
)

data_update_task_response = (
    {
        "1": {
            "desc": "Write English essay",
            "completed": False,
            "project": "school"
        }
    },
    {
        "1": {
            "desc": "Complete Web IV assignment",
            "completed": False,
            "project": None
        },
        "2": {
            "desc": "Study for test",
            "completed": True,
            "project": "school"
        }
    }
)


data_remove_task = (
    ("rem 1", {
        "1": {
            "desc": "Task one",
            "completed": False,
            "project": None
        },
        "2": {
            "desc": "Task two",
            "completed": False,
            "project": None
        }
    }),
    ("rem 2", {
        "1": {
            "desc": "Task one",
            "completed": False,
            "project": None
        },
        "2": {
            "desc": "Task two",
            "completed": False,
            "project": None
        }
    })
)

data_remove_task_response = (
    {
        "2": {
            "desc": "Task two",
            "completed": False,
            "project": None
        }
    },
    {
        "1": {
            "desc": "Task one",
            "completed": False,
            "project": None
        }
    }
)


data_mark_complete = (
    ("done 1", {
        "1": {
            "desc": "Task one",
            "completed": False,
            "project": None
        }
    }),
    ("done 2", {
        "1": {
            "desc": "Task one",
            "completed": False,
            "project": None
        },
        "2": {
            "desc": "Task two",
            "completed": False,
            "project": "school"
        }
    })
)

data_mark_complete_response = (
    {
        "1": {
            "desc": "Task one",
            "completed": True,
            "project": None
        }
    },
    {
        "1": {
            "desc": "Task one",
            "completed": False,
            "project": None
        },
        "2": {
            "desc": "Task two",
            "completed": True,
            "project": "school"
        }
    }
)


data_purge = (
    {
        "1": {
            "desc": "Task one",
            "completed": True,
            "project": None
        },
        "2": {
            "desc": "Task two",
            "completed": False,
            "project": None
        }
    },
    {
        "1": {
            "desc": "Task one",
            "completed": True,
            "project": None
        },
        "2": {
            "desc": "Task two",
            "completed": True,
            "project": "school"
        }
    },
    {
        "1": {
            "desc": "Task one",
            "completed": False,
            "project": None
        }
    }
)

data_purge_response = (
    {
        "2": {
            "desc": "Task two",
            "completed": False,
            "project": None
        }
    },
    {},
    {
        "1": {
            "desc": "Task one",
            "completed": False,
            "project": None
        }
    }
)


data_file = (
    {
        "1": {
            "desc": "Study",
            "completed": False,
            "project": "school"
        }
    },
    {
        "1": {
            "desc": "Study",
            "completed": False,
            "project": "school"
        },
        "2": {
            "desc": "Finish assignment",
            "completed": True,
            "project": None
        }
    }
)


def print_pass(the_data, i):
    print(f'{Fore.GREEN}Test {i} with {the_data} passed')


def print_fail(the_data, i):
    print(f'{Fore.RED}*** Test {i} with {the_data} failed.')


def run_add_task_test(test_data, expected):
    command, tasks = test_data

    with tempfile.NamedTemporaryFile(delete=False) as file:
        path = file.name

    try:
        tl.add_task(tasks, command, path)
        assert tasks == expected, tasks

    finally:
        os.remove(path)


def run_update_task_test(test_data, expected):
    command, tasks = test_data

    with tempfile.NamedTemporaryFile(delete=False) as file:
        path = file.name

    try:
        tl.update_task(tasks, command, path)
        assert tasks == expected, tasks

    finally:
        os.remove(path)


def run_remove_task_test(test_data, expected):
    command, tasks = test_data

    with tempfile.NamedTemporaryFile(delete=False) as file:
        path = file.name

    try:
        tl.remove_task(tasks, command, path)
        assert tasks == expected, tasks

    finally:
        os.remove(path)


def run_mark_complete_test(test_data, expected):
    command, tasks = test_data

    with tempfile.NamedTemporaryFile(delete=False) as file:
        path = file.name

    try:
        tl.mark_complete(tasks, command, path)
        assert tasks == expected, tasks

    finally:
        os.remove(path)


def run_purge_test(test_data, expected):

    with tempfile.NamedTemporaryFile(delete=False) as file:
        path = file.name

    try:
        tl.purge(test_data, path)
        assert test_data == expected, test_data

    finally:
        os.remove(path)


def run_file_test(test_data):

    with tempfile.NamedTemporaryFile(delete=False) as file:
        path = file.name

    try:
        tl.write_to_file(test_data, path)
        actual = tl.read_from_file(path)

        assert actual == test_data, actual

    finally:
        os.remove(path)


def run_task_magic_methods_test():

    task_1 = tl.Task(1, "Study", False, "school")
    task_2 = tl.Task(1, "Study", False, "school")

    assert str(task_1) == "Task id: 1\nDesc: Study\nCompleted: False\nProject: school"
    assert repr(task_1) == "Task(1, 'Study', False, 'school')"
    assert task_1 == task_2


def test_add_task():

    print("Test add_task")

    for i, test_val in enumerate(data_add_task):

        try:
            run_add_task_test(test_val, data_add_task_response[i])
            print_pass(test_val, i + 1)

        except AssertionError as test_data:
            print_fail(test_data, i + 1)
            continue


def test_update_task():

    print("Test update_task")

    for i, test_val in enumerate(data_update_task):

        try:
            run_update_task_test(test_val, data_update_task_response[i])
            print_pass(test_val, i + 1)

        except AssertionError as test_data:
            print_fail(test_data, i + 1)
            continue


def test_remove_task():

    print("Test remove_task")

    for i, test_val in enumerate(data_remove_task):

        try:
            run_remove_task_test(test_val, data_remove_task_response[i])
            print_pass(test_val, i + 1)

        except AssertionError as test_data:
            print_fail(test_data, i + 1)
            continue


def test_mark_complete():

    print("Test mark_complete")

    for i, test_val in enumerate(data_mark_complete):

        try:
            run_mark_complete_test(test_val, data_mark_complete_response[i])
            print_pass(test_val, i + 1)

        except AssertionError as test_data:
            print_fail(test_data, i + 1)
            continue


def test_purge():

    print("Test purge")

    for i, test_val in enumerate(data_purge):

        test_data = test_val.copy()

        try:
            run_purge_test(test_data, data_purge_response[i])
            print_pass(test_val, i + 1)

        except AssertionError as test_data:
            print_fail(test_data, i + 1)
            continue


def test_file():

    print("Test file read/write")

    for i, test_val in enumerate(data_file):

        try:
            run_file_test(test_val)
            print_pass(test_val, i + 1)

        except AssertionError as test_data:
            print_fail(test_data, i + 1)
            continue


def test_task_magic_methods():

    print("Test Task magic methods")

    try:
        run_task_magic_methods_test()
        print_pass("Task magic methods", 1)

    except AssertionError as test_data:
        print_fail(test_data, 1)


def do_tests():
    test_add_task()
    test_update_task()
    test_remove_task()
    test_mark_complete()
    test_purge()
    test_file()
    test_task_magic_methods()


if __name__ == "__main__":
    init(autoreset=True)
    do_tests()