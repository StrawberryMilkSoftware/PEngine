import basicfuncs as pebf
import sys
import os
 

helpstring = '''
PEngine is a text-based game engine, so commands are used to navigate the program.
Commands include (in order added):
help - Returns this help string.
exit - Closes the engine and returns to the PEngine shell.
newfile - Opens the new file wizard.
edit - Opens your default editor (editor.txt or setdefedit, default notepad) with the specified file.
read - Prints the content of a file to the screen.
'''

global currentDir
currentDir = None

def loadFromArg():
    pebf.clearScreen()
    try:
        global currentDir
        currentDir = sys.argv[1]
    except:
        print("No argument passed. Run 'pengine.py' instead.")
        sys.exit()
    print(f"Project '{currentDir}' loaded!")

def fileWizard():
    print("PEngine New File Wizard")
    filename = input("Enter a file name (no extension): ")
    filetypeoptions = ["Script", "Text", "Image"]
    filetype = pebf.createChoice(filetypeoptions, "Pick a file type")
    if filetype == "Script":
        fileext = "py"
        folder = "scripts"
        placeholder = ""
    elif filetype == "Text":
        fileext = "txt"
        folder = "text"
        placeholder = ""
    elif filetype == "Image":
        fileext = "peimg"
        folder = "images"
        placeholder = ""
    else:
        return
    pebf.createFile(f"projects/{currentDir}/assets/{folder}/{filename}.{fileext}", placeholder, False)
    
def editFile():

    file = input("Enter the file's path from /PROJECTNAME/assets/: ")

    efile = open("editor.txt", "r")
    editor = efile.read()
    os.system(f"{editor} projects/{currentDir}/assets/{file}")

def readFile():
    file = input("Enter the file's path from /PROJECTNAME/assets/: ")
    opened = open(f"projects/{currentDir}/assets/{file}")
    print(opened.read())

def handleCommand(cmd):
    if cmd == "help":
        print(helpstring)
    elif cmd == "exit":
        print("Returning to PEngine shell...")
        sys.exit()
    elif cmd == "newfile":
        fileWizard()
    elif cmd == "edit":
        editFile()
    elif cmd == "read":
        readFile()
    else:
        print(f"{cmd} is not a valid command. Try 'help' to get a list of commands.")

def startTerminal():
    print("Enter a command to get started!")
    print("'help' for help - 'exit' to exit")
    while True:
        cmd = input(" > ")
        handleCommand(cmd)

if __name__ == "__main__":
    loadFromArg()
    startTerminal()





