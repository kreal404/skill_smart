import logging

logging.basicConfig(filename='my_example.log', level=logging.DEBUG)

def count_words(string):
    assert isinstance(string, str), "Входной аргумент должен быть строкой"
    word_count = 0
    for i in range(len(string)):
        assert len(string.strip()) != 0, 'Количество слов в string не должно быть пустым'
        if string[i] == " ":
            word_count += 1

    word_count += 1
    return word_count

try:
    string = "Пример строки для подсчета слов"
    word_count = count_words(string)
    logging.info(f"Количество слов в строке '{string}': {word_count}")
    print("Количество слов в строке:", word_count)
except AssertionError as e:
    logging.error(str(e))
    print("Ошибка:", str(e))

logging.info("Программа завершена")