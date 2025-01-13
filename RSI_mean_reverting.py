import yfinance as yf
import talib
import matplotlib.pyplot as plt
import pandas_ta as ta
import pandas as pd
import numpy as np
from collections import Counter
from collections import defaultdict
import seaborn as sns
from scipy.stats import pearsonr

#creo le liste che alla fine del programma mi serviranno per contenere i dati da stampare e rappresentare
lista_date= []
lista_trade=[]
lista_budget_1=[]
lista_differenze_fail=[]
lista_differenze_gain=[]
trade_effettuati=0
valori_finali =[]
lista_media_variazioni=[]
numero_di_trade_effettuati=0

#parametri dei test
budget=100

data_inizio_test="2014-01-01"
data_fine_test="2024-12-31"
intervallo="1wk"

periodo= 10
stop_loss=  -0.25
take_profit= 0.25

# creo una lista contenente i ticker di alcune delle migliori aziende
tickers = [ 
    #americane
    'NVDA', 'AAPL', 'GOOGL', 'AMZN', 'KO', 'BAC', 'MSFT', 'T',  'F', 'PFE', 'JPM',  'WFC', 'HD', 'LLY', 'PG', 'MA', 'DIS', 'INTC', 'XOM',
    'CVX', 'MMM','CSCO','IBM','WMT', 'ORCL','ADBE','TXN', 'COST', 'TGT', 'MDT', 'LMT','AVGO', 'AMD', 'CRM', 'PYPL', 'TSLA', 'NFLX', 'V',
    'INTU', 'AMAT','MSCI', 'TMO','GILD', 'UNH', 'CI', 'ELV', 'ISRG','ABT', 'CME', 'SCHW', 'BKNG', 'SPGI','MO', 'PM', 'SBUX', 'UPS','HON', 'RTX', 'DE', 'NKE', 'LOW',
    #europee 
    #'CRH', 'ROG', 'DGE', 'NOV', 'DCC','SAP', 'BA', 'AZN', 'RMS', 'SAN',  
    #peggiorano il risultato
    'GE', 'VZ', 'MRK', 'JNJ', 'PEP', 'MCD',
]

# con un ciclo prendo i dataset dei prezzi dei vari titoli durante un range temporale

