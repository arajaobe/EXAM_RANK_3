

def sorter(strings: list[str]) -> list[str]:

    #res = strings
    #for val in res:
    #    i = 1
    #    minimun = ""
    #    for val2 in res[i:]:
    #        if len(val) > len(val2):
    #            minimun = val2
    #    if minimun:
    #        val = minimun
    #    i += 1

    #return res


    return sorted(strings, key=lambda word:(len(word), word.lower(), sum(c.lower() in "aoeui" for c in word)))



tst = ["apple", "catg", "bob"]
wd = "madam im adam"
reswd = "".join(wd.split())
rs = ""
print(sorted(tst))
for w in reversed(reswd):
    rs = rs + w
wd2 = "madamimadam"
if rs == wd2:
    print(True)
print(rs)