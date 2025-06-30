# Reto Unidad 1
Implementacion de practicas sobre los distintos modelos de representacion de datos

# Planteamiento del ejercicio a constuir

Trabajar sobre la plataforma github cada estudiante se debe crear una cuenta, luego organizar una carpeta donde tenga la siguiente estructura:

Tareas, Proyectos

En estas carpetas se subiran las tareas que se plantea en cada modulo y en la de proyectos, los dos proyectos que se hacen por modulo.

Nota: Realizar la siguiente practica:

- Realizar las practicas definidas en la plataforma google colab = Practicas
https://colab.research.google.com/drive/1K-pz-j6sycW6iBSgXTQzBGOncJb9oi08?usp=sharing

- Subir los ejercicios resueltos en su plataforma de github y pasar el link para las revisiones.

# Ejercicios Propuestos

## 1 : Methods

**Methods**

Here are some examples tailored for students to understand and implement various representation methods:

**Static Representation**

Scenario: Representing a library catalog.

Task: Create a program using a static data structure (like a list or dictionary) to store information about books in a library catalog. The program should allow users to:

Add new books: Include title, author, ISBN, and genre.
Search for books: By title, author, or ISBN.
Display all books: In a formatted way.

### Codigo

* Example:

catalog = {}  # Using a dictionary to store book information

def add_book(title, author, isbn, genre):
  catalog[isbn] = {'title': title, 'author': author, 'genre': genre}

def search_book(query):
  results = []
  for isbn, book_data in catalog.items():
    if query in book_data['title'] or query in book_data['author'] or query == isbn:
      results.append(book_data)
  return results

def display_catalog():
  for isbn, book_data in catalog.items():
    print(f"ISBN: {isbn}, Title: {book_data['title']}, Author: {book_data['author']}, Genre: {book_data['genre']}")

# Example usage
add_book("The Lord of the Rings", "J.R.R. Tolkien", "9780547928227", "Fantasy")
add_book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "9780345391803", "Science Fiction")

search_results = search_book("Tolkien")
print(search_results)

display_catalog()

Output :

## 2: Dynamic


Dynamic

Representation Scenario: Simulating a bank account.

Task: Create a program that uses a dynamic data structure (like a list) to represent a bank account's transaction history. The program should allow users to:

Deposit money: Add a transaction record with the amount and type "deposit". Withdraw money: Add a transaction record with the amount and type "withdrawal". View transaction history: Display all transactions in chronological order. Check balance: Calculate the current balance based on all transactions. Example:

### Codigo :

transactions = []

def deposit(amount):
  transactions.append({'type': 'deposit', 'amount': amount})

def withdraw(amount):
  transactions.append({'type': 'withdrawal', 'amount': amount})

def view_history():
  for transaction in transactions:
    print(f"{transaction['type'].capitalize()}: {transaction['amount']}")

def check_balance():
  balance = 0
  for transaction in transactions:
    if transaction['type'] == 'deposit':
      balance += transaction['amount']
    else:
      balance -= transaction['amount']
  return balance

* Example usage
deposit(1000)
withdraw(200)
deposit(500)

view_history()
print(f"Current balance: {check_balance()}")


## 3: Persistent

**Persistent**

Representation
Scenario: Creating a simple to-do list application.

Task: Develop a program that stores a to-do list persistently using a file (e.g., a text file or JSON file). The program should allow users to:

Add tasks: Append new tasks to the list.
Mark tasks as complete: Update the status of tasks.
View the to-do list: Display all tasks with their status.
Save and load the list: To and from the file.
Example (using a text file):


### codigo :

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

* Example usage
todo_list = load_todo_list()

add_task(todo_list, "Buy groceries")
add_task(todo_list, "Finish homework")

view_todo_list(todo_list)

mark_complete(todo_list, 0)

view_todo_list(todo_list)

save_todo_list(todo_list)


## 4: Simulated

Simulated

Representation Scenario: Modeling a traffic intersection.

Task: Create a program that simulates a traffic intersection with traffic lights and cars. Use objects to represent cars and traffic lights. The program should:

Create cars: With random arrival times and directions. Control traffic lights: Change lights at regular intervals. Move cars: Based on traffic light signals and car positions. Display the intersection: Visually represent the cars and traffic lights (e.g., using text-based output). Example (simplified):


### codigo :

import random
import time

class Car:
  def __init__(self, direction):
    self.direction = direction
    self.position = 0

class TrafficLight:
  def __init__(self):
    self.color = "red"

  def change_color(self):
    if self.color == "red":
      self.color = "green"
    else:
      self.color = "red"

# ... (rest of the simulation logic) ...
