import PySimpleGUI

feet_label = PySimpleGUI.Text("Enter a feet: ")
feet_input = PySimpleGUI.InputText(key="feet")
inches_label = PySimpleGUI.Text("Enter inches: ")
inches_input = PySimpleGUI.InputText(key="inches")
convert_button = PySimpleGUI.Button("Convert")

meters = "something"
convert_label = PySimpleGUI.Text(meters, key="convert_label")

window = PySimpleGUI.Window("Convertor",
                            layout=([feet_label, feet_input],
                                    [inches_label, inches_input],
                                    [convert_button, convert_label]))

while True:
    tuple = window.read()
    print("tuple: ", tuple)


window.close()