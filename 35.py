my_file = open("my_file.txt")
for line in my_file.readlines():
    print(line)

def appendName():
    name = input("enter name: ")
    names = open("names.txt", 'a+')
    names.write(f"{name}\n")

def readNames():
    names = open("names.txt")
    for line in my_file.readlines():
        print(line)

appendName()
readNames()