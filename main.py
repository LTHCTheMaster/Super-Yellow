from os import path
from sys import argv

variables: dict = dict()
NUMBERS: dict = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def red(cmd: list[str]):
    if len(cmd) > 1:
        var_name: str = cmd[0]
        var_value: list[int] = [NUMBERS[i] for i in cmd[1].split('|')]
        variables[var_name] = var_value
    elif len(cmd) == 1:
        variables[cmd[0]] = [0]

def green(cmd: list[str]):
    if len(cmd) > 1:
        var_name: str = cmd[0]
        var_value: bool = cmd[1] == "one"
        variables[var_name] = var_value
    elif len(cmd) == 1:
        variables[cmd[0]] = False

def blue(cmd: list[str]):
    if len(cmd) > 1:
        var_name: str = cmd[0]
        var_value: str = "".join([chr(sum([NUMBERS[i]*(10**(len(com.split("|"))-j-1)) if i != "" else 0 for j, i in enumerate(com.split("|"))])) for com in cmd[1:]])
        variables[var_name] = var_value
    elif len(cmd) == 1:
        variables[cmd[0]] = ""

def blackVar(var_name: str):
    local_var: list[int] | str | bool = variables[var_name]
    if isinstance(local_var, str):
        print(local_var, end="")
    elif isinstance(local_var, bool):
        print("one" if local_var else "zero",end="")
    else:
        print("".join([str(i) for i in local_var]),end="")

def black(cmd: list[str]):
    if len(cmd) == 1:
        if cmd[0].startswith("#"):
            blackVar(cmd[0][1:])
        else:
            com: list[str] = cmd[0].split("|")
            local_integer: int = sum([NUMBERS[i]*(10**(len(com)-j-1)) if i != "" else 0 for j, i in enumerate(com)])
            print(chr(local_integer),end="")
    else:
        if len(cmd) == 0:
            return
        for local_cmd in cmd:
            com: list[str] = local_cmd.split("|")
            local_integer: int = sum([NUMBERS[i]*(10**(len(com)-j-1)) if i != "" else 0 for j, i in enumerate(com)])
            print(chr(local_integer),end="")

def white(cmd: list[str]):
    if len(cmd) > 0:
        local_var: list[int] | str | bool = variables[cmd[0]]
        if isinstance(local_var, str):
            if len(cmd) > 1:
                black(cmd[1:])
            new_value: str = input("")
            variables[cmd[0]] = new_value
        elif isinstance(local_var, bool):
            pass
        else:
            if len(cmd) > 1:
                black(cmd[1:])
            new_value: list[int] = [int(i) for i in list(input(""))]
            variables[cmd[0]] = new_value

def compare(var_name_0: str, var_name_1: str) -> bool:
    local_var_0: list[int] | str | bool = variables[var_name_0]
    local_var_1: list[int] | str | bool = variables[var_name_1]
    if isinstance(local_var_0, bool):
        if isinstance(local_var_1, bool):
            return local_var_0 == local_var_1
        else: return False
    elif isinstance(local_var_0, str):
        if isinstance(local_var_1, str):
            return local_var_0 == local_var_1
        else: return False
    elif isinstance(local_var_0, list):
        if isinstance(local_var_1, list):
            return sum([i*(10**(len(local_var_0)-j-1)) for j, i in enumerate(local_var_0)]) == sum([i*(10**(len(local_var_1)-j-1)) for j, i in enumerate(local_var_1)])
        else: return False
    else:
        return False

def more(var_name_0: str, var_name_1: str) -> bool:
    local_var_0: list[int] | str | bool = variables[var_name_0]
    local_var_1: list[int] | str | bool = variables[var_name_1]
    if isinstance(local_var_0, list):
        if isinstance(local_var_1, list):
            return sum([i*(10**(len(local_var_0)-j-1)) for j, i in enumerate(local_var_0)]) > sum([i*(10**(len(local_var_1)-j-1)) for j, i in enumerate(local_var_1)])
        else: return False
    else:
        return False

def less(var_name_0: str, var_name_1: str) -> bool:
    local_var_0: list[int] | str | bool = variables[var_name_0]
    local_var_1: list[int] | str | bool = variables[var_name_1]
    if isinstance(local_var_0, list):
        if isinstance(local_var_1, list):
            return sum([i*(10**(len(local_var_0)-j-1)) for j, i in enumerate(local_var_0)]) < sum([i*(10**(len(local_var_1)-j-1)) for j, i in enumerate(local_var_1)])
        else: return False
    else:
        return False

def bronze(var_name_0: str, var_name_1: str):
    local_var_0: list[int] | str | bool = variables[var_name_0]
    local_var_1: list[int] | str | bool = variables[var_name_1]
    if isinstance(local_var_0, list):
        if isinstance(local_var_1, list):
            new_value: list[int] = [int(i) for i in list(str(sum([j*(10**(len(local_var_0)-k-1)) for k, j in enumerate(local_var_0)]) - sum([l*(10**(len(local_var_1)-m-1)) for m, l in enumerate(local_var_1)])))]
            variables[var_name_0] = new_value

def silver(var_name_0: str, var_name_1: str):
    local_var_0: list[int] | str | bool = variables[var_name_0]
    local_var_1: list[int] | str | bool = variables[var_name_1]
    if isinstance(local_var_0, list):
        if isinstance(local_var_1, list):
            new_value: list[int] = [int(i) for i in list(str(sum([j*(10**(len(local_var_0)-k-1)) for k, j in enumerate(local_var_0)]) + sum([l*(10**(len(local_var_1)-m-1)) for m, l in enumerate(local_var_1)])))]
            variables[var_name_0] = new_value
    elif isinstance(local_var_0, str):
        if isinstance(local_var_1, str):
            new_value: str = local_var_0 + local_var_1
            variables[var_name_0] = new_value

