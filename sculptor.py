
def string_sculptor(text: str) -> str:
    toggle = 0

    res = []
    for ch in text:
        if ch == " ":
            res.append(ch)
            toggle = 0
            continue
        if ch.isalpha():
            if toggle == 0:
                res.append(ch.lower())
                toggle = 1
            else:
                res.append(ch.upper())
                toggle = 0
        else:
            res.append(ch)
    print(res)
    return "".join(res)

print(string_sculptor("aaaa aaaaaa 256 aa58"))