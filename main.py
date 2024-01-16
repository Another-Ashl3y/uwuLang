import sys

variables = {
    "__config__":{
        "type":"string",
        "value":"hello world",
        "constant":True
    }
}

keywords = {
    "string_type" : "uwu",
    "int_type" : ":3",
    "mut_var" : "qwq",
    "const_var" : "owo",
    "set_operator" : "=",
}

openers = {
    "string_opener":"\""
}

def add_variable(name : str, t : str, value, constant : bool):
    variables[name] = {
        "type":t,
        "value":value,
        "constant":constant
    }


def get1st(x):
    return x[1]
def begin():
    arguments = sys.argv
    arguments.pop(0)
    if len(arguments) > 0:
        execution_file = arguments[0]
    else:
        print("Thank you for using the dumb language")
        print("Your so dumb you didnt enter a file")
        execution_file = input("Enter one here -> ")

    add_variable("__main__","string",execution_file,True)

    with open(execution_file,"r") as f:
        code = f.read()

    code = code.replace("\n", "")
    lines = code.split(";")
    return lines

def join(x: list, y:str):
    q = ""
    for i in x:
        q += i + y
    return q[0:-1]


def do(instructions):
    for i in instructions:
        parts = i.split(" ")
        if parts[0] == keywords["string_type"]:
            constant = parts[1] == keywords["const_var"]
            variable_name = parts[2]
            value = join(parts[3:None]," ")
            add_variable(variable_name, "string", value, constant)

do(begin())

