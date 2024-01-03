import streamlit as st
import functions

todos = functions.get_todos("todos.txt")
def new_todo():
    todo = st.session_state["new_todo"] + "\n"
    print(todo)

    todos.append(todo)

    functions.write_todos(todos)


st.title("My to-do app")
st.subheader("This is my todo app")
st.write("This app is used to increased the productivity of humans")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="",placeholder="Add new todo...", on_change=new_todo, key="new_todo")

print("Hello")

st.session_state