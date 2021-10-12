# Przygotować funkcję, która przyjmie w parametrach pierwszą literę imienia,
#  oraz nazwisko, a następnie zwróci te wartości połączone kropką. Przykładowe wyjście: J. Kowalski.
'''
def foo1(l, naz):
    print(f'{l}.{naz}')

foo1("A", "Kowalski")
'''
# Przygotować funkcję, która przyjmie w parametrach imię i nazwisko, oraz zwróci pierwszą literę imienia i nazwisko połączone kropką.
#  Funkcja powinna również dbać o poprawność wielkich liter. Przykładowo, wejście: (jan, kowalski), wyjście: J. Kowalski.
'''
def foo2(l, naz):
    print(f'{l.title()}.{naz.title()}')

foo2("m", "kot")
'''

#Przygotować funkcję, która przyjmie 3 argumenty: 2 pierwsze cyfry aktualnego roku,
# 2 ostatnie cyfry aktualnego roku, wiek użytkownika, a następnie zwróci jego rok urodzenia.
'''
def foo3(a1, a2, wiek):
    rok = a1 + a2
    print(rok)
    r2 = int(rok)
    ur = r2 - wiek
    print(f'Rok urodzenia: {ur}')

foo3("20", "20", 20)
'''
# Przygotować funkcję, która przyjmie 3 parametry: imię, nazwisko i funkcję przetwarzającą te dane,
# a następnie zwróci wynik działania funkcji przyjętej w 3. parametrze.
# Przykładwo, wejście: (jan, kowalski, funkcja_z_zadania_2), wyjście: J. Kowalski.
'''
def foo4(im, naz, foo2):
    foo2(im, naz)

foo4('k', 'nowak', foo2)
'''
# Przygotować funkcję, która przyjmie 2 argumenty, a następnie zwróci wynik ich dzielenia.
# Należy sprawdzić w jednej instrukcji if (bez użycia elif i else), czy obydwie liczby są dodatnie
# oraz czy druga liczba jest różna od 0.
'''
def foo5(a, b):
    res = a / b
    if a > 0 and b > 0:
        return res

print(foo5(10, 2))
print(foo5(13, 2))
'''
# Przygotować skrypt, w którym użytkownik będzie podawał kolejne liczby w pętli,
# dopóki suma wszystkich podanych do tej pory liczb nie osiągnie wartości 100.
''' 
def foo6():
    sum = 0
    while True:
        liczba = int(input("Podaj kolejna liczbe: "))
        sum += liczba
        if sum >= 100:
            break

foo6()
'''
# Przygotować funkcję, która przyjmie 1 argument w postaci listy, a następnie zwróci te elementy w postaci krotki.
'''
def foo7(li):
    return tuple(li)

l1 = ['cat', 'mouse', 'bird']
print(l1)
print(foo7(l1))
'''
# Przygotować skrypt, w którym użytkownik będzie wprowadzał do listy wartości używając pętli,
# a następnie wartości z tej zostanią zrzutowane do krotki.
''' 
def foo8():
    li = []
    for i in range(6):
        number = int(input('Podaj kolejne wartosci do listy: '))
        li.append(number)
    li = tuple(li)
    return li

print(foo8())
'''
# Przygotować funkcję, która przyjmie 1 argument całkowitoliczbowy, a następnie zwróci nazwę dnia tygodnia odpowiadającą
# przekazanemu argumentowi. Nie należy w tym zadaniu używać instrukcji warunkowych! Przykładowo, wejście: 6, wyjście: sobota.
''' 
def foo9(x):
    dni = ['poniedzialek', 'wtorek', 'sroda', 'czwartek', 'piatek', 'sobota', 'niedziela']
    print(dni[x-1])

foo9(1)
foo9(3)
foo9(7)
'''
# Przygotować funkcję, która przyjmie argument w postaci łańcucha znaków, a następnie zwróci wartość logiczną
# informującą o tym czy przekazany tekst jest palindromem.
'''

def foo10(arg):
    tekst = arg.lower().replace(' ', '')
    for i in range(1, len(tekst)):
        if tekst[i] != tekst[-(i+1)]:
            return False
            break
        else:
            continue
    return True

print(foo10('Drukarka'))
print(foo10('KaJaK'))
print(foo10('Akta generała ma mała renegatka'))






