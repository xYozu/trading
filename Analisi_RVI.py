import yfinance as yf
import talib
import matplotlib.pyplot as plt
import pandas_ta as ta


# Creo le liste che alla fine del programma mi serviranno per contenere i dati da stampare e rappresentare
lista_date = []
lista_trade = []
lista_budget_1 = []
budget = 100
lista_operazioni = []
trade_effettuati = 0
valori_finali = []

# Creo una lista contenente i tickers di alcune delle migliori aziende americane 
tickers = [ 'NVDA',  
    #'AAPL',
    #'GOOGL',
    #'AMZN', 
    #'KO',
    #'BAC',
    #'MSFT', 
    #'T',
    #'PFE', 
    #'TSLA' , 
    #'NFLX',
    #'JNJ', 'PG',
    #'V', 'MA','PEP', 
    'DIS', 'MCD', 'INTC',  'XOM',
    #'CVX', 
    #'MMM',
    #'ABBV',
    #'CSCO',
    #'IBM',
    #'WMT',  
    #'ORCL',
    #'ADBE',
    'TXN', 'COST', 'TGT', 'MDT', 'LMT',
    #'AVGO', 'AMD', 'CRM', 
    #'PYPL',
    #'INTU', 'AMAT', 
    #'FISV', 
    #'MSCI', 'TMO',
    #'GILD', 'UNH', 'CI', 'ELV', 'ISRG',
    #'ABT', 'CME', 'SCHW', 'BKNG', 'SPGI',
    #'MO', 'PM', 'SBUX', 
    #'CMCSA', 
    #'UPS',
    #'HON', 'RTX', 'DE', 'NKE', 'LOW'
]

# Con un ciclo prendo i dataset dei prezzi dei vari titoli in un range temporale
for ticker in tickers:

    print(f"Ticker:{ticker}") 
    df = yf.download(ticker, start="2017-01-01", end="2019-12-30", back_adjust=True)

    df_chiusura_adj = yf.download(ticker, start="2017-01-01", end="2019-12-30")

    df[['Adj Close']] = df_chiusura_adj[['Adj Close']]  # Poiché il primo dataset contiene i valori delle chiusure senza aggiustamenti come dividendi, split, ecc., prendo un dataset con le chiusure aggiustate e faccio il merge con il primo

    df['RSI'] = talib.RSI(df['Adj Close'], timeperiod=14)  # Con la libreria talib e ta creo gli indicatori da testare. Per maggiori informazioni sull'indicatore, leggere il README
    df['SMA'] = talib.SMA(df['RSI'], timeperiod=14)
    
    df['RVI_2'] = ta.rvi(df['Adj Close'], length=2, ma_length=2)  # Calcolo l'RVI di diversi periodi
    df['RVI_7'] = ta.rvi(df['Adj Close'], length=7, ma_length=7)
    df['RVI_14'] = ta.rvi(df['Adj Close'], length=14, ma_length=14)

    df.to_csv(f"{ticker}_rviscreener.csv")  # Creo un .csv del dataset del ticker
    
