import os
import sys
os.system('clear')
card_banco = raw_input("Che carta scoperta ha il banco?\n")
cp1 = raw_input("Quale carta hai ricevuto?\n")
cp2 = raw_input("Quale carta hai ricevuto ora?\n")
def ifOne(i):
    print("Function \t .\t.\t.\t.\tOK")
    if i == 'A':
        print("If \t\t .\t.\t.\t.\tOK")
        return 11
    else:
        print("Else \t\t .\t.\t.\t.\tOK")
        return eval(i)
        i = eval(i)
tot = 0
try:
    tot = ifOne(cp1) + ifOne(cp2)
    print(tot)
    if tot > 21:
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
[3,3,3,3,3,3,3,3,3,2],
[3,3,3,3,3,3,3,3,2,2],
[2,3,3,3,3,2,2,2,2,2],
[2,2,2,2,2,2,2,2,2,2]]
# 0 = surrender
# 1 = stand
# 2 = hit
# 3 = DoubleHit
# 4 = Split
def decision():
    convertionsPlayer = {21: 0, 20: 0, 19: 0, 18: 0, 17: 0, 16: 1, 15: 2, 14: 3, 13: 3, 12: 4, 11: 5, 10: 6, 9: 7, 8: 8, 7: 8, 6: 8,5: 8}
    convertionsTable = {2: 0, 3: 1, 4: 2, 5: 3, 6: 4, 7: 5, 8: 6, 9: 7, 10: 8, 11: 9}
    return decisionaltree[convertionsPlayer[tot]][convertionsTable[ifOne(card_banco)]]
print decision()

