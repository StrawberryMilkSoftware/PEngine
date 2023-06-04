# PEngine by Strawberry Milk Software

import basicfuncs as pebf # Import PEngine basic functions (basicfuncs.py)
import sys
import os


logo = '''
                                python3
  _____  ______             _    pengine.py        
 |  __ \\|  ____|           (_)           
 | |__) | |__   _ __   __ _ _ _ __   ___ 
 |  ___/|  __| | '_ \\ / _` | | '_ \\ / _ \\
 | |    | |____| | | | (_| | | | | |  __/
 |_|    |______|_| |_|\\__, |_|_| |_|\\___|
                       __/ |             
                      |___/     
                Strawberry Milk Software                
'''

helpstring = '''
PEngine is a text-based game engine, so commands are used to navigate the program.
Commands include (in order added):
help - Returns this help string.
exit - Closes PEngine.
newproject - Opens the new project wizard.
loadproject - Loads projects you've created.
delproject - Deletes projects you've created.
setdefedit - Sets the default code editor to use when editing scripts, text, and images.

'''

def loadEngine():
    os.system("title PEngine")

def NPWizard():
    print("PEngine New Project Wizard")
    projname = input("Enter a project name: ")
    projpath = os.path.dirname(__file__) + "/projects/" + projname
    print("Creating project...")
    mkdir = os.system(f"mkdir \"{projpath}\"")
    if mkdir == 1:
        print("Error creating project!")
        return
    os.system(f"mkdir \"{projpath}/assets\"")
    os.system(f"mkdir \"{projpath}/assets/scripts\"")
    os.system(f"mkdir \"{projpath}/assets/text\"")
    os.system(f"mkdir \"{projpath}/assets/images")
    pebf.createFile(f"{projpath}/assets/scripts/main.py", "# This will be run when opening your project in a package", True)
    pebf.createFile(f"{projpath}/assets/include.pengine", "scripts/main.py", True)
    pfFile = open("penginefuncs.py", "r")
    pf = pfFile.read()
    pebf.createFile(f"{projpath}/assets/scripts/penginefuncs.py", pf, True)
    print("Project created successfully!")
    

def loadProject():
    projects = next(os.walk(os.path.dirname(__file__) + '/projects'))[1]
    print("All projects:")
    projectsd = {}
    count = 1
    for p in projects:
        projectsd[str(count)] = p
        print(f"[{str(count)}] {p}")
        count += 1
    
    projnum = input("Enter a project number to load: ")
    try:
        project = projectsd[projnum]
    except:
        print("Invalid number!")
        return
    os.system(f"python3 {os.path.dirname(__file__)}/mainEngine.py {project}")

def deleteProject():
    projects = next(os.walk(os.path.dirname(__file__) + '/projects'))[1]
    project = pebf.createChoice(projects, "Choose a project to delete")
    print(f"Are you sure you want to delete {project}?")
    delconfirm = pebf.yesNo()
    if delconfirm:
        print(f"Deleting {project}...")
        pebf.delDir(f"\"{os.path.dirname(__file__)}/projects/{project}\"")
        print(f"Project deleted.")
    

def setDefaultEditor():
    editor = input("Enter a command to choose an editor: ")
    f = open("editor.txt", "w")
    f.write(editor)

def handleCommand(cmd):
    if cmd == "help":
        print(helpstring)
    elif cmd == "exit":
        print("Thanks for using PEngine!")
        sys.exit()
    elif cmd == "newproject":
        NPWizard()
    elif cmd == "loadproject":
        loadProject()
    elif cmd == "delproject":
        deleteProject()
    elif cmd == "setdefedit":
        setDefaultEditor()

    
    else:
        print(f"{cmd} is not a valid command. Try 'help' to get a list of commands.")

def start():
    print(logo)
    print("Loading PEngine...")
    loadEngine()
    pebf.clearScreen()
    print(logo)
    print("Welcome to PEngine!")
    print("Enter a command to get started!")
    print("'help' for help - 'exit' to exit")
    while(True):
        cmd = input(" > ")
        handleCommand(cmd)


if __name__ == "__main__":
    start()
