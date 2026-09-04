

def check_bv(s: str, bracket_open: str) -> bool:
    i = 0

    if bracket_open == "(":
        bracket_close = ")"
    elif bracket_open == "[":
        bracket_close = "]"
    elif bracket_open == "{":
        bracket_close = "}"

    for char in s:
        if char == bracket_open:
            i += 1
    if bracket_close not in s:
        return False
    else:
        j = 0
        for char in s:
            if char == bracket_close:
                j += 1
    if i != j:
        return False
    else:
        return True



def bv(s: str) -> bool:
    stack = []
    mapping = {")" : "(",
               "]" : "[",
               "}" : "{"
               }
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False

    return True


def bracket_validator(s: str) -> bool:
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack[-1] != pairs[ch]: # ([)]
                return False
            stack.pop()
    return not stack



#def bv(s: str) -> bool:
#    if ("(" or "[" or "{") in s:
#        char = "([{"
#        tmp = 1

#        for c in char:
#            res = 0
#            op = 0
#            if c in s:
#                res = 1
#                if check_bv(s, c):
#                    op = 1
#            if res and not op:
#                tmp = 0

#        if not tmp:
#            return False
#        else:
#            return True

#    return True



print(bracket_validator("("))
