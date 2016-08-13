# BlackJackBuster
Un software in grado di calcolare la probabilità di vincita nel gioco del BlackJack con il machine learning grazie a studi effettuati presso università.
# Strategia
Secondo gli studi del MIT queste sono le scelte che statiscticamente avranno più successo di vincita
## Base
Carte del Banco

|       | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |A |
|-------|----|----|----|----|----|----|----|----|----|----|
| 17-20 | S | S | S | S | S | S | S |  S |  S |  S |
|  16   | S | S | S | S | S | H | H | SU | SU | SU |
|  15   | S | S | S | S | S | H | H |  H | SU |  H |
| 13-14 | S | S | S | S | S | H | H |  H |  H |  H |
|  12   | H | H | S | S | S | H | H |  H |  H |  H |
|  11   | Dh | Dh | Dh | Dh | Dh | Dh | Dh | Dh | Dh |  H |
|  10   | Dh | Dh | Dh | Dh | Dh | Dh | Dh | Dh |  H |  H |
|   9   | H | Dh | Dh | Dh | Dh | H |  H |  H |  H |  H |
|  5-8  | H | H | H | H | H | H | H |  H |  H |  H |
## Coppie
Carte del Banco

|       | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | A |
|-------|----|----|----|----|----|----|----|----|----|----|
|  A,A  | SP | SP | SP | SP | SP | SP | SP | SP | SP | SP |
| 10,10 |  S |  S |  S |  S |  S |  S |  S |  S |  S |  S |
|  9,9  | SP | SP | SP | SP | SP |  S | SP | SP |  S |  S |
|  8,8  | SP | SP | SP | SP | SP | SP | SP | SP | SP | SP |
|  7,7  | SP | SP | SP | SP | SP | SP |  H |  H |  H |  H |
|  6,6  | SP | SP | SP | SP | SP |  H |  H |  H |  H |  H |
|  5,5  | Dh | Dh | Dh | Dh | Dh | Dh | Dh | Dh |  H |  H |
|  4,4  |  H |  H |  H | SP | SP |  H |  H |  H |  H |  H |
|2,2-3,3| SP | SP | SP | SP | SP | SP |  H |  H |  H |  H |
#ToDos
* Aggiungere Conteggio
