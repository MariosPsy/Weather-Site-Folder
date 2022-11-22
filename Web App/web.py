import streamlit
import functions

todos = functions.get_todo()

def add_todo():
    todo = streamlit.session_state["new_todo"] + "\n"
    print(todo)
    todos.append(todo)
    functions.write_todos(todos)

streamlit.title("My Todo App")
streamlit.subheader("This is a a check list")
streamlit.write("Click for deleting a job")
streamlit.checkbox("This is a check box function")

for index, todo in enumerate(todos):
    checkbox = streamlit.checkbox(todo, key=todo)
    if checkbox :
        print(checkbox)
        todos.pop(index)
        functions.write_todos(todos)
        del streamlit.session_state[todo]
        streamlit.experimental_rerun()

streamlit.text_input(label="Write down here", placeholder="Enter a new todo...",
                     on_change=add_todo, key="new_todo")

streamlit.session_state

print("Hello from the end of python script")