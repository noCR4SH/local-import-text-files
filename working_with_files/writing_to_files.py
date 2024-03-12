# opening file
file = open('test.txt', 'w')

# Writing into file
file.write("Hello World!\n")

lines_to_write = ["First Line\n", "Second Line\n", "Third Line"]

# Writing lines into file
file.writelines(lines_to_write)

file.close()

# using with
with open('with_test.txt', 'w') as file:
    file.writelines(lines_to_write)