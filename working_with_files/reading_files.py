# Opening a file
file = open('test_data.txt', 'r')

# Read all the lines as a list, each line is an item
print(file.readlines())

# Read one line, move cursor to the next one
#print(file.readline())

# Read all content
#print(file.read())

# Closing the file
file.close()

# Using with notation: file is accessible only within with instruction and it automatically closes the file
with open('test_data.txt', 'r') as file:
    content = file.read()
    print(content)
