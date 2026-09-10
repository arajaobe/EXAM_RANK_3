
def echo_validator(text: str) -> bool:
    copy_text = text
    rev = ""

    modified = "".join(copy_text.split()).lower()
    for w in reversed(modified):
        rev = rev + w

    if not text:
        return False

    if rev == "".join(text.split()).lower():
        return True
    return False


def ech_val(text: str) -> bool:
    copy_text = ""

    if not text:
        return False

    for w in text:
        if w.isalpha():
            copy_text = copy_text + w.lower()

    return copy_text == copy_text[::-1]


def e_v(text:str) -> bool:
    modified = "".join(text.split()).lower()

    if not modified:
        return False

    return text == modified[::-1]



#wd = " Ma dam    iM    adam "
#reswd = "".join(wd.split()).lower()
#rs = ""
#for w in reversed(reswd):
#    rs = rs + w
#wd2 = "maDamimadam".lower()
#if rs == wd2:
#    print(True)
#print(rs)

print(ech_val("race0car"))

print(echo_validator("race0car"))

print(e_v("  "))


