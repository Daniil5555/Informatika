# TODO импортировать необходимые молули
import csv  # Импортируем модуль в формате CSV
import json  # Импортируем модуль в формате JSON

INPUT_FILENAME = "input.csv"  # Файл для чтения данных
OUTPUT_FILENAME = "output.json"  # Файл для записи результата


def task() -> None:  # Пусть функция будет task без возврата
    with open(INPUT_FILENAME, "r") as file:  # Откроем файл INPUT_FILENAME на чтение в текстовом режиме с автоматическим закрытием
        reader = csv.DictReader(file)  # Пусть заголовки столбцов станут ключами, а данные в строке будут значениями
        data = list(reader)  # Переделываем в режим чтения
        # TODO считать содержимое csv файла

    with open(OUTPUT_FILENAME, "w") as f:  # Откроем файл OUTPUT_FILENAME для записи
        json.dump(data, f, ensure_ascii=False, indent=4)  # Сохраняем список в JSON с отступами в 4 пробела и с нормально отображающимися буквами
        # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:  # Откроем JSON для проверки результата
        for line in output_f:  # Переберем файл по строкам
            print(line, end="")  # Выводим результат
