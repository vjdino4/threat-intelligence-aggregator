def load_file(path):
    with open(path, "r") as file:
        data = file.read()
    return data
