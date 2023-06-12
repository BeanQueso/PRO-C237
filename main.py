import os

def change_file_name(path, new_name):
    directory, old_name = os.path.split(path)
    new_path = os.path.join(directory, new_name)
    os.rename(path, new_path)
    print(f"The file name has been changed to: {new_name}")
file_path = input("Enter the file path: ")
new_file_name = input("Enter the new file name: ")

change_file_name(file_path, new_file_name)
