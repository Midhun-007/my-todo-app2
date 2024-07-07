import streamlit as s
import function as f
todo=f.get_todo()
def add_todo():
    a=s.session_state['new_todo']
    f.write_todo(todo,a)
for i,j in enumerate(todo):
    checkbox=s.checkbox(j, key=j.strip('\n'))
    if checkbox:
        todo.pop(i)
        f.write_todo(todo)
        del s.session_state[j.strip('\n')]
        s.experimental_rerun()
s.title("My To-Do App")
s.subheader('Web App By Midhun')

print(todo)
s.text_input(label='',placeholder='Add a new Todo',key='new_todo',on_change=add_todo)
s.session_state
