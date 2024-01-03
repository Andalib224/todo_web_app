FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read the text file and return todos list"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Read the text file and write to-do item to the list of to-do items """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == '__main__':
    print("Hi! from Function")

