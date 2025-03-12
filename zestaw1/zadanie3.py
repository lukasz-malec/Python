import time
from datetime import datetime

def wyswietl_zegar():
    poczatek = chr(16)
    koniec = chr(17)

    # ukrycie kursora
    print("\033[?25l", end="", flush=True)

    try:
        while True:
            x = datetime.datetime.now()
            second = x.second
            minute = x.minute
            hour = x.hour
            print(f"{poczatek}  {hour:02}:{minute:02}:{second:02}  {koniec}", end="", flush=True)
            time.sleep(0.5)
            print("\r", end="", flush=True)


    except KeyboardInterrupt:
        print("\033[?25h", end="", flush=True)

if __name__ == "__main__":
    wyswietl_zegar()
