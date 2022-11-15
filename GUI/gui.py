import functions
import PySimpleGUI

print("Hi from gui.py")


#Create several instances for the window
label = PySimpleGUI.Text("Type in a to-do") #Label for the window
input_box = PySimpleGUI.InputText(tooltip="Enter todo", key="todo") #Input Box for the user
add_button = PySimpleGUI.Button("Add") #Button for a action

#Create the window instance
#------------------------ We put in the layout all the instance that we made
window = PySimpleGUI.Window("My to - do App",
                            layout=[[label], [input_box, add_button]],
                            font=("Helvetica",12)) #Here the double brackets is how the instance appear on the window line.
#window = PySimpleGUI.Window("My to - do App", layout=([[label], [input_box]]))  ## For example with this syntax we put the in diffrent rows

while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = functions.get_todo()
            todos.append(value["todo"] + "\n") #Append the user input
            functions.write_todos(todos)
        case PySimpleGUI.WINDOW_CLOSED :
            break

print("Hello after closing the window")
window.close()


