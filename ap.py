tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added:", task)

def show_tasks():
    print("Your Tasks:")
    for t in tasks:
        print("-", t)

# Example usage
add_task("Complete assignment")
show_tasks()
