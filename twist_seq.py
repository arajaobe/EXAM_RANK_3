
def twist_sequence(arr: list[int], k: int) -> list[int]:
    n = len(arr)

    if n == 0:
        return []

    k %= n

    if k == 0:
        return arr.copy()

    return arr[-k:] + arr[:-k]


print(twist_sequence([1,2,3,4,5], 2))