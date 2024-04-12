import random
i = 0
questionsList = ["Какая сегодня погода?", "Сколько тебе лет?", "Когда я буду счастлив?"]
timeList =["Плохая", "Хорошая", "50/50"]
eventList = ["10", "20", "30"]
objectList = ["Завтра", "На следующей неделе", "В следующем месяце"]
while i < 3:
 questions = input("введите свой вопрос")
 if questions in questionsList:
    if i == 0:
        time = timeList[random.randint(0, len(timeList) - 1)]
        print(time)
        i += 1
        continue
    if i == 1:
        event = eventList[random.randint(0, len(eventList) - 1)]
        print(event)
        i += 1
        continue
    if i == 2:
        object = objectList[random.randint(0, len(objectList) - 1)]
        print(object)
        i += 1
 else:
    print("Ваш вопрос не подходит!")
print("На этом вопросы всё!")