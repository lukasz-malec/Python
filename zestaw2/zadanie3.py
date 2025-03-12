def rzymskie_na_arabskie(rzymskie):

    roman_to_arabic_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    # wyjatki
    if not isinstance(rzymskie, str) or not rzymskie.isupper():
        raise ValueError("Niepoprawny symbol")
    

    wartosc = 0
    prev_value = 0
    repeat_count = 0
    max_repeats = {'I': 3, 'X': 3, 'C': 3, 'M': 3, 'V': 1, 'L': 1, 'D': 1}
    prev_char = ''


    # wyjątki
    for char in rzymskie:
        if char not in roman_to_arabic_map:
            raise ValueError(f"Niepoprawny symbol{char}.")
        value = roman_to_arabic_map[char]

        if char == prev_char:
            repeat_count += 1
            if repeat_count > max_repeats[char]:
                raise ValueError(f"Zbyt wiele powtórzeń symbolu '{char}' w liczbie rzymskiej.")
        else:
            repeat_count = 1
        

        # Sprawdzenie poprawności kolejności
        if prev_value and value > prev_value:
            if prev_char not in ('I', 'X', 'C') or value > prev_value * 10:
                raise ValueError(f"Nieprawidłowy zapis liczby rzymskiej: '{prev_char}{char}'.")

        # Obliczanie wyniku
        if value > prev_value:
            wartosc += value - 2 * prev_value 
        else:
            wartosc += value

        prev_value = value
        prev_char = char

    return wartosc


def arabskie_na_rzymskie(arabskie):

    if not isinstance(arabskie, int) or not (1 <= arabskie <= 3999):
        raise ValueError("Liczba musi być w zakresie 1‐3999")
    

    arabic_to_roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]


    wynik = []

    for value, numeral in arabic_to_roman_map:
        while arabskie >= value:
            wynik.append(numeral)
            arabskie -= value

    rzymskie = ''.join(wynik)

    return rzymskie



if __name__ == '__main__':
    try:
        # Przykłady konwersji rzymskiej na arabską
        rzymska = "MCMXCIV"
        print(f"Liczba rzymska {rzymska} to {rzymskie_na_arabskie(rzymska)} w arabskich.")
        
        # Przykłady konwersji arabskiej na rzymską
        arabska = 1994
        print(f"Liczba arabska {arabska} to {arabskie_na_rzymskie(arabska)} w rzymskich.")
        
    except ValueError as e:
        print(e)
