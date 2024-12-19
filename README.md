In questo spazio farò analisi veloci di dati riguardanti per lo più il prezzo delle azioni delle più grandi aziende americane. L'obiettivo è vedere se i soliti indicatori di analisi tecnica funzionano e cercare di utilizzarli combinati tra loro in modo tale da risultare più efficaci. Se i risultati ottenuti da una prima analisi sono piuttosto buoni, cercherò di ottimizzarli e migliorarli nel tempo. Come benchmark utilizzo l'andamento dell'indice Standard & Poor's 500 del periodo analizzato. Tali indicatori sono i più famosi e sono presenti nella libreria Python TA-lib.

"Analisi_RVI.py".
In "Analisi_RVI" analizzo l'indicatore Relative Volatility Index. L'RVI misura la deviazione standard dei prezzi nel tempo, ovvero è un indicatore di volatilità dei prezzi in un determinato periodo di tempo (es: 14 periodi = volatilità negli ultimi 14 giorni). Se la volatilità è al rialzo, siamo in una situazione di "iper-comprato", viceversa in "iper-venduto".

La strategia prevede di comprare in chiusura in una situazione di mercato di iper-venduto, ovvero con volatilità al ribasso, e controllare se il giorno dopo il prezzo chiude a un prezzo maggiore di quello acquistato (strategia reversal). Dopo vari test, i risultati hanno dimostrato che con un RVI a 14 periodi si batte il mercato poche volte. Inoltre, non tenendo conto di altri costi che per semplicità e velocità non ho considerato, come i costi di operazione e spread bid/ask, la strategia ha comunque mostrato dei risultati interessanti. Tuttavia, con un determinato numero di azioni e in alcuni periodi di tempo, il mercato è stato battuto (qualche volta anche in maniera sostanziosa). Questo mi fa pensare che potrei migliorare la strategia, magari facendo un'analisi macroeconomica sul perché per un numero di azioni o per un determinato periodo la strategia ha performato così bene. Successivamente, potrei calcolare i costi che dovrei affrontare e infine vedere se batterei un ETF a replica dell'S&P 500.




