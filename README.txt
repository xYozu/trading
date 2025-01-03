In questo spazio farò analisi veloci di dati riguardanti per lo più il prezzo delle azioni delle più grandi aziende americane.
L'obiettivo è vedere se i soliti indicatori di analisi tecnica funzionano e cercare di utilizzarli combinati tra loro in modo tale da risultare più efficaci. 
Se i risultati ottenuti da una prima analisi sono piuttosto buoni, cercherò di ottimizzarli e migliorarli nel tempo.
Come benchmark utilizzo l'andamento dell'indice Standard & Poor's 500 del periodo analizzato. 
Tali indicatori sono i più famosi e sono presenti nella libreria Python TA-lib.

"Analisi_RVI.py".
In "Analisi_RVI" analizzo l'indicatore Relative Volatility Index. L'RVI misura la deviazione standard dei prezzi nel tempo, ovvero è un indicatore di volatilità dei prezzi in un determinato periodo di tempo (es: 14 periodi = volatilità negli ultimi 14 giorni). Se la volatilità è al rialzo, siamo in una situazione di "iper-comprato", viceversa in "iper-venduto".

La strategia prevede di comprare in chiusura in una situazione di mercato di iper-venduto, ovvero con volatilità al ribasso, e controllare se il giorno dopo il prezzo chiude a un prezzo maggiore di quello acquistato (strategia reversal). 
Dopo vari test, i risultati hanno dimostrato che con un RVI a 14 periodi si batte il mercato poche volte. Inoltre, non tenendo conto di altri costi che per semplicità e velocità non ho considerato, come i costi di operazione e spread bid/ask, la strategia ha comunque mostrato dei risultati interessanti. 

"RSI_mean_reverting.py"( NON COMPLETO )

Nel file "RSI_mean_reverting.py" viene analizzata la media dell'indicatore Relative Strength Index (RSI). L'RSI è un indicatore utilizzato per misurare la "forza" o la "debolezza" di un asset in relazione ai suoi movimenti di prezzo recenti. Esso valuta la velocità e l'intensità delle variazioni di prezzo, fornendo segnali che possono suggerire condizioni di ipercomprato o ipervenduto. In particolare, l'RSI è comunemente calcolato su un periodo di 14 giorni, ma può essere adattato ad altre durate in base alle esigenze dell'analista.

Nel contesto di questo script, l'RSI viene calcolato su un periodo, e successivamente viene applicata una media mobile semplice (SMA) all'RSI stesso. La SMA è un tipo di media che calcola la media aritmetica dei valori dell'RSI su un determinato numero di periodi, filtrando così le fluttuazioni a breve termine e aiutando a identificare tendenze più stabili.

Il sistema di trading proposto nel codice è basato sull'osservazione di eventuali inversioni della media dell'RSI. Quando viene rilevata una deviazione significativa o una inversione di tendenza rispetto alla media, il modello attiva un segnale di acquisto per l'asset, con una durata massima dell'operazione di una settimana.

A seguito di una prima analisi, i risultati ottenuti indicavano buone possibilità di battere il benchmark.
Pertanto, ho deciso di eseguire una serie di test aggiuntivi per verificare la robustezza e la validità del modello, cercando di evitare il rischio di overfitting. 

budget iniziale=100, risk_free_rate= 0.03, alpha= 0.05, inizio_test=2007, fine_test=2022, 

I risultati del benchmark(Nasdaq 100) sono i seguenti:
Budget finale Benchmark = 610
Volatilità Benchmark = 0.02860
Sharpe Ratio Benchmark = 0.05518
VaR Benchmark = 0.04456
max_drawdown_benchmark 0.51907


Esempio risultato test :(RSI=10 periodi, SMA=10 periodi, stop_loss= -25%, take_profit=25%) 
Budget finale strategia = 479
Volatilità strategia = 0.02971
Sharpe Ratio strategia = 0.05335
VaR strategia = 0.04285
Max drawdown strategia: 0.4719

Questo esempio mostra come la strategia risulta meno performante rispetto al benchmark, tuttavia mostra una riduzione del rischio che però potrebbe essere causata, ad esempio, dal fatto che i titoli esaminati sono diversi da quelli presenti nell'indice ( praticamente avrei fatto stock picking ).
Le modifiche da apportare sono alla lista delle stock, inoltre voglio modificare lo stoploss, in modo tale da ridurre ulteriormente il rischio, infatti come mostrano gli ultimi due grafici, superato il minimo del 5% quasi mai il titolo tradato ha chiuso la settimana in positivo.










