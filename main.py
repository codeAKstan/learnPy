try:
    file_name = input("Enter file name: ")
    with open(file_name, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")

