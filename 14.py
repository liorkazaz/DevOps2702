def get5input():
    aa = [input('age') for i in range(5)]
    return max(aa)


age = get5input()
print(age)


def getMoshe():
    listOfNames = []

    while True:
        name = input('name')
        if name == "moshe":
            break
        listOfNames.append(name)
    return listOfNames


print(getMoshe())
