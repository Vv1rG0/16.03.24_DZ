import random
def randompass(length):
    password = ''
    for _ in range(length):
        password += str(random.randint(0, 9))
    return password
if __name__ == '__main__':
    length = int(input("Введите длину пароля: "))
    password = randompass(length)
    print(f"Сгенерированный пароль: {password}")