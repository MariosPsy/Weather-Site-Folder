import functions
import PySimpleGUI

print("Hi")


#Create several instances for the window
label = PySimpleGUI.Text("Type in a to-do") #Label for the window
input_box = PySimpleGUI.InputText(tooltip="Enter todo") #Input Box for the user
add_button = PySimpleGUI.Button("Add") #Button for a action

#Create the window instance
#-------------------------------------------- We put in the layout all the instance that we made
window = PySimpleGUI.Window("My to - do App", layout=([[label], [input_box, add_button]])) #Here the double brackets is how the instance appear on the window line.
#window = PySimpleGUI.Window("My to - do App", layout=([[label], [input_box]]))  ## For example with this syntax we put the in diffrent rows
window.read()
#Everything above window.read() is execute after closing the window
print("Hello after closing the window")
window.close()


