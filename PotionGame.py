import random

Health = 50

Difficulty = 1

PotionHealth = int(random.randint(25,50) / Difficulty)

Health = Health + PotionHealth

print(Health)