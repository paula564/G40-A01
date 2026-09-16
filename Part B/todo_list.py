class Task:
    def __init__(self, task_id: int, desc: str, completed: bool, project: str = None):
        self.task_id = task_id      
        self.desc = desc
        self.completed = completed  
        self.project = project
#maybe create enum for the different tasks?

def add_task(tasks, string):
    if "#" in string:
        description = string.split(" ", 1)[1]
        task_description, task_project = description.split("#", 1)[0].rstrip(), description.split("#", 1)[1].rstrip()
    else:
        task_description, task_project = string.split(" ", 1)[1], None

    task_id = len(tasks) + 1 if len(tasks) > 0 else 1
    task_object = Task(task_id, task_description, False, task_project)
    tasks[task_id] = task_object.__dict__

def update_task(tasks, string):
    description = string.removeprefix("upd ").strip().split(" ", 1)

    task_id = int(description[0])

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
    
    tasks[task_id].update(desc=new_task_description)
    
def main():
   tasks = {}
   while True:
        command = input("Please enter a command: ")
        match command.split(" ", 1)[0].lower():
            case "add":
                add_task(tasks, command)
                print(f"Added task to list: {tasks}")
            case "upd":
                update_task(tasks, command)
                print(f"Updated list: {tasks}")
            case "exit":
                break


if __name__ == "__main__":
    main()
