def load_todo_list(filename="todo.txt"):
  tasks = []
  try:
    with open(filename, "r") as file:
      for line in file:
        tasks.append(line.strip())
  except FileNotFoundError:
    pass  # Ignore if file doesn't exist
  return tasks

def save_todo_list(tasks, filename="todo.txt"):
  with open(filename, "w") as file:
    for task in tasks:
      file.write(task + "\n")

def add_task(tasks, task):
  tasks.append(task)

def mark_complete(tasks, task_index):
  if 0 <= task_index < len(tasks):
    tasks[task_index] = tasks[task_index] + " [Complete]"

def view_todo_list(tasks):
  for index, task in enumerate(tasks):
    print(f"{index + 1}. {task}")

# Example usage
todo_list = load_todo_list()

add_task(todo_list, "Buy groceries")
add_task(todo_list, "Finish homework")

view_todo_list(todo_list)

mark_complete(todo_list, 0)

view_todo_list(todo_list)

save_todo_list(todo_list)