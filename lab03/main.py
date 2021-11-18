from typing import List

# Zad.1. Zaimplementować funkcję numbers(n: int), która wypisze liczby od n do 0
def numbers(n: int) -> None:
    if n<0:
        return
    print(f'n: {n}')

    numbers(n - 1)

numbers(20)

# Zad.2. Zaimplementować funkcję fib(n: int) -> int, która obliczy n-ty wyraz ciągu Fibonacciego
def fib(n: int) -> int:
    if n<0:
        pass
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fibo = fib(n-2) + fib(n-1)
        return fibo

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))

#Zad.3. Zaimplementować funkcję power(number: int, n: int) -> int, której zadaniem jest zwrócenie wyniku
# działania $ number^n $ NIE UŻYWAĆ OPERATORA **
def power(number: int, n: int) -> int:
    if n == 0:
        return 1
    elif n == 1:
        return number
    elif n == 2:
        return number * number
    else:
        x = power(number, n-1)
        return number * x

print(power(5, 2))
print(power(5, 3))
print(power(4, 3))


# Zad.4 Zaimplementować funkcję reverse(txt: str) -> str, która zwróci odwrócony ciąg znaków przekazany w parametrze txt
def reverse(txt: str) -> str:
    if len(txt) == 0:
        return txt
    else:
        return reverse(txt[1:]) + txt[0]


print(reverse('myszka'))

# Zad.5. Zaimplementować funkcję factorial(n: int) -> int, która zwróci silnię wartości przekazanej w parametrze
def factorial(n: int) -> int:
    res: int = 1
    if n<0:
        pass
    elif n == 0 or n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        return res

print(factorial(3))

# Zad.6. Zaimplementować funkcję prime(n: int) -> bool, która sprawdzi, czy liczba podana w parametrze jest liczbą
# pierwszą. Podpowiedź: wystarczy sprawdzić czy n jest podzielne przez wszystkie liczby poprzedzające


# Zad.9. Zaimplementować funkcję remove_duplicates(txt: str) -> str, która zwróci wartość parametru txt pozbawioną
# sąsiadujących duplikujących się znaków. Przykład: XXYZZZ -> XYZ

def remove_duplicates(txt: str) -> str:
    if not txt:
        return ""
    elif len(txt) == 1:
        return txt
    elif txt[1] == txt[0]:
        return remove_duplicates(txt[1:])
    return txt[0] + remove_duplicates(txt[1:])

print(remove_duplicates('XXYZZZ'))

# Zad.10. Zaimplementować funkcję balanced_parentheses(n: int) -> str, która zwróci ciąg znaków o długości n
# zawierający wszystkie możliwe kombinacje ułożenia nawiasów. Przykład dla n = 4