for ticker in tickers:

    print(f"Ticker:{ticker}") 
    df = yf.download(ticker, start=data_inizio_test, end=data_fine_test, back_adjust=True, interval=intervallo)

    df_chiusura_adj= yf.download(ticker, start=data_inizio_test, end=data_fine_test, interval=intervallo)


    df[['Adj Close']]=df_chiusura_adj[['Adj Close']]  #"Poiché il primo dataset contiene i valori di chiusura non aggiustati (es. dividendi, split), prendo un dataset con le chiusure aggiustate e lo unisco con il primo

    df['RSI'] = talib.RSI(df['Adj Close'], timeperiod=periodo)#con talib e ta creo gli indicatori da testare, per maggiore informazioni sull'idicatore leggere il README
    df['SMA'] = talib.SMA(df['RSI'], timeperiod=periodo)
    
    df['RVI_2'] = ta.rvi(df['Adj Close'], length=2, ma_length=2)#calcolo l'rvi di diversi periodi
    df['RVI_7'] = ta.rvi(df['Adj Close'], length=7, ma_length=7)
    df['RVI_14'] = ta.rvi(df['Adj Close'], length=14, ma_length=14)
    df['Monthly_returns'] = df['Close'].pct_change()
    


    #df.to_csv(f"{ticker}_rviscreener.csv")# creo un csv del dataset del ticker
    
    for i in range(1, len(df)):# faccio un ciclo che iteri non più sui vari ticker ma sul dataset del ticker corrente
        if i==len(df)-4:#mi assicuro di non andare outofbonds
            break

    # dal dataset creo le variabili  che mi servinno per vedere i prezzi di apertura, chiusura, massimi e minimi di giornata e dei giorni successivi
    #


    # RSI RVI  SMA

        rvi_precedente2 = df['RVI_2'].iloc[i-1]
        rvi_attule7 = df['RVI_7'].iloc[i]
        rvi_attuale14 = df['RVI_14'].iloc[i]
        
        rsi_attule = df['RSI'].iloc[i]
        sma_attuale= df['SMA'].iloc[i]
        sma_precedente = df['SMA'].iloc[i-1]
        sma_successiva=df['SMA'].iloc[i+1]
        sma_2_volte_prima=df['SMA'].iloc[i-2]
        
    
    # aperture
        open_precedente= df['Open'].iloc[i-1]
        open_attuale=df['Open'].iloc[i]
        open_successiva= df['Open'].iloc[i+1]
        open_2 = df['Open'].iloc[i+2]
        open_3 = df['Open'].iloc[i+3]
       

    # chiusure
        close_meno2 = df['Adj Close'].iloc[i-2]
        close_precedente = df['Adj Close'].iloc[i-1]
        close = df['Adj Close'].iloc[i]# prezzo al quale io compro l'azione
        close_successiva = df['Adj Close'].iloc[i+1]# prezzo di chiusura del giorno successivo (close-close_successiva) sarà il mio guadagno (close_successiva-close)/close*100 sarà il mio guadagno in percentuale
            
        close_2 = df['Adj Close'].iloc[i+2]
        close_3 = df['Adj Close'].iloc[i+3]
        
    #massimi
        high_precedente= df['High'].iloc[i-1]
        high=df['High'].iloc[i]
        high_successivo= df['High'].iloc[i+1]# ho inserito anche massimi, minimi e aperture per vedere AD OCCHIO cio che succedeva i giorni successivi e le varie oscillazioni del prezzo 
        
        high_2 = df['High'].iloc[i+2]
        high_3 = df['High'].iloc[i+3]
        
    
    # minimi
        low=df['Low'].iloc[i]
        low_successivo= df['Low'].iloc[i+1]
        low_2 = df['Low'].iloc[i+2]
        low_3 = df['Low'].iloc[i+3]
        

    #volumi
        volume=df['Volume'].iloc[i]# il volume è la quantità di azioni scambiate
        
        if sma_attuale>sma_precedente and sma_2_volte_prima>sma_precedente:#controllo cosa succede quando ho una inversione della media dello RSI
               
            data=df.index[i].date()
            print(f"Date: {df.index[i].date()}, BUY")

            numero_di_trade_effettuati=numero_di_trade_effettuati+1
    
            #print(f"RSI oggi 12: {rsi_oggi}")
            print(f"SMA attuale : {sma_attuale}")
            print(f"SMA precedente : {sma_precedente}")
            print(f"SMA 2 volte prima : {sma_2_volte_prima}")

            print(f"comprato a: {close:.2f}")

            print(" ")
            print("-" * 100)
            print(" ")

            # stampo i vari risultati per vedere come varia durante le settimane
            print(f"close_successivo: {close_successiva}, profitto: {(close_successiva - close) / close }%")
            print(f"close_2: {close_2}, profitto: {(close_2 - close) / close }%")
            print(f"close_3: {close_3}, profitto: {(close_3 - close) / close }%")
                
            print(" ")
            print("-" * 100)
            #stampo i prezzi massimi raggiunti
            print(f"high_successivo: {high_successivo}, profitto: {(high_successivo-close)/close}%")
            print(f"high_2: {high_2}, profitto: {(high_2-close)/close}%")
            print(f"high_3: {high_3}, profitto: {(high_3-close)/close}%")
                
            print("-" * 100)
            print(" ")

            #minimi
            print(f"low_successivo: {low_successivo}, profitto: {(low_successivo-close)/close}%")
            print(f"low_2: {low_2}, profitto: {(low_2-close)/close}%")
            print(f"low_3: {low_3}, profitto: {(low_3-close)/close}%")
                
            print("-" * 100)
            print(" ")
            #aperture
            print(f"open_successivo: {open_successiva}, profitto: {(open_successiva-close)/close*100}%")
            print(f"open_2: {open_2}, profitto: {(open_2-close)/close}%")
            print(f"open_3: {open_3}, profitto: {(open_3-close)/close}%")
                
            print("-" * 100)
            print(" ")

            #volumi
            print("-" * 100)
            print(" ")
            print(f"VOLUME: {volume}")
              
            print("-" * 100)
            print(" ")

            #creo la variabile var1 che ad ogni ciclo sarà il valore del guadagno o perdita se ho acquistato la settimana n e venduto a n+1
            var1=round((close_successiva-close)/close, 3)
            high1=round((high_successivo-close)/close, 3)
            low1=round((low_successivo-close)/close, 3)
            open1=round((open_successiva-close)/close, 3)
            

            lista_media_variazioni.append(var1)
            if low1<stop_loss:#utilizzo il -x% come stoploss, ovvero aggiungo nella lista -x%
                trade={'date':df.index[i].date(), 'variazione':stop_loss, 'Alla apertura':open1, 'High_raggiunto':high1, 'Low_raggiunto':low1, 'ticker': ticker,}
                lista_trade.append(trade)
            elif high1>=take_profit:
                trade={'date':df.index[i].date(), 'variazione':take_profit, 'Alla apertura':open1, 'High_raggiunto':high1, 'Low_raggiunto':low1, 'ticker': ticker,}
                lista_trade.append(trade)
            else:
                trade={'date':df.index[i].date(), 'variazione':var1, 'Alla apertura':open1, 'High_raggiunto':high1, 'Low_raggiunto':low1, 'ticker': ticker,}
                lista_trade.append(trade)#aggiungo i dizionari in una lista

            #creo delle liste per vedere i massimi e i minimi
            if var1<0:
                print(f"low fail: {( low_successivo-close_successiva)/close_successiva:.2f}%")
                lista_differenze_fail.append(( low_successivo-close)/close )
            elif var1>0:
                print(f"low gain: {( low_successivo-close)/close:.2f}%")
                lista_differenze_gain.append(( low_successivo-close)/close)
            print("-" * 100)

