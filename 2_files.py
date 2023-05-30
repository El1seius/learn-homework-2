"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    with open('referat.txt', 'r', encoding='utf-8') as my_file:
        content = my_file.read()
        print(f'Длина строки: {len(content)}')

        num_word = content.split()
        print(f'Количество слов: метод split {len(num_word)}')

        count_word = content.count(" ") + 1
        print(f'Количество слов: метод cound {count_word}')

        swap = content.replace('.', '!')
        print(swap)

    with open('referat2.txt', 'w', encoding='utf-8') as write_swap:
        write_swap.write(swap)

if __name__ == "__main__":
    main()
