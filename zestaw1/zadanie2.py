def rysuj_miarke(dlugosc):
    pelna_miarka = ""
    text = ("|...." * dlugosc) + "|"
    pelna_miarka += text + "\n" + "0"
    
    # Rysowanie numerów na miarce
    for i in range(dlugosc):
        if i < 9:
            pelna_miarka += "    " + str(i + 1)
        elif i < 99:
            pelna_miarka += "   " + str(i + 1)
        else:
            pelna_miarka += "  " + str(i + 1)

    # TODO: Zaimplementuj rysowanie miarki
    return pelna_miarka  # Zwracanie wyniku jako string

def main():
    dlugosc_miarki = 123  # Możesz zmienić długość miarki
    miarka = rysuj_miarke(dlugosc_miarki)
    print(miarka)

if __name__ == "__main__":
    main()
    