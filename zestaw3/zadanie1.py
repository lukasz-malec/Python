import json
import re

def process_tram_data(input_file):
    # Wczytaj dane z pliku JSON input_file
    with open(input_file, "r", encoding="utf-8") as read_file:
        data = json.load(read_file)

    
    # Przekształć dane na format słownikowy


    # trams - zawartość do zapisu w pliku 'tramwaje_out.json'
    # line_stop_counts - lista krotek (linia, liczba przystanków)
    # all_stops - set ze wszystkich przystanków

    trams = {}
    all_stops = set()

    for tram in data['tramwaje']:
        line = int(tram['linia'])  
        stops = []
        
        for stop in tram['przystanek']:
            stop_name = re.sub(r' \d+$', '', stop['nazwa'])  # usunięcie końcówek 
            stops.append(stop_name)
            all_stops.add(stop_name)          # dodanie do zbioru przystnakow
        
        
        trams[line] = tuple(stops)
    

    # Posortowanie linii według liczby przystanków
    line_stop_counts = sorted(
        [(line, len(stops)) for line, stops in trams.items()],
        key=lambda x: x[1],
        reverse=True
    )

    
    return trams, line_stop_counts, len(all_stops)




if __name__ == '__main__':
    # Wywołanie funkcji
    trams, line_stop_counts, unique_stop_count = process_tram_data('tramwaje.json')

    # Zapisz dane do nowego pliku JSON 'tramwaje_out.json'
    with open('tramwaje_out.json', "w", encoding="utf-8") as file:
        json.dump(trams, file, ensure_ascii=False)


    # Wypisz wyniki: linia - liczba przystanków (po tym posortowane od największego) 
    # Wypisz wyniki: liczba wszystkich unikanych przystanków

    # print("Linia - Liczba przystanków:")
    for line, count in line_stop_counts:
        print(f"{line} - {count}")
    
    print(unique_stop_count)