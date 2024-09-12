file = open("./input10.txt").readlines()


def isClose(token):
    return token in [")", "]", "}", ">"]


def invertChar(token):
    if token == "{":
        return "}"
    elif token == "[":
        return "]"
    elif token == "<":
        return ">"
    elif token == "(":
        return ")"
    else:
        return "+"


def_lines = []
ans = 0
ans_key = {")": 3, "}": 1197, "]": 57, ">": 25137}
for line in file:
    line = line.strip()
    stack = []
    t = 0
    is_def = False
    for char in line:
        if len(stack) > 0:
            if invertChar(stack[-1]) == char:
                stack.pop(-1)
            else:
                if isClose(char):
                    if not is_def:
                        ans += ans_key[char]
                    is_def = True
                stack.append(char)
        else:
            stack.append(char)
        t += 1
    if is_def:
        def_lines.append(line)
print(ans)