lista_trade_ordinati= sorted(lista_trade, key=lambda x: x['date'])#ordino i dizionari nella lista in base alla data 

#poichè più titoli ogni settimana soddisfano le condizioni di entrata provvedo a fare la media dei ritorni di tutti i titoli tradati nella settimanaa, come se avessero tutti lo stesso peso e splittassi il budget
for i, valore in enumerate(lista_trade_ordinati):
    print(f"Dopo variazione {lista_trade_ordinati[i]}%")

date= [d['date'] for d in lista_trade_ordinati]
conta = Counter(date)
lista_doppioni = [d for d in lista_trade_ordinati if conta[d['date']] >= 1]


date_groups = defaultdict(list)
# Raggruppo i valori per data
for item in lista_doppioni:
    date_groups[item['date']].append(item['variazione'])

# Calcolo la media per ogni data
result = []
for date, variazioni in date_groups.items():
    media_variazione = sum(variazioni) / len(variazioni)
    result.append({'date': date, 'variazione media': media_variazione})

strategy_returns=[]
for item in result: 
    variazione = item['variazione media']# prendo dal dizionario il valore della variazione del prezzo
    strategy_returns.append(variazione)

for item in result: #modifico il budget in base alla lista contenente i vari guadagni/perdite derivati dai trade eseguiti
    variazione = item['variazione media']# prendo dal dizionario il valore della variazione percentuale 
    budget *= (1 + variazione ) # modifico il budget
    valori_finali.append(budget)

for i, valore in enumerate(valori_finali):# stampo il dizionario e il valore del budget dopo la variazione
    print(f"Dopo variazione {result[i]}%: {valore:.2f}")


media=sum(lista_media_variazioni)/len(lista_media_variazioni)
#print(f"media delle varizioni {media}%")
print(f"trade totali  {numero_di_trade_effettuati}")


#con questa funzione controllo come si è comportato un benchmark nello stesso arco temporale
def grafico_benchmark(budget=100, ticker="^NDX", inizio=data_inizio_test, fine=data_fine_test ): #NASDAQ-100 (^NDX)
    #iShares MSCI ACWI ETF (ACWI)      
    #iShares MSCI World ETF (URTH)
    #SPDR S&P 500 ETF (SPY)
    #Vanguard Total Stock Market ETF (VTI)
    #iShares MSCI Emerging Markets ETF (EEM) 
    #Vanguard FTSE All-World ex-US ETF (VEU)
    #Obbligazioni: Bloomberg Barclays Global Aggregate Bond Index Ticker: LAGG oppure Bloomberg Barclays U.S. Treasury Bond IndexTicker: GOVT
    
    benchmark = yf.download(ticker, start=inizio, end=fine, interval=intervallo)
    benchmark_chiusura_adj= yf.download(ticker, start=data_inizio_test, end=data_fine_test, interval=intervallo)
    benchmark[['Adj Close']]=benchmark_chiusura_adj[['Adj Close']] 
    
    benchmark['Rendimento'] = benchmark['Adj Close'].pct_change()  # Calcolo il rendimento 
    benchmark['Budget'] = budget * (1 + benchmark['Rendimento']).cumprod()
    benchmark.to_csv(f"controllo_dati_funzione_benchmark.csv")
    
    lista_rendimenti_in_centesimi=benchmark['Rendimento'].dropna().tolist()

    plt.figure(figsize=(12, 6))
    plt.plot(benchmark.index, benchmark['Budget'], label="benchmark", color='blue')
    plt.title(f"Andamento dell'investimento con il benchmark con un budget di {budget} dal {inizio} al {fine}")
    plt.xlabel("Data")
    plt.ylabel("Valore dell'investimento")
    plt.legend(loc="upper left")
    plt.grid(True)
    plt.show()

    return lista_rendimenti_in_centesimi

