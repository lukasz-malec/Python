def dodaj_element(wejscie):
    # może warto zdefiniować zagnieżdżoną funkcję

    # szukanie najbardziej zagnieżdzonych elementów taplicy
    # listy, krotki oraz slowniki

    def depth(wejscie,poziom ,wynik):
        if isinstance(wejscie, list):
    
            if poziom > wynik[0]:  # Znaleziono nowy głębszy poziom
                wynik[0] = poziom
                wynik[1] = [wejscie]
            elif poziom == wynik[0]:  # Poziom taki sam, dodaj listę
                wynik[1].append(wejscie)
            for element in wejscie:
                depth(element, poziom + 1, wynik)

        elif isinstance(wejscie, (tuple, set)):
            for element in wejscie:
                depth(element, poziom + 1, wynik)

        elif isinstance(wejscie, dict):
            for wartość in wejscie.values():
                depth(wartość, poziom + 1, wynik)


    wynik = [0, []]  # maksymalny poziom, listy na tym poziomie
    poziom = 0
    depth(wejscie, poziom, wynik)

    # Dodanie elementów
    for lista in wynik[1]:
        if lista:  # lista jet  nie pusta
            ostatni_element = lista[-1]
            if isinstance(ostatni_element, int):  
                lista.append(ostatni_element + 1)
            else: 
                lista.append(1)
        else:  #  lista jest pusta
            lista.append(1)

    return wejscie




if __name__ == '__main__':
    input_list = [
     1, 2, [3, 4, [5, {"klucz": [5, 6], "tekst": [1, 2]}], 5],
     "hello", 3, [4, 5], 5, (6, (1, [7, 8]))
    ]
    output_list = dodaj_element(input_list)
    print(input_list)   