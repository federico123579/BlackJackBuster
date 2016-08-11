import os
import sys
choice = 'y'
while choice == 'y':
 os.system('clear')
 card_banco = raw_input("Che carta scoperta ha il banco?\n")
 cp1 = raw_input("Quale carta hai ricevuto?\n")
 cp2 = raw_input("Quale carta hai ricevuto ora?\n")
 def ifOne(i):
     if i == 'A':
         return 11
     else:
         return eval(i)
         i = eval(i)
 tot = 0
 try:
     tot = ifOne(cp1) + ifOne(cp2)
     print(tot)
     if tot > 22:
         print("Hai sforato, mi dispiace")
 except TypeError:
     print("Ops.. Hai inserito un valore errato! Ritenta")
 try:
     card_banco + 0
 except TypeError:
     print("Ops.. Hai inserito un valore errato! Ritenta")
 os.system('clear')
 decisionaltree = [
 [1,1,1,1,1,1,1,1,1,1],
 [1,1,1,1,1,2,2,0,0,0],
 [1,1,1,1,1,2,2,2,0,2],
 [1,1,1,1,1,2,2,2,2,2],
 [2,2,1,1,1,2,2,2,2,2],
 [3,3,3,3,3,3,3,3,3,2],
 [3,3,3,3,3,3,3,3,2,2],
 [2,3,3,3,3,2,2,2,2,2],
 [2,2,2,2,2,2,2,2,2,2],
 [4,4,4,4,4,4,4,4,4,4],
 [1,1,1,1,1,1,1,1,1,1],
 [4,4,4,4,4,1,4,4,1,1],
 [4,4,4,4,4,4,4,4,4,4],
 [4,4,4,4,4,4,2,2,2,2],
 [4,4,4,4,4,2,2,2,2,2],
 [3,3,3,3,3,3,3,3,2,2],
 [2,2,2,4,4,2,2,2,2,2],
 [4,4,4,4,4,4,2,2,2,2]]
 # 0 = surrender
 # 1 = stand
 # 2 = hit
 # 3 = DoubleHit
 # 4 = Split
 def decision():
     convertionsPlayer = {21: 0, 20: 0, 19: 0, 18: 0, 17: 0, 16: 1, 15: 2, 14: 3, 13: 3, 12: 4, 11: 5, 10: 6, 9: 7, 8: 8, 7: 8, 6: 8,5: 8}
     convertionsTable = {2: 0, 3: 1, 4: 2, 5: 3, 6: 4, 7: 5, 8: 6, 9: 7, 10: 8, 11: 9}
     convertionsDouble = {22: 9, 20: 10, 18: 11, 16: 12, 14: 13, 12: 14, 10: 15, 8: 16, 6: 17, 4: 17}
     if ifOne(cp1) == ifOne(cp2) and tot == (22 or 20 or 18 or 16 or 14 or 12 or 10 or 8 or 6 or 4):
         return decisionaltree[convertionsDouble[tot]][convertionsTable[ifOne(card_banco)]]
     elif tot > 21:
         return 5
     else:
         return decisionaltree[convertionsPlayer[tot]][convertionsTable[ifOne(card_banco)]]
 statements = {0: "Arrenditi", 1: "Fermati", 2: "Chiedi Carta", 3: "Raddoppia, se non puoi, chiedi carta", 4: "Sdoppia", 5: "Sforato"}
 dec = decision()
 print statements[dec]
 while dec == 2:
     cp3 = ifOne(raw_input("Che carta hai ricevuto?\n"))
     tot += cp3
     dec = decision()
     print(tot)
     print(statements[dec])
 if dec == 3:
     cp3 = ifOne(raw_input("Che carta hai ricevuto?\n"))
     tot += cp3
     if tot > 21:
         print(statements[5]) 
 choice = raw_input("Vuoi rigiocare?(y/n)\n")

