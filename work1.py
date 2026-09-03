

def check_bv(s: str, bracket_open: str, bracket_close: str) -> bool:
    i = 0
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
    if ("(" or "[" or "{") in s:
        if "(" in s:
            if check_bv(s, "(", ")"):
                ok1 = 1
        else:
            

        if "[" in s:
            if check_bv(s, "[", "]"):
                ok2 = 2
        if "{" in s:
            if check_bv(s, "{", "}"):
                ok3 = 1





    return False

print(bv("(((j[hj)))"))
