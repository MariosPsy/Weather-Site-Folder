import functions
import PySimpleGUI

print("Hi from gui.py")


#Create several instances for the window
label = PySimpleGUI.Text("Type in a to-do") #Label for the window
input_box = PySimpleGUI.InputText(tooltip="Enter todo", key="todo") #Input Box for the user
add_button = PySimpleGUI.Button("Add") #Button for a action
list_box = PySimpleGUI.Listbox(values=functions.get_todo(), key="existing_todo",
                               enable_events=True, size=[45,10])
edit_button = PySimpleGUI.Button("Edit")

delete_button = PySimpleGUI.Button("Delete")

#Create the window instance
#------------------------ We put in the layout all the instance that we made
window = PySimpleGUI.Window("My to - do App",
                            layout=[[label],
                                    [input_box, add_button],
                                    [list_box, edit_button, delete_button]],
                            font=("Helvetica",12)) #Here the double brackets is how the instance appear on the window line.
#window = PySimpleGUI.Window("My to - do App", layout=([[label], [input_box]]))  ## For example with this syntax we put the in diffrent rows

while True:
    event, value = window.read()
    print("event:",event)
    print("value:",value)
    match event:
        case "Add":
            todos = functions.get_todo()
            todos.append(value["todo"]+ "\n") #Append the user input
            functions.write_todos(todos)
            window["existing_todo"].update(values=todos)
        case "Edit":
            todo_to_edit = value["existing_todo"][0] #Get the string from dictionary
            new_todo = value["todo"] + "\n" #Get the input string

            todos = functions.get_todo()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['existing_todo'].update(values=todos)
        case "Delete":
            todo_to_delete = value["existing_todo"][0]
            print("value 0 :", todo_to_delete, "type ", type(todo_to_delete))
            todos = functions.get_todo()
            print("todos list ", todos)
            todos.remove(todo_to_delete)
            functions.write_todos(todos)
            window["existing_todo"].update(value=todos)
        case "existing_todo":
            window["todo"].update(value=value["existing_todo"][0])
        case PySimpleGUI.WINDOW_CLOSED :
            break

print("Hello before closing the window")
window.close()


