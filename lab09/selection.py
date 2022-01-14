from typing import List


def sortowanie_przez_wybieranie(l: List[int], rosnaco: bool) -> None:
    for i in range(len(l) - 1):
        extr_index: int = i
        for j in range(i + 1, len(l)):
            if rosnaco:
                if l[j] < l[extr_index]:
                    extr_index = j
            else:
                if l[j] > l[extr_index]:
                    extr_index = j

        temp: int = l[i]
        l[i] = l[extr_index]
        l[extr_index] = temp


li: List = [9, 2, 1, 5, 8, 0, 6, 4, 3, 7]
print(li)
sortowanie_przez_wybieranie(li, True)
print(li)
