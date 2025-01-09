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

budget iniziale=100, risk_free_rate= 0.03, alpha= 0.95, inizio_test=2006, fine_test=2022

I risultati del benchmark(Nasdaq 100) sono i seguenti:

Budget finale Benchmark = 630
Volatilità Benchmark = 0.02824
Sharpe Ratio Benchmark = 0.52806
VaR Benchmark = -0.04257
Max drawdown benchmark= -0.51907
Expected shortfall benchmark: -0.06158

Esempio risultato test :(RSI=10 periodi, SMA=10 periodi, stop_loss= -25%, take_profit=25%) 

Budget finale strategia = 1810
Volatilità strategia = 0.03240
Sharpe Ratio strategia = 0.67133
VaR strategia = -0.04996
Max drawdown strategia: -0.52238
Expected shortfall strategia: -0.07424

Questo esempio evidenzia come la strategia abbia ottenuto performances superiori rispetto al benchmark, ma è probabile che ciò dipenda dal fatto che i titoli analizzati sono cresciuti costantemente dal 2006 ad oggi, e difficilmente sarebbero stati selezionati per la strategia sin dal 2006, poiché non possedevano una qualità tale da giustificarne l'inclusione all'epoca. Inoltre come è possibile notare la strategia presenta un rischio più elevato anche se leggermente "giustificato" dallo Sharpe.

Infatti, mi è bastato restringere il periodo del test per mostrare come i risultati precedenti siano frutto, molto probabilmente, di uno "stock picking". Ecco i nuovi risultati:

budget iniziale=100, risk_free_rate= 0.03, alpha= 0.95, inizio_test=2012, fine_test=2022

I risultati del benchmark(Nasdaq 100):

Budget finale Benchmark = 464
Volatilità Benchmark = 0.02582
Sharpe Ratio Benchmark = 0.74979
VaR Benchmark = -0.04086
Max drawdown benchmark= -0.35486
Expected shortfall benchmark: -0.06042

Risultato test :(RSI=10 periodi, SMA=10 periodi, stop_loss= -25%, take_profit=25%)

Budget finale strategia = 298
Volatilità strategia = 0.02513
Sharpe Ratio strategia = 0.58199
VaR strategia = -0.04256
Max drawdown strategia: -0.42737
Expected shortfall strategia: -0.06246

Questi risultati mostrano come l'indice batta la strategia praticamente in tutto.

Tuttavia, a seguito di alcune analisi, ho riscontrato che è possibile ridurre il rischio della strategia, sia modificando l'indicatore che regolando lo stop loss, mantenendo comunque un livello di rumore accettabile. Attualmente, il codice esamina parzialmente questo aspetto, ma provvederò a aggiornarlo.








