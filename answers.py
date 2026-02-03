#question 1
import os.path


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
        with open(origin_path, "r") as file:
            content_file = file.read()
            with open(target_path, "w") as new_file:
                new_file.write(content_file)
    except:
        print("One of the paths is invalid.")

#question 4
def num_lines(path:str):
    try:
        counter = 0
        with open(path, "r") as file:
            for line in file:
                counter += 1
            return counter
    except:
        print("The path is invalid.")

#question 5
def search_word(path:str, word:str):
    try:
        counter = 0
        word = word + " " #זה נועד למנוע מצב שמילה שהיא חלק ממילה אחרת תיספר בטעות. זה פתרןן חלקי והמקסימום בלי ספריות מיוחדות
        with open(path, "r") as file:
            for line in file:
                if word in line:
                    counter += 1
            return counter
    except:
        print("The path or word is invalid.")

#question 6
def copy_from_py_to_txt(path:str):
    try:
        split_path = os.path.splitext(path)
        if split_path[1] == ".py":
            new_path = split_path[0] + ".txt"
            with open(path, "r") as file:
                content_file = file.read()
            with open(new_path, "w") as new_file:
                new_file.write(content_file)
        else:
            print("The file is not a py file")
    except:
        print("The path is invalid.")

#question 7
def replace_text(path:str, origin_string:str, target_string:str):
    try:
        with open(path, "r") as file:
            new_content = file.read()
            new_content = new_content.replace(origin_string, target_string)
        with open(path, "w") as file:
            file.write(new_content)
    except Exception as e:
        print(f"There have an error {e}")

#question 8
def add_strings_to_file(path:str, strings_list:list):
    try:
         with open(path, "a") as file:
             for string in strings_list:
                 file.write(string)
    except Exception as e:
        print(f"There have an error {e}")