plt.figure(figsize=(12, 6))
plt.plot(valori_finali, label='MY_STRATEGY', color='r')      
plt.title(f"Andamento budget")
plt.xlabel("numero di trade")
plt.ylabel("Valore Budget")
plt.grid(False)
plt.show()


def mostra_correlazione(dati):#mi serviva per vedere se vi era una correlazione con le apertura, considerando che io mi aspetto una inversione e un aumento del prezzo volevo vedere se una apertura positiva si concludesse con una chiusura positiva o un max per poi riscendere
    
    aperture = [d['Alla apertura'] for d in dati if 'Alla apertura' in d]
    high_raggiunto = [d['High_raggiunto'] for d in dati if 'High_raggiunto' in d]
    low_raggiunto = [d['Low_raggiunto'] for d in dati if 'Low_raggiunto' in d]
    variazione = [d['variazione'] for d in dati if 'variazione' in d]
    
    df = pd.DataFrame({
        'apertura': aperture,
        'high_raggiunto': high_raggiunto,
        'low_raggiunto': low_raggiunto,
        'variazione': variazione,    
    })
    
    # Calcolo la matrice di correlazione
    correlazione_matrix = df.corr()

    # Matrice di correlazione con una heatmap, 
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlazione_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1, fmt=".2f", linewidths=0.5)
    plt.title('Matrice di Correlazione tra le Variabili')
    plt.show()

    # Stampo le correlazioni tra ogni coppia di variabili
    for var1 in df.columns:
        for var2 in df.columns:
            if var1 != var2:
                correlazione, _ = pearsonr(df[var1], df[var2])
                print(f"Correlazione tra {var1} e {var2}: {correlazione:.2f}")

mostra_correlazione(lista_trade_ordinati)

def risk_calculator(returns_1, returns_2, risk_free_rate=0.03, alpha=0.05):# calcolo il rischio storico della strategia e del benchmrk per compararli
    
    def volatility(returns):

        dev_std=np.std(returns)

        return  dev_std


    def sharpe_ratio(returns, risk_free_rate):

        rendimento_settimanale_medio= np.mean(returns) 
        volatilita = volatility(returns)
        rendimento_annuo = (1 + rendimento_settimanale_medio)**52 - 1
        volatilita_annua = volatilita * np.sqrt(52)
        sharpe=(rendimento_annuo - risk_free_rate )/ volatilita_annua

        return sharpe

    def value_at_risk(returns, alpha):
        
        rendimenti_ordinati = np.sort(returns)
        indice = int(alpha * len(rendimenti_ordinati))
        var = rendimenti_ordinati[indice]

        return var
    
    def expected_shortfall(returns, alpha):
        
        # Ordinare i rendimenti
        rendimenti_ordinati = np.sort(returns)
    
    
        indice_var = int(alpha * len(rendimenti_ordinati))
        rendimenti_peggiori = rendimenti_ordinati[:indice_var]
        es = np.mean(rendimenti_peggiori)

        return es

    def max_drawdown(rendimenti):
        
        capitale_iniziale = 100
        valori_portafoglio = [capitale_iniziale]
    
        for rendimento in rendimenti:
            valore_attuale = valori_portafoglio[-1] * (1 + rendimento)
            valori_portafoglio.append(valore_attuale)
    
        # Calcolare il massimo drawdown
        peak = valori_portafoglio[0]  # il picco iniziale
        max_dd = 0  # massimo drawdown inizializzato a 0
    
        for valore in valori_portafoglio:
            if valore > peak:
                peak = valore  # nuovo picco
            drawdown = (peak - valore) / peak  # calcolo del drawdown
            max_dd = max(max_dd, drawdown)  # aggiorno il massimo drawdown se necessario
    
        return -max_dd # ritorniamo il max drawdown 

    volatility_1=volatility(returns_1)
    volatility_2=volatility(returns_2)
    sharpe_1=sharpe_ratio(returns_1, risk_free_rate)
    sharpe_2=sharpe_ratio(returns_2, risk_free_rate)
    VaR_benchmark=value_at_risk(returns_1, alpha)
    VaR_strategy=value_at_risk(returns_2, alpha)
    max_drawdown_benchmark=max_drawdown(returns_1)
    max_drawdown_strategia=max_drawdown(returns_2)
    expected_shortfall_benchmark=expected_shortfall(returns_1, alpha)
    expected_shortfall_strategia=expected_shortfall(returns_2, alpha)

    risultati_rischio={ 'volatilità_benchmark':volatility_1,
                        'volatilità_strategia':volatility_2, 
                        'sharpe_rateo_benchmark':sharpe_1, 
                        'sharpe_rateo_strategia':sharpe_2, 
                        'VaR_benchmark':VaR_benchmark, 
                        'VaR_strategy':VaR_strategy,
                        'max_drawdown_benchmark': max_drawdown_benchmark,
                        'max_drawdown_strategia': max_drawdown_strategia,
                        'expected_shortfall_benchmark': expected_shortfall_benchmark,
                        'expected_shortfall_strategia': expected_shortfall_strategia,



                        }

    return risultati_rischio

