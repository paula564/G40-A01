from pathlib import Path
import json


class Task:
    def __init__(self, task_id: int, desc: str, completed: bool, project: str = None):
        self.task_id = task_id      
        self.desc = desc
        self.completed = completed  
        self.project = project
#maybe create enum for the different tasks?

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
    if "#" in string:
        description = string.split(" ", 1)[1]
        task_description, task_project = description.split("#", 1)[0].rstrip(), description.split("#", 1)[1].rstrip()
    else:
        task_description, task_project = string.split(" ", 1)[1], None

    task_id = len(tasks) + 1 if len(tasks) > 0 else 1
    task_object = Task(task_id, task_description, False, task_project)
    tasks[str(task_id)] = task_object.__dict__

    write_to_file(tasks, path)
    
        

def update_task(tasks, string, path):
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

def remove_task(tasks, string, path):
    task_id = string.removeprefix("rem ").strip()
    if str(task_id) not in tasks:
            print(f"The task with id #{task_id} does not exist. Please add it before attempting to remove it.")
            return
    del tasks[str(task_id)]

    write_to_file(tasks, path)


    
    
def main():
   path = "tasks.txt"
   tasks = read_from_file(path) or {}
   while True:
        command = input("Please enter a command: ")
        match command.split(" ", 1)[0].lower():
            case "add":
                add_task(tasks, command, path)
                print(f"Added task to list: {tasks}")
            case "upd":
                update_task(tasks, command, path)
                print(f"Updated list: {tasks}")
            case "rem":
                remove_task(tasks, command, path)
                print(f"Updated list: {tasks}")
            case "exit":
                break


if __name__ == "__main__":
    main()
