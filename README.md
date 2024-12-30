In questo spazio farò analisi veloci di dati riguardanti per lo più il prezzo delle azioni delle più grandi aziende americane. L'obiettivo è vedere se i soliti indicatori di analisi tecnica funzionano e cercare di utilizzarli combinati tra loro in modo tale da risultare più efficaci. Se i risultati ottenuti da una prima analisi sono piuttosto buoni, cercherò di ottimizzarli e migliorarli nel tempo. Come benchmark utilizzo l'andamento dell'indice Standard & Poor's 500 del periodo analizzato. Tali indicatori sono i più famosi e sono presenti nella libreria Python TA-lib.

"Analisi_RVI.py".
In "Analisi_RVI" analizzo l'indicatore Relative Volatility Index. L'RVI misura la deviazione standard dei prezzi nel tempo, ovvero è un indicatore di volatilità dei prezzi in un determinato periodo di tempo (es: 14 periodi = volatilità negli ultimi 14 giorni). Se la volatilità è al rialzo, siamo in una situazione di "iper-comprato", viceversa in "iper-venduto".

La strategia prevede di comprare in chiusura in una situazione di mercato di iper-venduto, ovvero con volatilità al ribasso, e controllare se il giorno dopo il prezzo chiude a un prezzo maggiore di quello acquistato (strategia reversal). 
Dopo vari test, i risultati hanno dimostrato che con un RVI a 14 periodi si batte il mercato poche volte. Inoltre, non tenendo conto di altri costi che per semplicità e velocità non ho considerato, come i costi di operazione e spread bid/ask, la strategia ha comunque mostrato dei risultati interessanti. 
Tuttavia, con un determinato numero di azioni e in alcuni periodi di tempo, il mercato è stato battuto (qualche volta anche in maniera sostanziosa). Questo mi fa pensare che potrei migliorare la strategia, magari facendo un'analisi macroeconomica sul perché per un numero di azioni o per un determinato periodo la strategia ha performato così bene.
Successivamente, potrei calcolare i costi che dovrei affrontare e infine vedere se batterei un ETF a replica dell'S&P 500.

"RSI_mean_reverting.py"

Nel file "RSI_mean_reverting.py" viene analizzata la media dell'indicatore Relative Strength Index (RSI). L'RSI è un indicatore utilizzato per misurare la "forza" o la "debolezza" di un asset in relazione ai suoi movimenti di prezzo recenti. Esso valuta la velocità e l'intensità delle variazioni di prezzo, fornendo segnali che possono suggerire condizioni di ipercomprato o ipervenduto. In particolare, l'RSI è comunemente calcolato su un periodo di 14 giorni, ma può essere adattato ad altre durate in base alle esigenze dell'analista.

Nel contesto di questo script, l'RSI viene calcolato su un periodo di 14 periodi, e successivamente viene applicata una media mobile semplice (SMA) all'RSI stesso. La SMA è un tipo di media che calcola la media aritmetica dei valori dell'RSI su un determinato numero di periodi, filtrando così le fluttuazioni a breve termine e aiutando a identificare tendenze più stabili.

Il sistema di trading proposto nel codice è basato sull'osservazione di eventuali inversioni della media dell'RSI. Quando viene rilevata una deviazione significativa o una inversione di tendenza rispetto alla media, il modello attiva un segnale di acquisto per l'asset, con una durata massima dell'operazione di una settimana.

A seguito di una prima analisi, i risultati ottenuti indicavano buone possibilità di battere il benchmark. Pertanto, ho deciso di eseguire una serie di test aggiuntivi per verificare la robustezza e la validità del modello, cercando di evitare il rischio di overfitting. L'overfitting si verifica quando un modello si adatta troppo strettamente ai dati storici, compromettendo la sua capacità di generalizzare e fornire previsioni accurate su nuovi dati. Per contrastare questo fenomeno, ho prestato particolare attenzione a non rendere il modello troppo complesso, bilanciando la ricerca di performance con la necessità di mantenere una certa generalizzabilità. I test sono stati effettuati utilizzando diverse configurazioni e periodi di valutazione per confermare che i risultati fossero robusti e non frutto di un adattamento eccessivo ai dati passati.

I risultati del benchmark sono i seguenti:
Budget finale Benchmark = 375
Volatilità Benchmark = 0.02627
Sharpe Ratio Benchmark = 0.04952
VaR Benchmark = 0.04137

I test condotti invece:(budget iniziale=100)

Test #1
Parametri: RSI = 14 periodi, SMA = 14 periodi, Take Profit = 25%, Stop Loss = -10%, durata test = 15 anni (2007-2022), Benchmark = SPY (Standard & Poor's 500), Risk-Free Rate = 0.03, Alpha = 0.05, 
Risultati:
Budget finale = 298$
Volatilità Strategia = 0.03216
Sharpe Ratio Strategia = 0.04494
VaR Strategia = 0.05124

Test #2  

Parametri: RSI = 14 periodi, SMA = 14 periodi, Take Profit = 25%, Stop Loss = -5%, durata test = 15 anni (2007-2022), Benchmark = SPY (Standard & Poor's 500), Risk-Free Rate = 0.03, Alpha = 0.05, budget_iniziale=100$
Risultati:

Budget finale = 464
Volatilità Strategia = 0.02908
Sharpe Ratio Strategia = 0.06788
VaR Strategia = 0.05000

Test #4

Parametri: RSI = 14 periodi, SMA = 14 periodi, Take Profit = 25%, Stop Loss = -4%, durata test = 15 anni (2007-2022), Benchmark = SPY (Standard & Poor's 500), Risk-Free Rate = 0.03, Alpha = 0.05
Risultati:

Budget finale = 442
Volatilità Strategia = 0.02777
Sharpe Ratio Strategia = 0.06716
VaR Strategia = 0.04000

Test #3

Parametri: RSI = 14 periodi, SMA = 14 periodi, Take Profit = 25%, Stop Loss = -3%, durata test = 15 anni (2007-2022), Benchmark = SPY (Standard & Poor's 500), Risk-Free Rate = 0.03, Alpha = 0.05
Risultati:

Budget finale = 567
Volatilità Strategia = 0.02603
Sharpe Ratio Strategia = 0.08351
VaR Strategia = 0.03000

Test #4

Parametri: RSI = 10 periodi, SMA = 10 periodi, Take Profit = 25%, Stop Loss = -5%, durata test = 15 anni (2007-2022), Benchmark = SPY (Standard & Poor's 500), Risk-Free Rate = 0.03, Alpha = 0.05
Risultati:

Budget finale = 623
Volatilità Strategia = 0.02836
Sharpe Ratio Strategia = 0.08155
VaR Strategia = 0.04275

Test #5

Parametri: RSI = 5 periodi, SMA = 5 periodi, Take Profit = 25%, Stop Loss = -5%, durata test = 15 anni (2007-2022), Benchmark = SPY (Standard & Poor's 500), Risk-Free Rate = 0.03, Alpha = 0.05
Risultati:

Budget finale = 534
Volatilità Strategia = 0.02618
Sharpe Ratio Strategia = 0.07362
VaR Strategia = 0.04085




