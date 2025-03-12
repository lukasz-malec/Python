import tkinter as tk
from tkinter import Label, StringVar
from datetime import datetime
from tkcalendar import Calendar  # pip install tkcalendar

okno = tk.Tk()
# tytuł, rozmiar, blokada wielkości
okno.title("Zegar i Kalendarz")
okno.resizable(False, False)
okno.geometry("400x400")

# utwórz StringVar()

okno.label_text = tk.StringVar()

def update_date_time():
	# dzien = i tak dalej... miesiac, rok, czas, dzien
	# czytamy datetime.today().strftime('%A')
	# kody https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
	
	dzien_tygodnia = datetime.today().strftime('%A')
	dzien = datetime.today().strftime('%d')
	miesiac = datetime.today().strftime('%B')
	rok = datetime.today().strftime('%Y')
	czas = datetime.today().strftime('%X')

	dt = f"{dzien_tygodnia}, {dzien} {miesiac} {rok} \n {czas}" 
	# dt = dzien + ... + "\n" + ...

	# ustaw za pomocą .set dt dla StringVar zrobinego powyżej
	# ważne: rekurencyjne odświeżanie etykiety - patrz poniżej


	okno.label_text.set(dt)
	date_time.after(1000, update_date_time)

# widget Label ustawiony na StringVar zrobiony na początku, rozmiar, czcionki, tło - wg uznania 
# date_time = Label(...
date_time = tk.Label(okno,textvar = okno.label_text, background="black", foreground="white", font = ("Arial", 20))
date_time.pack(anchor="center", fill=tk.BOTH, ipady = 40)

current_time = datetime.now()
# przyda się do kalendarza
# day = odczytaj przez .strftime('%d')
# month = 
# year = 

# utwórz cal = Calendar(...
# wstaw przez .pack poniżej zegara

day = datetime.today().strftime('%d')
month = datetime.today().strftime('%m') 
year = datetime.today().strftime('%Y')
cal = Calendar(okno, selectmode='day', year=int(year), month=int(month), day=int(day))

cal.pack(fill = tk.BOTH, padx = 40, pady = 40)
update_date_time()

okno.mainloop()