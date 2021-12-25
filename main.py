"""Heitetään kolikkoa viidesti:
Klaava!
Klaava!
Klaava!
Klaava!
Klaava!"""
import random
numerot = []
print("Heitetään kolikkoa viidesti:")
while True:
    if len(numerot) == 5:
        break
    luku = random.randint(0,1)
    numerot.append(luku)
    if luku == 1:
        print("Kruuna!")
    else:
        print("Klaava!")