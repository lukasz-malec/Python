import sys

# Funkcja do rozkładania liczby na czynniki pierwsze i formatowania wyniku
def rozklad_na_czynniki(n):
    # zwrócić sformatowany ciąg, np. "2^3*3^4*5^2"
    k = 2
    czynniki = []

    # rozkład na czynniki
    while n > 1:
        while n % k == 0:
            czynniki.append(k)
            n = n // k
        k += 1
    
    # formatowanie wyniku
    czynniki_str = [str(x) for x in czynniki]
    zbior = sorted(set(czynniki_str), key=int)

    results = [f"{x}^{czynniki_str.count(x)}" if czynniki_str.count(x) != 1 else x for x in zbior]
    final_results = "*".join(results)
    
    return final_results

# Główna funkcja programu
if __name__ == "__main__":
    argv = sys.argv[1:]  # Pobieranie argumentów zewnętrznych (liczby)

    for arg in argv:
        liczba = int(arg)
        wynik = rozklad_na_czynniki(liczba)
        print(f"{liczba} = {wynik}")
