# Basic PEngine Included Functions and Imports

import os


def createChoice(options=[], prompt="Pick a number..."):
    choices = {}
    count = 1
    for o in options:
        choices[str(count)] = o
        print(f"[{str(count)}] {o}")
        count += 1
    
    num = input(f"{prompt}: ")
    try:
        return choices[num]
    except:
        print("Invalid choice")
        return

def yesNo():
    c = createChoice(["Yes", "No"])
    if c == "Yes":
        return True
    return False

def clearScreen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def delDir(dir):
    if os.name == 'nt':
        os.system(f"rd {dir} /s /q")
    else:
        os.system(f"rm -rf {dir}")

def delFile(file):
    if os.name == 'nt':
        os.system(f"del {file}")
    else:
        os.system(f"rm -rf {file}")


def createFile(file_path, placeholder="", silent=True):
    if not os.path.exists(file_path):
        with open(file_path,"a+") as f:
            if not placeholder == "":
                f.write(placeholder)
    elif not silent:
        print("File already exists.")
        