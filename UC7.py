import random

botNumber = random.randint(1, 10)
playerNumber = int(input("Введите число: "))

MAX = max(botNumber, playerNumber)
MIN = min(botNumber, playerNumber)

while playerNumber != botNumber:

    if playerNumber > botNumber:
        MAX = playerNumber
    else:
        MIN = playerNumber

    if abs(MAX - MIN) == 1 or abs(MAX - MIN) == 2:
        print("Горячо")
    else:
        print("Холодно")

    playerNumber = int(input("Введите число: "))

print(f"Ты угадал число! {botNumber}")