#guardo l'andamento del benchmark
risultati_benchmark=grafico_benchmark()

#guardo il rischio associato alla performance
risultati_rischio=risk_calculator(risultati_benchmark, strategy_returns)
print(f"quantità variazioni strategia {len(strategy_returns)}")
print(f"quantità variazioni benchmark {len(risultati_benchmark)}")
print(f"risultati analisi del rischio {risultati_rischio} ")

#analizzo i drawdown massimi ottenuti durante l'esposizione
#fail
plt.figure(figsize=(14, 8))
plt.scatter(lista_differenze_fail, list(range(len(lista_differenze_fail))), marker='x', color='b') 
plt.title(f"minimi raggiunti e trade persi")
plt.xlabel("Percentuale minimo")
plt.ylabel("trade")
plt.grid(False)
plt.show()
#gain
plt.figure(figsize=(14, 8))
plt.scatter(lista_differenze_gain, list(range(len(lista_differenze_gain))), marker='x', color='g')
plt.title(f"minimi raggiunti e trade vinti")
plt.xlabel("Percentuale minimo")
plt.ylabel("trade")
plt.grid(False)
plt.show()

#come è possibile notare superato il -5% di loss quasi mai il titolo ha chiuso successivmente in positivo, potrebbe essere un buon segnale di stoploss, analizzo quale potrebbe essere un buon stoploss

def good_stoploss(gain, fail):
    
    
    mean_gain, std_gain = np.mean(gain), np.std(gain)
    mean_fail, std_fail = np.mean(fail), np.std(fail)

    # Usa np.linspace per creare l'intervallo di x
    x1 = np.linspace(min(gain), max(gain), len(gain))
    x2 = np.linspace(min(fail), max(fail), len(fail))
    # Calcola la distribuzione normale per ciascuna lista
    y1 = (1/(std_gain * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x1 - mean_gain) / std_gain)**2)
    y2 = (1/(std_fail * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x2 - mean_fail) / std_fail)**2)

    # Visualizza il grafico delle distribuzioni
    plt.figure(figsize=(14, 8))
    plt.plot(x1, y1, label="Distribuzione dei minimi dei trade conclusi in profitto", color="blue")
    plt.axvline(x=mean_gain, color='blue',linewidth=1)
    plt.plot(x2, y2, label="Distribuzione dei minimi dei trade conclusi in perdita", color="red")
    plt.axvline(x=mean_fail, color='red',linewidth=1)
    plt.title("Distribuzione")
    plt.xlabel("Valori")
    plt.ylabel("Densità di Probabilità")
    plt.legend()
    plt.show()

    return mean_gain-std_gain

stoploss_possibile=good_stoploss(lista_differenze_gain, lista_differenze_fail)
print(f"possibile stoploss {stoploss_possibile}")


