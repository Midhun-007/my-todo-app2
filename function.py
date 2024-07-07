def get_todo():
    with open('todos.txt','r') as f:
        todo1=f.readlines()
    return todo1
def write_todo(todo2,b1=None):
    with open("todos.txt",'w') as f:
        if b1!=None:
            todo2.append(b1+'\n')
        f.writelines(todo2)