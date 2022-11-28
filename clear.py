import os

DEFAULT = object()

def clear(lines = DEFAULT):
        
    if lines is DEFAULT :
        os.system("cls")
        print()
        print()
        print()
    elif lines != DEFAULT:
        os.system("cls")

        [print() for i in range(lines)]
