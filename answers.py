#question 1
def print_file(path:str):
    try:
        with open(path,"r") as file:
            print(file.read())
    except:
        print("The path is invalid.")

#question 2
def write_file(path:str, string:str):
    try:
        with open(path,"w") as file:
            file.write(string)
    except:
        print("The path or the string is invalid.")
#question 3
def copy_file_content(origin_path:str, target_path:str):
    try:
        with open(target_path, "w") as file:
            file.write(origin_path)
    except:
        print("One of the paths is invalid.")
