In questo spazio farò analisi veloci di dati riguardanti per lo più il prezzo delle azioni delle più grandi aziende americane.
L'obiettivo è vedere se i soliti indicatori di analisi tecnica funzionano e cercare di utilizzarli combinati tra loro in modo tale da risultare più efficaci. 
Se i risultati ottenuti da una prima analisi sono piuttosto buoni, cercherò di ottimizzarli e migliorarli nel tempo.
Come benchmark utilizzo l'andamento dell'indice Standard & Poor's 500 del periodo analizzato. 
Tali indicatori sono i più famosi e sono presenti nella libreria Python TA-lib.

"Analisi_RVI.py".
In "Analisi_RVI" analizzo l'indicatore Relative Volatility Index. L'RVI misura la deviazione standard dei prezzi nel tempo, ovvero è un indicatore di volatilità dei prezzi in un determinato periodo di tempo (es: 14 periodi = volatilità negli ultimi 14 giorni). Se la volatilità è al rialzo, siamo in una situazione di "iper-comprato", viceversa in "iper-venduto".

La strategia prevede di comprare in chiusura in una situazione di mercato di iper-venduto, ovvero con volatilità al ribasso, e controllare se il giorno dopo il prezzo chiude a un prezzo maggiore di quello acquistato (strategia reversal). 
Dopo vari test, i risultati hanno dimostrato che con un RVI a 14 periodi si batte il mercato poche volte. Inoltre, non tenendo conto di altri costi che per semplicità e velocità non ho considerato, come i costi di operazione e spread bid/ask, la strategia ha comunque mostrato dei risultati interessanti. 
Tuttavia, con un determinato numero di azioni e in alcuni periodi di tempo, il mercato è stato battuto (qualche volta anche in maniera sostanziosa). Questo mi fa pensare che potrei migliorare la strategia, magari facendo un'analisi macroeconomica sul perché per un numero di azioni o per un determinato periodo la strategia ha performato così bene.
Successivamente, potrei calcolare i costi che dovrei affrontare e infine vedere se batterei un ETF a replica dell'S&P 500.

"RSI_mean_reverting.py"( NON COMPLETO )

Nel file "RSI_mean_reverting.py" viene analizzata la media dell'indicatore Relative Strength Index (RSI). L'RSI è un indicatore utilizzato per misurare la "forza" o la "debolezza" di un asset in relazione ai suoi movimenti di prezzo recenti. Esso valuta la velocità e l'intensità delle variazioni di prezzo, fornendo segnali che possono suggerire condizioni di ipercomprato o ipervenduto. In particolare, l'RSI è comunemente calcolato su un periodo di 14 giorni, ma può essere adattato ad altre durate in base alle esigenze dell'analista.

Nel contesto di questo script, l'RSI viene calcolato su un periodo, e successivamente viene applicata una media mobile semplice (SMA) all'RSI stesso. La SMA è un tipo di media che calcola la media aritmetica dei valori dell'RSI su un determinato numero di periodi, filtrando così le fluttuazioni a breve termine e aiutando a identificare tendenze più stabili.

Il sistema di trading proposto nel codice è basato sull'osservazione di eventuali inversioni della media dell'RSI. Quando viene rilevata una deviazione significativa o una inversione di tendenza rispetto alla media, il modello attiva un segnale di acquisto per l'asset, con una durata massima dell'operazione di una settimana.

A seguito di una prima analisi, i risultati ottenuti indicavano buone possibilità di battere il benchmark.
Pertanto, ho deciso di eseguire una serie di test aggiuntivi per verificare la robustezza e la validità del modello, cercando di evitare il rischio di overfitting. 

budget iniziale=100, risk_free_rate= 0.03, alpha= 0.05, inizio_test=2007, fine_test=2022, 

I risultati del benchmark sono i seguenti:
Budget finale Benchmark = 375
Volatilità Benchmark = 0.02627
Sharpe Ratio Benchmark = 0.04952
VaR Benchmark = 0.04137


Risultati test #1:(RSI=10 periodi, SMA=10 periodi, stop_loss= -10%, take_profit=25%) 
Budget finale strategia = 652
Volatilità strategia = 0.02993
Sharpe Ratio strategia = 0.08099
VaR strategia = 0.04500


Risultati test #2:(RSI=10 periodi, SMA=10 periodi, stop_loss= -5%, take_profit=25%) 
Budget finale strategia = 623
Volatilità strategia = 0.02836
Sharpe Ratio strategia = 0.08157
VaR strategia = 0.04275


Risultati test #3:(RSI=5 periodi, SMA=5 periodi, stop_loss= -10%, take_profit=25%) 
Budget finale strategia = 362
Volatilità strategia = 0.02851
Sharpe Ratio strategia = 0.05196
VaR strategia = 0.04700


Risultati test #4:(RSI=5 periodi, SMA=5 periodi, stop_loss= -5%, take_profit=25%) 
Budget finale strategia = 533
Volatilità strategia = 0.02618
Sharpe Ratio strategia = 0.07359
VaR strategia = 0.04085


Risultati test #5:(RSI=15 periodi, SMA=15 periodi, stop_loss= -5%, take_profit=25%) 
Budget finale strategia = 533
Volatilità strategia = 0.02618
Sharpe Ratio strategia = 0.07359
VaR strategia = 0.04085