# Faccio un ciclo che iteri non più sui vari ticker ma sul dataset del ticker corrente
    for i in range(1, len(df)):
        if i == len(df)-9:  # Mi assicuro di non andare out of bounds
            break

    # Dal dataset creo le variabili che mi servono per vedere i prezzi di apertura, chiusura, massimi e minimi di giornata e dei giorni successivi

    # RSI, RVI, SMA: per la strategia utilizzo solo l'RVI, gli altri due indicatori, anche se sono inseriti, non li ho utilizzati per testare la strategia

        rvi_ieri2 = df['RVI_2'].iloc[i-1]
        rvi_oggi2 = df['RVI_2'].iloc[i]
        rvi_ieri7 = df['RVI_7'].iloc[i-1]
        rvi_oggi7 = df['RVI_7'].iloc[i]
        rvi_ieri14 = df['RVI_14'].iloc[i-1]
        rvi_oggi14 = df['RVI_14'].iloc[i]

        rsi_oggi = df['RSI'].iloc[i]
        sma_oggi = df['SMA'].iloc[i]
        rsi_ieri = df['RSI'].iloc[i-1]
        sma_ieri = df['SMA'].iloc[i-1]
        sma_7_giorni = df['SMA'].iloc[i-7]
    
    # Aperture
        open_successiva = df['Open'].iloc[i+1]
        open_2 = df['Open'].iloc[i+2]
        open_3 = df['Open'].iloc[i+3]
        open_4 = df['Open'].iloc[i+4]
        open_5 = df['Open'].iloc[i+5]
        open_6 = df['Open'].iloc[i+6]
        open_7 = df['Open'].iloc[i+7]

    # Chiusure
        close = df['Adj Close'].iloc[i]  # Prezzo al quale io compro l'azione
        close_successiva = df['Adj Close'].iloc[i+1]  # Prezzo di chiusura del giorno successivo (close-close_successiva) sarà il mio guadagno (close_successiva-close)/close*100 sarà il mio guadagno in percentuale
            
        close_2 = df['Adj Close'].iloc[i+2]
        close_3 = df['Adj Close'].iloc[i+3]
        close_4 = df['Adj Close'].iloc[i+4]
        close_5 = df['Adj Close'].iloc[i+5]
        close_6 = df['Adj Close'].iloc[i+6]
        close_7 = df['Adj Close'].iloc[i+7]

    # Massimi
        high_successivo = df['High'].iloc[i+1]  # Ho inserito anche massimi, minimi e aperture per vedere ad occhio ciò che succedeva nei giorni successivi (per magari una strategia futura) e le varie oscillazioni del prezzo 
        
        high_2 = df['High'].iloc[i+2]
        high_3 = df['High'].iloc[i+3]
        high_4 = df['High'].iloc[i+4]
        high_5 = df['High'].iloc[i+5]
        high_6 = df['High'].iloc[i+6]
        high_7 = df['High'].iloc[i+7]
    
    # Minimi
        low_successivo = df['Low'].iloc[i+1]
        low_2 = df['Low'].iloc[i+2]
        low_3 = df['Low'].iloc[i+3]
        low_4 = df['Low'].iloc[i+4]
        low_5 = df['Low'].iloc[i+5]
        low_6 = df['Low'].iloc[i+6]
        low_7 = df['Low'].iloc[i+7]

    # Volumi
        volume = df['Volume'].iloc[i]  # Il volume è la quantità di azioni scambiate

        if rvi_oggi14 < 20:  # Controllo se l'RVI del giorno ha un valore inferiore a 20, che identifica un valore di volatilità al ribasso (iper-venduto). Quindi teoricamente, se il prezzo tende a scendere, può esserci una continuazione del trend o una inversione. Io controllo se vi è una inversione, infatti compro il giorno in cui il titolo chiude con un valore di RVI sotto 20 e vendo alla chiusura del giorno dopo
            print(f"Date: {df.index[i].date()}, BUY")  # Data del giorno in cui acquisto
            print(f"RVI oggi 14: {rvi_oggi14}")  # Valore dell'RVI alla chiusura
            print(f"Comprato a: {close:.2f}")  # Faccio in modo che il mio prezzo di acquisto sia quello di chiusura di giornata
            print(" ")
            # Stampo i vari risultati per vedere come variano le chiusure e quindi i possibili ritorni, in questo caso dopo una giornata, 2, 3... una settimana dopo
            print(f"close_successivo: {close_successiva}, profitto: {(close_successiva-close)/close*100}%")
            print(f"close_2: {close_2}, profitto: {(close_2-close)/close*100}%")
            print(f"close_3: {close_3}, profitto: {(close_3-close)/close*100}%")
            print(f"close_4: {close_4}, profitto: {(close_4-close)/close*100}%")
            print(f"close_5: {close_5}, profitto: {(close_5-close)/close*100}%")
            print(f"close_6: {close_6}, profitto: {(close_6-close)/close*100}%")
            print(f"close_7: {close_7}, profitto: {(close_7-close)/close*100}%")

            print(" ")
            print("-" * 100)
            # Stampo i prezzi massimi raggiunti
            print(f"high_successivo: {high_successivo}, profitto: {(high_successivo-close)/close*100}%")
            print(f"high_2: {high_2}, profitto: {(high_2-close)/close*100}%")
            print(f"high_3: {high_3}, profitto: {(high_3-close)/close*100}%")
            print(f"high_4: {high_4}, profitto: {(high_4-close)/close*100}%")
            print(f"high_5: {high_5}, profitto: {(high_5-close)/close*100}%")
            print(f"high_6: {high_6}, profitto: {(high_6-close)/close*100}%")
            print(f"high_7: {high_7}, profitto: {(high_7-close)/close*100}%")

            var1 = (close_successiva - close) / close * 100  # Creo la variabile var1 che ad ogni ciclo sarà il valore del guadagno o perdita se ho acquistato il giorno n e venduto il giorno n+1
            trade = {'date': df.index[i].date(), 'variazione': var1, 'ticker': ticker}  # Creo un dizionario che tiene conto della data del trade, la variazione (guadagno/perdita percentuale) e il ticker della stock tradata
            lista_trade.append(trade)  # Aggiungo i dizionari in una lista
            trade_effettuati = trade_effettuati + 1
            print("-" * 100)

lista_trade_ordinati = sorted(lista_trade, key=lambda x: x['date'])  # Ordino i dizionari nella lista in base alla data 

lista_trade_unici = []
date_incontrate = set()

for item in lista_trade_ordinati:  # Dopo aver ordinato la lista, provvedo ad eliminare giorni in cui ho tradato più di un titolo. Poiché io utilizzo tutto il budget per ogni trade, posso fare un solo acquisto al giorno, quindi elimino le date in cui ho acquistato più volte lasciandone una sola. NB: se ho fatto più acquisti in un giorno, mi rimarrà solo quello fatto con il ticker posizionato prima nella lista
    data = item['date']
    if data not in date_incontrate:
        lista_trade_unici.append(item)
        date_incontrate.add(data)

for item in lista_trade_unici:  # Modifico il budget in base alla lista contenente i vari guadagni derivati dai trade eseguiti
    variazione = item['variazione']  # Prendo dal dizionario il valore della variazione percentuale 
    budget *= (1 + variazione / 100)  # Modifico il budget
    valori_finali.append(budget)

print("Valori finali dopo ogni variazione percentuale:")
for i, valore in enumerate(valori_finali):  # Stampo il dizionario e il valore del budget dopo la variazione
    print(f"Dopo variazione {lista_trade_unici[i]}%: {valore:.2f}")
print(f"Trade effettuati: {trade_effettuati}")

# Creo un grafico che mostri l'andamento del budget
plt.plot(valori_finali, marker='o', color='r')
plt.title(f"Andamento budget")
plt.xlabel("Numero di trade")
plt.ylabel("Valore Budget")
plt.grid(False)
    
# Mostra il grafico finale, per compararlo con il benchmark utilizzo TradingView, successivamente penso di aggiungere l'andamento dell'S&P 500 così da compararlo direttamente nel grafico
plt.show()

# Conclusioni
# In base ai test effettuati si dimostra che l'utilizzo dell'RVI non batte il mercato in maniera costante, ma può essere utile come indicatore di supporto in una strategia più complessa. Inoltre la strategia non prevede una gestione del rischio, che potrebbe migliorarne i risultati.  

