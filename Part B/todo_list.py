class Task:
    def __init__(self, task_id: int, desc: str, completed: bool, project: str = None):
        self.task_id = task_id      
        self.desc = desc
        self.completed = completed  
        self.project = project

def add_task(tasks, string):
    if "#" in string:
        description = string.split(" ", 1)[1]
        task_description, task_project = description.split("#", 1)[0].rstrip(), description.split("#", 1)[1].rstrip()
    else:
        task_description, task_project = string.split(" ", 1)[1], None

    task_id = len(tasks) + 1 if len(tasks) > 0 else 1
    task_object = Task(task_id, task_description, False, task_project)
    tasks[task_id] = task_object.__dict__
    

def main():
   tasks = {}
   while True:
        command = input("Please enter a command: ")
        if command.split(" ", 1)[0] == "add":
            add_task(tasks, command)
            print(f"The task object: {tasks[1]}")
            print(f"The list of tasks: {tasks}")
        if command.split(" ", 1)[0] == "exit":
            break
    

if __name__ == "__main__":
    main()
