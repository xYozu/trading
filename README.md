# Trading (questo è un esempio di alcuni script veloci che ho scritto)
In questo spazio farò analisi veloci di dati riguardanti per lo più il prezzo delle azioni delle più grandi aziende americane, l'obbiettivo è vedere se i soliti indicatori di analisi tecnica funzionano e cercare di 
utilizzarli combinati tra loro in modo tale da risultare più efficaci.
Se i risultati ottenuti da una prima andalisi sono piuttosto buoni cercherò di ottimizzarli e migliorarli nel tempo.
Come Benchmark utilizzo l'andamento dell'indice Standard & Poor 500 del periodo analizzato, tali indicatori sono i più famosi e sono presenti nella libreria python TA-lib.

1)"Analisi_RVI.py".

In "Analisi_RVI" analizzo l'indicatore Relative Volatility Index, l'RVI misura la deviazione standard dei prezzi nel tempo, ovvero è un idicatore di volatilità dei prezzi in un determinato periodo di tempo (es: 14 periodi= volatilità negli ultimi 14 giorni), se la volatilità è al rialzo siamo in una situazione di "iper-comprato", viceversa in "iper-venduto".

La strategia prevede di comprare in chiusura in una situazione di mercato di iper-venduto, ovvero con volatilità al ribasso e controllare se il giorno dopo il prezzo chiude ad un prezzo maggiore di quello acquistato (strategia reversal). Dopo vari test i risultati hanno dimostrato che con un rvi a 14 periodi si batte il mercato poche volte, inoltre non tenedo conto di altri costi che per semplicità e velocità non ho considerato, come i costi di operazione e spread bid/ask.
Tuttavia con un determinato numero di azioni e in alcuni periodi di tempo il mercato è stato battuto (qualche volta anche in maniera sostanziosa), questo mi fa pensare che potrei migliorare la strategia magari facendo una analisi macroeconomica sul perchè per un numero di azioni o per un derterminato periodo la strategia ha performato così bene, successivamente potrei calcolare i costi che dovrei affrontare e infine vedere se batterei un ETF a replica dell'S&P 500.




