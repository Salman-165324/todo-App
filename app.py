# Target to build a todo app with add, show, edit, complete and Exit functionality.

todo_list = []
completed_task = []
while True:
    user_command = input("Please write Add, Show, Edit, Complete and Exit to perform a task:\n")

    match user_command:

        case 'Add':
            while True:
                user_input = input("Please write your todo items or write 'Back' to go back:\n")
                if user_input == "Back":
                    break
                todo_list.append(user_input)

        case 'Show':
            for todo in todo_list:
                print(todo)
        case 'Edit':
            print("Inside Edit")
        case 'Complete':
            print("Todo items to mark complete:\n")
            for counter, todo in enumerate(todo_list, 1):
                print(f"{counter}. {todo}")
            to_complete_todo_serial_no = int(
                input("Enter the serial no. of the todo item you want add to the completed todo list:\n"))
            removed_item = todo_list.pop(to_complete_todo_serial_no - 1)

            completed_task.append(removed_item)
            print("Your completed task's List:\n")
            for counter, todo in enumerate(completed_task, 1):
                print(f"{counter}. {todo}")

        case 'Exit':
            print("Tata Bye Bye. Never see you again")
            break
