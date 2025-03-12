def fun(n):
    # zwróć liczbę - największą przerwę
    binary = bin(n).replace("0b", "")
    result = 0
    counter = 0
    start = False

    for x in binary:
        if x == "0":
            start = True
        else:
            start = False
            if counter >= result:
                result = counter
            counter = 0

        if start:
            counter += 1
        
    return result


if __name__ == "__main__":
    N = 529 # przykladowa wartosc, oczekiwany wynik 4
    wynik = fun(N)
    print(f"Reprezentacja binarna {N}: {bin(N)}")
    print(f"fun({N}): {wynik}")

