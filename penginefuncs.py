# Pengine Built-In Functions

def printText(filename):
    f = open(f"../text/{filename}", "r")
    print(f.read())

def readText(filename):
    f = open(f"../text/{filename}", "r")
    return f.read()

def displayImage(filename):
    f = open(f"../images/{filename}", "r")
    lines = f.readlines()
    for line in lines:
        print(line)

def readImage(filename):
    f = open(f"../images/{filename}", "r")
    return f.read()