
def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    if not isinstance(number, str) or not isinstance(from_base, int) or not isinstance(to_base, int):
        return "ERROR"

    if from_base < 2 or from_base > 36 or to_base < 2 or to_base > 36:
        return "ERROR"

    s = number.strip()
    if s == "":
        return "ERROR"

    try:
        value = int(s, from_base)
    except ValueError:
        return "ERROR"

    if value == 0:
        return "0"

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    neg = value < 0

    n = -value if neg else value

    out = []

    while n:
        out.append(digits[n % to_base])
        n //= to_base
        #n =  n // to_base

    if neg:
        out.append("-")

    return "".join(reversed(out))



def number_base(number: str, from_base: int, to_base: int) -> str:
    if not isinstance(number, str) or not isinstance(from_base, int) or not isinstance(to_base, int):
        return "ERROR"

    if from_base < 2 or from_base > 36 or to_base < 2 or to_base > 36:
        return "ERROR"

    s = number.strip()
    if s == "":
        return "ERROR"

    try:
        value = int(s, from_base)
    except ValueError:
        return "ERROR"

    if value == 0:
        return "0"

    neg = value < 0

    n = - value if neg else value

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    out = []
    while n:
        out.append(digits[n % to_base])
        n //= to_base

    if neg:
        out.append("-")

    return "".join(reversed(out))




res = number_base_converter("123", 1, 10)

print(res)




