import sys

if (sys.platform == "win32"):
    print("Hello Windows User!")
    print("Type something, please ", end='')
    testInput = input()
    print("You typed: " + testInput, end='\n')
else:
    print("error")