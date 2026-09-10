
def inter(s1: str, s2: str) -> str:
    new_txt = ""
    already = ""

    for c1 in s1:
        for c2 in s2:
            if c1 == c2:
                if c1 in already:
                    break
                else:
                    new_txt = new_txt + c2

                already = already + c2

    return new_txt



# inter("hello", "world")   -> "lo"

new = inter("xyz", "abc")

print(new)