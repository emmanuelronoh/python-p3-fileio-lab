def write_file(file_path, content):
    """Write content to a file, creating the file if it does not exist."""
    with open(f'{file_path}.txt', 'w') as f:
        f.write(content)

def append_file(file_path, content):
    """Append content to a file, creating the file if it does not exist."""
    with open(f'{file_path}.txt', 'a') as f:
        f.write(content)

def read_file(file_path):
    """Read content from a file."""
    with open(f'{file_path}.txt', 'r') as f:
        return f.read()

