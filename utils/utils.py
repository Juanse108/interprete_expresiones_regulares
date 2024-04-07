import os


def WriteToFile(filename, source):
    # Check if directory exists, create it if not
    directory = os.path.dirname(filename)
    if not os.path.exists(directory):
        os.makedirs(directory)  # Create all necessary subdirectories

    with open(filename, 'w') as _file:
        _file.write(source)