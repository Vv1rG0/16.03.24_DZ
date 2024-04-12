def find(text, word):
    text1 = text.lower()
    word1 = word.lower()
    
    position = text1.find(word1)
    if position != -1:
        print(f"Слово '{word}' найдено в тексте на позиции {position}.")
    else:
        print(f"Слово '{word}' не найдено в тексте.")

text = input("Введите текст: ")
word = input("Введите слово для поиска: ")

find(text, word)