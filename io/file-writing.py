import sys

file_name = "test.txt"

def read_write_to_file(file):
    
    file_text = file.readlines()
    
    print("File text read is ", file_text, "text")
    
    if(file_text == " "):
        file.write(file_text)
    else:
        file_text = "test\n"
        file.write(file_text)    
    file.close()

    print("Printed ", file_text, "to file", file_name, end='')
    print("Exiting...")

print("Trying to open the file", file_name, "...")

try:
    with open(file_name, mode='a+') as file:
        read_write_to_file(file)
except IOError:
    print("There was an error openning the file ", file_name)
    sys.exit()
