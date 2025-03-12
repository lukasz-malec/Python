import string
import re
from collections import Counter

def liczbaSlow(tekst):
    znaki_specjalne = list(string.whitespace) + list(string.punctuation)

    # zamiana znaków przystankowyc na spacje
    for x in znaki_specjalne:
        tekst = tekst.replace(x, " ")    

    # zamiana ciagu cyfr na spacje
    tekst = re.sub(r"\d+", " ", tekst)
    tablica = list(tekst.split(" "))


    licznik_slow = 0
    for y in tablica:
        element = str(y)
        if element.isalpha():
            licznik_slow += 1
    
    return licznik_slow



def liczbaLiter(tekst):
    znaki_specjalne = list(string.whitespace) + list(string.punctuation)

    # usuwanie znaków przystankowych 
    for x in znaki_specjalne:
        tekst = tekst.replace(x, " ") 

    licznik_liter = 0
    for y in tekst:
        element = str(y)
        if element.isalpha():
            licznik_liter += 1

    return licznik_liter
    

def liczbaCyfr(tekst):
    znaki_specjalne = list(string.whitespace) + list(string.punctuation)

    # usuwanie znaków przystankowych 
    for x in znaki_specjalne:
        tekst = tekst.replace(x, " ") 

    licznik_cyfr = 0
    for y in tekst:
        element = str(y)
        if element.isnumeric():
            licznik_cyfr += 1
    return licznik_cyfr


def MyCounter(tekst):
    znaki_specjalne = list(string.whitespace) + list(string.punctuation)

    # usuwanie znaków przystankowych 
    for x in znaki_specjalne:
        tekst = tekst.replace(x, "")
    
    litery = [char for char in tekst if char.isalpha()]
    cyfry = [char for char in tekst if char.isdigit()]


    litery.sort()
    cyfry.sort()

    # Łączenie posortowanych liter i cyfr
    tekst = "".join(litery) + "".join(cyfry)

    tekst = str(tekst).lower()
    licznik = Counter(tekst)

    return licznik


def statystyka_lancucha(tekst):
    # dostosu tak, aby instrukcja return była ok
    liczba_slow = liczbaSlow(tekst)
    liczba_liter = liczbaLiter(tekst)
    liczba_cyfr = liczbaCyfr(tekst)
    statystyka_posortowana = MyCounter(tekst)

    return {
        "liczba_slow": liczba_slow, # liczba
        "liczba_liter": liczba_liter, # liczba
        "liczba_cyfr": liczba_cyfr, # liczba
        "statystyka": statystyka_posortowana # słownik typu 'a': 1, '2': 3
    }

# Przykładowe użycie
if __name__ == "__main__":
    tekst_wejsciowy = "Ala ma 3 koty i 2 psy"
    wynik = statystyka_lancucha(tekst_wejsciowy)
    
    # Wyświetlanie wyników
    print("Liczba słów:", wynik["liczba_slow"])
    print("Liczba liter:", wynik["liczba_liter"])
    print("Liczba cyfr:", wynik["liczba_cyfr"])
    print("Statystyka częstości występowania:")
    for znak, liczba in wynik["statystyka"].items():
        print(f"'{znak}': {liczba}", end=" ")
