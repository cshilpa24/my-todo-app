FILEPATH = "todos.txt"


def get_todos(filepath='todos.txt'):
    """ The function to read file contents from a local file. 
    Each line is an individual item that is assigned to a list."""
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos, filepath='todos.txt'):
    """ The function to write list content to a local file. 
    Each line in the file is passed as a member of list."""
    with open(filepath, 'w') as file:
        file.writelines(todos)


def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {'feet':feet, 'inches':inches}


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters

if __name__ == "__main__":
    print("Hello from functions")