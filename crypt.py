

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



def cryptic_sorter(strings: list[str]) -> list[str]:
    vowels = set("aeiou")

    def key_fn(word: str):
        lw = word.lower()
        return (len(word), lw, sum(ch in vowels for ch in lw))

    return sorted(strings, key=key_fn)


def cy(strings: list[str]) -> list[str]:
    vowels = set("aeiou")

    def key_fn(word: str):
        lw = word.lower()
        return (len(word), lw, sum(ch in vowels for ch in lw))

    return sorted(strings, key=key_fn)



#lst = ["apple","cat","Batman","dog","elephant"]
lst = ["aaa","bbb","AAA","BBB"]


res = cryptic_sorter(lst)
print(res)