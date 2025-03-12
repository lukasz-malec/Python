import os
import time

def wyczysc_ekran():
    # Czyszczenie ekranu w zależności od systemu operacyjnego
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Unix/Linux/Mac


def przesun_tekst_w_pionie(tekst, wysokosc_okna, opoznienie=0.1):
    pozycja = 1
    kierunek = 1
    # ukrycie kursora
    print("\033[?25l", end="", flush=True)
    try:
        while True:

            wyczysc_ekran()
            print("\n" * pozycja + tekst)
            
            pozycja += kierunek

            # Odbijanie się od krawędzi
            if pozycja == wysokosc_okna: 
                kierunek = -1
            elif pozycja == 0: 
                kierunek = 1

            time.sleep(opoznienie)
    except KeyboardInterrupt:
        print("\033[?25h", end="", flush=True)


if __name__ == "__main__":
    tekst = "  Hello world!  "  # tekst do przesuwania
    wysokosc_okna = 20  # Wysokość "okna" terminala
    przesun_tekst_w_pionie(tekst, wysokosc_okna)
