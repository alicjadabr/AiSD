from typing import List


def sortowanie_przez_wstawianie(l: List[int], rosnaco: bool) -> None:
    n: int = len(l)
    for i in range(1, n):
        key: int = l[i]
        j = i - 1
        if rosnaco:
            while j >= 0 and l[j] > key:
                l[j + 1] = l[j]
                j = j - 1
                l[j + 1] = key
        else:
            while j >= 0 and l[j] < key:
                l[j + 1] = l[j]
                j = j - 1
                l[j + 1] = key


li: List = [9, 2, 1, 5, 8, 0, 6, 4, 3, 7]
print(li)
sortowanie_przez_wstawianie(li, False)
print(li)