def gold(var_name_0: str, var_name_1: str):
    local_var_0: list[int] | str | bool = variables[var_name_0]
    local_var_1: list[int] | str | bool = variables[var_name_1]
    if isinstance(local_var_0, list):
        if isinstance(local_var_1, list):
            new_value: list[int] = [int(i) for i in list(str(sum([j*(10**(len(local_var_0)-k-1)) for k, j in enumerate(local_var_0)]) * sum([l*(10**(len(local_var_1)-m-1)) for m, l in enumerate(local_var_1)])))]
            variables[var_name_0] = new_value
    elif isinstance(local_var_0, str):
        if isinstance(local_var_1, list):
            new_value: str = local_var_0 * sum([i*(10**(len(local_var_1)-j-1)) for j, i in enumerate(local_var_1)])
            variables[var_name_0] = new_value

def purple(var_name_0: str, var_name_1: str):
    local_var_0: list[int] | str | bool = variables[var_name_0]
    local_var_1: list[int] | str | bool = variables[var_name_1]
    if isinstance(local_var_0, list):
        if isinstance(local_var_1, list):
            new_value: list[int] = [int(i) for i in list(str(sum([j*(10**(len(local_var_0)-k-1)) for k, j in enumerate(local_var_0)]) // sum([l*(10**(len(local_var_1)-m-1)) for m, l in enumerate(local_var_1)])))]
            variables[var_name_0] = new_value

def russet(var_name_0: str, var_name_1: str):
    local_var_0: list[int] | str | bool = variables[var_name_0]
    local_var_1: list[int] | str | bool = variables[var_name_1]
    if isinstance(local_var_0, list):
        if isinstance(local_var_1, list):
            new_value: list[int] = [int(i) for i in list(str(sum([j*(10**(len(local_var_0)-k-1)) for k, j in enumerate(local_var_0)]) % sum([l*(10**(len(local_var_1)-m-1)) for m, l in enumerate(local_var_1)])))]
            variables[var_name_0] = new_value

def pink(var_name_0: str, var_name_1: str):
    local_var_0: list[int] | str | bool = variables[var_name_0]
    local_var_1: list[int] | str | bool = variables[var_name_1]
    if isinstance(local_var_0, bool):
        if isinstance(local_var_1, bool):
            new_value: bool = local_var_0 and local_var_1
            variables[var_name_0] = new_value

def brown(var_name_0: str, var_name_1: str):
    local_var_0: list[int] | str | bool = variables[var_name_0]
    local_var_1: list[int] | str | bool = variables[var_name_1]
    if isinstance(local_var_0, bool):
        if isinstance(local_var_1, bool):
            new_value: bool = local_var_0 or local_var_1
            variables[var_name_0] = new_value

def orange(var_name: str):
    local_var: list[int] | str | bool = variables[var_name]
    if isinstance(local_var, bool):
        new_value: bool = not local_var
        variables[var_name] = new_value

def interpret(filepath: str):
    content: list[str] = []
    try:
        file = open(filepath, 'r', encoding='utf-8')
        content = file.read().split('\n')
        file.close()
    except:
        print("Unable to read file")
    index: int = 0
    line: str = ""
    while index < len(content) and index > -1:
        try:
            line = content[index]
            cmd: list[str] = line.split(" ")
            match cmd[0]:
                case "black":
                    black(cmd[1:])
                case "red":
                    red(cmd[1:])
                case "green":
                    green(cmd[1:])
                case "blue":
                    blue(cmd[1:])
                case "white":
                    white(cmd[1:])
                case "yellow":
                    index = int(cmd[1]) - 2
                case "magenta":
                    if compare(cmd[1], cmd[2]):
                        index = int(cmd[3]) - 2
                case "cyan":
                    if not compare(cmd[1], cmd[2]):
                        index = int(cmd[3]) - 2
                case "gray":
                    if more(cmd[1], cmd[2]):
                        index = int(cmd[3]) - 2
                case "grey":
                    if less(cmd[1], cmd[2]):
                        index = int(cmd[3]) - 2
                case "infrared":
                    print("",end="\r")
                case "ultraviolet":
                    print("")
                case "bronze":
                    bronze(cmd[1], cmd[2])
                case "silver":
                    silver(cmd[1], cmd[2])
                case "gold":
                    gold(cmd[1], cmd[2])
                case "teal":
                    variables[cmd[1]] = variables[cmd[2]]
                case "purple":
                    purple(cmd[1], cmd[2])
                case "russet":
                    russet(cmd[1], cmd[2])
                case "pink":
                    pink(cmd[1], cmd[2])
                case "brown":
                    brown(cmd[1], cmd[2])
                case "orange":
                    orange(cmd[1])
        except KeyboardInterrupt:
            raise KeyboardInterrupt()
        except:
            pass
        index += 1

def main() -> None:
    if len(argv) < 2:
        user_input_path: str = input("file: ")
        if user_input_path.endswith('.redgreen'):
            if path.exists(user_input_path):
                interpret(user_input_path)
            else:
                print("This file doesn't exist")
        else:
            print("This file extension is not usable here")
    else:
        if argv[1].endswith('.redgreen'):
            if path.exists(argv[1]):
                interpret(argv[1])
            else:
                print("This file doesn't exist")
        else:
            print("This file extension is not usable here")

if __name__ == '__main__':
    main()
