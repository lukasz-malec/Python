import time

def pasek_postepu(dlugosc_paska):
    # Ukrycie kursora
    print("\033[?25l", end="")

    kreski = "-" * dlugosc_paska
    print(f"|{kreski}|0%", end = "", flush = True)

    print("\r", end= "", flush=True)
    time.sleep(0.5)

    for liczba in range(1,dlugosc_paska+1):
        reszta = "=" * liczba
        kreski = "-" * (dlugosc_paska - liczba)
        procent = int((liczba/dlugosc_paska) * 100)
        print(f"|{reszta}{kreski}",end="", flush= True )
        print(f"|{procent}%", end = "", flush = True)

        time.sleep(0.1)
        print("\r", end= "", flush=True)

if __name__ == "__main__":
    dlugosc_paska = 20  # długość paska
    pasek_postepu(dlugosc_paska)
