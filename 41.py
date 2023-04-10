# importing the module
import ast

# reading the data from the file
with open('dict.txt') as f:
    data = f.read()
    d = ast.literal_eval(data)

print(d["name"])