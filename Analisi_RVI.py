import yfinance as yf
import talib
import matplotlib.pyplot as plt
import pandas_ta as ta


#creo le liste che alla fine del progrmamma mi serviranno per contenere i dati da stampare e rappresentare
lista_date= []
lista_trade=[]
lista_budget_1=[]
budget=100
lista_operazioni=[]
trade_effettuati=0
valori_finali =[]

# creo una lista contenente i ticker di alcune delle migiori aziende americane 
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
# con un ciclo prendo i dataset dei prezzi dei vari titoli durante un range temporale
for ticker in tickers:

    print(f"Ticker:{ticker}") 
    df = yf.download(ticker, start="2017-01-01", end="2019-12-30", back_adjust=True)

    df_chiusura_adj= yf.download(ticker, start="2017-01-01", end="2019-12-30")


    df[['Adj Close']]=df_chiusura_adj[['Adj Close']]  #poichè il primo dataset contiene i valori delle ciusure senza aggiustamenti come dividendi split ecc prendo un dataset con le chiusure aggiustate e faccio merge con il primo

    df['RSI'] = talib.RSI(df['Adj Close'], timeperiod=14)#con la libreria talib e ta creo gli indicatori da testare, per maggiore informazini sull'idicatore leggere il README
    df['SMA'] = talib.SMA(df['RSI'], timeperiod=14)
    
    df['RVI_2'] = ta.rvi(df['Adj Close'], length=2, ma_length=2)#calcolo l'rvi di diversi periodi
    df['RVI_7'] = ta.rvi(df['Adj Close'], length=7, ma_length=7)
    df['RVI_14'] = ta.rvi(df['Adj Close'], length=14, ma_length=14)
    


