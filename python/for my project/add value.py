def format_file(filename):
    # Open the file for reading
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Modify each non-empty line by adding '@' to the beginning
    formatted_lines = ['@' + line.strip() if line.strip() else '' for line in lines]

    # Open the file for writing
    with open(filename, 'w') as file:
        file.write('\n'.join(formatted_lines))

# Example usage:
filename = 'fff.txt'  # Replace 'example.txt' with your file name
format_file(filename)