#Frontend - GUI

#from functions import get_todos, write_todos
import functions
import time

file_mod = "todos.txt" 
        
now = time.strftime("%b %d, %Y %H:%M:%S")


while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = functions.get_todos(file_mod)
        todos.append(todo + "\n")
        functions.write_todos(file_mod, todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos(file_mod)
        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}--{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1
            todos = functions.get_todos("todos.txt")
            new_todo = input("Enter new todo")
            todos[number] = new_todo + "\n"
            functions.write_todos(file_mod, todos) #reference the function from the imported file
        except ValueError:
            print("Command not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos("todos.txt")
            index = number -1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index) #removes item from todos list
            functions.write_todos(file_mod, todos)
            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("No item with that number exists.")
            continue

    elif  user_action.startswith("exit"):
        break

    else:
        print("Command is not valid!")
print("Bye!")

#for i, j in enumerate ("Hello"): #here, i is index and j is the item for that index
#   print(i, j) 

#ips = ['100.122.133.105', '100.122.133.111']
#user_input = int(input("Enter the index of the IP you want: "))
#message = f"You chose: {ips[user_input]}"
#print(message)