# Optionally, save to a CSV file
    df.to_csv(f"{ticker}_rviscreener.csv")# creo un csv del dataset del ticker
    
    for i in range(1, len(df)):# faccio un ciclo che iteri non più su i vari ticker ma sul dataset del ticker corrente
        if i==len(df)-9:#mi assicuro di non andare outofbonds
            break

    # dal dataset creo le variabili  che mi servinno per vedere i prezzi di apertura, chiusura, massimi e minimi di giornata e dei giorni successivi

    # RSI RVI  SMA

        rvi_ieri2 = df['RVI_2'].iloc[i-1]
        rvi_oggi2 = df['RVI_2'].iloc[i]
        rvi_ieri7 = df['RVI_7'].iloc[i-1]
        rvi_oggi7 = df['RVI_7'].iloc[i]
        rvi_ieri14 = df['RVI_14'].iloc[i-1]
        rvi_oggi14 = df['RVI_14'].iloc[i]



        rsi_oggi = df['RSI'].iloc[i]
        sma_oggi= df['SMA'].iloc[i]
        rsi_ieri = df['RSI'].iloc[i-1]
        sma_ieri = df['SMA'].iloc[i-1]
        sma_7_giorni=df['SMA'].iloc[i-7]
    
    # aperture
        open_successiva= df['Open'].iloc[i+1]
        open_2 = df['Open'].iloc[i+2]
        open_3 = df['Open'].iloc[i+3]
        open_4 = df['Open'].iloc[i+4]
        open_5 = df['Open'].iloc[i+5]
        open_6 = df['Open'].iloc[i+6]
        open_7 = df['Open'].iloc[i+7]

    # chiusure
        close = df['Adj Close'].iloc[i]# prezzo al quale io compro l'azione
        close_successiva = df['Adj Close'].iloc[i+1]# prezzo di chiusura del giorno successivo (close-close_successiva) sarà il mio guadagno (close_successiva-close)/close*100 sarà il mio guadagno in percentuale
            
        close_2 = df['Adj Close'].iloc[i+2]
        close_3 = df['Adj Close'].iloc[i+3]
        close_4 = df['Adj Close'].iloc[i+4]
        close_5 = df['Adj Close'].iloc[i+5]
        close_6 = df['Adj Close'].iloc[i+6]
        close_7 = df['Adj Close'].iloc[i+7]

    #massimi
        high_successivo= df['High'].iloc[i+1]# ho inserito anche massimi, minimi e aperture per vedere AD OCCHIO cio che succedeva i giorni successivi e le varie oscillazioni del prezzo 
        
        high_2 = df['High'].iloc[i+2]
        high_3 = df['High'].iloc[i+3]
        high_4 = df['High'].iloc[i+4]
        high_5 = df['High'].iloc[i+5]
        high_6 = df['High'].iloc[i+6]
        high_7 = df['High'].iloc[i+7]
    
    # minimi
        low_successivo= df['Low'].iloc[i+1]
        low_2 = df['Low'].iloc[i+2]
        low_3 = df['Low'].iloc[i+3]
        low_4 = df['Low'].iloc[i+4]
        low_5 = df['Low'].iloc[i+5]
        low_6 = df['Low'].iloc[i+6]
        low_7 = df['Low'].iloc[i+7]

    #volumi
        volume=df['Volume'].iloc[i]# il volume è la quantità di azioni scambiate

        if rvi_oggi14<20:# controllo se l'rvi del giorno ha un valore inferiore a 20, che identifica un valore di voltilita al ribasso, quindi teoricamente se il prezzo tende a scendere può esserci una continuazione del trendo o una inversione, io controllo se vi è una inversione, infatti compro il giorno in cui il titolo chiude con un valore di rvi sotto 20 e vendo alla chiusura del giorno dopo
                
                print(f"Date: {df.index[i].date()}, BUY")
                
                print(f"RVI oggi 14: {rvi_oggi14}")

                print(f"comprato a: {close:.2f}")# faccio in modo che il mio prezzo di acquisto sia quello di chiusura di giornata

                print(" ")
                # stampo i vari risultati per vedere come varia durante i le giornate, in questo caso dopo una giornata, 2, 3...una settimana dopo
                print(f"close_successivo: {close_successiva}, profitto: {(close_successiva-close)/close*100}%")
                print(f"close_2: {close_2}, profitto: {(close_2-close)/close*100}%")
                print(f"close_3: {close_3}, profitto: {(close_3-close)/close*100}%")
                print(f"close_4: {close_4}, profitto: {(close_4-close)/close*100}%")
                print(f"close_5: {close_5}, profitto: {(close_5-close)/close*100}%")
                print(f"close_6: {close_6}, profitto: {(close_6-close)/close*100}%")
                print(f"close_7: {close_7}, profitto: {(close_7-close)/close*100}%")

                print(" ")
                print("-" * 100)
                #stampo i prezzi massimi raggiunti
                print(f"high_successivo: {high_successivo}, profitto: {(high_successivo-close)/close*100}%")
                print(f"high_2: {high_2}, profitto: {(high_2-close)/close*100}%")
                print(f"high_3: {high_3}, profitto: {(high_3-close)/close*100}%")
                print(f"high_4: {high_4}, profitto: {(high_4-close)/close*100}%")
                print(f"high_5: {high_5}, profitto: {(high_5-close)/close*100}%")
                print(f"high_6: {high_6}, profitto: {(high_6-close)/close*100}%")
                print(f"high_7: {high_7}, profitto: {(high_7-close)/close*100}%")

                var1=(close_successiva-close)/close*100#creo la variabile var1 che ad ogni ciclo sarà il valore del guadagno o perdita su ho acquistato il giorno n e venduto il giorno n+1
                trade={'date':df.index[i].date(), 'variazione':var1, 'ticker': ticker}# creo un dizionrio che tiene conto della data del trade, la variazione(gadagno perdit percentule) e il ticker della stock tradata
                lista_trade.append(trade)#aggiungo i dizionari in una lista
                        
                trade_effettuati=trade_effettuati+1
                print("-" * 100)

lista_trade_ordinati= sorted(lista_trade, key=lambda x: x['date'])#ordino i dizionari nella lista in base alla data 

lista_trade_unici = []
date_incontrate = set()

for item in lista_trade_ordinati: #dopo aver ordinto la lista provvedo ad eliminare giorni in cui ho tradato più di un titolo
    data = item['date']
    if data not in date_incontrate:
        lista_trade_unici.append(item)
        date_incontrate.add(data)

for item in lista_trade_unici: #modifico il budget in base alla lista contenente i vari guadagni derivati dai trade eseguiti
    variazione = item['variazione']# prendo dal dizionario il valore della variazione percentuale 
    budget *= (1 + variazione / 100) # modifico il budget
    valori_finali.append(budget)

print("Valori finali dopo ogni variazione percentuale:")
for i, valore in enumerate(valori_finali):# stampo il dizionario e il valore del budget dopo la variazione
    print(f"Dopo variazione {lista_trade_unici[i]}%: {valore:.2f}")
print(f"trade effettuati: {trade_effettuati}")



#creo un grafico che mostri l'andamento del budget
plt.plot(valori_finali, marker='o', color='r')
    
plt.title(f"Andamento budget")
plt.xlabel("numero di trade")
plt.ylabel("Valore Budget")
plt.grid(False)
    
# Mostra il grafico finale
plt.show()

#Conclusioni
#in base ai test effettuati si dimostra che l'utilizzo del RVI non batte il mercato in maniera costante
#
