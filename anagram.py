
def anagram(s1: str, s2: str) -> bool:

    new_txt1 = "".join(s1.split()).lower()

    new_txt2 = "".join(s2.split()).lower()


    if len(new_txt1) != len(new_txt2):
        return False

    for w in new_txt1:
        counter = new_txt1.count(w)
        counter2 = new_txt2.count(w)
        if counter != counter2:
            return False

    return True




# anagram("listen", "silent")

def ana(s1: str, s2: str) -> bool:
    nt1 = sorted(s1.replace(" ", "").lower())
    nt1 = sorted(s1.lower().replace(" ", ""))

    nt2 = sorted(s2.replace(" ", "").lower())

    return nt1 == nt2


print(ana("kDormitory", "Dirty RooKm"))