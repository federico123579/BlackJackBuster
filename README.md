# BlackJackBuster
Un software in grado di calcolare la probabilità di vincita nel gioco del BlackJack con il machine learning grazie a studi effettuati presso università.
# Strategia
### Probabilità di sballare per il giocatore

La tabella che vedete sotto mostra le probabilità di sballare per il giocatore che decide di chiedere carta. Sballare significa che il punteggio che totalizza è superiore al 21 e che quindi perderà la mano. Due percentuali sono abbastanza evidenti: se avete meno di 12 e chiedete una carta non potrete certo sballare, perché al massimo arriverete a 21, mentre se già avete ventuno e decidete di tirare, allora sballerete sicuramente, perché 21 è il punteggio massimo consentito. 

|Valore della mano|Probabilità di sballare|
|---|---|
|meno di 12|0%|
|12|31%|
|13|39%|
|14|56%|
|15|58%|
|16|62%|
|17|69%|
|18|77%|
|19|85%|
|20|92%|
|21|100%|
### Probabilità di sballare per il mazziere
Come si può facilmente intuire, le carte peggiori per il casinò sono il 5 e il 6, mentre le migliori sono un asso o una qualsiasi carta di valore dieci. 

|Carta scoperta del banco|Probabilità di sballare per il banco|
|---|---|
|Todo|Todo|
## Base
Carte del Banco

|       | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |A |
|-------|----|----|----|----|----|----|----|----|----|----|
| **17-20** | S | S | S | S | S | S | S |  S |  S |  S |
|  **16**   | S | S | S | S | S | H | H | SU | SU | SU |
|  **15**   | S | S | S | S | S | H | H |  H | SU |  H |
| **13-14** | S | S | S | S | S | H | H |  H |  H |  H |
|  **12**   | H | H | S | S | S | H | H |  H |  H |  H |
|  **11**   | Dh | Dh | Dh | Dh | Dh | Dh | Dh | Dh | Dh |  H |
|  **10**   | Dh | Dh | Dh | Dh | Dh | Dh | Dh | Dh |  H |  H |
|   **9**   | H | Dh | Dh | Dh | Dh | H |  H |  H |  H |  H |
|  **5-8**  | H | H | H | H | H | H | H |  H |  H |  H |
### Coppie
Carte del Banco

|       | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | A |
|-------|----|----|----|----|----|----|----|----|----|----|
|  **A,A**  | SP | SP | SP | SP | SP | SP | SP | SP | SP | SP |
| **10,10** |  S |  S |  S |  S |  S |  S |  S |  S |  S |  S |
|  **9,9**  | SP | SP | SP | SP | SP |  S | SP | SP |  S |  S |
|  **8,8**  | SP | SP | SP | SP | SP | SP | SP | SP | SP | SP |
|  **7,7**  | SP | SP | SP | SP | SP | SP |  H |  H |  H |  H |
|  **6,6**  | SP | SP | SP | SP | SP |  H |  H |  H |  H |  H |
|  **5,5**  | Dh | Dh | Dh | Dh | Dh | Dh | Dh | Dh |  H |  H |
|  **4,4**  |  H |  H |  H | SP | SP |  H |  H |  H |  H |  H |
|**2,2-3,3**| SP | SP | SP | SP | SP | SP |  H |  H |  H |  H |
## Tecniche
|   | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10, J, Q, K | A |
|---|---|---|---|---|---|---|---|---|---|---|
| **Hi-Lo** | +1 | +1 | +1 | +1 | +1 | 0 | 0 | 0 | -1 | -1 |
| **Hi-Opt I** | 0 | +1 | +1 | +1 | +1 | 0 | 0 | 0 | -1 | 0 |
| **Hi-Opt II** | +1 | +1 | +2 | +2 | +1 | +1 | 0 | 0 | -2 | 0 |
| **KO** | +1 | +1 | +1 | +1 | +1 | +1 | 0 | 0 | -1 | -1 |
| **Omega II** | +1 | +1 | +2 | +2 | +2 | +1 | 0 | -1 | -2 | 0 |
| **Red 7** | +1 | +1 | +1 | +1 | +1 | +0.5 | 0 | 0 | -1 | -1 |
| **Zen Count** | +1 | +1 | +2 | +2 | +2 | +1 | 0 | 0 | -2 | -1 |
#ToDos
* Aggiungere Conteggio
