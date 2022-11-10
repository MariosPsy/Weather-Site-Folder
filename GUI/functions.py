FILEPATH = "todo_item.txt"

def get_todo(filepath=FILEPATH) :
    """Read a text file and return
     the list of the to-do items """

    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items in the text file"""

    with open(filepath, "w") as file :
        file.writelines(todos_arg)


print("Hello from outside")

if __name__ == "__main__" :
    print("Hello")
    print(get_todos())

