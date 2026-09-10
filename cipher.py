
def cipher(text: str, shift: int) -> str:
    result = []

    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            newchar = chr((ord(ch) - base + shift) % 26 + base)
            result.append(newchar)
        else:
            result.append(ch)

    return "".join(result)


print(cipher("hello", 3))

# base = ord('A') if ch.isupper() else ord('a')
# new_char = chr((ord(ch) - base + shift) % 26 + base)