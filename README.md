In questo spazio farò analisi veloci di dati riguardanti per lo più il prezzo delle azioni delle più grandi aziende americane. L'obiettivo è vedere se i soliti indicatori di analisi tecnica funzionano e cercare di utilizzarli combinati tra loro in modo tale da risultare più efficaci. Se i risultati ottenuti da una prima analisi sono piuttosto buoni, cercherò di ottimizzarli e migliorarli nel tempo. Come benchmark utilizzo l'andamento dell'indice Standard & Poor's 500 del periodo analizzato. Tali indicatori sono i più famosi e sono presenti nella libreria Python TA-lib.

"Analisi_RVI.py".
In "Analisi_RVI" analizzo l'indicatore Relative Volatility Index. L'RVI misura la deviazione standard dei prezzi nel tempo, ovvero è un indicatore di volatilità dei prezzi in un determinato periodo di tempo (es: 14 periodi = volatilità negli ultimi 14 giorni). Se la volatilità è al rialzo, siamo in una situazione di "iper-comprato", viceversa in "iper-venduto".

La strategia prevede di comprare in chiusura in una situazione di mercato di iper-venduto, ovvero con volatilità al ribasso, e controllare se il giorno dopo il prezzo chiude a un prezzo maggiore di quello acquistato (strategia reversal). 
Dopo vari test, i risultati hanno dimostrato che con un RVI a 14 periodi si batte il mercato poche volte. Inoltre, non tenendo conto di altri costi che per semplicità e velocità non ho considerato, come i costi di operazione e spread bid/ask, la strategia ha comunque mostrato dei risultati interessanti. 
Tuttavia, con un determinato numero di azioni e in alcuni periodi di tempo, il mercato è stato battuto (qualche volta anche in maniera sostanziosa). Questo mi fa pensare che potrei migliorare la strategia, magari facendo un'analisi macroeconomica sul perché per un numero di azioni o per un determinato periodo la strategia ha performato così bene.
Successivamente, potrei calcolare i costi che dovrei affrontare e infine vedere se batterei un ETF a replica dell'S&P 500.

"RSI_mean_reverting.py"
Nel file "RSI_mean_reverting.py" viene analizzata la media dell'indicatore Relative Strength Index (RSI). L'RSI è un indicatore utilizzato per misurare la "forza" o la "debolezza" di un asset in relazione ai suoi movimenti di prezzo recenti. Esso valuta la velocità e l'intensità delle variazioni di prezzo, fornendo segnali che possono suggerire condizioni di ipercomprato o ipervenduto. In particolare, l'RSI è comunemente calcolato su un periodo di 14 giorni, ma può essere adattato ad altre durate in base alle esigenze dell'analista.
Nel contesto di questo script, l'RSI viene calcolato su un periodo di 14 periodi, e successivamente viene applicata una media mobile semplice (SMA) all'RSI stesso. La SMA è un tipo di media che calcola la media aritmetica dei valori dell'RSI su un determinato numero di periodi, filtrando così le fluttuazioni di breve termine e aiutando a identificare tendenze più stabili.
Il sistema di trading proposto nel codice è basato sull'osservazione di eventuali inversioni della media dell'RSI. Quando viene rilevata una deviazione significativa o una inversione di tendenza rispetto alla media, il modello attiva un segnale di acquisto per l'asset, con una durata massima dell'operazione di una settimana. 
A seguito di una prima analisi, i risultati ottenuti indicavano buone possibilità di battere il benchmark. Pertanto, ho deciso di eseguire una serie di test aggiuntivi per verificare la robustezza e la validità del modello, cercando di evitare il rischio di overfitting. L'overfitting si verifica quando un modello si adatta troppo strettamente ai dati storici, compromettendo la sua capacità di generalizzare e fornire previsioni accurate su nuovi dati. Per contrastare questo fenomeno, ho prestato particolare attenzione a non rendere il modello troppo complesso, bilanciando la ricerca di performance con la necessità di mantenere una certa generalizzabilità. I test sono stati effettuati utilizzando diverse configurazioni e periodi di valutazione per confermare che i risultati fossero robusti e non frutto di un adattamento eccessivo ai dati passati.


Test #1
Paramentri: RSI= 14 periodi, SMA= 14 periodi, Take_profit= 25%, Stop_loss= -25%, durata test= 15 anni (2007-2022), Benchmark= SPY(Standard & Poor 500), risk_free_rte=0.03, alpha=0.05
Risultati: Budget_finale= 238$, Budget_finale_Benchmark=375$, volatilità_benchmark= 0.02627, volatilità_strategia= 0.03439, sharpe_rateo_benchmark= 0.04952, sharpe_rateo_strategia= 0.03521, 
VaR_benchmark= 0.04137, VaR_strategia: 0.05160

Test #2
Paramentri: RSI= 14 periodi, SMA= 14 periodi, Take_profit= 25%, Stop_loss= -10%, durata test= 15 anni (2007-2022), Benchmark= SPY(Standard & Poor 500), risk_free_rte=0.03, alpha=0.05
Risultati: Budget_finale= 298$, Budget_finale_Benchmark=375$, volatilità_benchmark= 0.02627, volatilità_strategia= 0.03216, sharpe_rateo_benchmark= 0.04952, sharpe_rateo_strategia= 0.04494, 
VaR_benchmark= 0.04137, VaR_strategia: 0.05124

Test #3
Paramentri: RSI= 14 periodi, SMA= 14 periodi, Take_profit= 25%, Stop_loss= -5%, durata test= 15 anni (2007-2022), Benchmark= SPY(Standard & Poor 500), risk_free_rte=0.03, alpha=0.05
Risultati: Budget_finale= 464$, Budget_finale_Benchmark=375$, volatilità_benchmark= 0.02627, volatilità_strategia= 0.02908, sharpe_rateo_benchmark= 0.04952, sharpe_rateo_strategia= 0.06788, 
VaR_benchmark= 0.04137, VaR_strategia: 0.05000

Test #4
Paramentri: RSI= 14 periodi, SMA= 14 periodi, Take_profit= 25%, Stop_loss= -4%, durata test= 15 anni (2007-2022), Benchmark= SPY(Standard & Poor 500), risk_free_rte=0.03, alpha=0.05
Risultati: Budget_finale= 442$, Budget_finale_Benchmark=375$, volatilità_benchmark= 0.02627, volatilità_strategia= 0.02777, sharpe_rateo_benchmark= 0.04952, sharpe_rateo_strategia=  0.06716, 
VaR_benchmark= 0.04137, VaR_strategia: 0.04000

Test #5
Paramentri: RSI= 14 periodi, SMA= 14 periodi, Take_profit= 25%, Stop_loss= -3%, durata test= 15 anni (2007-2022), Benchmark= SPY(Standard & Poor 500), risk_free_rte=0.03, alpha=0.05
Risultati: Budget_finale= 567$, Budget_finale_Benchmark=375$, volatilità_benchmark= 0.02627, volatilità_strategia= 0.02603, sharpe_rateo_benchmark= 0.04952, sharpe_rateo_strategia=  0.08351, 
VaR_benchmark= 0.04137, VaR_strategia: 0.03000



