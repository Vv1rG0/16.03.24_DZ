import random
print("Добро пожаловать в игру - камень, ножницы, бумага,ящерица,спок!")
playerScore = 0
botScore = 0
for i in range(3):
    answer = input("Что выберешь?\n").lower()
    if answer.find("камень") != -1:
        answer = "к"
    elif answer.find("ножницы") != -1:
        answer = "н"
    elif answer.find("ящерица") != -1 or answer.find("ящерицу") != -1:
        answer = "я"
    elif answer.find("спок") != -1:
        answer = "с"
    elif answer.find("бумага") != -1 or answer.find("бумагу") != -1:
        answer = "б"
    botAnswer = random.choice(["камень", "ножницы", "бумага", "ящерица", "спок"])
    print(f"А я выберу {botAnswer}")
    botAnswer = botAnswer[0]
    print(botAnswer)
    if answer == botAnswer:
        print("Ничья!")
        print(f"Счет игрока = '{playerScore}'")
        print(f"Счет бота = '{botScore}'")
    elif (answer == "к" and botAnswer == "н") or \
         (answer == "к" and botAnswer == "я") or \
         (answer == "н" and botAnswer == "б") or \
         (answer == "н" and botAnswer == "я") or \
         (answer == "я" and botAnswer == "б") or \
         (answer == "я" and botAnswer == "с") or \
         (answer == "с" and botAnswer == "к") or \
         (answer == "с" and botAnswer == "н") or \
         (answer == "б" and botAnswer == "с") or \
         (answer == "б" and botAnswer == "к"):
        print("Ты победил!")
        playerScore += 1
        print(f"Счет игрока = '{playerScore}'")
        print(f"Счет бота = '{botScore}'")
    else:
        print("Я победил!")
        botScore += 1
        print(f"Счет игрока = '{playerScore}'")
        print(f"Счет бота = '{botScore}'")
if playerScore == botScore:
    print("Ничья по итогам трёх раундов!")
elif playerScore > botScore:
    print("Ты победил по итогам трёх раундов")
else:
    print("Я победил по итогам трёх раундов")