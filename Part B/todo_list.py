from pathlib import Path
import json

class Task:

    def __init__(self, task_id: int, desc: str, completed: bool, project: str = None):

        self.task_id = task_id
        self.desc = desc
        self.completed = completed
        self.project = project

    def __str__(self):
        return f"Task id: {self.task_id}\nDesc: {self.desc}\nCompleted: {self.completed}\nProject: {self.project}"

    def __repr__(self):
        return f"Task({self.task_id}, {self.desc!r}, {self.completed}, {self.project!r})"

    def __eq__(self, other):
        if not isinstance(other, Task):
            return False
        return self.task_id == other.task_id and self.desc == other.desc and self.completed == other.completed and self.project == other.project


def write_to_file(tasks, path):

    with open(path, "w", encoding="utf-8") as file:
        file.write(json.dumps(tasks, indent=4))

def read_from_file(path):

    file_path = Path(path)

    if file_path.exists():
        with open(path, 'r') as file:
            return json.load(file)
    else:
        return None

def add_task(tasks, string, path):

    try:
        if "#" in string:
            description = string.split(" ", 1)[1]
            task_description, task_project = description.split("#", 1)[0].rstrip(), description.split("#", 1)[1].rstrip()

            if " " in task_project:
                raise ValueError
        else:
            task_description, task_project = string.split(" ", 1)[1], None

        task_id = max([int(key) for key in tasks.keys()]) + 1 if len(tasks) > 0 else 1
        task_object = Task(task_id, task_description, False, task_project)
        tasks[str(task_id)] = {"desc": task_object.desc, "completed": task_object.completed, "project": task_object.project}

        write_to_file(tasks, path)
        print(f"Task #{task_id} has been added.")

    except (IndexError, ValueError):

        print("Invalid task format.")

def update_task(tasks, string, path):

    try:
        description = string.removeprefix("upd ").strip().split(" ", 1)
        task_id = str(description[0])

        if task_id not in tasks:

            print(f"The task with id #{task_id} does not exist. Please add it before attempting to update it.")
            return

        if len(description) == 2 and description[1].strip() != "":
            new_task_description = description[1]

        else:
            new_task_description = ""

            while not new_task_description:
                new_task_description = input(f"Enter the new description for task {task_id}: ").strip()

                if not new_task_description:
                    print("Description cannot be empty. Please try again.")

        tasks[str(task_id)].update(desc=new_task_description)

        write_to_file(tasks, path)
        print(f"Task # {task_id} has been updated.")

    except (IndexError, ValueError):
        print("Invalid update format.")


def remove_task(tasks, string, path):

    try:
        task_id = string.removeprefix("rem ").strip()

        if str(task_id) not in tasks:
            print(f"The task with id #{task_id} does not exist. Please add it before attempting to remove it.")
            return

        del tasks[str(task_id)]

        write_to_file(tasks, path)

        print(f"Task #{task_id} has been removed.")

    except (IndexError, ValueError):
        print("Invalid remove format.")

def mark_complete(tasks, string, path):

    try:
        description = string.removeprefix("done ").strip().split(" ", 1)
        task_id = str(description[0])

        if task_id not in tasks:
            print(f"The task with id #{task_id} does not exist. Please add it before attempting to mark it as complete.")
            return

        tasks[str(task_id)].update(completed=True)

        write_to_file(tasks, path)
        print(f"Task #{task_id} has been marked as completed.")

    except (IndexError, ValueError):

        print("Invalid done format.")


def list_all(tasks):
    if len(tasks) == 0:
        print("There are no tasks in the list.")
    for outer_key, inner_dict in sorted(tasks.items(), key=lambda item: int(item[0])):

        print(f"Task id: {outer_key}")
        print(f"Desc: {inner_dict['desc']}")
        print(f"Completed: {inner_dict['completed']}")
        print(f"Project: {inner_dict['project']}")
        print()


def list_todo(tasks):
    if len(tasks) == 0:
            print("There are no tasks in the list.")
    for outer_key, inner_dict in sorted(tasks.items(), key=lambda item: int(item[0])):

        if inner_dict["completed"] == False:

            print(f"Task id: {outer_key}")
            print(f"Desc: {inner_dict['desc']}")
            print(f"Completed: {inner_dict['completed']}")
            print(f"Project: {inner_dict['project']}")
            print()


def purge(tasks, path):

    completed_keys = [key for key, task in tasks.items() if task["completed"]]

    if len(completed_keys) == 0:
        print("No tasks in the list are completed.")
    else:
        for key in completed_keys:
                del tasks[key]
        
        write_to_file(tasks, path)
        print("Tasks purged.")
        
def main():

    path = "tasks.txt"

    try:
        tasks = read_from_file(path) or {}

    except (json.JSONDecodeError, OSError):
        tasks = {}

    print("---Task manager---")
    

    while True:
        print()
        print("Commands:")
        print("add -> i.e add [task description]")
        print("update -> i.e upd [task id]")
        print("remove -> i.e rem [task id]")
        print("mark as done -> i.e done [task id]")
        print("list all -> i.e list all")
        print("list todo -> i.e list todo")
        print("purge -> i.e purge")

        print()

        command = input("Please enter a command: ")
        print()

        match command.split(" ", 1)[0].lower():
            case "add":
                add_task(tasks, command, path)
            case "upd":
                update_task(tasks, command, path)
            case "rem":
                remove_task(tasks, command, path)
            case "done":
                mark_complete(tasks, command, path)
            case "list":
                try:
                    if command.split(" ", 1)[1].lower() == "all":
                        list_all(tasks)

                    elif command.split(" ", 1)[1].lower() == "todo":
                        list_todo(tasks)

                except IndexError:
                    print("Please specify 'all' or 'todo'.")

            case "purge":
                purge(tasks, path)
            case "exit":
                break

if __name__ == "__main__":
    main()