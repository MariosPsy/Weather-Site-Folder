import PySimpleGUI

feet_label = PySimpleGUI.Text("Enter a feet: ")
feet_input = PySimpleGUI.InputText(key="feet")
inches_label = PySimpleGUI.Text("Enter inches: ")
inches_input = PySimpleGUI.InputText(key="inches")
convert_button = PySimpleGUI.Button("Convert")

convert_label = PySimpleGUI.Text("None", key="convert_label")

window = PySimpleGUI.Window("Convertor",
                            layout=([feet_label, feet_input],
                                    [inches_label, inches_input],
                                    [convert_button, convert_label]))

while True:
    tuple = window.read()
    print("tuple: ", tuple)
    if tuple[0] == PySimpleGUI.WINDOW_CLOSED :
        break
    elif tuple[0] == "Convert" :
        float_feet = tuple[1]["feet"]
        float_feet = float(float_feet.replace(",", "."))
        result_feet = round((float_feet * 0.3048), 4)
        window["convert_label"].update(value="{} m".format(result_feet))


window.close()