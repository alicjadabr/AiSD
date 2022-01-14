from typing import List


def sortowanie_babelkowe(l: List[int], rosnaco: bool) -> None:
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            if rosnaco:
                if l[i] > l[j]:
                    temp: int = l[i]
                    l[i] = l[j]
                    l[j] = temp
            else:
                if l[i] < l[j]:
                    temp: int = l[i]
                    l[i] = l[j]
                    l[j] = temp


li: List = [9, 2, 1, 5, 8, 0, 6, 4, 3, 7]
print(li)
sortowanie_babelkowe(li, False)
print(li)
