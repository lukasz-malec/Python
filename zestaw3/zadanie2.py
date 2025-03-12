import yfinance as yf
import pandas as pd
import numpy as np

def find_crossovers():
    """
    Pobiera dane BTC-USD od 2024-01-01, oblicza 50-dniową i 200-dniową średnią kroczącą,
    identyfikuje punkty przecięcia i zwraca listę dat tych przecięć.
    
    Returns:
        list: Lista dat przecięć w formacie 'YYYY-MM-DD'.
    """
    btc_data = yf.download('BTC-USD', start='2024-01-01')

    btc_data['50-day MA'] = btc_data['Close'].rolling(window=50).mean()
    btc_data['200-day MA'] = btc_data['Close'].rolling(window=200).mean()

    crossover_dates = []

    # wykrywanie przeciec
    # 1 - kiedy 50-dniowa średnia krocząca > powyżej 200-dniowej średniej
    # 2 - kiedy  50-dniowa średnia krocząca =< poniżej 200-dniowej średniej

    for i in range(1, len(btc_data)):
        if btc_data['50-day MA'].iloc[i] > btc_data['200-day MA'].iloc[i] and btc_data['50-day MA'].iloc[i - 1] <= btc_data['200-day MA'].iloc[i - 1]:
            crossover_dates.append(btc_data.index[i].strftime('%Y-%m-%d'))  

        elif btc_data['50-day MA'].iloc[i] < btc_data['200-day MA'].iloc[i] and btc_data['50-day MA'].iloc[i - 1] >= btc_data['200-day MA'].iloc[i - 1]:
            crossover_dates.append(btc_data.index[i].strftime('%Y-%m-%d'))  

    return crossover_dates



def calculate_total_btc_traded():
    """
    Pobiera dane BTC-USD z całego 2024 roku, oblicza ilość BTC handlowanych w każdym dniu
    oraz zwraca łączną ilość BTC dla dnia z najwyższym wolumenem.
    
    Returns:
        int: Łączna ilość BTC handlowanych w dniu z najwyższym wolumenem.
    """

    btc_data = yf.download('BTC-USD', start='2024-01-01')

    # Obliczenie ilości BTC handlowanych w każdym dniu
    btc_data['BTC Traded'] = btc_data['Volume'] / btc_data['Close']

   
    max_btc_day = btc_data['BTC Traded'].idxmax() # dzien z najwyzszym wolemenem 
    max_btc_traded = btc_data['BTC Traded'].loc[max_btc_day]  # Ilość BTC w tym dniu 


    return int(max_btc_traded)


if __name__ == '__main__':
    # Wywołanie funkcji i uzyskanie wyników
    crossover_dates = find_crossovers()
    total_traded = calculate_total_btc_traded()
    
    # Drukowanie wyników w żądanym formacie
    print(" ".join(crossover_dates))
    print(total_traded)
