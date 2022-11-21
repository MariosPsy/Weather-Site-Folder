import PySimpleGUI

feet_label = PySimpleGUI.Text("Enter a feet: ")
feet_input = PySimpleGUI.InputText(key="feet")
inches_label = PySimpleGUI.Text("Enter inches: ")
inches_input = PySimpleGUI.InputText(key="inches")
convert_button = PySimpleGUI.Button("Convert")
exit_button = PySimpleGUI.Button("Exit")
convert_label = PySimpleGUI.Text(key="convert_label")

PySimpleGUI.theme("Dark")

window = PySimpleGUI.Window("Convertor",
                            layout=([feet_label, feet_input],
                                    [inches_label, inches_input],
                                    [convert_button,exit_button, convert_label]))

while True:
    tuple = window.read()
    print("tuple: ", tuple)
    if tuple[0] == PySimpleGUI.WINDOW_CLOSED :
        break
    elif tuple[0] == "Convert" :
        if (tuple[1]["feet"] == "" and tuple[1]["inches"]) == "" :
            PySimpleGUI.popup("Enter at list one data")
        elif tuple[1]["feet"] == "" and tuple[1]["inches"] != "" :
            float_feet = 0
            float_inches = float(tuple[1]["inches"].replace(",", "."))
        else :
            float_feet = float(tuple[1]["feet"].replace(",", "."))
            float_inches = 0
        result_feet = round(((float_feet * 0.3048) + (float_inches * 0.0254)), 4)
        window["convert_label"].update(value="{} m".format(result_feet))
    elif tuple[0] == "Exit" :
        break


window.close()