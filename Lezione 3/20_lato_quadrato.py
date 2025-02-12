import math
area = float(input("Inserisci l'area del quadrato: "))
lato = math.sqrt(area)
lato_arrotondato = round(lato, 1)
print("Il lato del quadrato è:", lato_arrotondato)